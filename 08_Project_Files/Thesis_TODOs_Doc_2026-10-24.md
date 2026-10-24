# Thesis TODOs — Google Doc snapshot, 2026-10-24

Verbatim export of the team Google Doc "Thesis TODOs" (https://docs.google.com/document/d/1CGnMtbTdSsbwPcrbIO2r6esDijB4x9-Oth6HXV78cJ0/edit), last modified 2026-10-24T11:51Z. Each `#` heading below with no bold is a Doc tab. The Doc is the source of truth; this copy goes stale as soon as the Doc changes.

---

# deprecated 2  

  - **\*\*Introduce a Framework\*\***

  

**Related Literature Notes:**

  - Most of the research on sim-racing optimization is set to target on autonomous racing agents, with relatively less work on integrated optimization frameworks for human drivers [(Hojaji et. al. 2026; Kabzan et al. 2019; Lee et al. 2025)](https://www.zotero.org/google-docs/?EI8dmN). 
  - Trajectory optimization, RL control, and racing-line generation are framed as autonomous control problems in F1TENTH, TORCS, and full-size racecars [(Evans, Engelbrecht, and Jordaan 2023; Garlick and Bradley 2021; Ghignone, Baumann, and Magno 2022; Samak, Samak, and Kandhasamy 2021)](https://www.zotero.org/google-docs/?qQYZDa). These approaches are limited when it comes to providing insights for improving human performance (Hojaji et. al., 2026).

  

**Problem statement:**

Hojaji et al. (2023, 2024) identified telemetry features associated with driver performance and showed that ML can classify performance levels and highlight key metrics such as speed, steering behavior, and lane deviation [(Hojaji et al. 2024; Hojaji, Toth, and Campbell 2023)](https://www.zotero.org/google-docs/?0uGnbI). Hojaji et al. (2026) extended this line of work by integrating ML-based feature importance with an evolutionary algorithm to optimize sector-level performance indicators and generate faster, smoother, and more stable idealized laps for coaching purposes [(Hojaji, Toth, and Campbell 2026)](https://www.zotero.org/google-docs/?vIvKuT). A key remaining gap is that feature importance was computed globally rather than at the **sector level**, because reliable segment-specific estimation would require larger datasets, leaving open the question of which circuit segments most strongly influence optimal lap performance [(Hojaji, Toth, and Campbell 2026)](https://www.zotero.org/google-docs/?xv76Jr).

  

**Objectives:**

  - To construct a micro-sector telemetry dataset by extracting and processing sequential driving data from a racing simulator environment. 
  - To develop a predictive machine learning model that quantifies corner interdependencies and identifies optimal speed-tradeoffs across sequential track sectors. 
  - To optimize overall lap-time performance by integrating the sector-importance model with an evolutionary algorithm, and validating the generated racing lines against human baseline telemetry. 

  

References:

[Evans, B., H. Engelbrecht, and H. Jordaan. 2023. “High-Speed Autonomous Racing Using Trajectory-Aided Deep Reinforcement Learning.” *IEEE Robotics and Automation Letters* 8: 5353–59. doi:10.1109/lra.2023.3295252. ](https://www.zotero.org/google-docs/?jsdCqp)

[Garlick, Sam, and Andrew Bradley. 2021. “Real-Time Optimal Trajectory Planning for Autonomous Vehicles and Lap Time Simulation Using Machine Learning.” *Vehicle System Dynamics* 60: 4269–89. doi:10.1080/00423114.2021.2011929. ](https://www.zotero.org/google-docs/?jsdCqp)

[Ghignone, Edoardo, N. Baumann, and Michele Magno. 2022. “TC-Driver: A Trajectory-Conditioned Reinforcement Learning Approach to Zero-Shot Autonomous Racing.” *IEEE Transactions on Field Robotics* 1: 527–36. doi:10.55417/fr.2023020. ](https://www.zotero.org/google-docs/?jsdCqp)

[Hojaji, Fazilat, Adam Toth, and Mark Campbell. 2026. “Optimizing Sim Racing Performance Using Machine Learning and Evolutionary Algorithms:” In *Proceedings of the 18th International Conference on Agents and Artificial Intelligence*, Marbella, Spain: SCITEPRESS - Science and Technology Publications, 997–1004. doi:10.5220/0014609600004052. ](https://www.zotero.org/google-docs/?jsdCqp)

[Hojaji, Fazilat, Adam J. Toth, and Mark J. Campbell. 2023. “A Machine Learning Approach for Modeling and Analyzing of Driver Performance in Simulated Racing.” In *Artificial Intelligence and Cognitive Science*, Communications in Computer and Information Science, eds. Luca Longo and Ruairi O’Reilly. Cham: Springer Nature Switzerland, 95–105. doi:10.1007/978-3-031-26438-2\_8. ](https://www.zotero.org/google-docs/?jsdCqp)

[Hojaji, Fazilat, Adam J. Toth, John M. Joyce, and Mark J. Campbell. 2024. “An AI Approach for Analyzing Driving Behaviour in Simulated Racing Using Telemetry Data.” In *Games and Learning Alliance*, eds. Pierpaolo Dondio, Mariana Rocha, Attracta Brennan, Avo Schönbohm, Francesca De Rosa, Antti Koskinen, and Francesco Bellotti. Cham: Springer Nature Switzerland, 194–203. doi:10.1007/978-3-031-49065-1\_19. ](https://www.zotero.org/google-docs/?jsdCqp)

[Kabzan, Juraj, Lukas Hewing, Alexander Liniger, and Melanie N. Zeilinger. 2019. “Learning-Based Model Predictive Control for Autonomous Racing.” *IEEE Robotics and Automation Letters* 4(4): 3363–70. doi:10.1109/LRA.2019.2926677. ](https://www.zotero.org/google-docs/?jsdCqp)

[Lee, Hojoon, Takuma Seno, Jun Jet Tai, Kaushik Subramanian, Kenta Kawamoto, Peter Stone, and Peter R. Wurman. 2025. “A Champion-Level Vision-Based Reinforcement Learning Agent for Competitive Racing in Gran Turismo 7.” *IEEE Robotics and Automation Letters* 10(6): 5545–52. doi:10.1109/LRA.2025.3560873. ](https://www.zotero.org/google-docs/?jsdCqp)

[Samak, Chinmay Vilas, Tanmay Vilas Samak, and S. Kandhasamy. 2021. “Autonomous Racing Using a Hybrid Imitation-Reinforcement Learning Architecture.” *ArXiv* abs/2110.05437. doi:10.48550/arxiv.2110.05437.   
](https://www.zotero.org/google-docs/?jsdCqp)

# deprecated  

# TODO

1.  Attempt to translate SCP SCR to CPP for Assetto Corsa.
2.  Verify if the algorithm is properly implemented before concluding the potential problems.
3.  Once verified, identify the potential problems and go from there.

  

# Backup Ideas

1.    
      

# refined methodology  

## Framework Diagram

# Methodology

  

#### **Data Collection and Simulator Reliability**

This thesis uses two datasets: a main dataset from Hojaji et al. [(2024)](https://www.zotero.org/google-docs/?TsaHqa), used to build and test the method, and an external test set recorded for this thesis, used only to check whether the trained surrogate holds for new drivers, a newer version of the simulator and different hardware.

**Main dataset (Hojaji et al., 2024).** The main dataset is the segment-specific behavioural dataset published as supplementary material with Hojaji et al. [(2024)](https://www.zotero.org/google-docs/?fbovsU) under a Creative Commons CC BY 4.0 licence (the article states that "the main datasets have been included as supplementary files"; the channels and metrics are described in its Tables A1 and A2). It holds 826 laps from 166 drivers in Assetto Corsa Competizione (ACC), all driving the McLaren 720S GT3 at Brands Hatch, recorded between October 2022 and January 2023. In that study all drivers used the same track, vehicle setup and game setup [(Hojaji et al., 2024)](https://www.zotero.org/google-docs/?NBSJfV). Each lap is already divided into 19 microsectors (9 corners and 10 straights, with the start/finish straight split into its start and end parts). For each microsector the dataset gives its time, seven summary statistics (minimum, maximum, mean, start, end, change and standard deviation) for each telemetry channel, and eight driver-input KPIs: brake length, brake duration, trail-braking duration, throttle duration, throttle application speed, throttle release, peak steering value and time to peak steering. Because the speed at the start of each microsector equals the speed at the end of the previous one, entry and exit speeds can be read directly. Drivers contributed between 1 and 8 laps each (median 5).

**External test set (recorded for this thesis).** To test the surrogate outside the data it was built on, 10 recruited drivers each record 30 laps of the McLaren 720S GT3 at Brands Hatch in ACC v1.10.4 on their own rigs at home. The software and in-game settings are fixed and sent to every driver as an instruction sheet with the car setup file; the hardware is not fixed, so each driver reports it on a short form (Appendix 1). The minimum requirement is a steering wheel with pedals. Telemetry is exported with ACC's built-in MoTeC logging [(Vasilakos, 2019)](https://www.zotero.org/google-docs/?U6Ry3e) and processed with the same MoTeC i2 Pro workspace, maths channels and export settings as the main dataset, so that the same 19 microsectors and the same KPIs are produced. Drivers upload the raw MoTeC files (.ld and .ldx) and the form to a set out google drive for uniformity.

These laps are never used for training, feature selection or tuning. Because they differ from the main dataset in simulator version, hardware and drivers, they show how far the surrogate's accuracy carries over to new conditions. Hardware is recorded because force-feedback settings can change lap time and some steering measures [(Murphy et al., 2026)](https://www.zotero.org/google-docs/?x3aspp) and a limited field of view can affect perceived speed [(Kemeny & Panerai, 2003)](https://www.zotero.org/google-docs/?FJPupw).

  

### **Simulator Validity and Scope**

A simulator should not be labelled "valid" or "invalid" as a whole. Its validity depends on the research question and the variables measured [(Himmels et al., 2023)](https://www.zotero.org/google-docs/?gdjubt). Absolute and relative validity both describe how a simulator compares with real driving, and this study makes no such comparison. It does not claim that ACC telemetry is equivalent to real-car telemetry. Its context is sim racing as an esport: the drivers, laps, fast reference and optimized targets all exist inside ACC, and every comparison is made between laps recorded in the same simulator with the same car and track. The results are therefore stated for competitive sim racing in ACC, not for professional real-world racing. The wider evidence on simulator validity, including studies suggesting that simulator measures partly reflect real driving skill, is reviewed in \[Chapter 2 (Section 2.2)\].

**Consistency of the measurements.** Separately from validity, the study checks how consistent each control KPI is across a driver's recorded laps, measured as the coefficient of variation of that KPI in each microsector, averaged over drivers with at least two valid laps. KPIs with low consistency are reported as a limitation.

  

#### **Step 0:** **Setup and Settings**

These settings apply to the external test set. The main dataset (Hojaji et al., 2024) was recorded by its authors with one shared car setup and game setup.

  - **\*\*Hardware:\*\* Drivers use their own rigs. The minimum requirement is a steering wheel with pedals; each driver's hardware is recorded on the driver form (Appendix 1).**
  - **\*\*Software:\*\* Assetto Corsa Competizione v1.10.4 (racing simulator), MoTeC i2 Pro 1.1 (telemetry analysis)**
  - **\*\*Simulation Settings:\*\***   
      - **\*\*Car:\*\* McLaren 720S GT3, default setup, sent to drivers as the setup file**
      - **\*\*Track:\*\* Brands Hatch**
      - **\*\*Assists:\*\* ABS 5, traction control 5, stability control off, auto clutch on**
      - **\*\*Track Conditions:\*\* clear weather, fixed grip state, fixed track temperature (26 °C), fixed time of day 12:00 PM, dynamic weather off**
      - **\*\*Session:\*\* practice session, soft tyres, 20 L of fuel, fuel consumption rate 0x.**

 

#### **Step 1: Sequential Preprocessing and Microsector Segmentation**

  - **Input:** Segment-level telemetry of Hojaji et al. [(2024)](https://www.zotero.org/google-docs/?nB4d6O), with each lap already divided into microsectors, plus the external test laps exported with the same MoTeC workspace and settings.
  - **Microsectors:** Each lap is divided into M = 19 ordered microsectors (9 corners and 10 straights, with the start/finish straight split into its start and end parts), following the segmentation of Hojaji et al. [(2024)](https://www.zotero.org/google-docs/?COjTSd), with boundaries fixed by track distance so that every lap is divided at the same points.
  - **Lap filter:** Remove in-laps, out-laps, standing starts and invalid laps, including laps whose recorded lap time does not match the sum of their microsector times. Then remove outlier laps whose lap time lies more than three standard deviations from the mean of all laps (|z| \> 3). The filter is applied to the main dataset and, separately, to the external test laps. The final numbers of drivers and laps are reported after filtering.
  - **Split:** Valid laps of the main dataset are split 70/30 into training and test sets by driver, so no driver appears in both. The test set is used only for the final surrogate test. The external test laps are kept apart and never used for training, feature selection or tuning.
  - **Control KPIs:** Control KPIs are driver inputs only. The candidates are the eight KPIs computed in the dataset (brake length, brake duration, trail-braking duration, throttle duration, throttle application speed, throttle release, peak steering value and time to peak steering) plus summary statistics of the driver-input channels for each microsector: maximum and mean brake, maximum and mean throttle, share of the microsector at full throttle, maximum, mean and standard deviation of the absolute steering angle, steering reversal rate, and lowest gear. Channels that describe the car's response rather than the driver's input (speed, accelerations, lane deviation, understeer and oversteer, ABS and traction control activity) are excluded. Step 3 selects the top K = 10 from this pool.

#### **Step 2: Performance Stratification (Clustering)**

  - **Process:** Apply K-Means clustering to the lap times of all valid laps of the main dataset, with the number of clusters k chosen by the Elbow Method and Silhouette Coefficient, to label laps by skill tier (Fast, Medium and Slow if k = 3). The fastest cluster serves as the Fast reference whatever the value of k. Following Hojaji et al. (2024), lap time alone is clustered. Only lap time is used, so labelling the test laps passes no KPI information into training.
  - **\*\*Objective:\*\* To define the Fast reference used later: the Fast-cluster test laps on which the surrogate is evaluated (Step 4), and the fast-lap entry speeds and KPI medians used by the GA and its output (Step 5). Fast-lap values used in Step 5 are taken from training laps only.**

#### **Step 3: Microsector-Level Feature Selection**

  - **Process:** Using the training laps, candidate KPIs whose Pearson correlation is weak (|r| \< 0.1) with both Δtn and vexit,n are removed. A single XGBoost model is then fitted on all training laps, with the remaining candidate KPIs, the microsector index n and the entry speed ventry,n as inputs, and Δtn and vexit,n as outputs. KPI importance is measured as the mean absolute SHAP value, computed with TreeSHAP (Lundberg et al., 2020) and grouped by microsector. For each microsector, the importances for each target are normalized to sum to 1 and the two targets are averaged. These values are then averaged across microsectors, and the top K = 10 KPIs, common to all microsectors, form the GA genes. The per-microsector importances are also reported. This model is used only for ranking; the surrogate is trained in Step 4.
  - **Objective:** Identify the top K = 10 (to be consistent with Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?oGP4F3)) control KPIs, common to all microsectors, that best predict each microsector’s time Δtn​ and exit speed vexit, n, given its ventry,n​ instead of ranking KPIs against global lap time, and report which KPIs matter most in each microsector. 

  
  

#### **Step 4: Interdependency Surrogate Modeling**

  - **Process:** Train a single multi-output XGBoost regressor, shared by all microsectors, on the training laps. Its inputs are the K control KPIs selected in Step 3, the entry speed ventry,n and the microsector index n, and its outputs are Δtn and vexit,n.
  - **Mapping:****  
    **fML: (sn, ventry,n, n) → (Δtn, vexit,n), where sn is the selected control KPIs of microsector n
  - **Validation:** Hyperparameters are tuned by grid search inside 10-fold cross-validation grouped by driver on the training laps, scored by Mean Absolute Error (MAE). The model is then refit on all training laps with the best hyperparameters. MAE and R² measure how accurately the surrogate predicts each microsector's time and the exit speed passed on to the next, and are reported on the test set overall and on its Fast-cluster laps. Each test lap is also rolled out through the chained surrogate: starting from its recorded entry speed at microsector 1, the predicted exit speed of each microsector is used as the entry speed of the next, and the predicted lap time and boundary speeds are compared with the recorded ones. The surrogate is then evaluated once on the external test set (MAE, R² and lap rollout), to check how well it carries over to new drivers, a newer version of ACC and different hardware.

#### **Step 5: Genetic Algorithm Optimization with a Coupled Fitness Function**

  - **Process:** The evolutionary search reuses the genetic algorithm (GA) of Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?0XsXcK) without modification, so that the fitness function is the only component that differs from the baseline. The population of 120 individuals evolves for 200 generations using two-point crossover (probability 0.8) and Gaussian mutation (standard deviation 0.05) applied to each gene with probability 0.15; mutated genes are clipped to the training range of that KPI. Elitism is exercised by preserving the two best individuals in each generation and tournament selection with a size of three [(Hojaji et al., 2026)](https://www.zotero.org/google-docs/?VIGfyQ).
  - **Initialization:** Each chromosome holds the K = 10 selected control KPIs for each of the M microsectors, giving M × K genes (190 for M = 19 and K = 10). Each gene is initialized randomly within the min–max scaled range of that KPI observed in the training laps.
  - **Fitness Evaluation:** Each individual is scored as Fitness = T + λ·P, with λ = 0.1 taken from Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?GPUGSa) without tuning. P is rebuilt from the penalty description in Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?GPUGSa), because its formulas and thresholds are not reported. Instead of scaling a baseline time for each microsector independently, the candidate's KPIs are decoded to their original units and passed through the Step 4 surrogate one microsector at a time. The first microsector's entry speed is set to the mean entry speed of the Fast-cluster training laps and is fixed, so that improvements come from driver inputs rather than a faster start. The predicted exit speed of each microsector n becomes the entry speed of microsector n+1 (ventry,n+1 = vexit,n). T is the sum of the predicted microsector times Δtn. The 90–105% clamp of the baseline is not applied, because the surrogate replaces the time model it bounded; both fitness variants of the comparison below are treated the same way. Lap closure is not enforced: the last microsector's predicted exit speed is not required to match the fixed entry speed of the first. This is treated as a simplification, and the gap is reported for each optimized lap.
  - **Output:** Optimized per-microsector targets for the selected control KPIs. Each target is reported against the median of that KPI in that microsector over the Fast-cluster training laps, and the difference is phrased as a coaching instruction, for example "microsector 7: hold trail braking 0.2 s longer than the fast-lap median".

  

## **Structural Limitations of Independent Microsector Evaluation and the Justification for Chained Evaluation**

**Note:** We use the word *microsector* for a single corner or straight segment, which Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?use6PA) call sectors (10 corner and 10 straight), to distinguish them from a track's official timing sectors.

  

**The Baseline Approach and the Mechanism of Isolation** In the baseline evolutionary algorithm framework, driving trajectories are encoded as chromosomes spanning 20 track microsectors, with new candidate inputs generated via two-point crossover and Gaussian mutation. A key limitation of this architecture is its reliance on an independent, static fitness evaluation model. To estimate performance, the algorithm retrieves a baseline microsector time and applies a linear adjustment based on how the mutated Key Performance Indicators (KPIs) deviate from a neutral midpoint. The fitness value of an individual is computed as the sum of all adjusted microsector times plus a penalty term across the full lap. The penalty term discourages three kinds of unrealistic candidates: sudden changes in a KPI between consecutive microsectors, unusually large gradients within a single microsector, and KPI values that exceed predefined physical thresholds. In addition, each adjusted microsector time is clamped to between 90% and 105% of its baseline time [(Hojaji et al., 2026)](https://www.zotero.org/google-docs/?c8p8Em). 

  

**The Microsector Interdependency**

Lap-time simulation has long treated a lap as a continuous problem in which the speed at any point is bounded by the track sections before and after it. In quasi-steady-state methods, speed profiles are integrated forward out of one corner and backward from the next, and joined where they meet [(Kapania et al., 2016; Lenzo & Rossi, 2020; Veneri & Massaro, 2020)](https://www.zotero.org/google-docs/?GtctQ9). Likewise, data-driven racing-line models perform better when given both the preceding and the upcoming track geometry [(Garlick & Bradley, 2021)](https://www.zotero.org/google-docs/?VwAslh).

The fitness function of Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?dd5wKR) does not represent this coupling. Each microsector time is scaled from that microsector's own KPI vector and the results are summed, so a change to the KPIs of microsector n cannot alter the predicted time of microsector n+1. The penalties and the clamp limit how far a candidate can depart from realistic values and how much any single microsector can gain, but they do not model how the state in which a microsector is exited affects the time of the next. For example, raising the speed KPI of a corner shortens that microsector's predicted time, while the extra braking this demands in the preceding straight, or the compromised exit it may cause, is never charged to the neighbouring microsectors. We therefore argue that microsector-independent evaluation can credit candidate laps with microsector-level gains that are mutually inconsistent.

  

**The Proposed Solution: Chained Microsector Surrogate Fitness**

The proposed framework keeps the optimizer, its settings and its initialization identical to the baseline and replaces only the fitness function. The baseline's linear, microsector-independent time model is replaced by an XGBoost surrogate that predicts each microsector's time and exit speed from its KPIs and its entry speed. Chaining these predictions carries the state in which one microsector is exited into the next, so a change that **shortens one microsector at the expense of its neighbour** is reflected in the predicted lap time. This coupling is intended to approximate the interdependence between microsectors, so that the KPIs found by the GA account for it.

Because the GA is held fixed, differences in the optimized laps can be attributed to the fitness function rather than to the search procedure. We test this by running the same GA with two fitness variants: the proposed coupled fitness, and a microsector-independent variant in which each microsector's entry speed is taken from the mean entry speed of the Fast cluster training laps at each microsector rather than from the preceding prediction. Both variants use the same selected KPIs, penalty term and random seeds. Each variant is run with 30 random seeds, shared between the variants so that runs are paired. The best lap of every run is also scored by the chained surrogate, a common judge validated by the rollout test; the gap between the independent variant's own predicted lap time and its chained lap time shows how much independent evaluation overstates the gain. Paired differences are tested with a Wilcoxon signed-rank test and count only when larger than the rollout lap-time error. Because the comparison is between two fitness variants on the same data, it does not depend on using the same track as the baseline. This thesis uses Brands Hatch [(Hojaji et al., 2024)](https://www.zotero.org/google-docs/?3sYwsc) rather than Laguna Seca [(Hojaji et al., 2026)](https://www.zotero.org/google-docs/?LQRi5J).

  

## **Significance of the Study**

This study is expected to benefit the following groups.

**Sim racers.** The study produces per-microsector targets for a driver's own inputs, such as braking, throttle and steering, each expressed relative to the median of the fast laps in that microsector (for example, “microsector 7: hold trail braking 0.2 s longer than the fast-lap median”). Because the fitness function passes the predicted exit speed of each microsector to the next microsector as its entry speed, the targets account for how a change in one corner or straight affects the rest of the lap, and they do not assume an entry speed that the preceding microsector cannot deliver. The method relies only on telemetry that drivers can already export from Assetto Corsa Competizione (ACC). It is also tested on laps recorded by drivers on their own home equipment, which shows whether the targets remain usable outside the dataset the model was built on.

**Coaches and esports teams.** The study reports which driver inputs the model relies on most in each microsector, rather than only across the whole lap. Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?VTZuMX) computed feature importance globally and noted that reliable segment-specific estimation would require larger datasets. This study does not fit separate models for each microsector. It derives per-microsector importance from a single model pooled across all microsectors, which gives coaches and teams a data-driven indication of where on the track a driver may focus practice and which inputs to work on there.

**Researchers.** This study extends the framework of Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?xsWlJD) by replacing its fixed linear formula for estimating microsector times with a trained surrogate model, chained so that the predicted exit speed of each microsector becomes the entry speed of the next. Because the genetic algorithm is kept identical to the baseline, the comparison between the coupled and the microsector-independent fitness isolates the effect of microsector coupling on the optimized lap. The study is built on a publicly available dataset [(Hojaji et al., 2024)](https://www.zotero.org/google-docs/?uCKHzE) released under a CC BY 4.0 license, so other researchers can reproduce and extend it.

# References

[Garlick, S., & Bradley, A. (2021). Real-time optimal trajectory planning for autonomous vehicles and lap time simulation using machine learning. *Vehicle System Dynamics*, *60*, 4269–4289. https://doi.org/10.1080/00423114.2021.2011929 ](https://www.zotero.org/google-docs/?tRTxoT)

[Himmels, C., Parduzi, A., Fischer, M., & Riener, A. (2023). Towards a common understanding of driving simulator validity. *Adjunct Proceedings of the 15th International Conference on Automotive User Interfaces and Interactive Vehicular Applications (AutomotiveUI ’23 Adjunct)*, 191–196. https://doi.org/10.1145/3581961.3609895 ](https://www.zotero.org/google-docs/?tRTxoT)

[Hojaji, F., Toth, A., & Campbell, M. (2026). Optimizing Sim Racing Performance Using Machine Learning and Evolutionary Algorithms. *Proceedings of the 18th International Conference on Agents and Artificial Intelligence*, 997–1004. https://doi.org/10.5220/0014609600004052 ](https://www.zotero.org/google-docs/?tRTxoT)

[Hojaji, F., Toth, A. J., Joyce, J. M., & Campbell, M. J. (2024). AI-enabled prediction of sim racing performance using telemetry data. *Computers in Human Behavior Reports*, *14*, 100414. https://doi.org/10.1016/j.chbr.2024.100414 ](https://www.zotero.org/google-docs/?tRTxoT)

[Kapania, N. R., Subosits, J., & Christian Gerdes, J. (2016). A Sequential Two-Step Algorithm for Fast Generation of Vehicle Racing Trajectories. *Journal of Dynamic Systems, Measurement, and Control*, *138*(9), 091005. https://doi.org/10.1115/1.4033311 ](https://www.zotero.org/google-docs/?tRTxoT)

[Kemeny, A., & Panerai, F. (2003). Evaluating perception in driving simulation experiments. *Trends in Cognitive Sciences*, *7*(1), 31–37. https://doi.org/10.1016/S1364-6613(02)00011-6 ](https://www.zotero.org/google-docs/?tRTxoT)

[Lenzo, B., & Rossi, V. (2020). A Simple Mono-Dimensional Approach for Lap Time Optimisation. *Applied Sciences*, *10*(4), 1498. https://doi.org/10.3390/app10041498 ](https://www.zotero.org/google-docs/?tRTxoT)

[Murphy, C. J., Toth, A. J., Hojaji, F., & Campbell, M. J. (2026). Force feedback drives sim racing performance: The influence of force and vibrotactile haptic feedback in simulator steering wheels. *Computers in Human Behavior Reports*, *22*, 100993. https://doi.org/10.1016/j.chbr.2026.100993 ](https://www.zotero.org/google-docs/?tRTxoT)

[Vasilakos, A. (2019, March). *ACC Blog: MoTeC telemetry and dedicated ACC workspace*. https://www.overtake.gg/threads/acc-blog-motec-telemetry-and-dedicated-acc-workspace.165714/ ](https://www.zotero.org/google-docs/?tRTxoT)

[Veneri, M., & Massaro, M. (2020). A free-trajectory quasi-steady-state optimal-control method for minimum lap-time of race vehicles. *Vehicle System Dynamics*, *58*(6), 933–954. https://doi.org/10.1080/00423114.2019.1608364 ](https://www.zotero.org/google-docs/?tRTxoT)

# Appendix 1: Driver Form (sim racing telemetry study)

Fill this in after your session and upload it with your MoTeC files.

## 1\. About you

1\. Participant ID (given to you by the researcher): \_\_\_\_\_\_

2\. Age: \_\_\_\_\_\_

3\. Country: \_\_\_\_\_\_

4\. How long have you been sim racing? ( ) Less than 6 months ( ) 6 to 12 months ( ) 1 to 3 years ( ) More than 3 years

5\. Roughly how many hours a week do you sim race? \_\_\_\_\_\_

6\. Hours driven in Assetto Corsa Competizione (from Steam): \_\_\_\_\_\_

7\. Have you driven the McLaren 720S GT3 at Brands Hatch before? ( ) Never ( ) A few times ( ) Often

8\. Do you race competitively (online leagues or esports)? ( ) No ( ) Yes, at what level: \_\_\_\_\_\_

9\. Real-world driving: ( ) No licence ( ) Road licence ( ) Track days or karting ( ) Racing licence

## 2\. Your setup

10\. Wheel base (brand and model): \_\_\_\_\_\_

11\. Pedals (brand and model): \_\_\_\_\_\_

12\. Brake pedal type: ( ) Potentiometer ( ) Load cell ( ) Hydraulic ( ) Not sure

13\. Wheel rotation set in your wheel software (degrees): \_\_\_\_\_\_

14\. Force feedback strength (in-game and in your wheel software): \_\_\_\_\_\_

15\. Shifting: ( ) Paddles ( ) H-shifter or sequential shifter

16\. Display: ( ) Monitor ( ) Triple monitors ( ) TV ( ) VR headset. Size (inches): \_\_\_\_\_\_

17\. Seating: ( ) Cockpit or rig ( ) Desk chair ( ) Other: \_\_\_\_\_\_

18\. Motion platform or bass shakers? ( ) No ( ) Yes: \_\_\_\_\_\_

  

## 3\. Session check

19\. Did you use the setup file and settings from the instruction sheet? ( ) Yes ( ) No, what changed: \_\_\_\_\_\_

20\. Please attach screenshots of the in-game Assists and Session settings screens.

21\. Number of warm-up laps driven: \_\_\_\_\_\_ Number of recorded laps driven: \_\_\_\_\_\_

22\. Did you drive the whole session yourself? ( ) Yes ( ) No

23\. Did you feel any dizziness, nausea or discomfort during the session? ( ) No ( ) Yes, a little ( ) Yes, a lot

24\. Did anything go wrong (crash, disconnect, game freeze, interruption)? ( ) No ( ) Yes: \_\_\_\_\_\_

  

## 4\. Consent

25\. I confirm that I gave informed consent before the session and agree to my anonymised telemetry being used for research. ( ) Yes

  
  
  

# literature review  

   

   

# **Chapter 2: Review of Related Literature**

## **2.1 Introduction and Scope**

This chapter reviews the literature needed to answer one question: how should an evolutionary optimizer of sim-racing driver inputs evaluate a lap whose parts depend on one another? It first establishes why simulator telemetry is a sound source of data for this question (2.2). It then reviews how machine learning has been used to analyse driver performance from such telemetry, and what studies of driving technique show about the inputs that change lap time (2.3). It describes the framework this thesis extends, the genetic algorithm of Hojaji et al. (2026) (2.4). Section 2.5 reviews the physical reasons why the parts of a lap cannot be scored independently. Sections 2.6 and 2.7 review optimizers and learned models that do or do not carry this dependence, together with the known risks of chaining learned models, and 2.8 brings the strands together into the research gap.

Sources were located through Consensus, Google Scholar and arXiv, supplemented by publisher pages. Peer-reviewed full texts were preferred, so that no central claim rests on an abstract alone.

Three terms are used throughout. A microsector is a single corner or a single straight. Hojaji et al. call the same unit a "sector" (2026) or a "segment" (2024b). In this thesis "sector" keeps its usual meaning of an official timing sector, which spans several microsectors. Control KPIs are measures of the driver's inputs, such as brake duration or peak steering angle. Entry, apex and exit speed and microsector time are state or outcome variables, because they result from those inputs. A surrogate is a model that stands in for the true evaluator of a candidate lap, which here would be driving the lap in the simulator.

## **2.2 Simulator Validity and Reliability**

### **2.2.1 What "valid" means for this thesis**

A simulator should not be labelled "valid" or "invalid" as a whole, because its validity depends on the research question and the variables measured (Himmels et al., 2023). Himmels et al. (2023) distinguish two kinds of validity. A simulator has absolute validity when its measurements match those from real driving, and relative validity when effects in the simulator point in the same direction as in real driving. Both kinds compare a simulator with the real world.

This thesis makes no such comparison and does not claim that telemetry from Assetto Corsa Competizione (ACC) is equivalent to real-car telemetry. Its context is sim racing as an esport. The drivers, the laps, the fast reference and the optimized targets all exist inside ACC, and every comparison is made between laps recorded in the same simulator, with the same car, setup, track and conditions. The question is how to drive faster in the simulator, so the data need to be sound for that purpose only. The results are therefore stated for competitive sim racing in ACC, specifically the McLaren 720S GT3 at Brands Hatch, and not for real-world racing. This follows the research the thesis builds on, which treats sim racing performance as an outcome of interest in its own right (Hojaji et al., 2024b, 2026; Joyce et al., 2024).

### **2.2.2 Mixed evidence on simulator–real equivalence**

The wider validation literature gives a further reason to keep the claims inside the simulator, because its findings are mixed. A systematic review of driving simulator validation studies reported that roughly half of the simulators examined achieved absolute or relative validity, while about a third produced non-valid results, and that the relationship between simulator fidelity and validity was not straightforward (Wynne et al., 2019) . A comparison of six driving simulators reported good absolute validity for headway distance and lateral position but inconsistent results for driving speed (Himmels et al., 2024) , and speed is a central outcome in this thesis. In an earlier road-safety study, speed showed relative but not absolute validity, because participants drove faster in the real car than in the simulator (Godley et al., 2002). Real racing also places physical load and stress on the driver that a simulator does not reproduce (Holland et al., 2025). Apart from Holland et al. (2025), these studies concern road driving, so they are background rather than direct evidence about ACC.

### **2.2.3 Evidence that simulator measures reflect driving skill**

Although the thesis does not depend on it, some studies suggest that measures taken in racing simulators partly reflect real driving skill. In a fixed-base simulator, racing drivers achieved faster lap times, showed higher steering activity and followed a better racing line than non-racing drivers (van Leeuwen et al., 2017), although the sample was small and the simulator was not ACC. In a professional driver-in-the-loop simulator, the slower lap times of amateur drivers came mainly from weaker vehicle handling rather than from their choice of line (von Schleinitz et al., 2022). With consumer racing-simulator hardware running the original Assetto Corsa, lap time correlated with driving-speed measures taken on a research simulator (Tiu et al., 2020), although that study's participants and purpose differ greatly from this one. Together, these findings suggest that what separates fast and slow laps in a simulator is at least partly driving skill and not only familiarity with the game. They are supporting context, and the conclusions of this thesis do not rely on them.

### **2.2.4 Precedent for the data and pipeline**

ACC telemetry captured with MoTeC has been used in several peer-reviewed studies of sim racing performance by one research group (Hojaji et al., 2024b, 2026; Joyce et al., 2024), and the main dataset of this thesis is the one published with Hojaji et al. (2024b). Remonda et al. (2021) compared drivers in a professional racing simulator using per-segment telemetry features such as brake point and segment entry and exit speeds, which is a precedent for measuring driver behaviour at the level of individual track sections. The developer states that ACC's tracks are laser-scanned and that its physics simulate modern GT cars (KUNOS Simulazioni, n.d.). These are the developer's own claims, not independent validation, and the thesis does not rely on them.

Separately from validity, the thesis checks the reliability of its measurements, meaning how consistent each KPI is across a driver's recorded laps. The procedure is described in Chapter 3.

## **2.3 Telemetry-Based Analysis of Driver Performance**

### **2.3.1 Predicting and stratifying performance**

A line of work by Hojaji and colleagues has shown that telemetry from ACC can predict how well a sim racer drives. Hojaji et al. (2023) extracted KPIs from ACC telemetry and used support vector machine, XGBoost and random forest feature selection to reduce 84 candidate features to 10 that predict a driver's performance level. Speed, steering and lane-deviation KPIs were among the most informative (Hojaji et al., 2023, 2024a).

Hojaji et al. (2024b) went further and divided each lap at Brands Hatch into 19 segments (their term: 10 straights and 9 turns). They grouped laps into skill levels by applying K-Means clustering to lap time, choosing the number of clusters with the Elbow method and the Silhouette coefficient. The stratification step of this thesis (Chapter 3, Step 2) follows that procedure, and the segment-level dataset published with that study is the main dataset used here.

In these studies, importance is measured against lap-level performance, either a performance class or lap time. They therefore show which KPIs matter for a lap, but not where on the lap they matter.

### **2.3.2 Per-corner explanation and coaching**

Bae et al. (2025) moved the unit of analysis to the individual corner. They trained a per-corner skill classifier, explained it with SHAP (Lundberg & Lee, 2017) and used it to generate counterfactual advice that moves a driver toward the expert class. Their "Strategic Features" include a corner's entry maximum velocity, exit maximum velocity and entry minimum velocity. Other systems also give per-corner advice against a reference: Kaufman et al. (2024) derive the reference from a reinforcement-learning agent, and Nunes et al. (2026) generate feedback with a large language model from rule-based diagnoses. Nunes et al. (2026) name "a speed deficit carried over from the previous corner" among their diagnoses, which shows that the carry-over of speed between corners is visible in human sim-racing data.

These coaching systems do not need to model how one corner affects the next. A driver carries out the advice in the simulator, and the simulator's physics enforces the coupling. In Bae et al. (2025), for example, entry and exit speed are features of the same corner, which suits advice that a real driver will act on. A lap produced by an optimizer has no driver to enforce the coupling, so the model that evaluates the lap must carry it instead. In this thesis, entry speed is therefore treated as a state inherited from the previous microsector: it enters the model as a covariate and is never a decision variable.

### **2.3.3 Driver inputs that change lap time**

Studies of race driving technique show that lap time responds to the driver's own inputs, which supports control KPIs as the variables to optimize. Trail braking, in which braking continues into corner entry, emerges as the solution of the minimum-time cornering problem under set boundary conditions at the corner exit, and a few parameters of the driver's steering, throttle and brake commands reproduce it across corner geometries (Velenis et al., 2008) . Cornering techniques described by professional drivers can be written as simple families of curves, and the choice between them changed lap time on an autonomous race car (Theodosis & Gerdes, 2011) . On a real Formula Student car, cueing the driver with a braking point computed from a simulation of the section ahead reduced lap time (Peitzmeier et al., 2023) . Drivers also improve lap by lap by correcting earlier errors, an adaptation that race-engineering experts identified and that a learned driver model reproduced (Löckel et al., 2023). Hojaji et al. (2026) likewise report trail-braking duration among the KPIs that changed most in their optimized lap. These studies concern technique within a corner; how the result of one corner carries into the next is taken up in 2.5.

## **2.4 The Baseline: Hojaji et al. (2026)**

Hojaji et al. (2026) extended this line of work from analysis to optimization, and their framework is the closest prior optimization of human driver inputs in sim racing. A genetic algorithm (GA) evolves a lap encoded as 20 sectors (their term for microsectors: 10 corner-dominant and 10 straight-dominant), each described by a vector of 10 scaled KPIs, to produce an idealized lap for coaching. The data were recorded in ACC with the McLaren 720S GT3 at Laguna Seca.

Each candidate lap is scored as Fitness = T + λ·P, with λ = 0.1. T is "the predicted lap time obtained from the sector-based surrogate model" (Hojaji et al., 2026, p. ). For each microsector, this model takes a baseline time from fast laps and adjusts it linearly by how far that microsector's KPIs deviate from the midpoint of their scaled range, and the adjusted time is clamped to between 90% and 105% of the baseline. The penalty P discourages three kinds of unrealistic candidates: sudden changes in a KPI between consecutive microsectors, unusually large gradients within a microsector, and KPI values beyond predefined physical thresholds. The optimized lap, at about 81–82 s, was reported as "around 4–5 seconds" faster than the fastest human lap (Hojaji et al., 2026) . That lap is judged only by its predicted time, and the paper reports no replay of it in the simulator, so its quality rests on the fitness function alone. It is physically unverified, which is not the same as physically impossible.

The framework has two limitations that this thesis addresses. The first is stated by the authors: feature importance was computed globally rather than per microsector, because reliable segment-specific estimation would require larger datasets (Hojaji et al., 2026) \[verify wording and page\]. The second follows from the fitness equation. Each microsector's time depends only on that microsector's own KPIs, so no speed is passed from one microsector to the next. The penalties limit implausible KPI values and abrupt changes, but they carry no state. A similar limit has been reported for another surrogate used to evaluate racing drivers, whose models "compute each data point isolated from its temporal surrounding" (von Schleinitz et al., 2022).

The two limitations are linked. To rank KPIs for each microsector, the model must predict each microsector's own time and exit speed, and both depend on the speed with which the car enters that microsector (2.5). For this reason, entry speed is included as a covariate in the per-microsector feature selection of this thesis, and the gap named in the problem statement leads directly to the coupling gap. The GA settings and λ are kept unchanged, and the penalty P is rebuilt from the authors' description, so that the fitness is the only change (Chapter 3).

## **2.5 Physical Interdependence of Microsectors**

Lap-time simulation has long treated speed as continuous along the lap (see Massaro & Limebeer, 2021, for a review). Quasi-steady-state methods integrate the speed profile forward out of one corner and backward from the next, and join the two profiles where they meet (Brayshaw & Harrison, 2005; Kapania et al., 2016; Lenzo & Rossi, 2020; Veneri & Massaro, 2020). The speed at which the car leaves one section of track therefore bounds what is achievable in the next.

It follows that a gain in one microsector can carry a cost into the next. A later, faster entry into a corner may shorten that corner's time but cost exit speed, which then lengthens the following straight. Conversely, a slower entry can buy exit speed that pays off on the straight. This trade-off is this thesis's own reasoning from the mechanism described in the lap-time simulation literature, and it is the "speed trade-off" that Objective 2 refers to.

Optimization studies that score only part of a lap treat exit speed as worth something in its own right, which is consistent with this reasoning. Maniowski (2016) used a GA to optimize a driver's steering, brake and throttle actions through one corner of a multibody vehicle model, with section time and corner-exit velocity as separate criteria . In online time-optimal planning, adding an exit-speed term at the end of the planning horizon brought lap times closer to the offline minimum-lap-time solution than minimizing time alone, and moved the planner between early-apex and late-apex lines (Taddei et al., 2025). In both cases, exit speed matters because it is carried into the track that follows, which is the dependence that the chained surrogate of this thesis represents between microsectors.

Learned models show the same dependence. A data-driven racing-line model performed better when it was given both the preceding and the upcoming track geometry (Garlick & Bradley, 2021).

A fitness function that scores microsectors independently can therefore credit a candidate lap with gains that could not occur together. Evolutionary search is known to exploit such gaps in its evaluator (Lehman et al., 2020) , and optimizing against a learned model in particular tends to find inputs that the model scores well but that lie outside the data it was trained on (Trabucco et al., 2021; Kim et al., 2026). Whether this changes the optimized result in practice is an empirical question, and the ablation in Chapter 3 is designed to answer it.

## **2.6 Racing Optimizers that Carry the Coupling**

Most optimization research in racing targets autonomous agents rather than human drivers. Learning-based control and reinforcement learning produce fast driving policies, up to champion level in Gran Turismo 7 (Kabzan et al., 2019; Samak et al., 2021; Ghignone et al., 2022; Evans et al., 2023; Lee et al., 2025), and trajectory optimization and racing-line generation solve the lap as a whole (Garlick & Bradley, 2021; Massaro & Limebeer, 2021).

Evolutionary racing-line optimization carries the coupling by evaluating each candidate in a full simulator (Cardamone et al., 2010) or through a forward–backward physics speed profile over track segments (their term), using a GA and CMA-ES (Klapálek et al., 2024). Maniowski (2016) applied a GA to a driver's own actions rather than to the line, but over a single corner and through a multibody vehicle model verified against road tests .

These methods need a vehicle model or a simulator in the loop. They output a racing line, a trajectory, a policy or, for one corner, a set of driver actions, rather than targets for a human driver's inputs over each microsector of a full lap derived from that driver population's telemetry.

Botta et al. (2012) replaced full simulation inside the EA with a cheaper physics-based lap-time estimate, which performed worse. This is the racing precedent for scoring candidates with a surrogate, for the risk that it brings, and for checking a surrogate-optimized lap against something outside the model (Objective 3).

## **2.7 Learned and Chained Surrogates**

### **2.7.1 Surrogates in offline data-driven EAs**

A surrogate stands in for an evaluator that is unavailable or expensive (Jin, 2011). Data-driven evolutionary optimization is called offline when no new data can be generated during the search (Jin et al., 2019), which is the case here: the telemetry is fixed and no simulator is run inside the optimizer. In offline optimization the surrogate is fitted once to historical data, so the search can be trusted only where those data lie (Wang et al., 2019), which is why the GA initializes genes within the training-lap ranges and clips mutated genes to them. Surrogate errors can also accumulate and mislead the ranking of candidates (Liu et al., 2022) , so a difference between optimized laps should be trusted only if it is larger than the surrogate's own error.

By this definition the baseline's linear scaler is already a surrogate, and Hojaji et al. (2026) call it a "sector-based surrogate model". The thesis replaces it with a learned surrogate and so inherits the risks noted in 2.5 and 2.6.

### **2.7.2 Learned lap-time models in racing**

Learned lap-time models already exist in racing. A Gaussian-process surrogate of whole-lap time guides Bayesian trajectory optimization (Nam et al., 2026), and LightGBM predicts per-segment time (their term) from car setup in Assetto Corsa, reconstructing held-out lap time with 0.223 s mean absolute error (Satujoda & Huggins, 2026). Neither carries state from one part of the lap to the next: Nam et al. score the whole lap, and Satujoda and Huggins describe no carry-over between segments and report that "Telemetry-derived quantities were not used to generate the winning setup".

Gradient-boosted trees (Chen & Guestrin, 2016) suit tabular KPI data. In large benchmarks they matched or outperformed deep learning on medium-sized tabular data, with less tuning (Grinsztajn et al., 2022; Shwartz-Ziv & Armon, 2022), and light tuning of a boosted-tree model often mattered more than the choice of model family (McElfresh et al., 2023). XGBoost, LightGBM and CatBoost differ little in accuracy (Bentéjac et al., 2021), and gradient-boosted trees have served as EA surrogates (Mao et al., 2024). Their weakness for optimization is that they interpolate only: predictions degrade when a feature lies outside the training range (Malistov & Trushin, 2019) , which is a further reason to keep the search within the observed KPI ranges.

### **2.7.3 Chained surrogates outside racing**

Outside racing, linking per-stage models so that one stage's output is the next stage's input is established. It is formalized as function networks (Astudillo & Frazier, 2021; Kiroirwal et al., 2026) and has been applied with a GA to fed-batch fermentation (Chen et al., 2004) and with stacked Gaussian processes to multistage manufacturing (Geiger et al., 2023). In linked Gaussian-process emulators of computer models, linking per-stage emulators predicted a chain better than one emulator of the whole (Kyzyurova et al., 2018; Sanson et al., 2019). Geiger et al.'s comparison of joint and cascaded optimization parallels the coupled-versus-independent ablation used here.

Chaining carries two documented risks. When a learned one-step model is applied repeatedly, with its output fed back as its next input, its errors compound and move its inputs away from the training distribution (Venkatraman et al., 2015; Lambert et al., 2022). In regressor chains, a model trained on the true values of an upstream target but run on predicted values faces a mismatch between the inputs it was trained on and those it receives (Spyromitros-Xioufis et al., 2016). The surrogate in this thesis is trained on measured entry speeds but, inside the fitness, receives chained predictions, so Chapter 3 rolls each test lap through the full chain rather than judging the surrogate on per-microsector error alone.

### **2.7.4 Interpreting and validating the surrogate**

The methods used to select, validate and compare in Chapter 3 also rest on established work. TreeSHAP computes exact SHAP values for tree ensembles, avoids the inconsistency of gain-based importance, and builds global importance by aggregating local explanations (Lundberg et al., 2020). SHAP values explain the model rather than causation, and standard approximations can mislead when features are correlated (Aas et al., 2021), a limitation that applies to correlated control KPIs. Because laps are nested within drivers, random cross-validation would underestimate error; blocked or grouped validation is recommended whenever such dependence exists (Roberts et al., 2017), and non-independence between training and test data is a recognized form of leakage (Kapoor & Narayanan, 2023). Results of evolutionary runs rarely meet the assumptions of parametric tests, so paired comparisons of algorithm variants over seeds are usually made with nonparametric tests such as the Wilcoxon signed-rank test (Derrac et al., 2011; Carrasco et al., 2020).

## **2.8 Synthesis and Research Gap**

### **2.8.1 Synthesis**

Table 2.1 compares the closest studies on the three properties this thesis combines: a time model learned from human telemetry, state carried across microsector boundaries inside the evaluator, and driver control KPIs as decision variables. Three groups emerge. Coaching systems give advice to a driver, whose simulator enforces the coupling. Physics- and simulator-based optimizers carry the coupling through a vehicle model, but they optimize a racing line, a control policy or, over a single corner, a driver's actions on a vehicle model. Learned surrogates do not chain in racing, and where chained surrogates are used in other fields, they do not involve drivers.

*Table 2.1. Closest studies compared on the properties combined in this thesis. Units are given in each study's own term; "not described" means the paper does not describe it, not that it is absent.*

### **2.8.2 Research gap**

Most optimization research in racing targets autonomous agents (Kabzan et al., 2019; Evans et al., 2023; Lee et al., 2025). The closest optimization of human driver KPIs in sim racing (Hojaji et al., 2026) ranked KPIs globally, noting that estimating importance for each microsector would require larger datasets, and scored each microsector independently before summing, relying on penalties for abrupt transitions, within-microsector gradients and out-of-range values. Coaching systems advise a real driver (Bae et al., 2025; Kaufman et al., 2024; Nunes et al., 2026), so the driver and the simulator's physics enforce the coupling between microsectors. An optimizer's candidate laps, by contrast, exist only inside its fitness model, so that model must carry the coupling. Physics- and simulator-based optimizers do carry it through a vehicle model, but they optimize a racing line (Cardamone et al., 2010; Klapálek et al., 2024) or, over a single corner, a driver's actions on a calibrated vehicle model (Maniowski, 2016), and they value exit speed for the same reason (Taddei et al., 2025). Learned per-segment time models exist in sim racing but describe no carry-over of state and are not used as an optimizer's fitness (Satujoda & Huggins, 2026). Chained surrogates are established in multistage manufacturing and process optimization (Chen et al., 2004; Geiger et al., 2023) and have been formalized as function networks (Astudillo & Frazier, 2021), and their known risks, compounding error and a mismatch between training and prediction inputs (Venkatraman et al., 2015; Spyromitros-Xioufis et al., 2016), mean that a chained fitness has to be checked by rolling whole laps through the chain.

In the literature reviewed here, we did not find a study that uses a surrogate learned from human telemetry to propagate boundary speed between microsectors inside an evolutionary optimization of driver control KPIs, or that measures how that coupling changes the optimized result against an otherwise identical variant in which each microsector's entry speed is fixed at its mean fast-lap value. This thesis therefore adapts an established idea, the chained surrogate, to the optimization of sim-racing driver inputs and tests its effect by ablation. It claims no novelty for the physical coupling itself, for valuing exit speed in lap optimization, for chaining surrogates, for per-segment machine-learning time models or for diagnosing carried-over speed. Per-microsector feature selection follows from the chained surrogate, whose inputs must be ranked against its own targets, and it also answers the limitation stated by Hojaji et al. (2026).

  
  

  
  

# for consultation \#2  

  
  
  

## **Title: Extending an ML-EA Framework with a Microsector-Chained Surrogate Model for Sim Racing Performance Optimization**

## **On Simulator Validity**

  - A simulator should not be labelled valid or invalid, as it depends on the research question and the variables being measured [(Himmels et al., 2023)](https://www.zotero.org/google-docs/?gdjubt).
  - This study does not claim that ACC telemetry equals real-life telemetry. 
  - The context is within sim racing as an esport, therefore the results are stated for competitive sim racing in ACC, not professional real-world racing.   

## **Data**

  - The dataset from Hojaji [(2024)](https://www.zotero.org/google-docs/?r1sX1n) will be used, as well as our own dataset (to be collected) for further validation of the model.
      
      - From Hojaji [(2024)](https://www.zotero.org/google-docs/?tFEVr7): 826 laps at Brands Hatch; McLaren 720S GT3; Track is divided into 19 microsectors (10 straight, 9 corners). All drivers use the same vehicle, track, and game setup. <https://www.sciencedirect.com/science/article/pii/S2451958824000472?via%3Dihub>
      - Our own data (external test set): 10 drivers × 30 laps of the McLaren 720S GT3 at Brands Hatch in ACC v1.10.4, recorded remotely on each driver's own rig (minimum: steering wheel and pedals). Every driver receives an instruction sheet and the car setup file, so software and in-game settings are fixed. Hardware is reported on a driver form. Telemetry is exported with ACC's built-in MoTeC logging and processed with the same MoTeC i2 Pro workspace and export settings as the main dataset, giving the same 19 microsectors and KPIs. Drivers upload the raw MoTeC files and the form to a shared Google Drive folder. These laps are never used for training, feature selection or tuning. Results are reported per driver and pooled. Mixed hardware is a limitation.

  

  - For each microsector the dataset gives its **time**, seven summary statistics (**minimum**, **maximum**, **mean**, **start**, **end**, **change** and **standard deviation**) for each telemetry channel, and eight driver-input KPIs: **brake length, brake duration, trail-braking duration, throttle duration, throttle application speed, throttle release, peak steering value** and **time to peak steering**.
  - Candidate control KPIs: the eight dataset KPIs plus per-microsector statistics of the driver-input channels (maximum and mean brake, maximum and mean throttle, share of the microsector at full throttle, maximum, mean and SD of the absolute steering angle, steering reversal rate, lowest gear). Channels that describe the car's response (speed, accelerations, lane deviation, understeer and oversteer, ABS and traction control activity) are excluded.
  - Cleaning removes in-laps, out-laps, standing starts and invalid laps (including laps whose lap time does not match the sum of their microsector times), plus any lap whose lap time is more than 3 SD from the mean of all laps (|z| \> 3). Applied separately to the external laps.
  - Split: 70/30 train/test by driver, so no driver appears in both sets. The test set is used only for the final surrogate test.

<!-- end list -->

  - Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?zjymVi) used Laguna Seca. This study uses Brands Hatch [(Hojaji et al., 2024)](https://www.zotero.org/google-docs/?hJfFKx). Because the comparison is between two fitness functions on the same  data, it does not depend on using the baseline's track.

## **Training**

  - Clustering: K-Means on the lap times of all valid laps, with k chosen by the Elbow method and Silhouette score. The fastest cluster is the Fast reference. Fast-lap values used by the GA come from training laps only. 

<!-- end list -->

  - Feature selection (training laps only): Using Pearson correlation filter, drop candidate KPIs with |r| \< 0.1 against both microsector time and exit speed. Fit one screening XGBoost with the remaining KPIs, entry speed and microsector index as inputs. Rank KPIs by mean |SHAP| per microsector, normalized and averaged over the two targets and the 19 microsectors, and keep the top 10. The per-microsector SHAP values are also reported.

<!-- end list -->

  - Surrogate: one multi-output XGBoost shared by all microsectors. It maps (selected KPIs, entry speed, microsector index) to (microsector time, exit speed) and is trained on all training laps. Pooling all 19 microsectors in one model trains it on every microsector row (about 15,700 before filtering and splitting) instead of on 19 small per-microsector sets.
  - Hyperparameters tuned by grid search in 10-fold CV grouped by driver (MAE), then refit on all training laps.

## **Optimization**

  - **Baseline problem**: Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?ihZB5a) score each microsector on its own by scaling a baseline time from that microsector's KPIs, so a change in microsector n cannot change the predicted time of microsector n+1.
  - **GA**: the GA of Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?0u3kQo) is reused unchanged, so the fitness function is the only difference from the baseline. Population 120, 200 generations, two-point crossover (0.8), Gaussian mutation (rate 0.15 per gene, SD 0.05), elitism of the two best individuals, tournament size 3. Mutated genes are clipped to the training range. The best fitness per generation is reported to show it levels off before generation  200.
  - **Chromosome**: the 10 selected KPIs for each of the 19 microsectors (190 genes), initialized randomly within the training range of each KPI.
  - **Coupled fitness function**: Fitness = T + λP, with λ = 0.1 taken from Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?AoaHyr) without tuning. P is rebuilt from the penalty description in Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?iyNYrJ), because its formulas and thresholds are not reported. Each candidate is passed through the surrogate model one microsector at a time. Microsector 1 starts from the mean entry speed of the Fast-cluster training laps, and each predicted exit  speed becomes the next microsector's entry speed. T is the sum of the predicted microsector times. The baseline's 90–105% clamp is not used.
  - **Output**: per-microsector KPI  targets, each reported against the Fast-cluster median, for example "microsector 7: hold trail braking 0.2 s longer than the  fast-lap median".

## **Testing**

  - Test set: MAE and R² overall and on Fast-cluster laps.
  - Lap rollout on each test lap: start from the recorded entry speed and feed each predicted exit speed in as the next entry speed. Predicted lap time and boundary speeds are then compared with the recorded ones.
  - External set: MAE, R² and lap rollout, run once.   

<!-- end list -->

  - Fitness comparison: the same GA is run with the coupled fitness function and with a microsector-independent fitness function, in which each microsector's entry speed is fixed at the Fast-cluster training mean for that microsector. Each runs with the same 30 random seeds. The best lap of every run is re-scored by the chained surrogate model. Paired differences are tested with a Wilcoxon signed-rank test and count only if larger than the rollout lap-time error.  

<!-- end list -->

  - Limitations: mixed home hardware in the external set; SHAP explains the model, not causation, and correlated KPIs share credit; lap closure (last exit speed vs first entry speed) is not enforced, and the gap is reported; KPIs with low consistency across a driver's laps (coefficient of variation) are reported.

  

## **Significance of the Study**

This study is expected to benefit the following groups.

**Sim racers.** The study produces per-microsector targets for a driver's own inputs, such as braking, throttle and steering, each expressed relative to the median of the fast laps in that microsector (for example, “microsector 7: hold trail braking 0.2 s longer than the fast-lap median”). Because the fitness function passes the predicted exit speed of each microsector to the next microsector as its entry speed, the targets account for how a change in one corner or straight affects the rest of the lap, and they do not assume an entry speed that the preceding microsector cannot deliver. The method relies only on telemetry that drivers can already export from Assetto Corsa Competizione (ACC). It is also tested on laps recorded by drivers on their own home equipment, which shows whether the targets remain usable outside the dataset the model was built on.

**Coaches and esports teams.** The study reports which driver inputs the model relies on most in each microsector, rather than only across the whole lap. Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?VTZuMX) computed feature importance globally and noted that reliable segment-specific estimation would require larger datasets. This study does not fit separate models for each microsector. It derives per-microsector importance from a single model pooled across all microsectors, which gives coaches and teams a data-driven indication of where on the track a driver may focus practice and which inputs to work on there.

**Researchers.** This study extends the framework of Hojaji et al. [(2026)](https://www.zotero.org/google-docs/?xsWlJD) by replacing its fixed linear formula for estimating microsector times with a trained surrogate model, chained so that the predicted exit speed of each microsector becomes the entry speed of the next. Because the genetic algorithm is kept identical to the baseline, the comparison between the coupled and the microsector-independent fitness isolates the effect of microsector coupling on the optimized lap. The study is built on a publicly available dataset [(Hojaji et al., 2024)](https://www.zotero.org/google-docs/?uCKHzE) released under a CC BY 4.0 license, so other researchers can reproduce and extend it.

  

## **References**

[Himmels, C., Parduzi, A., Fischer, M., & Riener, A. (2023). Towards a common understanding of driving simulator validity. *Adjunct Proceedings of the 15th International Conference on Automotive User Interfaces and Interactive Vehicular Applications (AutomotiveUI ’23 Adjunct)*, 191–196. https://doi.org/10.1145/3581961.3609895 ](https://www.zotero.org/google-docs/?y1RuwS)

[Hojaji, F., Toth, A., & Campbell, M. (2026). Optimizing Sim Racing Performance Using Machine Learning and Evolutionary Algorithms. *Proceedings of the 18th International Conference on Agents and Artificial Intelligence*, 997–1004. https://doi.org/10.5220/0014609600004052 ](https://www.zotero.org/google-docs/?y1RuwS)

[Hojaji, F., Toth, A. J., Joyce, J. M., & Campbell, M. J. (2024). AI-enabled prediction of sim racing performance using telemetry data. *Computers in Human Behavior Reports*, *14*, 100414. https://doi.org/10.1016/j.chbr.2024.100414 ](https://www.zotero.org/google-docs/?y1RuwS)

  
