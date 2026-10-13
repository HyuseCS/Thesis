# Methodology Diagram

\[ Raw MoTeC CSVs \]  
        │  
       ▼  
1\. Sequential Preprocessing & Feature Extraction 	   (Consistent with Hojaji’s framework)  
   (Clean, slice into micro-sectors, compute scalar KPIs)  
        │  
       ▼  
2\. Performance Stratification (Clustering)		(Consistent with Hojaji’s framework)  
   (K-Means on lap times to separate Fast / Medium / Slow)  
        **│**  
        ├──────────────────────────────────────────┐  
        ▼                                          					           ▼  
   \[ Fast Cluster \]                         				     \[ Sub-Optimal Lap \]  
        │                                          						│  
       ▼                                           						│  
3\. Segment-Level Feature Selection                  			 	│  
   (Rank KPIs that predict exit speed across n→n+1)			│  
 (here, the difference is that we rank KPIs predictive of the exit speed	│  
Towards the next segment Vs. in Hojaji where they ranked KPIs most 	│  
predictive of the entire circuit’s lap time. This in theory provides a more	│  
Accurate synthetic lap produced by the DE since it accounts the 		│  
Fact that the driver’s performance of a certain microsector affects		│  
Their performance on the following microsectors.)       			│  
        │                                         					            │	  
       ▼                                          						│  
4\. Interdependency Surrogate Modeling              				│  
   (Train XGBoost: S\_n KPIs \+ V\_entry → V\_exit, Δt)			│  
(a new addition; this model will be used for predicting exit speed)		│  
        │                                          						│  
       ▼                                         					           ▼  
5\. Sequential Differential Evolution Optimization   	    		        ◄┘  
   (Seed sub-optimal lap; iteratively evolve segment KPIs via ML chain)  
(vs. Genetic algorithm used in Hojaji)

# Methodology

#### **Step 1: Sequential Preprocessing & Micro-Sector Granulation**

* **Input:** Raw 50 Hz MoTeC telemetry CSV files from simulator outings.  
* **Process:** Remove in-laps, out-laps, and invalid laps (∣z∣\>3 filter). Slice continuous telemetry into ordered micro-sectors (corners and straights) defined by the circuit track map.  
* **Output:** A structured tabular dataset where each row represents a discrete sector m of a specific lap, containing summary scalar KPIs (peak brake, trail brake duration, apex speed, peak steer angle, entry speed, exit speed, sector duration).

#### **Step 2: Performance Stratification (Clustering)**

* **Process:** Apply K-Means clustering (evaluated via the Elbow Method and Silhouette Coefficient) to stratify laps into discrete skill tiers (Fast, Medium, Slow).  
* **Role:**  
  1. Isolate the **Fast cluster** to train the surrogate model on physically valid, high-skill trajectories.  
  2. Select representative laps from the **Medium/Slow clusters** to serve as the initial evaluation baselines for DE optimization.  
     

#### **Step 3: Segment-Level Feature Selection**

* **Process:** Apply Pearson correlation and tree-based feature importance (XGBoost/Random Forest) specifically at the segment boundary level.  
* **Objective:** Identify the top K scalar KPIs in Sector n that demonstrate the highest predictive power over Sector n+1 exit velocity and combined sector time (tn​ \+ tn+1​), shifting away from global lap-time correlations.

#### **Step 4: Interdependency Surrogate Modeling**

* **Process:** Train a multi-output or chained `XGBRegressor` on the Fast cluster dataset.  
* **Mapping:**  
  𝜧ML​: (sn​, ventry,n​)⟶(Δtn​, vexit, n​, alat, peak,n​)  
* **Validation:** 10-fold cross-validation evaluated on Mean Absolute Error (MAE) and R2 to ensure the surrogate accurately models momentum transfer between adjacent sectors.

#### **Step 5: Sequential Differential Evolution Optimization**

* **Decision Vector:** A parameterized vector representing the top K scalar KPIs across all M circuit sectors:  
  x \= \[s1​,s2​,…,sM​\] ∈ RM×K  
* **Initialization:** Seed the population with a target sub-optimal human lap from Step 2, bounded by physical parameter limits \[xjmin​,xjmax​\].  
* **Fitness Evaluation:** Pass the candidate vector through the trained surrogate model sequentially:  
  ventry,n+1 ​ \= vexit,n​  
  Compute total predicted lap time ∑Δtn​ plus penalty functions for friction circle exceedance (alat​ \> alimit​).  
* **Output:** An optimized set of sector-by-sector scalar target KPIs ready to be translated directly into driver coaching recommendations.

### 

# Structural Limitations of Independent Sector Evaluation and the Sequential Optimization Justification

**The Baseline Approach and the Mechanism of Isolation** In the baseline evolutionary algorithm framework, driving trajectories are encoded as chromosomes spanning 20 track sectors, with new candidate inputs generated via two-point crossover and Gaussian mutation. A critical limitation of this architecture is its reliance on an independent, static fitness evaluation model. To estimate performance, the algorithm retrieves a baseline sector time and applies a linear adjustment based on how the mutated Key Performance Indicators (KPIs) deviate from a neutral midpoint. The fitness value of an individual—and thus the total lap time—is computed simply as the sum of all adjusted sector times across the full lap.

**The Kinematic Disconnect**

Evaluating micro-sectors in isolation fundamentally contradicts the continuous physics of real-world vehicle dynamics. Because the baseline algorithm calculates the time of microsector n independently of microsector n+1, it fails to account for causal momentum transfer. Mathematically, this allows the evolutionary algorithm to exploit the fitness function by generating unphysical driving lines (Hojaji et. al., 2026). For example, the algorithm can mutate a driver's inputs to carry maximum velocity deep into a hairpin, thereby artificially minimizing that specific sector's time, without the model recognizing that the resulting exit trajectory would compromise the subsequent straightaway, or worse, physically impossible (Eshof et. al, 2025; Roh et. al., 2025; Wachter et. al., 2026).

Hojaji (2026) recognized this potential for erratic data generation and attempted to mitigate it by applying statistical penalties to sudden KPI transitions between consecutive sectors. However, mathematically penalizing a jagged numerical transition acts merely as a statistical heuristic; it does not explicitly enforce true kinematic feasibility or simulate the physical consequences of a compromised corner exit.

**The Proposed Solution: Sequential Differential Evolution**

To resolve this limitation, the proposed framework transitions from an isolated summation model to a sequential interdependency model. By replacing the static linear scaler with an XGBoost regression surrogate, the fitness function actively simulates causality. The model explicitly calculates micro-sector n+1's entry state based on micro-sector n's predicted exit velocity.

Coupling this sequential fitness function with Differential Evolution (DE) allows for highly efficient, continuous parameter optimization across the segmented chain. When the DE algorithm proposes a set of segment KPIs, the surrogate model evaluates them chronologically, forcing the optimization loop to respect the physical conservation of momentum. This architectural shift ensures that the generated telemetry tradeoffs represent genuinely drivable, high-performance racing lines rather than statistical anomalies optimized in a vacuum.

