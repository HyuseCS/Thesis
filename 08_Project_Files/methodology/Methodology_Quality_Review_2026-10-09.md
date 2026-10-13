# Quick quality review: refined methodology tab (2026-10-09)

Source: Google Doc "Thesis TODOs", refined methodology tab, read 2026-10-09 09:35 UTC. Known todo items (data collection placeholders, optimized-lap validation, common-judge limitation) are in `todos/Todos_2026-10-03.md` and not repeated here.

## Would draw questions from a panel
1. **Penalty thresholds for the new KPIs (Step 5).** The penalty P of Hojaji et al. (2026) uses "predefined physical thresholds" for their KPIs. Step 1 now adds KPIs they didn't have (steering reversal rate, share at full throttle, lowest gear, steering-angle statistics). Say how thresholds and transition limits are set for these, for example the 1st–99th percentile of the training laps.
2. **XGBoost tuning (Step 4).** The external test set is "never used for … tuning", but no tuning step exists. Add one line: hyperparameters chosen by grouped (by-driver) CV on the training laps, with the search method (grid or random) and the parameters searched.
3. **Cleaning numbers (Step 1).** The data section says 826 laps from 166 drivers; after your cleaning it is 817 laps from 165 drivers. State the after-cleaning count in Step 1, and say which rules actually apply to this dataset. It is already segmented, so "remove in-laps and out-laps" may not apply.
4. **"Newer version of the simulator."** The data section claims the external test set uses a newer ACC version than the main dataset, but the main dataset's ACC version isn't stated. Give it (from Hojaji et al., 2024) or drop "newer".
5. **KPI consistency check (Simulator Validity).** Drivers have 1–8 laps (median 5), so an ICC across a driver's laps can't use 1-lap drivers. Say that drivers with fewer than 2 (or 3) laps are excluded from this check.

## Clarity and wording
6. **Pearson filter threshold (Step 3).** "Weakly correlated" needs a number, for example |r| < 0.1 with both targets.
7. **Microsector index as input (Step 4).** Say it is treated as categorical (one-hot or XGBoost's categorical support), so the model doesn't read microsector 10 as "more than" microsector 9.
8. **Step 1 duplicate.** The Outlier filter bullet repeats "Slice each lap into M = 19 ordered microsectors…" from the Microsectors bullet. Delete it.
9. **Step 0 Session line.** "practice,soft, 20L 0x fuel cons" → for example "Practice session, soft tyres, 20 L fuel, fuel consumption off".
10. **Heading.** "Data Collection and Simulator Reliability" now holds a "Simulator Validity and Scope" subsection. Rename the heading to "Data Collection and Simulator Validity" for consistency.
11. **Notation.** Step 4 writes "R2" twice; use R². Δtn and vexit,n are plain text in Steps 3 and 5 but use underscores (Δt_n, v_exit,n) in Step 4. Pick one style, ideally Google Docs subscripts.
12. **Typed citation.** Step 0's first line, "The main dataset (Hojaji et al., 2024) was recorded…", is still typed rather than a Zotero citation.

## Fine as is
The dataset switch is consistent across Steps 0–5 (Brands Hatch, M = 19, 190 genes, split by driver). The data collection section answers the adviser's comment, and the ablation design (paired seeds, common judge, Wilcoxon, rollout-error threshold) is sound.
