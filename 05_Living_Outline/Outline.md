# Thesis Outline — Extending an ML-EA Framework with a Microsector-Chained Surrogate Model for Sim Racing Performance Optimization

Anchor: [[GOAL]] (v0.5). Source of truth for written text: the Google Doc "Thesis TODOs" (snapshot `08_Project_Files/Thesis_TODOs_Doc_2026-10-24.md`). Literature table: [[matrix]].

## Chapter 1 — Introduction
1.1 Background: sim racing as an esport and a measured performance domain
1.2 Problem: Hojaji et al. (2026) score each microsector independently and rank KPIs globally; no fitness carries speed from one microsector to the next
1.3 Objectives (wording pending in the Doc → [[GOAL]] G1–G4)
1.4 Scope and limitations (ACC, McLaren 720S GT3, Brands Hatch; no simulator–real equivalence claim — [[GOAL]] §3)
1.5 Significance: sim racers, coaches and esports teams, researchers (Doc, "Significance of the Study")

## Chapter 2 — Review of Related Literature (Doc tab "literature review")
2.1 Introduction and Scope
2.2 Simulator Validity and Reliability (2.2.1–2.2.4)
2.3 Telemetry-Based Analysis of Driver Performance (2.3.1 stratifying performance, 2.3.2 per-corner coaching, 2.3.3 driver inputs that change lap time)
2.4 The Baseline: Hojaji et al. (2026)
2.5 Physical Interdependence of Microsectors
2.6 Racing Optimizers that Carry the Coupling
2.7 Learned and Chained Surrogates (2.7.1–2.7.4)
2.8 Synthesis and Research Gap (Table 2.1)

## Chapter 3 — Methodology (Doc tab "refined methodology")
3.1 Data Collection and Simulator Reliability: main dataset (Hojaji et al. 2024) and external test set (10 drivers × 30 laps) — G1
3.2 Simulator Validity and Scope; KPI consistency check
3.3 Step 0: Setup and Settings
3.4 Step 1: Preprocessing, microsector segmentation (M = 19), lap filter, driver-grouped 70/30 split, control KPI pool — G1
3.5 Step 2: K-Means stratification on lap time; Fast reference
3.6 Step 3: Pearson screen + TreeSHAP feature selection (K = 10); per-microsector importance — G2
3.7 Step 4: Shared multi-output XGBoost surrogate; grouped CV; test, lap rollout, external test — G2
3.8 Step 5: Hojaji et al.'s GA with the coupled fitness — G3
3.9 Structural limitations of independent evaluation and the coupled vs independent ablation (30 paired seeds, common judge, Wilcoxon) — G4

## Chapter 4 — Results and Discussion
4.1 The cleaned dataset and counts after filtering (S1)
4.2 Surrogate accuracy: grouped CV, test set, lap rollout (S2)
4.3 External test set, per driver and pooled (S3)
4.4 Per-microsector KPI importance (descriptive, with rank stability)
4.5 Ablation: coupled vs independent fitness (S4)
4.6 Optimized targets vs the Fast cluster; the coaching read-out (S5)

## Chapter 5 — Conclusion and Recommendations
5.1 Answers to the objectives
5.2 Limitations (mixed home hardware, SHAP is not causal, lap closure gap, low-consistency KPIs, common judge is the proposed model)
5.3 Future work (optimizer comparison such as DE)
