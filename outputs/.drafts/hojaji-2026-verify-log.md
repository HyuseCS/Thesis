# Verify log: hojaji-2026 (2026-10-03)

## Checked
- P2/P3/P8 claims with Sec./Fig./Table locations: matched against the three vault notes. P8 also checked against the PDF text (reference list has no P7/SSRN entry).
- P5: checked against PMC11130932 (title, N 88/104, n 22+22, Tobii 50 Hz, TRACK:HUD 2.44 vs 4.11 p 0.003 d 0.969 in Table 1, corner TFDn 101.70 vs 113.79 p 0.018 d 0.740 in Table 2, 9 corner sectors, data on email request). All match.
- P4: checked against UL Pure abstract (174, 1,327 laps, 97.19 %, speed > lateral acc > steering angle > lane deviation). Matches. No snippet-only P4 number is used as fact.
- P6/P7/P9/P10: checked against the two research files. Labels kept (abstract / search text / abstract-level / title only).
- DOIs: all 10 resolve. 403 after redirect: P5 (MDPI), P7 (SSRN). 503 at check time: P10 (Taylor & Francis). No dead links.
- Other URLs: UL Pure P6, Crossref P7, DOAJ P4, SCITEPRESS PDF return 200. ScienceDirect P9 page returns 403 to curl (blocked, not dead).

## Changed
- P5 location: "(P5 Results)" -> "`Table 1`"; corner stat now cites `Table 2`.
- P5: "Per-corner results were not confirmed" -> "reports corner metrics averaged over the 9 corners, not per corner" (PMC Methods and Table 2).
- P8/P7: "does not cite P7 by name in our reading" -> "reference list contains no P7 entry" (checked in PDF).
- P3 pivotal item: "first paper to overlay" -> "first paper in the corpus to overlay" (note says "first corpus paper").
- Consensus "method stack": P3 cited for the k-means step only (P3 has no classifier).
- Added inline [n] citations and a numbered Sources section (22 entries).

## Not verified
- Fig. 2 (P8) and Fig. 3 (P2) chart readings (~0.96 etc.): taken from vault notes, marked "read from chart". Not re-measured.
- P6 "154,000 games, 97 %" and P9 details: abstract-level only. P9 page blocked, so the text comes from a search-tool summary.
- P4 CC-BY licence: from DOAJ record per research file; the P4 page is blocked.
- P7 "high congruence" quote and counts: search-result text only.
- "Ten papers found via Semantic Scholar, OpenAlex, Crossref" and ORCID: cited to the publication log [16]; not re-checked here.
- Remonda 2021/2025 attributions: from Crossref reference lists in the research file; not re-fetched.
- P3 557 vs 556 lap count inconsistency (note) not mentioned in the draft; left as is.
