# Evidence: Hojaji P4 (CHB Reports 2024) and P7 (SSRN 2025) — telemetry papers

Date of check: 2026-10-03. Task: read full text of P4 and P7 and extract 10 items.

## Coverage Status (read this first)

**The full text of neither paper could be read.** Every route was tried and blocked.

| Route tried | Result |
|---|---|
| ScienceDirect article page (WebFetch, curl, headless Chromium) | HTTP 403 / Cloudflare "Just a moment" / Cloudflare error 1000 |
| ScienceDirect via r.jina.ai proxy | Captcha page returned |
| Elsevier API `api.elsevier.com/content/article/pii/...` | HTTP 400 (no API key / view not allowed) |
| SSRN 4683736, 5255017, 5263021 (`papers.cfm`, `Delivery.cfm`, `doi.org`) | HTTP 403 "Content Blocked" (Elsevier Content Protection) |
| ResearchGate 379899903 / 377170551 | HTTP 403 / "Access restricted" |
| UL Pure page | HTTP 200, **abstract only** (read directly) |
| UL research repository (figshare/DSpace, DOI 10.34961/researchrepository-ul.25795402.v1) | HTTP 403 for page; figshare API "Entity not found"; no file link found |
| Unpaywall, Semantic Scholar `openAccessPdf`, OpenAlex locations | All point back to the blocked publisher DOI; no direct PDF URL. S2 has no record of the SSRN DOIs. |
| Wayback Machine, scholar.archive.org, fatcat, Europe PMC, CORE | No snapshot / challenge page / no record / HTTP 429 |

I did not try to defeat the bot protection any further.

What I **did** read directly:
- P4 abstract (UL Pure page, DOAJ record).
- P4, P7 reference lists (Crossref).
- P7 abstract via search-engine result text only (SSRN page itself blocked).
- The **2026 ICAART paper (P8)** in the local vault (`/home/hyuse/Desktop/Thesis/01_Corpus/ingested/2026/Hojaji2026_TelemetryEA.pdf`) and the local vault notes for P3 and P8. These are different papers. They are secondary evidence about P4/P7.

What I got only as **search-engine summary text** (the search tool's own paraphrase of the page; I did not see the page; marked "snippet" below). These summaries mixed content between papers at least once (a P7 query returned P8's abstract wording), so treat each snippet as **unverified** and check against the PDF before citing.

**Where the user can get the PDFs:** P4 is CC-BY open access. Open `https://doi.org/10.1016/j.chbr.2024.100414` in a normal browser, download, and drop the PDF in `01_Corpus/` for ingestion. P7 needs a browser on SSRN (`https://ssrn.com/abstract=5255017` or `5263021`).

## Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|---|---|---|---|---|
| 1 | UL Pure record, P4 (abstract, read directly) | https://pure.ul.ie/en/publications/ai-enabled-prediction-of-sim-racing-performance-using-telemetry-d/ | MoTeC i2 Pro v1.1.5, ACC v1.9, 174 participants, 1327 laps, Brands-Hatch; laps clustered by lap time; hybrid feature selection (two correlation analyses + three ML models); best accuracy 97.19%; speed > lateral acceleration > steering angle > lane deviation | primary (abstract) | high |
| 2 | DOAJ record P4 | https://doaj.org/api/search/articles/doi:10.1016/j.chbr.2024.100414 | Bibliographic data, keywords, CC-BY; May 2024; vol 14 | primary (metadata) | high |
| 3 | Crossref P4 reference list | https://api.crossref.org/works/10.1016/j.chbr.2024.100414 | 54 references; cites MoTeC i2 Pro, MacQueen k-means, Breiman RF, Chen XGBoost, Cortes SVM, Lundberg SHAP, Remonda 2021 | primary (metadata) | high |
| 4 | Crossref SSRN 5255017 (P7) | https://api.crossref.org/works/10.2139/ssrn.5255017 | 26 listed references; cites P4 first, k-means, GBM, XGBoost, SVM (Cristianini), RF, "Brands Hatch vs Laguna Seca" web source, Remonda 2025 benchmark | primary (metadata) | high |
| 5 | Crossref SSRN 5263021 (P7, second record) | https://api.crossref.org/works/10.2139/ssrn.5263021 | Same title; 17 references; same first 17 refs as 5255017 | primary (metadata) | high |
| 6 | SSRN P7 page (search-engine text only; page blocked) | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5255017 and https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5263021 | Pipeline: data collection, preprocessing, clustering, ML modelling; Laguna Seca vs earlier Brands Hatch; 135 participants, 1180 laps; "average speed, lateral acceleration, steering reversal rate, and lane deviation showed high congruence" | snippet | medium |
| 7 | P8 ICAART 2026 PDF (local vault, read directly) | file: /home/hyuse/Desktop/Thesis/01_Corpus/ingested/2026/Hojaji2026_TelemetryEA.pdf ; public copy https://www.scitepress.org/Papers/2026/146096/146096.pdf | Same Gamescom 2024 Laguna Seca dataset (135 participants, 1,180 laps). Says KPI definitions "are provided in our previous study (Hojaji et al., 2024)" | primary (different paper) | high |
| 8 | Local vault note for P8 | file: /home/hyuse/Desktop/Thesis/02_Source_Notes/Hojaji2026_TelemetryEA.md | Rig, logger, 50 Hz, 74 channels, cleaning counts, top-10 KPI list for the Laguna Seca data | secondary (own notes) | medium |
| 9 | Local vault note for P3 (GALA 2023) | file: /home/hyuse/Desktop/Thesis/02_Source_Notes/Hojaji2024_DrivingBehaviour.md ; paper https://link.springer.com/chapter/10.1007/978-3-031-49065-1_19 | Earlier Brands Hatch paper by same authors with KPI wording (lane deviation, steering reversal, trail braking, throttle release) | secondary (different paper) | medium |
| 10 | Web-search summaries of P4 full text (ScienceDirect page) | https://www.sciencedirect.com/science/article/pii/S2451958824000472 | Snippet claims: 84 features; two datasets with 62 features each; 1,327 laps and 15,694 segment rows; K by Elbow + Silhouette; XGBoost AUC 0.971, accuracy 0.96, F1 0.93, abs. mean error 0.011; 19 segments (S1..S10, T1..T9); MoTeC gives no off-track information | snippet | low |

## Findings

Legend: **[READ]** I read the text myself. **[ABS]** from the abstract I read. **[SNIP]** search-engine summary only; unverified. **[SEC]** from a different paper or my own vault notes; not from P4/P7. **[NR]** not retrievable.

### P4 — Hojaji, Toth, Joyce, Campbell (2024), Computers in Human Behavior Reports 14, 100414

**1. Simulator, car, circuit, rig, logger, rate, channels**
- Logger: MoTeC i2 Pro v1.1.5 (Australia). Simulator: Assetto Corsa Competizione v1.9 (KUNOS Simulazioni). Circuit: Brands-Hatch. "professional racing simulator". [ABS][1]
- Car, rig hardware, sample rate: **not retrievable**. [NR]
- Channels: snippet says "out of 84 features, a subset of 10 features was selected"; two datasets "each containing 62 data features" [SNIP][10]. In P3 (different paper) MoTeC records "up to 84 metrics" at 50 Hz [SEC][9]. Do not assume P4 uses 50 Hz without checking.

**2. Participants, laps, cleaning**
- 174 participants, 1327 laps. [ABS][1]
- Snippet: lap dataset 1,327 laps; segment dataset 15,694 rows [SNIP][10]. Whether 1,327 is before or after cleaning is **unknown**. Raw lap count, cleaning rules, thresholds: [NR]. (The reference list includes Smiti 2020 "A critical overview of outlier detection methods" and Tukey 1977, which suggests an outlier step [3]; this is an inference, not a reading.)
- The same authors' P3 removed zero-time, in-laps, out-laps and used z-score outlier removal; z threshold not reported in P3 [SEC][9]. P8 used |z| > 3 [SEC][8]. Not confirmed for P4.

**3. Performance labels**
- "We clustered the obtained laps based on performance (lap-time), and then identified driving behaviors within performance groups." [ABS][1]
- k chosen by Elbow method and Silhouette Coefficient (snippet) [SNIP][10]. Reference list has MacQueen (k-means) [3]. k value, cluster sizes, balance: [NR]. A clustering "accuracy rate of 86.34%" appears in a snippet [SNIP, unverified]. Note P3 reported an undefined "accuracy" of 81.42% for k-means [SEC][9]; the same issue (what accuracy means for unsupervised clustering) probably applies.

**4. Granularity**
- Two datasets, one lap-level (throughout the lap) and one segment-level (specific segments of the track); segment dataset 15,694 rows [SNIP][10]. Snippet says Brands-Hatch has 19 segments: 10 straights (S1..S10) and nine turns (T1..T9) [SNIP][10]. This conflicts with P3, which my note records as S1–S9 and T1–T9 [SEC][9]. Check in the PDF.
- Whether any sector-level result (importance or accuracy per sector) is reported: [NR]. Abstract mentions only the lap ("critical factors that influenced driving performance during a lap") [ABS][1].

**5. KPI list and definitions**
- Abstract names: average speed, lateral acceleration, steering angle, lane deviation. [ABS][1]
- Snippet for P4 top 5 (XGBoost): averages of "(i) speed, (ii) absolute lateral acceleration, (iii) steering reversal rate per lap, (iv) lane deviation and (v) absolute steering angle." [SNIP] The search tool returned this under a query that also matched P7 and P8, so I cannot tell if it is P4 or P7 text. It differs from the P4 abstract order (steering angle ahead of lane deviation).
- Definitions (snippets; wording matches my P3 note, so P4 likely reuses P3 text) [SNIP][SEC]:
  - Lane deviation: "difference between the car's lateral position and the centre of the lane", described as based on the steering angle data channel.
  - Trail braking application: "percentage of the distance between maximum brake and brake release divided by the length of braking zone".
  - Steering reversal rate: P3 says "number of times the driver crossed the centred position of the wheel" [SEC][9].
  - Throttle release application: "distance covered from throttle application to throttle release" [SEC][9].
  - Understeer / oversteer: qualitative only in P3 [SEC][9].
- Full list of P4 KPI definitions: **[NR]. Must be read from the PDF.** P8 explicitly defers to P4 for all definitions [7].

**6. Models, validation, metrics**
- "hybrid feature selection approach using two correlation analyses and three ML models"; "best model achieved a prediction accuracy of 97.19%". [ABS][1]
- Models (snippet): XGBoost, SVM, Random Forest (RandomForestClassifier) [SNIP][10]. References support this [3].
- Snippet metrics for XGBoost: AUC 0.971, accuracy 0.96, F1 0.93, absolute mean error 0.011 [SNIP, unverified]. These conflict with the 97.19% in the abstract unless they are for different datasets (lap vs segment) or models. **Do not cite these numbers.**
- Split, CV folds, RF and SVM numbers, hyperparameters: [NR]. In P8 the same group used 70/30 split plus 10-fold CV, with XGBoost accuracy 0.87 / F1 0.85 / AUC 0.90 / MAE 0.42 s on Laguna Seca segments [SEC][8]; not confirmed for P4.
- Reference list has Lundberg "unified approach to interpreting model predictions" (SHAP) and Rodriguez-Perez (Shapley values) [3], so P4 may use SHAP; not confirmed.

**7. Feature importance ranking**
- Abstract: "average speed is the most important metric, followed by lateral acceleration, steering angle, and lane deviation." [ABS][1] Method (XGBoost importance vs SHAP vs other), top-N table, scores: [NR]. Snippet top 5 above [SNIP].

**8. (P7 only)**

**9. Code / data release**
- Not stated in the abstract. Data/code availability statement: [NR]. No repository found for any of these papers (also in `/home/hyuse/Desktop/Thesis/notes/hojaji-2026-publications.md`).

**10. Limitations / future work (exact quotes)**
- No exact quote retrieved. Snippet paraphrase only: "MoTec providing no information regarding off-tracking" [SNIP]. [NR] for quotes.

### P7 — Hojaji, Toth, Joyce, Murphy, Campbell (2025), SSRN preprint (two records: 5255017 and 5263021)

Two SSRN records with the same title exist [4][5]. 5255017 lists 26 references and 5263021 lists 17 [4][5]; differences between the two versions' text are unknown.

**1. Simulator, car, circuit, rig, logger, rate, channels**
- Circuit: Laguna Seca, "expanding on prior research conducted on the Brands Hatch track". Simulator ACC v1.9. Event: Gamescom 2024, Cologne. [SNIP][6]
- From P8 (same data): McLaren 720S GT3, Playseat Sensation Pro, Logitech Pro wheelbase and pedals, 32-inch monitor, MoTeC i2 Pro, 50 Hz, 74 channels. [SEC][7][8] Inference: P7 uses the same dataset because participant and lap counts (135, 1180) match [6][7]. Confirm in P7.

**2. Participants, laps, cleaning**
- 135 participants, 1180 laps. [SNIP][6] Matches P8 Sec. 3.1 [7].
- From P8 (same data, probably same pipeline): 910 laps after removing zero-time, in-, out- and corrupt laps; 865 after |z| > 3; 17,279 segment entries. [SEC][8] P7's own counts: [NR].

**3. Labels**
- Pipeline includes "clustering" [SNIP][6]. k, sizes, balance: [NR]. P8 (same data): k-means, k = 3 (fast/medium/slow), mean lap times 86.4 / 91.2 / 96.8 s; sizes not reported [SEC][8].

**4. Granularity**
- Abstract-level text names no sector analysis [SNIP][6]. [NR].

**5. KPIs**
- Metrics named in the snippet: average speed, lateral acceleration, steering reversal rate, lane deviation [SNIP][6]. The definitions are P4's by citation (P4 is the first entry in the P7 reference list [4]). I could not read how P7 states them. [NR]

**6. Models and metrics**
- Reference list shows k-means (MacQueen), gradient boosting (Friedman), XGBoost (Chen), SVM (Cristianini), Random Forest (Breiman) [4]. No metric numbers retrieved. [NR]
- One snippet gave "XGBoost achieved the highest [performance]" with speed, trail-braking, steering angle, oversteer, lane deviation as top. This is P8's abstract wording, not P7's. Ignore it for P7. [7]

**7. Feature importance**
- [NR] for P7. For the same data, P8 Fig. 2 (read from chart in my earlier note): speed ~1.0, abs lateral accel ~0.96, steering reversal rate ~0.65, abs longitudinal accel ~0.5, steering duration ~0.42, lane deviation / abs steering angle / brake ~0.33, oversteer ~0.25, trail braking duration ~0.24 [SEC][8]. This is P8, not P7. The text of P8 lists a different top 5 [8]. Do not attribute to P7.

**8. Cross-track consistency**
- Claim: "Metrics such as average speed, lateral acceleration, steering reversal rate, and lane deviation showed high congruence with those from Brands Hatch." [SNIP][6] Whether the ranking changes, by how much, any rank correlation or per-KPI rank shift: **[NR]**. This is the single most important missing number for the thesis question.

**9. Code / data release**
- [NR]. Nothing found.

**10. Limitations / future work**
- [NR] (no quote). For comparison, P8 states: "The dataset is limited to one circuit and one car configuration, which may restrict generalizability" and that "retraining of the ML models and re-optimization of the EA would be required for each new circuit" [SEC][8].

### Cross-paper facts that are verified (from the local P8 PDF and notes)
- P8 uses the same Laguna Seca dataset described in the P7 abstract (135 participants, 1,180 laps) [6][7].
- P8 defers all KPI definitions to P4 [7].
- P4 and P7 are both authored by Hojaji, Toth, Joyce (+ Murphy on P7), Campbell [1][4].
- P4 is cited as the first reference in P7's reference list [4].

## Unresolved / follow-up
1. Obtain P4 PDF (CC-BY; open `https://doi.org/10.1016/j.chbr.2024.100414` in a normal browser) and ingest. Items 1-7, 9, 10 for P4 then become answerable.
2. Obtain P7 PDF from SSRN in a browser (either ID) and compare the two versions. Items 1-10 for P7 then become answerable.
3. Re-verify every [SNIP] line before use. Especially: 84 / 62 features, 15,694 rows, 19 segments (S1..S10, T1..T9), the XGBoost metrics (AUC 0.971 etc.), and the top-5 order.

## Sources
1. UL Pure, AI-enabled prediction of sim racing performance using telemetry data — https://pure.ul.ie/en/publications/ai-enabled-prediction-of-sim-racing-performance-using-telemetry-d/
2. DOAJ API record for 10.1016/j.chbr.2024.100414 — https://doaj.org/api/search/articles/doi:10.1016/j.chbr.2024.100414
3. Crossref, 10.1016/j.chbr.2024.100414 — https://api.crossref.org/works/10.1016/j.chbr.2024.100414
4. Crossref, 10.2139/ssrn.5255017 — https://api.crossref.org/works/10.2139/ssrn.5255017
5. Crossref, 10.2139/ssrn.5263021 — https://api.crossref.org/works/10.2139/ssrn.5263021
6. SSRN, Evaluating the Consistency of Key Performance Metrics... (page blocked; search-result text only) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5255017 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5263021
7. Hojaji, Toth, Campbell (2026), Optimizing Sim Racing Performance Using ML and EAs, ICAART — https://www.scitepress.org/Papers/2026/146096/146096.pdf (local: /home/hyuse/Desktop/Thesis/01_Corpus/ingested/2026/Hojaji2026_TelemetryEA.pdf)
8. Vault note — /home/hyuse/Desktop/Thesis/02_Source_Notes/Hojaji2026_TelemetryEA.md
9. Vault note, Hojaji et al. GALA 2023 — /home/hyuse/Desktop/Thesis/02_Source_Notes/Hojaji2024_DrivingBehaviour.md ; https://link.springer.com/chapter/10.1007/978-3-031-49065-1_19
10. ScienceDirect P4 page (blocked; search-result text only) — https://www.sciencedirect.com/science/article/pii/S2451958824000472
