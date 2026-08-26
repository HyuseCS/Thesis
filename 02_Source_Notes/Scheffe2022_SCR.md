# Scheffe2022_SCR — Sequential Convex Programming Methods for Real-time Optimal Trajectory Planning in Autonomous Vehicle Racing

**1. Provenance & Objective**
- Citation: P. Scheffe, T. M. Henneken, M. Kloock, B. Alrifaee, *IEEE Transactions on Intelligent Vehicles*, 2022. DOI: 10.1109/TIV.2022.3168130. `Scheffe2022_SCR.pdf`
- Core Goal: A real-time-capable MPC trajectory planner for autonomous racing that convexifies nonconvex track constraints by **restriction** (SCR) instead of **relaxation** (SL), so every solution is guaranteed feasible in the original nonconvex problem. (`Sec. I-C`)
- Code/data: GitHub `embedded-software-laboratory/sequential-convex-programming`; Code Ocean capsule 6818033. (`Supplementary Material`)

**2. Methodology Breakdown**
- Vehicle Model Used: kinetic **single-track** model + Pacejka Magic Tire Formula; states $p, v, \phi, \omega$, inputs steering $\delta$ and motor duty $\tau$. Also a **linear** point-mass comparison model with velocity-dependent half-ellipse acceleration limits. (`Sec. II-A`, Eqs. 2–6)
- Track Convexification Method: track area $T$ covered by union of $N_\text{polygons}$ overlapping convex polygons; restriction function $R_T(\bar p)=P_{l(\bar p)}$ proven valid in `Appendix B`. Built by **Algorithm 2**: `tessellateTrack` → `mergePolygons` → `addOverlaps`. (`Sec. V-E`)
- Optimization Solver: `cplexqp`, IBM ILOG CPLEX 12.10, MATLAB R2021a. Real-time iteration (RTI) SCP with $N_\text{RTI}=1$, $\Delta t = 0.1$ s. (`Sec. VI`, `Algorithm 1`)
- Benchmark hardware: AMD Ryzen 5 3600 4.2 GHz hexacore, 16 GB RAM, Windows 10. (`Sec. VI`)
- Testbed: 1:43-scaled Hockenheimring, **simulation only**. (`Sec. VI`)

```mermaid
flowchart LR
    A["Track boundaries T_L, T_R"] --> B["Tessellation<br/>1090 polygons"]
    B --> C["Merging<br/>178 polygons, eps_A = 0.0006 m^2"]
    C --> D["Overlapping<br/>178 enlarged polygons"]
    D --> E["Affine constraint set T_SCR"]
    E --> F["QP solved by cplexqp"]
```
*(counts from `Fig. 3`, `Sec. V-E2`)*

**3. Key Findings & Performance Metrics**
| Metric | SL | SCR | Source |
| :--- | :--- | :--- | :--- |
| Lap time, standing start | 11.0 s | 10.1 s (−8.91 %) | `Table I` |
| Lap time, flying lap | 10.0 s | 9.3 s (−7.53 %) | `Table I` |
| Median solver time | ~35 ms | ~73 ms | `Fig. 8` |
| 99th percentile | ~43 ms | ~83 ms | `Fig. 8` |
| Maximum | ~48 ms | ~87 ms | `Fig. 8` |
| Feasibility in nonconvex problem | not guaranteed | guaranteed | `Sec. I-C`, `Thm. 2` |

- SCR costs **approximately double** the computation time of SL, "mainly determined by the optimization time, which grows with the number of constraints". (`Sec. VI-B`, `Fig. 8`)
- Max and 99th percentile stay close to the median → predictable timing, a desired real-time property. (`Sec. VI-B`)
- Raising SL to $N_\text{RTI}=50$ still gives slightly worse lap times than **one** SCR iteration, at up to **ten times** the computation time. (`Sec. VI-B`)
- Recursive feasibility proven under terminal constraint $v^{(H_p)}=0$. (`Thm. 1`, `Appendix A`)

**4. Critique & Optimization Vectors**
- **Simulation only.** No hardware validation; authors defer real experiments in the Cyber-Physical Mobility Lab to future work. Flag as a hardware-implementation bottleneck. (`Sec. VII`)
- **Constraint bloat.** The polygonal representation puts more constraints in the QP than SL's tangent lines; solver time scales with that count. Authors note it "can be reduced by a coarser representation of the track, i.e., using polygons with fewer sides" but do not quantify the lap-time/solve-time trade-off curve. (`Sec. VI-B`)
- **Offline vs online geometry.** Algorithm 2 (tessellate → merge → overlap) is stated as a sequential, iterative construction. Merging repeats until no polygons can be merged — the cost of this step and whether it is precomputed once per track or recomputed is not reported. Optimization vector: parallelize or precompute, and quantify. (`Sec. V-E2`, `Algorithm 2`)
- **Index function $l(\bar p)$** does a nearest/most-forward search over polygons each timestep; complexity not reported. Candidate for spatial indexing. (`Sec. V-E1`, Eq. 16 analogue)
- **Merging is a relaxation.** $\Delta A(P_i,P_{i+1}) \le \varepsilon_A$ admits a small non-track area — the restriction guarantee is therefore $\varepsilon_A$-approximate. Authors call it "a minor relaxation" without bounding its effect. (`Sec. V-E2b`)
- **Terminal constraint $v^{(H_p)}=0$** forces a predicted standstill, which is conservative and costs progress; a less restrictive terminal set is an open vector. (`Eq. 13`)
- **No obstacles/opponents evaluated.** Stated as extendable via linearization but not benchmarked. (`Sec. VII`)
- **Single solver, single machine.** CPLEX-only; no comparison to OSQP/HPIPM or embedded targets. Real-time claim is tied to a desktop Ryzen 5. (`Sec. VI`)
