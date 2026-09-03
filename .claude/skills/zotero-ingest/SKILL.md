---
name: zotero-ingest
description: Pull new PDFs from the Zotero Thesis collection and run the full AGENTS.md §5 ingestion (source note, matrix row, move to ingested/<year>/). Use when the user says /zotero-ingest, "sync zotero", or "pull new papers".
---

# Zotero Ingest

The full procedure lives in AGENTS.md §5 ("How files arrive" + "Ingestion procedure") — it is the single source of truth so every harness runs the same steps. Follow it:

1. Run `python scripts/zotero_pull.py` from the repo root. If it errors, report the message and stop.
2. For every PDF in the root of `01_Corpus/`, execute the AGENTS.md §5 ingestion procedure, one paper at a time. All AGENTS.md rules apply, especially §1 (zero hallucination) and §4 (blind-spot checklist).
3. Report per paper: citation key, note written, matrix row added, moved.
