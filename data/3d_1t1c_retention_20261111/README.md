# Independent 3D BCAT 1T1C SN I–V/100-ns Hold screening — 2026-11-11

**Lineage:** `3D-Sun-SADDLE-V1 / Flat upper S/D` (Hurkx ON working model). **Maturity:** `CMP-EXECUTED external / exported numerical QC / SCIENTIFIC-PROVISIONAL`; 1.0 → 0.8 V **integral estimate only**; no direct threshold crossing or calibrated physical DRAM retention.

## Scope and files

- SWB user-run `CMP_3D_Temp_Copy` (SN I–V) and `CMP_3D_Temp_Copy_Copy` (floating hold); MEB `36/41/48/54/60` nm × T `233/300/340/380` K = 20 conditions per branch.
- SN I–V: **20/20** valid `IVSN_0P8_TO_1P0_n*_ivsn_sys.plt` curves at 101 VSN points (0.800–1.000 V, 0.002 V increments). Negative cell SN currents in all 20.
- Direct Hold: **16/20** completed a **100 ns** floating interval; 4 failures `48/233 (n123: ~4.9 ns partial)`, `36/380 (n1968)`, `54/380 (n2238)`, `60/380 (n2328)`. **0/16** completed holds reached 0.8 V. The 3 hot cases fail before the transient steady-state initialization; the cold case fails after partial progress.
- Temporary circuit/metric assumptions: `Ccell_F=1e-14` (10 fF), `VWL_HOLD=-0.7 V`, common initial VSN=1.0 V, BL=body=0 V, `t_hold=1e-7 s`. Preserve original 3D device current scaling; do **not** silently reuse historical 2D `AreaFactor=0.017`.
- Actual data plots: `IVSN_0P8_TO_1P0_n*_ivsn_sys.plt` and `DIRECT_HOLD_n*_hold_sys.plt`; unprefixed `n*_ivsn_sys.plt` / `n*_hold_sys.plt` can be initialization-only and are **not** the scientific time/voltage curves.
- Original user-supplied archive `CMP_3D_1T1C_RESULTS_REVIEW.tar.gz` SHA256 `861104a9aa070b8ba1078d64c056b8f11cc76c8c6415b50e21cce885041dc371`. Unmodified native PLT/TDR/full execution logs/decks remain in user external storage under D-005; the repository stores generated, bounded numeric CSV and SVG visualizations.

## Tracked numerical evidence

| File | Description |
|---|---|
| `ivsn_all.csv` | 2020 exported voltage–current rows (20 cases × 101 points), full-precision model current and voltage-source current, **not** raw binary PLT |
| `case_metrics.csv` | Full 20-condition numeric QC; 100ns Hold status, node mappings, current sign, KCL, voltage loss and t_est |
| `retention_integrated_20matrix_seconds.csv` | 20 estimates in seconds, MEB rows × temperature columns |
| `direct_hold_100ns_loss_16matrix_uV.csv` | Completed 100ns voltage losses in microvolts; blanks for failed cases |
| `hold_status_20matrix.csv` | Direct Hold pass/fail flags |
| `CMP_300K_MEB_six_metrics.csv` | 300K DC/Hurkx from existing Nov-09 Git dataset joined to Nov-11 I–V integral and 100-ns Hold |
| `figures/*.svg` | Six separately labelled 300 K MEB comparison plots (new compact SVG renders, not source PNG byte-for-byte copies) |

## Calculation

Using the user-established project-internal comparator `VSN=1.0 → 0.8 V` and a constant **assumed** capacitor `10 fF`,

```text
t_est(1.0 -> 0.8 V) = integral[0.8, 1.0] Ccell / (-I_cell_SN(V)) dV
```

All `I_cell_SN` rows are negative in the defined discharge direction; trapezoidal numerical integration (see `code/scripts/analysis/3d_retention_20261111/`). 16/16 completed direct Holds show close early-time agreement with the SN I–V initial-slope prediction (maximum relative difference recorded in review: ~0.0766%), but this is *only a short-time consistency check*. The resulting milliseconds/seconds estimates have **not** been directly transient-validated for full 0.2 V loss, and neither Ceff nor mesh/drain-contact and low-T physics is fully validated.

## Critical interpretation boundaries

- `Hurkx_ON_minus_OFF_A` in the 300K source CSV is **Hurkx-dependent terminal excess** (negative-gate Vg=-0.7, Vd=1.2 V), not independently verified pure collected GIDL; it is a **different bias and terminal quantity** from floating SN discharge current.
- `t_est` is a specific assumed-`Ccell`, assumed-physics model estimate **not** a measured 1.0→0.8 V crossing time or real refresh interval.
- 54/60 nm mapping in external 1T1C archive follows SWB depth ordering (source SDE PP was not included); verify exact PP mesh and contact identity before promotion.
- Keep 2D Run 7, independent 3D temperature source campaign, and this 3D MixedMode branch separate.
- The old Nov-09 `HANDOFF` said 3D retention not executed: that is correct **as of Nov-09** but superseded by this **Nov-11 provisional** checkpoint; do not retroactively change Nov-09 evidence.
- Proposed design-range criteria **not frozen or validated for production**: see `docs/evidence/3d_meb_exploratory_range_20261111.md`.

## Read next

- [Evidence](../../docs/evidence/3d_1t1c_ivsn_hold_analysis_20261111.md)
- [Progress / recovery](../../docs/progress/3d_1t1c_retention_checkpoint_20261111.md)
- [Source DC and 140-temperature analysis](../3d_meb_temp140_partial_20261109/README.md)
- [Recalculation script](../../code/scripts/analysis/3d_retention_20261111/)
