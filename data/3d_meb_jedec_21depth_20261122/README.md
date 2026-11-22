# 3D BCAT six-metric DOE — 21-depth checkpoint, 2026-11-22

**CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** Same `3D-Sun-SADDLE-V1 / Flat upper S/D` lineage and four-temperature, five-mode campaign as the [immutable Nov-21 18-depth archive](../3d_meb_jedec_18depth_20261121/README.md). This increment adds 48, 59, 60 nm only. The full 24–60 nm sweep remains incomplete.

| File | Rows | Scope |
|---|---:|---|
| [node_qc_60_new.csv](node_qc_60_new.csv) | 60 | New three-depth target audit |
| [six_metrics_12_new.csv](six_metrics_12_new.csv) | 12 | Three depths × four T |
| [dc_curves_new.csv](dc_curves_new.csv) | 5,117 | 47 complete DC curves, target drain bias |
| [ivsn_curves_new.csv](ivsn_curves_new.csv) | 1,111 | 11 exact 101-point IVSN curves |
| [node_qc_420.csv](node_qc_420.csv) | 420 | Sorted cumulative 21-depth QC, 409 PASS / 11 RERUN |
| [six_metrics_84_conditions.csv](six_metrics_84_conditions.csv) | 84 | Sorted cumulative master, 75 complete five-mode rows |

For cumulative extracted curves, concatenate the parent archive's `dc_curves.csv` / `ivsn_curves.csv` with the respective new delta; the sets of depth keys are disjoint. Historical curve files are not copied or rewritten.

All 58 selected new PP SDevice decks match the previous template per mode, and the three supplemental executed PP SDE decks match the previous SDE after normalizing only depth, temperature, node/output identifiers and comments as appropriate. Native mesh equality is not established. Two incomplete endpoints are retained as QC records with missing metrics, never treated as valid curves.

See [source manifest](SOURCE_MANIFEST.md), [extraction script](../../code/scripts/analysis/3d_meb_jedec_20261122/qc_nov22.py) and [checkpoint](../../docs/progress/3d_meb_jedec_21depth_checkpoint_20261122.md). Reproduce using NumPy and the external ZIPs (including the original Nov-19/21 sources for template comparison): `python code/scripts/analysis/3d_meb_jedec_20261122/qc_nov22.py --archive-dir /path/to/exports`.

All extraction definitions and scientific claim boundaries in the parent README remain unchanged, including constant assumed 10 fF, omitted SRH, signed Hurkx proxy, and engineering refresh-reference screening only. No fabricated-device or production retention claim.
