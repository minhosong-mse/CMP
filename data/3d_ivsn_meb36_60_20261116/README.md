# CMP 3D BCAT IVSN — 36–60 nm × 4 temperatures (2026-11-16)

## Scope
Independent 3D-Sun-SADDLE-V1 / Flat upper S/D, Hurkx ON. 25 MEB depths at 1 nm increments × 233/300/340/380 K, 100 model-internal estimates. The 24 newly supplied PLTs correspond to runs completed Nov 13; 76 previous estimates are carried forward from GitHub main. Not a directly measured 1.0→0.8 V crossing time, validated cell Ceff, isolated GIDL, or production retention/refresh specification.

## Conditions and calculation
- SN=0.8–1.0 V, 101 samples at 0.002 V spacing, WL=-0.7 V, BL/body=0 V; Ccell assumed 10 fF.
- Integrate Ccell/(-I_SN) over increasing VSN via trapezoids; compare to Simpson quadrature.
- 24/24 verified against SWB tree, SDE PP MEB, actual grid reference, SDevice PP temperature/model/circuit and completion log. Device PP normalized for node IDs and temperature is identical among the 24 cases. This does not verify binary TDR equivalence with older runs.
- All 2424 newly supplied samples are finite, negative SN current and exact voltage sweep. 18 ordinary PASS; 6 low-current KCL warnings (all 233 K); maximum absolute residual 4.9921e-18 A, maximum relative 7.1965%; new warning threshold >1% relative. Simpson vs trapezoid maximum relative difference 8.0949e-6. Prior 68-case QC labels retained; 36/60 nm old curve KCL rechecked from Git raw CSV, warning at 233 K. Overall 75 ordinary PASS and 25 233 K warning, no omitted estimates. KCL is circuit SN residual I_cell_SN + I_vsn_SN.

## Results
All 24 adjacent MEB increments increase t_est at each T. 36→60 nm gain 4.2833x, 3.4818x, 1.8440x, 1.2221x at 233, 300, 340, 380 K respectively. Largest proportional 1-nm gains end at 48, 38, 38, 37 nm respectively; cold interpretation provisional. Incremental gains are not uniformly diminishing over every interval. 55→60 nm gains 15.24%, 12.96%, 5.24%, 1.76% respectively.

## Files
- RETENTION_100_CASE_MASTER.csv: long table with one row per depth/temperature, QC and source cohort.
- RETENTION_MATRIX_SECONDS.csv: 25×4, all seconds.
- RETENTION_MATRIX_READABLE.csv: 233 K seconds, other columns milliseconds.
- IVSN_24_new_case_QC.csv: new per-case node mapping, three current checkpoints and KCL/quad checks.
- IVSN_24_new_curves.csv: all 2424 source-derived voltage/current rows.
- RELATIVE_RETENTION_VS36.csv, INCREMENTAL_GAIN_PER_NM.csv: normalized and neighboring-depth changes.
- figures/: 6 plots in SVG and PNG. Arrhenius plot is diagnostic only, no activation-energy fit.
- QC_SUMMARY.json: computation summary, original ZIP hash and coverage.
- reproduction/: analysis script and prior Git CSV inputs (place the original user ZIP in reproduction/upload/ before running the script).

## Provenance
Source archive CMP_IVSN_MISSING_6MEB_EXPORT_20261116_180122.zip SHA256 e520735bd1ff85747a1d2c8d91a69e7b9b9fab9e69d59776fea29e453bc6121f; source ZIP remains external (D-005).
Previous Git inputs:
- https://github.com/minhosong-mse/CMP/blob/main/data/3d_ivsn_meb41_57_20261113/Retention_combined_36_41to57_60_seconds.csv (blob 464fab87eec9585c2fd1764d54086a4f57bbfeb6)
- https://github.com/minhosong-mse/CMP/blob/main/data/3d_ivsn_meb41_57_20261113/IVSN_68_case_node_map_and_QC.csv (blob 5e1d473f216be66d73d356952535b3231dc4b7b1)
- https://github.com/minhosong-mse/CMP/blob/main/data/3d_1t1c_retention_20261111/case_metrics.csv (blob d900a21e822d6d0e52ee27aa485036c797667b55)
- https://github.com/minhosong-mse/CMP/blob/main/data/3d_1t1c_retention_20261111/ivsn_all.csv (36/60 nm subset copied for rechecking endpoint QC)

## Next work
No new simulations were performed for this archive. Validate cold numerical floor and 3D current scaling, Ceff, mesh/contact geometry and selected direct Hold/Write/Read. Match dense DC/Hurkx to the relevant MEB set before final design-range selection. The prior 44–55 nm exploratory range is not frozen.
