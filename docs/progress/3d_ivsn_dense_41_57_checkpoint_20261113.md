# 2026-11-13 — Dense MEB41–57 SN-IV extraction checkpoint

**Status: 68/68 numerical extraction complete; physical retention PROVISIONAL.**

- Externally executed (not during Git synchronization): 17×4 independent 3D SN-current/VSN curves at 101 points per curve; MEB and T preprocessor mapping 68/68 verified.
- 68 10-fF assumed-C integral `t_est(1→0.8V)` values committed with node map, QC and eight SVG plots. No direct 0.8V crossing or long Floating Hold in new 68-case campaign.
- Independent original PLT replay/trapezoid mismatch max `4.98e-14`, quadrature crosscheck max `8.18e-06`; 12 older overlap conditions reproduce.
- 51 PASS + 17 numerical-floor KCL warnings all at 233K; precision/physics not closed. 41→57nm gains: `3.298×, 1.666×, 1.222×, 1.067×` at `233/300/340/380 K`.
- 42/44/46/50/52/56nm in prior future-IVSN plan now completed at all four temperatures; 38/40/58nm not covered. The 44–55nm prior filter overlap remains exploratory; new 1nm DC/Hurkx/Write/Read are not executed.
- User original `CMP_IVSN_41_57_EXPORT.zip` SHA256 `070ce72a011977647e24365f00b7266068531c8b833ea4ca13191e2f488253a1`; native PLT and per-V curve archive remain external (D-005), numerical integrals and maps committed.
- **NEXT:** priority 233K current KCL/Ceff/mesh/outer Drain contact QC, then missing matched dense DC/GIDL and selected direct Hold + Write/Read; old 4 failed Hold and 2 independent DC partial runs remain separately open.

[Detailed evidence](../evidence/3d_ivsn_dense_41_57_analysis_20261113.md) | [Data/graphs](../../data/3d_ivsn_meb41_57_20261113/README.md)
