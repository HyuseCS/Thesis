# Section C fixes (paste-ready)

Based on the Google Doc as read on 2026-09-26 at about 03:03 UTC. Grouped by where each fix goes. Item numbers match `Methodology_Review_v1.md`.

## Step 1

**C5 (title).** Replace "Sequential Preprocessing & Micro-Sector Granulation" with:
> Sequential Preprocessing and Microsector Segmentation

**C3 (outlier filter).** Replace "Remove in-laps, out-laps, and invalid laps (∣z∣>3 filter)." with:
> Remove in-laps, out-laps and invalid laps, then remove outlier laps whose lap time lies more than three standard deviations from the mean of that driver's laps (|z| > 3).

**C4 + C10 (microsectors and M).** Replace "Slice continuous telemetry into ordered microsectors (corners and straights) defined by the circuit track map." with:
> Slice each lap into M = 20 ordered microsectors (10 corners and 10 straights, following the layout of Hojaji et al., 2026), with boundaries fixed by track distance so that every lap is divided at the same points.

Only keep "M = 20" and the Hojaji layout if you use Laguna Seca. For another track, state its own M and corner/straight split.

## Step 2

**C1 + C2 (clustering) and C14 (asterisks).** Replace the Process bullet with:
> **Process:** Apply K-Means clustering to lap times, with the number of clusters k chosen by the Elbow Method and Silhouette Coefficient, to label laps by skill tier (Fast, Medium and Slow if k = 3). The fastest cluster serves as the Fast reference whatever the value of k. Following Hojaji et al. (2024), lap time alone is clustered.

Then retype the Objective bullet so the literal asterisks disappear:
> **Objective:** To validate the synthetic laps generated against real human telemetry.

Citation note: the Step 2 citation is Hojaji et al. (2024) in *Computers in Human Behavior Reports*, which isn't in Thesis.bib yet. Your problem statement already cites a different Hojaji et al. 2024 (the GALA chapter), so once both are in Zotero they'll need 2024a/2024b.

## Step 4

**C6 + C7 (model type, one surrogate).** Replace the Process bullet with:
> **Process:** Train a single multi-output XGBoost regressor, shared by all microsectors, on the training laps. Its inputs are the control KPIs selected in Step 3, the entry speed v_entry,n and the microsector index n, and its outputs are Δt_n and v_exit,n.

This drops "multi-output or chained", so "chained" now only ever means the microsector chain. It also fixes the lowercase "step 3".

**C16 (symbol).** In the Mapping line, retype the model symbol so it reads plainly:
> f_ML: (s_n, v_entry,n) → (Δt_n, v_exit,n), where s_n is the selected control KPIs of microsector n

If you add the microsector index as an input (C7 above), write it as f_ML: (s_n, v_entry,n, n) → (Δt_n, v_exit,n).

## Step 5

**C8 (chromosome length).** Add at the start of the Initialization bullet:
> Each chromosome holds the K = 10 selected control KPIs for each of the M microsectors, giving M × K genes (200 for M = 20).

## Structural Limitations section

**C13 (heading).** Replace "Structural Limitations of Independent Sector Evaluation and the Sequential Optimization Justification" with:
> Structural Limitations of Independent Microsector Evaluation and the Justification for Chained Evaluation

## Main tab

**C13 (terminology).**
- Problem statement: "optimize sector-level performance indicators" → "optimize microsector-level performance indicators".
- Problem statement: "at the **sector level**" → "at the **microsector level**".
- Problem statement: "which circuit segments most strongly influence" → "which microsectors most strongly influence".
- Objective 1: "micro-sector telemetry dataset" → "microsector telemetry dataset".
- Objectives 2 and 3 ("sequential track sectors", "sector-importance model", "racing lines") are rewritten under E2, so leave them for that pass.
- Optional: copy the methodology tab's one-line definition of *microsector* into the problem statement, where the term first appears.

**C11 ("et. al.").** In Related Literature Notes, change "Hojaji et. al." to "Hojaji et al." in both places. The first sits inside a Zotero citation: fix it in Zotero's citation editor, or a Zotero refresh will put the old text back.
