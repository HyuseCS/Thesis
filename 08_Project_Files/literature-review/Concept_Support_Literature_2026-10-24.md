# Literature that supports the concept (search of 2026-10-24)

**What this covers.** New sources, not already in the library, that support the coupled (microsector-chained) fitness and the methods around it. They cover: racing principles and driver practice that cut lap time, XGBoost for tabular regression, chained prediction and error build-up, TreeSHAP, grouped validation, surrogate-assisted EAs, and the statistics for the ablation. BibTeX for every source is in `references/Concept_Support_2026-10-24.bib`.

**Search route.** Consensus first, then a web check of each record (Google Scholar could not be reached from this session, so publisher, arXiv and university repository pages stood in for it), and arXiv for preprints. I preferred open-access copies.

**Already in the library, so not repeated here:** Kapania 2016, Lenzo & Rossi 2020, Veneri & Massaro 2020, Heilmeier 2020, Braghin 2008, Kegelman 2017, Garlick & Bradley 2021, Lehman 2020, Jin 2011, Wang 2019, Chen & Guestrin 2016, Lundberg & Lee 2017, Mao 2024, Geiger 2023, Astudillo & Frazier 2021, Kyzyurova 2018, Sanson 2019, van Leeuwen 2017, Remonda 2021, Hojaji 2023/2024/2026, Nunes 2026, Bae 2025, Satujoda & Huggins 2026.

---

## Bottom line

1. **The coupling has support from three independent directions.** Optimal-control lap studies build it in. A GA over driver inputs, scored on both section time and exit speed (Maniowski 2016), shows that exit speed is treated as its own objective. A time-optimal planner improved its lap time by adding an exit-speed term at the end of each planning horizon (Taddei et al. 2025). Both say the same thing as the chain: a microsector's exit speed is worth time in the next one.
2. **Driver inputs are a sound search space.** A few parameters of steering, brake and throttle are enough to reproduce minimum-time cornering (Velenis et al. 2008). Braking-point timing alone changes lap time measurably (Peitzmeier et al. 2023). This supports treating control KPIs as the genes.
3. **XGBoost fits the data.** Large benchmarks find gradient-boosted trees as good as or better than deep models on medium-sized tabular data like yours (~15k rows), with less tuning (Grinsztajn et al. 2022; Shwartz-Ziv & Armon 2022; McElfresh et al. 2023).
4. **The three risks of a chained surrogate are documented, and the methodology already checks each of them.** First, an error in one step feeds the next, so errors build up along the chain (Venkatraman et al. 2015; Lambert et al. 2022). This is why Step 4 rolls whole test laps through the chain. Second, a model trained on true entry speeds but run on its own predicted ones sees inputs it was not trained on (Spyromitros-Xioufis et al. 2016). Third, an optimizer will find inputs that fool a learned model outside its data (Trabucco et al. 2021; Kim et al. 2025). Clipping genes to the training range addresses this. These sources turn two points the skeleton marks as "your own reasoning" (2.7.2 and 2.7.3) into cited claims.
5. **No source tests a microsector-chained learned fitness for sim racing.** That combination is still the gap. Describe it as a change relative to Hojaji et al. (2026), not as a "first".

---

## A. Racing principles: why exit speed carries into the next microsector

| # | Source | Access | Claim it supports | Where it goes |
|---|---|---|---|---|
| A1 | **Maniowski, M. (2016).** Optimisation of driver actions in RWD race car including tyre thermodynamics. *Vehicle System Dynamics* 54(4). | Abstract (repository record) | A GA optimized 16 driver-action parameters (steering, brake and throttle traces) over one corner section, with **section time and corner-exit velocity as two separate criteria**. It cut section time by about 5% and raised exit velocity by about 4%. This is the closest precedent: GA genes are driver inputs, and exit speed counts because it carries into what follows. | 2.6 (racing optimizers); 2.5 support |
| A2 | **Taddei, S., Piccinini, M., & Biral, F. (2025).** Biasing the driving style of an artificial race driver for online time-optimal maneuver planning. *IEEE Intelligent Vehicles Symposium (IV)*. arXiv:2504.12744. | Open (arXiv) | An MPC planner that **adds exit-speed maximization** at the end of its horizon to time minimization got lap times closer to the offline minimum-lap-time solution than pure time minimization did. It also moved between early and late apexes. In other words, a planner that sees only time up to a boundary falls short unless the speed handed to the next stretch is valued too. This is the same argument as coupled versus microsector-independent fitness. | 2.5 (sentence 2); ablation rationale |
| A3 | **Massaro, M., & Limebeer, D. J. N. (2021).** Minimum-lap-time optimisation and simulation. *Vehicle System Dynamics* 59(7), 1069–1113. | Open (Padova accepted manuscript) | A survey of minimum-lap-time methods (quasi-steady-state and transient; fixed and free trajectory). Use it as the single review citation for "lap time is solved as one continuous problem along the track". | 2.5 (sentence 1) |
| A4 | **Brayshaw, D. L., & Harrison, M. F. (2005).** A quasi steady state approach to race car lap simulation in order to understand the effects of racing line and centre of gravity location. *Proc. IMechE Part D* 219(6), 725–739. | Abstract | The classic quasi-steady-state lap simulation built on a GG-speed diagram. The speed profile around the lap is continuous and limited by the corners on either side. A long-standing engineering source for the mechanism Kapania and Lenzo describe. | 2.5 (sentence 1) |
| A5 | **Theodosis, P. A., & Gerdes, J. C. (2011).** Generating a racing line for an autonomous racecar using professional driving techniques. *ASME Dynamic Systems and Control Conference*, 853–860. | Abstract | Professional cornering techniques (straights, clothoids, constant-radius arcs; two-phase versus three-phase corners) can be written down and compared, and the choice changes lap time on a real car. Supports "racing practice" as something measurable, not folklore. | 2.5 or 2.3.2 (background on technique) |
| A6 | **Velenis, E., Tsiotras, P., & Lu, J. (2008).** Optimality properties and driver input parameterization for trail-braking cornering. *European Journal of Control* 14(4), 308–320. | Abstract | Trail braking falls out of the **minimum-time cornering problem under set boundary conditions** at the corner exit. A few parameters of the driver's steering, throttle and brake reproduce it across corner shapes. This supports a small set of control KPIs per microsector as a valid search space, and trail braking as one of them (Hojaji 2026 also ranks trail-braking duration highly). | Step 1 KPI pool; 2.4 |
| A7 | **Peitzmeier, F., Mockenhaupt, J., & Reith, D. (2023).** Optimum real time estimation and interfacing of braking points for racing car. *IEEE Trans. Vehicular Technology* 72(2), 1710–1719. doi:10.1109/TVT.2022.3211840 | Abstract | On a real Formula Student car, telling the driver the best braking point (from a simulation of the section ahead) reduced lap time. Supports braking inputs as KPIs that change lap time. | Step 1 KPI pool; 2.3 |
| A8 | **Löckel, S., Ju, S., Schaller, M., van Vliet, P., & Peters, J. (2023).** An adaptive human driver model for realistic race car simulations. *IEEE Trans. Systems, Man, and Cybernetics: Systems* 53(11), 6718–6730. arXiv:2203.01909 | Open (arXiv) | From the literature, a race-engineer interview and a survey of 12 experts, the authors identify how drivers adapt lap by lap to go faster. Their model fixes earlier driving errors lap after lap, the way human drivers do. Supports the view that lap time comes from correctable driver inputs, which is the premise of giving drivers optimized KPI targets. | 2.3.2; significance |

**How to use A1 and A2 without overclaiming.** Both are physics or MPC methods on one corner or one horizon. They do not use telemetry-trained surrogates. Cite them for the principle that exit speed has value beyond its own section, not as prior versions of your method.

---

## B. XGBoost for the surrogate

| # | Source | Access | Claim it supports | Where it goes |
|---|---|---|---|---|
| B1 | **Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022).** Why do tree-based models still outperform deep learning on typical tabular data? *NeurIPS 35, Datasets & Benchmarks*. arXiv:2207.08815 | Open | Over 45 datasets, tree models (XGBoost, RF) remain state of the art on medium-sized tabular data (~10k samples). They also cope better with uninformative features and irregular functions. Your pooled set (~15k rows) is in this range. | 2.7.2; Step 4 model choice |
| B2 | **Shwartz-Ziv, R., & Armon, A. (2022).** Tabular data: Deep learning is not all you need. *Information Fusion* 81, 84–90. doi:10.1016/j.inffus.2021.11.011 | Open (arXiv:2106.03253) | XGBoost beat recent deep tabular models, including on the datasets those models were introduced with, and needed much less tuning. | Step 4 model choice |
| B3 | **McElfresh, D., et al. (2023).** When do neural nets outperform boosted trees on tabular data? *NeurIPS 36, Datasets & Benchmarks*. arXiv:2305.02997 | Open | Over 176 datasets, light hyperparameter tuning of a GBDT often matters more than the choice between GBDT and neural nets. GBDTs handle skewed and heavy-tailed features better. Supports the grid search in grouped CV, and telemetry KPIs, which are often skewed. | Step 4 (grid search) |
| B4 | **Bentéjac, C., Csörgő, A., & Martínez-Muñoz, G. (2021).** A comparative analysis of gradient boosting algorithms. *Artificial Intelligence Review* 54, 1937–1967. doi:10.1007/s10462-020-09896-5 | Open (arXiv:1911.04245) | Compares XGBoost, LightGBM and CatBoost with tuned and default settings. Differences are small, and the paper shows which XGBoost hyperparameters matter most. Use it to justify XGBoost over its siblings and to pick the grid. | Step 4 (grid) |

---

## C. Chained prediction and error build-up (the risk the chain takes on)

| # | Source | Access | Claim it supports | Where it goes |
|---|---|---|---|---|
| C1 | **Spyromitros-Xioufis, E., Tsoumakas, G., Groves, W., & Vlahavas, I. (2016).** Multi-target regression via input space expansion: treating targets as inputs. *Machine Learning* 104(1), 55–98. arXiv:1211.6581 | Open (arXiv) | Regressor chains feed one predicted target in as an input to the next model. The paper names the core problem: **the chained input's values differ between training (true values) and prediction (predicted values)**, and using out-of-sample estimates during training mitigates it. Your surrogate is trained on measured v_entry,n but run on chained, predicted v_exit,n-1. This is the exact mismatch. | 2.7.3; Step 4 limitation |
| C2 | **Venkatraman, A., Hebert, M., & Bagnell, J. A. (2015).** Improving multi-step prediction of learned time series models. *AAAI-15*, 3024–3030. doi:10.1609/aaai.v29i1.9590 | Open (AAAI OJS) | When a learned one-step model is applied repeatedly, feeding its output back in as its next input, errors compound and shift the input distribution away from the training data. This is the chained rollout, n to n+1, in another field. | 2.7.3 (sentence 2); Step 4 rollout test |
| C3 | **Lambert, N., Pister, K., & Calandra, R. (2022).** Investigating compounding prediction errors in learned dynamics models. arXiv:2203.09637 | Open (preprint) | Long-horizon error in composed one-step predictions depends most on the system's own dynamics. Supports reporting rollout error as a function of chain position, not only one per-microsector MAE. | Step 4 (report error vs microsector index) |
| C4 | **Liu, Z., Wang, H., & Jin, Y. (2022).** Performance indicator-based adaptive model selection for offline data-driven multiobjective evolutionary optimization. *IEEE Trans. Cybernetics* (early access 2022). | Abstract | In offline data-driven EAs, **surrogate approximation errors accumulate and can mislead the ranking of solutions**. This backs your rule that a fitness difference counts only if it is larger than the rollout error. | Evaluation (ablation decision rule) |

**What this means for the design (my recommendation, no change needed now).** Keep the chain as designed. In Step 4, report rollout error per microsector position along the lap, and state the train/predict mismatch (C1) as a limitation. C1's remedy, training on out-of-fold predicted entry speeds, is a reasonable future-work line. It is not worth adding now because it changes Step 4's training and the rollout test already measures the effect.

---

## D. TreeSHAP and feature selection

| # | Source | Access | Claim it supports | Where it goes |
|---|---|---|---|---|
| D1 | **Lundberg, S. M., Erion, G., Chen, H., et al. (2020).** From local explanations to global understanding with explainable AI for trees. *Nature Machine Intelligence* 2, 56–67. doi:10.1038/s42256-019-0138-9 | Open (PMC) | The TreeSHAP paper: exact SHAP values for tree ensembles in polynomial time. It shows gain and split-count importances are inconsistent, and that global importance can be built by averaging local SHAP values. Cite it for the Step 3 method (mean \|SHAP\|), alongside Lundberg & Lee 2017, which is already in the library. | Step 3 |
| D2 | **Aas, K., Jullum, M., & Løland, A. (2021).** Explaining individual predictions when features are dependent: more accurate approximations to Shapley values. *Artificial Intelligence* 298, 103502. doi:10.1016/j.artint.2021.103502 | Open (arXiv:1903.10464) | Standard SHAP approximations assume independent features and can mislead when features are correlated. This is the citation for your stated limitation that correlated KPIs split credit. | Step 3 limitation |

---

## E. Grouped validation (split by driver)

| # | Source | Access | Claim it supports | Where it goes |
|---|---|---|---|---|
| E1 | **Roberts, D. R., et al. (2017).** Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure. *Ecography* 40(8), 913–929. doi:10.1111/ecog.02881 | Open | Random CV badly underestimates error when data have group structure. Blocked CV is recommended whenever such dependence exists. Laps nested in drivers are hierarchical, so this supports the by-driver split and grouped 10-fold CV. | Step 4 split |
| E2 | **Kapoor, S., & Narayanan, A. (2023).** Leakage and the reproducibility crisis in machine-learning-based science. *Patterns* 4(9), 100804. doi:10.1016/j.patter.2023.100804 | Open | A taxonomy of leakage across 17 fields, including non-independence between training and test data. Supports keeping laps whole and drivers unseen in the test set. | Step 4 split |

---

## F. Surrogate-assisted EAs and why the search stays inside the data

| # | Source | Access | Claim it supports | Where it goes |
|---|---|---|---|---|
| F1 | **Jin, Y., Wang, H., Chugh, T., Guo, D., & Miettinen, K. (2019).** Data-driven evolutionary optimization: an overview and case studies. *IEEE Trans. Evolutionary Computation* 23(3), 442–458. doi:10.1109/TEVC.2018.2869001 | Open (Jyväskylä repository) | A taxonomy of data-driven EAs. Offline problems are those where no new data can be generated during the search. Your setup (a fixed telemetry set, no simulator in the loop) is offline by this definition. It updates Jin 2011, which is already in the library. | 2.7.1 |
| F2 | **Trabucco, B., Kumar, A., Geng, X., & Levine, S. (2021).** Conservative objective models for effective offline model-based optimization. *ICML*, PMLR 139, 10358–10368. | Open (PMLR) | Optimizing against a learned model easily finds inputs that "fool" the model into predicting a good value outside the data. This is the formal version of Lehman 2020's point, and it supports clipping mutated genes to the training range and the rollout check. | 2.5 (sentence 4); Step 5 bounds |
| F3 | **Kim, M., Gu, J., Yuan, Y., Yun, T., Liu, Z., Bengio, Y., & Chen, C. (2026).** Offline model-based optimization: comprehensive review. *TMLR*. arXiv:2503.17286 | Open | Reviews offline MBO. The main difficulty is estimating the objective beyond the data, which invites "objective hacking". A recent review citation for F2's point. | 2.7.1 |
| F4 | **Malistov, A., & Trushin, A. (2019).** Gradient boosted trees with extrapolation. *IEEE ICMLA 2019*. | Abstract | Gradient-boosted trees only interpolate, so predictions degrade when a feature is outside the training range. This gives a source for the skeleton's 2.7.2 sentence 3, "tree models predict a constant outside the training range", which was marked as your own reasoning. | 2.7.2 (sentence 3); Step 5 clipping |

---

## G. Statistics for the ablation

| # | Source | Access | Claim it supports | Where it goes |
|---|---|---|---|---|
| G1 | **Derrac, J., García, S., Molina, D., & Herrera, F. (2011).** A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms. *Swarm and Evolutionary Computation* 1(1), 3–18. doi:10.1016/j.swevo.2011.02.002 | Abstract | EA results usually break the normality assumption, so pairwise nonparametric tests such as the Wilcoxon signed-rank test are the standard choice. Cite it for the paired-seed Wilcoxon in the ablation. | Evaluation |
| G2 | **Carrasco, J., García, S., Rueda, M. M., Das, S., & Herrera, F. (2020).** Recent trends in the use of statistical tests for comparing swarm and evolutionary computing algorithms: practical guidelines and a critical review. *Swarm and Evolutionary Computation* 54, 100665. doi:10.1016/j.swevo.2020.100665 | Open (arXiv:2002.09227) | Updated guidance, with each test's assumptions and pitfalls. Use it with G1 for the test choice and for reporting effect sizes as well as p-values. | Evaluation |

---

## Considered and left out

- Two Korean papers (Jang, 2002 and 2003) on corner exit speed against straight-line time. They are on topic, but I could not confirm the venue.
- Kato (2018) on expert brake and throttle timing, and Negi et al. (2019) on race drivers versus experienced drivers. Each has small samples, and van Leeuwen 2017 already covers the point.
- XGBoost+NSGA-II building and machining papers. They show XGBoost as an EA fitness, but Mao 2024 already covers that, and one record (Wu et al. 2024) could not be confirmed.
- Offline RL (COMBO and others). These are outside the scope.

## Verification notes

- Every source above appeared in Consensus with an abstract and was checked against a publisher, arXiv or repository page.
- DOIs I confirmed in the web check: A7, C2, F1. Taken from the publisher record or well known: B2, B4, D1, D2, E1, E2, G1, G2. Not shown in any page I could reach, and so left out of the BibTeX: A1, A3, A4, A5, A6, A8 (IEEE Xplore 10173774), C1, C4, F4. Importing those by title in Zotero will fill the DOIs. Check that each matches.
- "Access" says what I could read. "Abstract" means the claim rests on the abstract only, so read the paper before quoting it in the chapter.
