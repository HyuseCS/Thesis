# AGENTS.md — Operating Guidelines for LLM Agents

This is a thesis vault, not a codebase. It converges literature, methodology, and computational profiling toward one thesis on optimizing the **Sequential Convex Restriction (SCR)** algorithm for real-time trajectory planning.

Read [[GOAL]] before doing anything else. It is the anchor. Every action must trace to a goal in it.

---

## 1. The Prime Directive: Zero Hallucination

**Every factual claim, number, metric, equation, or definition in this vault carries a source.**

- From a paper: cite the file and the location. `Scheffe2022_SCR.pdf, Fig. 8` or `Sec. V-E2`. Not just the filename — the *place* in it.
- From our own work: cite the run, commit, or script that produced it.
- From nowhere: **do not write it.**

If you cannot source a number, say "not reported in the source" and move on. That sentence is a valid research finding. An invented number is thesis-ending misconduct.

Specific traps:
- Do not read a value off a bar chart and present it as exact. Write `~73 ms (Fig. 8, read from chart)`.
- Do not convert, round, or unit-shift a number and drop the original.
- Do not merge two papers' metrics into one comparison unless the hardware and scenario match. If they do not, say so.
- Do not fill a table cell with a plausible value to make the table look complete. Write `not reported`.

---

## 2. Computational Focus

This thesis is about *cost*, not elegance. When extracting or writing:

- Prioritize algorithmic complexity (Big O), constraint counts, solver time, hardware specs, sampling periods.
- Never write "Algorithm X is better." Write **why** and **at what computational cost**, with the number.
- Always attach the hardware to a timing number. "73 ms" is meaningless; "~73 ms median on an AMD Ryzen 5 3600, MATLAB R2021a + CPLEX 12.10" is a datum.
- Always attach the problem size. Solve time without constraint count or horizon length cannot be compared to anything.

---

## 3. Visual Mapping

Generate Mermaid.js diagrams for algorithm control flow wherever it clarifies (e.g. Tessellation → Merging → Overlapping in SCR).

Rules:
- Quote node labels containing math, brackets, or commas: `A["Merging<br/>178 polygons"]`. Unquoted labels break Obsidian's renderer.
- A diagram is a claim too. Numbers inside it need the same citation as prose — put the source under the diagram.
- Do not invent a control flow the paper does not describe. If a step's ordering is unstated, say so rather than drawing a guess.

---

## 4. Identify Blind Spots

Actively hunt gaps in the authors' methodology. This is where the thesis contribution comes from. Standing checklist for every paper:

- **Simulation only?** Flag as a hardware-implementation bottleneck.
- **What is not timed?** A step described but never measured is a candidate contribution.
- **What is tuned but never swept?** A free parameter with one reported value is an unexplored axis.
- **Commercial/proprietary tooling?** It hides whether the result is the algorithm or the solver.
- **Where does the paper hedge?** Phrases like "can be reduced by", "minor relaxation", "future work" are the author naming their own gap. Quote them exactly — an admitted gap is far stronger evidence than one you inferred.
- **What scales badly?** Anything reported at one problem size only.

Record findings in the note's *Critique & Optimization Vectors* section, each with a citation.

---

## 5. Vault Layout & Ingestion

| Path | Contents |
| :--- | :--- |
| `GOAL.md` | The anchor. Gates G1–G4, success criteria, non-goals, risks, revision log. |
| `01_Corpus/` | Drop zone — raw, un-ingested files. |
| `01_Corpus/ingested/<year>/` | Immutable source files, after ingestion. Never delete. |
| `02_Source_Notes/` | One note per paper, from `Template.md`. |
| `03_Thematic_Synthesis/` | Concepts aggregated across papers. |
| `04_Argument_Matrix/matrix.md` | Master comparison table. |
| `05_Living_Outline/` | The compiling thesis draft. |
| `assets/` | Charts and diagrams. |

**How files arrive:** the standard route is the Zotero pipeline — `python scripts/zotero_pull.py` downloads new PDFs from the user's Zotero collection into the drop zone, each with a `<CitationKey>.zotero.json` metadata sidecar and an entry in `01_Corpus/.zotero_state.json` (status `downloaded`). Setup is in [README.md](README.md). When the user asks to "sync zotero", "pull new papers", or "ingest", run the script and then the procedure below for each new paper.

**Ingestion procedure** — a file in the root of `01_Corpus/` is not yet ingested. Steps 1–2 are per-paper and may run in parallel (e.g. one subagent per paper); steps 3–5 touch shared files and must run sequentially in one thread:

1. Confirm the citation key `AuthorYear_Keyword`. The script proposes one; refine the `Keyword` if the paper suggests a better one (e.g. the algorithm's name). Year = publication year. If you rename, rename the PDF, the sidecar, and the `citation_key` fields in the sidecar and state file.
2. Read the whole paper, then write `02_Source_Notes/AuthorYear_Keyword.md`. Use `02_Source_Notes/Scheffe2022_SCR.md` as the structural gold standard (richer than `Template.md`). Citation data (authors, venue, DOI) comes from the sidecar, not from memory.
3. Add a row to `04_Argument_Matrix/matrix.md` linking `[[AuthorYear_Keyword]]`.
4. Move the PDF and its sidecar to `01_Corpus/ingested/<publication year>/`.
5. Set the item's `status` to `ingested` in `01_Corpus/.zotero_state.json`.

The move is the last step that matters and marks it done. Never move before the note exists. A paper that fails ingestion stays in the drop zone with status `downloaded` — report the specific blocker.

Reading large PDFs: use page ranges, and read the **whole** paper before writing the note. Appendices carry the proofs; the results section carries the numbers you actually need.

---

## 5b. Required Tooling: the Academic Research Skill

**This vault expects the `academic-research-skills` plugin. Use it — do not hand-roll what it already does.**

If your agent has it, prefer it for the tasks below. Ad-hoc prose written from scratch will drift from academic conventions; the skill enforces them.

| Task in this vault | Use |
| :--- | :--- |
| Literature search, evidence synthesis, gap mapping | `deep-research` |
| Comparing papers by WHY / HOW / WHAT | `/ars-3w` |
| Annotated bibliography for `03_Thematic_Synthesis/` | `/ars-lit-review` |
| Verifying a claim before it enters the vault | `deep-research` fact-check mode |
| Planning a chapter of `05_Living_Outline/` | `/ars-plan` |
| Building a detailed outline + evidence map | `/ars-outline` |
| Drafting the thesis or a paper from the vault | `academic-paper` |
| Checking citations | `/ars-citation-check` |
| Abstract + keywords | `/ars-abstract` |
| Simulated peer review before submission | `academic-paper-reviewer` / `/ars-reviewer` |
| Responding to real reviewer comments | `/ars-revision-coach`, `/ars-rebuttal-audit` |
| AI-use disclosure for the venue | `/ars-disclosure` |
| Full research → write → review → revise chain | `academic-pipeline` |

The skill supports §1 of this document — it has its own source-verification and citation-checking machinery. **It does not replace §1.** A citation the skill produced still needs to be true, and you still check it.

**If the skill is not available**, stop and tell the user to install it:

```
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
/reload-plugins
```

Or from the repository directly: <https://github.com/imbad0202/academic-research-skills>

Do not silently proceed without it. Say what is missing, give the commands, and let the user decide whether to install or continue anyway.

---

## 6. Writing Conventions

- Link between notes with `[[wikilinks]]`, not paths. This is an Obsidian vault.
- Citation keys are `AuthorYear_Keyword`, matching the corpus filename exactly.
- Math in LaTeX: `$inline$` and `$$block$$`.
- Keep the source paper's own notation ($H_p$, $\varepsilon_A$, $b_\text{max}$, $R_T$). Do not rename symbols — it silently breaks traceability to the source.
- Tables over prose for anything comparative.
- `GOAL.md` §7 revision log: never edit a goal silently. Bump the version, add a row.

---

## 7. Scope Discipline

- Do the task asked. Do not "improve" adjacent notes, reformat unrelated files, or reorganize the vault unprompted.
- A question is a question. "Should we use OSQP?" is not "port everything to OSQP." Answer first, act when told.
- Gates are gates. Do not start G4 work because it is more interesting than G2. An unvalidated port producing a fast lap time proves nothing.
- Corpus files are immutable. Read them, never edit them.
- `01_Corpus/**/*.pdf` is gitignored — the repo is public and the papers are copyrighted. Do not commit them.

---

## 8. Reporting

Report what happened, not what should have happened.

- A failed port, a failed simulator interface, or an extension that loses lap time are all valid, publishable findings. Report them plainly.
- Never present a projected, expected, or estimated result as measured. Label projections as projections.
- If a step was skipped or a check not run, say so.
- If an instruction here conflicts with what the data shows, follow the data and flag the conflict.
