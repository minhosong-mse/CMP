# 3D BCAT — 34-depth MEB × temperature checkpoint (2026-11-23)

**CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** Append-only extension of the [33-depth Nov-23 checkpoint](../3d_meb_jedec_33depth_20261123/README.md). The previously archived 33-depth, 21-depth, and older snapshots remain immutable.

Active lineage: `3D-Sun-SADDLE-V1 / Flat upper S/D`; 24–60 nm MEB at 1 nm steps, four temperatures (233.15, 300, 358.15, 368.15 K), five RunModes (0/1/5/6/7), 740 expected SDevice targets. The new external other-account archive adds **41 nm** from `CMP_final_Copy2`; 20/20 unique cases were mapped and independently checked to their native terminal bias and executed source/log. No Sentaurus simulations were run during analysis.

| Item | Verified |
|---|---:|
| MEB depths exported | **34/37** |
| Native mapped endpoints | **680/740** |
| Numerically endpoint-complete | **676/740** (676/680 exported) |
| Five-mode complete depth × temperature rows | **132/136** |
| Historic R1 recoveries maintained | **11/11** |
| New 41 nm nodes | **20/20 PASS** |
| Still unexported | **35, 47, 53 nm** (60 nodes) |
| Exported incomplete | **4** at 358.15 K: 27/M1, 40/M1, 46/M1, 58/M7 |
| Unvalidated campaign endpoints | **64/740** |

## Data

- [node_qc_680.csv](node_qc_680.csv): canonical 680-case endpoint audit, sorted and unique by (MEB, TempK, RunMode); retains the R1 recovery selections from the 33-depth checkpoint.
- [six_metrics_136_conditions.csv](six_metrics_136_conditions.csv): canonical six-metric table, 34 depths × 4 T; 132 five-mode complete rows.
- [selected_cases_267.csv](selected_cases_267.csv): 247 previously accepted Nov-23 new/recovery curves plus the 20 new 41 nm curves, project-qualified with original native PLT hash (not the entire 676-case historical source ledger).
- [depth_status.csv](depth_status.csv), [remaining_reruns.csv](remaining_reruns.csv): coverage and exact remaining numerical rerun list.
- [meb41_node_qc.csv](meb41_node_qc.csv) and [meb41_six_metrics.csv](meb41_six_metrics.csv): isolated 41 nm audit and four temperature metrics.
- [meb41_dc_curves.csv](meb41_dc_curves.csv) and [meb41_ivsn_curves.csv](meb41_ivsn_curves.csv): native-extracted endpoint-complete 41 nm curves, not cumulative copies.
- [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md): source SHA-256, copy deduplication, template comparison and provenance limits.
- [41 nm QC reproduction code](../../code/scripts/analysis/3d_meb_jedec_20261123/qc_meb41.py): reads native 41 nm ZIP and main-account 40 nm reference, as well as previous locally generated increment files; not a fully standalone GitHub-only reproducer.

Previously published 33-depth curve deltas and older immutable parent curves remain in their original folders. To recover **all cumulative curves**, assemble historical checkpoint curves and append Nov-23 33-depth deltas, then this new 41 nm delta, without duplicate case keys. Native solver ZIPs are retained externally per D-005.

## Scientific limitations

The 41 nm 233.15 K IVSN sweep has **4.01% maximum relative low-current KCL residual**; retain `LOW_CURRENT_KCL_WARNING`. Previous 33-depth data had 22 such warnings, so cumulative warnings among validated 233.15 K IVSN curves are **23**. The native terminal endpoint still passed.

`t_est_s` integrates an **assumed constant 10 fF** cell capacitance over 0.8–1.0 V; it is not measured physical retention. Signed Hurkx ON−OFF leakage is a proxy, not independently collected pure GIDL. SRH is omitted, exact binary mesh equivalence is not demonstrated, and no production optimum/JEDEC compliance has been claimed. Four R1 reruns are pending, not yet validated.
