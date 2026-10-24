# Chapter 2: Review of Related Literature

> **Superseded (2026-10-24).** The Google Doc "Thesis TODOs" now holds the current text of this section. Repo copy: `08_Project_Files/Thesis_TODOs_Doc_2026-10-24.md`. This file is kept for history.

## 2.1 Introduction and Scope

This chapter reviews the literature needed to answer one question: how should an evolutionary optimizer of sim-racing driver inputs evaluate a lap whose parts depend on one another? It first establishes why simulator telemetry is a sound source of data for this question (2.2). It then reviews how machine learning has been used to analyse driver performance from such telemetry (2.3) and describes the framework this thesis extends, the genetic algorithm of Hojaji et al. (2026) (2.4). Section 2.5 reviews the physical reasons why the parts of a lap cannot be scored independently. Sections 2.6 and 2.7 review optimizers and learned models that do or do not carry this dependence, and 2.8 brings the strands together into the research gap.

Sources were located through Consensus, Google Scholar and arXiv, supplemented by publisher pages, and covered work published between [years]. Peer-reviewed full texts were preferred, so that no central claim rests on an abstract alone.

Three terms are used throughout. A **microsector** is a single corner or a single straight. Hojaji et al. call the same unit a "sector" (2026) or a "segment" (2024b). In this thesis "sector" keeps its usual meaning of an official timing sector, which spans several microsectors. **Control KPIs** are measures of the driver's inputs, such as brake duration or peak steering angle. Entry, apex and exit speed and microsector time are **state or outcome variables**, because they result from those inputs. A **surrogate** is a model that stands in for the true evaluator of a candidate lap, which here would be driving the lap in the simulator.

---

## 2.2 Simulator Validity and Reliability

### 2.2.1 What "valid" means for this thesis

A simulator should not be labelled "valid" or "invalid" as a whole, because its validity depends on the research question and the variables measured (Himmels et al., 2023). Himmels et al. (2023) distinguish two kinds of validity. A simulator has **absolute validity** when its measurements match those from real driving, and **relative validity** when effects in the simulator point in the same direction as in real driving. Both kinds compare a simulator with the real world.

This thesis makes no such comparison and does not claim that telemetry from Assetto Corsa Competizione (ACC) is equivalent to real-car telemetry. Its context is sim racing as an esport. The drivers, the laps, the fast reference and the optimized targets all exist inside ACC, and every comparison is made between laps recorded in the same simulator, with the same car, setup, track and conditions. The question is how to drive faster in the simulator, so the data need to be sound for that purpose only. The results are therefore stated for competitive sim racing in ACC, specifically the McLaren 720S GT3 at Brands Hatch, and not for real-world racing. This follows the research the thesis builds on, which treats sim racing performance as an outcome of interest in its own right (Hojaji et al., 2024b, 2026; Joyce et al., 2024).

### 2.2.2 Mixed evidence on simulator–real equivalence

The wider validation literature gives a further reason to keep the claims inside the simulator, because its findings are mixed. A systematic review of driving simulator validation studies reported that roughly half of the simulators examined achieved absolute or relative validity, while about a third produced non-valid results, and that the relationship between simulator fidelity and validity was not straightforward (Wynne et al., 2019) [verify]. A comparison of six driving simulators reported good absolute validity for headway distance and lateral position but inconsistent results for driving speed (Himmels et al., 2024) [verify], and speed is a central outcome in this thesis. In an earlier road-safety study, speed showed relative but not absolute validity, because participants drove faster in the real car than in the simulator (Godley et al., 2002). Real racing also places physical load and stress on the driver that a simulator does not reproduce (Holland et al., 2025). Apart from Holland et al. (2025), these studies concern road driving, so they are background rather than direct evidence about ACC.

### 2.2.3 Evidence that simulator measures reflect driving skill

Although the thesis does not depend on it, some studies suggest that measures taken in racing simulators partly reflect real driving skill. In a fixed-base simulator, racing drivers achieved faster lap times, showed higher steering activity and followed a better racing line than non-racing drivers (van Leeuwen et al., 2017), although the sample was small and the simulator was not ACC. In a professional driver-in-the-loop simulator, the slower lap times of amateur drivers came mainly from weaker vehicle handling rather than from their choice of line (von Schleinitz et al., 2022). With consumer racing-simulator hardware running the original Assetto Corsa, lap time correlated with driving-speed measures taken on a research simulator (Tiu et al., 2020), although that study's participants and purpose differ greatly from this one. Together, these findings suggest that what separates fast and slow laps in a simulator is at least partly driving skill and not only familiarity with the game. They are supporting context, and the conclusions of this thesis do not rely on them.

### 2.2.4 Precedent for the data and pipeline

ACC telemetry captured with MoTeC has been used in several peer-reviewed studies of sim racing performance by one research group (Hojaji et al., 2024b, 2026; Joyce et al., 2024), and the main dataset of this thesis is the one published with Hojaji et al. (2024b). Remonda et al. (2021) compared drivers in a professional racing simulator using per-segment telemetry features such as brake point and segment entry and exit speeds, which is a precedent for measuring driver behaviour at the level of individual track sections. The developer states that ACC's tracks are laser-scanned and that its physics simulate modern GT cars (KUNOS Simulazioni, n.d.). These are the developer's own claims, not independent validation, and the thesis does not rely on them.

Separately from validity, the thesis checks the **reliability** of its measurements, meaning how consistent each KPI is across a driver's recorded laps. The procedure is described in Chapter 3.

---

## 2.3 Telemetry-Based Analysis of Driver Performance

### 2.3.1 Predicting and stratifying performance

A line of work by Hojaji and colleagues has shown that telemetry from ACC can predict how well a sim racer drives. Hojaji et al. (2023) extracted KPIs from ACC telemetry and used support vector machine, XGBoost and random forest feature selection to reduce 84 candidate features to 10 that predict a driver's performance level. Speed, steering and lane-deviation KPIs were among the most informative (Hojaji et al., 2023, 2024a).

Hojaji et al. (2024b) went further and divided each lap at Brands Hatch into 19 segments (their term: 10 straights and 9 turns). They grouped laps into skill levels by applying K-Means clustering to lap time, choosing the number of clusters with the Elbow method and the Silhouette coefficient. The stratification step of this thesis (Chapter 3, Step 2) follows that procedure, and the segment-level dataset published with that study is the main dataset used here.

In these studies, importance is measured against lap-level performance, either a performance class or lap time. They therefore show which KPIs matter for a lap, but not where on the lap they matter.

### 2.3.2 Per-corner explanation and coaching

Bae et al. (2025) moved the unit of analysis to the individual corner. They trained a per-corner skill classifier, explained it with SHAP (Lundberg & Lee, 2017) and used it to generate counterfactual advice that moves a driver toward the expert class. Their "Strategic Features" include a corner's entry maximum velocity, exit maximum velocity and entry minimum velocity. Other systems also give per-corner advice against a reference: Kaufman et al. (2024) derive the reference from a reinforcement-learning agent, and Nunes et al. (2026) generate feedback with a large language model from rule-based diagnoses. Nunes et al. (2026) name "a speed deficit carried over from the previous corner" among their diagnoses, which shows that the carry-over of speed between corners is visible in human sim-racing data.

These coaching systems do not need to model how one corner affects the next. A driver carries out the advice in the simulator, and the simulator's physics enforces the coupling. In Bae et al. (2025), for example, entry and exit speed are features of the same corner, which suits advice that a real driver will act on. A lap produced by an optimizer has no driver to enforce the coupling, so the model that evaluates the lap must carry it instead. In this thesis, entry speed is therefore treated as a state inherited from the previous microsector: it enters the model as a covariate and is never a decision variable.

---

## 2.4 The Baseline: Hojaji et al. (2026)

Hojaji et al. (2026) extended this line of work from analysis to optimization, and their framework is the closest prior optimization of human driver inputs in sim racing. A genetic algorithm (GA) evolves a lap encoded as 20 sectors (their term for microsectors: 10 corner-dominant and 10 straight-dominant), each described by a vector of 10 scaled KPIs, to produce an idealized lap for coaching. The data were recorded in ACC with the McLaren 720S GT3 at Laguna Seca.

Each candidate lap is scored as Fitness = T + λ·P, with λ = 0.1. T is "the predicted lap time obtained from the sector-based surrogate model" (Hojaji et al., 2026, p. [verify]). For each microsector, this model takes a baseline time from fast laps and adjusts it linearly by how far that microsector's KPIs deviate from the midpoint of their scaled range, and the adjusted time is clamped to between 90% and 105% of the baseline. The penalty P discourages three kinds of unrealistic candidates: sudden changes in a KPI between consecutive microsectors, unusually large gradients within a microsector, and KPI values beyond predefined physical thresholds. The optimized lap, at about 81–82 s, was reported as "around 4–5 seconds" faster than the fastest human lap (Hojaji et al., 2026) [verify]. That lap is judged only by its predicted time, and the paper reports no replay of it in the simulator, so its quality rests on the fitness function alone. It is physically unverified, which is not the same as physically impossible.

The framework has two limitations that this thesis addresses. The first is stated by the authors: feature importance was computed globally rather than per microsector, because reliable segment-specific estimation would require larger datasets (Hojaji et al., 2026) [verify wording and page]. The second follows from the fitness equation. Each microsector's time depends only on that microsector's own KPIs, so no speed is passed from one microsector to the next. The penalties limit implausible KPI values and abrupt changes, but they carry no state. A similar limit has been reported for another surrogate used to evaluate racing drivers, whose models "compute each data point isolated from its temporal surrounding" (von Schleinitz et al., 2022).

The two limitations are linked. To rank KPIs for each microsector, the model must predict each microsector's own time and exit speed, and both depend on the speed with which the car enters that microsector (2.5). For this reason, entry speed is included as a covariate in the per-microsector feature selection of this thesis, and the gap named in the problem statement leads directly to the coupling gap. The GA itself, with its settings and penalty P, is kept unchanged (Chapter 3).

---

## 2.5 Physical Interdependence of Microsectors

Lap-time simulation has long treated speed as continuous along the lap. Quasi-steady-state methods integrate the speed profile forward out of one corner and backward from the next, and join the two profiles where they meet (Kapania et al., 2016; Lenzo & Rossi, 2020; Veneri & Massaro, 2020). The speed at which the car leaves one section of track therefore bounds what is achievable in the next.

It follows that a gain in one microsector can carry a cost into the next. A later, faster entry into a corner may shorten that corner's time but cost exit speed, which then lengthens the following straight. Conversely, a slower entry can buy exit speed that pays off on the straight. This trade-off is this thesis's own reasoning from the mechanism described in the lap-time simulation literature, and it is the "speed trade-off" that Objective 2 refers to.

Learned models show the same dependence. A data-driven racing-line model performed better when it was given both the preceding and the upcoming track geometry (Garlick & Bradley, 2021).

A fitness function that scores microsectors independently can therefore credit a candidate lap with gains that could not occur together. Evolutionary search is known to exploit such gaps in its evaluator (Lehman et al., 2020) [verify]. Whether this changes the optimized result in practice is an empirical question, and the ablation in Chapter 3 is designed to answer it.

---

## 2.8 Synthesis and Research Gap

### 2.8.1 Synthesis

Table 2.1 compares the closest studies on the three properties this thesis combines: a time model learned from human telemetry, state carried across microsector boundaries inside the evaluator, and driver control KPIs as decision variables. Three groups emerge. Coaching systems give advice to a driver, whose simulator enforces the coupling. Physics- and simulator-based optimizers carry the coupling through a vehicle model, but they optimize a racing line or a control policy. Learned surrogates do not chain in racing, and where chained surrogates are used in other fields, they do not involve drivers.

**Table 2.1.** Closest studies compared on the properties combined in this thesis. Units are given in each study's own term; "not described" means the paper does not describe it, not that it is absent.

| Study | Data | Unit (their term) | Time model | State carried across boundaries | Decision variables | Optimizer |
|---|---|---|---|---|---|---|
| Hojaji et al. (2026) | ACC, Laguna Seca | 20 "sectors" | Linear scaler, clamped | No; penalties only | Driver KPIs | GA |
| Hojaji et al. (2024b) | ACC, Brands Hatch | 19 "segments" | ML prediction | Not applicable | None | None |
| Bae et al. (2025) | Racing simulator | Corner | Skill classifier with SHAP | Not needed: the driver enforces it | Per-corner features | Counterfactual search |
| Nunes et al. (2026) | iRacing | "Corner-aligned sectors" | Rule-based heuristics | Diagnosed, not modelled | None | None |
| Satujoda & Huggins (2026) | Assetto Corsa | "Segments" | LightGBM per segment | Not described | Car setup | Staged search; model not the fitness |
| Cardamone et al. (2010); Botta et al. (2012) | TORCS; racing game | "Track sections" | Simulator; physics estimate | Yes, through simulator or physics | Racing line | GA; EA |
| Klapálek et al. (2024) | Autonomous racing | "Track segments" | Physics speed profile | Yes, through physics | Racing line | GA, CMA-ES |
| Geiger et al. (2023) | Manufacturing | Process stage | Stacked Gaussian processes | Yes, learned | Process parameters | Joint vs cascaded |
| **This thesis** | ACC, human telemetry | Microsector | **XGBoost, chained (v_exit,n → v_entry,n+1)** | **Yes, learned** (ablation arm: no) | Driver control KPIs | GA (Hojaji settings) |

### 2.8.2 Research gap

Most optimization research in racing targets autonomous agents (Kabzan et al., 2019; Evans et al., 2023; Lee et al., 2025). The closest optimization of human driver KPIs in sim racing (Hojaji et al., 2026) ranked KPIs globally, noting that estimating importance for each microsector would require larger datasets, and scored each microsector independently before summing, relying on penalties for abrupt transitions, within-microsector gradients and out-of-range values. Coaching systems advise a real driver (Bae et al., 2025; Kaufman et al., 2024; Nunes et al., 2026), so the driver and the simulator's physics enforce the coupling between microsectors. An optimizer's candidate laps, by contrast, exist only inside its fitness model, so that model must carry the coupling. Physics- and simulator-based optimizers do carry it through a vehicle model, but they optimize a racing line rather than a driver's inputs (Cardamone et al., 2010; Klapálek et al., 2024). Learned per-segment time models exist in sim racing but describe no carry-over of state and are not used as an optimizer's fitness (Satujoda & Huggins, 2026). Chained surrogates are established in multistage manufacturing and process optimization (Chen et al., 2004; Geiger et al., 2023) and have been formalized as function networks (Astudillo & Frazier, 2021).

To our knowledge, no work has used a surrogate learned from human telemetry to propagate boundary speed between microsectors inside an evolutionary optimization of driver control KPIs, or measured how that coupling changes the optimized result against an otherwise identical variant in which each microsector's entry speed is fixed at its mean fast-lap value. This thesis therefore adapts an established idea, the chained surrogate, to the optimization of sim-racing driver inputs and tests its effect by ablation. It claims no novelty for the physical coupling itself, for chaining surrogates, for per-segment machine-learning time models or for diagnosing carried-over speed. Per-microsector feature selection follows from the chained surrogate, whose inputs must be ranked against its own targets, and it also answers the limitation stated by Hojaji et al. (2026).

