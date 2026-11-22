# Numerical recovery R1 — 2026-11-22

**PLANNED / STATIC-CHECKED / EXTERNAL EXECUTION RESULTS PENDING.** User requested a modified SDevice CMD and will supply rerun data when available. Do not claim convergence recovery before endpoint QC.

Source: [CMP_3D_JEDEC_RECOVERY_R1_des.cmd](../../code/sdevice/3d_sun_saddle_v1/CMP_3D_JEDEC_RECOVERY_R1_des.cmd), SHA-256 `c0ee12be0d25c6c399dab6ea5d20248e1cb34de3c4b8faa128bb4f2d314d6e44`. Closest executed PP parents: 60/358.15/M1 pp3364 and 48/368.15/M7 pp339; their actual T-2022.03 decks use 32 threads. Geometry/SDE/mesh policy, material and Hurkx physics, Digits, ErrRef, WF, bias, output prefixes, 101-point IVSN sampling, and Mode1 Ion TDR target are preserved. Mode 0 and 6 are unchanged relative to executed 32-thread parents.

| Numerical control | Original | R1 |
|---|---|---|
| Mode 1/5 ramp InitialStep | 1e-3 | 1e-4 |
| Mode 1/5 ramp Increment | 1.30 | 1.15 |
| Mode 1/5 MinStep/MaxStep | 1e-6 / 0.01 | 1e-9 / 0.005 |
| Mode 1/5 ramp Coupled Iterations | 40 | 80 |
| Mode 1/5 extrapolation cutoff | global on | Extrapolate(MinStep=1e-5) |
| Mode 1/5 ExitOnFailure | absent | enabled |
| Mode 7 PRE/IVSN InitialStep | 1e-4 / 1e-3 | 1e-4 / 2.5e-4 |
| Mode 7 ramp Increment | 1.2 | 1.1 |
| Mode 7 MinStep/MaxStep | 1e-10 / 0.01 | 1e-12 / 0.005 |
| Mode 7 Math Iterations | 50 | 80 |
| Mode 7 extrapolation cutoff | global on | Extrapolate(MinStep=1e-6) |

Manual: Synopsys Sentaurus Device User Guide T-2022.03, Ch. 4 Quasistationary Ramps (normalized stepping, small-step Extrapolate.MinStep), Ch. 6 nonlinear iterations and Math keyword reference (ExitOnFailure). Static branch expansion checked 5 modes × 4 temperatures, compared both exact executed PP parents and checked unchanged goals/physics/output. Native Workbench preprocess/solver was not executed in this session.

## Selective recovery list

| Account | Original project | MEB nm | Temp K | Mode | Original node |
|---|---|---:|---:|---:|---:|
| main | CMP_3D_Temp_24-35 | 24 | 368.15 | 1 | 3084 |
| main | CMP_3D_Temp_36-48 | 36 | 368.15 | 1 | 3058 |
| main | CMP_3D_Temp_36-48_Copy | 44 | 233.15 | 1 | 3248 |
| main | CMP_3D_Temp_36-48_Copy | 44 | 368.15 | 1 | 3266 |
| main | CMP_3D_Temp_36-48_Copy | 44 | 368.15 | 5 | 3267 |
| main | CMP_3D_Temp_36-48_Copy | 45 | 358.15 | 1 | 3286 |
| main | CMP_3D_Temp_49-60 | 49 | 358.15 | 1 | 3078 |
| main | CMP_3D_Temp_49-60 | 49 | 358.15 | 7 | 3081 |
| main | CMP_3D_Temp_49-60 | 49 | 368.15 | 7 | 3087 |
| main | CMP_3D_Temp_49-60_Copy_Copy | 60 | 358.15 | 1 | 3364 |
| other | CMP_final | 48 | 368.15 | 7 | 339 |

49/358.15/M7 n3081 was pending/absent, not a demonstrated convergence failure. Check current external SWB status first; do not rerun if target already completes. Use copied projects, same SDE/mesh, new R1 SDevice source, only selected targets. Copied project node IDs may differ; map by (MEB,T,mode) and identify project. Archive previous partial logs and do not replace existing valid jobs.

On return, capture exact native PLTs, status/log, PP source, tree mapping, mode1 Ion TDR and actual grid-level PP SDE. Check all endpoints, exact mode7 sweep/sign, finite data, physical and numerical lineage. Distinguish R1 recovery from original executed solver in provenance; compare overlap if necessary, do not silently promote recovered values or claim production retention. Checkpoint before recovery: [21-depth archive](../../data/3d_meb_jedec_21depth_20261122/README.md).
