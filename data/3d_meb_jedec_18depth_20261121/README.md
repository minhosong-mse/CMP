# 3D BCAT six-metric MEB × temperature archive — 2026-11-21

**CMP-EXECUTED / PROVISIONAL.** `3D-Sun-SADDLE-V1 / Flat upper S/D`, fixed geometry/mesh policy and Hurkx ON except mode 6. The actual campaign uses `DBCAT_nm=24..60`, `TempK=233.15/300/358.15/368.15`, `RunMode=0/1/5/6/7`. This differs from the Nov-16 planned 36–60 nm / five-T grid; do not mix historical 233/340/380 K data into this archive.

## Data index

| File | Rows (excluding header) | Contents |
|---|---:|---|
| [node_qc_360.csv](node_qc_360.csv) | 360 | One record per target (depth, T, mode); selected project, node, grid, endpoint and QC |
| [six_metrics_72_conditions.csv](six_metrics_72_conditions.csv) | 72 | 18 depths × four T; six metrics plus control currents, Vth, IVSN residual and screen |
| [dc_curves.csv](dc_curves.csv) | 30,354 | Target-Vd native drain current vs gate voltage for 281 endpoint-complete DC runs |
| [ivsn_curves.csv](ivsn_curves.csv) | 7,070 | 70 exact prefixed SN-current curves, 101 points each |

Original native PP, PLT, TDR and full logs are external per D-005. The extracted curves contain the actual gate sweep at the target drain bias, not the entire native drain-ramp trajectory. Partial/failed cases are identified in node QC; no synthetic replacement or extrapolation. The source/QC manifest is [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md).

## Extraction and claim boundaries

- Modes 0/1: Id–Vg at Vd=0.05/1.2 V, endpoint Vg=1.5/2.0 V, respectively. Ion at Vg=1.2 V/high Vd, Ioff at Vg=0/high Vd; log-current interpolation for Ion when bracket currents are positive; SS from voltage difference over 1e-10 to 1e-8 A; DIBL at the 8.5e-8 A constant-current threshold divided by 1.15 V (reported in mV/V). Currents are native device amperes, not normalized A/µm.
- Modes 5/6: Vd=1.2 V and Vg=-0.7 V, signed drain current Hurkx ON minus OFF. This model-specific difference is not established pure collected GIDL.
- Mode 7: signed SN current at VSN=0.8..1.0 V, WL=-0.7 V, BL/body=0 V; 101-point trapezoidal integral C/(-I_SN), assumed C=10 fF, omitted SRH. `Ieq_A=2e-15/t_est_s`; `retention_screen` uses 64 ms except 368.15 K (32 ms). Screen labels are numerical engineering references, not product/JEDEC compliance. Ten 233.15 K cases carry >1% relative KCL residual warnings (max 14.84%); retain caution, not unqualified pass.
- PASS in node QC means completed target endpoint, finite curve, done log/status and consistent PP DBCAT/T/Hurkx; mode 7 also verifies exact sweep and sign. Normalized executed PP SDE and SDevice content was checked separately across all 351 selected cases and agrees (one geometry template, one device template per mode, ignoring depth/T/node substitutions and comments). This is not a native mesh equality or full physical validation claim.
- [Extraction/QC script](../../code/scripts/analysis/3d_meb_jedec_20261121/qc_nov21.py) and [progress](../../docs/progress/3d_meb_jedec_18depth_checkpoint_20261121.md). See [evidence](../../docs/evidence/3d_meb_jedec_18depth_qc_20261121.md) for gaps and next action.
