# 2026-10-08 G0 source recovery and same-36-nm spatial bridge audit

> Status: INPUT RECOVERED / STATIC ASSOCIATION CHECKED / CROSS-MESH NUMERICAL EQUIVALENCE NOT DEMONSTRATED.
> Provenance: user-uploaded FZ-C Workbench source/CSV/logs and a pair of actual Sentaurus T-2022.03 TDRs. No new TCAD execution; FZ-C calibration/freeze remains unchanged.

## Inputs and reproducibility

- Executed FZ-C Workbench nominal GIDL meshes: Mesh0 n1→n4 (27,176 elements), Mesh1 n10→n11 (43,015), Mesh2 n13→n14 (53,509).
- FZ-C Mesh2 source TDR SHA256: c8e8513680e124f23496a2e191950f95f35a17a3c4df63554e15e8c79a96fb96.
- Atlas Level2 nominal GIDL n9 TDR SHA256: 6e70c44db66aae4b7cd98fe643d2492784ca40eb821d6597560122dcf2d2a888.
- Local read-only audit packages (not committed because they contain local-only datasets): CMP_G0_FZC_BRIDGE_REVIEW_20261008.zip SHA256 e11cd0a193e018be530ffc1450e2d5e110d6b0172391fa14ce92d77d03de7f3e; CMP_G0_36nm_SPATIAL_TDR_AUDIT_20261008.zip SHA256 f062a039675c01aeff93a7763fe5a5df7a9fc9a2282b5065b2b48ba3e37b2bfd.
- Workbench original FZ-C SDevice source byte-matched executed sdevice_des.cmd; nominal SDE geometry/doping/contact and SDevice physical settings, bias, solver were statically aligned with Atlas at 36 nm. The mesh refinement policies are different, not simply two resolutions of identical grids.

## Results at 36 nm, 300 K

| Quantity | FZ-C Mesh2 | Atlas L2 |
|---|---:|---:|
| Entire grid elements | 53,509 | about 15,279 |
| Silicon triangles in TDR | 42,607 | 11,079 |
| Silicon material area (um^2) | 0.140535805428 | 0.140535805428 |
| GIDL-bias total drain current (A/um) | 5.825589e-13 | 1.088559e-12 |
| Peak Band2BandGeneration (cm^-3 s^-1) | 7.263497e23 | 2.460872e23 |
| Whole-Silicon integrated BTBT (s^-1 um^-1) | 3.255346e6 | 1.151020e6 |
| E at own BTBT hotspot (V/cm) | 1.142258e6 | 1.040113e6 |
| Xhot (um) | 0.034863281 | 0.036328125 |
| Yhot (um) | 0.252174000 | 0.252890625 |

Relative Atlas change: terminal current +86.86%, integrated BTBT -64.64%, peak BTBT -66.12%, hotspot E -8.94%. The Atlas TDR whole-Si integral reproduces the committed 300 K Atlas master within 0.000432%. Geometry region areas match but are not sufficient to prove identical discretized solutions. On matched spatial coordinates the electrostatic potential differs by about 17–20 mV. Differences do not prove a unique microscopic mechanism or that mesh alone explains the terminal-current discrepancy.

Importantly, GIDL-bias terminal drain current is not pure BTBT current. Matched ON/OFF source data are available for Atlas, but not for frozen FZ-C; FZ-C OFF must not be inferred by subtracting integrated BTBT.

## Decision / claim boundary (2026-10-09)

The user explicitly elected to proceed from the completed physical paper calibration using the post-freeze Atlas L2 as a SEPARATELY LABELED working numerical branch. This does not equate Atlas L2 to frozen FZ-C Mesh2, does not re-freeze its physics, and does not reopen old calibration knobs. The old freeze is historical evidence, not a compulsory reference run at every temperature.

Remaining numerical-risk note: mesh-family discrepancy and complete Atlas L2↔L3 convergence over the full MEB/temperature domain are not resolved. Maintain conditional accuracy/retention claims. Continue downstream work with within-Atlas comparisons and targeted mesh review only if supported by anomalous data or stronger absolute-accuracy claims. Do not re-run the 300 K full Atlas or retune FZ-C by default.

Cross-references: docs/progress/b0_2d_paper_cal_mesh_revalidation_20261007.md; data/paper_cal/atlas_300k_20261008/processed/MEB_300K_ATLAS_MASTER_VALIDATED.csv.
