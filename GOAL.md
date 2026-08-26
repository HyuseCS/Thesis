# GOAL — Thesis Anchor

> Working title (TBD): *A Real-Time C++ Sequential Convex Restriction Trajectory Planner Evaluated in a High-Fidelity Racing Simulator*
>
> This file is the anchor. Every note, experiment, and chapter in this vault must trace back to a numbered goal below. If a task does not serve G1–G4, it is out of scope.
>
> **Status: v0.1 — DRAFT, not yet reviewed by adviser.** This document is expected to change. See §7.

---

## 0. Origin

The thesis builds on [[Scheffe2022_SCR]] (Scheffe, Henneken, Kloock, Alrifaee, *IEEE T-IV* 2022). That paper proposes **Sequential Convex Restriction (SCR)**: convexify the nonconvex race-track constraint by covering the track with **overlapping convex polygons**, so every solution of the convex sub-problem is guaranteed feasible in the original nonconvex problem (`Thm. 2`, `Appendix B`). Its rival, **Sequential Linearization (SL)**, relaxes the constraint instead and can therefore produce trajectories that leave the track (`Fig. 6`).

Reported results, all from the source paper:

| Metric | SL | SCR | Source |
| :--- | :--- | :--- | :--- |
| Lap time, standing start | 11.0 s | 10.1 s (−8.91 %) | `Table I` |
| Lap time, flying lap | 10.0 s | 9.3 s (−7.53 %) | `Table I` |
| Median solver time | ~35 ms | ~73 ms | `Fig. 8` |
| Maximum solver time | ~48 ms | ~87 ms | `Fig. 8` |
| Feasible in nonconvex problem | not guaranteed | guaranteed | `Thm. 2` |

Two facts define the whole thesis:

1. **SCR is better but expensive.** ~73 ms median against a 100 ms sampling time (`Sec. VI`). The real-time margin is ~27 ms.
2. **SCR was never run outside MATLAB simulation.** The authors state real experiments are future work (`Sec. VII`). The implementation is MATLAB R2021a with the commercial solver `cplexqp` (IBM ILOG CPLEX 12.10) on an AMD Ryzen 5 3600 desktop (`Sec. VI`).

The thesis attacks fact 2 first, then fact 1.

---

## 1. Goal Statement

**Port SCR from MATLAB to real-time C++, validate it as a faithful reproduction of the published algorithm, drive a vehicle in Assetto Corsa with it, then extend the algorithm with new parameters that reduce lap time against SL and against unmodified SCR — while keeping the feasibility guarantee that defines SCR.**

The goal decomposes into four sequential goals. Each is a gate: **G(n+1) must not start until G(n) passes its exit criteria.**

---

### G1 — Port: SCR in real-time C++

Reimplement the SCR trajectory planner of [[Scheffe2022_SCR]] in C++, replacing MATLAB and CPLEX.

Scope:
- General Trajectory Program (`Eq. 14`), single-track vehicle model + Pacejka Magic Tire Formula (`Sec. II-A`, `Eqs. 2–3`).
- Track polygon construction, Algorithm 2: `tessellateTrack` → `mergePolygons` → `addOverlaps` (`Sec. V-E2`).
- Track restriction function $R_T$ (`Eq. 28`), acceleration restriction $R_\mathcal{A}$ (`Eq. 27`).
- RTI control loop, Algorithm 1, with $N_\text{RTI} = 1$.
- Terminal constraint $v^{(H_p)} = 0$ (`Eq. 13`) — kept in G1 exactly as published, questioned in G4.

Exit criteria:
- **G1.1** The C++ planner solves the same QP (`Eq. 36`) as the MATLAB reference on the 1:43 Hockenheimring track data from the authors' public repository.
- **G1.2** Median solve time measured and reported on documented hardware. Target: **≤ 73 ms**, the published median. A slower port is a failed port until explained.
- **G1.3** No commercial solver dependency. Free QP solver only.
- **G1.4** Deterministic timing: 99th percentile within 20 % of median, matching the "close to the median" property the authors call desirable (`Sec. VI-B`).

Open decisions (resolve before coding — see [[Roadmap]]):
- QP solver choice: OSQP, HPIPM, qpOASES, or Clarabel.
- Whether Algorithm 2 runs **offline once per track** or **online per timestep**. The paper does not say, and does not time it. **This is the first real research question of the thesis, not an implementation detail.**

---

### G2 — Validate: prove the port is the same algorithm

A port that runs is not a port that is correct. Before any Assetto Corsa work or any novelty, prove equivalence to the published algorithm.

Exit criteria:
- **G2.1 Guarantee holds.** Over a full lap, every planned position $p^{(j)}$ lies inside the true nonconvex track area $T$. Zero violations. This is the property SCR exists for (`Thm. 2`); if the port violates it, the port is wrong.
- **G2.2 Recursive feasibility holds.** The warm-start trajectory of `Thm. 1` / `Eq. 22` is feasible at every timestep. No solver infeasibility over a full lap.
- **G2.3 SL baseline reproduced.** SL (`Eq. 18`) implemented in the same C++ codebase, so all comparisons are same-code, same-solver, same-machine.
- **G2.4 Published trend reproduced.** In the paper's own MATLAB-equivalent scenario, the port reproduces the qualitative results of `Table I` and `Fig. 8`: SCR beats SL on lap time, SCR costs roughly double the solve time of SL.
- **G2.5 Deviation register.** Every place the C++ differs from the paper (solver tolerance, $\varepsilon_A$, $b_\text{max}$, $n_\text{acc}$, polygon count) is written down with its numerical effect. Assumed-equal is not validated.

Note on G2.4: reproducing the *trend* is the criterion, not reproducing 9.3 s. Absolute lap time depends on solver, tolerances, and machine. Claiming exact reproduction would be a fabricated result.

---

### G3 — Deploy: Assetto Corsa as the evaluation environment

Replace the paper's MATLAB simulation with Assetto Corsa, a commercial high-fidelity racing simulator. This directly addresses the "simulation only, hardware is future work" gap of `Sec. VII` — AC is not hardware, but it is an **independent, unmodelled, higher-fidelity plant** that the planner does not control and cannot see inside.

That independence is the scientific value, and also the difficulty. It creates a problem the source paper never had:

> **The plant/model mismatch problem.** The paper's planner predicts with the same single-track model that generates the simulated motion (`Eq. 1`). In Assetto Corsa the true plant is a proprietary tire and suspension model. The planner's internal model becomes an *approximation of a black box*. Model mismatch, not solve time, may turn out to be the dominant error source.

Exit criteria:
- **G3.1 State in.** Read vehicle state (position, velocity, heading, yaw rate) from AC at a documented rate and latency.
- **G3.2 Control out.** Apply steering and throttle/brake to the AC car from the C++ planner.
- **G3.3 Track in.** Extract an AC track centre line and boundaries, and build the polygon set of `Algorithm 2` from it. This is a scale jump: the paper used a 1:43 track ~250 m long with 1090 tessellated polygons merged to 178 (`Fig. 3`). A full-scale AC circuit is 3–7 km. **Constraint count is a function of track length — verify it, do not assume it scales.**
- **G3.4 Model fit.** Identify single-track and Pacejka parameters for the chosen AC car ($m$, $I_z$, $l_f$, $l_r$, $B$, $C$, $D$ per axle, motor curve $C_{m1}, C_{m2}, C_{r0}, C_{r2}$). Report the fit error against AC telemetry.
- **G3.5 Closed loop.** The car completes a full clean lap of one circuit under SCR control, no manual intervention, no off-track excursion.
- **G3.6 Timing budget.** End-to-end loop latency (read → plan → actuate) measured and reported, not just QP solve time. The paper reports only solver time (`Fig. 8`); a closed loop has more.

Fixed for the whole thesis before G3 starts: **one car, one circuit, one AC physics/assist configuration.** Changing any of them invalidates every prior lap time.

Risk, stated plainly: AC has no official trajectory-control API. State reading is a solved problem (shared memory / UDP telemetry). **Writing control input is the hard part and is the single largest schedule risk in this thesis.** G3.2 is the make-or-break task. If it cannot be done, the fallback environment must be chosen early, not late.

---

### G4 — Extend: the novelty

Add parameters to SCR that improve lap time relative to (a) SL and (b) unmodified SCR, in Assetto Corsa, without breaking the feasibility guarantee of `Thm. 2`.

The specific parameters are **deliberately not fixed yet.** They must be chosen from measurement made in G1–G3, not from a guess made today. Choosing the novelty before profiling would be picking an answer before seeing the problem.

Candidate directions already visible in the source paper, kept as a menu:

| Candidate | Paper's own opening | Where |
| :--- | :--- | :--- |
| Adaptive polygon resolution (fewer edges far from the vehicle) | "can be reduced by a coarser representation of the track, i.e., using polygons with fewer sides" — proposed, never quantified | `Sec. VI-B` |
| Less conservative terminal constraint than $v^{(H_p)} = 0$ | Forces a predicted standstill every timestep; conservative by construction | `Eq. 13` |
| Tuning / adapting the merge tolerance $\varepsilon_A$ | Authors call merging "a minor relaxation" and do not bound its effect | `Sec. V-E2b` |
| Tuning the acceleration restriction $b_\text{max} \in (0,1)$ | A free conservatism knob, never swept | `Eq. 27` |
| Faster polygon index lookup $l(\bar p)$ | Complexity never reported | `Sec. V-E1` |
| Parallelising Algorithm 2 | Stated as a sequential loop | `Alg. 2` |

Exit criteria:
- **G4.1** At least one parameter extension is implemented and its effect swept, not just demonstrated at one setting.
- **G4.2** Lap time improves against the G2.3 SL baseline and against unmodified SCR, in the same AC configuration, over repeated laps with variance reported. One fast lap is not a result.
- **G4.3 The guarantee survives.** The extension is shown — by proof against the restriction conditions `Eq. 21`, or by exhaustive measurement — not to break feasibility. **An extension that gains lap time by weakening the restriction is not an improvement to SCR; it is a step back toward SL, and must be reported as such.**
- **G4.4** Real-time capability retained: end-to-end latency below the control period.

---

## 2. Success Criteria — the whole thesis in one table

| ID | Claim to be earned | Measured by | Threshold |
| :--- | :--- | :--- | :--- |
| S1 | SCR runs in real-time C++ without a commercial solver | median QP solve time | ≤ 73 ms, free solver |
| S2 | The port is the published algorithm | track-constraint violations per lap | exactly 0 |
| S3 | SCR controls a car in a high-fidelity simulator | clean unassisted laps completed | ≥ 1, then repeatable |
| S4 | The extension is faster | mean lap time vs SL and vs plain SCR, n laps | improvement > run-to-run std. dev. |
| S5 | The extension is still SCR | feasibility under the extension | guarantee proven or exhaustively unviolated |

---

## 3. Non-Goals

Named so they cannot creep in:

- Physical RC-car or full-scale hardware experiments.
- Opponents, obstacles, or overtaking. The source paper excludes them too (`Sec. VII`).
- Multi-vehicle / networked MPC.
- Beating a human driver or a commercial racing AI.
- Learning-based or end-to-end approaches.
- Being a better AC modder. Interfacing with AC is a **means**, not a contribution. It belongs in an implementation chapter, not the novelty chapter.

---

## 4. Standing Risks

| # | Risk | Hits | Mitigation |
| :--- | :--- | :--- | :--- |
| R1 | No supported way to write control input into AC | G3.2 | Prove input actuation on day one of G3, before any other G3 work. Pick fallback early if it fails. |
| R2 | Plant/model mismatch dominates; the car cannot follow the plan regardless of planner quality | G3.4, G3.5 | Explicit system-identification step with reported fit error. A tracking controller sits between planner and car; keep it fixed and documented so planner comparisons stay fair. |
| R3 | Full-scale track → far more polygons → solve time exceeds real-time | G3.3 | Measure constraint count vs track length early. This risk is also **the strongest motivation for the G4 novelty** — do not treat it purely as a problem. |
| R4 | Free solver is slower than CPLEX, so the port "fails" G1.2 for a reason unrelated to the algorithm | G1.2 | Benchmark ≥ 2 solvers on the same QP before committing. Report solver as a stated variable, not a hidden one. |
| R5 | AC run-to-run variance is larger than the lap-time gain being claimed | G4.2 | Establish the noise floor from repeated identical laps **before** claiming any improvement. |
| R6 | The novelty is chosen too early, from intuition instead of profiling | G4 | G4 stays a menu until G1–G3 data exists. This is deliberate, not indecision. |

---

## 5. Working Directives

Inherited from [[CLAUDE]], restated because they bind this goal:

1. **Zero hallucination.** Every number in this vault carries a source, e.g. `Scheffe2022_SCR.pdf, Fig. 8`. Numbers from our own experiments carry the run that produced them.
2. **Computational focus.** Never "X is faster". Always how much faster, on what hardware, at what constraint count.
3. **Gates are gates.** No novelty before validation. An unvalidated port producing a fast lap time proves nothing.
4. **Report what happened.** A failed port, a failed AC interface, or an extension that loses lap time are all publishable findings if reported honestly. A quietly dropped negative result is not.

---

## 6. Still Undecided

To be filled in as the work starts. Each blocks the roadmap step that needs it.

- [ ] QP solver — blocks G1
- [ ] Algorithm 2 offline vs online — blocks G1
- [ ] AC state-read interface — blocks G3.1
- [ ] AC control-write interface — blocks G3.2, **highest risk**
- [ ] AC car and circuit, fixed for the thesis — blocks G3
- [ ] Tracking controller between planned trajectory and AC inputs — blocks G3.5
- [ ] Development/benchmark hardware, documented — blocks every timing number
- [ ] The novelty parameter(s) — blocks G4, intentionally deferred

---

## 7. Revision Log

This goal is provisional. It will change as the adviser reviews it and as G1–G3 produce data. That is expected, not failure — but changes must be **recorded**, not silently applied, or the thesis loses its own history.

**How to revise:**
1. Bump the version in the header (v0.1 → v0.2).
2. Add a row below: what changed, why, who asked.
3. If a gate (G1–G4), a success criterion (S1–S5), or a non-goal changes, say so explicitly in the row. Those are the load-bearing parts.
4. Never delete a superseded goal. Strike it through and keep it. A dropped direction is evidence of how the work developed, and advisers ask about it.

| Version | Date | Changed | Reason | Source |
| :--- | :--- | :--- | :--- | :--- |
| v0.1 | 2026-08-26 | Initial draft: G1 port → G2 validate → G3 Assetto Corsa → G4 novelty | First formalization from [[Scheffe2022_SCR]] and student's stated direction | Student |

**Open questions to put to the adviser** (these are the parts most likely to move):

- Is Assetto Corsa an acceptable evaluation environment for the degree, or is a hardware/ROS testbed expected? This decides G3 entirely.
- Is "port + validate + extend" enough novelty, or must the contribution be purely algorithmic? This decides whether G1–G3 are contribution or preamble.
- Is the G4 novelty allowed to stay undecided until G3 data exists (§4 R6), or must it be committed up front for the proposal?
- Scope of comparison: is SL the only required baseline, or must other planners be included?
- Is a negative result on G4 acceptable?
