# Is the proposal a real research gap?

Assessment date: 2026-09-25. Five searches ran in parallel, each from a different angle (see "How this was searched" at the end).
Access levels: **[full]** means full text was read. **[full*]** means full text was read through a summarizing fetch tool, so check every quote against the PDF before citing it. **[abstract]** and **[title]** mean only the abstract or title was seen.

## Verdict: the gap is real, but narrower than the current draft states

No published work does what the proposal does. That means all three of these together:

1. A **learned** surrogate trained on human telemetry that **chains microsectors**, feeding v_exit of microsector n in as v_entry of microsector n+1, inside the fitness function.
2. **Driver KPIs** as the decision variables. Prior work optimizes racing-line geometry or car setup instead.
3. An **ablation** comparing a coupled fitness against a microsector-independent fitness.

Microsector-boundary feature selection (KPIs of n predicting what happens in n+1) was not found in any racing paper either.

Three parts of the proposal are **not** new on their own. The thesis should not claim them:

| Idea | Why it is not new by itself |
|---|---|
| Speed coupling between neighbouring track sections | Standard in physics-based lap-time simulation (forward/backward speed integration; Kapania 2016 etc., already in A1). Also used with GA/CMA-ES over track segments (Klapálek 2024, 2026). |
| "Chained ML surrogate + evolutionary/Bayesian optimizer" as a method | Established in multistage manufacturing and process control, and in UQ (Geiger 2023; Kiroirwal 2026; Astudillo & Frazier 2021; Chen 2004). |
| Per-segment ML model of segment time from sim telemetry | Satujoda & Huggins 2026 (Assetto Corsa, LightGBM, 50 segments). |
| Noticing that a speed deficit is carried over from the previous corner | Nunes et al. 2026 uses it as a rule-based coaching diagnosis. |

**Suggested novelty statement:**
> To our knowledge, this is the first work to replace a microsector-independent fitness with a learned, microsector-chained surrogate that propagates boundary speed from human telemetry, and to optimize driver KPIs through it, evaluated by ablation against the independent formulation.

Frame the surrogate chain as an *application and adaptation* of known function-network / multistage-surrogate ideas to sim racing. Do not present it as a new optimization method: an EC or ML examiner would reject that claim.

## What Hojaji et al. (2026) actually says (baseline) [full*]
Source: https://www.scitepress.org/Papers/2026/146096/146096.pdf. Check page numbers before citing.
- Chromosome: "Each chromosome encodes an entire lap as a sequence of 20 sectors (10 corner-dominant and 10 straight-dominant segments), with each sector represented by a vector of scaled KPI values"
- Fitness: "Fitness = T + λ ⋅ P where T is the predicted lap time obtained from the sector-based surrogate model, P is the aggregated penalty term, and λ = 0.1"
- Microsector time: "For each sector, the algorithm retrieves a baseline sector time derived from fast human laps and adjusts it according to the individual's KPI values. The adjustment is implemented using a simple linear model in which the deviation of the sector's KPI vector from the neutral midpoint (0.5 after min–max scaling) produces a proportional time gain or loss." Each time is clamped to 90–105% of its baseline.
- Coupling between microsectors is limited to a penalty: "Penalties are applied when individuals exhibit sudden KPI transitions between consecutive sectors, unusually large gradients within a single sector, or values that exceed predefined physical thresholds…"
- The paper gives GA settings but no reason for choosing a GA, and it never mentions DE.
- Future work (verbatim): "Future work should include multi-circuit and multi-vehicle datasets … Another promising direction is the development of real-time adaptive ML–EA systems capable of providing dynamic coaching feedback…" It does not announce coupling, DE or a learned surrogate.

**Implications**
- Hojaji already calls their linear scaler a "surrogate". Always call yours a *learned, microsector-chained* surrogate.
- Their KPI-transition penalty is a weak, statistical form of coupling. The independent arm of your ablation should **keep that penalty**, otherwise a reviewer will say you compared against a straw man.
- Hojaji says "sector" for what you call a microsector. Map the terms once in the thesis.

## Closest papers and how the proposal differs

### Sim racing and coaching
1. **Satujoda, S.S. & Huggins, K. (2026).** Staged GT3 Setup Optimization with Setup-Conditioned Telemetry Response Modeling in Simulation. *Vehicles* 8(7):146. https://www.mdpi.com/2624-8921/8/7/146 (open access) [full*, re-checked by me]
   - LightGBM predicts per-segment time and response metrics from setup parameters. Summing segments reconstructs lap time: "reconstructed held-out file-level lap time with 0.223 s mean absolute error".
   - Segment rows use "setup parameters, phase/context identifiers, and track-position segment information". Entry speed and previous-segment state are not mentioned.
   - The model is not the optimizer's fitness: "Telemetry-derived quantities were not used to generate the winning setup".
   - **How the proposal differs:** it chains segments, uses driver KPIs rather than setup, and puts the model inside DE. **This is the paper a reviewer is most likely to raise. Cite it and set yourself apart from it.**
2. **Nunes, T., Medeiros, M., Silva, M., Bittencourt, J.C.N., Costa, D.G. & Silva, I. (2026).** Explaining Driver Behavior in Sim Racing with Shannon Entropy and LLM Feedback. *Entropy* 28(9):960. https://www.mdpi.com/1099-4300/28/9/960 [full*, re-checked by me]
   - Uses iRacing, with corner-aligned sectors compared against a proficiency-matched reference driver. Section 4.2 names "a speed deficit carried over from the previous corner".
   - Everything is rule-based: "A deterministic, physics-informed heuristic layer then identifies kinematic performance gaps". There is no learned model and no optimizer.
   - **How the proposal differs:** it turns this heuristic into a learned model and optimizes through it. Claim to be first to *model and optimize* the coupling, not first to *recognize* it.
3. **Bae et al. (2025).** Data-Driven Driver Training via Counterfactual and Language-Based Guidance in Racing Scenarios. *IEEE Access* 13:170181–170199. doi:10.1109/ACCESS.2025.3615128 [abstract]
   - A per-corner skill classifier, with SHAP counterfactuals toward the "expert" class and an LLM producing feedback. The abstract suggests corners are handled independently.
   - **Update 2026-09-26 (fas read the full text):** its "Strategic Features" include ENTRY max velocity, EXIT max velocity and ENTRY min velocity. These are features of the *same* corner in a per-corner classifier. Nothing indicates that one corner's exit is carried into the next corner's entry.
   - **Consequence:** do not claim novelty for using entry or exit speed as features. What remains distinct is treating entry speed as an *inherited state* (a covariate fixed by microsector n−1, never a gene) and propagating v_exit,n into v_entry,n+1 inside the fitness.
   - **Not a flaw in their setting (fas, 2026-09-26):** Bae's advice is executed by a real driver on track, so physics enforces the coupling. Their method does not need to model it. The contrast to draw: in Hojaji's setup and in this thesis, the optimized lap exists only inside the fitness model and is never driven, so the fitness itself must carry the coupling. At most, note that Bae's advice does not estimate its cost at the previous corner.
4. **Hojaji et al. (2024).** AI-enabled prediction of sim racing performance using telemetry data. *Computers in Human Behavior Reports* 14:100414. https://www.sciencedirect.com/science/article/pii/S2451958824000472 [abstract + partial]
   - ACC at Brands Hatch, with the lap already split into "19 segments: 10 straights and 9 turns". Prediction only; no optimization.
5. **Kaufman et al. (TRI, 2024).** Learning Racing From an AI Coach. arXiv:2401.04206 [full*]
   - Per-corner instructions, with the ideal line coming from an RL agent. Inter-corner coupling is not modelled explicitly.
6. **von Schleinitz et al. (2022).** Race Driver Evaluation at a Driving Simulator using a physical Model and a Machine Learning Approach. arXiv:2201.12939 [full*]
   - Uses an LSTM surrogate for driver evaluation. It explicitly admits: "the models compute each data point isolated from its temporal surrounding. Dynamic effects due to changed accelerations from the optimised states are not respected". **This supports your gap.**
7. **Commercial coaches** (Hotlap.ai, trophi.ai, Track Titan, Coach Dave Delta) [vendor pages]
   - They grade each corner against a reference lap. None documents propagation between corners. They are closed products, so say "no documented coupling", not "no coupling".

### Evolutionary racing-line work (coupling through physics or a simulator, not a learned model)
8. **Cardamone, Loiacono, Lanzi & Bardelli (2010).** Searching for the optimal racing line using genetic algorithms. IEEE CIG. [full*]
   - A GA evolves a weight per track section, and fitness is a full TORCS simulator lap.
9. **Botta, Gautieri, Loiacono & Lanzi (2012).** Evolving the optimal racing line in a high-end racing game. IEEE CIG. [full*]
   - Compares a cheap estimated fitness (Simplix's physics lap-time estimator) with full simulation inside an EA. **This is the precedent for a surrogate fitness in a racing EA.** The estimate was physics-based, scored the whole line, and performed worse.
10. **Klapálek et al. (2024).** Study of Track Segmentation for Lap Time Optimization. SCITEPRESS. https://www.scitepress.org/Papers/2024/127286/127286.pdf [full*]. Also **Klapálek et al. (2026)**, *Robotics and Autonomous Systems* [abstract].
    - GA and CMA-ES over track segments, with boundary speed propagated by a forward/backward physics speed profile. **A reviewer will say "segment coupling is standard". Your answer is that here the coupling is learned from human telemetry and the decision variables are driver KPIs.**
11. **Nam et al. (2026).** Track-Centric Iterative Learning for Global Trajectory Optimization in Autonomous Racing. IEEE RA-L, arXiv:2601.21027 [full*]
    - A GP lap-time surrogate searched with Bayesian optimization, scoring the whole lap with no segment chaining. Related: Jain & Morari (2020), CDC [abstract].

### Methodological precedents for the chained surrogate (outside racing)
12. **Geiger et al. (2023).** Solving multi-objective inverse problems of chained manufacturing processes. *CIRP J. Manuf. Sci. Technol.* [abstract]
    - One GP per stage, "stacked to build a unified surrogate model that represents the entire manufacturing process chain", comparing joint with cascaded optimization. **Its joint-vs-cascaded comparison mirrors your coupled-vs-independent ablation.**
13. **Astudillo, R. & Frazier, P. (2021).** Bayesian Optimization of Function Networks. NeurIPS. arXiv:2112.15311 [abstract]
    - "each function takes as input the output of its parent nodes". This is the general formulation your chain is an instance of.
14. **Kiroirwal, Pfrommer & Beyerer (2026).** Joint Parameter and State-Space Bayesian Optimization. arXiv:2602.17679 [full*]
    - A DAG of GP surrogates in which intermediate outputs feed later subprocesses.
15. **Kyzyurova, Berger & Wolpert (2018)**, SIAM/ASA JUQ, and **Sanson, Le Maître & Congedo (2019)**, CMAME [abstract]
    - Linking per-stage emulators beats emulating the whole chain directly. **This supports your premise that a chained model should beat a single global lap-time model.**
16. **Chen et al. (2004).** Modelling and optimization of fed-batch fermentation processes using dynamic neural networks and genetic algorithms. *Biochemical Engineering Journal* [abstract]
    - NN sub-models whose outputs feed the next sub-model, optimized with a GA. This is the closest structural analogue to your method.
17. **Mao et al. (2024).** An XGBoost-assisted evolutionary algorithm for expensive multiobjective optimization problems. *Information Sciences* [abstract]
    - XGBoost as the surrogate inside an EA is already published, so the model choice is not a contribution.

## DE over GA: literature support exists, but mostly general
Hojaji gives no justification for choosing a GA, so the burden is only on you to justify DE.
- **Only domain-specific comparison found:** Molina-Pérez et al. (2025), "Simplified Racing Trajectory Optimization via Evolutionary Algorithms", ISCMI 2025 [abstract]: "DE outperforms GA in terms of solution quality and robustness, achieving lower lap times with reduced variance." It optimizes racing-line geometry with a physics evaluator. The author list and DOI still need confirming.
- **General benchmarks:** Storn & Price (1997), J. Global Optim. 11:341–359: DE is designed for nonlinear, non-differentiable continuous functions, which suits a piecewise-constant XGBoost fitness. Vesterstrom & Thomsen (2004), CEC: DE generally beat PSO and an EA across 34 benchmarks, **but lost on noisy functions**, and surrogate error behaves like noise. Das & Suganthan (2011), IEEE TEVC; Das, Mullick & Suganthan (2016), Swarm Evol. Comput.
- **Strongest argument, from non-separability:** chaining v_exit into v_entry makes the KPIs of neighbouring microsectors interdependent. Coordinate-wise GA operators degrade on such problems (Salomon 1996, BioSystems; Iorio & Li 2004, "Traditional genetic algorithms... have significant trouble with problems with interdependent relationships between decision variables" [full]). DE's difference-vector mutation is rotation-invariant. **But this only holds with a high crossover rate (CR ≈ 0.9).** Low-CR binomial crossover is not rotation-invariant (Opara & Arabas 2019 [full]: "Classical DE is not rotationally invariant"; Caraffini & Neri 2019; Montgomery & Chen 2010).
- **Counterpoints to acknowledge:**
  - An examiner may ask "why not CMA-ES?", which is rotation-invariant by design (Hansen, arXiv:1604.00772).
  - Tree ensembles can be optimized exactly as a MIP (Mišić 2020, *Operations Research*), although chaining makes that harder.
  - No free lunch applies.
- **Recommendation:** add an optimizer arm to the ablation, running Hojaji's GA against DE (and CMA-ES if time allows) on the same surrogate across several seeds. The DE claim then rests on your own evidence instead of analogy.

**Draft justification paragraph (adapt it; confirm the Molina-Pérez details first):**
> We replace the genetic algorithm of Hojaji et al. (2026) with Differential Evolution (DE), a derivative-free optimizer designed for continuous, possibly non-differentiable objectives (Storn & Price, 1997), which suits the piecewise-constant fitness of a gradient-boosted tree surrogate. DE has generally outperformed conventional evolutionary algorithms on numerical benchmarks (Vesterstrom & Thomsen, 2004; Das et al., 2016), and in a racing-trajectory study it achieved lower lap times with lower variance than a GA (Molina-Pérez et al., 2025). Because our surrogate passes exit speed from each microsector to the next, the KPIs of adjacent microsectors are coupled and the problem is non-separable. Coordinate-wise GA operators are known to degrade on such problems (Salomon, 1996; Iorio & Li, 2004), whereas DE's difference-vector mutation is rotation invariant; we use a high crossover rate (CR ≈ 0.9) to preserve this property (Opara & Arabas, 2019). Consistent with the no-free-lunch theorem, we treat this choice as a hypothesis and compare DE against the original GA empirically.

## Risks examiners are likely to raise
1. **Compounding error along 20 chained predictions.** XGBoost gives no uncertainty estimate, so DE may exploit extrapolation. Bound the search to the observed data range (Wang et al. 2019, already in A1), or use ensemble variance as a penalty. The linked-emulator and function-network literature treats this as an expected concern.
2. **Straw-man ablation.** Keep Hojaji's transition penalty in the independent arm.
3. **Hojaji's group is active.** They have a cross-track SSRN preprint and a stated aim of real-time ML–EA coaching. Re-run this search before submission.
4. **Bae et al. 2025.** Resolved 2026-09-26: its features include per-corner entry and exit speed, and its advice is applied by a real driver, so the coupling is enforced physically. Position against it as described in entry 3 above; do not present it as a flawed method.

## Suggested additions to Zotero
- Satujoda & Huggins 2026, doi:10.3390/vehicles8070146
- Nunes et al. 2026, doi:10.3390/e28090960
- Hojaji et al. 2024, CHB Reports 14:100414
- Bae et al. 2025, doi:10.1109/ACCESS.2025.3615128
- von Schleinitz et al. 2022, arXiv:2201.12939
- Botta et al. 2012, IEEE CIG; Cardamone et al. 2010, IEEE CIG
- Klapálek et al. 2024, SCITEPRESS
- Geiger et al. 2023, CIRP JMST
- Astudillo & Frazier 2021, arXiv:2112.15311
- Storn & Price 1997, doi:10.1023/A:1008202821328
- Vesterstrom & Thomsen 2004, CEC
- Opara & Arabas 2019, Swarm Evol. Comput. 44
- Salomon 1996, doi:10.1016/0303-2647(96)01621-8
- Iorio & Li 2004, LNAI 3339
- Molina-Pérez et al. 2025, ISCMI (confirm details)

## How this was searched
- **Angles:** five parallel searches:
  1. Data-driven coupling of track segments.
  2. Surrogate-assisted EAs and chained surrogates.
  3. Telemetry coaching with per-segment targets.
  4. DE vs GA.
  5. Hojaji's own papers and papers citing them.
- **Sources:** Consensus first, then Scholar Gateway, web search, arXiv and publisher pages.
- **Gaps in coverage:**
  - Google Scholar (robots.txt), IEEE Xplore, ACM DL, Semantic Scholar and OpenAlex were blocked or rate-limited from this environment. Several IEEE/ACM items are therefore abstract-only.
  - The "cited by" check on Hojaji is incomplete. Only the group's own follow-ups were found.
  - The Consensus monthly quota is now used up (resets 1 October).
- **Verification:** I re-checked the Satujoda and Nunes quotes against the publisher pages. I dropped one claimed quote about Satujoda ("independent rows rather than sequential states") because it could not be found.
