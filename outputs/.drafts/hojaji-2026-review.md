# Review: hojaji-2026-cited.md (2026-10-03)

Reviewed file: `outputs/.drafts/hojaji-2026-cited.md` (143 lines). Draft not edited.
Evidence checked: the three vault notes, both research files, the verify log, the publication log, GOAL.md, plus the P8 and P2 PDFs (`pdftotext`) and the Crossref P4 reference list.

## Summary

The draft reviews the ten esports papers by Hojaji and co-authors (P1–P10). It reads four in full (P2, P3, P5, P8). It traces one method line, P2 → P3 → P4 → P7 → P8, and argues that the line moves from "which features matter" to a prescriptive EA. Then it lists consensus, disagreements, gaps mapped to GOAL.md, and next steps.

The draft is careful about read level in most places: P4/P7 numbers are labelled abstract or search text, chart readings are marked, and our own arithmetic is marked. The main problems are (1) a factual error about P8 that sits on the thesis gap, (2) corpus-wide "never" claims that the four-of-ten read level cannot support, (3) a P7 → P8 link built on search snippets that the research file says are contaminated, and (4) a pivotal-paper ranking with no stated, evidenced criterion.

## Strengths

- [S1] Read level is shown per paper in the table (lines 11–22), and line 24 states the coverage limit openly.
- [S2] Most numbers trace to a section, table or figure. Spot checks of P2 (782 laps, 92.2 %, Table 2 counts), P3 (557 laps, k = 2, 81.42 %), P5 (Table 1/2 statistics) and P8 (865 laps, Acc 0.87/F1 0.85/AUC 0.90, 20 × 10 chromosome, 91.05 s) all match the notes and PDFs.
- [S3] Snippet-only P4 numbers (19 segments, 15,694 rows) are kept out of the body and put in Open Questions (line 114). This follows the research-file warning.
- [S4] The P8 text-vs-figure KPI mismatch (line 87) and the baseline mismatch (line 91) are real and match the P8 note.

## Weaknesses

- [W1] **FATAL:** Lines 52 and 97 misstate how P8 trains its importance model. Line 52: "The lap stays the unit of the importance model in every paper read in full." Line 97: sections exist "as EA genes (P8), never as model units." P8 `Sec. 3.4` says: "The segment dataset from the previous step was divided into 70% training and 30% validation". So the P8 XGBoost model is trained on 17,279 segment rows (`Sec. 3.2`), with segment labels from "lap time and segment time" (`Sec. 3.3`). The gap P8 admits (`Sec. 5`) is narrower: importance is *pooled* over all sectors, not computed *per* sector. This matters for the thesis. G2.3 compares a sector-level model to a global baseline. If the thesis says "first to use sectors as model units", a reader with P8 open will reject it. **Fix:** Line 52: "P8 trains on segment rows, but computes one importance ranking pooled over all sectors (`Sec. 3.4`, `Sec. 5`). P2 trains on laps." Line 97: "Sections are plot bands (P3), pooled training rows and EA genes (P8). No paper reports per-sector importance." Also, in the P8 row at line 50, change "Granularity" to "segment rows, pooled importance; EA over 20 sectors".

- [W2] **MAJOR:** Corpus-wide absence claims go beyond the read level. Line 97 says "Sector-level importance is never computed." Line 90 says class balance is "Never addressed." Line 56 says P5 has "the only statistical test at corner level found in the corpus." Only 4 of 10 papers were read. P4 is unread, and snippet text says P4 has a segment dataset (line 114). P4 is the most likely counterexample. Partial support exists: P8 `Sec. 5` reports only P8's own importance as global. **Fix:** Scope each claim. For example: "Not computed in P2, P3 or P8 (read in full). P8 names it as future work (`Sec. 5`). P4 and P7 unread; P4 snippet text mentions a segment dataset [22]." Do not build on item 6.1 until P4 is read (action 7.1).

- [W3] **MAJOR:** The P7 → P8 link (line 34, line 38, line 116) and the P7 node "135 drivers" (line 32) rest on one search snippet. The research file says snippets "mixed content between papers at least once (a P7 query returned P8's abstract wording)" (research-telemetry line 29). So the matching counts 135 / 1,180 could be P8 text that was returned for a P7 query. In that case, the match is circular. **Fix:** At line 38 and line 116, add: "the P7 counts come from one search snippet, and the same tool returned P8 text for a P7 query once, so the match may be an artefact." Draw the P7 node without counts, or label them "snippet, unverified". Treat the link as unconfirmed until the P7 PDF is read.

- [W4] **MAJOR:** The pivotal-paper ranking (lines 64–73) is not justified. The stated criterion, "how much each changed the direction of the corpus" (line 66), is never measured. (a) P8 is ranked first, but it is the newest paper, so no later paper can show it changed direction. Its position rests on what it does, not on its influence. (b) P4 is ranked third, but it is the only paper with documented uptake: P8 adopts its framework (`Sec. 3`), P7 cites it first (Crossref [21]), and it cites P2 and P3 (Crossref [20]; checked in this review). (c) P7 is ranked fourth, as "first cross-track test", based only on search text. **Fix:** Pick one of two options. Option 1: drop the numbering and call the section "Key papers by role" (origin P2, framework P4, prescriptive step P8). Option 2: state a measurable criterion, such as in-corpus citations from Crossref reference lists plus method reuse, and rank by it. With that criterion, P4 probably ranks first. For both options, mark P7 as "provisional, search text only".

- [W5] **MAJOR:** The clamp-floor argument (line 68) depends on which baseline you use, and line 91 shows that the baseline is unclear. 0.9 × 91.05 s = 81.945 s is correct. But the clamp is per sector, relative to a "baseline sector time derived from fast human laps" (P8 `Sec. 3.5.2`). If the baseline is the Fig. 3 line (~89 s), the floor is ~80.1 s. If it is the fast-cluster mean (86.4 s), the floor is ~77.8 s. The Fig. 3 best curve ends at ~81.3 s (P8 note), which is above both of those floors. **Fix:** "If the 91.05 s start value is the clamp baseline, the reported ~81–82 s sits at the 90 % floor (81.9 s, our arithmetic). With the Fig. 3 baseline (~89 s, read from chart), the floor is ~80.1 s and the result is above it. The paper does not let us tell which applies." Move this point from the ranking into §5 next to line 91.

- [W6] **MAJOR:** T3 (lines 60–62) says something about P1 and P10 that their read level cannot support. The heading "The same KPI-ranking method in other esports (P1, P6, P10)" and the sentence "the lab treats 'rank KPIs by ML' as a general esports method" are supported only by P6 (abstract). P1's abstract describes kinematic phases and tDCS. No ML ranking is mentioned (research-adjacent lines 39–43). P10 is title only. **Fix:** Rename the heading to "Other esports work (P1, P6, P10)". Change the sentence to: "P6 (abstract) applies ML KPI ranking to League of Legends. P1 and P10 show no ML ranking at the level read."

- [W7] **MINOR:** Line 98 says "P3 notes a T2 → T3 carry-over in prose only." P3 describes earlier braking at T3 that ends "with less speed". The carry-over reading is from our vault note ("hints at carry-over"), not from the authors. **Fix:** "P3 describes T3 braking differences (`Sec. 3.2`). Reading these as T2 → T3 carry-over is our interpretation."

- [W8] **MINOR:** The consensus on lateral acceleration (line 77) leaves out the contrary observations. P2 `Sec. 3.3` and P3 `Sec. 3.2` both report "no discernible trend" in lateral acceleration between groups. That does not contradict importance rank, but readers should see it. **Fix:** Add one clause that says this, and that importance rank and group-mean traces measure different things.

- [W9] **MINOR:** Line 78 treats "lane deviation" as one metric across papers. In P2 it is a MoTeC i2 math channel (P2 note, `Sec. 2.2`). In P3/P8 it is a derived KPI whose definition is in P4 (unread). **Fix:** "Same name. It is not confirmed that the definitions are the same."

- [W10] **MINOR:** Line 79, "tree-based classifiers with XGBoost best". SVM was also compared (P2, P8), and P8 does not report RF/SVM scores, so its "best" cannot be checked (P8 note). Line 50 also gives P8's "Acc 0.87" without its odd "MAE = 0.42 s" for a classifier. **Fix:** "XGBoost vs RF vs SVM; XGBoost reported best (P8 gives no RF/SVM scores)."

- [W11] **MINOR:** The class-balance row (line 90) leaves out P2 MIDDLE = 219. It also misses two count inconsistencies in the sources. P2: 91 + 219 + 475 = 785, but the paper reports 782 laps (`Table 2` vs `Sec. 2.2`). P3: 115 + 441 = 556, but the paper reports 557 laps (verify log line 26). **Fix:** Give all three P2 classes and add one row, "Lap counts do not sum", for P2 and P3.

- [W12] **MINOR:** The trajectory diagram (lines 28–37) has arrows with no source. Crossref shows that P4 cites P2 and P3 (checked in this review), but the draft does not cite this. The P5---P3 and P9---P8 lines have no stated meaning. **Fix:** Add "(P4 cites P2 and P3; P7 cites P4; P8 adopts P4: Crossref [20, 21], P8 `Sec. 3`)" to the caption on line 38, and label the side lines "same rig/track context".

- [W13] **MINOR:** Zombie promise at line 95, "Each item maps to [[GOAL]]". Item 4 maps to risk R6, not a goal. Item 5 maps to nothing. **Fix:** Map item 5 to R3 / G1 (fixed car and circuit), or change the line to "maps to a GOAL gate or risk".

- [W14] **MINOR:** Line 108 says P9 is "CC BY-NC-ND" with no citation. The source is the Unpaywall record in research-adjacent row 11, which is not in Sources. Line 109 recommends Remonda papers with "topic not checked", which is a reading action with no stated reason. **Fix:** Add the Unpaywall URL as a source. Check the Remonda titles (Crossref gives them) or drop item 7.4.

- [W15] **MINOR:** Line 9 says the ten papers "were found through Semantic Scholar, OpenAlex and Crossref". The publication log says S2 and OpenAlex gave the list, and Crossref was used for author lists. Line 70, "Largest sample in the line, 174 participants": P2's driver count is not reported, so this holds only among papers that report participants. **Fix:** Change the wording to match the log. Add "among papers reporting participant counts".

## Questions for Authors

- [Q1] What is the label of the P8 segment-level classifier, and how many segment clusters are there? (`Sec. 3.3` gives none.) This sets what "global importance" means for the G2.3 baseline.
- [Q2] Which baseline does the P8 clamp use: 91.05 s, the Fig. 3 line, or the fast-lap mean?
- [Q3] Does P4 report any per-segment result? (The P4 PDF must be read before §6 item 1 can stand.)

## Verdict

The draft is usable as a working map after fixes, but not yet as thesis evidence. Fix W1 before anything in §6 is quoted, because it misstates the closest prior work on the exact point the thesis claims. Then fix W2–W5, which are scoping and justification fixes. The remaining items are wording. Revision priority: high for W1–W5, low for the rest. Confidence: high for W1 (checked against the P8 PDF text), W3 (research-file warning) and W5 (arithmetic). Medium for W4, because a ranking criterion is a judgement.

## Revision Plan

1. W1: rewrite lines 50, 52 and 97 to say that P8 trains on segment rows with pooled importance.
2. W2: scope every "never" / "only" claim (lines 56, 90, 97) to the papers read in full. Gate §6.1 on reading P4.
3. W3: label the P7 counts and the P7 → P8 link as snippet-based and possibly contaminated (lines 32, 38, 116).
4. W4: replace the ranking with roles, or rank by a stated criterion based on citations and reuse. Mark P7 as provisional.
5. W5: make the clamp-floor point conditional on the baseline, and move it beside line 91.
6. W6: narrow T3 to P6.
7. W7–W15: one-line wording and citation fixes as listed.

## Inline Annotations

> "The lap stays the unit of the importance model in every paper read in full." (line 52)
**[W1] FATAL:** P8 `Sec. 3.4`: "The segment dataset ... was divided into 70% training and 30% validation". The model trains on segment rows, and only the importance ranking is global. P3 and P5 have no importance model at all.

> "Sections exist as plot bands (P3) and as EA genes (P8), never as model units." (line 97)
**[W1] FATAL:** Contradicted by P8 `Sec. 3.3–3.4`. Segments are the training rows. The gap is per-sector importance, not segments as units.

> "**Sector-level importance is never computed.**" (line 97)
**[W2] MAJOR:** "Never" covers 10 papers, but only 3 telemetry papers were read. The likely counterexample, P4, is unread.

> "This is the only statistical test at corner level found in the corpus." (line 56)
**[W2] MAJOR:** The P5 test is pooled over 9 corners (the draft says so in the next sentence). It is not corner-level, and P4/P7 are unread. Use: "the only corner-pooled statistical test in the papers read in full".

> "| Class balance | Never addressed." (line 90)
**[W2] MAJOR / [W11] MINOR:** Scope to P2, P3, P8. Add P2 MIDDLE 219 and the 785 ≠ 782 and 556 ≠ 557 count gaps.

> "The P7 → P8 link is inferred: both report 135 participants and 1,180 laps." (line 38)
**[W3] MAJOR:** The P7 side of this match is one search snippet from a tool that is known to return P8 text for P7 queries (research-telemetry line 29).

> "Ranked by how much each changed the direction of the corpus, not by venue." (line 66)
**[W4] MAJOR:** No influence evidence is given for any paper. The only documented uptake (P8 `Sec. 3`, Crossref references) points to P4, which is ranked third.

> "**P7 (2025, preprint)** — first cross-track test." (line 71)
**[W4] MAJOR:** A pivotal ranking based on search-result text only. Mark it provisional.

> "the ~81–82 s result is close to the 90 % clamp floor of 81.945 s" (line 68)
**[W5] MAJOR:** True only if the clamp baseline is 91.05 s. Line 91 shows that the baseline is ambiguous. With the Fig. 3 baseline (~89 s), the floor is ~80.1 s, which is below the reported result.

> "These show the lab treats "rank KPIs by ML" as a general esports method." (line 62)
**[W6] MAJOR:** Only P6 supports this. The P1 abstract is about kinematics and tDCS. P10 is title only.

> "P3 notes a T2 → T3 carry-over in prose only" (line 98)
**[W7] MINOR:** The carry-over interpretation comes from our note, not from the authors.

> "Third in P2 (`Fig. 3`), second in P4 (abstract) [11], second in P8" (line 77)
**[W8] MINOR:** P2 `Sec. 3.3` and P3 `Sec. 3.2` report "no discernible trend" in lateral acceleration between groups. Mention this.

> "Each item maps to [[GOAL]]." (line 95)
**[W13] MINOR:** Item 5 maps to nothing. Item 4 maps to a risk, not a goal.

> "Get the P9 PDF (CC BY-NC-ND)" (line 108)
**[W14] MINOR:** No source. Cite Unpaywall (research-adjacent row 11).

## Sources

- P8 PDF text, `Sec. 3.3–3.5`, `Sec. 5`: `/home/hyuse/Desktop/Thesis/01_Corpus/ingested/2026/Hojaji2026_TelemetryEA.pdf` (public: https://www.scitepress.org/Papers/2026/146096/146096.pdf)
- P2 PDF text, `Sec. 2.2`, `Sec. 3.2`, `Table 2`: `/home/hyuse/Desktop/Thesis/01_Corpus/ingested/2023/Hojaji2023_TelemetryML.pdf`
- Crossref P4 reference list (cites P2 and P3; Remonda 2021 confirmed by title): https://api.crossref.org/works/10.1016/j.chbr.2024.100414
- Vault notes, research files, verify log and publication log, as named in the task.
