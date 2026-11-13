# 3D BCAT 41–57 nm dense IVSN retention screen — 2026-11-13

**Scientific maturity: PROVISIONAL**. User-executed independent 3D-Sun-SADDLE-V1 / Flat upper S/D Hurkx ON simulation; 17 MEB depths (41..57nm in 1nm steps) × 233/300/340/380K = **68/68 SN I–V sweeps**, each 101 points over VSN 0.8–1.0V. **No direct VSN=0.8V hold threshold was simulated.**

### Repository files

- `Retention_41_57_by_temperature_readable_units.csv`: original 17×4 time estimates, 233K in s, rest in ms.
- `IVSN_RETENTION_MATRIX_seconds.csv`: 17×4 estimates converted to SI seconds.
- `IVSN_68_case_node_map_and_QC.csv`: 68-case independent MEB/temp/node map and preliminary PASS / low-current KCL-warning status.
- `Retention_combined_36_41to57_60_seconds.csv`: earlier 2026-11-11 36nm/60nm reference, plus dense 41..57nm results; not a new full-range execution.
- `Relative_retention_vs41.csv`: dimensionless 17×4 gain, separate temperature baselines.
- `QC_SUMMARY_INDEPENDENT.json`: source hashes and integration/overlap provenance.
- `ANALYSIS_REPORT.md`: detailed 2026-11-13 analysis text.
- `figures/`: newly regenerated SVG visualizations (not original PNG bytewise copies).

### Numerical evidence and source

User-uploaded original `CMP_IVSN_41_57_EXPORT.zip` SHA256 `070ce72a011977647e24365f00b7266068531c8b833ea4ca13191e2f488253a1`, full analyzed archive SHA256 `7298101ad4a3daa14a732eae4b54a04f0b80cefdeacdc7bda4d42284f3ab8ca6`. Native PLT/PP/SDE/source and original per-voltage `IVSN_CURVES.csv` remain in user's original external ZIP under D-005; **the 6868-point raw curve CSV is not committed here**. Git preserves all 68 estimated times, source node mapping and QC; original ZIP is necessary for exact curve-level reprocessing.

All 68 mappings verified against SDE PP and SDevice temperature; 68/68 integrals reproduced to max relative `4.98e-14`; Simpson vs trapezoid `8.18e-06`; 12/12 historical overlap with prior 41/48/54nm×4T reproduces to `4.44e-14`. 51 PASS, 17 **233K low-current KCL WARNING** with absolute residual up to `4.93e-18 A` (~9.76% relative) requiring cold numerical review.

Retention *estimate*: `t_est = integral_0.8^1.0 C_assumed / (-I_SN(V)) dV` with constant **10fF**. This is not direct 1.0→0.8V transient crossing, a calibrated production-cell retention, refresh, or isolated pure GIDL metric. 3D Ceff/current scaling, 233K physics, mesh and outer-drain x≈60nm contact/BTBT attribution remain open.

41→57nm gain: 233K **3.298×**, 300K **1.666×**, 340K **1.222×**, 380K **1.067×**. All 16 intermediate 1nm intervals show increasing `t_est` for every temperature in this screening model. Previous hypothetical 44–55nm DC/Hurkx overlap is **not validated by this IVSN-only dataset**. 1nm DC/GIDL and Write/Read not executed.

See [analysis](../../docs/evidence/3d_ivsn_dense_41_57_analysis_20261113.md) and [progress](../../docs/progress/3d_ivsn_dense_41_57_checkpoint_20261113.md).
