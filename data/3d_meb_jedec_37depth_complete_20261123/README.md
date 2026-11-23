# CMP 3D BCAT — full 37-depth DOE data archive (2026-11-23)

**Numerical data-acquisition complete / CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** This is a **new append-only successor** to the historical [737/740 checkpoint](../3d_meb_jedec_37depth_20261123/README.md). Neither its original failures, earlier outputs, nor the root README were retroactively rewritten.

The active controlled lineage is `3D-Sun-SADDLE-V1 / Flat upper S/D`: MEB **24–60 nm (1 nm steps)**, temperature **233.15 / 300 / 358.15 / 368.15 K**, RunModes **0, 1, 5, 6, 7**. This yields **37 × 4 × 5 = 740** planned SDevice endpoints.

| Data-acquisition QC | Validated |
|---|---:|
| Source-mapped MEB depths | **37/37** |
| Terminal-complete SDevice cases | **740/740** |
| Five-mode-complete MEB × temperature rows | **148/148** |
| Historical original failures recovered using *numerical-only* R1 | **19 total** (11 + 5 + final 3) |
| Unresolved numerical endpoints | **0** |
| 233.15 K IVSN *low-current relative-KCL* warnings | **25** (retain warnings) |

**Last added data:** MAIN-account `CMP_eeeeeeee_53` MEB53 R1 reruns at (358.15 K, Mode1, n39), (358.15 K, Mode5, n40), (368.15 K, Mode7, n47) all passed original native log, preprocessed-source, SWB tree, target-bias and PLT checks. Mode7 contains exactly 101 samples from VSN 0.8 to 1.0 V. The 17 previously verified MEB53 cases are retained from the original `CMP_MAIN_MEB53_NOV23_20261123_192708.zip` rather than unrun placeholders in the last recovery export.

## Full-grid normalized outputs

- [node_qc_740.csv](node_qc_740.csv) — one unique accepted case per `(MEB_nm, Temp_K, RunMode)`, with account-specific ZIP/project/node/grid and R1 provenance; **all 740 PASS**.
- [six_metrics_148_conditions.csv](six_metrics_148_conditions.csv) — complete all-temperature MEB master with **Ion, Ioff, SS, DIBL, signed Hurkx ON−OFF leakage proxy and assumed 10 fF IVSN-integrated `t_est`**. All 148 rows have five accepted source modes.
- [selected_cases_331.csv](selected_cases_331.csv) — **Nov-23 incremental** 331-case selected PLT-hash ledger, of which 19 are numerical-only R1; not an independently exhaustive 740-case historical raw candidate ledger.
- [depth_status_37.csv](depth_status_37.csv) — 37 depths, 20 accepted endpoints each.
- [Final MEB53 isolated 3-node QC](meb53_r1_node_qc_3.csv), [selected source hashes](meb53_r1_selected_sources_3.csv), [native PP/log/PLT provenance](meb53_r1_native_provenance_3.csv), [metric patches](meb53_r1_metric_patches_2.csv), [ZIP source manifest](meb53_r1_source_manifest.json). Original failed endpoints are preserved in the [36-depth checkpoint](../3d_meb_jedec_36depth_20261123/README.md) and the [37-depth pre-recovery checkpoint](../3d_meb_jedec_37depth_20261123/README.md).

## Newly GitHub-archived raw curve deltas

The previous 37-depth checkpoint recorded some *source curves only in conversation QC packages*. They are now archived here as CSVs. Concatenate each DC family in numbered order, **discarding the repeated header after the first part**:

| Curve family | GitHub file names | Data rows |
|---|---|---:|
| New MEB35 + five previous R1, DC | `meb35_and_five_r1_dc_part01.csv` … `part05.csv` | **2,607** |
| New MEB35 + five previous R1, IVSN | `meb35_and_five_r1_ivsn.csv` | **505** |
| Original accepted MEB47, DC | `meb47_dc_part01.csv` … `part03.csv` | **1,618** |
| Original accepted MEB47, IVSN | `meb47_ivsn.csv` | **404** |
| Original accepted MEB53, DC | `meb53_original_dc_part01.csv` … `part03.csv` | **1,503** |
| Original accepted MEB53, IVSN | `meb53_original_ivsn.csv` | **303** |
| **Final** MEB53 three-R1, DC | `meb53_r1_dc_curves.csv` | **446** |
| **Final** MEB53 three-R1, IVSN | `meb53_r1_ivsn.csv` | **101** |

Total **6,174 selected incremental DC** + **1,313 selected incremental IVSN** rows added/preserved. **These are deltas, not the entire historical 740-case raw curve series.** Older curve sets remain in their immutable historical GitHub checkpoint folders; match by `(MEB,TempK,RunMode)` and project-qualified node identity. The final 53 nm recovered curve supersedes only the three original incomplete keys, *not* other 53 nm raw traces.

Source provenance: [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md). Native ZIPs including PLT/3D TDR/log/source/mesh remain **external per CMP D-005**, with source names and SHA256 recorded rather than pushed into GitHub.

## Reproduction and completeness check

- [Final MEB53 native-source parser](../../code/scripts/analysis/3d_meb_jedec_20261123/qc_meb53_final_r1.py) (external native ZIPs, NumPy)
- [MEB35 and five earlier R1 native-source parser](../../code/scripts/analysis/3d_meb_jedec_20261123/qc_meb35_five_r1.py)
- [Final GitHub CSV integrity audit](../../code/scripts/analysis/3d_meb_jedec_20261123/validate_37depth_complete.py), from repository root: `python3 code/scripts/analysis/3d_meb_jedec_20261123/validate_37depth_complete.py`.

**Meaning of completion:** all **planned numerical source endpoints and six-metric extraction inputs** have been acquired and internally audited. It is **not** a calibrated production DRAM / physical retention / JEDEC compliance result. `t_est` assumes fixed 10 fF, not measured 1T1C retention; signed Hurkx ON−OFF is **not independently isolated pure GIDL**. Omitted SRH, 25 low-current KCL warnings, and unproven bit-identical native 3D mesh equality remain. **Optimal MEB selection, relative design range, final physical interpretation and conclusions are explicitly deferred.**