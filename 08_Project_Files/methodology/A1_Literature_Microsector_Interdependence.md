# A1: Literature on micro-sector interdependence

For: "The Kinematic Disconnect" paragraph of the methodology justification (review item A1).
Searched 2026-09-25: Consensus, then Google Scholar / arXiv via web search. Open-access versions are preferred and linked where one exists.

## Bottom line

- **Well supported:** speed, and therefore time, in one part of a lap depends on the sections before and after it. Every standard lap-time simulation method builds this in: speed profiles are integrated forward out of one corner and backward from the next, then joined. Sources 1 to 4 below.
- **Supported in general:** evolutionary algorithms exploit weaknesses in a fitness function or surrogate model (sources 5 to 6).
- **Not found:** a paper showing that *sector-independent fitness in a sim-racing EA* produces unphysical laps. Nobody has published this about Hojaji et al. (2026). It is **your claim**. Write it as an argument that follows from sources 1 to 6, and ideally demonstrate it with your own baseline replication (for example, show an EA-optimized lap in which sector n's exit speed does not match sector n+1's entry speed).

---

## 1. Physical coupling between track sections

### 1.1 Garlick & Bradley (2021), *Vehicle System Dynamics*, already in Thesis.bib
Open access: https://arxiv.org/pdf/2102.02315
Quoted from the full text, Section 2.2:
> "the racing line at any point on the circuit is influenced by the preceding curvature (thus resulting in the current vehicle position) and the upcoming curvature of the circuit."

They found that their model improved when it was given track information both before and after the current position ("bidirectional Foresight").
**Use for:** the most direct statement that no track section can be judged in isolation. It is already in your library.

### 1.2 Veneri & Massaro (2020), "A free-trajectory quasi-steady-state optimal-control method for minimum lap-time of race vehicles", *Vehicle System Dynamics*
Open-access author version: https://www.research.unipd.it/bitstream/11577/3297111/2/2019%20-%20A%20free-trajectory%20quasi-steady-state%20optimal-control%20method%20for%20minimum%20lap-time%20of%20race%20vehicles%20-%20MM.pdf
Quoted from Section 3.2, describing the standard apex-finding method:
> "The speed profiles between two apexes (acceleration out of turn i and deceleration into turn i+1) are then connected at their intersection point."

**Use for:** the time spent between two corners is set jointly by the exit of turn i and the entry of turn i+1. This is exactly the n → n+1 coupling your surrogate models.

### 1.3 Kapania, Subosits & Gerdes (2016), "A Sequential Two-Step Algorithm for Fast Generation of Vehicle Racing Trajectories", *J. Dynamic Systems, Measurement, and Control* 138(9), doi:10.1115/1.4033311
Open access: https://arxiv.org/pdf/1902.00606
Quoted from Section 3:
> "The next step is a forward integration step, where the velocity of a given point is determined by the velocity of the previous point and the available longitudinal force."
> "...the backward integration step occurs, where the available longitudinal force for deceleration is again constrained by the lateral force demand on all tires."

Quoted from Section 4.1:
> "minimizing curvature is not the same as minimizing lap time and provides no guarantee of finding the time-optimal solution."

**Use for:** velocity at a point is a function of velocity at the previous point, which is your v_entry,n+1 = v_exit,n rule. The backward pass also supports combined lateral and longitudinal grip (review item B1).

### 1.4 Lenzo & Rossi (2020), "A Simple Mono-Dimensional Approach for Lap Time Optimisation", *Applied Sciences* 10(4):1498, doi:10.3390/app10041498
Open access (CC BY): https://www.mdpi.com/2076-3417/10/4/1498
Quoted:
> "The acceleration and braking zones are worked out by forward and backward integration, respectively, after and before each apex, and the speed profiles between the apexes are connected at their intersection points"

**Use for:** a second open-access description of the same mechanism. It is a short, citable source for the "standard practice" statement.

### Optional supporting sources (abstract only, paywalled)
- Heilmeier et al. (2020), "Minimum curvature trajectory planning and control for an autonomous race car", *VSD* 58(10), doi:10.1080/00423114.2019.1631455. The abstract says the velocity profile is computed "using a forward-backward-solver that considers the velocity dependent longitudinal and lateral acceleration limits". Its authors are well known (TUM, Roborace).
- Braghin et al. (2008), "Race driver model", *Computers & Structures*, doi:10.1016/j.compstruc.2007.04.028. The abstract calls the optimal trajectory "the best compromise between the shortest track and the track that allows to achieve the highest speeds". Use it for trade-offs at lap level rather than sector level.

## 2. Evolutionary search exploits fitness-model flaws

### 2.1 Lehman, Clune, Misevic et al. (2020), "The Surprising Creativity of Digital Evolution", *Artificial Life* 26(2)
Open access: https://arxiv.org/abs/1803.03453
Abstract: evolving systems end up "subverting their intentions, exposing unrecognized bugs in their code". The paper collects many cases of EAs exploiting fitness functions and simulators.
**Use for:** the general claim that an EA "can exploit the fitness function". Keep it general; it is not about racing.

### 2.2 Wang, Jin, Sun & Doherty (2019), "Offline Data-Driven Evolutionary Optimization Using Selective Surrogate Ensembles", *IEEE Trans. Evolutionary Computation*
Abstract: "Since the surrogate models solely depend on the given historical data, the optimization algorithm is able to search only in a very limited decision space".
**Use for:** your setup is offline and data-driven. This source supports bounding DE to the observed data range (review item A5). It also frames Hojaji's linear scaler and your XGBoost model as the same kind of object, a surrogate.

### 2.3 Jin (2011), "Surrogate-assisted evolutionary computation: Recent advances and future challenges", *Swarm and Evolutionary Computation*
The standard survey of surrogate-assisted EAs (1,397 citations). Use it to position Step 4 and Step 5. Abstract only checked.

## 3. Related sim-racing work (for Step 3, sector-level analysis)
- Bae et al. (2025), "Data-Driven Driver Training via Counterfactual and Language-Based Guidance in Racing Scenarios", *IEEE Access*. It classifies skill **per corner** and gives SHAP-based counterfactual coaching per corner. This is the closest prior work to your sector-level feature selection, and its corner-by-corner treatment is another example of isolated evaluation. Checked from the abstract only; I could not open the full text.
- Kegelman et al. (2017), *VSD*. Real race data show that drivers "anchor their racing lines at specific locations" and that there is "a family of solutions in terms of paths and speed". Use it to argue that one optimal set of KPIs per sector is a simplification.
- Remonda et al. (2021), *PLOS ONE* (open access). Compares human and RL driving in a professional simulator using telemetry and supports simulator data validity (review item E3).

---

## Suggested rewrite of the A1 sentence (for you to adapt)

> Lap-time simulation has long treated a lap as a continuous problem in which the speed at any point is bounded by the sections before and after it: speed profiles are integrated forward from one corner's apex and backward from the next, and joined where they meet (Kapania et al., 2016; Veneri & Massaro, 2020; Lenzo & Rossi, 2020). Likewise, data-driven racing-line models perform better when they are given both preceding and upcoming track geometry (Garlick & Bradley, 2021). The baseline fitness function of Hojaji et al. (2026) does not reflect this coupling: each sector time is scaled from its own KPIs alone and then summed. We therefore argue that it permits candidate laps whose sector-level gains are mutually inconsistent, for example a later, faster corner entry that is credited to sector n without its cost to the exit speed carried into sector n+1. Because evolutionary search is known to exploit any such gap in its fitness model (Lehman et al., 2020), this motivates a fitness function that propagates boundary state between sectors.

This wording makes no claim about Hojaji et al. that they did not make, and it cites every factual claim.

## To add to Zotero (by DOI)
- 10.1115/1.4033311 (Kapania 2016)
- 10.3390/app10041498 (Lenzo 2020)
- 10.1080/00423114.2019.1608349 (Veneri 2020; confirm in Zotero, I did not verify this DOI directly)
- 10.1162/artl_a_00319 (Lehman 2020; confirm in Zotero)
- 10.1109/TEVC.2018.2834881 (Wang 2019; confirm in Zotero)
- 10.1016/j.swevo.2011.05.001 (Jin 2011; confirm in Zotero)
- Optional: 10.1080/00423114.2019.1631455 (Heilmeier 2020), 10.1016/j.compstruc.2007.04.028 (Braghin 2008)

---

## Making A1 hold up without relying on argument alone (added 2026-09-25)

Split the claim into parts. Each part then rests on something checkable.

1. **A published fact about the baseline:** Hojaji et al. (2026) define Fitness = T + λ·P, where T sums sector times and each sector time is scaled only from that sector's own KPI vector. The fitness therefore has no term linking sector n to sector n+1. Cite their method section; this is a property of their equation, not an opinion.
2. **A published fact about vehicle dynamics:** in real lap-time physics, sector n+1's time depends on sector n's exit speed (Kapania et al., 2016; Veneri & Massaro, 2020; Garlick & Bradley, 2021).
3. **Evidence from the baseline's own results:** their EA lap (about 81–82 s, "around 4–5 seconds" faster than the fastest human lap) is a surrogate prediction and was never driven or replayed in the simulator. Its Table 1 reports simultaneous increases in average speed (×1.11), lateral acceleration (×1.22) and longitudinal acceleration (×1.62) alongside *less* total braking (×0.93). Say "physically unverified", not "unphysical". The lap time on its own is not implausible for elite ACC drivers. Check whether the Table 1 ratios compare against the average human lap or the best human lap before quoting them.
4. **Your own evidence (strongest):**
   - *Preliminary data analysis:* on your telemetry, test whether v_exit,n predicts Δt_(n+1) after controlling for sector n+1's own KPIs (partial correlation, or the gain in R² from adding v_exit,n). A significant effect shows, in real driver data, the coupling the baseline omits. This is Step 3's analysis anyway.
   - *Baseline replication:* run the baseline GA and measure boundary-speed consistency in its optimized laps, for example the implied |v_exit,n − v_entry,(n+1)|, or pass its KPIs through your chained surrogate and compare lap times.
   - State this as a hypothesis or research question, e.g. H1: "Sector-independent fitness overestimates the attainable lap-time gain relative to a boundary-coupled fitness." Testing it becomes part of your contribution.
