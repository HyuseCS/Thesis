# Literature review draft: reliability of simulator data

Moved from the methodology on 2026-10-03 at fas's request. Intended for section 2.2 (Sim racing as a research platform) of the literature review skeleton. Only the abstract was read for Wynne et al. 2019 and Himmels et al. 2024, so their claims are worded cautiously; Himmels et al. 2023's validity definitions are on p. 192.

## 2.2.x Reliability of simulator data (draft text)

**Position of this thesis.** This thesis does not claim that ACC telemetry is equivalent to real-car telemetry, and it makes no claims about real-world racing. Its context is competitive sim racing: the drivers, the laps, the fast reference and the optimized targets all exist inside ACC, and the targets the genetic algorithm produces are meant for sim racers driving the McLaren 720S GT3 at Brands Hatch in ACC. The question the thesis asks is how to drive faster in the simulator, so the data only need to be reliable for that purpose. This follows the research it builds on, which treats sim racing performance as the outcome of interest in its own right (Hojaji et al., 2024, 2026; Joyce et al., 2024).

**Why equivalence is not needed.** A simulator should not be labelled "valid" or "invalid" as a whole. Its validity depends on the research question and the dependent variables (Himmels et al., 2023). Himmels et al. (2023) separate two kinds of validity:

- **Absolute validity:** the numbers from the simulator match the numbers from real driving.
- **Relative validity:** effects in the simulator point in the same direction as effects in real driving.

Both compare a simulator with the real world. This thesis compares laps, drivers and microsectors with each other, all recorded in the same simulator with the same car, setup, track and conditions. Neither kind of validity is required for that comparison, and the thesis does not test either.

**Why the thesis does not claim equivalence.** The evidence that simulator data match real driving is mixed, which is another reason to keep the claims inside the simulator:

- A systematic review of simulator validation studies found that about half of the simulators reached absolute or relative validity and about one third gave non-valid results, and the link between fidelity and validity was "not straightforward" (Wynne et al., 2019).
- Across six driving simulators, absolute validity was good for headway distance and lateral position but inconsistent for driving speed (Himmels et al., 2024). Speed is a central outcome in this thesis.
- In a road-safety study, speed showed relative but not absolute validity, because participants drove faster in the real car (Godley et al., 2002).
- Real racing also adds physical load and stress that a simulator does not reproduce (Holland et al., 2025).

These studies concern road driving, apart from Holland et al. (2025), so they are background rather than direct evidence about ACC.

**Evidence that simulator measures reflect real skill.** Although the thesis does not rely on it, some studies suggest that measures from racing simulators do reflect real driving skill:

- In a fixed-base simulator, racing drivers had faster lap times, higher steering activity and a better racing line than non-racing drivers (van Leeuwen et al., 2017). The sample was small and the simulator was not ACC.
- In a professional driver-in-the-loop simulator, amateurs' slower lap times came mainly from weaker handling skill rather than from their choice of line (von Schleinitz et al., 2022). This was a high-end professional simulator, not ACC.
- In a pilot study with consumer racing-simulator hardware and the original Assetto Corsa, lap time correlated with driving-speed measures on a research simulator (Tiu et al., 2020). The participants and comparison were very different from this thesis.

This evidence suggests that what separates fast and slow laps in a simulator is at least partly real driving skill, not only knowledge of the game. It is supporting context, and the thesis's conclusions do not depend on it.

**Precedent for the data and pipeline.** One research group has used ACC telemetry captured with MoTeC in several peer-reviewed studies of sim racing performance (Hojaji et al., 2024, 2026; Joyce et al., 2024). Remonda et al. (2021) used per-segment telemetry features, such as brake point and segment entry and exit speeds, to compare drivers in a professional racing simulator, which is a precedent for segment-level KPIs. The developer states that ACC's tracks are laser-scanned and its physics simulate modern GT cars (KUNOS Simulazioni, n.d.); these are the developer's own claims, not independent validation, and the thesis does not rely on them.

### References

- Godley, S. T., Triggs, T. J., & Fildes, B. N. (2002). Driving simulator validation for speed research. *Accident Analysis & Prevention, 34*(5), 589-600. https://doi.org/10.1016/S0001-4575(01)00056-2
- Himmels, C., Parduzi, A., Fischer, M., & Riener, A. (2023). Towards a common understanding of driving simulator validity. In *Adjunct Proceedings of the 15th International Conference on Automotive User Interfaces and Interactive Vehicular Applications (AutomotiveUI '23 Adjunct)* (pp. 191-196). ACM. https://doi.org/10.1145/3581961.3609895
- Himmels, C., Venrooij, J., Parduzi, A., Peller, M., & Riener, A. (2024). The bigger the better? Investigating the effects of driving simulator fidelity on driving behavior and perception. *Transportation Research Part F: Traffic Psychology and Behaviour, 101*, 250-266. https://doi.org/10.1016/j.trf.2024.01.007
- Hojaji, F., Toth, A. J., Joyce, J. M., & Campbell, M. J. (2024). AI-enabled prediction of sim racing performance using telemetry data. *Computers in Human Behavior Reports, 14*, 100414. https://doi.org/10.1016/j.chbr.2024.100414
- Hojaji, F., Toth, A., & Campbell, M. (2026). Optimizing sim racing performance using machine learning and evolutionary algorithms. In *Proceedings of the 18th International Conference on Agents and Artificial Intelligence (ICAART 2026)*, Vol. 1, pp. 997-1004. SciTePress. https://doi.org/10.5220/0014609600004052
- Holland, J., Davis, M., & Ferguson, D. (2025). Physiological responses of race car drivers in authentic and simulated motor-racing. *Frontiers in Sports and Active Living, 7*, 1498686. https://doi.org/10.3389/fspor.2025.1498686
- Joyce, J. M., Campbell, M. J., Hojaji, F., & Toth, A. J. (2024). Less is more: Higher-skilled sim racers allocate significantly less attention to the track relative to the display features than lower-skilled sim racers. *Vision, 8*(2), 27. https://doi.org/10.3390/vision8020027
- Lee, J. D., Hoffman, J. D., Brown, T. L., & McGehee, D. V. (2002). *Comparison of driver braking responses in a high fidelity driving simulator and on a test track* (Report No. DOT HS 809 447). U.S. Department of Transportation, National Highway Traffic Safety Administration. https://www.nhtsa.gov/sites/nhtsa.gov/files/documents/dot_hs_809_447.pdf
- Remonda, A., Veas, E., & Luzhnica, G. (2021). Comparing driving behavior of humans and autonomous driving in a professional racing simulator. *PLOS ONE, 16*(2), e0245320. https://doi.org/10.1371/journal.pone.0245320
- Tiu, J., Harmon, A. C., Stowe, J. D., Zwa, A., Kinnear, M., Dimitrov, L., Nolte, T., & Carr, D. B. (2020). Feasibility and validity of a low-cost racing simulator in driving assessment after stroke. *Geriatrics, 5*(2), 35. https://doi.org/10.3390/geriatrics5020035
- van Leeuwen, P. M., de Groot, S., Happee, R., & de Winter, J. C. F. (2017). Differences between racing and non-racing drivers: A simulator study using eye-tracking. *PLOS ONE, 12*(11), e0186871. https://doi.org/10.1371/journal.pone.0186871
- von Schleinitz, J., Schwarzhuber, T., Wörle, L., Graf, M., Eichberger, A., Trutschnig, W., & Schröder, A. (2022). Race driver evaluation at a driving simulator using a physical model and a machine learning approach. *arXiv preprint* arXiv:2201.12939. https://arxiv.org/abs/2201.12939
- Wynne, R. A., Beanland, V., & Salmon, P. M. (2019). Systematic review of driving simulator validation studies. *Safety Science, 117*, 138-151. https://doi.org/10.1016/j.ssci.2019.04.004
