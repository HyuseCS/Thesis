> **SUPERSEDED (2026-09-11).** This is the original vault specification, written when the thesis was about optimizing SCR. The vault was rebased on `01_Corpus/thesis new base.md`. Current rules: [AGENTS.md](AGENTS.md). Current anchor: [GOAL.md](GOAL.md). Kept for history only.

# LLM Thesis Repository: SCR Optimization

This repository is designed to strictly converge literature, methodologies, and computational profiling toward drafting a thesis on optimizing the Sequential Convex Restriction (SCR) algorithm for real-time trajectory planning.

## 1. Directory Structure
Initialize the following folders in the root directory:
- `01_Corpus/` (Strictly immutable `.pdf` and `.bib` files. Naming convention: `AuthorYear_Keyword.pdf`)
- `02_Source_Notes/` (LLM-generated methodological breakdowns of each paper)
- `03_Thematic_Synthesis/` (Aggregated concepts: e.g., Polygon Generation, Time Complexity, SL vs SCR)
- `04_Argument_Matrix/` (Tabular tracking of conflicting methodologies or performance benchmarks)
- `05_Living_Outline/` (The continuously compiling draft of the final thesis)
- `assets/` (Visualizations, performance charts, and Mermaid diagrams)

## 2. LLM System Prompt (The Schema)
*Provide these instructions to your LLM agent when interacting with this vault.*

**Directives:**
1. **Zero Hallucination Tolerance:** Every factual claim, performance metric, or mathematical definition written in this repository must be appended with a citation to the specific source document (e.g., `Scheffe2022_SCR.pdf, Sec. V-E`).
2. **Computational Focus:** When extracting information, prioritize algorithmic complexity (Big O), hardware constraints, and solver time metrics. Do not settle for "Algorithm X is better"; extract exactly *why* and *at what computational cost*.
3. **Visual Mapping:** Wherever applicable, generate Mermaid.js charts to visualize algorithm control flows (e.g., Tessellation -> Merging -> Overlapping steps in SCR). 
4. **Identify Blind Spots:** Actively search for gaps in the authors' methodologies. If a paper tests exclusively in simulation, flag it as a potential bottleneck for physical hardware implementation.

## 3. Core File Templates

### A. The Literature Matrix (`04_Argument_Matrix/matrix.md`)
Maintain a master table of all ingested papers to track performance trade-offs.

| Citation Key | Core Algorithm | Constraint Handling | Median Solver Time | Track Adherence | Core Bottleneck |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Scheffe2022_SCR` | SCR | Restriction (Polygons) | ~75ms (Double SL) | Guaranteed | Polygon overlap & generation constraint bloat |
| `[Next_Paper]` | SL | Relaxation (Linear) | ~35ms | Violates physical bounds | Trust region prohibitive at start |

### B. Source Note Template (`02_Source_Notes/Template.md`)
*Use this structure for every ingested paper.*

**1. Provenance & Objective**
- Citation: 
- Core Goal: (e.g., Real-time Model Predictive Control trajectory planner)

**2. Methodology Breakdown**
- Vehicle Model Used: 
- Track Convexification Method: 
- Optimization Solver: 

**3. Key Findings & Performance Metrics**
- (Extract exact latency numbers, lap times, and hardware specs used for benchmarking)

**4. Critique & Optimization Vectors**
- What are the computational flaws in this paper?
- Where can the data structures or loops be optimized (e.g., parallelizing the polygon generation)?

### C. Thematic Synthesis: Computational Bottlenecks (`03_Thematic_Synthesis/SCR_Bottlenecks.md`)
*Continuously update this page as new papers are ingested.*

**Current Consensus on SCR Inefficiencies:**
The core limitation of the Sequential Convex Restriction (SCR) is not in its mathematical safety, but its polynomial time complexity per iteration. 
*   **The Constraint Bloat:** SCR demands an inherently higher number of constraints than SL because it approximates the track as overlapping convex polygons. 
*   **The Geometric Generation Overhead:** The step-by-step process of Tessellation $\rightarrow$ Merging $\rightarrow$ Overlapping is currently evaluated iteratively. 

**Thesis Trajectory:** 
The optimization must target the data structures operating during the polygon expansion phase. Future literature searches should focus on fast convex hull algorithms, parallelized geometric constraint generation, or dynamic constraint dropping for distant time horizons.
