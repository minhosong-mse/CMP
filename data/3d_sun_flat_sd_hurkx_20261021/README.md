# 3D Flat S/D — drain-boundary and Hurkx ON/OFF checkpoint (2026-10-21)

**CMP-EXECUTED numerical control, physical GIDL claim PROVISIONAL.** Parent: [2026-10-20 data](../3d_sun_flat_sd_ab_20261020/README.md); [close-out progress](../../docs/progress/3d_flat_sd_boundary_hurkx_20261021.md).

## Tracked lightweight derivations
- [boundary_mesh_ab_roi.csv](boundary_mesh_ab_roi.csv): A=n41/n47 and B=n46/n48 native TDR ROI *maxima* at HIGHNEG -1V.
- [boundary_z48_line.csv](boundary_z48_line.csv): fixed z=-48nm, y~6.5nm x cuts, sampled local doping/E/BTBT; this cut is not a full-device field integral.
- [hurkx_terminal_selected_bias.csv](hurkx_terminal_selected_bias.csv): native ON/OFF terminal TotalCurrent at four selected gate voltages (205-point matched raw PLTs external).
- [hurkx_spatial_roi_on_off.csv](hurkx_spatial_roi_on_off.csv): ON/OFF 3D ROI extrema, field and Band2BandGeneration, Mesh A only.
- [hurkx_cutline_on_off_qc.csv](hurkx_cutline_on_off_qc.csv): 12 cuts/843 matched samples; field and signed min/max BTBT, OFF all-zero sampled generation.
- [native_archive_sha256.csv](native_archive_sha256.csv): original uploaded/source ZIP hashes. Original multimegabyte TDR/PLT/log archives and analysis ZIPs are **not committed**.
- All CSVs are derived exports and/or selected records from native user-supplied input; **not synthetic simulation runs**. The reports and scripts in this checkpoint reproduce/describe these sources; raw native evidence remains archived outside GitHub.

## Conditions, status, limitations
3D-Sun-SADDLE-V1 Flat upper S/D; mesh A=n41/n47, independent B=n46/n48 for pre-ON/OFF boundary grid audit; T300K, DBCAT36nm, WF4.8eV, Vd1.2V, Vg=-1V; only `Recombination(Band2Band(Hurkx))` toggled ON/OFF on A. ON/OFF 205 matched gate-sweep points and 4-terminal KCL verified. Drain TotalCurrent ON=9.13930068118819e-14A, OFF=5.37371375833755e-15A, difference 8.601929305354435e-14A (~94.1202% ON reduction). Source negligible, substrate counters drain. Existing finite x=60nm peak |E| 3.85967MV/cm persists with Hurkx OFF; does not prove physical corner/contact independence.

`q∫max(G,0)dV` is **positive generation-equivalent current, NOT terminal GIDL**. Current 1D cuts and ROI peak exports are not signed 3D volume integrals; exact contact Face 91 polygon and hotspot membership not yet directly proven. 3D model remains PROVISIONAL; no MEB48/temperature/retention/optimum claims.
