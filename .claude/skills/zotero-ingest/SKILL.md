---
name: zotero-ingest
description: Pull new PDFs from the Zotero Thesis collection and run the full AGENTS.md §5 ingestion (source note, matrix row, move to ingested/<year>/). Use when the user says /zotero-ingest, "sync zotero", or "pull new papers".
---

# Zotero Ingest

## Step 1 — Pull

Run `python scripts/zotero_pull.py` from the repo root. It downloads new PDFs from the Zotero collection into `01_Corpus/` with a `<CitationKey>.zotero.json` metadata sidecar, and records them in `01_Corpus/.zotero_state.json` with status `downloaded`. If it errors, report the message and stop.

## Step 2 — Ingest each new paper, one at a time

For every PDF sitting in the root of `01_Corpus/` (not in `ingested/`), follow AGENTS.md §5 exactly. Process papers sequentially — never in parallel — so edits to the matrix and state file cannot conflict.

Per paper:

1. **Confirm the citation key.** The script proposed `AuthorYear_Keyword` from Zotero metadata (see the sidecar). Refine the `Keyword` if a better one is obvious from the paper (e.g. the algorithm's name). The year must be the publication year. If you rename, rename the PDF, the sidecar, and the `citation_key` fields inside the sidecar and `.zotero_state.json`.
2. **Read the whole paper** (page ranges for large PDFs), per AGENTS.md §5.
3. **Write `02_Source_Notes/<CitationKey>.md`.** Use `02_Source_Notes/Scheffe2022_SCR.md` as the structural gold standard — it is richer than `Template.md`. Citation data (authors, venue, DOI) comes from the sidecar, not from memory. All AGENTS.md rules apply, especially §1 (zero hallucination, location-level cites) and §4 (blind-spot checklist).
4. **Add a row** to `04_Argument_Matrix/matrix.md` linking `[[<CitationKey>]]`.
5. **Move** the PDF and its sidecar to `01_Corpus/ingested/<publication year>/`. This is the last step and the done-marker — never move before the note exists.
6. **Update state**: set the item's `status` to `ingested` in `01_Corpus/.zotero_state.json`.

## Step 3 — Report

List per paper: citation key, note written, matrix row added, moved. A paper that failed ingestion stays in the drop zone with status `downloaded` — name the specific blocker.
