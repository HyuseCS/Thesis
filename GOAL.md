# GOAL — Thesis Anchor

> Working title (TBD): *Micro-Sector Feature Importance and Evolutionary Lap Optimization for Human Sim-Racing Performance*
>
> This file is the anchor. Every note, experiment, and chapter in this vault must trace back to a numbered goal below. If a task does not serve G1–G4, it is out of scope.
>
> **Status: v0.2 — REBASED.** This supersedes the SCR-port goal of v0.1. The old gates are kept, struck through, in §8. Sequential Convex Restriction is now a Related Literature item, not a build target.

---

## 0. Origin

The base document is `01_Corpus/thesis new base.md`. Everything in this section is drawn from it; papers marked *(not yet ingested)* have no source note in this vault yet, so their claims are carried at the base document's word and must be re-verified on ingestion (AGENTS.md §1).

**Literature position.** Most sim-racing optimization work targets autonomous racing agents; integrated optimization frameworks for *human* drivers are comparatively rare (Hojaji et al. 2026; Kabzan et al. 2019; Lee et al. 2025 — *not yet ingested*). Trajectory optimization, RL control, and racing-line generation are framed as autonomous control problems in F1TENTH, TORCS, and full-size racecars (Evans, Engelbrecht, and Jordaan 2023; Garlick and Bradley 2021; Ghignone, Baumann, and Magno 2022; Samak, Samak, and Kandhasamy 2021 — *not yet ingested*). Those approaches give limited insight for improving *human* performance (Hojaji et al. 2026).

**The lineage this thesis extends.**

| Work | What it did | Status in vault |
| :--- | :--- | :--- |
| Hojaji, Toth, Campbell 2023 | ML on human sim-racing telemetry: k-means performance levels, XGBoost classification, 10-feature ranking (speed, RPM, g_lat, throttle, steer, lane deviation …) | Ingested — [[Hojaji2023_TelemetryML]] |
| Hojaji et al. 2024 | AI analysis of driving behaviour from telemetry | Not yet ingested |
| Hojaji, Toth, Campbell 2026 | ML feature importance + evolutionary algorithm to optimize sector-level performance indicators and generate faster, smoother, more stable idealized laps for coaching | Not yet ingested |

**Problem statement.** Hojaji et al. (2026) computed feature importance **globally**, not at the **sector level**, because reliable segment-specific estimation would need a larger dataset. This leaves open which circuit segments most strongly influence optimal lap performance (`thesis new base.md`, Problem statement). The same gap is named one paper earlier: *"It would also be possible to focus on a specific segment rather than the data for the full lap to estimate the lap time. We defer this work as the future work."* ([[Hojaji2023_TelemetryML]], `Sec. 3.2`).

That open question is this thesis.

---

## 1. Goal Statement

**Build a micro-sector telemetry dataset from a racing simulator, model how sequential track segments influence each other and where speed must be traded between them, then drive an evolutionary optimizer with that sector-level importance to produce faster idealized laps — validated against human baseline telemetry.**

The three objectives of the base document map to G1–G3. G4 is the validation the base document attaches to objective 3, promoted to its own gate because a generated lap that no human could drive is not a result.

Each gate is a gate: **G(n+1) must not start until G(n) passes its exit criteria.**

---

### G1 — Dataset: micro-sector telemetry

*Base objective 1: "construct a micro-sector telemetry dataset by extracting and processing sequential driving data from a racing simulator environment."*

Exit criteria:
- **G1.1 Segmentation defined.** The rule that splits the track into micro-sectors is written down and reproducible: boundary criterion, sector count, and how corners versus straights are handled. Two people running the rule must get the same sectors.
- **G1.2 Sequence preserved.** Each lap is a *sequence* of micro-sector records, with entry/exit state (at minimum entry speed, exit speed, min speed) carried per sector. Order is data, not metadata — G2 cannot measure interdependency without it.
- **G1.3 Scale and balance reported.** Number of laps, drivers, and sectors; performance-class counts. [[Hojaji2023_TelemetryML]] carried 475 FAST against 91 SLOW laps (`Table 2`) and never addressed it. Ours is reported before any model is trained.
- **G1.4 Cleaning documented with counts.** Invalid/pit/outlier laps removed, with before-and-after counts and the exact threshold, per [[Hojaji2023_TelemetryML]] `Sec. 2.2`.
- **G1.5 Pipeline is in the repo.** Extraction and processing run from committed scripts. No opaque manual step in proprietary tooling — the MoTec i2 Pro math-channel opacity is a stated critique of the prior work, and repeating it would inherit the flaw.

Open decisions (resolve before collecting — see §6): simulator, telemetry source, car and circuit, micro-sector definition.

---

### G2 — Model: sector importance and corner interdependency

*Base objective 2: "develop a predictive machine learning model that quantifies corner interdependencies and identifies optimal speed-tradeoffs across sequential track sectors."*

Exit criteria:
- **G2.1 Importance with uncertainty.** Sector-level feature importance is estimated with cross-validation and reported with spread, plus per-class precision/recall. A single 70/30 split and one headline accuracy number (the prior work's only classification result, `Sec. 3.2`) is not enough evidence at sector granularity.
- **G2.2 Interdependency quantified.** The effect of sector *i* on sector *i+1* (and beyond) is reported as a measured effect size with its uncertainty, not asserted. Name the measure before running it.
- **G2.3 Beats the global baseline.** A lap-level (global) importance model is trained on the same data and compared against the sector-level model. This comparison *is* the gap Hojaji et al. (2026) left open; without it the thesis has no claim.
- **G2.4 Data sufficiency answered.** The prior work's stated reason for skipping sector-level estimation was dataset size. Report a learning curve: how many laps per sector are needed before importance estimates stabilize. A negative answer here is a publishable finding.
- **G2.5 Importance is not causality.** Any claim that a sector "causes" lap-time loss states what supports it — correlation, ablation, or intervention — and does not overreach.

---

### G3 — Optimize: evolutionary algorithm driven by sector importance

*Base objective 3, part 1: "optimize overall lap-time performance by integrating the sector-importance model with an evolutionary algorithm."*

Exit criteria:
- **G3.1 Integration is real.** Sector importance enters the search explicitly (objective terms, weighting, or search-space shaping) and where it enters is documented.
- **G3.2 Feasibility defined up front.** The bound that keeps a generated lap physically attainable is stated *before* optimization runs, and every reported lap satisfies it. An optimizer with no bound will return an impossible lap and call it optimal.
- **G3.3 Ablation, not a demo.** Three arms on the same data: EA + sector importance, EA + global importance, EA alone. One configuration producing one fast lap is not a result.
- **G3.4 Cost reported.** Population, generations, wall-clock time, and hardware. [[Hojaji2023_TelemetryML]] reports no computational cost at all; this vault does not repeat that (AGENTS.md §2).

---

### G4 — Validate against human baseline telemetry

*Base objective 3, part 2: "validating the generated racing lines against human baseline telemetry."*

Exit criteria:
- **G4.1 Baseline fixed first.** The human baseline is defined before optimization results exist: which laps, which drivers, which summary statistic, and the run-to-run spread. Improvement is claimed against that spread, not against a single best lap.
- **G4.2 Improvement measured.** Optimized lap time versus the baseline, with variance. An improvement smaller than the human lap-to-lap standard deviation is not an improvement.
- **G4.3 Attainability shown.** The generated line stays within track limits and within the vehicle behaviour actually observed in the telemetry. A line the data never demonstrates is a claim about a car, not about a driver.
- **G4.4 Coaching read-out.** The result is expressed as which micro-sectors carry the available time — the practical output the base document points at. A number with no sector attached does not help a driver.

---

## 2. Success Criteria — the whole thesis in one table

| ID | Claim to be earned | Measured by | Threshold |
| :--- | :--- | :--- | :--- |
| S1 | A reproducible micro-sector telemetry dataset exists | laps, drivers, sectors, class balance, cleaning counts | all reported; pipeline reruns from committed scripts |
| S2 | Sector-level importance is estimable from our data | stability of importance under cross-validation | spread reported; stabilization point identified |
| S3 | Sector-level beats lap-level importance | model comparison on the same data (G2.3) | sector model better on the stated metric, or the negative result reported |
| S4 | Corner interdependency is measurable | effect size of sector *i* on sector *i+1* | effect reported with uncertainty |
| S5 | Importance-guided EA produces a faster attainable lap | optimized lap time vs human baseline, n runs | gain > baseline standard deviation, and feasible under G3.2 |

---

## 3. Non-Goals

Named so they cannot creep in:

- Building an autonomous racing agent or a real-time onboard controller.
- Porting, reimplementing, or optimizing SCR, SL, or any MPC planner. SCR is Related Literature (§0, [[Scheffe2022_SCR]]), not a deliverable.
- Real-time execution. This work is offline analysis and offline optimization.
- Physical hardware, RC cars, or a driving rig study.
- Opponents, traffic, overtaking, race strategy, tyre wear, fuel.
- Beating a commercial racing AI or a professional driver.
- Simulator modding as a contribution. Telemetry extraction is a means; it belongs in an implementation chapter.

---

## 4. Standing Risks

| # | Risk | Hits | Mitigation |
| :--- | :--- | :--- | :--- |
| R1 | Not enough laps for stable sector-level importance — the exact reason the prior work stopped here | G2.1, G2.4 | Learning curve early, before the full model is built. If the data cannot support it, that answer is the finding — report it, do not pad the dataset. |
| R2 | Results depend on an arbitrary micro-sector definition | G1.1, G2.3 | Sweep granularity (coarse → fine) and show which conclusions survive. |
| R3 | Confounds: mixed cars, setups, and unknown drivers make importance encode the car, not the driver | G1.3, G2.2 | Fix one car and one circuit for the whole thesis. Record driver identity or accept and state the pooling. |
| R4 | The EA returns a lap no human could drive | G3.2, G4.3 | Feasibility bound defined before the first run, not fitted afterwards. |
| R5 | Feature importance read as causality | G2.5 | Ablation or intervention before any causal wording. |
| R6 | The Hojaji 2026 method cannot be reproduced as a comparison baseline (2023 released no code) | G2.3, G3.3 | Check for released code on ingestion. If absent, the baseline is our own global-importance model, and the difference from their exact method is stated. |
| R7 | The base document's key papers (2024, 2026, and the autonomous-racing set) are not yet in the vault | §0, all of Chapter 2 | Ingest them before any claim rests on them. Until then they are marked *not yet ingested*. |

---

## 5. Working Directives

Inherited from [[AGENTS]], restated because they bind this goal:

1. **Zero hallucination.** Every number carries a source — a paper and its location, or the script and run that produced it.
2. **Report the cost.** Dataset size, model, hyperparameters, hardware, and runtime accompany every result. "The model performs well" is not a finding.
3. **Gates are gates.** No optimization before the model is validated; no improvement claim before the baseline spread is known.
4. **Report what happened.** "Sector-level importance is not estimable from a dataset this size" is a real answer to the open question, and it is publishable. A quietly dropped negative result is not.

---

## 6. Still Undecided

Each blocks the step that needs it.

- [ ] Simulator (Assetto Corsa / ACC / iRacing / other) — blocks G1
- [ ] Telemetry source: our own recorded laps, or public repositories as in [[Hojaji2023_TelemetryML]] `Sec. 2.1` — blocks G1
- [ ] Car and circuit, fixed for the thesis — blocks G1, G4
- [ ] Micro-sector definition and count — blocks G1.1
- [ ] Model family for sector importance — blocks G2
- [ ] Evolutionary algorithm: representation, operators, library — blocks G3
- [ ] Human baseline set and its statistic — blocks G4.1
- [ ] Hardware for every reported runtime — blocks G3.4

---

## 7. Revision Log

This goal is provisional. Changes are **recorded**, not silently applied.

**How to revise:**
1. Bump the version in the header.
2. Add a row below: what changed, why, who asked.
3. If a gate, a success criterion, or a non-goal changes, say so explicitly in the row.
4. Never delete a superseded goal. Strike it through and keep it (see §8).

| Version | Date | Changed | Reason | Source |
| :--- | :--- | :--- | :--- | :--- |
| v0.1 | 2026-08-26 | Initial draft: G1 port SCR to C++ → G2 validate → G3 Assetto Corsa → G4 novelty | First formalization from [[Scheffe2022_SCR]] | Student |
| v0.2 | 2026-09-11 | **Full rebase.** Topic changed from porting SCR to micro-sector telemetry ML + evolutionary lap optimization for human drivers. All gates G1–G4 replaced, all success criteria S1–S5 replaced, non-goals rewritten (SCR moved to Related Literature). v0.1 gates struck through in §8. | New base document `01_Corpus/thesis new base.md` | Student |

**Open questions for the adviser** (the v0.1 set is void — it was SCR/Assetto-Corsa specific):

1. Is the micro-sector extension of Hojaji et al. (2026) enough novelty for the degree, or must the optimization method itself be new?
2. Must the generated racing line be validated on a live driver, or is validation against recorded human baseline telemetry sufficient?
3. Is public-repository telemetry (unknown drivers and setups, as in the 2023 paper) acceptable data, or must laps be collected under controlled conditions?
4. How many circuits are required — one, as in the prior work, or must generalization across tracks be shown?
5. Is a negative result on G2.4 (dataset too small for stable sector-level importance) an acceptable thesis outcome?

---

## 8. Superseded — v0.1 Gates (SCR port)

Kept for history. **None of this is in scope.** [[Scheffe2022_SCR]] remains a valid source note and a Related Literature entry.

- ~~**G1 — Port:** reimplement the SCR trajectory planner in real-time C++, replacing MATLAB and CPLEX; median solve time ≤ 73 ms with a free QP solver.~~
- ~~**G2 — Validate:** prove the C++ port is the published algorithm; zero track-constraint violations, recursive feasibility, SL baseline in the same codebase.~~
- ~~**G3 — Deploy:** drive a car in Assetto Corsa under SCR control; state read, control write, track polygon extraction, vehicle system identification, closed-loop lap.~~
- ~~**G4 — Extend:** add parameters to SCR that improve lap time against SL and against unmodified SCR without breaking the feasibility guarantee of `Thm. 2`.~~

Reason dropped: the thesis was rebased on `01_Corpus/thesis new base.md` (2026-09-11), which targets human driver performance, not autonomous trajectory planning.
