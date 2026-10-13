# Chapter 2: Review of Related Literature (skeleton v3)

Version 3, 2026-10-03. It replaces v1 (2026-09-25). Section 2.2 now carries the simulator validity and reliability argument moved out of the methodology. This is an outline to draft from, not prose.

## Scope (settled; do not re-open in the chapter)
- **Sole contribution:** a learned, microsector-chained XGBoost surrogate fitness (v_entry,n+1 = v_exit,n), tested by ablation against a variant that fixes each microsector's entry speed at its mean fast-lap value, with the same surrogate, GA, KPIs, penalty P and seeds. Neither uses Hojaji's 90–105% clamp.
- **Optimizer:** Hojaji et al.'s (2026) GA, unchanged. No optimizer comparison and no DE.
- **Genes:** control KPIs only. Entry, apex and exit speed and microsector time are state or outcome variables; v_entry,1 is fixed at the mean fast-lap entry speed.
- **Supporting steps, not contributions:** per-microsector feature selection (v_entry,n as covariate, top K = 10, SHAP reported), the 70/30 split, grouped 10-fold CV and the test-lap rollout.
- **Terms:** a microsector is one corner or straight. Other papers' units are marked "(their term)".

## Map: sections to objectives and method steps

| Section | Supports | Pages |
|---|---|---|
| 2.1 Introduction and scope | All | 1 |
| 2.2 Simulator validity and reliability | Obj 1, Step 1; adviser comment on reliability | 2 |
| 2.3 Telemetry-based analysis of driver performance | Problem statement; Obj 1 segmentation; Steps 2 and 3 | 3 |
| 2.4 The baseline: Hojaji et al. (2026) | Problem-statement gap; Step 5; Obj 3 | 2.5 |
| 2.5 Physical interdependence of microsectors | Obj 2 (coupling, speed trade-offs); Step 4 | 2 |
| 2.6 Racing optimizers that carry the coupling | Your framing (autonomous agents vs human drivers); Obj 3 | 1.5 |
| 2.7 Learned and chained surrogates | Obj 2, Step 4 (model, chain, rollout); Step 5 | 3.5 |
| 2.8 Synthesis and research gap | The contribution and its ablation | 2.5 |
| 2.9 Summary and conceptual framework | Adviser comment on the diagram; bridge to Ch 3 | 1 |

Obj 1: microsector dataset. Obj 2: interdependence and speed trade-offs. Obj 3: GA optimization validated against human telemetry. If long, cut [O] sources, then shorten 2.3 and 2.6, never 2.4 or 2.8.

## How to read
- **Tags** read [status; reading; priority]. Status: a `bib key`, or "add" to Zotero. Reading: full; full\* (via a summarizing tool, so check quotes against the PDF); partial; abs (abstract only); none means you already cite it. Priority: **C** carries the argument or appears in the matrix or gap, so read it in full; **S** gets one sentence or a grouped citation; **O** is cut first.
- Labels are placeholders. Insert citations through Zotero in the doc's Chicago author-date style.
- Ignore the DE material in `Research_Gap_Assessment.md` and `A1_...md`; gap entry 3 replaces A1's note on Bae.
- Cut from v1: commercial coaching tools, Quadflieg, Jain & Morari, the SSRN preprint, Braghin. Kegelman 2017 moves to Chapter 3 (validating against the Fast-cluster distribution rather than one best lap).

**Hojaji citation labels**

| Label here | Venue | Key | Renders as (Chicago) |
|---|---|---|---|
| Hojaji 2023 | AICS, CCIS 1662 | `longo_machine_2023` | Hojaji, Toth, and Campbell 2023 |
| Hojaji 2024a | GALA, LNCS 14475 ("An AI Approach…") | `dondio_ai_2024` | Hojaji et al. 2024a |
| Hojaji 2024b | *CHB Reports* 14:100414 ("AI-enabled prediction…") | add | Hojaji et al. 2024b |
| Hojaji 2026 | ICAART | `hojaji_optimizing_2026` | Hojaji, Toth, and Campbell 2026 |

Both 2024 papers have the same four authors, so they need suffixes, assigned by title order ignoring "An" (so GALA should be "a"). Zotero assigns them; confirm after import. GALA is 2024, not 2023 as v1 said.

---

## 2.1 Introduction and scope
**Purpose:** state the question the chapter answers, how sources were found, and the terms.

**Topic sentences**
1. This chapter reviews the literature needed to answer one question: how should an evolutionary optimizer of sim-racing driver inputs evaluate a lap whose microsectors depend on one another?
2. Sources were located through Consensus, Scholar Gateway, web search, arXiv and publisher pages, covering [years], and peer-reviewed full texts were preferred, so that no core claim rests on an abstract alone.
3. A microsector is one corner or one straight; Hojaji et al. call the same unit a "sector" (2026) or a "segment" (2024b), and "sector" otherwise means an official timing sector spanning several microsectors.
4. Control KPIs are driver inputs; entry, apex and exit speed and microsector time are state or outcome variables; and a surrogate is a model that stands in for the true evaluator of a candidate lap. [Roadmap sentence follows.]

**Leads to:** the data source the thesis rests on (2.2).

## 2.2 Simulator validity and reliability
**Purpose:** carry the full argument for why ACC telemetry is a sound dataset for this thesis, and where that soundness ends. This answers the adviser's comment on Objective 1. Chapter 3 keeps only a short recap that points here.

**Topic sentences**
1. A simulator should not be labelled "valid" or "invalid" as a whole, because its validity depends on the research question and the variables measured (Himmels et al. 2023, p. 192). Absolute and relative validity both describe how a simulator compares with real driving.
2. This thesis makes no such comparison and does not claim that ACC telemetry is equivalent to real-car telemetry. Its context is sim racing as an esport: the drivers, laps, fast reference and optimized targets all exist inside ACC, and every comparison is between laps recorded in the same simulator, car, setup, track and conditions. Results are therefore stated for competitive sim racing in ACC, not for professional real-world racing.
3. Evidence that simulator measures partly reflect real driving skill is supporting only, not a premise. Racing drivers had faster lap times, higher steering activity and a better line than non-racing drivers in a fixed-base simulator (van Leeuwen et al. 2017). In a professional simulator, amateurs' slower laps came mainly from weaker handling rather than line choice (von Schleinitz et al. 2022). With consumer racing hardware and the original Assetto Corsa, lap time correlated with driving-speed measures on a research simulator (Tiu et al. 2020). None of these used ACC.
4. The wider validation literature is mixed, which is why the claims stay inside the simulator. About half of simulators reached absolute or relative validity (Wynne et al. 2019). Speed, a central outcome here, was inconsistent across six simulators (Himmels et al. 2024) and showed relative but not absolute validity in a road study (Godley et al. 2002). Real racing adds physical load and stress a simulator lacks (Holland et al. 2025). Most of these concern road driving, so they are background, not direct evidence about ACC.
5. Precedent supports the data and pipeline. ACC telemetry captured with MoTeC underlies several peer-reviewed sim-racing studies (Hojaji 2024b; Hojaji 2026; Joyce et al. 2024). Remonda et al. (2021) compared drivers on per-segment telemetry features such as brake point and entry and exit speed, a precedent for microsector-level KPIs. The developer states that ACC's tracks are laser-scanned and its physics simulate modern GT cars (KUNOS Simulazioni n.d.); present these as the developer's own claims, not validation.
6. Separately from validity, the thesis checks reliability: how consistent each KPI is across a driver's recorded laps (for example with an intraclass correlation). KPIs with low consistency are reported as a limitation (method in Chapter 3).

**Sources** (full references and draft text: `literature-review/Simulator_Reliability_Draft.md`)
- Himmels et al. 2023, doi:10.1145/3581961.3609895 [add; full; C; definitions on p. 192]
- van Leeuwen et al. 2017, doi:10.1371/journal.pone.0186871 [add; full; C]
- Wynne et al. 2019, doi:10.1016/j.ssci.2019.04.004 [add; abs; C]
- Himmels et al. 2024, doi:10.1016/j.trf.2024.01.007 [add; abs; S]
- Godley et al. 2002, doi:10.1016/S0001-4575(01)00056-2 [add; S]
- Holland et al. 2025, doi:10.3389/fspor.2025.1498686 [add; S]
- von Schleinitz et al. 2022, arXiv:2201.12939 [add; full\*; S]
- Tiu et al. 2020, doi:10.3390/geriatrics5020035 [add; S]
- Joyce et al. 2024, doi:10.3390/vision8020027 [add; S]
- Remonda et al. 2021, doi:10.1371/journal.pone.0245320 [add; full\*; S]
- KUNOS Simulazioni n.d., ACC product page [add as web page; O]
- The Hojaji papers are cited here and described in 2.3 and 2.4.

**Notes**
- Keep sentence 3 framed as supporting evidence. Every comparison in the thesis is inside ACC, so the argument does not depend on it.
- Do not claim simulators are standard for professional training (only a passing remark in Remonda).
- Check the wording of van Leeuwen, von Schleinitz and Tiu against the PDFs before quoting. Murphy 2026 and the ACC export blog stay in Chapter 3 (hardware and data collection).
- Threats-to-validity table, data collection and the reliability statistic stay in Chapter 3.

**Leads to:** how has prior work analysed driver performance from this telemetry?

## 2.3 Telemetry-based analysis of driver performance
**Purpose:** show how ML has predicted, stratified and explained driver skill, and at what unit of the lap.

### 2.3.1 Predicting and stratifying performance
**Topic sentences**
1. Hojaji and colleagues showed that KPIs extracted from ACC telemetry predict a driver's performance level, with SVM, XGBoost and RF feature selection reducing 84 features to 10 (Hojaji 2023), and that speed, steering and line-deviation KPIs are among the most informative (Hojaji 2023; 2024a).
2. Hojaji et al. (2024b) clustered laps by K-Means on lap time, choosing k by the Elbow and Silhouette criteria, and divided the Brands Hatch lap into 19 segments (their term: 10 straights and 9 turns); Step 2 follows this procedure.
3. In these studies importance is measured against lap-level performance, either a performance class or lap time, so it shows which KPIs matter for a lap but not where on the lap they matter.

**Sources:** `longo_machine_2023` [bib; C]; `dondio_ai_2024` [bib; C]; Hojaji 2024b, doi:10.1016/j.chbr.2024.100414 [add; partial; C; open access].

**Notes**
- Record each prior ACC study's drivers, laps and track (2024b: 174, 1327, Brands Hatch), so Chapter 3 can answer the "larger datasets" point (review E4).
- Segmentation precedent (Obj 1), in their terms: Hojaji 2024b (19 segments), Hojaji 2026 (20 sectors), Klapálek et al. 2024, Nunes et al. 2026 (corner-aligned sectors).

### 2.3.2 Per-corner explanation and coaching
**Topic sentences**
1. Bae et al. (2025) move the unit of analysis to the corner: a per-corner skill classifier, explained with SHAP (Lundberg & Lee 2017), yields counterfactual advice toward the expert class, and its "Strategic Features" include the corner's ENTRY max velocity, EXIT max velocity and ENTRY min velocity.
2. Other systems also advise per corner against a reference, from a reinforcement-learning reference line (Kaufman et al. 2024) or as LLM feedback on rule-based diagnoses (Nunes et al. 2026), and Nunes et al. name "a speed deficit carried over from the previous corner", so the carry-over is visible in human sim-racing data.
3. These systems need not model the coupling between corners, because a driver carries out the advice in the simulator, whose physics enforces it; a lap produced by an optimizer has no driver to do this.

**Sources:** Bae et al. 2025, doi:10.1109/ACCESS.2025.3615128 [add; full; C]; Nunes et al. 2026 [add; full\*; C]; Lundberg & Lee 2017 [add; S; required, since SHAP is reported]; Kaufman et al. 2024 [add; full\*; S]; Costa et al. 2025, Han et al. 2025, Bugeja et al. 2017 [add; abs; O].

**Notes**
- Contrast, not criticism: in Bae, entry and exit speed are features of the same corner, which suits advice a real driver carries out. Here, entry speed is a state inherited from microsector n−1: a covariate, never a gene.
- Per-microsector SHAP (Step 3) answers the problem statement's question of which microsectors matter most. It is a supporting step, not a contribution.

**Leads to:** the one sim-racing study whose optimized lap exists only inside a model (2.4).

## 2.4 The baseline: Hojaji et al. (2026)
**Purpose:** describe the framework the thesis modifies and its two limitations: the one the authors state and the one in its equation.

**Topic sentences**
1. Hojaji, Toth, and Campbell (2026) extend this line into optimization and are the closest optimization framework for human drivers: a genetic algorithm evolves a lap encoded as 20 sectors (their term for microsectors; 10 corner-dominant and 10 straight-dominant), each a vector of 10 scaled KPIs, to produce an idealized lap for coaching.
2. Fitness is T + λP with λ = 0.1, where T sums microsector times, each a fast-lap baseline time adjusted linearly by the deviation of that microsector's KPIs from the scaled midpoint and clamped to 90–105%, and P penalizes sudden KPI transitions between consecutive microsectors, unusually large gradients within a microsector and values beyond physical thresholds.
3. The optimized lap (about 81–82 s, "around 4–5 seconds" faster than the fastest human lap) is judged only by its predicted time, and the paper reports no replay in the simulator, so the lap is physically unverified and its quality rests on the fitness function alone.
4. The framework has two limitations: the authors computed feature importance globally, because "reliable segment-specific estimation would require larger datasets" [your doc's wording; verify it and the page in the PDF], and, as a property of the equation, each microsector's time depends only on its own KPIs, so no speed passes across a boundary.

**Sources:** `hojaji_optimizing_2026` [bib; full\*; C]; von Schleinitz et al. 2022, arXiv:2201.12939 [add; full\*; S]; one GA textbook [add; S; see Open items].

**Notes**
- Link the limitations: ranking importance per microsector means modelling each microsector's Δt_n and v_exit,n, which depend on the inherited entry speed (2.5). So v_entry,n is a covariate in Step 3, and the problem-statement gap leads to the coupling gap.
- The penalties limit implausible KPIs but carry no state; von Schleinitz et al. (2022) report the same limit in their surrogate: "each data point isolated from its temporal surrounding".
- Chapter 3 lists the GA settings and states that P is kept, and the clamp dropped, in both variants.
- Objective 3: the baseline lap was never checked outside its model, so the thesis compares optimized control KPIs with Fast-cluster telemetry.

**Leads to:** is scoring each microsector independently physically justified?

## 2.5 Physical interdependence of microsectors
**Purpose:** show that a microsector's time depends on the speed it inherits; this grounds the chain and Objective 2's speed trade-offs.

**Topic sentences**
1. Quasi-steady-state lap-time simulation treats speed as continuous along the lap: it integrates speed forward out of one apex and backward from the next, and joins the two profiles where they meet (Kapania et al. 2016; Lenzo & Rossi 2020; Veneri & Massaro 2020).
2. The speed at which the car leaves microsector n therefore bounds what is achievable in microsector n+1, so a gain in one microsector can carry a cost into the next: a later, faster entry can cost exit speed, and a slower entry can buy exit speed for the following straight.
3. Learned models show the same dependence, since a data-driven racing-line model improved when it was given both preceding and upcoming track geometry (Garlick & Bradley 2021).
4. A fitness that scores microsectors independently can therefore credit gains that could not occur together, and evolutionary search can exploit such gaps in its evaluator (Lehman et al. 2020); whether this changes the optimized result is what the ablation tests.

**Sources:** Kapania et al. 2016 [add; full; C]; Veneri & Massaro 2020 [add; full; C]; Lenzo & Rossi 2020 [add; full; C]; `garlick_real-time_2021` [bib; full; C]; Lehman et al. 2020 [add; abs; S; arXiv:1803.03453]; Heilmeier et al. 2020 [add; abs; O].

**Notes:** the trade-off in sentence 2 is your reasoning from the cited mechanism; write it as such.

**Leads to:** how have optimizers carried this coupling?

## 2.6 Racing optimizers that carry the coupling
**Purpose:** show that most racing-optimization research targets autonomous agents rather than human drivers, and that methods carrying the coupling do so through a vehicle model or simulator.

**Topic sentences**
1. Most optimization research in racing targets autonomous agents rather than human drivers: learning-based control and reinforcement learning produce fast policies, up to champion level in Gran Turismo 7 (Kabzan et al. 2019; Samak et al. 2021; Ghignone et al. 2022; Evans et al. 2023; Lee et al. 2025), and trajectory optimization and racing-line generation solve the lap as a whole (Garlick & Bradley 2021).
2. Evolutionary racing-line optimization carries the coupling by evaluating each candidate in a full simulator (Cardamone et al. 2010) or through a forward-backward physics speed profile over track segments (their term), using a GA and CMA-ES (Klapálek et al. 2024).
3. These methods need a vehicle model or a simulator in the loop, and they output a racing line, a trajectory or a policy rather than per-microsector targets for a human driver's own inputs, which limits what they offer for improving human performance (Hojaji 2026).
4. Botta et al. (2012) replaced full simulation inside the EA with a cheaper physics-based lap-time estimate, which performed worse; this is the racing precedent for scoring candidates with a surrogate, for the risk that brings, and for checking a surrogate-optimized lap against something outside the model (Objective 3).

**Sources:** `kabzan_learning-based_2019`, `samak_autonomous_2021`, `ghignone_tc-driver_2022`, `evans_high-speed_2023`, `lee_champion-level_2025` [bib; S; grouped]; Cardamone et al. 2010 [add; full\*; S]; Klapálek et al. 2024 [add; full\*; C]; Botta et al. 2012 [add; full\*; C]; `eshof_sequential_2025`, `wachter_spatially-aware_2026` [bib; abs; O; whole-lap trajectory optimization only]; `roh_speed_2025` [bib; O]; Klapálek et al. 2026 [add; abs; O].

**Notes:** confirm Hojaji 2026 states the limit in sentence 3. Do not cite eshof, wachter or roh for coupling.

**Leads to:** can a model learned from telemetry stand in for the simulator and still carry the coupling?

## 2.7 Learned and chained surrogates
**Purpose:** frame Hojaji's linear scaler and the proposed XGBoost chain as surrogates, and show that learned racing models do not chain while chaining is established elsewhere.

### 2.7.1 Surrogates in offline data-driven EAs
**Topic sentences**
1. A surrogate stands in for an unavailable or expensive evaluator (Jin 2011); in offline data-driven optimization it is fitted once to historical data, so the search can be trusted only where those data lie (Wang et al. 2019), which is why Step 5 initializes genes within the training-lap ranges.
2. By this definition the baseline's linear scaler is already a surrogate, and Hojaji, Toth, and Campbell (2026) call it a "sector-based surrogate model"; the thesis replaces it with a learned surrogate and so inherits the risks noted in 2.5 and 2.6.

**Sources:** Jin 2011 [add; abs; S]; Wang et al. 2019 [add; abs; C].

### 2.7.2 Learned lap-time models in racing
**Topic sentences**
1. Learned lap-time models already exist in racing: a Gaussian-process surrogate of whole-lap time guides Bayesian trajectory optimization (Nam et al. 2026), and LightGBM predicts per-segment time (their term) from car setup in Assetto Corsa, reconstructing held-out lap time with 0.223 s mean absolute error (Satujoda & Huggins 2026).
2. Neither carries state from one part of the lap to the next: Nam et al. score the whole lap, and Satujoda & Huggins describe no carry-over between segments and report that "Telemetry-derived quantities were not used to generate the winning setup".
3. Gradient-boosted trees (Chen & Guestrin 2016) suit tabular KPI data and have served as EA surrogates (Mao et al. 2024), but tree models predict a constant outside the training range, which is another reason to keep the search within the observed KPI ranges.

**Sources:** Satujoda & Huggins 2026, doi:10.3390/vehicles8070146 [add; full\*; C; the paper a reviewer is most likely to raise]; Nam et al. 2026 [add; full\*; S]; Chen & Guestrin 2016 [add; S]; Mao et al. 2024 [add; abs; S].

### 2.7.3 Chained surrogates outside racing
**Topic sentences**
1. Outside racing, linking per-stage models so that one stage's output is the next stage's input is established: it is formalized as function networks (Astudillo & Frazier 2021; Kiroirwal et al. 2026) and has been applied with a GA to fed-batch fermentation (Chen et al. 2004) and with stacked Gaussian processes to multistage manufacturing (Geiger et al. 2023).
2. In linked Gaussian-process emulators of computer models, linking per-stage emulators predicted a chain better than one emulator of the whole (Kyzyurova et al. 2018; Sanson et al. 2019), but an error at one stage feeds every later stage, which is why Step 4 rolls each test lap through the full chain.
3. Geiger et al.'s comparison of joint and cascaded optimization parallels the coupled-versus-independent ablation used here.

**Sources:** Geiger et al. 2023 [add; abs; C]; Astudillo & Frazier 2021 [add; abs; C]; Kiroirwal et al. 2026 [add; full\*; S]; Chen et al. 2004 [add; abs; S]; Kyzyurova et al. 2018, Sanson et al. 2019 [add; abs; S].

**Notes:** tree extrapolation (2.7.2) and error propagation along a chain are your own reasoning unless a source you read states them. The thesis adapts chaining to sim racing; it does not invent it.

**Leads to:** learned racing models do not chain, and chaining has not reached the optimization of driver inputs (2.8).

## 2.8 Synthesis and research gap
**Purpose:** show in one table the combination no prior study has, and state the gap.

**Topic sentences**
1. Table 2.x compares the closest studies on the three properties this thesis combines: a time model learned from human telemetry, state carried across microsector boundaries inside the evaluator, and driver control KPIs as decision variables.
2. Three groups emerge: coaching systems, whose coupling the driver enforces; physics- and simulator-based optimizers, which carry it through a vehicle model but optimize a line or a policy; and learned surrogates, which do not chain in racing and, where they chain elsewhere, do not involve drivers.
3. [Gap statement, 2.8.2.]
4. The thesis therefore adapts an established idea, the chained surrogate, to optimizing sim-racing driver inputs and tests its effect by ablation, claiming no novelty for coupling itself, for chaining, for per-segment ML time models or for diagnosing carried-over speed.

### 2.8.1 Synthesis matrix

| Study | Data | Unit (their term) | Time model | State carried across boundaries | Decision variables | Optimizer |
|---|---|---|---|---|---|---|
| Hojaji 2026 | ACC, Laguna Seca | 20 "sectors" | Linear scaler, clamped | No; penalties only | Driver KPIs | GA |
| Hojaji 2024b | ACC, Brands Hatch; 174 participants, 1327 laps | 19 "segments" | ML prediction (models: verify) | Not applicable | None | None |
| Bae et al. 2025 | Racing simulator | Corner | Skill classifier with SHAP | Not needed: the driver enforces it | Per-corner features | Counterfactual search |
| Nunes et al. 2026 | iRacing | "Corner-aligned sectors" | Rule-based heuristics | Diagnosed, not modelled | None | None |
| Satujoda & Huggins 2026 | Assetto Corsa | 50 "segments" | LightGBM per segment | Not described | Car setup | Staged search; model not the fitness |
| Cardamone 2010; Botta 2012 | TORCS; racing game | "Track sections" | Simulator; physics estimate | Yes, through simulator or physics | Racing line | GA; EA |
| Klapálek et al. 2024 | Autonomous racing | "Track segments" | Physics speed profile | Yes, through physics | Racing line | GA, CMA-ES |
| Nam et al. 2026 | Autonomous racing | Whole lap | GP lap-time surrogate | No units to link | Trajectory | Bayesian optimization |
| Geiger et al. 2023 | Manufacturing | Process stage | Stacked GPs | Yes, learned | Process parameters | Joint vs cascaded (verify) |
| **This thesis** | ACC, human telemetry | Microsector | **XGBoost, chained v_exit,n → v_entry,n+1** | **Yes, learned** (ablation arm: no) | Driver control KPIs | GA (Hojaji settings) |

Units are in each study's own term. "Not described" means not described, not absent.

### 2.8.2 Gap statement (draft)
> Most racing optimization targets autonomous agents (Kabzan et al. 2019; Evans et al. 2023; Lee et al. 2025). The closest optimization of human driver KPIs in sim racing (Hojaji, Toth, and Campbell 2026) ranked KPIs globally, noting that estimating importance for each microsector would require larger datasets, and scored each microsector independently before summing, relying on penalties for abrupt transitions, within-microsector gradients and out-of-range values. Coaching systems advise a real driver (Bae et al. 2025; Kaufman et al. 2024; Nunes et al. 2026), so the driver and the simulator's physics enforce the coupling between microsectors. An optimizer's candidate laps exist only inside its fitness model, so that model must carry the coupling. Physics- and simulator-based optimizers carry it through a vehicle model, but they optimize a racing line, not a driver's inputs (Cardamone et al. 2010; Klapálek et al. 2024). Learned per-segment time models exist in sim racing but describe no carry-over of state and are not used as an optimizer's fitness (Satujoda and Huggins 2026). Chained surrogates are established in multistage manufacturing and process optimization (Geiger et al. 2023; Chen et al. 2004) and formalized as function networks (Astudillo and Frazier 2021; Kiroirwal et al. 2026). To our knowledge, no work has used a surrogate learned from human telemetry to propagate boundary speed between microsectors inside an evolutionary optimization of driver control KPIs, or measured how that coupling changes the optimized result against an otherwise identical variant in which each microsector's entry speed is fixed at its mean fast-lap value.

Then add one sentence: per-microsector feature selection follows from the chained surrogate, whose inputs must be ranked against its own targets, and also answers the baseline's stated limitation.

**Claims to avoid**
- Being first to link track sections by speed (physics), chain surrogates (2.7.3), notice carried-over speed deficits (Nunes), model per-segment time with ML (Satujoda) or use entry and exit speed as features (Bae).
- Per-microsector feature selection or SHAP as a contribution.
- "Unphysical" baseline laps (say "physically unverified"); Bae or other coaching systems as flawed.
- Transfer to real-world driving.

**Leads to:** the chapter summary and framework figure (2.9).

## 2.9 Summary and conceptual framework
**Purpose:** restate the gap, show the baseline and proposed frameworks side by side (adviser comment on the methodology), and bridge to Chapter 3.

**Topic sentences**
1. Coaching systems get the coupling between microsectors from the driver, and physics-based optimizers get it from a vehicle model, while the baseline optimizer of driver KPIs evaluates each microsector independently (Hojaji 2026).
2. Figure 2.x places the baseline framework beside the proposed one: the only highlighted change is the fitness, and the microsector-independent variant appears as the ablation arm.
3. Chapter 3 describes how each block is implemented and how the two fitness variants are compared.

**Figure:** reuse `methodology/diagrams/Frameworks_Baseline_vs_Proposed.drawio` so Chapters 2 and 3 share one picture.
- Baseline: telemetry → global KPI importance → linear per-microsector scaler with clamp, plus P → GA → KPI lap judged by predicted time.
- Proposed: ACC/MoTeC telemetry → microsector segmentation, 70/30 split → K-Means stratification → per-microsector feature selection (top 10) → **chained XGBoost surrogate, v_entry,n+1 = v_exit,n** (only highlighted box; ablation arm noted on it) → Hojaji GA, unchanged → per-microsector control-KPI targets → validation against Fast-cluster telemetry.

**Leads to:** Chapter 3 (Methodology).

---

## Open items
1. **Read in full before drafting:** Geiger 2023 and Astudillo & Frazier 2021 (they anchor the gap), Hojaji 2024b (models, k, dataset), Wang 2019, van Leeuwen 2017, Lehman 2020.
2. **Check in the Hojaji 2026 PDF, with pages:** the "larger datasets" sentence, the stated limit for human drivers, v1's 91.05 s mean and 86 s best, the absence of a simulator replay, drivers, laps and track, and the title (stray colon in the bib).
3. **Check before citing:** Bugeja 2017 and Han 2025 abstracts before finalizing 2.8 (Bugeja's title overlaps this niche); Klapálek 2026 (keep only if it optimizes over track segments); `roh_speed_2025`. Unverified lead for 2.2: "Sensitive and Reliable Measures of Driver Performance in Simulated Motor-Racing" (PubMed 31523355); cite only after confirming its details.
4. **GA textbook:** Goldberg 1989 (add-list) or Eiben & Smith 2015 (covers Gaussian mutation; access unchecked).
5. **Zotero and Thesis.bib:** add the "add" sources, including the new 2.2 sources (Himmels 2023 and 2024, van Leeuwen, Wynne, Godley, Holland, Tiu, Joyce, Remonda, KUNOS page); confirm the 2024a/2024b letters; use published versions of Lundberg & Lee, Astudillo & Frazier and Nam; drop "(only if you use SHAP)" and cut sources from `Zotero_To_Add.md`; fix the ghignone and garlick years, consensus.app URLs, samak's type, "van den Eshof", the `dondio_ai_2024` series and the editor-based keys.
6. **Your doc (not edited):** the problem statement names only the global-importance gap; one sentence naming the coupling gap would align Chapters 1 and 2. Add the 2024a/2024b letters there and in Step 2, and replace "racing lines" with "per-microsector control-KPI targets" (review C13, E2).
7. **Search coverage:** Google Scholar, IEEE Xplore and ACM DL were not reachable; search them (including new work by Hojaji's group) before submission, and fill in the years in 2.1.
8. **Foreign/Local headings:** if required, add a table mapping sources to them. No Philippine sim-racing studies were found.
