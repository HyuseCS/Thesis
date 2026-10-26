# Thesis TODOs — Google Doc snapshot, 2026-10-26 (two tabs)

Verbatim export of two tabs from the team Google Doc "Thesis TODOs" (https://docs.google.com/document/d/1CGnMtbTdSsbwPcrbIO2r6esDijB4x9-Oth6HXV78cJ0/edit), read 2026-10-26: "Potential Thesis paper" and "Consultation Reviewer". The other used tabs are in `Thesis_TODOs_Doc_2026-10-24.md`. The Doc is the source of truth; this copy goes stale as soon as the Doc changes.

---

# Potential Thesis paper  

# Potential Thesis Paper

## Extending an ML-EA Framework with a Microsector-Chained Surrogate Model for Sim Racing Performance Optimization

# I. Introduction

## A. Background of the Study

## B. Problem Statement

*Version 1 (2026-10-24). Built from Section 2.8 of the literature review tab.*

An optimizer of sim-racing driver inputs judges each candidate lap only through its fitness model, because no driver drives the lap. In the closest framework (Hojaji et al., 2026), that model scores each microsector independently and links microsectors only through penalties on KPI values, so the speed carried from one microsector into the next is not represented. Optimizers that do carry this coupling need a vehicle model or a simulator, and they optimize a racing line or a single corner, not a human driver’s inputs over a full lap. We found no study that uses a surrogate learned from human telemetry to carry boundary speed between microsectors in an evolutionary optimization of driver control KPIs, or that measures how this coupling changes the optimized result.

## C. Objectives

## D. Significance of the Study

# II. Review of Related Literature

## **A. Introduction and Scope**

This chapter reviews the literature needed to answer one question: how should an evolutionary optimizer of sim-racing driver inputs evaluate a lap whose parts depend on one another? It first establishes why simulator telemetry is a sound source of data for this question (2.2). It then reviews how machine learning has been used to analyse driver performance from such telemetry, and what studies of driving technique show about the inputs that change lap time (2.3). It describes the framework this thesis extends, the genetic algorithm of Hojaji et al. (2026) (2.4). Section 2.5 reviews the physical reasons why the parts of a lap cannot be scored independently. Sections 2.6 and 2.7 review optimizers and learned models that do or do not carry this dependence, together with the known risks of chaining learned models, and 2.8 brings the strands together into the research gap.

Sources were located through Consensus, Google Scholar and arXiv, supplemented by publisher pages. Peer-reviewed full texts were preferred, so that no central claim rests on an abstract alone.

Three terms are used throughout. A microsector is a single corner or a single straight. Hojaji et al. call the same unit a "sector" (2026) or a "segment" (2024b). In this thesis "sector" keeps its usual meaning of an official timing sector, which spans several microsectors. Control KPIs are measures of the driver's inputs, such as brake duration or peak steering angle. Entry, apex and exit speed and microsector time are state or outcome variables, because they result from those inputs. A surrogate is a model that stands in for the true evaluator of a candidate lap, which here would be driving the lap in the simulator.

## **B. Simulator Validity and Reliability**

### **1. What "valid" means for this thesis**

A simulator should not be labelled "valid" or "invalid" as a whole, because its validity depends on the research question and the variables measured (Himmels et al., 2023). Himmels et al. (2023) distinguish two kinds of validity. A simulator has absolute validity when its measurements match those from real driving, and relative validity when effects in the simulator point in the same direction as in real driving. Both kinds compare a simulator with the real world.

This thesis makes no such comparison and does not claim that telemetry from Assetto Corsa Competizione (ACC) is equivalent to real-car telemetry. Its context is sim racing as an esport. The drivers, the laps, the fast reference and the optimized targets all exist inside ACC, and every comparison is made between laps recorded in the same simulator, with the same car, setup, track and conditions. The question is how to drive faster in the simulator, so the data need to be sound for that purpose only. The results are therefore stated for competitive sim racing in ACC, specifically the McLaren 720S GT3 at Brands Hatch, and not for real-world racing. This follows the research the thesis builds on, which treats sim racing performance as an outcome of interest in its own right (Hojaji et al., 2024b, 2026; Joyce et al., 2024).

### **2. Mixed evidence on simulator–real equivalence**

The wider validation literature gives a further reason to keep the claims inside the simulator, because its findings are mixed. A systematic review of driving simulator validation studies reported that roughly half of the simulators examined achieved absolute or relative validity, while about a third produced non-valid results, and that the relationship between simulator fidelity and validity was not straightforward (Wynne et al., 2019) . A comparison of six driving simulators reported good absolute validity for headway distance and lateral position but inconsistent results for driving speed (Himmels et al., 2024) , and speed is a central outcome in this thesis. In an earlier road-safety study, speed showed relative but not absolute validity, because participants drove faster in the real car than in the simulator (Godley et al., 2002). Real racing also places physical load and stress on the driver that a simulator does not reproduce (Holland et al., 2025). Apart from Holland et al. (2025), these studies concern road driving, so they are background rather than direct evidence about ACC.

### **3. Evidence that simulator measures reflect driving skill**

Although the thesis does not depend on it, some studies suggest that measures taken in racing simulators partly reflect real driving skill. In a fixed-base simulator, racing drivers achieved faster lap times, showed higher steering activity and followed a better racing line than non-racing drivers (van Leeuwen et al., 2017), although the sample was small and the simulator was not ACC. In a professional driver-in-the-loop simulator, the slower lap times of amateur drivers came mainly from weaker vehicle handling rather than from their choice of line (von Schleinitz et al., 2022). With consumer racing-simulator hardware running the original Assetto Corsa, lap time correlated with driving-speed measures taken on a research simulator (Tiu et al., 2020), although that study's participants and purpose differ greatly from this one. Together, these findings suggest that what separates fast and slow laps in a simulator is at least partly driving skill and not only familiarity with the game. They are supporting context, and the conclusions of this thesis do not rely on them.

### **4. Precedent for the data and pipeline**

ACC telemetry captured with MoTeC has been used in several peer-reviewed studies of sim racing performance by one research group (Hojaji et al., 2024b, 2026; Joyce et al., 2024), and the main dataset of this thesis is the one published with Hojaji et al. (2024b). Remonda et al. (2021) compared drivers in a professional racing simulator using per-segment telemetry features such as brake point and segment entry and exit speeds, which is a precedent for measuring driver behaviour at the level of individual track sections. The developer states that ACC's tracks are laser-scanned and that its physics simulate modern GT cars (KUNOS Simulazioni, n.d.). These are the developer's own claims, not independent validation, and the thesis does not rely on them.

Separately from validity, the thesis checks the reliability of its measurements, meaning how consistent each KPI is across a driver's recorded laps. The procedure is described in Chapter 3.

## **C. Telemetry-Based Analysis of Driver Performance**

### **1. Predicting and stratifying performance**

A line of work by Hojaji and colleagues has shown that telemetry from ACC can predict how well a sim racer drives. Hojaji et al. (2023) extracted KPIs from ACC telemetry and used support vector machine, XGBoost and random forest feature selection to reduce 84 candidate features to 10 that predict a driver's performance level. Speed, steering and lane-deviation KPIs were among the most informative (Hojaji et al., 2023, 2024a).

Hojaji et al. (2024b) went further and divided each lap at Brands Hatch into 19 segments (their term: 10 straights and 9 turns). They grouped laps into skill levels by applying K-Means clustering to lap time, choosing the number of clusters with the Elbow method and the Silhouette coefficient. The stratification step of this thesis (Chapter 3, Step 2) follows that procedure, and the segment-level dataset published with that study is the main dataset used here.

In these studies, importance is measured against lap-level performance, either a performance class or lap time. They therefore show which KPIs matter for a lap, but not where on the lap they matter.

### **2. Per-corner explanation and coaching**

Bae et al. (2025) moved the unit of analysis to the individual corner. They trained a per-corner skill classifier, explained it with SHAP (Lundberg & Lee, 2017) and used it to generate counterfactual advice that moves a driver toward the expert class. Their "Strategic Features" include a corner's entry maximum velocity, exit maximum velocity and entry minimum velocity. Other systems also give per-corner advice against a reference: Kaufman et al. (2024) derive the reference from a reinforcement-learning agent, and Nunes et al. (2026) generate feedback with a large language model from rule-based diagnoses. Nunes et al. (2026) name "a speed deficit carried over from the previous corner" among their diagnoses, which shows that the carry-over of speed between corners is visible in human sim-racing data.

These coaching systems do not need to model how one corner affects the next. A driver carries out the advice in the simulator, and the simulator's physics enforces the coupling. In Bae et al. (2025), for example, entry and exit speed are features of the same corner, which suits advice that a real driver will act on. A lap produced by an optimizer has no driver to enforce the coupling, so the model that evaluates the lap must carry it instead. In this thesis, entry speed is therefore treated as a state inherited from the previous microsector: it enters the model as a covariate and is never a decision variable.

### **3. Driver inputs that change lap time**

Studies of race driving technique show that lap time responds to the driver's own inputs, which supports control KPIs as the variables to optimize. Trail braking, in which braking continues into corner entry, emerges as the solution of the minimum-time cornering problem under set boundary conditions at the corner exit, and a few parameters of the driver's steering, throttle and brake commands reproduce it across corner geometries (Velenis et al., 2008) . Cornering techniques described by professional drivers can be written as simple families of curves, and the choice between them changed lap time on an autonomous race car (Theodosis & Gerdes, 2011) . On a real Formula Student car, cueing the driver with a braking point computed from a simulation of the section ahead reduced lap time (Peitzmeier et al., 2023) . Drivers also improve lap by lap by correcting earlier errors, an adaptation that race-engineering experts identified and that a learned driver model reproduced (Löckel et al., 2023). Hojaji et al. (2026) likewise report trail-braking duration among the KPIs that changed most in their optimized lap. These studies concern technique within a corner; how the result of one corner carries into the next is taken up in 2.5.

## **D. The Baseline: Hojaji et al. (2026)**

Hojaji et al. (2026) extended this line of work from analysis to optimization, and their framework is the closest prior optimization of human driver inputs in sim racing. A genetic algorithm (GA) evolves a lap encoded as 20 sectors (their term for microsectors: 10 corner-dominant and 10 straight-dominant), each described by a vector of 10 scaled KPIs, to produce an idealized lap for coaching. The data were recorded in ACC with the McLaren 720S GT3 at Laguna Seca.

Each candidate lap is scored as Fitness = T + λ·P, with λ = 0.1. T is "the predicted lap time obtained from the sector-based surrogate model" (Hojaji et al., 2026, p. ). For each microsector, this model takes a baseline time from fast laps and adjusts it linearly by how far that microsector's KPIs deviate from the midpoint of their scaled range, and the adjusted time is clamped to between 90% and 105% of the baseline. The penalty P discourages three kinds of unrealistic candidates: sudden changes in a KPI between consecutive microsectors, unusually large gradients within a microsector, and KPI values beyond predefined physical thresholds. The optimized lap, at about 81–82 s, was reported as "around 4–5 seconds" faster than the fastest human lap (Hojaji et al., 2026) . That lap is judged only by its predicted time, and the paper reports no replay of it in the simulator, so its quality rests on the fitness function alone. It is physically unverified, which is not the same as physically impossible.

The framework has two limitations that this thesis addresses. The first is stated by the authors: feature importance was computed globally rather than per microsector, because reliable segment-specific estimation would require larger datasets (Hojaji et al., 2026) \[verify wording and page\]. The second follows from the fitness equation. Each microsector's time depends only on that microsector's own KPIs, so no speed is passed from one microsector to the next. The penalties limit implausible KPI values and abrupt changes, but they carry no state. A similar limit has been reported for another surrogate used to evaluate racing drivers, whose models "compute each data point isolated from its temporal surrounding" (von Schleinitz et al., 2022).

The two limitations are linked. To rank KPIs for each microsector, the model must predict each microsector's own time and exit speed, and both depend on the speed with which the car enters that microsector (2.5). For this reason, entry speed is included as a covariate in the per-microsector feature selection of this thesis, and the gap named in the problem statement leads directly to the coupling gap. The GA settings and λ are kept unchanged, and the penalty P is rebuilt from the authors' description, so that the fitness is the only change (Chapter 3).

## **E. Physical Interdependence of Microsectors**

Lap-time simulation has long treated speed as continuous along the lap (see Massaro & Limebeer, 2021, for a review). Quasi-steady-state methods integrate the speed profile forward out of one corner and backward from the next, and join the two profiles where they meet (Brayshaw & Harrison, 2005; Kapania et al., 2016; Lenzo & Rossi, 2020; Veneri & Massaro, 2020). The speed at which the car leaves one section of track therefore bounds what is achievable in the next.

It follows that a gain in one microsector can carry a cost into the next. A later, faster entry into a corner may shorten that corner's time but cost exit speed, which then lengthens the following straight. Conversely, a slower entry can buy exit speed that pays off on the straight. This trade-off is this thesis's own reasoning from the mechanism described in the lap-time simulation literature, and it is the "speed trade-off" that Objective 2 refers to.

Optimization studies that score only part of a lap treat exit speed as worth something in its own right, which is consistent with this reasoning. Maniowski (2016) used a GA to optimize a driver's steering, brake and throttle actions through one corner of a multibody vehicle model, with section time and corner-exit velocity as separate criteria . In online time-optimal planning, adding an exit-speed term at the end of the planning horizon brought lap times closer to the offline minimum-lap-time solution than minimizing time alone, and moved the planner between early-apex and late-apex lines (Taddei et al., 2025). In both cases, exit speed matters because it is carried into the track that follows, which is the dependence that the chained surrogate of this thesis represents between microsectors.

Learned models show the same dependence. A data-driven racing-line model performed better when it was given both the preceding and the upcoming track geometry (Garlick & Bradley, 2021).

A fitness function that scores microsectors independently can therefore credit a candidate lap with gains that could not occur together. Evolutionary search is known to exploit such gaps in its evaluator (Lehman et al., 2020) , and optimizing against a learned model in particular tends to find inputs that the model scores well but that lie outside the data it was trained on (Trabucco et al., 2021; Kim et al., 2026). Whether this changes the optimized result in practice is an empirical question, and the ablation in Chapter 3 is designed to answer it.

## **F. Racing Optimizers that Carry the Coupling**

Most optimization research in racing targets autonomous agents rather than human drivers. Learning-based control and reinforcement learning produce fast driving policies, up to champion level in Gran Turismo 7 (Kabzan et al., 2019; Samak et al., 2021; Ghignone et al., 2022; Evans et al., 2023; Lee et al., 2025), and trajectory optimization and racing-line generation solve the lap as a whole (Garlick & Bradley, 2021; Massaro & Limebeer, 2021).

Evolutionary racing-line optimization carries the coupling by evaluating each candidate in a full simulator (Cardamone et al., 2010) or through a forward–backward physics speed profile over track segments (their term), using a GA and CMA-ES (Klapálek et al., 2024). Maniowski (2016) applied a GA to a driver's own actions rather than to the line, but over a single corner and through a multibody vehicle model verified against road tests .

These methods need a vehicle model or a simulator in the loop. They output a racing line, a trajectory, a policy or, for one corner, a set of driver actions, rather than targets for a human driver's inputs over each microsector of a full lap derived from that driver population's telemetry.

Botta et al. (2012) replaced full simulation inside the EA with a cheaper physics-based lap-time estimate, which performed worse. This is the racing precedent for scoring candidates with a surrogate, for the risk that it brings, and for checking a surrogate-optimized lap against something outside the model (Objective 3).

## **G. Learned and Chained Surrogates**

### **1. Surrogates in offline data-driven EAs**

A surrogate stands in for an evaluator that is unavailable or expensive (Jin, 2011). Data-driven evolutionary optimization is called offline when no new data can be generated during the search (Jin et al., 2019), which is the case here: the telemetry is fixed and no simulator is run inside the optimizer. In offline optimization the surrogate is fitted once to historical data, so the search can be trusted only where those data lie (Wang et al., 2019), which is why the GA initializes genes within the training-lap ranges and clips mutated genes to them. Surrogate errors can also accumulate and mislead the ranking of candidates (Liu et al., 2022) , so a difference between optimized laps should be trusted only if it is larger than the surrogate's own error.

By this definition the baseline's linear scaler is already a surrogate, and Hojaji et al. (2026) call it a "sector-based surrogate model". The thesis replaces it with a learned surrogate and so inherits the risks noted in 2.5 and 2.6.

### **2. Learned lap-time models in racing**

Learned lap-time models already exist in racing. A Gaussian-process surrogate of whole-lap time guides Bayesian trajectory optimization (Nam et al., 2026), and LightGBM predicts per-segment time (their term) from car setup in Assetto Corsa, reconstructing held-out lap time with 0.223 s mean absolute error (Satujoda & Huggins, 2026). Neither carries state from one part of the lap to the next: Nam et al. score the whole lap, and Satujoda and Huggins describe no carry-over between segments and report that "Telemetry-derived quantities were not used to generate the winning setup".

Gradient-boosted trees (Chen & Guestrin, 2016) suit tabular KPI data. In large benchmarks they matched or outperformed deep learning on medium-sized tabular data, with less tuning (Grinsztajn et al., 2022; Shwartz-Ziv & Armon, 2022), and light tuning of a boosted-tree model often mattered more than the choice of model family (McElfresh et al., 2023). XGBoost, LightGBM and CatBoost differ little in accuracy (Bentéjac et al., 2021), and gradient-boosted trees have served as EA surrogates (Mao et al., 2024). Their weakness for optimization is that they interpolate only: predictions degrade when a feature lies outside the training range (Malistov & Trushin, 2019) , which is a further reason to keep the search within the observed KPI ranges.

### **3. Chained surrogates outside racing**

Outside racing, linking per-stage models so that one stage's output is the next stage's input is established. It is formalized as function networks (Astudillo & Frazier, 2021; Kiroirwal et al., 2026) and has been applied with a GA to fed-batch fermentation (Chen et al., 2004) and with stacked Gaussian processes to multistage manufacturing (Geiger et al., 2023). In linked Gaussian-process emulators of computer models, linking per-stage emulators predicted a chain better than one emulator of the whole (Kyzyurova et al., 2018; Sanson et al., 2019). Geiger et al.'s comparison of joint and cascaded optimization parallels the coupled-versus-independent ablation used here.

Chaining carries two documented risks. When a learned one-step model is applied repeatedly, with its output fed back as its next input, its errors compound and move its inputs away from the training distribution (Venkatraman et al., 2015; Lambert et al., 2022). In regressor chains, a model trained on the true values of an upstream target but run on predicted values faces a mismatch between the inputs it was trained on and those it receives (Spyromitros-Xioufis et al., 2016). The surrogate in this thesis is trained on measured entry speeds but, inside the fitness, receives chained predictions, so Chapter 3 rolls each test lap through the full chain rather than judging the surrogate on per-microsector error alone.

### **4. Interpreting and validating the surrogate**

The methods used to select, validate and compare in Chapter 3 also rest on established work. TreeSHAP computes exact SHAP values for tree ensembles, avoids the inconsistency of gain-based importance, and builds global importance by aggregating local explanations (Lundberg et al., 2020). SHAP values explain the model rather than causation, and standard approximations can mislead when features are correlated (Aas et al., 2021), a limitation that applies to correlated control KPIs. Because laps are nested within drivers, random cross-validation would underestimate error; blocked or grouped validation is recommended whenever such dependence exists (Roberts et al., 2017), and non-independence between training and test data is a recognized form of leakage (Kapoor & Narayanan, 2023). Results of evolutionary runs rarely meet the assumptions of parametric tests, so paired comparisons of algorithm variants over seeds are usually made with nonparametric tests such as the Wilcoxon signed-rank test (Derrac et al., 2011; Carrasco et al., 2020).

## **H. Synthesis and Research Gap**

### **1. Synthesis**

Table 2.1 compares the closest studies on the three properties this thesis combines: a time model learned from human telemetry, state carried across microsector boundaries inside the evaluator, and driver control KPIs as decision variables. Three groups emerge. Coaching systems give advice to a driver, whose simulator enforces the coupling. Physics- and simulator-based optimizers carry the coupling through a vehicle model, but they optimize a racing line, a control policy or, over a single corner, a driver's actions on a vehicle model. Learned surrogates do not chain in racing, and where chained surrogates are used in other fields, they do not involve drivers.

*Table 2.1. Closest studies compared on the properties combined in this thesis. Units are given in each study's own term; "not described" means the paper does not describe it, not that it is absent.*

### **2. Research gap**

Most optimization research in racing targets autonomous agents (Kabzan et al., 2019; Evans et al., 2023; Lee et al., 2025). The closest optimization of human driver KPIs in sim racing (Hojaji et al., 2026) ranked KPIs globally, noting that estimating importance for each microsector would require larger datasets, and scored each microsector independently before summing, relying on penalties for abrupt transitions, within-microsector gradients and out-of-range values. Coaching systems advise a real driver (Bae et al., 2025; Kaufman et al., 2024; Nunes et al., 2026), so the driver and the simulator's physics enforce the coupling between microsectors. An optimizer's candidate laps, by contrast, exist only inside its fitness model, so that model must carry the coupling. Physics- and simulator-based optimizers do carry it through a vehicle model, but they optimize a racing line (Cardamone et al., 2010; Klapálek et al., 2024) or, over a single corner, a driver's actions on a calibrated vehicle model (Maniowski, 2016), and they value exit speed for the same reason (Taddei et al., 2025). Learned per-segment time models exist in sim racing but describe no carry-over of state and are not used as an optimizer's fitness (Satujoda & Huggins, 2026). Chained surrogates are established in multistage manufacturing and process optimization (Chen et al., 2004; Geiger et al., 2023) and have been formalized as function networks (Astudillo & Frazier, 2021), and their known risks, compounding error and a mismatch between training and prediction inputs (Venkatraman et al., 2015; Spyromitros-Xioufis et al., 2016), mean that a chained fitness has to be checked by rolling whole laps through the chain.

In the literature reviewed here, we did not find a study that uses a surrogate learned from human telemetry to propagate boundary speed between microsectors inside an evolutionary optimization of driver control KPIs, or that measures how that coupling changes the optimized result against an otherwise identical variant in which each microsector's entry speed is fixed at its mean fast-lap value. This thesis therefore adapts an established idea, the chained surrogate, to the optimization of sim-racing driver inputs and tests its effect by ablation. It claims no novelty for the physical coupling itself, for valuing exit speed in lap optimization, for chaining surrogates, for per-segment machine-learning time models or for diagnosing carried-over speed. Per-microsector feature selection follows from the chained surrogate, whose inputs must be ranked against its own targets, and it also answers the limitation stated by Hojaji et al. (2026).

  
  

  

# III. Methodology

# IV. Presentation, Analysis, and Interpretation of Data

# V. Summary, Conclusions, and Recommendations  

# Consultation Reviewer  

# **Consultation Reviewer**

## **What we say, what we don’t claim, and short answers for the adviser**

24 October 2026

Read this before the consultation. It follows the “for consultation \#2” tab and the “refined methodology” tab as they stood on 24 October 2026. Section 3 is the most important part: each row says what to avoid and what to say instead. Section 6 lists places where the current consultation tab still says more than we can defend, in case the adviser points at them.

# **1. The study in 30 seconds**

Hojaji et al. (2026) used a genetic algorithm (GA) to find an “idealized” lap of driver-input KPIs. Their fitness function scores each microsector on its own, using a hand-written formula that scales a baseline time, and adds the times up. So a change in one microsector can never change the predicted time of the next one. In real driving, the speed you leave one microsector with is the speed you enter the next one with.

We keep their GA and its settings, and change only the fitness function. A trained XGBoost surrogate model predicts each microsector’s time and exit speed from its KPIs and its entry speed. The coupled fitness function calls this model microsector by microsector and passes each predicted exit speed on as the next entry speed. We then run the same GA with a coupled and a microsector-independent fitness function and measure what the coupling changes.

**Our one contribution:** the coupled (microsector-chained) fitness function, and the comparison that measures its effect. Everything else (dataset, GA, SHAP, clustering) is a method choice, not a contribution.

**Title in the tab:** “Extending an ML-EA Framework with a Microsector-Chained Surrogate Model for Sim Racing Performance Optimization”.

# **2. What the study does**

|  |  |  |
| :-: | :-: | :-: |
| \*\*Step\*\* | \*\*What we do\*\* | \*\*Detail to remember\*\* |
| Data | Hojaji et al. (2024) public dataset, CC BY 4.0 | Brands Hatch, McLaren 720S GT3, ACC. 826 laps, 166 drivers raw. Already split into 19 microsectors (9 corners, 10 straights). 8 ready-made driver-input KPIs plus summary statistics per channel |
| External test set | Our own laps | 10 drivers × 30 laps, ACC v1.10.4, hom  of e rigs (minimum wheel and pedals), instruction sheet and setup file, driver form, same MoTeC workspace. Never used for training, feature selection or tuning |
| Candidate KPIs | Driver inputs only | 8 dataset KPIs plus brake, throttle, steering and gear statistics. Speeds, accelerations, lane deviation, ABS/TC activity are excluded (they describe the car, not the driver) |
| Cleaning | Remove in/out-laps, standing starts, invalid laps, then \|z\| \\\> 3 on lap time across all laps | Final counts reported after filtering |
| Split | 70/30 by driver | No driver in both sets; laps kept whole |
| Clustering | K-Means on lap time only; k by Elbow and Silhouette | Fastest cluster = Fast reference (entry speeds, KPI medians, Fast-lap test scores) |
| Feature selection | Pearson pre-filter (drop \|r\| \\\< 0.1 with both targets), one screening XGBoost, TreeSHAP | Mean \|SHAP\| per microsector, normalized, averaged over both targets and all microsectors; top K = 10 common to all microsectors |
| Surrogate model | One multi-output XGBoost shared by all 19 microsectors | (10 KPIs, entry speed, microsector index) → (microsector time, exit speed). Grid search in 10-fold CV grouped by driver, refit on all training laps |
| Surrogate tests | Test set, then external set once | MAE and R² overall and on Fast-cluster laps; lap rollout (chain predictions through a whole recorded lap and compare lap time and boundary speeds) |
| Optimization | Hojaji’s GA unchanged | Pop 120, 200 generations, two-point crossover 0.8, Gaussian mutation SD 0.05 at 0.15 per gene, elitism 2, tournament 3. 190 genes (19 × 10). Entry speed of microsector 1 fixed at the Fast-cluster mean. No 90–105% clamp |
| Fitness | Fitness = T + λP | λ = 0.1 inherited from Hojaji without tuning; P rebuilt from their description |
| Comparison | Coupled vs microsector-independent fitness | Independent variant: each microsector’s entry speed fixed at its Fast-cluster training mean. 30 paired seeds. Every best lap re-scored by the chained surrogate. Wilcoxon signed-rank test; a difference counts only if larger than the rollout lap-time error |
| Output | Per-microsector KPI targets | Reported against the Fast-cluster median, e.g. “microsector 7: hold trail braking 0.2 s longer than the fast-lap median” |

# **3. What we do NOT claim, and what to say instead**

|  |  |  |
| :-: | :-: | :-: |
| \*\*Don’t say\*\* | \*\*Say instead\*\* | \*\*Why\*\* |
| “We are the first to…” / “No one has done this.” | “Hojaji et al. (2026) score each microsector on its own. We replace that with a trained surrogate model chained by exit speed.” If pressed: “We did not find a study that does this for human driver inputs.” | We can’t prove a negative, and the group decided not to make “first” claims. |
| “Learned surrogate fitness” or “the surrogate is the fitness.” | “The surrogate model predicts a microsector’s time and exit speed. The coupled fitness function calls it microsector by microsector and adds the penalty.” | Two separate parts; mixing them confuses what is trained and what is the GA’s scoring rule. |
| “Our results apply to real racing.” / “Sim telemetry is the same as real telemetry.” | “Results are stated for competitive sim racing in ACC. Every comparison is between laps in the same simulator, car and track.” | We make no comparison with real driving (Himmels et al., 2023: validity depends on the question). |
| “We solve Hojaji’s data problem.” / “We have enough data for per-microsector models.” | “We don’t fit 19 separate models. One model is pooled across all microsectors (about 15,700 rows before filtering), and the GA uses one common set of 10 KPIs. Per-microsector importance is reported as descriptive.” | Our dataset is about the same size as theirs. Hojaji said segment-specific estimation needs larger datasets; we don’t claim to disprove that. |
| “We improved the GA.” / “DE would do better.” | “The GA is kept exactly as Hojaji’s, so the fitness function is the only change. Comparing optimizers such as DE is future work.” | Changing the optimizer would mix two effects. |
| “λ = 0.1 is the best value.” / “We used Hojaji’s penalty formula.” | “λ = 0.1 is inherited from Hojaji without tuning; their paper gives no rationale and tests no other value. P is rebuilt from their description, because they don’t report its formulas or thresholds.” | Their Sec. 3.5.2 only says what each penalty discourages. |
| “Our optimized lap is achievable / validated / drivable.” | “The optimized targets are judged only by the surrogate model. They are not driven in ACC; whether drivers can reach them is outside our scope.” | No step checks the optimized lap against driving. The human vs EA lap comparison was dropped. |
| “The external laps show the targets work for real drivers.” | “The external laps test whether the surrogate model’s predictions hold for new drivers, a newer ACC version and different hardware.” | They are used only for MAE, R² and rollout of the surrogate. |
| “We replicate Hojaji et al. (2026).” / “Our lap is X s faster than theirs.” | “We reuse their GA settings and fitness structure. Full replication is out of scope: no code was released and they used Laguna Seca.” | Different track and data; lap times are not comparable. |
| “Coupling between corners is our discovery.” / “Chained models are new.” | “Speed coupling is standard in lap-time simulation (Kapania et al., 2016), and chained surrogates exist in other fields (e.g. manufacturing, Geiger et al., 2023). What we change is that the GA’s fitness for human driver inputs carries this coupling.” | The physics and the chaining idea are not ours. |
| “Hojaji’s results are wrong.” / “Their gain is just the clamp.” | “Their fitness scores microsectors independently, so it can’t represent speed carried from one microsector to the next. We measure what changes when it does.” | Critique the design, not the authors. See Q22 if the clamp comes up. |
| “Coaching systems like Bae et al. ignore coupling.” | “A coaching system doesn’t need it: a real driver carries out the advice and the simulator’s physics enforces the coupling. An optimized lap exists only inside the fitness model, so the model itself has to carry it.” | Bae’s approach isn’t flawed for its purpose. |
| “Coupling will make the laps faster.” | “Coupling should stop the fitness from crediting gains that the next microsector can’t deliver. We measure how much independent scoring overstates the gain. No difference is also a result.” | Our hypothesis is about realism of the score, not a faster lap. |
| “SHAP shows which inputs cause faster laps.” | “SHAP shows which inputs the model relies on. It explains the model, not causation, and correlated KPIs share credit.” | Stated limitation. |
| “Because the GA is identical to the baseline, the comparison isolates coupling.” | “Both variants use the same surrogate model, GA, penalty and random seeds, so the only difference is where entry speed comes from.” | Keeping the GA identical to Hojaji is what makes the fitness the only change from the baseline; the shared setup is what isolates coupling within our comparison. |
| “Racing line” / “trajectory” | “Driver-input targets: braking, throttle, steering per microsector.” | We don’t optimize a path on the track. |
| “Sector” | “Microsector” (one corner or one straight). | A sector is a larger official timing section. Hojaji calls microsectors “sectors” (2026) or “segments” (2024). |
| “The KPIs are validated.” | “We check KPI consistency across a driver’s laps (coefficient of variation) and report low-consistency KPIs.” | That is consistency (reliability), not validity. |
| “Works for any track or car.” | “One track (Brands Hatch), one car (McLaren 720S GT3), one simulator.” | Scope. |

# **4. Terms to get right**

|  |  |
| :-: | :-: |
| \*\*Term\*\* | \*\*Meaning\*\* |
| Microsector | One corner or one straight. 19 at Brands Hatch. |
| Control KPI | A driver-input measure (e.g. brake duration, trail-braking duration, peak steering). The only feature candidates and the only GA genes. |
| State / outcome variables | Entry speed, exit speed, microsector time. They result from the inputs, so they are never genes. |
| Surrogate model | The trained XGBoost: (KPIs, entry speed, microsector index) → (time, exit speed). Stands in for actually driving the lap. |
| Coupled fitness function | Scores a GA individual by calling the surrogate microsector by microsector from a fixed first entry speed, passing each exit speed on as the next entry speed. Fitness = T + λP. |
| Microsector-independent fitness | Same surrogate, but each microsector’s entry speed is fixed at its Fast-cluster mean instead of coming from the previous prediction. |
| Lap rollout | Running a recorded test lap through the chained surrogate from its real first entry speed and comparing predicted lap time and boundary speeds with the recorded ones. The strict accuracy test, because errors add up along the lap. |
| Fast reference | The fastest K-Means cluster of lap times. |
| Lap closure | Whether the last exit speed matches the first entry speed. Not enforced; the gap is reported. |

# **5. Likely adviser questions with short answers**

**Q1. What exactly is new here?** The coupled fitness function: the GA’s score is computed by chaining a trained surrogate model through the lap, so a change in one microsector affects the next. We measure its effect by comparing it with a microsector-independent fitness, with everything else held equal.

**Q2. Isn’t this just Hojaji’s study again?** No. We keep their GA so the comparison is fair, but we replace their fitness. Their microsector times come from a hand-written scaling formula with no link between microsectors. Ours come from a trained model chained by exit speed, and we test what that changes.

**Q3. Their paper also used XGBoost. What’s different?** They used XGBoost, RF and SVM only as fast/slow classifiers to rank features. Their fitness was not a trained model. Ours is a regression model that predicts time and exit speed and is used inside the fitness.

**Q4. Why not change the GA too, or use DE, CMA-ES or reinforcement learning?** Changing the optimizer would mix two effects. With the GA fixed, any difference comes from the fitness. Optimizer comparison is future work.

**Q5. Why XGBoost for the surrogate?** It performs well on tabular data, handles nonlinear interactions, supports multi-output regression, and is fast enough to be called 19 times per individual over 120 × 200 evaluations. It also matches the model family used in this line of work.

**Q6. Why is entry speed not a gene?** It is a result of the previous microsector’s inputs. If the GA could set it, it could “teleport” speed into a corner. Only the first entry speed is set, and it is fixed at the Fast-cluster mean so the GA can’t gain from a faster start.

**Q7. How do you know the surrogate is accurate enough?** Grouped cross-validation during tuning, MAE and R² on held-out drivers (overall and on Fast-cluster laps), the lap rollout (the strict test, since errors accumulate when chained), and once on the external laps.

**Q8. Errors add up when you chain 19 predictions. Isn’t that a problem?** Yes, and that’s why the lap rollout is part of the evaluation. Its lap-time error is also the threshold: a difference between the two fitness variants counts only if it is larger than that error.

**Q9. You judge both variants with the chained surrogate. Doesn’t that favour the coupled one?** It is the only evaluator available without driving the laps. It is validated separately by the rollout, and differences count only above its error. We state this as a limitation.

**Q10. Can drivers actually reach the optimized targets?** We don’t test that. The targets are judged only by the surrogate and are not driven in ACC. We present them as targets relative to the fast-lap median, not as a proven lap.

**Q11. What is the external dataset for, then?** To test whether the surrogate’s predictions hold for new drivers, a newer ACC version (v1.10.4) and different home hardware. It is never used for training, feature selection or tuning.

**Q12. Are 10 drivers enough?** It is an external check of the surrogate, not the training data. Results are reported per driver and pooled, so the reader sees the spread. More drivers would make it stronger, and mixed hardware is a stated limitation.

**Q13. Why Brands Hatch, not Laguna Seca like the baseline?** The Hojaji et al. (2024) Brands Hatch dataset is public, already divided into microsectors and licensed for reuse (CC BY 4.0). Our comparison is between two fitness functions on the same data, so it doesn’t need the baseline’s track.

**Q14. Hojaji said per-microsector importance needs more data, and your dataset is about the same size. How do you handle that?** We don’t claim to have solved it. We fit one model pooled across all microsectors (about 15,700 rows before filtering and splitting) instead of 19 small ones, and the GA uses one common set of 10 KPIs, so no decision rests on a single microsector’s ranking. Per-microsector importance is reported as descriptive, with that limitation stated.

**Q15. Why K = 10?** To match Hojaji et al. (2026), so the number of genes per microsector is the same as the baseline.

**Q16. Why the Pearson |r| \< 0.1 cut-off?** It is a light pre-filter that drops only KPIs with almost no linear relation to either target (0.1 is a small effect by Cohen, 1988). The ranking itself is done with SHAP.

**Q17. Why SHAP and not built-in XGBoost importance?** TreeSHAP gives consistent per-feature attributions that can be grouped by microsector, which gain-based importance doesn’t do cleanly. It is a method choice, not a contribution, and it explains the model, not causation.

**Q18. Why split by driver?** So the model is tested on drivers it never saw. Otherwise a driver’s style leaks from training into testing.

**Q19. Why cluster on lap time only?** It follows Hojaji et al. (2024), and it passes no KPI information into training. The Fast cluster is only a reference for entry speeds, KPI medians and the Fast-lap test score.

**Q20. Where do λ and P come from?** λ = 0.1 is taken from Hojaji et al. (2026) without tuning; their paper gives no source or rationale and tests no other value. P is rebuilt from their description (sudden KPI changes between microsectors, large gradients within a microsector, values beyond physical limits), because they don’t report the formulas or thresholds.

**Q21. Why drop their 90–105% clamp?** The clamp bounded their hand-written formula. The trained surrogate replaces that formula, and both of our variants are treated the same way.

**Q22. (If raised) Isn’t Hojaji’s optimum just the clamp floor?** We noticed that 90% of their 91.05 s baseline is about 81.9 s, close to the 81–82 s they report, but the paper doesn’t discuss it and we don’t build our argument on it. Our point is only that their fitness scores microsectors independently.

**Q23. How are the GA genes scaled? An SD of 0.05 in what unit?** Genes are min–max scaled to \[0, 1\] using each KPI’s training range (following Hojaji, Sec. 3.5.1), so the SD is 5% of that range. Mutated genes are clipped to \[0, 1\], and genes are decoded to original units before the surrogate is called.

**Q24. What if coupling makes no difference?** That is still a result: it would show independent scoring is adequate for this setup. The Wilcoxon test with the rollout threshold tells us either way.

**Q25. Why 30 seeds and Wilcoxon?** The GA is random, so each variant is run with the same 30 seeds to pair the runs. Wilcoxon signed-rank is a paired test that doesn’t assume normally distributed differences.

**Q26. How does a driver use the output?** Each optimized target is compared with the Fast-cluster median for that KPI in that microsector and phrased as an instruction, e.g. “microsector 7: hold trail braking 0.2 s longer than the fast-lap median”.

**Q27. Does this help real-world racing drivers?** Not claimed. The results are stated for competitive sim racing in ACC.

# **6. Places in the current consultation tab to watch**

These were found in the 24 October check (Consultation\_Check\_2026-10-24.docx) and were still in the tab when this reviewer was written. If you fix them before the meeting, skip this section; if not, use the wording on the right when you speak.

|  |  |  |
| :-: | :-: | :-: |
| \*\*Where\*\* | \*\*Current text\*\* | \*\*What to say\*\* |
| Optimization, GA bullet | Gives SD 0.05 without saying genes are scaled | “Genes are min–max scaled to \\\[0, 1\\\], so the SD is 5% of each KPI’s training range.” (Q23) |
| Testing, Limitations | Doesn’t say the targets are judged only by the surrogate | “The optimized targets are judged only by the surrogate and not driven in ACC.” (Q10) |
| Significance, Sim racers | “they do not assume an entry speed that the preceding microsector cannot deliver” and “shows whether the targets remain usable outside the dataset” | “…according to the surrogate model” and “shows whether the surrogate model’s predictions hold for new drivers and equipment.” |
| Significance, Researchers | “Because the genetic algorithm is kept identical to the baseline, the comparison … isolates the effect of microsector coupling” | “Both variants share the surrogate, GA, penalty and seeds, so the comparison isolates coupling.” |
| Data bullet | “our own dataset … for further validation of the model” | “an external test of the surrogate model” |
| Diagram, first box | “165 drivers, 817 laps after cleaning” | “826 laps from 166 drivers before cleaning; final counts after filtering are reported.” |
| Refined methodology, Proposed Solution | “keeps the optimizer, its settings and its initialization identical” | Initialization is within the training-lap ranges, not the full dataset, so say “the optimizer and its settings are identical”. |
| Old objectives (tab now labelled “deprecated 2”) | Objective 3: “validating the generated racing lines against human baseline telemetry”; Objective 2: “corner interdependencies … sequential track sectors” | If the adviser asks about objectives: “We optimize per-microsector driver-input targets with Hojaji’s GA using a coupled fitness, and measure the coupling’s effect against a microsector-independent fitness.” |

# **7. Numbers to have ready**

|  |  |
| :-: | :-: |
| \*\*Item\*\* | \*\*Value\*\* |
| Hojaji et al. (2026) baseline | Laguna Seca, McLaren 720S GT3, 135 drivers, 1,180 raw laps, 865 after cleaning, 20 microsectors × 10 KPIs |
| Their reported optimized lap | About 81–82 s, 4–5 s faster than the fastest human lap; never driven |
| Our main dataset | Brands Hatch, 826 laps, 166 drivers raw; 19 microsectors; final counts reported after filtering (don’t quote a final number yet) |
| Rows for the pooled model | About 15,700 (826 × 19) before filtering and splitting |
| External set | 10 drivers × 30 laps, ACC v1.10.4 |
| GA | Pop 120, 200 generations, crossover 0.8, mutation 0.15 per gene with SD 0.05, elitism 2, tournament 3, 190 genes |
| Fitness | T + λP, λ = 0.1 |
| Comparison | 2 fitness variants × 30 paired seeds, Wilcoxon signed-rank |
| Split and tuning | 70/30 by driver; 10-fold CV grouped by driver |

  
  
