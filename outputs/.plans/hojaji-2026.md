# Plan: hojaji-2026 (publication-corpus review)

Input: "hojaji 2026". Read as: the research corpus of Fazilat Hojaji (with A. Toth, M. Campbell), anchored on Hojaji2026_TelemetryEA (ICAART/SPIKE 2026).

## Key questions
- Q1 Identity: who is F. Hojaji, affiliation, lab, co-authors.
- Q2 Corpus: all reachable publications (title, year, venue, DOI/URL).
- Q3 Trajectory: how did methods, data, and granularity change from first paper to 2026?
- Q4 Which 3-5 papers changed the direction most?
- Q5 What does the corpus leave open at sector level (the thesis gap, GOAL.md G2.3)?
- Q6 Is any code or data released (GOAL.md R6)?

## Sources
Author profiles (Google Scholar, ORCID, Semantic Scholar, UL research portal), publisher pages (SciTePress, Springer, Elsevier), local source notes in 02_Source_Notes/.
Period: all years, focus 2022-2026.

## Expected sections
Identity; publication log; trajectories; pivotal papers; consensus / disagreements; gaps vs. thesis; next reading.

## Task ledger
| ID | Task | Owner | Status |
|---|---|---|---|
| T1 | Identity + publication log -> notes/hojaji-2026-publications.md | lead | done |
| T2 | Per-paper methods/data extraction for non-ingested papers -> outputs/.drafts/hojaji-2026-research-*.md | researcher | done (P4, P7, P6, P9 blocked: abstract only) |
| T3 | Synthesis draft -> outputs/.drafts/hojaji-2026-draft.md | lead | done |
| T4 | Citations + URL check -> outputs/.drafts/hojaji-2026-cited.md | verifier | done |
| T5 | Review -> outputs/.drafts/hojaji-2026-review.md | reviewer | done (2 passes) |
| T6 | Deliver outputs/hojaji-2026.md + .provenance.md | lead | done |

## Verification log
(filled during run)

- 2026-10-03: verifier pass ok; review 1 FATAL fixed; review 2 clean. Final at outputs/hojaji-2026.md.
