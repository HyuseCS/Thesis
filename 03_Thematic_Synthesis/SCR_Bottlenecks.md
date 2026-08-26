# Computational Bottlenecks

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

**Thesis Trajectory:**
Optimization must target the data structures operating during the polygon expansion phase. Future literature searches: fast convex hull algorithms, parallelized geometric constraint generation, dynamic constraint dropping for distant time horizons.
