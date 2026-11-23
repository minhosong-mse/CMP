# CMP 3D BCAT — 37-depth MEB × temperature DOE checkpoint (2026-11-23)

**PAUSED / CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** Append-only successor to the immutable [36-depth checkpoint](../3d_meb_jedec_36depth_20261123/README.md). Complete **MEB depth coverage**, but not yet complete SDevice endpoints: three 53 nm conditions require recovery.

Lineage: `3D-Sun-SADDLE-V1 / Flat upper S/D`, MEB 24–60 nm at 1 nm spacing, four temperatures (233.15, 300, 358.15, 368.15 K), five modes (0, 1, 5, 6, 7). No physical retuning of source SDE/mesh/WF/Hurkx, and no new Sentaurus solver work was carried out by the archive/QC analysis.

| Checkpoint indicator | Verified count |
|---|---:|
| Exported MEB depths | **37/37** |
| Mapped native target keys | **740/740** |
| Terminal/log/source PP PASS | **737/740** |
| Numerically incomplete endpoints | **3** (all at MEB53) |
| Complete five-mode MEB×T rows | **146/148** |
| MEB 35 newly acquired | **20/20 PASS** |
| Previously failed cases recovered by numerical R1 from this archive | **5/5 PASS** |
| Previous independently recovered R1 cases | **11/11** (retained without duplication) |
| Cold IVSN low-current relative-KCL warnings | **25** (unchanged) |

## Cumulative masters

- [node_qc_740.csv](node_qc_740.csv) — canonical 740 unique MEB/T/mode source identities, including five new R1 selections.
- [six_metrics_148_conditions.csv](six_metrics_148_conditions.csv) — canonical 148 depth×temperature six-metric table; only 146 rows have all five RunModes.
- [selected_cases_328.csv](selected_cases_328.csv) — incremental selected Nov-23 source ledger with node/project, R1 lineage and native PLT SHA256 (not the full historical 737-case source ledger).
- [depth_status_37.csv](depth_status_37.csv) — all 37 depths mapped, MEB53 17/20 currently complete.
- [remaining_reruns_3.csv](remaining_reruns_3.csv) — exact remaining 53 nm recovery targets.
- [accepted_node_qc_25.csv](accepted_node_qc_25.csv), [selected_sources_25.csv](selected_sources_25.csv) — accepted current-archive 35 nm + 5 numerical R1 cases only.
- [metrics_delta_9rows.csv](metrics_delta_9rows.csv) — four new MEB35 rows plus five partial recovery patches; **not** the complete 148-row table.
- [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md) — authoritative native ZIP SHA256, provenance, extraction/merge rules and physical-claim limits.

The current source ZIP also provides 2,607 new complete DC curve points and 505 IVSN points; these incremental curves and a runnable native-ZIP QC extractor were saved in the session's separate downloadable QC package rather than copied into this GitHub summary. Previous GitHub curve archives remain unchanged. Native SWB ZIPs remain external per D-005.

[37-depth scientific checkpoint](../../docs/progress/3d_meb_jedec_37depth_checkpoint_20261123.md) · [CSV integrity validator](../../code/scripts/analysis/3d_meb_jedec_20261123/validate_37depth.py)

## Three uncompleted conditions — **do not count as PASS**

| MEB | Temperature | Mode | Original failure |
|---:|---:|---:|---|
| 53 nm | 358.15 K | 1 | `CMP_3D_Temp_49-60_Copy_Copy / n3182` |
| 53 nm | 358.15 K | 5 | `CMP_3D_Temp_49-60_Copy_Copy / n3183` |
| 53 nm | 368.15 K | 7 | `CMP_3D_Temp_49-60_Copy_Copy / n3191` |

[53 nm isolated three-node R1 execution kit](../../docs/progress/3d_meb53_r1_selective_rerun_20261123.md) is **prepared only**; no verified recovery data yet. Original incomplete evidence is retained in the immutable 36-depth checkpoint.

## Scientific limits

`t_est_s` uses an **assumed constant 10 fF** IVSN charge-loss integral over 0.8–1.0 V, not direct physical 1T1C retention or JEDEC-compliant measurement. Signed Hurkx ON−OFF is a relative model-dependent leakage proxy, not independently isolated pure GIDL. Omitted SRH, 25 low-temperature relative KCL warnings, source/solver lineage uncertainty, and lack of demonstrated native 3D mesh equivalence remain. **No final optimum, production design range, or DOE freeze is claimed.** The root README and prior 36/35/34/33/21/18-depth checkpoints remain unmodified.
