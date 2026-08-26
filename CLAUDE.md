# Vault Directives (SCR Thesis)

1. **Zero Hallucination Tolerance:** Every factual claim, performance metric, or mathematical definition must carry a citation to the source document (e.g. `Scheffe2022_SCR.pdf, Sec. V-E`).
2. **Computational Focus:** Prioritize algorithmic complexity (Big O), hardware constraints, solver time. Never write "Algorithm X is better" without *why* and *at what computational cost*.
3. **Visual Mapping:** Generate Mermaid.js charts for algorithm control flows (e.g. Tessellation -> Merging -> Overlapping).
4. **Identify Blind Spots:** Flag gaps in authors' methodologies. Simulation-only testing = flag as hardware-implementation bottleneck.

## Layout
- `01_Corpus/` — immutable `.pdf` / `.bib`. Naming: `AuthorYear_Keyword.pdf`
  - Root of `01_Corpus/` is the **drop zone**: raw, un-ingested files sit here.
  - `01_Corpus/ingested/<year>/` — a file moves here the moment its source note exists.
- `02_Source_Notes/` — one note per paper, from `Template.md`
- `03_Thematic_Synthesis/` — aggregated concepts
- `04_Argument_Matrix/matrix.md` — master comparison table
- `05_Living_Outline/` — compiling thesis draft
- `assets/` — charts and diagrams

## Ingestion Policy
A file in the root of `01_Corpus/` is **not yet ingested**. To ingest it:

1. Rename to `AuthorYear_Keyword.pdf`.
2. Write `02_Source_Notes/AuthorYear_Keyword.md` from `Template.md`, with citations to sections/figures.
3. Add a row to `04_Argument_Matrix/matrix.md` linking `[[AuthorYear_Keyword]]`.
4. **Move the file to `01_Corpus/ingested/<publication year>/`.** Create the year folder if missing.

The move is the last step and marks the work done. Anything left in the drop zone is a backlog item. Never move a file before its source note exists, and never delete from `ingested/` — the corpus is immutable.
