# 3D BCAT — 33-depth MEB × temperature six-metric checkpoint (2026-11-23)

**PAUSED / SCIENTIFIC-PROVISIONAL.** This is a provenance-preserving successor to the immutable [21-depth checkpoint](../3d_meb_jedec_21depth_20261122/README.md) for `3D-Sun-SADDLE-V1 / Flat upper S/D`, with unchanged 4 temperatures (233.15/300/358.15/368.15 K) and five modes (0/1/5/6/7). No further Sentaurus simulation was executed inside GitHub.

| Progress | Verified |
|---|---:|
| MEB depths 24–60 nm with exported results | **33 / 37** |
| Mapped native SDevice endpoints | **660 / 740** |
| Numerically complete endpoints (target + source + log QC) | **656 / 740** |
| Numerically complete among mapped endpoints | **656 / 660** |
| Five-RunMode complete MEB × temperature rows | **128 / 132** |
| Former partial endpoints recovered using numerical R1 | **11 / 11** |
| New incomplete endpoints awaiting recovery | **4** |

**Still not exported:** `35, 41, 47, 53 nm` (80 jobs). **Still not numerically complete:** `27/358.15K/M1`, `40/358.15K/M1`, `46/358.15K/M1`, `58/358.15K/M7`. Exactly **84 / 740** endpoints are not yet validated.

## Canonical CSVs

| File | Data rows | Meaning |
|---|---:|---|
| [node_qc_660.csv](node_qc_660.csv) | 660 | Current canonical sorted node audit, with accepted R1 recovery source identified |
| [six_metrics_132_conditions.csv](six_metrics_132_conditions.csv) | 132 | Full merged temperature × MEB six-metric table (128 five-mode complete) |
| [node_qc_all_candidates.csv](node_qc_all_candidates.csv) | 262 | Nov-23 raw candidate audit including duplicated project copies and historical failures |
| [selected_cases.csv](selected_cases.csv) | 247 | Unique accepted Nov-23 new/recovery source cases, per-native-PLT hash |
| [six_metrics_delta_and_recovery.csv](six_metrics_delta_and_recovery.csv) | 57 | 48 new temperature rows + 9 recovery supplement rows, **not** the merged master |
| [dc_curves_delta_part01.csv](dc_curves_delta_part01.csv) / [02](dc_curves_delta_part02.csv) / [03](dc_curves_delta_part03.csv) | 22,168 combined | Only newly selected endpoint-complete DC curve points, including R1 recovered modes |
| [ivsn_curves_delta_and_recovery.csv](ivsn_curves_delta_and_recovery.csv) | 5,050 | Only new/recovery IVSN source points (50 × 101) |
| [depth_status.csv](depth_status.csv) | 37 | Current MEB-level coverage |
| [remaining_reruns.csv](remaining_reruns.csv) | 4 | Exact account/project/node and bias targets for pending R1 reruns |
| [meb54_node_qc.csv](meb54_node_qc.csv) | 20 | Specific final exported depth QC |

Read the [source manifest and merge rules](SOURCE_MANIFEST.md) before regenerating or using this master. Original 18-depth / 21-depth evidence and root README are untouched.

**Guardrails:** `t_est` uses a *fixed assumed* 10 fF capacitor and integrated I–VSN, not actual 1T1C retention; signed Hurkx-ON minus OFF is a model-dependent leakage proxy, not independently collected pure GIDL. Omitted SRH, unverified native mesh equality, and 233.15 K KCL warnings remain limitations. A production design window and physically calibrated optimum remain **NOT DEMONSTRATED**.
