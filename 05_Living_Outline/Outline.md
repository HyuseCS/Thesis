# Thesis Outline — Micro-Sector Telemetry Analysis for Sim-Racing Lap Optimization

Anchor: [[GOAL]] (v0.2). Base document: `01_Corpus/thesis new base.md`. Literature table: [[matrix]].

## Chapter 1 — Introduction
1.1 Background: sim racing as a measured performance domain
1.2 Problem: sector-level feature importance is unresolved — Hojaji et al. (2026) computed importance globally because segment-specific estimation needs more data
1.3 Objectives (three, from the base document → [[GOAL]] G1–G4)
1.4 Scope and limitations (one simulator, one car, one circuit — [[GOAL]] §3, §6)
1.5 Significance: driver coaching, not autonomous control

## Chapter 2 — Review of Related Literature
2.1 Autonomous racing optimization
  - Trajectory optimization and MPC: [[Scheffe2022_SCR]], Kabzan et al. 2019 *(not yet ingested)*
  - RL and learned control: [[Evans2023_TAL]], [[Ghignone2023_TCDriver]], [[Samak2021_HybridImitationRL]], Lee et al. 2025 *(not yet ingested)*
  - ML racing-line generation: [[Garlick2021_MLTrajectory]]
  - Synthesis: what this body of work optimizes, and why it transfers poorly to human drivers
2.2 Telemetry analysis of human drivers
  - [[Hojaji2023_TelemetryML]], Hojaji et al. 2024 *(not yet ingested)*
2.3 ML + evolutionary optimization for sim-racing performance
  - Hojaji et al. 2026 *(not yet ingested)* — the direct predecessor
2.4 Track segmentation and sector-level analysis
2.5 Synthesis and the gap — see [[matrix]]

## Chapter 3 — Methodology
3.1 Simulator, car, circuit, and telemetry acquisition (G1)
3.2 Micro-sector definition and the segmentation rule (G1.1)
3.3 Dataset construction, cleaning, and class balance (G1.3–G1.5)
3.4 Sector-importance model and corner-interdependency measure (G2)
3.5 Evolutionary lap optimizer and the feasibility bound (G3)
3.6 Validation design against human baseline telemetry (G4)

## Chapter 4 — Results and Discussion
4.1 The micro-sector dataset
4.2 Sector-level importance vs global importance (G2.3) and data sufficiency (G2.4)
4.3 Corner interdependency and speed trade-offs
4.4 Optimizer ablation: sector-guided vs global-guided vs unguided (G3.3)
4.5 Validation against the human baseline (G4)
4.6 Which micro-sectors carry the available time — the coaching read-out

## Chapter 5 — Conclusion and Recommendations
5.1 Answers to the three objectives
5.2 Limitations
5.3 Future work
