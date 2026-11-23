# 3D BCAT — 36-depth MEB × temperature DOE checkpoint (2026-11-23)

**CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** Append-only update to the [35-depth checkpoint](../3d_meb_jedec_35depth_20261123/README.md). Lineage: `3D-Sun-SADDLE-V1 / Flat upper S/D`, 24–60 nm × 4 T (233.15, 300, 358.15, 368.15 K) × modes 0, 1, 5, 6, 7; expected 740 cases.

| Item | Actual verified result |
|---|---:|
| MEB depths exported | **36/37** |
| Native unique mapped endpoints | **720/740** |
| Terminal endpoint/log/PP PASS | **712/720** (712/740 campaign) |
| Five-mode-complete MEB × temperature rows | **137/144** |
| Prior numerical R1 recovered cases | **11/11**, unchanged |
| Added MEB 53 | **17/20 PASS** |
| Still not exported | **35 nm only**, 20 jobs |
| Exported but not terminal-complete | **8** |
| Campaign endpoints not yet validated | **28/740** |

## New MEB 53: three failures (none replaced by another project copy)

| Temp K | Mode | Project | Node | Observed final bias | Required |
|---:|---:|---|---:|---|---|
| 358.15 | 1 | CMP_3D_Temp_49-60_Copy_Copy | 3182 | Vd 0.8886529545 V, Vg 0.0014228319 V | Vd 1.2 V, Vg 2.0 V |
| 358.15 | 5 | CMP_3D_Temp_49-60_Copy_Copy | 3183 | Vd 0.8796529545 V, Vg 0 V | Vd 1.2 V, Vg -0.7 V |
| 368.15 | 7 | CMP_3D_Temp_49-60_Copy_Copy | 3191 | VSN 0.806 V; 4 samples | VSN 1.0 V; 101 samples |

All three terminal logs report Newton nonconvergence and step size less than MinStep. Modes 1 and 5 are SWB Done but incomplete in native PLT; mode 7 is SWB Failed. No other copied project included completed curves for these specific targets. **Do not use partial traces to calculate final metrics.**

## Canonical files

- [node_qc_720.csv](node_qc_720.csv) — 720 unique MEB/T/mode provenance and endpoint-status records.
- [six_metrics_144_conditions.csv](six_metrics_144_conditions.csv) — cumulative six-metric master (137 full five-mode conditions).
- [selected_cases_303.csv](selected_cases_303.csv) — 286 previous accepted Nov-23 sources + 17 accepted MEB 53 sources; not the full historical 712-case PLT ledger.
- [remaining_reruns.csv](remaining_reruns.csv) — 8 specific numerical-recovery targets.
- [depth_status.csv](depth_status.csv) — exactly one unexported depth 35 nm.
- [meb53_node_qc.csv](meb53_node_qc.csv), [meb53_six_metrics.csv](meb53_six_metrics.csv), [meb53_selected_cases.csv](meb53_selected_cases.csv), [meb53_reruns.csv](meb53_reruns.csv) — isolated 53 nm evidence.
- [meb53_dc_curves.csv](meb53_dc_curves.csv) — 1,503 selected complete-DC points.
- [meb53_ivsn_curves.csv](meb53_ivsn_curves.csv) — 303 selected IVSN points, 3 curves × 101.
- [source manifest](SOURCE_MANIFEST.md) and [machine-readable candidate manifest](meb53_source_manifest.json).
- [native ZIP parser/QC code](../../code/scripts/analysis/3d_meb_jedec_20261123/qc_meb53.py) and [36-depth CSV consistency validator](../../code/scripts/analysis/3d_meb_jedec_20261123/validate_36depth.py).

Prior 35/34/33/21/18-depth archives and root README remain unchanged. Native SWB export ZIP remains external under D-005. Previous curves are not duplicated into this folder; for all curves append parent checkpoint sources plus new 53 nm deltas by (MEB,T,RunMode) key.

## Caveats

MEB 53 at 233.15 K has 5.74% maximum **relative low-current** IVSN KCL residual and is marked `LOW_CURRENT_KCL_WARNING`; cumulative cold warnings **25**. Numerically terminal-complete is **not** equivalent to physical model validation. Constant assumed 10 fF integrated `t_est_s` is not measured 1T1C retention. Hurkx ON−OFF current is a signed model-dependent leakage proxy, not independent pure GIDL. SRH omission, unproven native binary mesh equivalence, and production/JEDEC limitations remain. No final optimum has been established.
