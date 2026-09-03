---
name: zotero-ingest
description: Pull new PDFs from the Zotero Thesis collection and run the full AGENTS.md §5 ingestion (source note, matrix row, move to ingested/<year>/). Use when the user says /zotero-ingest, "sync zotero", or "pull new papers".
---

# Zotero Ingest (orchestrator)

The ingestion contract lives in AGENTS.md §5 — read it first. This skill is the Claude Code execution layer: per-paper work fans out to subagents; shared files stay in the main thread.

## Step 1 — Pull

Run `python scripts/zotero_pull.py` from the repo root. If it errors, report the message and stop.

## Step 2 — Fan out (one subagent per paper)

For every PDF in the root of `01_Corpus/` (not in `ingested/`), spawn a `paper-ingester` agent — all in parallel, in a single message. Give each agent only its citation key. Each agent reads its paper, writes its source note, and returns: `final_key`, `note`, `matrix_row`, `year`, `blockers`.

Subagents never touch shared files. If two agents return the same `final_key`, resolve the collision yourself before Step 3.

## Step 3 — Merge (main thread, sequential)

For each returned paper, in order:

1. If `final_key` differs from the given key: rename the PDF and sidecar, update `citation_key` inside the sidecar, and verify the note filename matches `final_key`.
2. Append the returned `matrix_row` to `04_Argument_Matrix/matrix.md`.
3. Move the PDF and sidecar to `01_Corpus/ingested/<year>/`. Last step per AGENTS.md — never before the note exists.
4. Set the item's `status` to `ingested` in `01_Corpus/.zotero_state.json`.

A paper whose agent reported blockers stays in the drop zone with status `downloaded`.

## Step 4 — Report

Per paper: citation key, note written, matrix row added, moved — plus the specific blocker for any paper left in the drop zone.

## Fallback

In a harness without subagents, follow AGENTS.md §5 sequentially — same result, slower.
