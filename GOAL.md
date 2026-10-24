# GOAL — Thesis Anchor

> Title: *Extending an ML-EA Framework with a Microsector-Chained Surrogate Model for Sim Racing Performance Optimization* (Google Doc "Thesis TODOs", tab "for consultation #2")
>
> This file is the anchor. Every note, experiment, and chapter in this vault must trace back to a numbered goal below. If a task does not serve G1–G4, it is out of scope.
>
> **Status: v0.5 — synced with the Google Doc (2026-10-24).** Supersedes v0.4. v0.5 adopts the Doc title and the method details listed in §7. Simulator, data, microsector count, model, optimizer and evaluation design are fixed (§6). v0.4 adds the lap filter, the external test set size, the Pearson + TreeSHAP feature selection and the surrogate tuning (§7). The v0.2 gates are kept, struck through, in §8. The Google Doc "Thesis TODOs" is the source of truth for written thesis text, but only its tabs "refined methodology", "literature review" and "for consultation #2"; ignore the other tabs. This file must not contradict them.

**Terminology.** A *microsector* is one individual corner or straight. A *sector* is a larger track portion spanning several microsectors. Use "microsector" for the unit of analysis throughout.

---

## 0. Origin

The original base document is `01_Corpus/thesis new base.md` (2026-09-11). Its problem statement framed the gap as global vs sector-level feature importance. Reading Hojaji et al. (2026) in full narrowed that gap (see Problem statement below and [[Hojaji2026_TelemetryEA]]).

**Literature position.** Most sim-racing optimization work targets autonomous racing agents; integrated optimization frameworks for *human* drivers are comparatively rare (Hojaji et al. 2026; Kabzan et al. 2019; Lee et al. 2025). Trajectory optimization, RL control, and racing-line generation are framed as autonomous control problems (Evans, Engelbrecht, and Jordaan 2023; Garlick and Bradley 2021; Ghignone, Baumann, and Magno 2022; Samak, Samak, and Kandhasamy 2021). Those approaches give limited insight for improving *human* performance (Hojaji et al. 2026).

**The lineage this thesis extends.**

| Work | What it did | Status in vault |
| :--- | :--- | :--- |
| Hojaji, Toth, Campbell 2023 | ML on human sim-racing telemetry: k-means performance levels, XGBoost classification, 10-feature ranking | Ingested — [[Hojaji2023_TelemetryML]] |
| Hojaji et al. 2024a (GALA) | Driving-behaviour metrics from 93 lab participants, FAST/SLOW comparison | Ingested — [[Hojaji2024_DrivingBehaviour]] |
| Hojaji et al. 2024b (*Computers in Human Behavior Reports* 14:100414) | Brands Hatch segment-level dataset (ACC, McLaren 720S GT3); **this thesis's training and test data** (CC BY 4.0) | Not yet ingested |
| Hojaji, Toth, Campbell 2026 (ICAART) | GA over per-microsector KPI vectors; fitness is a hand-written scaling formula, not a trained model; XGBoost/RF/SVM used only for feature importance | Ingested — [[Hojaji2026_TelemetryEA]] |

**Problem statement.** In Hojaji et al. (2026), each microsector's time is scaled independently from a fast-lap baseline; microsectors interact only through a smoothness penalty. Their optimized lap exists only inside that fitness model, so no real driver carries speed from one microsector to the next. The fitness itself must carry that coupling, and nothing in this line of work does.

**Novelty statement** (see `08_Project_Files/research-gap/Research_Gap_Assessment.md`):
> To our knowledge, this is the first work to replace a microsector-independent fitness with a learned, microsector-chained surrogate that propagates boundary speed from human telemetry, and to optimize driver KPIs through it, evaluated by ablation against the independent formulation.

Not new on their own, and not claimed: speed coupling between track sections (lap-time simulation), chained surrogate + evolutionary optimizer as a general method (manufacturing, UQ), per-segment ML models of segment time.

---

## 1. Goal Statement

**Train a learned, microsector-chained surrogate on human telemetry (Hojaji et al. 2024b, Brands Hatch), use it as the fitness function of Hojaji et al.'s (2026) genetic algorithm unchanged, and show by ablation whether the coupled fitness changes the optimized lap compared with a microsector-independent fitness.**

The coupled fitness is the only change from the baseline and the sole contribution. Each gate is a gate: **G(n+1) must not start until G(n) passes its exit criteria.**

---

### G1 — Dataset

*Objective 1 (refinement pending in the Google Doc): prepare a microsector telemetry dataset from existing sim racing telemetry (Hojaji et al. 2024b), extended with an external test set recorded in the same simulator.*

Settled:
- Source: Hojaji et al. 2024b supplementary data, `01_Corpus/data collection setup/segment level data behaviour.csv` (166 drivers, 826 laps). ACC, McLaren 720S GT3, Brands Hatch, recorded Oct 2022 – Jan 2023.
- Cleaned file: `01_Corpus/data collection setup/segment_level_cleaned.csv` — **817 laps, 165 drivers, M = 19 microsectors** per lap. "Str 0-1(End)" unified to "Str 0-1 (End)"; driver D_045 dropped (all laps had lap-time mismatches); Lap 1 standing starts of P_001, P_010, P_052, P_062 dropped; D_058 Lap 3 kept.
- Lap filter: remove in/out-laps, standing starts, invalid laps and lap-time mismatches, then laps with |z| > 3 on lap time across all laps (drivers have only 1–8 laps, median 5), not per driver. Applied to the main dataset and, separately, to the external laps. The 817 count is **before** the |z| filter; final counts are reported after filtering.
- Split: valid laps 70/30 train/test **by driver**; all microsectors of a lap stay together. 10-fold CV on the training set, grouped the same way. Step 2 clusters all valid laps of the main dataset on lap time only (K-Means, k by Elbow method and Silhouette coefficient); the fastest cluster is the Fast reference whatever k is. Fast-lap values used by the GA come from training laps only.
- Microsector boundaries are fixed by track distance, so every lap is divided at the same points.
- Measurement consistency: for each control KPI, the coefficient of variation in each microsector, averaged over drivers with at least two valid laps. KPIs with low consistency are reported as a limitation.
- External test set: our own remotely collected laps (Brands Hatch, ACC v1.10.4, drivers' own rigs, instruction sheet and car setup file, driver form for hardware in Appendix 1; raw MoTeC .ld/.ldx files uploaded to a shared Google Drive folder). **10 drivers × 30 clean timed laps.** **Never used for training, feature selection or tuning.** Mixed hardware and the small driver count are stated limitations.

Exit criteria:
- **G1.1** Cleaning documented with before/after counts (done for the main dataset up to the |z| filter; counts after the |z| filter still to report).
- **G1.2** Each lap is an ordered sequence of 19 microsector records with entry and exit speed.
- **G1.3** External test set collected, cleaned with the same rules (lap filter applied separately), and its size reported.
- **G1.4** Pipeline runs from committed scripts in `07_Code/`.

---

### G2 — Model: the microsector-chained surrogate

*Objective 2 (refinement pending): develop a chained surrogate model that predicts each microsector's time and exit speed from the driver's control KPIs and the entry speed carried over from the previous microsector.*

Settled:
- **Variables.** Control KPIs (driver inputs) are the only feature-selection candidates and the only GA genes. Entry/apex/exit speed and microsector time are state/outcome variables. v_entry,1 is fixed to the mean entry speed of the Fast-cluster training laps at microsector 1.
- **Candidate pool.** The 8 ready-made driver-input KPIs in the dataset (brake length, brake duration, trail-braking duration, throttle duration, throttle application speed, throttle release, peak steering value, time to peak steering) plus per-microsector driver-input statistics: max and mean brake, max and mean throttle, share of the microsector at full throttle, max, mean and SD of the absolute steering angle, steering reversal rate, lowest gear. Car-response channels (speed, accelerations, lane deviation, understeer and oversteer, ABS and TC activity) are excluded.
- **Feature selection** (training laps only). Drop candidate KPIs with Pearson |r| < 0.1 (Cohen, 1988) with both microsector time and exit speed. Fit one screening XGBoost (default hyperparameters, no CV) on all training laps with the remaining KPIs, entry speed and microsector index as inputs. Rank by mean |SHAP| (TreeSHAP) per microsector; normalize per microsector per target, average the two targets, average across microsectors; keep the top **K = 10**, common to all microsectors. RF, SVM and gain importance are not used. The same SHAP values give the per-microsector importance table. The screening model is for ranking only.
- **Surrogate.** One multi-output XGBoost shared by all microsectors, inputs = the 10 KPIs + entry speed + microsector index, outputs = microsector time and exit speed; v_exit of microsector n feeds v_entry of n+1. Trained on all valid training laps (not Fast laps only). Tuned by grid search in driver-grouped 10-fold CV (MAE), then refit on all training laps.
- **Per-microsector importance is descriptive.** The thesis does not claim to fix Hojaji et al.'s (2026) data limitation: the Brands Hatch data (817 laps) is about the size of their Laguna Seca data (865 laps). Per-microsector importances are reported with bootstrap rank stability (`08_Project_Files/reviewer/Thesis_Reviewer_2026-10-13.md`, Q16).

Exit criteria:
- **G2.1** Grouped 10-fold CV results reported with spread.
- **G2.2** Final test on held-out drivers: MAE and R² overall and on Fast-cluster laps.
- **G2.3** Lap rollout on test laps, starting from each lap's recorded entry speed at microsector 1: chained prediction of lap time vs actual, with the rollout error reported (it sets the threshold in G4).
- **G2.4** External test set scored the same way, per driver and pooled.
- **G2.5** Importance is not causality: no causal wording without support.
- **G2.6** Per-microsector importance table reported with bootstrap rank stability.

---

### G3 — Optimize: Hojaji's GA with the chained fitness

*Objective 3, part 1 (refinement pending): optimize lap time by using the chained surrogate as the fitness function of a genetic algorithm.*

Settled — Hojaji et al. (2026) settings and initialization, unchanged:
- Population 120, 200 generations, two-point crossover 0.8, Gaussian mutation rate 0.15 with sigma 0.05, elitism of the two best individuals, tournament size 3, lambda 0.1 (not tuned), random initialization within the observed KPI ranges of the training laps. Mutated genes are clipped to the training range of each KPI.
- The penalty P is rebuilt from Hojaji et al.'s (2026) description, because its formulas and thresholds are not reported.
- The best fitness per generation is reported, to show that it levels off before generation 200.
- Genome: 19 microsectors × 10 KPIs = **190 genes**.
- Fitness = chained lap time + lambda × penalty.
- Hojaji's 90–105 % microsector-time clamp is **not** used.
- Output: per-microsector KPI targets, each reported against the median of that KPI in that microsector over the Fast-cluster training laps and phrased as a coaching instruction (e.g. "microsector 7: hold trail braking 0.2 s longer than the fast-lap median").
- Lap closure is not enforced; the gap between the last microsector's exit speed and the fixed v_entry,1 is reported per optimized lap (`Methodology_Revised_2026-10-17.md`, Step 5).
- Differential evolution is dropped (future work). No optimizer-comparison arms.

Exit criteria:
- **G3.1** Both fitness variants run with paired seeds.
- **G3.2** Cost reported: runs, wall-clock time, hardware.

---

### G4 — Evaluate: ablation and validation

*Objective 3, part 2 (refinement pending): validate the optimized microsector KPI targets against human telemetry from the fastest drivers.*

Settled:
- **Ablation.** Coupled (chained) fitness vs microsector-independent fitness (entry speed = mean entry speed of the Fast-cluster training laps at each microsector). Both variants use the same selected KPIs, penalty term and 30 random seeds, shared so that runs are paired.
- **Common judge.** Both variants' best laps are re-scored by the one chained surrogate, validated by the lap rollout on test laps. The gap between the independent variant's own predicted lap time and its chained lap time shows how much independent evaluation overstates the gain.
- **Statistics.** Paired seeds, Wilcoxon signed-rank test. A difference counts only if it is larger than the rollout error (G2.3).
- The human-lap vs Hojaji EA lap comparison is **dropped**.

Exit criteria:
- **G4.1** Ablation result reported with the test statistic and effect size.
- **G4.2** Optimized KPI targets compared with the Fast cluster's distribution per microsector (percentile or z-score; inside the observed range or not), for both variants.
- **G4.3** Limitation stated: the common judge is the proposed surrogate itself, and Hojaji's published lap times are not compared directly.
- **G4.4** Coaching read-out: which microsectors carry the difference between variants.

---

## 2. Success Criteria

| ID | Claim to be earned | Measured by | Threshold |
| :--- | :--- | :--- | :--- |
| S1 | Clean, reproducible microsector dataset | laps, drivers, microsectors, cleaning counts | counts before (817 laps / 165 drivers) and after the \|z\| filter reported, M = 19; scripts committed |
| S2 | The chained surrogate predicts held-out laps | MAE, R², lap rollout error on test drivers | reported overall and on Fast-cluster laps |
| S3 | The surrogate holds on independent laps | same metrics on the external test set | reported per driver and pooled, with hardware and driver-count caveats |
| S4 | Coupling changes the optimized lap | paired ablation, Wilcoxon | difference larger than rollout error, or the negative result reported |
| S5 | Optimized targets are plausible for humans | position within the Fast cluster's distribution per microsector | reported for both variants |

---

## 3. Non-Goals

- Building an autonomous racing agent or a real-time controller.
- Porting or optimizing SCR, SL, or any MPC planner (Related Literature only, [[Scheffe2022_SCR]]).
- Comparing optimizers (DE, CMA-ES, etc.) — future work.
- Full replication of Hojaji et al. (2026) — no code was released.
- Claiming simulator telemetry equals real-world telemetry. The context is competitive sim racing as an esport; evidence that simulator measures reflect real skill is supporting only.
- Driving the optimized lap with a human, or comparing it with Hojaji's published EA lap time.
- Multiple tracks or cars.
- Opponents, traffic, strategy, tyre wear, fuel.

---

## 4. Standing Risks

| # | Risk | Hits | Mitigation |
| :--- | :--- | :--- | :--- |
| R1 | Rollout error accumulates across 19 chained microsectors | G2.3, G4 | Report rollout error; differences smaller than it do not count. |
| R2 | The GA exploits surrogate errors outside the data | G3, G4.2 | Initialization within observed KPI ranges; G4.2 range check. |
| R3 | Few laps per driver (1–8) | G1, G2 | Split and CV grouped by driver; filter across all laps. |
| R4 | Mixed hardware and only 10 drivers in the external test set | G1.3, G2.4 | Driver form records hardware; per-driver results; stated limitation. |
| R5 | Common judge is the proposed model | G4 | Stated limitation (G4.3). |
| R6 | Data from an older ACC version than the external test set | G2.4 | Stated limitation. |
| R7 | Per-microsector importance unstable at this data size | G2.6 | Reported as descriptive with bootstrap rank stability; GA genes use the top 10 averaged across microsectors. |

---

## 5. Working Directives

Inherited from [[AGENTS]]:

1. **Zero hallucination.** Every number carries a source.
2. **Report the cost.** Dataset size, model, hyperparameters, hardware, runtime.
3. **Gates are gates.**
4. **Report what happened**, including negative results.

---

## 6. Decisions

All v0.2 open decisions are resolved:

- [x] Simulator: Assetto Corsa Competizione (main data from an older version; external test set on v1.10.4)
- [x] Telemetry source: Hojaji et al. 2024b dataset for training/testing; own laps as external test set only
- [x] Car and circuit: McLaren 720S GT3, Brands Hatch
- [x] Microsectors: M = 19 (the dataset's segments)
- [x] Model: one microsector-chained XGBoost surrogate; top K = 10 control KPIs by Pearson screen + TreeSHAP
- [x] Evolutionary algorithm: Hojaji et al. (2026) GA, settings unchanged
- [x] Evaluation: coupled vs independent fitness ablation, common judge, Wilcoxon
- [ ] Hardware for every reported runtime — record when experiments run

Still open (tracked in `08_Project_Files/todos/`): Objective wording (none of the three Doc tabs we use states the objectives yet), the driver instruction sheet, and the common-judge limitation in the methodology text. The driver form is done (Doc, Appendix 1).

---

## 7. Revision Log

Changes are **recorded**, not silently applied. Bump the version, add a row, never delete a superseded goal (strike it through in §8).

| Version | Date | Changed | Reason | Source |
| :--- | :--- | :--- | :--- | :--- |
| v0.1 | 2026-08-26 | Initial draft: G1 port SCR to C++ → G2 validate → G3 Assetto Corsa → G4 novelty | First formalization from [[Scheffe2022_SCR]] | Student |
| v0.2 | 2026-09-11 | **Full rebase.** Topic changed from porting SCR to micro-sector telemetry ML + evolutionary lap optimization for human drivers. | New base document `01_Corpus/thesis new base.md` | Student |
| v0.3 | 2026-10-13 | **Decisions settled.** Gap narrowed from sector-level vs global importance to a learned microsector-chained fitness. Data switched to Hojaji et al. 2024b (817 laps, 165 drivers, M = 19); own laps external test only. GA unchanged; clamp and DE dropped. Three-arm ablation replaced by coupled vs independent fitness; human-baseline lap comparison dropped. All gates G1–G4 and S1–S5 replaced; v0.2 gates struck through in §8. | Methodology decisions 2026-09-25 to 2026-10-03, recorded in the Google Doc "Thesis TODOs" | Student |
| v0.4 | 2026-10-18 | **Methods detailed.** Lap filter defined (\|z\| > 3 across all laps, separate for external laps; 817 is pre-filter, S1 changed). External test set fixed at 10 drivers × 30 laps, kept out of feature selection and tuning, reported per driver. Feature selection = Pearson \|r\| < 0.1 screen + TreeSHAP; RF/SVM/gain dropped. Surrogate is one shared XGBoost (KPIs + entry speed + microsector index), grid-searched in grouped CV. Per-microsector importance descriptive (G2.6, R7). Lap closure not enforced, gap reported. | Commit `16c45ff`: AGENTS.md §0 (2026-10-18), `08_Project_Files/methodology/Methodology_Revised_2026-10-17.md`, reviewer note Q16 | Student |
| v0.5 | 2026-10-24 | **Synced with the Google Doc.** Title set to the Doc title. Added from the Doc: K-Means with Elbow + Silhouette and Fast reference = fastest cluster; microsector boundaries by track distance; KPI consistency check (CV); full candidate KPI pool and excluded car-response channels; fast-lap entry speeds and medians taken from Fast-cluster training laps; elitism 2, tournament 3, gene clipping, P rebuilt from description, convergence reported; output as coaching targets vs Fast-cluster median; 30 paired seeds; overstatement gap of the independent variant. | Google Doc "Thesis TODOs" (tabs "refined methodology", "for consultation #2"), snapshot `08_Project_Files/Thesis_TODOs_Doc_2026-10-24.md` | Student |

---

## 8. Superseded Gates

### v0.2 (micro-sector importance) — superseded 2026-10-13

- ~~**G1 — Dataset:** record our own micro-sector telemetry dataset; simulator, car, circuit and micro-sector rule undecided.~~
- ~~**G2 — Model:** sector-level feature importance vs a global importance model (G2.3), learning curve for data sufficiency (G2.4), interdependency effect size.~~
- ~~**G3 — Optimize:** three-arm ablation: EA + sector importance, EA + global importance, EA alone.~~
- ~~**G4 — Validate:** optimized lap time vs a human baseline lap and its lap-to-lap spread.~~

Reason dropped: the global-vs-sector-importance gap was narrowed after reading Hojaji et al. (2026) in full; the dataset question was answered by the Hojaji et al. 2024b release; see v0.3 in §7.

### v0.1 (SCR port) — superseded 2026-09-11

Kept for history. **None of this is in scope.** [[Scheffe2022_SCR]] remains a valid source note and a Related Literature entry.

- ~~**G1 — Port:** reimplement the SCR trajectory planner in real-time C++, replacing MATLAB and CPLEX; median solve time ≤ 73 ms with a free QP solver.~~
- ~~**G2 — Validate:** prove the C++ port is the published algorithm; zero track-constraint violations, recursive feasibility, SL baseline in the same codebase.~~
- ~~**G3 — Deploy:** drive a car in Assetto Corsa under SCR control; state read, control write, track polygon extraction, vehicle system identification, closed-loop lap.~~
- ~~**G4 — Extend:** add parameters to SCR that improve lap time against SL and against unmodified SCR without breaking the feasibility guarantee of `Thm. 2`.~~

Reason dropped: the thesis was rebased on `01_Corpus/thesis new base.md` (2026-09-11), which targets human driver performance, not autonomous trajectory planning.
