# SCR Computational Bottlenecks

**Scope note (2026-09-11):** this page is Related Literature only. Since the rebase ([[GOAL]] v0.2) the thesis does not optimize SCR. Kept because it characterizes the autonomous trajectory-optimization branch of Chapter 2.

**Current Consensus on SCR Inefficiencies:**
The core limitation of the Sequential Convex Restriction (SCR) is not its mathematical safety, but its polynomial time complexity per iteration.

- **The Constraint Bloat:** SCR demands an inherently higher number of constraints than SL because it approximates the track as overlapping convex polygons.
- **The Geometric Generation Overhead:** The step-by-step process of Tessellation $\rightarrow$ Merging $\rightarrow$ Overlapping is currently evaluated iteratively.

```mermaid
flowchart LR
    A[Track Boundary] --> B[Tessellation]
    B --> C[Merging]
    C --> D[Overlapping]
    D --> E[Convex Constraint Set]
```

**Why it sits in the RRL:** SCR buys a feasibility guarantee with roughly double the solve time of SL (~73 ms vs ~35 ms, `Fig. 8`). That trade is a controller-design concern. It produces no per-corner attribution and no output a human driver can act on, which is the limitation the base document names for this whole branch of work (`thesis new base.md`, Related Literature Notes).
