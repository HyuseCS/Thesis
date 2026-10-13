# Review of the methodology draft

Source: the live Google Doc "Thesis TODOs" (https://docs.google.com/document/d/1CGnMtbTdSsbwPcrbIO2r6esDijB4x9-Oth6HXV78cJ0), "refined methodology" and "main" tabs. Last re-checked 2026-09-26 at about 03:25 UTC, and the whole doc was read, through to "…penalty term and random seeds." (the new "literature review" tab is still empty).
First version reviewed: `methodology/Thesis_TODOs_methodology_v1.md` (the original upload).
Baseline checked against: Hojaji, Toth & Campbell (2026), ICAART, full text at https://www.scitepress.org/Papers/2026/146096/146096.pdf

**Status key:** ✅ resolved · 🟡 partly addressed · 🔴 open · ⚪ no longer applies

**Decisions already made (2026-09-25 and 2026-09-26):**
- "Microsector" means a single corner or straight. Hojaji et al. call these "sectors"; "sector" is reserved for official timing sectors.
- Hojaji's GA is kept unchanged: population 120, 200 generations, tournament selection of size 3, two-point crossover 0.8, Gaussian mutation 0.15 (σ 0.05), elitism 2, random initialization within min–max ranges, and λ = 0.1.
- The contribution is the chained (coupled) surrogate fitness. It is tested against a microsector-independent variant on the same GA. DE, and DE vs GA, are out of scope.
- Only **control KPIs** (driver inputs) are feature-selection candidates and GA genes. Entry, exit and apex speed and microsector time are state or outcome variables.
- The control-KPI list in Step 1 is intentionally open ("…") and K may change if fewer than 10 control KPIs are available.
- **Data split (Step 1):** valid laps are split 70/30 into training and test sets, by driver where enough drivers are available and otherwise by lap. The test set is used only for the final surrogate test.
- Step 3 ranks the control KPIs of microsector n against its own Δt_n and v_exit,n, with v_entry,n as a covariate, on the **training laps**. Importances for the two targets are normalized and averaged, then averaged across microsectors. The top K = 10 KPIs (matching Hojaji et al., 2026) are common to all microsectors. Per-microsector SHAP importances are also reported.
- **Surrogate (Step 4):** trained on the training laps of all clusters. 10-fold cross-validation on the training data is grouped by the same unit as the split. MAE and R² are reported on the test set overall and on its Fast-cluster laps.
- **GA inputs (Step 5):** genes are initialized within the ranges observed in the training laps. v_entry,1 is not a gene; it is fixed at the mean fast-lap entry speed so that improvements come from driver inputs rather than a faster start. The baseline's 90–105% clamp is not applied, in either fitness variant.

---

## A. Problems that would draw examiner objections

### A1. Claim that independent evaluation produces unphysical laps ✅
The "Microsector Interdependency" section now:
- cites Kapania et al. (2016), Lenzo & Rossi (2020), Veneri & Massaro (2020) and Garlick & Bradley (2021) for the physics, all checked against their full text;
- describes Hojaji's fitness accurately (each microsector scaled from its own KPIs, then summed, plus a penalty term);
- answers the transition-penalty objection;
- frames the flaw as an argument and names the test (coupled vs independent fitness).

Remaining: the section heading still reads "Structural Limitations of Independent **Sector** Evaluation…" (see C13).

### A2. The baseline's safeguards are described only partly ✅
"The Baseline Approach" now describes all three penalty types (sudden changes between consecutive microsectors, large gradients within a microsector, values beyond physical thresholds) and the 90–105% clamp on each adjusted microsector time, citing Hojaji et al. (2026). "The Microsector Interdependency" now argues that the penalties and the clamp limit how far a candidate can depart from realistic values and how much one microsector can gain, but do not model how the exit state of microsector n affects microsector n+1.

### A3. Step 3 and Step 4 target different things ✅
Step 3 now ranks the control KPIs of microsector n against Δt_n and v_exit,n, with v_entry,n as a covariate, which is exactly what Step 4's surrogate predicts. It also states how the two targets and the per-microsector rankings are combined, fixes K = 10 with a reason, uses the training laps, and keeps per-microsector SHAP importance to answer the problem statement's microsector-level gap.

### A4. Entry, exit and apex speed are listed as KPIs but are also chained state ✅
Step 1 now separates **control KPIs** (the only feature-selection candidates and GA genes) from **state and outcome variables**, and gives each state variable its role: exit speed and time are predicted, entry speed is passed on from the previous microsector, and apex speed is descriptive only. a_lat,peak is no longer an output in Step 4. s_n is now defined in Step 4.

### A5. Surrogate trained on Fast laps only, but asked about the whole KPI range ✅
Now resolved:
- Step 1 splits the valid laps 70/30 before any modelling, by driver where possible and otherwise by lap, and keeps the test set for the final surrogate test only.
- Steps 3 and 4 both use the training laps of all clusters, so feature selection and the surrogate see the same data.
- Step 4 cross-validates on the training data, grouped by the same unit as the split, and reports test MAE and R² overall and on the Fast-cluster laps, where the GA will search.
- Step 5 initializes genes within the training-lap ranges, so the GA starts where the surrogate has data.

Optional:
- In Step 1, after "otherwise by lap", add "(a limitation, since one driver's laps may then appear in both sets)".
- Gaussian mutation can still move genes slightly outside the training range. Reporting how often this happens would show that the surrogate was rarely asked to extrapolate.

---

## B. Technical soundness

### B1. Friction-circle penalty and the unused a_lat output ✅
Step 5 uses Hojaji's penalty term P unchanged, and Step 4 no longer predicts a_lat,peak, so nothing is left unused. If you later want a combined-grip check, add it to *both* fitness variants (for example sqrt(a_lat² + a_long²) ≤ a_limit from Fast-lap data).

### B2. Error accumulates along the chain ✅
Step 4 now uses grouped cross-validation and rolls each test lap out through the chained surrogate, comparing predicted and recorded lap time and boundary speeds.

### B3. Lap closure ✅
Step 5 states that lap closure is not enforced, treats it as a simplification, and reports the gap for each optimized lap.

### B4. Physics wording ✅
"Momentum transfer" is gone; Step 4's Validation now says it measures how accurately the surrogate predicts each microsector's time and the exit speed passed on to the next.

### B5. GA settings ✅
Step 5 states all of Hojaji's GA settings, including tournament selection of size 3, and their random initialization. The number of runs is tracked under B6.

### B6. Fair comparison ✅
The Proposed Solution now states 30 paired seeds per variant, scoring the best lap of every run with the chained surrogate as a common judge (validated by the rollout test), the overstatement gap of the independent variant, and a Wilcoxon signed-rank test with the rollout lap-time error as the smallest meaningful difference.

Remaining note: state as a limitation that the common judge is the proposed model itself. Hojaji's published lap times are not compared directly, since data and KPI sets differ.

### B7. Turning targets into coaching ✅
Step 5's Output now reports each target against the Fast-cluster median and phrases the difference as a coaching instruction, with an example.

### B8. Is the 90–105% clamp part of your fitness? ✅
Step 5 now states: "The 90–105% clamp of the baseline is not applied, because the surrogate replaces the time model it bounded; both fitness variants are treated the same way."

Why drop it: XGBoost predictions stay close to the training range, so the 90% floor adds little; with all laps in training, the 105% ceiling would bind often in early generations and give many candidates identical times. Near the optimum it probably rarely binds, so the choice is low-stakes. Optional evidence at no extra cost: log how often the clamp *would* have bound during the runs.

---

## C. Internal consistency and wording

| # | Location | Issue | Status | Suggested fix |
|---|---|---|---|---|
| C1 | Step 2 | k chosen by Elbow and Silhouette; Fast cluster is the reference whatever k is. | ✅ | Done. |
| C2 | Step 2 | Lap time alone is clustered, following Hojaji et al. (2024). | ✅ | Done. Add the CHB Reports paper to Zotero (see D). |
| C3 | Step 1 | Outlier filter now names lap time, per driver. | ✅ | Done. |
| C4 | Step 1 | M = 20 with distance-based boundaries, following Hojaji's layout. | ✅ | Done. Revisit if the track is not Laguna Seca. |
| C5 | Step 1 | Title now "Sequential Preprocessing and Microsector Segmentation". | ✅ | Done. |
| C6 | Step 4 | Now one multi-output XGBoost regressor. | ✅ | Done. |
| C7 | Step 4 | One surrogate shared by all microsectors, with the microsector index as input. | ✅ | Done. |
| C8 | Step 5 | Chromosome length stated (M × K = 200). | ✅ | Done. |
| C9 | Diagram | Seeding a sub-optimal lap. | ⚪ | Seeding dropped. |
| C10 | Throughout | M = 20 stated in Step 1. | ✅ | Done. |
| C11 | Main tab | "Hojaji et. al." (should be "et al."). | 🟡 | Two occurrences remain in Related Literature Notes; the first is inside a Zotero citation, so fix it in Zotero. |
| C12 | Step 1 | Data source details. | 🔴 | Covered by E3. |
| C13 | Main tab | Methodology tab and section heading now use "microsector". Main tab still has "sector-level", "sector level", "circuit segments" and "micro-sector" (Objective 1). | 🟡 | Replacements are in `Section_C_fixes.md`; Objectives 2 and 3 go with E2. |
| C14 | Step 2 | Literal asterisks removed. | ✅ | Done. |
| C15 | Step 4 | s_n undefined. | ✅ | Now "where s_n is the selected control KPIs of microsector n". |
| C16 | Step 4 | Symbol now f_ML. | ✅ | Done. |

---

## D. Citation check

| Claim in doc | Cited | Verdict |
|---|---|---|
| Baseline GA: 20 microsectors, two-point crossover, Gaussian mutation, elitism 2, tournament size 3 | Hojaji 2026 | **Correct.** |
| Baseline fitness: linear adjustment from a neutral midpoint, summed, plus penalty | Hojaji 2026 | **Correct.** |
| Baseline penalty types (transitions, within-microsector gradients, physical thresholds) and the 90–105% clamp | Hojaji 2026 | **Correct.** Matches the paper's wording. |
| K = 10 for consistency with the baseline | Hojaji 2026 | **Correct.** Their chromosome uses 10 KPIs per sector. |
| Speed at a point is bounded by neighbouring sections; forward/backward integration | Kapania 2016; Lenzo & Rossi 2020; Veneri & Massaro 2020 | **Supported.** Checked against the full texts. |
| Racing-line models improve with preceding and upcoming geometry | Garlick & Bradley 2021 | **Supported.** Section 2.2. |
| Unphysical lines / "physically impossible" | (removed) | ⚪ Removed from the doc. |
| DE efficiency | (removed) | ⚪ DE dropped. |
| Global vs sector-level feature importance | Hojaji 2026 (Problem statement) | **Correct**, and it's your strongest link to the baseline. |
| Clustering rationale (Step 2) | Hojaji et al. (2024) | **Now cited in the doc.** Hojaji et al. (2024), *Computers in Human Behavior Reports* ([open access](https://www.sciencedirect.com/science/article/pii/S2451958824000472)), used lap-time K-Means with Elbow and Silhouette to compare skill levels. It isn't in Thesis.bib yet. |

---

## E. Links to the main tab and adviser comments

### E1. Objective 3's validation step 🟡
Step 2 says the clusters are used "to validate the synthetic laps generated against real human telemetry", which gives stratification a purpose. Step 4 now validates the *surrogate* against real laps, but no step yet says how the *optimized laps* are validated.

**Fix:** add it to Step 5 or a short Step 6. For each microsector, compare each optimized KPI with the Fast cluster's distribution (for example its percentile or z-score, and whether it falls inside the observed range). Report this for both fitness variants.

### E2. "Racing lines" vs KPIs 🔴
Objectives 2 and 3 still say "racing lines", "optimal speed-tradeoffs across sequential track sectors" and "sector-importance model". The method outputs per-microsector KPI targets and uses a chained surrogate. Align the objectives with the method, for example: "…develop a chained surrogate model that predicts microsector time and exit speed from driver KPIs and entry speed…", "…validate the optimized microsector targets against human telemetry".

### E3. Open adviser comment: data collection and simulator reliability 🟡 (in progress)
The adviser asks how the dataset will be collected, how reliable simulator data is, and for a detailed discussion. A draft section built from verified sources is being prepared (data collection protocol mirroring Hojaji et al. 2026: ACC v1.9, McLaren 720S GT3, Laguna Seca, identical setups and fixed track conditions, Playseat cockpit with Logitech wheel and pedals, MoTeC i2 Pro at 50 Hz with 74 channels; reliability evidence; threats to validity and mitigations). Undecided details (number of drivers, hardware) will be placeholders.

### E4. Dataset size 🔴
The problem statement notes that sector-level estimation "would require larger datasets". State the expected number of drivers and laps, and therefore microsector rows. The number of drivers also decides whether Step 1 can split by driver or has to fall back to splitting by lap, and it supports one global surrogate (C7).

### E5. Open adviser comment: baseline vs proposed diagram 🟡 (ready to insert)
Updated diagram: `methodology/diagrams/Frameworks_Baseline_vs_Proposed.png` (insert under "Methodology Diagram") and the editable `.drawio`. Blue marks the contributions (microsector-level feature selection, chained surrogate, coupled fitness), yellow the unchanged GA, green the evaluation additions (split, ablation), grey what matches the baseline. The baseline column was checked against Hojaji et al. (2026). Mark ✅ once it is in the doc.

---


## Shortest path from here
1. **E5:** insert the diagram PNG under "Methodology Diagram".
2. **E3:** add the data collection and reliability section once the draft is ready.
3. **E1:** say how the optimized laps are validated against the Fast cluster (the Output's comparison with the Fast-cluster median is a start).
4. **E2, C13, C11:** align the objectives and main-tab wording with the method.
5. **E4:** state the expected number of drivers and laps.
6. **D:** add Hojaji et al. (2024, CHB Reports) to Zotero and disambiguate the two 2024 papers (2024a/2024b).
