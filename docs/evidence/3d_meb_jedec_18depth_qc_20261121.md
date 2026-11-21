# 2026-11-21 — 18-depth six-metric DOE checkpoint

The actual grid is 24–60 nm at 1 nm intervals, four exact temperatures (233.15/300/358.15/368.15 K), five independent modes (0/1/5/6/7). 740 target jobs; 18 depths exported, 351/360 jobs endpoint-complete, 389 outstanding against full grid. The prior Nov-16 five-temperature plan remains historical. 340 K was not part of these exports.

## Coverage

| Mode | PASS/72 | Incomplete |
|---|---:|---:|
| 0 | 72 | 0 |
| 1 | 66 | 6 |
| 5 | 71 | 1 |
| 6 | 72 | 0 |
| 7 | 70 | 2 |

65/72 rows contain all five modes; Ion/Ioff/SS/DIBL 66 each, Hurkx excess 71, retention estimate 70. 13 depths have all 20 modes/T combinations. The separate account's 28/29 nm cases are 40/40. Valid duplicate PLTs were checked for exact numerical equality before counting once. After normalizing only DBCAT depth, temperature, node identifiers, whitespace and comment lines, all selected PP SDE commands match one template and each SDevice mode matches one template across accounts. Native binary mesh equivalence and calibrated production physics are not demonstrated.

## Outstanding cases to recover selectively

| Depth (nm) | T (K) | Mode | Project | Node | Issue |
|---:|---:|---:|---|---:|---|
| 24 | 368.15 | 1 | CMP_3D_Temp_24-35 | 3084 | Vg=0.0078624 V vs 2 V |
| 36 | 368.15 | 1 | CMP_3D_Temp_36-48 | 3058 | Vg=0 V, target not reached |
| 44 | 233.15 | 1 | CMP_3D_Temp_36-48_Copy | 3248 | Vg=0.441769635 V vs 2 V |
| 44 | 368.15 | 1 | CMP_3D_Temp_36-48_Copy | 3266 | Vg=0 V, target not reached |
| 44 | 368.15 | 5 | CMP_3D_Temp_36-48_Copy | 3267 | Vg=0 V vs -0.7 V |
| 45 | 358.15 | 1 | CMP_3D_Temp_36-48_Copy | 3286 | Newton/MinStep termination; Vd≈0.963 V, Vg=0 V |
| 49 | 358.15 | 1 | CMP_3D_Temp_49-60 | 3078 | Vg=0.01520503 V vs 2 V |
| 49 | 358.15 | 7 | CMP_3D_Temp_49-60 | 3081 | Exact IVSN PLT absent/pending |
| 49 | 368.15 | 7 | CMP_3D_Temp_49-60 | 3087 | VSN=0.996 V vs 1 V |

19 depths not yet exported: 26, 27, 34, 35, 39, 40, 41, 42, 43, 46, 47, 48, 52, 53, 54, 57, 58, 59, 60 nm (380 jobs). Check SWB state first; export any already-complete jobs and selectively recover the nine incomplete/missing endpoints. No physical/model retune authorized by this checkpoint.

## Numerical observations (interim only)

At 300 K all 18 depths have all six metrics. Across the sampled 24→56 nm endpoints, Ion 3.6470→3.3153 µA, Ioff 23.3555→7.7609 fA, SS 78.8545→81.9773 mV/dec, DIBL 21.1690→27.3638 mV/V, Hurkx ON−OFF 89.7962→15.0809 fA, and constant-10fF IVSN estimate 34.0039→211.8701 ms. These are interval endpoints from a still-incomplete grid; no optimum or final P/NP range has been selected. At 300 K ten of 18 numerical retention estimates meet the 64 ms reference; all 17 available estimates at each high-temperature point (358.15 and 368.15 K) are below their respective 64/32 ms reference. 233.15 K has 18/18 numerical estimates meeting 64 ms, ten carrying low-current relative KCL warnings (>1%, maximum 14.84% at 55 nm).

Raw device current and assumed capacitance are model-internal; no physical retention, direct 0.8 V crossing, calibrated refresh reduction, pure GIDL or production optimum claim. Preserve separate prior 100-case IVSN history and old 2D results. Spatial TDR transport analysis is not performed here.

[Source data and definitions](../../data/3d_meb_jedec_18depth_20261121/README.md).
