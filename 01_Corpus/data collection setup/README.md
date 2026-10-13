# Hojaji et al. (2024) Brands Hatch data

The CSV files in this folder come from the supplementary material of:

Hojaji, F., Toth, A. J., Joyce, J. M., & Campbell, M. J. (2024). AI-enabled prediction of sim racing performance using telemetry data. *Computers in Human Behavior Reports*, 14, 100414. https://doi.org/10.1016/j.chbr.2024.100414

Licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Reused here with attribution.

- `segment level data behaviour.csv`: original segment-level file (166 drivers, 826 laps, 19 microsectors per lap).
- `segment_level_cleaned.csv`: our cleaned copy (165 drivers, 817 laps). Changes: "Str 0-1(End)" unified to "Str 0-1 (End)"; driver D_045 dropped (lap-time mismatches); Lap 1 standing starts of P_001, P_010, P_052, P_062 dropped.
- `time series data.csv`: time-series sample (one driver, 50 Hz MoTeC, 83 channels).
