# Independent 3D BCAT 41–57 nm × 4-T SN I–V screen — 2026-11-13

**Evidence status:** 68 externally executed SN I–V cases and 68 integral Retention estimates, numerically QC-verified; **physical Retention, direct 0.8 V threshold and an effective design range NOT YET VERIFIED**. The active model remains `3D-Sun-SADDLE-V1 / Flat upper S/D` with Hurkx ON.

## Source and extraction

- Exact MEB `41..57 nm` step 1 × T `233/300/340/380 K`: 68/68 completed I–VSN sweeps, each with 101 sampled points `V_SN=0.8..1.0V` (6868 samples total). SDE preprocessor structure mapping and SDevice temperature checked for all 68.
- The source file is `IVSN_0P8_TO_1P0_n*_ivsn_sys.plt`, *not* `n*_ivsn_sys.plt`. Original user-provided source archive `CMP_IVSN_41_57_EXPORT.zip` SHA-256: `070ce72a011977647e24365f00b7266068531c8b833ea4ca13191e2f488253a1`; original analysis archive SHA-256: `7298101ad4a3daa14a732eae4b54a04f0b80cefdeacdc7bda4d42284f3ab8ca6`.
- All 68 native PLT data re-integrated vs stored CSV to max relative mismatch `4.98e-14`; Simpson vs trapezoid max relative difference `8.18e-06` (only quadrature accuracy). Historical `41/48/54 nm × 4 T` overlaps `12/12` with maximum relative deviation `4.44e-14`. Existing Nov-11 evidence remains frozen.
- `51` normal PASS, `17` low-current KCL numerical warnings **all at 233 K**; maximum absolute KCL residual `~4.93e-18 A`, relative mismatch up to `~9.76%`. Do not treat 233K absolute t_est as precisely validated.

## Results and claims

`t_est(1.0→0.8V) = ∫[0.8,1.0] C_assumed / (-I_SN(V)) dV`, with assumed `Ccell=1e-14F` (10fF) and `VWL_HOLD=-0.7 V`. The circuit's true `Ceff(V,T)`, 3D current scaling, mesh/Drain-face attribution and 233K physics are unverified.

| T | 41nm t_est | 57nm t_est | Gain 41→57 |
|---|---:|---:|---:|
| 233K | 27.106s | 89.386s | 3.298× |
| 300K | 130.476ms | 217.369ms | 1.666× |
| 340K | 14.807ms | 18.099ms | 1.222× |
| 380K | 1.881ms | 2.008ms | 1.067× |

All 16 one-nm intervals show monotonic increasing estimated Retention with MEB at each temperature. The model shows smaller incremental gains at high temperature. **This is not proof that model-internal GIDL alone causes the improvement**, or that these estimates equal directly reached VSN=0.8 crossing times.

The older tentative **44–55nm** multi-metric filter overlap used *five* 300K DC/Hurkx points `36/41/48/54/60`. This new 68-case experiment has **SN I–V only**: there is **no new dense 1nm DC/GIDL, Write/Read, full transient Hold or 3D Cgd**; no design-range freeze.

## Artifact boundary

The repository contains [exact 17×4 matrix](../../data/3d_ivsn_meb41_57_20261113/IVSN_RETENTION_MATRIX_seconds.csv), [68 case-node/QC mapping](../../data/3d_ivsn_meb41_57_20261113/IVSN_68_case_node_map_and_QC.csv), [full original analysis report](../../data/3d_ivsn_meb41_57_20261113/ANALYSIS_REPORT.md) and [8 new SVG graphs](../../data/3d_ivsn_meb41_57_20261113/figures). Original native PLT, `pp*_des.cmd`, `pp*_dvs.cmd`, the original PNG charts and **6868-row per-voltage `IVSN_CURVES.csv` are retained in the user-provided external archive, not committed to Git** (D-005). Full curve-source re-analysis must fetch that original archive, not reconstruct from t_est.

## Next gate

Validate 233K low-current numerical precision, representative 3D Ceff/current/mesh equivalence, outer-drain x≈60nm Face91; obtain matched 1nm DC/Hurkx at relevant new MEB to assess actual multi-metric overlap; test selected-depth true Floating Hold and Write/Read. The existing four failed 100ns Hold conditions and two Nov-09 partial DC conditions remain independent recovery cases. Previously proposed 300K SN-IV extra points `42/44/46/50/52/56` are now completed **across all four T**; `38/40/58` are not covered by this new dataset.

[Progress](../progress/3d_ivsn_dense_41_57_checkpoint_20261113.md) | [Source data](../../data/3d_ivsn_meb41_57_20261113/README.md)
