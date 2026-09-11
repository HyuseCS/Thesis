**Related Literature Notes:**

- Most of the research on sim-racing optimization is set to target on autonomous racing agents, with relatively less work on integrated optimization frameworks for human drivers [(Hojaji et. al. 2026; Kabzan et al. 2019; Lee et al. 2025\)](https://www.zotero.org/google-docs/?EI8dmN).&nbsp;  
- Trajectory optimization, RL control, and racing-line generation are framed as autonomous control problems in F1TENTH, TORCS, and full-size racecars [(Evans, Engelbrecht, and Jordaan 2023; Garlick and Bradley 2021; Ghignone, Baumann, and Magno 2022; Samak, Samak, and Kandhasamy 2021\)](https://www.zotero.org/google-docs/?qQYZDa). These approaches are limited when it comes to providing insights for improving human performance (Hojaji et. al., 2026).  
  &nbsp;  
  **Problem statement:**  
  Hojaji et al. (2023, 2024\) identified telemetry features associated with driver performance and showed that ML can classify performance levels and highlight key metrics such as speed, steering behavior, and lane deviation [(Hojaji et al. 2024; Hojaji, Toth, and Campbell 2023\)](https://www.zotero.org/google-docs/?0uGnbI). Hojaji et al. (2026) extended this line of work by integrating ML-based feature importance with an evolutionary algorithm to optimize sector-level performance indicators and generate faster, smoother, and more stable idealized laps for coaching purposes [(Hojaji, Toth, and Campbell 2026\)](https://www.zotero.org/google-docs/?vIvKuT). A key remaining gap is that feature importance was computed globally rather than at the **sector level**, because reliable segment-specific estimation would require larger datasets, leaving open the question of which circuit segments most strongly influence optimal lap performance [(Hojaji, Toth, and Campbell 2026\)](https://www.zotero.org/google-docs/?xv76Jr).  
  &nbsp;  
  **Objectives:**  
- To construct a micro-sector telemetry dataset by extracting and processing sequential driving data from a racing simulator environment.&nbsp;  
- To develop a predictive machine learning model that quantifies corner interdependencies and identifies optimal speed-tradeoffs across sequential track sectors.&nbsp;  
- To optimize overall lap-time performance by integrating the sector-importance model with an evolutionary algorithm, and validating the generated racing lines against human baseline telemetry.&nbsp;

&nbsp;

References:

[Evans, B., H. Engelbrecht, and H. Jordaan. 2023\. “High-Speed Autonomous Racing Using Trajectory-Aided Deep Reinforcement Learning.” *IEEE Robotics and Automation Letters* 8: 5353–59. doi:10.1109/lra.2023.3295252.](https://www.zotero.org/google-docs/?jsdCqp)&nbsp;

[Garlick, Sam, and Andrew Bradley. 2021\. “Real-Time Optimal Trajectory Planning for Autonomous Vehicles and Lap Time Simulation Using Machine Learning.” *Vehicle System Dynamics* 60: 4269–89. doi:10.1080/00423114.2021.2011929.](https://www.zotero.org/google-docs/?jsdCqp)&nbsp;

[Ghignone, Edoardo, N. Baumann, and Michele Magno. 2022\. “TC-Driver: A Trajectory-Conditioned Reinforcement Learning Approach to Zero-Shot Autonomous Racing.” *IEEE Transactions on Field Robotics* 1: 527–36. doi:10.55417/fr.2023020.](https://www.zotero.org/google-docs/?jsdCqp)&nbsp;

[Hojaji, Fazilat, Adam Toth, and Mark Campbell. 2026\. “Optimizing Sim Racing Performance Using Machine Learning and Evolutionary Algorithms:” In *Proceedings of the 18th International Conference on Agents and Artificial Intelligence*, Marbella, Spain: SCITEPRESS \- Science and Technology Publications, 997–1004. doi:10.5220/0014609600004052.](https://www.zotero.org/google-docs/?jsdCqp)&nbsp;

[Hojaji, Fazilat, Adam J. Toth, and Mark J. Campbell. 2023\. “A Machine Learning Approach for Modeling and Analyzing of Driver Performance in Simulated Racing.” In *Artificial Intelligence and Cognitive Science*, Communications in Computer and Information Science, eds. Luca Longo and Ruairi O’Reilly. Cham: Springer Nature Switzerland, 95–105. doi:10.1007/978-3-031-26438-2\_8.](https://www.zotero.org/google-docs/?jsdCqp)&nbsp;

[Hojaji, Fazilat, Adam J. Toth, John M. Joyce, and Mark J. Campbell. 2024\. “An AI Approach for Analyzing Driving Behaviour in Simulated Racing Using Telemetry Data.” In *Games and Learning Alliance*, eds. Pierpaolo Dondio, Mariana Rocha, Attracta Brennan, Avo Schönbohm, Francesca De Rosa, Antti Koskinen, and Francesco Bellotti. Cham: Springer Nature Switzerland, 194–203. doi:10.1007/978-3-031-49065-1\_19.](https://www.zotero.org/google-docs/?jsdCqp)&nbsp;

[Kabzan, Juraj, Lukas Hewing, Alexander Liniger, and Melanie N. Zeilinger. 2019\. “Learning-Based Model Predictive Control for Autonomous Racing.” *IEEE Robotics and Automation Letters* 4(4): 3363–70. doi:10.1109/LRA.2019.2926677.](https://www.zotero.org/google-docs/?jsdCqp)&nbsp;

[Lee, Hojoon, Takuma Seno, Jun Jet Tai, Kaushik Subramanian, Kenta Kawamoto, Peter Stone, and Peter R. Wurman. 2025\. “A Champion-Level Vision-Based Reinforcement Learning Agent for Competitive Racing in Gran Turismo 7.” *IEEE Robotics and Automation Letters* 10(6): 5545–52. doi:10.1109/LRA.2025.3560873.](https://www.zotero.org/google-docs/?jsdCqp)&nbsp;

[Samak, Chinmay Vilas, Tanmay Vilas Samak, and S. Kandhasamy. 2021\. “Autonomous Racing Using a Hybrid Imitation-Reinforcement Learning Architecture.” *ArXiv* abs/2110.05437. doi:10.48550/arxiv.2110.05437.](https://www.zotero.org/google-docs/?jsdCqp)&nbsp;