# Literature Matrix

| Citation Key | Core Algorithm | Constraint Handling | Median Solver Time | Track Adherence | Core Bottleneck |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [[Scheffe2022_SCR]] | SCR (RTI-MPC, single-track + Pacejka) | Restriction (overlapping convex polygons) | ~73 ms (`Fig. 8`) | Guaranteed feasible (`Thm. 2`) | Constraint count from polygonal track; ~2x SL solve time |
| [[Scheffe2022_SCR]] (baseline) | SL | Relaxation (tangent lines + slack + trust region) | ~35 ms (`Fig. 8`) | Can violate nonconvex track constraint (`Fig. 6`) | Trust region prohibitive at standing start (`Sec. VI-B`) |
