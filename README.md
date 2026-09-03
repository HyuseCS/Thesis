# Thesis Vault

Obsidian vault for a thesis on optimizing the Sequential Convex Restriction (SCR) algorithm for real-time trajectory planning. Agent rules live in [AGENTS.md](AGENTS.md); the research anchor is [GOAL.md](GOAL.md).

## Getting papers in: Zotero pipeline

Papers flow from a Zotero collection into the vault. One-time setup:

1. Put your thesis papers in a Zotero collection (folder) named **Thesis** (or another name, see step 3). Each entry needs the actual PDF attached (drag the PDF onto the entry, or right-click → Find Full Text) — citation-only entries cannot be downloaded. Make sure file sync is on so the PDFs are uploaded to zotero.org.
2. Create a **read-only** API key at <https://www.zotero.org/settings/keys> (New Private Key). For a group library, grant the key read access to that group. The group's numeric ID is in its URL: `zotero.org/groups/<groupID>/<name>`.
3. Create `.env` at the repo root (gitignored — the repo is public, never commit this file):

   ```
   ZOTERO_GROUP_ID=1234567
   ZOTERO_API_KEY=your-key-here
   ZOTERO_COLLECTION=Thesis
   ```

   For a personal library, use `ZOTERO_USER_ID=` instead of `ZOTERO_GROUP_ID=` (your userID is shown on the API key page).

## Usage

- **Full pipeline (recommended):** in Claude Code, run `/zotero-ingest`. It downloads new PDFs and performs the complete AGENTS.md §5 ingestion: source note, argument-matrix row, move to `01_Corpus/ingested/<year>/`.
- **Download only:** `python scripts/zotero_pull.py`. New PDFs and their `.zotero.json` metadata sidecars land in `01_Corpus/` (the drop zone) and wait for ingestion.

The script only fetches items it has not seen before, tracked in `01_Corpus/.zotero_state.json`. Re-running is always safe. Items without a PDF attachment in Zotero are reported, not downloaded.

Note: PDFs are gitignored (copyrighted, public repo). Metadata sidecars and the state file are committed.
