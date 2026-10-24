# 2026-10-25 3D Vg=0.6 V, Vd=1.2 V 24/36/48 nm TDR analysis — evidence index

**Lineage:** `3D-Sun-SADDLE-V1 / Flat upper S/D`; CurveGrid1/Mesh A, WF4.8eV, 300K, Hurkx ON. Scientific interpretation: [session close-out](../../docs/progress/3d_vg06_channel_working_baseline_closeout_20261025.md).

## Immutable external source packages (user-supplied; NOT Git-hosted)

| Archive | SHA256 | Content and role |
|---|---|---|
| `CMP_3D_VG06_VD12_24_36_48_TDR.zip` | `91dade0a9d2c445d3e7398bc6929cd4f9db20cdd0efa3dbe689c80e52558b81c` | Three individual 3D HDF5 TDR binaries + each `run_des.cmd`, SDE executed source, console log, per-depth source manifest, SHA-256 manifest |
| `CMP_3D_VG06_VD12_SPATIAL_QC_20261024.zip` | `9f26d37e04d630fd3ee4d857469a5108e12d24f53589220ee543911217c03e83` | Original extended analysis report, full XYZ Silicon matched-point CSV (~905 KB), Y–Z crosssection summary, four PNG plots |

Native TDR SHA-256 verified against the source archive manifest (HDF5 readable):

| MEB nm | SDE→SDevice | Original TDR filename inside each MEB folder | Bytes | SHA-256 |
|---:|---|---|---:|---|
| 24 | 1→2 | `CMP_B0_IDVD_VG06_FINAL_des.tdr` | 5,612,287 | `47424fc64bd9d96536c0730719e97bc44666d25bc47ec4e464304b7a2da6718a` |
| 36 | 4→5 | `CMP_B0_IDVD_VG06_FINAL_des.tdr` | 5,553,223 | `3ddc6360c0efbbc5d7a7c0e2eed260167ccaaca31e542dabf8eb44184f1a3774` |
| 48 | 6→7 | `CMP_B0_IDVD_VG06_FINAL_des.tdr` | 5,509,526 | `46e85b7ec13ae372a6ac0dcc1d7f4a00bf354d319a06c0aed49e08382649546e` |

All three independent SDevice runs returned exit code 0 and a final TDR; DBCAT_nm, CurveGrid1, Grid path, Vg0.6/Vd1.2 targets, WF4.8, Hurkx ON and output existence were checked in per-depth source manifests. DO NOT infer MEB from the identical TDR basenames; the per-depth ZIP directories and source manifests are authoritative.

## Repo artifacts

- [CSV: Common 3D Silicon crosssection summaries](channel_crosssection_xyz_summary.csv): selected matched x-coordinates for each MEB, sampled y–z area, average electrostatic potential and sampled summed electron concentration. Full 51-row and per-point original tables are in the immutable external analysis ZIP.
- [SVG: section potential versus x](figures/01_channel_potential_vs_x.svg).
- [SVG: eDensity ratio 48/24 versus x](figures/02_channel_edensity_ratio_48_over_24.svg).
- Prior separate high-Vd Id–Vg 24/36/48 numeric [21-sample CSV](../3d_sun_meb_paper_interim_20261024/idvg_highvd_sample21.csv); earlier [five-sweep DC verification](../3d_sun_meb_paper_interim_20261024/README.md).

**Sampling:** Silicon `R.SiSubstrate`, common x stations, `y=−8…8 nm`, `z=−100…−75 nm` in 1nm steps; 442 valid points at x=−15nm. Tetra interpolation from native HDF5, **not** vertex index comparison; summed `eDensity` is a proxy, not a volume current integral.

**Caveats:** Retention/production calibration/global physical optimum not shown; potential-only barrier is approximate; Mesh A/B 36nm Id differs ≈5%; outer Drain domain/contact influence is unresolved for strong GIDL claims. No binary 3D TDR committed due to size (D-005).
