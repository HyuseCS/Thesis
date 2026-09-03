# Literature Matrix

| Citation Key | Core Algorithm | Constraint Handling | Median Solver Time | Track Adherence | Core Bottleneck |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [[Scheffe2022_SCR]] | SCR (RTI-MPC, single-track + Pacejka) | Restriction (overlapping convex polygons) | ~73 ms (`Fig. 8`) | Guaranteed feasible (`Thm. 2`) | Constraint count from polygonal track; ~2x SL solve time |
| [[Scheffe2022_SCR]] (baseline) | SL | Relaxation (tangent lines + slack + trust region) | ~35 ms (`Fig. 8`) | Can violate nonconvex track constraint (`Fig. 6`) | Trust region prohibitive at standing start (`Sec. VI-B`) |
| [[Hojaji2023_TelemetryML]] | k-means clustering + XGBoost classification of human sim-racing telemetry (no planner/solver) | n/a — no optimization; data-driven feature ranking (`Sec. 3.2`) | not reported (offline analysis, no hardware/timing given) | n/a — human laps, lane deviation is a ranked feature (`Fig. 3`) | Zero computational profiling; single 70/30 split, class imbalance 475 FAST vs 91 SLOW (`Table 2`) |
