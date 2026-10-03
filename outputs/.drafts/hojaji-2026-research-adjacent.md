# Hojaji et al. research-adjacent papers: evidence extract

Date: 2026-10-03. Rule applied: no invented numbers. Only P5 was read in full text. P1, P6, P9, P10 full text was blocked (HTTP 403 on ScienceDirect, SSRN, UL repository, ResearchGate; P1 is closed access; P10 is a book chapter with no public abstract). Those entries contain only what search snippets and publisher metadata page text said.

## Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|--------|-----|-----------|------|------------|
| 1 | Joyce, Campbell, Hojaji, Toth. Less Is More. Vision 8(2):27 (2024). Full text read via PMC | https://pmc.ncbi.nlm.nih.gov/articles/PMC11130932/ | High-skill sim racers allocate less overt attention to track; corner-sector analysis | primary, full text | high |
| 2 | Toth, Hojaji, Campbell. Target acquisition kinematic phases. CHB 139:107554 (Feb 2023). Abstract only (UL Pure) | https://pure.ul.ie/en/publications/exploring-the-mechanisms-of-target-acquisition-performance-in-esp/ | Higher-expertise gamers show superior motor planning and sensory-motor integration | primary, abstract only | medium |
| 3 | Same paper, ScienceDirect abstract page | https://www.sciencedirect.com/science/article/abs/pii/S0747563222003740 | Metadata and highlights via search result only (page fetch gave 403 directly; summary text came from the tool-returned page summary) | secondary | medium |
| 4 | Hojaji et al. Deep learning KPIs in LoL. CHB Reports 19:100718 (Aug 2025). Abstract only (UL Pure) | https://pure.ul.ie/en/publications/deep-learning-techniques-for-identifying-kpis-in-league-of-legend/ | 154,000 games, Riot API, 97% accuracy; turrets lost most important | primary, abstract only | medium |
| 5 | Same, publisher page (search snippet only; fetch 403) | https://www.sciencedirect.com/science/article/pii/S2451958825001332 | Open access CC BY-NC-ND per Unpaywall; full text not read | primary, not read | low for contents |
| 6 | Murphy, Toth, Hojaji, Campbell. Force feedback drives sim racing performance. CHB Reports (2026). Abstract from search-tool summary of SSRN/ScienceDirect (page fetch 403) | https://www.sciencedirect.com/science/article/pii/S2451958826000679 | 59 sim racers, Brands Hatch, BMW M4 GT3, iRacing, 5 laps, 4 haptic conditions | secondary summary of abstract | medium |
| 7 | Same, SSRN preprint (Aug 2025) | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5392178 | Preprint page (not fetched; 403) | primary, not read | low |
| 8 | PESS blog post on P9 | https://pess.blog/2026/03/19/publication-force-feedback-drives-sim-racing-performance-the-influence-of-force-and-vibrotactile-haptic-feedback-in-simulator-steering-wheels-dr-adam-toth/ | Publication date 19 Mar 2026; impact statement only | secondary | medium |
| 9 | Routledge, The Psychology of Esports Performance (2026) | https://www.routledge.com/The-Psychology-of-Esports-Performance/Sharpe-Poulus/p/book/9781041122067 | Chapter listed (as "Chapter 4"); no chapter abstract | primary, TOC only | high for listing |
| 10 | Taylor & Francis chapter page (DOI redirect) | https://www.taylorfrancis.com/books/9781003663676/chapters/10.4324/9781003663676-5 | Title and authors only; page showed "Chapter Number: 5" (differs from Routledge "Chapter 4"; unresolved) | primary, metadata | medium |
| 11 | Unpaywall record for P6/P9/P1 | https://api.unpaywall.org/v2/10.1016/j.chbr.2025.100718 | P6 and P9 gold OA CC BY-NC-ND; P1 closed | primary metadata | high |

## P5 (Joyce et al. 2024, Vision) [1] -- FULL TEXT READ

1. Question and setup: do high- and low-skilled sim racers allocate visual attention differently in time-trial driving? Assetto Corsa Competizione v1.8.18, McLaren 720S GT3 (fixed setup), Brands Hatch. Playseat Sensation, Logitech G Pro wheelbase and pedals, 55-inch Samsung monitor at 120 Hz. (Methods) [1]
2. Sample: N = 88 after exclusions (104 initial). Skill = lap-time percentile split: top 25% high (n=22), bottom 25% low (n=22). Age 30.84 +/- 9.51. 8 laps at maximum speed; fastest lap analysed. Eye tracking: Tobii Pro Glasses 3, 50 Hz. [1]
3. Method: independent t-tests with Sidak correction, Cohen's d, Shapiro-Wilk; 3 outliers removed. AOIs: TRACK vs HUD elements. Metrics: total fixation duration (TFD), average fixation duration, fixation count, normalised to lap time and corner-sector time, TRACK:HUD ratio. No ML, no cross-validation. [1]
   Reported (high vs low): lap time 87,029 +/- 1,238 ms vs 96,480 +/- 4,855 ms, p<0.001, d=2.762. TFD 80,681 +/- 2,070 vs 91,183 +/- 5,483 ms, d=2.661. Normalised TFD 92.71 +/- 2.11% vs 94.50 +/- 2.8%, p=0.013, d=0.729. TRACK:HUD 2.44 +/- 1.06 vs 4.11 +/- 2.27, p=0.003, d=0.969. Corner TFD 44,170 +/- 6,615 vs 55,147 +/- 11,210 ms, d=1.220. Normalised corner TFD 101.70 +/- 15.82% vs 113.79 +/- 16.95%, p=0.018, d=0.740. No significant difference in fixation count or average fixation duration. [1]
4. Granularity: whole lap and 9 corner sectors on the fastest lap. Corner-level metrics reported as aggregate over corners per the extract; per-corner results not confirmed in my extract (unverified). [1]
5. Sector-level implication: the paper's own claim is attention-related ("High-skilled sim racers allocate significantly less overt attention to the track relative to other areas of the display"). Nothing about telemetry-based sector analytics: not addressed. [1]
6. Code/data: "Data can be obtained from M.J.C. via email request." No code repository. [1]
7. Limitations (Discussion, quotes via fetch tool):
   - "Unfortunately, given that our eye tracking device had a low sampling rate of 50 Hz, we could not accurately measure smooth pursuit movement."
   - "it is possible that participants could have also been covertly attending."
   - "The groups in the current study may be more homogenous compared to those previous studies given that low-skilled sim racers still committed over 4 h per week to sim race training."
   Future work: "Eye movement variables that were not assessed in this study, such as saccades and gaze distribution, should be investigated in the future".
   Caveat: quotes were returned by a summarising fetch tool, not verbatim from my own reading of raw text; re-check against the PMC page before quoting in the thesis.

## P1 (Toth, Hojaji, Campbell, CHB 139:107554, 2023) [2][3][11] -- ABSTRACT ONLY
Note: published online 2022-11-02, issue Feb 2023. Title: "Exploring the mechanisms of target acquisition performance in esports: The role of component kinematic phases on a first person shooter motor skill."
1. Question: how expert gamers differ from amateurs in FPS target acquisition via kinematics of cursor movement; effect of practice and tDCS. Game/task: FPS aiming motor skill (specific game/task not confirmed). [2][3]
2. Sample, skill measure, trials: not read. 
3. Method/numbers: not read. Abstract claim only: "gamers of higher expertise show evidence of superior motor planning and sensory-motor integration". Keywords: kinematics, motor learning, tDCS. [2][3]
4. Granularity: kinematic phases within a single aiming movement (title); details not read.
5. Sim racing implication: not addressed (as far as abstract shows). Not relevant to sim racing except as lab precedent for phase-level decomposition of a skill.
6. Code/data: unknown. 7. Limitations: not read.

## P6 (Hojaji et al., CHB Reports 19:100718, Aug 2025) [4][5] -- ABSTRACT ONLY
Authors: Hojaji, McIlroy, Dupuy, Pedroni, Toth, Campbell.
1. League of Legends: win prediction, map navigation, vision control. [4]
2. Sample: 154,000 games from Riot Games' official API. Skill measure and per-player split: not read. [4]
3. Method: neural network (deep learning) models; "97 % accuracy" in predicting outcome. Validation scheme, architecture, hyperparameters, importance method: not read. Importance order per abstract: fewer turrets lost, then higher bounty level, turrets destroyed, less damage taken, more dragons. "higher-skilled players spend more time near key map objectives". [4]
4. Granularity: whole-match outcome features plus map-position (spatial) analysis; phase-level detail not read.
5. Sim-racing implication: not addressed. Inference only: same lab uses ML to rank KPIs, which is the methodological analogue for sector-level KPI ranking.
6. Code/data: Riot API data; any release statement not read. 7. Limitations: not read.

## P9 (Murphy, Toth, Hojaji, Campbell, CHB Reports 2026) [6][7][8] -- ABSTRACT-LEVEL ONLY
Published 2026-03-09 per search summary; blog dated 2026-03-19. Open access (Unpaywall) but ScienceDirect blocked me.
1. Question: effect of force feedback (FFB) and vibrotactile feedback on sim racing performance. iRacing, BMW M4 GT3, Brands Hatch. [6]
2. Sample: 59 experienced sim racers in mid- and high feedback-intensity groups; 5 laps; 4 conditions (none, FFB only, vibrotactile only, combined). Skill measure: not read. [6]
3. Method/results from abstract summary: FFB-only lap times faster than none and vibrotactile-only; mid intensity faster than high or no FFB; no benefit from vibrotactile; participants rated any-feedback conditions higher. Stats test, effect sizes, p-values: not read. [6]
4. Granularity: lap times (whole lap) per the summary; sector analysis not confirmed.
5. Sector-level implication: not read.
6. Code/data: not read. 7. Limitations/future work: not read.
Caveat: the abstract wording came through a search-tool summary, not my own read of the page.

## P10 (Campbell, Hojaji, Cregan, Toth, chapter, 2026) [9][10]
In "The Psychology of Esports Performance" (Routledge, 2026), listed in Section I "Foundations of Esports Psychology". No abstract reachable. Contents, numbers, limitations: not read. Chapter number conflict (Routledge says 4; T&F page says 5; DOI ends -5): unresolved.

## Coverage Status
- Read in full: P5 only.
- Abstract/metadata only: P1, P6, P9 (via search-tool summaries), P10 (title and authors only).
- Blocked: ScienceDirect (403), SSRN (403), UL research repository (403/401), ResearchGate (403), Elsevier API (400). Crossref and Semantic Scholar have no abstracts for these DOIs.
- Fix suggestion: user opens P6 and P9 via campus or browser (both CC BY-NC-ND open access) and drops PDFs in the corpus; then re-run extraction items 2-7. P1 needs library access.
