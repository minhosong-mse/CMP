# CMP 3D — 신규 MEB 41–57 nm × 4 temperature IVSN 분석

> **Executed data:** 68 SN I–V sweeps. **Metric:** constant-C 10 fF integral estimate of VSN 1.0→0.8 V. **NOT** a directly simulated Hold threshold time.

## QC

- Model lineage: `3D-Sun-SADDLE-V1 / Flat upper S/D`, 3D Hurkx ON; source SDE preprocessed files confirm depth and SDevice files confirm temperature.
- 17 depths × 4 temperatures = 68/68 exact mapped unique cases, 101 points per curve, 6,868 voltage-current samples.
- All 68 `IVSN_0P8_TO_1P0_n*_ivsn_sys.plt` native source arrays and original SHA256 verified; independent raw re-integration matches extracted CSV to max relative error `4.98e-14`.
- Independent Simpson–trapezoid relative difference max `8.18e-06` (integration quadrature numeric stability only, not physical-model uncertainty).
- Prior original 41/48/54 nm × four temperatures overlap = 12/12 values identical within rounding; max relative discrepancy `4.44e-14`.
- Status: `PASS=51`, `PASS_LOW_CURRENT_KCL_WARNING=17` (all 233 K). At 233 K, absolute source/KCL residuals can reach `4.93e-18 A` with relative mismatch approaching `9.76%`; treat cold absolute retention precision as provisional.
- No 3D Ceff calibration, AreaFactor validation, mesh convergence or outer-drain contact/BTBT collection isolation; 100ns direct Hold does not establish the full 1.0→0.8V crossing time.

## Extracted retention matrix

| MEB (nm) | 233 K (s) | 300 K (ms) | 340 K (ms) | 380 K (ms) |
|---:|---:|---:|---:|---:|
| 41 | 27.106 | 130.476 | 14.807 | 1.881 |
| 42 | 28.328 | 141.044 | 15.177 | 1.893 |
| 43 | 30.088 | 150.800 | 15.484 | 1.903 |
| 44 | 32.587 | 158.137 | 15.712 | 1.912 |
| 45 | 35.460 | 163.828 | 15.901 | 1.919 |
| 46 | 39.787 | 168.975 | 16.093 | 1.927 |
| 47 | 44.775 | 173.091 | 16.262 | 1.934 |
| 48 | 50.747 | 177.004 | 16.435 | 1.941 |
| 49 | 57.187 | 180.898 | 16.612 | 1.949 |
| 50 | 63.218 | 184.659 | 16.783 | 1.956 |
| 51 | 69.035 | 188.861 | 16.971 | 1.964 |
| 52 | 73.754 | 193.065 | 17.154 | 1.971 |
| 53 | 77.822 | 197.439 | 17.338 | 1.978 |
| 54 | 81.337 | 202.245 | 17.533 | 1.986 |
| 55 | 84.203 | 207.011 | 17.719 | 1.993 |
| 56 | 86.763 | 211.870 | 17.901 | 2.000 |
| 57 | 89.386 | 217.369 | 18.099 | 2.008 |

## Quantitative trend, 41→57 nm

- 233 K: 27.106→89.386 s; +229.8% (3.298×).
- 300 K: 130.476→217.369 ms; +66.6% (1.666×).
- 340 K: 14.807→18.099 ms; +22.2% (1.222×).
- 380 K: 1.881→2.008 ms; +6.7% (1.067×).

- For every tested temperature, estimated retention increases monotonically at all 16 one-nm steps. Gains are **relative**, and the high-temperature (380 K) effect is markedly compressed.
- At 300 K, 41→48 nm: 35.7%, 48→54 nm: 14.3%, 54→57 nm: 7.5%. These spans differ in width, so they should not be compared as equal ΔMEB increments.
- Existing **36 and 60 nm** cases are included only as standalone historical reference markers. There is no newly executed 36→41 or 57→60 interpolation in the uploaded 68-case archive.
- The prior hypothetical 44–55 nm overlap (relative Ion/SS/DIBL/Hurkx/t_est filters) is still a screening hypothesis: this archive contains only new SN I–V, **not** newly executed 1 nm DC/GIDL/Write/Read guardrails.

## Suggested next gate

1. Preserve all 68 raw sources; identify actual new vs previously run 12 shared cases. No need to rerun completed SN I–V.
2. Cross-match 41–57 nm depth-specific 3D DC/Hurkx metrics from existing Git 24–48 nm data where the exact mesh/physics protocol matches; measure new 49–57 nm DC/GIDL only if necessary.
3. Check source device Ccell, real 3D current/mesh equivalence, selected-point mesh sensitivity and x≈60nm Outer Drain contact; specifically investigate 233K low-current KCL warning.
4. For a selected set around 44–55 nm, run longer direct Hold and Write/Read guardrails, retaining the distinction between 10 fF integral estimates and direct 0.8V crossing.

## Files

- `Retention_41_57_by_temperature_readable_units.csv` — convenient display units.
- `Retention_combined_36_41to57_60_seconds.csv` — exact union of old 36, 60 with new 41–57.
- `IVSN_CASE_QC.csv`, `IVSN_CURVES.csv`, `IVSN_RETENTION_MATRIX_seconds.csv` — untouched exported text.
- `QC_recomputed_from_native_68.csv` — independent native-PLT SHA, current and integral cross-check.
- `overlap_with_20261111_12conditions.csv` — overlap reproducibility.
- `01…05*.png` — temperature trend, dense 300K, relative-gain and individual-temperature figures.
