# 2026-11-16 independent 3D IVSN full 36–60 nm × four-temperature archive

**Status: CMP-EXECUTED external, extracted numerical evidence complete; SCIENTIFIC-PROVISIONAL.** No new SDevice execution or model changes for this archival task.

## Source and QC

- Newly supplied external archive `CMP_IVSN_MISSING_6MEB_EXPORT_20261116_180122.zip`, SHA256 `e520735bd1ff85747a1d2c8d91a69e7b9b9fab9e69d59776fea29e453bc6121f`, covers 37/38/39/40/58/59nm × 233/300/340/380K from Nov-13 runs. The remaining 76 estimates are taken without value changes from the pre-existing Nov-11 and Nov-13 Git datasets.
- New 24/24 SWB tree, actual SDE PP/grid and SDevice PP temperature/model/circuit checks, exact complete target voltage grids (101 each), negative SN currents, positive voltage-source currents, done log/STA. 2424 new extracted samples. Normalizing temperatures and node IDs yields identical device decks among the 24.
- New 18 normal PASS and 6 low-current 233K warnings: maximum circuit SN KCL residual 4.9921e-18 A; relative 7.1965%. Simpson vs trapezoid maximum relative difference 8.0949e-6. Earlier 68-case QC labels retained; old 36/60nm curves checked again from Git source. Total 75 ordinary PASS / 25 233K warning. This is curve-level evidence, not mesh convergence or cold physical-model validation.
- [Long-format master](../../data/3d_ivsn_meb36_60_20261116/RETENTION_100_CASE_MASTER.csv), [25×4 SI matrix](../../data/3d_ivsn_meb36_60_20261116/RETENTION_MATRIX_SECONDS.csv), [new case QC](../../data/3d_ivsn_meb36_60_20261116/IVSN_24_new_case_QC.csv), [new curves](../../data/3d_ivsn_meb36_60_20261116/IVSN_24_new_curves.csv), [source and reproduction instructions](../../data/3d_ivsn_meb36_60_20261116/README.md).

## Results

Assumed constant Ccell=10fF and WL=-0.7 V, BL/body=0: t_est = integral from VSN=0.8 to 1.0 V of Ccell/(-I_SN). No direct 0.8 V hold crossing.

| T (K) | 36nm t_est | 60nm t_est | 36→60 gain | 55→60 gain |
|---:|---:|---:|---:|---:|
| 233 | 22.655 s | 97.038 s | 4.2833× | 15.24% |
| 300 | 67.161 ms | 233.837 ms | 3.4818× | 12.96% |
| 340 | 10.112 ms | 18.647 ms | 1.8440× | 5.24% |
| 380 | 1.660 ms | 2.028 ms | 1.2221× | 1.76% |

All 24 consecutive 1nm increases are monotonic at every temperature. Incremental gains are not uniformly diminishing at all depths; 233K interpretation requires numerical caution. [Six SVG plots](../../data/3d_ivsn_meb36_60_20261116/figures/). No Arrhenius activation energy is fitted.

## Boundaries / next action

Do not equate t_est with measured or production retention, refresh interval, isolated collected GIDL, or a final 44–55nm design range. Dense matched DC/Hurkx, representative cold precision, 3D mesh/current scale/Ceff, drain outer boundary, four prior failed Hold runs, two prior incomplete DC runs, and selected direct Hold/Write/Read remain open. Native PLT/PP/log ZIP held externally per D-005; no historical source or root README altered.
