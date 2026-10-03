# Review 2: hojaji-2026.md vs prior review W1-W15 (2026-10-03)

Files compared: `outputs/.drafts/hojaji-2026-cited.md` -> `outputs/hojaji-2026.md`. No file edited.
Checked against: P8 PDF text (`pdftotext`), vault notes for P8, P2 (`Hojaji2023_TelemetryML.md`), P3 (`Hojaji2024_DrivingBehaviour.md`), `GOAL.md`, verify log, research files.

## Part 1. Status of W1-W15

| ID | Status | Evidence |
| :-- | :-- | :-- |
| W1 FATAL | RESOLVED | Final lines 50, 52, 97 now say P8 trains on segment rows and pools importance. P8 text: "The segment dataset from the previous step was divided into 70% training and 30% validation" (Sec. 3.4, pdftotext l.315-316); "computed globally rather than at the individual sector level" (Sec. 5, l.699). Clustering uses "lap time and segment time" (Sec. 3.3). "never as model units" is gone. |
| W2 | PARTLY | Lines 90 and 97 are scoped to "papers read in full" and P4 is flagged. Still open: line 56 says P5 is "the only statistical test at corner level" and then says it is pooled over 9 corners, not per corner. That is self-contradictory. Line 100 says no code/data release "was found" for P4 and P7, which are unread. |
| W3 | RESOLVED (small gap) | Caption (l.38) and l.116 say the counts come from one snippet and may be an artefact. The mermaid node on l.32 still shows "135 drivers" with no in-node label. |
| W4 | RESOLVED | Criterion is now stated (in-corpus uptake, l.66). P4 ranked first with Crossref/P8 Sec. 3 evidence. P8 listed "by role". P7 marked "unverified". Minor: P2 and P3 tie at one citing paper each (P4) and the order is not explained. |
| W5 | RESOLVED | Moved to l.91 and made conditional. Arithmetic checks: 0.9 x 91.05 = 81.945; 0.9 x 89 = 80.1. P8 text: baseline 91.05 s (Sec. 4.2, l.448); bounds "no shorter than 90% and no longer than 105%" (Sec. 3.5.2, l.385-386); clamp is per sector, so the lap-level floor is only an approximation. The text says "does not say which". Still mild: l.91 says the optimum "sits on" the floor, and 81.3-82 s vs 81.945 s is close but not equal. |
| W6 | RESOLVED | T3 heading is now "Other esports". l.62 limits the ML-ranking claim to P6 and says P1/P10 do not show it. |
| W7 | RESOLVED | l.98: "our interpretation, not P3's claim". Matches P3 note l.67. |
| W8 | RESOLVED | l.77 adds P2 "no discernible" g_lat trend (P2 note l.37, Sec. 3.3). P3 also says this (P3 note l.56) but is not cited there. Polish only. |
| W9 | RESOLVED | l.78 says the name may not mean the same computation. |
| W10 | RESOLVED | l.79 says XGBoost reported best; P8 gives no RF/SVM scores. The odd "MAE = 0.42 s" is still not noted in the table. Polish only. |
| W11 | RESOLVED | l.90 counts verified. P2: 475 + 219 + 91 = 785 vs 782 (P2 note l.11, l.30-32). P3: 441 + 115 = 556 vs 557 (P3 note l.15, l.48-49, l.70). All three P2 classes now shown. No separate "counts do not sum" row, but it is in the same cell. |
| W12 | RESOLVED | Caption l.38 cites Crossref [20, 21] and P8 Sec. 3. Side links labelled "shared setting only". The P2 -> P3 arrow has no stated support (P3 citing P2 is unchecked). |
| W13 | RESOLVED | l.95 now reads "map to GOAL gates and risks where one applies". Item 5 says "No GOAL gate". G1, G2, G2.3, G4 exist in GOAL.md. R6 exists (GOAL.md l.128). |
| W14 | PARTLY | Remonda item (l.109) is hedged ("Read them only if the titles prove...") but still a reading task with no reason. P9 "CC BY-NC-ND per Unpaywall" (l.108) has no Unpaywall URL in Sources. The Unpaywall row in research-adjacent covers the P6 record URL and mentions P9. |
| W15 | RESOLVED | l.9 now says S2 and OpenAlex, with Crossref for authors. The "largest sample" claim is gone; l.68 just gives 174. |

## Part 2. New or changed claims from the fixes

- [N1] MINOR. l.56: "Among the papers read in full, this is the only statistical test at corner level." Same sentence block says P5 pools 9 corners. Reword to "corner-pooled".
- [N2] MINOR. l.100: "No code or data release was found for P2, P3, P4, P7 or P8." P4 and P7 were not read. Add "(P4/P7 not read)". P2 used public MoTeC server data, not an author release; wording is OK but could confuse.
- [N3] MINOR. l.68-70 and l.69: "First ML on sim-racing telemetry by this lab", "first place the segment-level question is deferred", "first paper in the corpus to overlay track sections". The last is from the P3 note (l.6), but P5 (corner-sector fixations) is also in the corpus and the "first" comparison is not argued. Soften or drop "first".
- [N4] MINOR. l.62: "P6 shows the lab also applies ML KPI ranking". The P6 text in hand is an abstract: neural networks, 97 % win prediction. The title mentions "KPIs", so "ranking" is an inference.
- [N5] MINOR. l.32 diagram node keeps P7 counts without an "unverified" tag.
- No wrong numbers found. Checked: 865, 17,279, 0.87/0.85/0.90, 91.05 s, 91.2 s, 86.4 s, 81.945 s, 80.1 s, 785/782, 556/557, 475/219/91, 441/115, 18 sections (S1-S9, T1-T9). New cited claims (P4 cites P2/P3; P4 first in P7 refs; P8 has no P7 entry; P4 CC-BY via DOAJ) are backed by the research files and verify log, not re-fetched here.

## Verdict

No FATAL issue remains. W1 and W5 hold against the P8 PDF text. Remaining work is wording: W2 residuals, W14 sources, N1-N5. Confidence: high on W1/W5/W11 (checked to source text); medium on Crossref-derived claims (taken from earlier logs, not re-fetched).

## Sources

- `/home/hyuse/Desktop/Thesis/01_Corpus/ingested/2026/Hojaji2026_TelemetryEA.pdf` (public: https://www.scitepress.org/Papers/2026/146096/146096.pdf)
- Vault notes: `02_Source_Notes/Hojaji2026_TelemetryEA.md`, `Hojaji2023_TelemetryML.md`, `Hojaji2024_DrivingBehaviour.md`
- `GOAL.md`, `outputs/.drafts/hojaji-2026-verify-log.md`, `-research-telemetry.md`, `-research-adjacent.md`
