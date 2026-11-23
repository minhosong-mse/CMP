# 3D BCAT 35-depth MEB × temperature checkpoint — 2026-11-23

**CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** Additive successor to the [34-depth immutable archive](../3d_meb_jedec_34depth_20261123/README.md). Active lineage: `3D-Sun-SADDLE-V1 / Flat upper S/D`, 24–60 nm × 4 temperatures (233.15, 300, 358.15, 368.15 K) × RunModes (0,1,5,6,7), 740 planned endpoints.

| Coverage | Verified |
|---|---:|
| Exported MEB depths | **35/37** |
| Mapped target conditions | **700/740** |
| Numerically completed endpoints | **695/700** (**695/740** planned) |
| Complete five-mode depth×temperature rows | **135/140** |
| Previously recovered R1 conditions | **11/11**, unchanged |
| New 47 nm endpoints | **19/20** |
| Unexported MEB | **35, 53 nm** = 40 conditions |
| Incomplete exported endpoints | **5** |
| Remaining unvalidated endpoints | **45/740** |

47 nm runs were spread across **three** main-account SWB projects; each accepted row is project-qualified and source-tree/actual PP matched. The high-temperature `368.15 K / Mode 6 / n3346` was selected from `CMP_3D_Temp_36-48_Copy1_Copy`; `368.15 K / Mode 7 / n3347` was selected from `CMP_3D_Temp_36-48_Copy` and has exactly 101 samples from 0.8–1.0 V. The remaining 18 jobs were present in `CMP_3D_Temp_36-48_Copy1`, including one **incomplete** case.

**Important new failure:** 47 nm / 368.15 K / RunMode 5, main `CMP_3D_Temp_36-48_Copy1` node `3345`: the SWB status says Done and Sentaurus prints Good Bye, but log reports Newton nonconvergence and step size below MinStep; final PLT has `VG=0.0 V`, `VD=1.189584347 V` rather than `VG=-0.7 V`, `VD=1.2 V`. Not counted as endpoint complete. No alternate completed candidate found in the user ZIP. For that temperature, signed Hurkx ON−OFF metric is intentionally **blank**, while valid Ion/Ioff/SS/DIBL and IVSN estimate remain retained.

## Files

- [node_qc_700.csv](node_qc_700.csv): cumulative unique MEB/T/mode mapping, with five incomplete endpoints maintained as RERUN.
- [six_metrics_140_conditions.csv](six_metrics_140_conditions.csv): cumulative scientific-provisional performance table, with 135 complete five-mode rows.
- [meb47_node_qc.csv](meb47_node_qc.csv): isolated selected 47 nm QC and source project mapping; [meb47_six_metrics.csv](meb47_six_metrics.csv): four-temperature metric delta.
- [selected_cases_286.csv](selected_cases_286.csv): 267 earlier accepted Nov-23 sources plus **19** accepted 47 nm cases, with original PLT SHA-256; the old 34-depth selected file remains unchanged.
- [depth_status.csv](depth_status.csv): 37-depth coverage, and [remaining_reruns.csv](remaining_reruns.csv): five failed endpoint conditions.
- [source manifest](SOURCE_MANIFEST.md): raw ZIP SHA-256, project split and reproducibility limits.
- [47 nm extraction script](../../code/scripts/analysis/3d_meb_jedec_20261123/qc_meb47.py): native SWB source and metric extraction, using external ZIPs and earlier local QC deltas; NumPy required.

The original 47 nm `MEB47_DC_curves.csv` (1,618 selected DC points) and `MEB47_IVSN_curves.csv` (4 × 101 points) are preserved in the conversation's downloadable QC package, with the native ZIP remaining external per D-005. They are **not** asserted to be GitHub-hosted CSVs in this checkpoint. All earlier 34/33/21/18-depth GitHub archives remain untouched.

The 233.15 K 47 nm IVSN has **3.27% maximum relative low-current KCL residual**, so this depth adds one warning (cumulative **24**, not a numerical-endpoint failure). Native binary mesh equality has not been established.

**Claim limits:** constant assumed 10 fF charge-loss integration (`t_est_s`) is not measured DRAM retention. Signed Hurkx ON−OFF current is a model-dependent proxy, not pure GIDL; omitted SRH, low-current KCL warnings, numerical mesh uncertainty and production/JEDEC limits remain open. No final optimum/freeze claim.
