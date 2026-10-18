# Refined methodology, revised 2026-10-17

Paste-ready revision of the "refined methodology" tab, from "Data Collection and Simulator Reliability" through Step 5. Citations are typed as (Author, year). Where a sentence is unchanged from the doc, keep the doc's existing Zotero citation instead of pasting over it. The change list at the end says exactly which sentences changed.

---

## Data Collection and Simulator Reliability

This thesis uses two datasets: a main dataset from Hojaji et al. (2024), used to build and test the method, and an external test set recorded for this thesis, used only to check whether the trained surrogate holds for new drivers, a newer version of the simulator and different hardware.

**Main dataset (Hojaji et al., 2024).** The main dataset is the segment-specific behavioural dataset published as supplementary material with Hojaji et al. (2024) under a Creative Commons CC BY 4.0 licence (the article states that "the main datasets have been included as supplementary files"; the channels and metrics are described in its Tables A1 and A2). It holds 826 laps from 166 drivers in Assetto Corsa Competizione (ACC), all driving the McLaren 720S GT3 at Brands Hatch, recorded between October 2022 and January 2023. In that study all drivers used the same track, vehicle setup and game setup (Hojaji et al., 2024). Each lap is already divided into 19 microsectors (9 corners and 10 straights, with the start/finish straight split into its start and end parts). For each microsector the dataset gives its time, seven summary statistics (minimum, maximum, mean, start, end, change and standard deviation) for each telemetry channel, and eight driver-input KPIs: brake length, brake duration, trail-braking duration, throttle duration, throttle application speed, throttle release, peak steering value and time to peak steering. Because the speed at the start of each microsector equals the speed at the end of the previous one, entry and exit speeds can be read directly. Drivers contributed between 1 and 8 laps each (median 5).

**External test set (recorded for this thesis).** To test the surrogate outside the data it was built on, 5 recruited drivers each record 100 laps of the McLaren 720S GT3 at Brands Hatch in ACC v1.10.4 on their own rigs at home. The software and in-game settings in Step 0 are fixed and sent to every driver as an instruction sheet with the car setup file; the hardware is not fixed, so each driver reports it on a short form (Appendix 1). The minimum requirement is a steering wheel with pedals. Telemetry is exported with ACC's built-in MoTeC logging (Vasilakos, 2019) and processed with the same MoTeC i2 Pro workspace, maths channels and export settings as the main dataset, so that the same 19 microsectors and the same KPIs are produced. Drivers upload the raw MoTeC files (.ld and .ldx) and the form to a shared Google Drive folder.

These laps are never used for training, feature selection or tuning. Because they differ from the main dataset in simulator version, hardware and drivers, they show how far the surrogate's accuracy carries over to new conditions. Hardware is recorded because force-feedback settings can change lap time and some steering measures (Murphy et al., 2026) and a limited field of view can affect perceived speed (Kemeny & Panerai, 2003).

### Simulator Validity and Scope

A simulator should not be labelled "valid" or "invalid" as a whole. Its validity depends on the research question and the variables measured (Himmels et al., 2023). Absolute and relative validity both describe how a simulator compares with real driving, and this study makes no such comparison. It does not claim that ACC telemetry is equivalent to real-car telemetry. Its context is sim racing as an esport: the drivers, laps, fast reference and optimized targets all exist inside ACC, and every comparison is made between laps recorded in the same simulator with the same car and track. The results are therefore stated for competitive sim racing in ACC, not for professional real-world racing. The wider evidence on simulator validity, including studies suggesting that simulator measures partly reflect real driving skill, is reviewed in Chapter 2 (Section 2.2).

**Consistency of the measurements.** Separately from validity, the study checks how consistent each control KPI is across a driver's recorded laps, measured as the coefficient of variation of that KPI in each microsector, averaged over drivers with at least two valid laps. KPIs with low consistency are reported as a limitation.

## Step 0: Setup and Settings

These settings apply to the external test set. The main dataset (Hojaji et al., 2024) was recorded by its authors with one shared car setup and game setup.

- **Hardware:** Drivers use their own rigs. The minimum requirement is a steering wheel with pedals; each driver's hardware is recorded on the driver form (Appendix 1).
- **Software:** Assetto Corsa Competizione v1.10.4 (racing simulator), MoTeC i2 Pro 1.1 (telemetry analysis).
- **Simulation settings:**
  - **Car:** McLaren 720S GT3, default setup, sent to drivers as the setup file.
  - **Track:** Brands Hatch.
  - **Assists:** ABS 5, traction control 5, stability control off, auto clutch on.
  - **Track conditions:** clear weather, fixed grip state, fixed track temperature (26 °C), fixed time of day 12:00 PM, dynamic weather off.
  - **Session:** practice session, soft tyres, 20 L of fuel, fuel consumption rate 0x.

## Step 1: Sequential Preprocessing and Microsector Segmentation

- **Input:** Segment-level telemetry of Hojaji et al. (2024), with each lap already divided into microsectors, plus the external test laps exported with the same MoTeC workspace and settings.
- **Microsectors:** Each lap is divided into M = 19 ordered microsectors (9 corners and 10 straights, with the start/finish straight split into its start and end parts), following the segmentation of Hojaji et al. (2024), with boundaries fixed by track distance so that every lap is divided at the same points.
- **Lap filter:** Remove in-laps, out-laps, standing starts and invalid laps, including laps whose recorded lap time does not match the sum of their microsector times. Then remove outlier laps whose lap time lies more than three standard deviations from the mean of all laps (|z| > 3). The filter is applied to the main dataset and, separately, to the external test laps. The final numbers of drivers and laps are reported after filtering.
- **Split:** Valid laps of the main dataset are split 70/30 into training and test sets by driver, so no driver appears in both. The test set is used only for the final surrogate test. The external test laps are kept apart and never used for training, feature selection or tuning.
- **Control KPIs:** Control KPIs are driver inputs only. The candidates are the eight KPIs computed in the dataset (brake length, brake duration, trail-braking duration, throttle duration, throttle application speed, throttle release, peak steering value and time to peak steering) plus summary statistics of the driver-input channels for each microsector: maximum and mean brake, maximum and mean throttle, share of the microsector at full throttle, maximum, mean and standard deviation of the absolute steering angle, steering reversal rate, and lowest gear. Channels that describe the car's response rather than the driver's input (speed, accelerations, lane deviation, understeer and oversteer, ABS and traction control activity) are excluded. Step 3 selects the top K = 10 from this pool.

## Step 2: Performance Stratification (Clustering)

- **Process:** Apply K-Means clustering to the lap times of all valid laps of the main dataset, with the number of clusters k chosen by the Elbow Method and Silhouette Coefficient, to label laps by skill tier (Fast, Medium and Slow if k = 3). The fastest cluster serves as the Fast reference whatever the value of k. Following Hojaji et al. (2024), lap time alone is clustered. Only lap time is used, so labelling the test laps passes no KPI information into training.
- **Objective:** To define the Fast reference used later: the Fast-cluster test laps on which the surrogate is evaluated (Step 4), and the fast-lap entry speeds and KPI medians used by the GA and its output (Step 5). Fast-lap values used in Step 5 are taken from training laps only.

## Step 3: Microsector-Level Feature Selection

- **Process:** Using the training laps, candidate KPIs whose Pearson correlation is weak (|r| < 0.1; Cohen, 1988) with both Δt_n and v_exit,n are removed. A single XGBoost model is then fitted on all training laps, with the remaining candidate KPIs, the microsector index n and the entry speed v_entry,n as inputs, and Δt_n and v_exit,n as outputs. KPI importance is measured as the mean absolute SHAP value, computed with TreeSHAP (Lundberg et al., 2020) and grouped by microsector. For each microsector, the importances for each target are normalized to sum to 1 and the two targets are averaged. These values are then averaged across microsectors, and the top K = 10 KPIs, common to all microsectors, form the GA genes. The per-microsector importances are also reported. This model is used only for ranking; the surrogate is trained in Step 4.
- **Objective:** Identify the K = 10 control KPIs (to be consistent with Hojaji et al., 2026) that best predict each microsector's time Δt_n and exit speed v_exit,n given its entry speed v_entry,n, instead of ranking KPIs against global lap time, and report which KPIs matter most in each microsector.

## Step 4: Interdependency Surrogate Modeling

- **Process:** Train a single multi-output XGBoost regressor, shared by all microsectors, on the training laps. Its inputs are the K control KPIs selected in Step 3, the entry speed v_entry,n and the microsector index n, and its outputs are Δt_n and v_exit,n.
- **Mapping:** f_ML: (s_n, v_entry,n, n) → (Δt_n, v_exit,n), where s_n is the selected control KPIs of microsector n.
- **Validation:** Hyperparameters are tuned by grid search inside 10-fold cross-validation grouped by driver on the training laps, scored by Mean Absolute Error (MAE). The model is then refit on all training laps with the best hyperparameters. MAE and R² measure how accurately the surrogate predicts each microsector's time and the exit speed passed on to the next, and are reported on the test set overall and on its Fast-cluster laps. Each test lap is also rolled out through the chained surrogate: starting from its recorded entry speed at microsector 1, the predicted exit speed of each microsector is used as the entry speed of the next, and the predicted lap time and boundary speeds are compared with the recorded ones. The surrogate is then evaluated once on the external test set (MAE, R² and lap rollout), to check how well it carries over to new drivers, a newer version of ACC and different hardware.

## Step 5: Genetic Algorithm Optimization with a Coupled Fitness Function

- **Process:** The evolutionary search reuses the genetic algorithm (GA) of Hojaji et al. (2026) without modification, so that the fitness function is the only component that differs from the baseline. The population of 120 individuals evolves for 200 generations using two-point crossover (probability 0.8) and Gaussian mutation (rate 0.15, standard deviation 0.05), with elitism by preserving the two best individuals in each generation and tournament selection with a size of three (Hojaji et al., 2026).
- **Initialization:** Each chromosome holds the K = 10 selected control KPIs for each of the M microsectors, giving M × K genes (190 for M = 19 and K = 10). Each gene is initialized randomly within the min–max scaled range of that KPI observed in the training laps.
- **Fitness evaluation:** Each individual is scored as Fitness = T + λ·P, with λ = 0.1 and the penalty term P of Hojaji et al. (2026). Instead of scaling a baseline time for each microsector independently, the candidate's KPIs are decoded to their original units and passed through the Step 4 surrogate one microsector at a time. The first microsector's entry speed is set to the mean entry speed of the Fast-cluster training laps and is fixed, so that improvements come from driver inputs rather than a faster start. The predicted exit speed of each microsector n becomes the entry speed of microsector n+1 (v_entry,n+1 = v_exit,n). T is the sum of the predicted microsector times Δt_n. The 90–105% clamp of the baseline is not applied, because the surrogate replaces the time model it bounded; both fitness variants of the comparison below are treated the same way. Lap closure is not enforced: the last microsector's predicted exit speed is not required to match the fixed entry speed of the first. This is treated as a simplification, and the gap is reported for each optimized lap.
- **Output:** Optimized per-microsector targets for the selected control KPIs. Each target is reported against the median of that KPI in that microsector over the Fast-cluster training laps, and the difference is phrased as a coaching instruction, for example "microsector 7: hold trail braking 0.2 s longer than the fast-lap median".

---

## Change list (what to edit in the doc)

1. **External test set:** "in Latest ACC version" → "in ACC v1.10.4". "The software and in-game settings are fixed" → "The software and in-game settings in Step 0 are fixed". "to a set out google drive for uniformity" → "to a shared Google Drive folder".
2. **Main dataset:** "826 laps (817 after cleaning) from 166 drivers" → "826 laps from 166 drivers". The 817 count came from removing only corrupted laps and standing starts, before the |z| filter, so it is not the final count. Step 1 now reports the final count.
3. **Consistency of the measurements:** "how consistent each KPI is across a driver's recorded laps, using overall laptimes" → the coefficient-of-variation sentence above.
4. **Step 0:** "default setup" → "default setup, sent to drivers as the setup file" (the data section says a setup file is sent). Session line rewritten in full words.
5. **Step 1:** "Outlier filter" renamed "Lap filter". It now names standing starts and lap-time mismatches (the cleaning already done on the data), says it runs separately on the external laps, and drops the duplicate "Slice each lap into M = 19…" sentence. "so that every lap is divided at the same points" moved into the Microsectors line.
6. **Step 2:** now says all valid laps of the main dataset are clustered. The Objective is replaced: Step 2 defines the Fast reference, it does not validate laps.
7. **Step 3:** adds the Pearson threshold and says it is computed on the training laps, adds "the remaining candidate KPIs" to the inputs (the doc omits them), says each target is normalized before the two are averaged, and says this model is for ranking only. The Objective no longer says "in microsector n", because the K KPIs are common to all microsectors.
8. **Step 4:** adds MAE as the CV score, the refit on all training laps and "at microsector 1" for the rollout start.
9. **Step 5:** fast-lap entry speed and medians come from the Fast-cluster training laps. The clamp sentence moved after the chaining description, and "both fitness variants" now points to the comparison section below.

## Review log

- **Pass 1** (doc as of 2026-10-17 05:23 UTC): 5 inconsistencies (Step 3 inputs, Step 2 objective, Step 2 clustering scope, Step 1 duplicate slicing, KPI consistency measure) plus the missing Step 4 refit.
- **Pass 2** (draft 1 of this file): 4 more found and fixed: the 817 lap count clashing with the Step 1 |z| filter, the setup file vs "default setup" in Step 0, the external laps having no filter, and Step 5 fast-lap values with no data source.
- **Pass 3** (this file): no inconsistencies left within the data section and Steps 0 to 5.

Not changed, because they are design choices rather than inconsistencies: the external set size of 5 drivers × 100 laps (my recommendation in the thread was at least 30 drivers × 5 laps), and the |r| < 0.1 threshold, which is my recommendation and has not been confirmed. The "Structural Limitations" section was checked against Step 5. Its independent variant uses "the mean entry speed of fast laps at each microsector". To match Step 5, that should read "of the Fast-cluster training laps".
