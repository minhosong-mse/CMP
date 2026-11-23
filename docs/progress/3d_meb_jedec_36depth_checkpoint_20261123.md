# 2026-11-23 — 36-depth 3D BCAT MEB × 4T × 5-Mode checkpoint

**PAUSED / CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** This increments the verified [35-depth checkpoint](3d_meb_jedec_35depth_checkpoint_20261123.md) without modifying any parent data or changing the 3D geometry, physical models, Hurkx, grid-source or mesh policy. Source Sentaurus runs were performed externally by the user; analysis did not run new simulations.

## New external archive and provenance

- Main-account ZIP: `CMP_MAIN_MEB53_NOV23_20261123_192708.zip`; SHA-256 `691724181402bf429277cf6132f912263410375207c7d7f3c0667ea8dca17987`; ZIP integrity clean (310 entries).
- Unique new MEB53 targets: **20** across 4 temperatures × modes 0/1/5/6/7; **17 terminal/log/PP PASS**, **3 incomplete**. Selection spans original project `CMP_3D_Temp_49-60` (6 conditions) and `CMP_3D_Temp_49-60_Copy_Copy` (14).
- Original 53 nm `CANDIDATES.csv` covered other project copies, but none supplied a valid alternative for the three failed conditions.
- Per-grid executed SDE `pp3166_dvs.cmd`, source tree, device preprocessing, Hurkx mode branch, temperature, bias, finite native PLT, status and log were independently inspected. After node/depth normalization source SDE and mode-specific Device decks match the executed MEB54 parent; physical retuning **not** performed and bit-identical native binary meshes **not** demonstrated.
- 11 historical R1 recoveries embedded as candidate rows are **not re-counted**: previously accepted provenance remains unchanged.

## Corrected failure count for MEB53 (three, not one)

| Account | Original project | Depth nm | Temp K | RunMode | Node | Observed native last bias | Required |
|---|---|---:|---:|---:|---:|---|---|
| MAIN | CMP_3D_Temp_49-60_Copy_Copy | 53 | 358.15 | 1 | 3182 | VD 0.888652954462143 V, VG 0.001422831893572 V | VD 1.2 V, VG 2.0 V |
| MAIN | CMP_3D_Temp_49-60_Copy_Copy | 53 | 358.15 | 5 | 3183 | VD 0.879652954462143 V, VG 0 V | VD 1.2 V, VG -0.7 V |
| MAIN | CMP_3D_Temp_49-60_Copy_Copy | 53 | 368.15 | 7 | 3191 | VSN 0.806 V, 4 points | VSN 1.0 V, 101 points |

All logs reported `Newton didn't converge` and `Step-size less than MinStep`. Modes 1 and 5 had SWB `Done` despite failing terminal bias; mode 7 was `Failed`. Never accept log finish or SWB Done alone.

MEB53 233.15 K IVSN numerical relative-KCL residual = **5.7358%**: `LOW_CURRENT_KCL_WARNING` (cumulative cold warnings 25). This was an endpoint-complete run, but is still flagged for low-current numerical consistency.

## New cumulative count (36 depths)

- MEB depths exported: **36 / 37**; only **35 nm** not exported (20 target nodes).
- Unique mapped campaigns: **720/740**; true endpoint-complete: **712/720** (712/740).
- Valid modes complete at each depth×temperature: **137/144**. The other seven incomplete conditions are 27/358.15, 40/358.15, 46/358.15, 47/368.15, 53/358.15, 53/368.15, 58/358.15.
- Eight failed endpoints now require isolated numerical recovery: old five (27/358.15/M1, 40/358.15/M1, 46/358.15/M1, 47/368.15/M5, 58/358.15/M7) plus MEB53 three above.
- Campaign not-yet-validated: **28/740** = 20 unmapped MEB35 + 8 incomplete mapped cases.
- Current cumulative [node QC](../../data/3d_meb_jedec_36depth_20261123/node_qc_720.csv), [six-metric master](../../data/3d_meb_jedec_36depth_20261123/six_metrics_144_conditions.csv), [source/provenance manifest](../../data/3d_meb_jedec_36depth_20261123/SOURCE_MANIFEST.md), and [numerical rerun list](../../data/3d_meb_jedec_36depth_20261123/remaining_reruns.csv).
- Native source parser/QC: [qc_meb53.py](../../code/scripts/analysis/3d_meb_jedec_20261123/qc_meb53.py); CSV-only internal audit: [validate_36depth.py](../../code/scripts/analysis/3d_meb_jedec_20261123/validate_36depth.py).

## Scientific claim limits and next action

Ion, Ioff, SS and DIBL are extracted only from terminal-complete DC curves. Signed Hurkx ON−OFF is a leakage proxy and **not** measured pure GIDL. `t_est_s` integrates a hypothetical constant 10 fF Ccell, **not actual 1T1C retention** or a JEDEC-compliant measurement. SRH is omitted, low-current KCL caveats persist, binary native-mesh identity is unproven, and no production-design optimum has been established.

**Next:** receive MEB35 source ZIP (20 runs) and eight isolated numerical R1 recovery cases, preserve old failed traces, verify numerical endpoint/PP/log/101-point IVSN and update 37-depth/740 master. Do not rerun completed endpoints.
