# Provenance: hojaji-2026

- Date: 2026-10-03
- Review: outputs/hojaji-2026.md
- Type: publication-corpus review (Fazilat Hojaji, University of Limerick; anchor Hojaji2026_TelemetryEA)
- Plan: outputs/.plans/hojaji-2026.md
- Publication log: notes/hojaji-2026-publications.md

## Sources
| Status | Count | Items |
| :--- | :--- | :--- |
| Consulted | 10 corpus papers + author/metadata APIs | P1–P10; Semantic Scholar, OpenAlex, Crossref, Unpaywall, DOAJ, UL Pure, PMC |
| Accepted, full text | 4 | P2, P3, P8 (vault PDFs and notes), P5 (PMC) |
| Accepted, abstract / metadata level, labelled | 5 | P1, P4, P6, P9 (abstract), P10 (title only) |
| Accepted, search-result text only, labelled unverified | 1 | P7 |
| Rejected | search-engine summary lines for P4 (84/62 features, 15,694 rows, 19 segments, XGBoost AUC 0.971) — conflict with the abstract and could not be checked; kept only as an Open Question | |
| Out of scope | Hojaji 2010–2019 SOA governance and model-tracing papers | |

## Verification
- Verifier pass: all 10 DOIs resolve (P5, P7 publisher 403 after redirect; P10 503 at check time). Numbers for P2, P3, P5, P8 checked against notes, PDFs and PMC. Log: outputs/.drafts/hojaji-2026-verify-log.md
- Reviewer pass 1: 1 FATAL (P8 trains on segment rows; draft said lap-level), 5 MAJOR, 9 MINOR. Review: outputs/.drafts/hojaji-2026-review.md
- All FATAL and MAJOR fixed. Reviewer pass 2: no FATAL left, no wrong numbers. Review: outputs/.drafts/hojaji-2026-review2.md
- Lead spot checks: P8 PDF has no P7 reference; P8 Sec. 3.4 trains on the segment dataset; Crossref shows P4 cites P2 and P3 and P7's first reference is P4.

## Intermediate files
- outputs/.drafts/hojaji-2026-research-telemetry.md (P4, P7)
- outputs/.drafts/hojaji-2026-research-adjacent.md (P1, P5, P6, P9, P10)
- outputs/.drafts/hojaji-2026-draft.md, hojaji-2026-cited.md

## Unresolved corpus gaps
- P4, P6, P7, P9 full text blocked for automated access (ScienceDirect / SSRN bot protection). P4 and P7 are the most important.
- P1 is closed access. P10 has no public abstract.
- Google Scholar and UL Pure person page not readable (403); corpus list relies on Semantic Scholar + OpenAlex agreement.
- P9 Unpaywall licence URL not added to Sources.
