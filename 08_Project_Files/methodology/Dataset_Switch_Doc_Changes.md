# Doc changes for the switch to the Hojaji 2024 dataset (2026-10-03)

Decision: the main dataset is Hojaji et al. (2024), Brands Hatch, 166 drivers, 826 laps. Your own Brands Hatch laps are an external test set only. Paste these into "Thesis TODOs" (refined methodology tab).

## Data Collection and Simulator Reliability
Replace the first paragraph with the "Data Collection" text in `Data_Collection_and_Reliability.md` (main dataset + external test set). Replace the rest of that heading with the short "Simulator Validity and Scope" recap from the same file (the long version now lives in the literature review tab).

In the recap, "McLaren 720S GT3 at Laguna Seca" becomes "McLaren 720S GT3 at Brands Hatch". Make the same change in the literature review tab's "Position of this thesis" paragraph.

## Step 0: Setup and Settings
Add one line at the top:
> These settings apply to the external test set. The main dataset (Hojaji et al., 2024) was recorded by its authors with one shared car setup and game setup.

Then:
- **Hardware:** replace the laptop/PXN text with: "Drivers use their own rigs. The minimum requirement is a steering wheel with pedals; each driver's hardware is recorded on the driver form (Appendix 1)."
- **Track:** "WeatherTech Raceway Laguna Seca" becomes "Brands Hatch".
- Keep the software, car, assists, conditions and session lines as they are.

## Step 1
- **Input:** "Segment-level telemetry of Hojaji et al. (2024), with each lap already divided into microsectors, plus the external test laps exported with the same MoTeC workspace and settings."
- **Microsectors:** "Slice each lap into M = 20 ordered microsectors (10 corners and 10 straights)…" becomes:
  > Each lap is divided into M = 19 ordered microsectors (9 corners and 10 straights, with the start/finish straight split into its start and end parts), following the segmentation of Hojaji et al. (2024), with boundaries fixed by track distance.
- **Outlier filter:** "…from the mean of that driver's laps (|z| > 3)" becomes "…from the mean of all laps (|z| > 3)". Drivers have only 1 to 8 laps each, so a per-driver mean isn't reliable.
- **Split:** "Valid laps are then split 70/30 into training and test sets, by driver where enough drivers are available and otherwise by lap (a limitation…)" becomes:
  > Valid laps of the main dataset are split 70/30 into training and test sets by driver, so no driver appears in both. The test set is used only for the final surrogate test. The external test laps are kept apart and never used for training, feature selection or tuning.
- **Control KPIs (candidate pool).** Replace the Output bullet's KPI list with:
  > Control KPIs are driver inputs only. The candidates are the eight KPIs computed in the dataset (brake length, brake duration, trail-braking duration, throttle duration, throttle application speed, throttle release, peak steering value and time to peak steering) plus summary statistics of the driver-input channels for each microsector: maximum and mean brake, maximum and mean throttle, share of the microsector at full throttle, maximum, mean and standard deviation of the absolute steering angle, steering reversal rate, and lowest gear. Channels that describe the car's response rather than the driver's input (speed, accelerations, lane deviation, understeer and oversteer, ABS and traction control activity) are excluded. Step 3 selects the top K = 10 from this pool.

  Why: the dataset's eight computed KPIs are fewer than K = 10, so the pool is widened with input channels the dataset already contains. This keeps K = 10 as in Hojaji et al. (2026), and Step 3 still has a real selection to make.

## Step 3
- No change needed: K = 10 stays, selected from the widened pool in Step 1.

## Step 4
- **Validation:** "grouped by the same unit as the original split (by driver or lap)" becomes "grouped by driver".
- Add at the end:
  > The surrogate is then evaluated once on the external test set (MAE, R² and lap rollout), to check how well it carries over to new drivers, a newer version of ACC and different hardware.

## Step 5
- "giving M × K genes (200 for M = 20)" becomes "giving M × K genes (190 for M = 19 and K = 10)". Adjust if K changes.

## Structural Limitations section
- The "20 track microsectors" sentence describes Hojaji's 2026 baseline at Laguna Seca, so it stays. Add after the ablation paragraph:
  > Because the comparison is between two fitness variants on the same data, it does not depend on using the same track as the baseline. This thesis uses Brands Hatch (Hojaji et al., 2024) rather than Laguna Seca (Hojaji et al., 2026).

## Appendix 1 (driver form)
- Q7: "McLaren 720S GT3 at Laguna Seca" becomes "McLaren 720S GT3 at Brands Hatch".

## Main tab
- Objective 1 ("To construct a micro-sector telemetry dataset by extracting and processing…") becomes:
  > To prepare a microsector telemetry dataset from existing sim racing telemetry (Hojaji et al., 2024), extended with an external test set recorded in the same simulator.
