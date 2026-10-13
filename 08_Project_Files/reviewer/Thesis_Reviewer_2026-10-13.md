# Thesis Reviewer: Essential Points

Built from the Google Doc "Thesis TODOs" (read 2026-10-13) and project decisions. Where the doc and earlier decisions differ, the doc wins and the gap is listed at the end.

## 1. The thesis in one breath

Hojaji et al. (2026) used a genetic algorithm (GA) to generate an "idealized" lap of driver-input KPIs, but their fitness function scores every microsector on its own and adds the times up. In a real lap, the speed you leave one microsector with is the speed you enter the next one with. This thesis replaces only the fitness function with a **chained XGBoost surrogate**: it predicts each microsector's time and exit speed from its KPIs and its entry speed, and passes that exit speed on as the next entry speed. Everything else in the GA stays the same, so any difference in the result comes from the fitness function.

**Sole contribution:** a coupled (microsector-chained), learned fitness function for evolutionary optimization of human driver inputs, tested by ablation against an otherwise identical uncoupled version.

## 2. Key terms (say these correctly)

| Term | Meaning |
|---|---|
| Microsector | One corner or one straight. Never call it a "sector" (a sector is a larger timing section spanning several microsectors). Hojaji calls it "sector" (2026) or "segment" (2024). |
| Control KPI | A driver input measure (brake duration, trail-braking duration, peak steering...). These are the only GA genes. |
| State / outcome variables | Entry, apex, exit speed and microsector time. They result from inputs, so they are never genes. |
| Surrogate | A model that stands in for the real evaluator (actually driving the lap in ACC). |
| Coupling / chaining | v_entry,n+1 = v_exit,n inside the fitness function. |

## 3. Problem and research gap

- Most racing optimization research targets **autonomous agents** (RL, trajectory optimization, racing lines). Little work optimizes **human driver inputs**.
- Hojaji et al. (2023, 2024) showed telemetry KPIs predict driver skill. Hojaji et al. (2026) moved to optimization with a GA.
- **Gap 1 (stated by Hojaji 2026):** feature importance was computed globally, not per microsector, because they lacked data.
- **Gap 2 (follows from their fitness equation):** each microsector's time depends only on its own KPIs; no speed carries over between microsectors. Penalties limit unrealistic values and sudden jumps but carry no state.
- The two gaps are linked: to rank KPIs per microsector you must predict its time and exit speed, which both depend on entry speed. So per-microsector feature selection falls out of the chained surrogate.
- **Why coaching systems (Bae et al., 2025) don't need coupling:** a real driver executes their advice and the simulator's physics enforces the coupling. An optimized lap exists only inside the fitness model, so the model itself must carry it. Don't call Bae's approach flawed.
- **What we do NOT claim as novel:** the physical coupling itself, chaining surrogates (used in manufacturing, e.g. Geiger et al., 2023), per-segment ML time models, or diagnosing carried-over speed. The novelty is the combination: a learned, chained surrogate as the GA fitness for human driver KPIs, plus measuring its effect by ablation.

## 4. The baseline: Hojaji et al. (2026)

- ACC, McLaren 720S GT3, **Laguna Seca**, 20 microsectors, 10 KPIs each, 135 drivers, 865 laps after cleaning.
- GA: population 120, 200 generations, two-point crossover 0.8, Gaussian mutation rate 0.15 (sigma 0.05), elitism of 2, tournament size 3.
- Fitness = T + λ·P, λ = 0.1.
- Their "surrogate" is **not a trained model**. It is a hand-written formula: a fast-lap baseline time per microsector, scaled by how far the KPIs deviate from the midpoint (0.5) of their scaled range, clamped to 90–105% of baseline. Their XGBoost/RF/SVM were classifiers used only for feature importance.
- So this thesis's chained XGBoost is the **first learned surrogate** in this line of work.
- Their optimized lap (~81–82 s) was 4–5 s faster than the fastest human lap, but was never driven in the simulator. It is physically unverified (not proven impossible).

## 5. Data

- **Main dataset (train + test):** Hojaji et al. (2024), CHB Reports 14:100414, supplementary material, CC BY 4.0. ACC, McLaren 720S GT3, **Brands Hatch**, Oct 2022–Jan 2023, all drivers on the same setup.
  - Raw: 826 laps, 166 drivers. **After cleaning: 817 laps, 165 drivers.** 1–8 laps per driver (median 5).
  - Already divided into **M = 19 microsectors** (9 corners, 10 straights; start/finish straight split into start and end parts).
  - Per microsector: time, 7 summary stats per channel, and 8 ready-made driver-input KPIs.
- **External test set (own laps):** drivers recruited from various locations drive the same car/track in ACC v1.10.4 on their own rigs. Software/settings fixed via instruction sheet + setup file; hardware recorded via a 25-question driver form (Appendix 1); minimum is wheel + pedals. Same MoTeC workspace so the same 19 microsectors and KPIs come out. **Never used for training, feature selection or tuning.** It tests whether the surrogate carries over to new drivers, a newer ACC version and different hardware.
- **Why switch to Brands Hatch:** the 2024 dataset is public and segment-level; the comparison is between two fitness variants on the same data, so it does not need the baseline's track.

## 6. Method steps

| Step | What happens | Key detail to remember |
|---|---|---|
| 0. Setup | Settings for the external test set | ACC v1.10.4, MoTeC i2 Pro, McLaren default setup, ABS 5, TC 5, 26 °C, 12:00, dynamic weather off |
| 1. Preprocessing | Remove in/out/invalid laps, then |z| > 3 lap-time outliers across all laps (not per driver: too few laps per driver) | 70/30 split **by driver**; all microsectors of a lap stay together |
| | Control KPI pool | 8 dataset KPIs + driver-input channel stats (max/mean brake and throttle, full-throttle share, steering stats, reversal rate, lowest gear). Car-response channels excluded |
| 2. Clustering | K-Means on lap time only; k by Elbow + Silhouette | Fastest cluster = Fast reference |
| 3. Feature selection | Pearson filter, then XGBoost/RF importance per microsector against its own time and exit speed, with entry speed as covariate | Normalize + average the two importances, average across microsectors, keep **top K = 10** common to all microsectors (K matches Hojaji). SHAP reported per microsector |
| 4. Surrogate | One multi-output XGBoost shared by all microsectors | f_ML: (s_n, v_entry,n, n) → (Δt_n, v_exit,n). Trained on **all** training laps, not Fast laps only |
| | Validation | 10-fold CV grouped by driver; MAE and R² on test set overall and on Fast-cluster laps; **lap rollout** (chain predictions through the whole lap and compare with recorded lap time and boundary speeds); then once on the external test set |
| 5. GA | Hojaji's GA unchanged | 190 genes (19 × 10); random init within training-lap KPI ranges; v_entry,1 fixed at mean fast-lap entry speed; **no 90–105% clamp**; lap closure not enforced (gap reported) |
| Output | Optimized per-microsector KPI targets | Compared with the Fast-cluster median and phrased as coaching ("microsector 7: hold trail braking 0.2 s longer") |

## 7. Evaluation (the ablation)

- Two fitness variants, same GA, same selected KPIs, same penalty:
  1. **Coupled:** v_entry,n+1 = predicted v_exit,n.
  2. **Independent:** each microsector's entry speed fixed at its mean fast-lap entry speed.
- **30 paired seeds** (same seeds for both variants).
- **Common judge:** every run's best lap is re-scored by the chained surrogate, whose trustworthiness comes from the rollout test. The gap between the independent variant's own predicted time and its chained time shows how much independent scoring overstates the gain.
- **Wilcoxon signed-rank test** on paired differences; a difference counts only if it is larger than the rollout lap-time error.
- Dropped: comparison against Hojaji's EA lap (different track, no code), DE vs GA (future work).

## 8. Scope and limitations

- **No claim that ACC telemetry equals real-car telemetry.** The context is sim racing as an esport; all comparisons are inside ACC, same car and track. Evidence that simulator skill partly reflects real skill is supporting only (lit review 2.2).
- Validity is question-specific (Himmels et al., 2023): absolute vs relative validity both compare with real driving, which this thesis does not do.
- KPI **reliability** (consistency across a driver's laps) is checked separately; low-consistency KPIs are reported.
- Mixed hardware in the external test set (force feedback can change lap time: Murphy et al., 2026; field of view affects perceived speed).
- Older ACC version in the main dataset vs v1.10.4 for own laps.
- Optimized laps are not driven in the simulator; the surrogate is the judge.
- The common judge is the coupled variant's own model, which could favour it (rollout error threshold is the safeguard).
- Lap closure not enforced; one track, one car.
- Full replication of Hojaji is out of scope (no code released).

## 9. Likely panel questions with short answers

1. **What exactly is new?** A learned, chained surrogate as the GA fitness for human driver KPIs, and an ablation that measures what coupling changes. The GA is held fixed so the fitness is the only variable.
2. **Why not just improve the GA (DE, CMA-ES)?** Changing the optimizer would mix two effects. Holding it fixed isolates the fitness function. Optimizer comparison is future work.
3. **Why XGBoost?** It works well on tabular data, handles nonlinear interactions, supports multi-output regression, is fast enough to call 19 times per individual across 120 × 200 evaluations, and Hojaji already used it, so it is consistent with the line of work.
4. **Why is entry speed not a gene?** It is a result of the previous microsector's inputs. Letting the GA set it would let it "teleport" speed. Only v_entry,1 is set, and it is fixed so the GA can't exploit a faster start.
5. **How do you know the surrogate is accurate enough?** Grouped CV, held-out test MAE/R², the lap rollout (errors accumulate when chained, so this is the strict test), and the external test set.
6. **Isn't it unfair to judge both variants with the chained model?** It is the only evaluator available without driving the laps. It is validated independently by the rollout, and differences only count if larger than its rollout error. This is stated as a limitation.
7. **Why drop the 90–105% clamp?** The clamp bounded Hojaji's hand-written formula. The learned surrogate replaces that formula, and both variants are treated the same.
8. **Why split by driver?** So the model is tested on drivers it never saw; otherwise a driver's style leaks into the test set.
9. **Why K = 10?** To match Hojaji et al. (2026).
10. **Why Brands Hatch and not Laguna Seca?** The 2024 dataset is public, already segmented and licensed for reuse. The ablation compares two variants on the same data, so it does not need the baseline's track.
11. **Why record your own laps if you have the dataset?** As an external test of whether the surrogate generalizes to new drivers, a newer ACC version and different hardware. They are never used for training.
12. **Does this help real racing drivers?** Not claimed. Results apply to competitive sim racing in ACC.
13. **What if coupling makes no difference?** That is still a result: it would show independent scoring is adequate for this setup. The Wilcoxon test and rollout threshold tell us either way.
14. **How is the result useful to a driver?** Each optimized KPI target is compared with the Fast-cluster median and turned into a per-microsector coaching instruction.
15. **Why cluster by lap time only?** It follows Hojaji et al. (2024); the Fast cluster is just a reference for entry speeds and coaching comparisons.

## 10. Mismatches to fix in the doc before presenting

These are in the main tab, which you said you'd refine later; flagging only so the panel doesn't catch them first.

- **Problem statement** says "sector level" and "circuit segments"; the thesis term is microsector.
- **Objective 2** says "corner interdependencies" and "sequential track sectors"; should be microsectors (corners and straights).
- **Objective 3** says "validating the generated racing lines against human baseline telemetry". The thesis optimizes driver-input KPIs, not racing lines, and the human-lap comparison was dropped. It should describe the coupled vs independent ablation and the Fast-cluster comparison.
- **Step 2 objective** ("validate the synthetic laps against real human telemetry") has no matching step defining how that validation is done.
- Open placeholders in the methodology tab: number of drivers/laps, ACC version and upload location for the external set, reliability statistic, MoTeC appendix.
- Step 1's outlier filter repeats the "Slice each lap into M = 19" sentence from the Microsectors bullet.
