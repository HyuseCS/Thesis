# Vault Directives (SCR Thesis)

1. **Zero Hallucination Tolerance:** Every factual claim, performance metric, or mathematical definition must carry a citation to the source document (e.g. `Scheffe2022_SCR.pdf, Sec. V-E`).
2. **Computational Focus:** Prioritize algorithmic complexity (Big O), hardware constraints, solver time. Never write "Algorithm X is better" without *why* and *at what computational cost*.
3. **Visual Mapping:** Generate Mermaid.js charts for algorithm control flows (e.g. Tessellation -> Merging -> Overlapping).
4. **Identify Blind Spots:** Flag gaps in authors' methodologies. Simulation-only testing = flag as hardware-implementation bottleneck.

## Layout
- `01_Corpus/` — immutable `.pdf` / `.bib`. Naming: `AuthorYear_Keyword.pdf`
- `02_Source_Notes/` — one note per paper, from `Template.md`
- `03_Thematic_Synthesis/` — aggregated concepts
- `04_Argument_Matrix/matrix.md` — master comparison table
- `05_Living_Outline/` — compiling thesis draft
- `assets/` — charts and diagrams
