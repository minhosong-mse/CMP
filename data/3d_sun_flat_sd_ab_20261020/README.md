# Flat upper S/D 3D BCAT — 2026-10-20 SDE seam/CurveGrid + SDevice A/B provenance

**Actual status: CMP-EXECUTED selected-point DC/space A/B, interpretation PROVISIONAL.** New lineage continuation of 3D-Sun-SADDLE-V1 Flat S/D; does not replace 2D PAPER-CAL, older 3D-Sun-B0, or Rounded M1.

- [Full checkpoint, interpretation and ordered next actions](../../docs/progress/3d_sun_saddle_v1_flat_sd_ab_20261020.md)
- [`mesh/`](mesh/README.md): source-backed 7 MeshCases, 2 LocalCases, 4 CadSeamCases and final CurveGrid 1/2 quality and coordinates.
- [`device/`](device/CORE_RUN_QC.csv): original parsed PLT series for **six runs** (60+60 LOW,107+107 HIGHPOS,205+205 HIGHNEG original transfer samples), voltage-endpoint QC and 4-electrode KCL. `*_AB_INTERPOLATED.csv` are derived/resampled and **must not be called raw**.
- [`spatial/AB_MATCHED_BIAS_COMPARISON.csv`](spatial/AB_MATCHED_BIAS_COMPARISON.csv): 12 matched sweep-Vg conditions / 24 TDR snapshots, numerical A/B field, BTBT, ROI, centroid and peak-location comparisons.
- [`spatial/FULL_SPATIAL_METRICS.csv`](spatial/FULL_SPATIAL_METRICS.csv): source-resolved individual snapshots; `FULL_SPATIAL_BINS`, `FULL_REGION_BTBT`, `BTBT_SIGNED_GENERATION_AUDIT`, `BTBT_INTEGRAL_SPATIAL_ROI`, `HOTSPOT_LOCALIZATION_ROI`, `BTBT_SPATIAL_BINS` preserve spatial and signed definitions.
- [`figures/`](figures/): data-derived (not conceptual) SVG plots of HIGHNEG BTBT A/B vs negative gate and the normalized Gate–Drain-region source shift.
- [Source 2026-10-20 SDE/CAD/CurveGrid CMD](../../code/sde/3d_sun_saddle_v1/flat_sd_mesh_20261020/SDE_FLAT_SD_CADSEAM3_GATE_CURVEGRID_0to2_SWB.cmd); existing original D0/D1/D2 SDevice decks under `code/sdevice/3d_sun_saddle_v1/`; **executed** n47/n48 PP-CMD/Grid links must be used for replay.

## Exact source ZIP hashes (native user data, stored OUTSIDE GitHub)

| User evidence source file | SHA256 |
|---|---|
| `CMP_B0_3D_mesh_sdflat_MeshCase_0to6.zip` | `36d5443b8868d1dbbb21cee1079727405f38b0aa4b1056696dae456b87cf9ba1` |
| `CMP_3D_AB_DC_CORE.zip` | `31969567945a5dff6a927e7769bffa6a8351bcd9c454c938ef2f6a8ad2481b3a` |
| `CMP_3D_AB_SPATIAL_HIGHNEG.zip` | `519cddf0952e53db8bf754106ff0d731f4751750c1cda4eca48d50dbf87db2f9` |
| `CMP_3D_AB_SPATIAL_HIGHPOS(1).zip` | `b64784e61605dd58075750cf9f8577e05b49d6cd1adde88c3a8d0444ea1d2b0a` |
| `CMP_3D_AB_SPATIAL_LOW.zip` | `00e97896950ac66be5e69b3ca140775de4d31be92198030e550715761ad8ec50` |

Meshes A/B are CurveGrid1 n41→SDevice n47 and CurveGrid2 n46→SDevice n48 **within each SWB project**, all 300K/Hurkx/36nm nominal. Files `.tdr`, `.plt`, `.log` and PP-CMD in the archive are the primary evidence; committed CSVs and summary charts are extracted derivatives, not replacements.

**Physical scope warning:** Global |E| maximum x≈+60nm near drain outer domain; HIGHNEG gate-correlated BTBT x15..30nm is not yet proven to be *entire* drain GIDL. q∫max(G,0)dV is generation-equivalent, not terminal; signed negative term at some positive Vg is non-negligible. Remaining <1° tetra and <0.1nm edges forbid categorical full mesh convergence. No 3D temperature or retention result in this checkpoint.
