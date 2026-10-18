# AGENTS.md — Operating Guidelines for LLM Agents

This is a thesis vault, not a codebase. It converges literature, methodology, and measurement toward one thesis: a **learned, microsector-chained surrogate** trained on human sim-racing telemetry, used as the fitness function of an evolutionary lap optimizer, and evaluated by ablation against a microsector-independent fitness.

The vault was rebased on 2026-09-11. Its earlier subject — porting the Sequential Convex Restriction (SCR) planner to C++ — is now Related Literature only. See [[GOAL]] §8.

Read [[GOAL]] before doing anything else. It is the anchor. Every action must trace to a goal in it.

---

## 0. Settled Decisions (read first; these override older notes in this vault)

Status as of 2026-10-18. Where `GOAL.md`, `05_Living_Outline/` or older notes disagree, this section wins. The Google Doc "Thesis TODOs" is the source of truth for written thesis text; do not contradict it.

**Terminology**
- A *microsector* is one individual corner or straight. Never call these "sectors"; a sector is a larger track portion spanning several microsectors.

**Data**
- Training and testing use the Hojaji et al. (2024) Brands Hatch dataset (ACC, McLaren 720S GT3, recorded Oct 2022-Jan 2023; Computers in Human Behavior Reports 14:100414, CC BY 4.0, cite on reuse). File: `01_Corpus/data collection setup/segment_level_cleaned.csv`.
- Cleaned dataset: **817 laps, 165 drivers, M = 19 microsectors** per lap. Dropped: driver D_045 (lap-time mismatches) and the Lap 1 standing starts of P_001, P_010, P_052, P_062. "Str 0-1(End)" unified to "Str 0-1 (End)".
- Our own remotely collected laps (Brands Hatch, ACC v1.10.4, home rigs, Hojaji's instructions) are an **external test set only**. Never mix them into training, feature selection or tuning. Size: **10 drivers x 30 clean timed laps**; report external results per driver as well as pooled, and state the small driver count as a limitation.
- Lap filter: remove in/out-laps, standing starts, invalid laps and lap-time mismatches, then laps with |z| > 3 on lap time across all laps (not per driver). Applied to the main dataset and, separately, to the external laps. The 817 count is pre-|z|-filter; final counts are reported after filtering.
- Split: 70/30 train/test **by driver**; all microsectors of a lap stay together. 10-fold CV on the training set, grouped the same way. The test set is used only for the final surrogate test and the lap rollout.
- The Sebring / Ford Mustang GT3 files in `06_Datasets/` are pilot data, not thesis data.

**Variables and features**
- Genes are control KPIs (driver inputs) only. Entry/apex/exit speed and microsector time are state/outcome variables, not genes.
- v_entry,1 is fixed to the mean fast-lap entry speed at microsector 1.
- Feature selection (training laps only): drop candidate KPIs with Pearson |r| < 0.1 (Cohen, 1988) with both microsector time and exit speed. Then fit one screening XGBoost (default hyperparameters, no CV) on all training laps with the remaining KPIs, entry speed and microsector index as inputs. Rank by mean |SHAP| (TreeSHAP) per microsector, normalize per microsector per target, average the two targets, average across microsectors, keep the top **K = 10** common to all microsectors. RF, SVM and gain importance are not used. The same SHAP values give the per-microsector importance table.

**Model and optimizer**
- Surrogate: microsector-chained XGBoost on the 10 KPIs + entry speed + microsector index, trained on all valid training laps, tuned by grid search in driver-grouped 10-fold CV (MAE), then refit on all training laps. This is the first learned surrogate in this line of work (Hojaji et al. 2026 used a hand-written scaling formula).
- Optimizer: Hojaji et al. (2026)'s GA with their exact settings: population 120, 200 generations, two-point crossover 0.8, Gaussian mutation rate 0.15 with sigma 0.05, lambda 0.1, random initialization within observed KPI ranges of the training laps. 19 x 10 = 190 genes.
- Hojaji's 90-105% microsector-time clamp is **not** used.
- Differential evolution is dropped (future work only). Do not add optimizer-comparison arms.

**Evaluation**
- Ablation: coupled (chained) fitness vs a microsector-independent fitness (entry speed = mean fast-lap entry speed per microsector). Both variants' best laps are re-scored by the one chained surrogate (common judge), validated by lap rollout on test laps. Paired seeds, Wilcoxon test; a difference counts only if it exceeds rollout error.
- The human-lap vs Hojaji EA lap comparison is dropped.

**Scope**
- The thesis does not claim simulator telemetry equals real-world telemetry. The context is competitive sim racing as an esport.
- Full replication of Hojaji et al. is out of scope (no code released).

**Commits and files**
- No AI attribution anywhere: no `Co-Authored-By` trailers, no session links, no "Generated with ..." lines in commits, PR descriptions or files.

The methodology, literature review, research gap, reviewer notes, todos and references live in `08_Project_Files/` (mirrored from the project's shared folder).

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

## 2. Measurement Focus

This thesis is about *evidence*, not adjectives. When extracting from a paper or writing up our own work:

- Never write "Algorithm X is better" or "the model performs well". Write **how much better, on what data, measured how**, with the number.
- Every model result carries: dataset size, class balance, validation scheme (split or cross-validation), and the metric's definition. A single accuracy figure from one train/test split is a weak claim and must be labelled as one.
- Every runtime carries the hardware and the problem size. "3 hours of training" is meaningless without the machine and the data volume.
- Every telemetry figure carries the simulator, the car, the circuit, and the lap count. Numbers from different car/track/sim combinations are not comparable — say so rather than tabling them side by side.
- Solver time, constraint counts, and Big-O still matter for the trajectory-optimization papers in the Related Literature. Extract them as before; they characterize that body of work, they are not targets of this thesis.

## 3. Visual Mapping

Generate Mermaid.js diagrams for algorithm control flow wherever it clarifies (e.g. Tessellation → Merging → Overlapping in SCR).

Rules:
- Quote node labels containing math, brackets, or commas: `A["Merging<br/>178 polygons"]`. Unquoted labels break Obsidian's renderer.
- A diagram is a claim too. Numbers inside it need the same citation as prose — put the source under the diagram.
- Do not invent a control flow the paper does not describe. If a step's ordering is unstated, say so rather than drawing a guess.

---

## 4. Identify Blind Spots

Actively hunt gaps in the authors' methodology. This is where the thesis contribution comes from. Standing checklist for every paper:

- **Autonomous or human?** Who or what is being optimized, and is the output something a human driver could act on? This is the axis the thesis sits on.
- **What granularity?** Whole lap, sector, corner, or sample. A result reported only at lap level is a candidate for our sector-level question.
- **What is not measured?** A step described but never quantified is a candidate contribution.
- **What is tuned but never swept?** A free parameter with one reported value is an unexplored axis.
- **Commercial/proprietary tooling?** It hides whether the result is the algorithm or the solver.
- **Where does the paper hedge?** Phrases like "can be reduced by", "minor relaxation", "future work" are the author naming their own gap. Quote them exactly — an admitted gap is far stronger evidence than one you inferred.
- **What scales badly?** Anything reported at one problem size, one track, one car, or one simulator only.

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
| `06_Datasets/` | Telemetry and other data used by the thesis. |
| `07_Code/` | Analysis and model code. |
| `08_Project_Files/` | Thesis working files: methodology, literature review, research gap, reviewer notes, todos, references (.bib). |
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
