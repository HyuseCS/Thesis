# Sources to add to Zotero

Compiled 2026-09-26 from every [add] item in `literature-review/Literature_Review_Skeleton.md`. There are 38 items, and each appears once. DE-related papers are left out because DE was dropped.

## Part 1: paste into Zotero (25 items)

In Zotero, click the magic wand icon ("Add Item by Identifier"), paste this whole block, and press Enter. Zotero accepts one identifier per line.
After the import, check that each imported title matches the list in Part 3. Identifiers marked "confirm" in Part 3 came from memory rather than a verified page, so a wrong one would import a different paper.

```
10.1371/journal.pone.0245320
10.1016/j.chbr.2024.100414
10.2139/ssrn.5263021
10.1109/ACCESS.2025.3615128
arXiv:1705.07874
arXiv:2401.04206
10.1145/3744333.3747811
10.3390/e28090960
arXiv:2201.12939
10.1115/1.4033311
10.1080/00423114.2019.1608349
10.3390/app10041498
10.1080/00423114.2019.1631455
10.1016/j.compstruc.2007.04.028
arXiv:2601.21027
arXiv:2002.04794
10.1007/978-3-642-20525-5_15
10.1007/s10710-014-9227-z
10.1016/j.swevo.2011.05.001
10.1109/TEVC.2018.2834881
10.1162/artl_a_00319
10.1145/2939672.2939785
10.3390/vehicles8070146
arXiv:2112.15311
arXiv:2602.17679
```

## Part 2: add by title (13 items)

These have no identifier I could verify, and Crossref was blocked from here. Search each title in Google Scholar, open the publisher page, and save it with the Zotero Connector. For Goldberg, use the ISBN.

1. Kegelman, Harbott & Gerdes (2017). "Insights into vehicle trajectories at the handling limits: analysing open data from race car drivers." *Vehicle System Dynamics*.
2. Han et al. (2025). "Development of a Driving Guidance System to Improve Racing Performance." IEEE ITSC 2025.
3. Bugeja et al. (2017). "Telemetry-based optimisation for user training in racing simulators." VS-Games 2017.
4. Goldberg (1989). *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley. ISBN 0201157675. Alternatively, Holland (1975), *Adaptation in Natural and Artificial Systems*. Pick one.
5. Cardamone, Loiacono, Lanzi & Bardelli (2010). "Searching for the optimal racing line using genetic algorithms." IEEE CIG 2010.
6. Botta, Gautieri, Loiacono & Lanzi (2012). "Evolving the optimal racing line in a high-end racing game." IEEE CIG 2012.
7. Klapálek et al. (2024). "Study of Track Segmentation for Lap Time Optimization." SCITEPRESS. PDF: https://www.scitepress.org/Papers/2024/127286/127286.pdf
8. Klapálek et al. (2026). "Adapting to unknown environment conditions in autonomous racing competition using Iterative Learning Control." *Robotics and Autonomous Systems*.
9. Mao et al. (2024). "An XGBoost-assisted evolutionary algorithm for expensive multiobjective optimization problems." *Information Sciences*.
10. Kyzyurova, Berger & Wolpert (2018). "Coupling Computer Models through Linking Their Statistical Emulators." *SIAM/ASA J. Uncertainty Quantification*.
11. Sanson, Le Maître & Congedo (2019). "Systems of Gaussian process models for directed chains of solvers." *Computer Methods in Applied Mechanics and Engineering*.
12. Chen et al. (2004). "Modelling and optimization of fed-batch fermentation processes using dynamic neural networks and genetic algorithms." *Biochemical Engineering Journal*.
13. Geiger et al. (2023). "Solving multi-objective inverse problems of chained manufacturing processes." *CIRP Journal of Manufacturing Science and Technology*. https://www.sciencedirect.com/science/article/abs/pii/S1755581722001833

## Part 3: key for Part 1 (what each identifier should import)

| Identifier | Paper | Skeleton section | Check |
|---|---|---|---|
| 10.1371/journal.pone.0245320 | Remonda et al. 2021, human vs autonomous driving in a racing simulator, *PLOS ONE* | 2.2 | confirm |
| 10.1016/j.chbr.2024.100414 | Hojaji et al. 2024, "AI-enabled prediction of sim racing performance using telemetry data" | 2.2, 2.3.1 | confirm |
| 10.2139/ssrn.5263021 | Hojaji et al., "Evaluating the Consistency of Key Performance Metrics Across Different Tracks in Sim Racing Using Machine Learning" (SSRN) | 2.3.1 | confirm |
| 10.1109/ACCESS.2025.3615128 | Bae et al. 2025, counterfactual and language-based driver training | 2.3.2 | |
| arXiv:1705.07874 | Lundberg & Lee 2017, SHAP (only if you use SHAP) | 2.3.2 | |
| arXiv:2401.04206 | Kaufman et al. 2024 (TRI), learning racing from an AI coach | 2.3.3 | |
| 10.1145/3744333.3747811 | Costa et al. 2025, conversational AI coach, AutomotiveUI | 2.3.3 | |
| 10.3390/e28090960 | Nunes et al. 2026, Shannon entropy and LLM feedback, *Entropy* | 2.3.3 | |
| arXiv:2201.12939 | von Schleinitz et al. 2022, race driver evaluation at a driving simulator | 2.3.3 | |
| 10.1115/1.4033311 | Kapania, Subosits & Gerdes 2016, sequential two-step racing trajectories | 2.4 | |
| 10.1080/00423114.2019.1608349 | Veneri & Massaro 2020, free-trajectory quasi-steady-state minimum lap time | 2.4 | confirm |
| 10.3390/app10041498 | Lenzo & Rossi 2020, mono-dimensional lap time optimisation | 2.4 | |
| 10.1080/00423114.2019.1631455 | Heilmeier et al. 2020, minimum curvature trajectory planning | 2.4 | |
| 10.1016/j.compstruc.2007.04.028 | Braghin et al. 2008, race driver model | 2.4 | |
| arXiv:2601.21027 | Nam et al. 2026, track-centric iterative learning, IEEE RA-L | 2.5 | |
| arXiv:2002.04794 | Jain & Morari 2020, computing the racing line using Bayesian optimization | 2.5 | confirm |
| 10.1007/978-3-642-20525-5_15 | Quadflieg, Preuss & Rudolph 2011, "Driving Faster Than a Human Player" | 2.6.2 | |
| 10.1007/s10710-014-9227-z | Quadflieg et al. 2014, "Driving as a human", *GPEM* | 2.6.2 | |
| 10.1016/j.swevo.2011.05.001 | Jin 2011, surrogate-assisted evolutionary computation | 2.7.1 | confirm |
| 10.1109/TEVC.2018.2834881 | Wang, Jin, Sun & Doherty 2019, offline data-driven EA with selective surrogate ensembles | 2.7.1 | confirm |
| 10.1162/artl_a_00319 | Lehman et al. 2020, "The Surprising Creativity of Digital Evolution" | 2.7.1 | confirm |
| 10.1145/2939672.2939785 | Chen & Guestrin 2016, XGBoost | 2.7.2 | |
| 10.3390/vehicles8070146 | Satujoda & Huggins 2026, staged GT3 setup optimization | 2.7.2 | |
| arXiv:2112.15311 | Astudillo & Frazier 2021, Bayesian optimization of function networks | 2.7.3 | |
| arXiv:2602.17679 | Kiroirwal, Pfrommer & Beyerer 2026, joint parameter and state-space BO | 2.7.3 | |

For Kapania 2016 an open-access copy is at arXiv:1902.00606. For Lehman 2020 one is at arXiv:1803.03453.

## Part 4: added 2026-10-03 for section 2.2 (simulator validity and reliability)

Paste into "Add Item by Identifier" as before. Remonda 2021 (10.1371/journal.pone.0245320) is already in Part 1. Add the KUNOS ACC product page with the Zotero Connector as a web page.

```
10.1145/3581961.3609895
10.1016/j.trf.2024.01.007
10.1371/journal.pone.0186871
10.1016/j.ssci.2019.04.004
10.1016/S0001-4575(01)00056-2
10.3389/fspor.2025.1498686
10.3390/geriatrics5020035
10.3390/vision8020027
```
These are Himmels et al. 2023, Himmels et al. 2024, van Leeuwen et al. 2017, Wynne et al. 2019, Godley et al. 2002, Holland et al. 2025, Tiu et al. 2020 and Joyce et al. 2024, with references taken from `literature-review/Simulator_Reliability_Draft.md`.
