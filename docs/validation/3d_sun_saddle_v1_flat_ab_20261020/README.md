# Selected-point Flat-S/D 3D A/B numerical checkpoint — 2026-10-20

**PROVISIONAL physically; CMP-EXECUTED numerical result.** A=n41 SDE CurveGrid1 (SDevice n47), B=n46 CurveGrid2 (n48). At MEB36nm, T300K, Hurkx and common CAD, all 6 LOW/HIGHPOS/HIGHNEG sweeps completed, 24 spatial snapshots compared. See [full scientific progress and limitations](../../progress/3d_sun_saddle_v1_flat_sd_ab_20261020.md).

**Best-supported result:** LOWVD Vth spread 3.58mV, HIGHVD spread 2.33mV; HIGHNEG Vg=-1 positive BTBT generation-equivalent spread +0.025%, OFF drain terminal current ~9.14e-14A, and 0→-1V gatedrain-area generation fraction x15..30nm grows 22.48%→74.23% at Mesh A. A/B signed terminal/KCL and hotspot locations agree within tested conditions, but this is not a validated pure-GIDL attribution.

**Physical blockers:** peak field on finite Drain boundary x=+60nm, substrate-dominant OFF drain-to-body path, charged-carrier collection/mechanism unisolated, imperfect tetra at z≈-73nm and incomplete full 3D quantitative paper equivalence. OFF-current ≠ all-GIDL; temperature/retention not measured by these runs.

**Next FIRST:** audit drain outer contact/junction boundary using existing native output, then bounded Hurkx ON/OFF at Vd1.2V/Vg-1V/300K; conditional finite-domain sensitivity; then same-definition 36→48nm selected-point comparison. No MEB×T large sweep or absolute paper fitting.

[Data/evidence index](../../../data/3d_sun_flat_sd_ab_20261020/README.md) · [SDE seam and CurveGrid code](../../../code/sde/3d_sun_saddle_v1/flat_sd_mesh_20261020/) · [Historical separate rounded M1](../3d_sun_saddle_v1_20261017/README.md)
