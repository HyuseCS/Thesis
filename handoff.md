# Handoff — Hojaji literature review

Date: 2026-10-03. Commit: `1ed0e6b`.

## Done
- Literature review of Fazilat Hojaji's esports corpus (P1–P10, 2022–2026): `outputs/hojaji-2026.md`
- Provenance: `outputs/hojaji-2026.provenance.md`
- Publication list: `notes/hojaji-2026-publications.md`
- Plan and ledger: `outputs/.plans/hojaji-2026.md`
- Drafts, research files and two review passes: `outputs/.drafts/hojaji-2026-*.md`

## Limit
Only P2, P3, P5 and P8 were read in full. P4, P6, P7 and P9 parts come from abstracts or search text, because publisher sites block automated download. P1 is not open access. P10 has a title only. These parts are labelled in the review.

## Next steps
1. Download P4 in a browser: https://doi.org/10.1016/j.chbr.2024.100414 (CC-BY). Save the PDF to `01_Corpus/`.
2. Download P7 from SSRN: https://ssrn.com/abstract=5255017. Save the PDF to `01_Corpus/`.
3. Optional: download P9 (https://doi.org/10.1016/j.chbr.2026.100993) only if hardware becomes a control variable in G1.
4. Run `/zotero-ingest` to write source notes for the new PDFs.
5. Update `outputs/hojaji-2026.md`:
   - Replace abstract-level P4 and P7 rows in §2 T1 and §3 with full-text facts.
   - Answer the three Open Questions: does P4 have segment analysis ("19 segments", "15,694 rows" are unverified)? Does P7 report a rank shift between tracks? Is P7's dataset the same as P8's?
   - Re-check §6 item 1 (no sector-level importance). P4 is the most likely counterexample.
   - Re-check §6 item 4 (no code or data release) for P4 and P7.
6. Run the verifier and reviewer again on the updated review, then update the provenance file.

## Key facts to keep
- P8 trains its classifier on segment rows (`Sec. 3.4`), but pools importance into one global ranking (`Sec. 5`). The thesis gap is per-sector importance, not "sectors as units".
- P8's ~81–82 s optimum sits on the 90 % clamp floor only if the baseline is 91.05 s. With the ~89 s baseline in `Fig. 3`, it does not. The paper does not say which.
- P8 does not cite P7. The P7 → P8 dataset link rests on one unverified search snippet.
