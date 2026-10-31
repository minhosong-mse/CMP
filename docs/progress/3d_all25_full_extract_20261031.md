# 2026-10-31 — 3D MEB 24–48 nm all-25 extraction and numerical QC checkpoint (approved extraction checkpoint)

> **Current status: 175/175 extraction/QC pass.** The accompanying CSV/ROI and cutline evidence is tracked as a versioned 3D extraction checkpoint; this is not a paper-calibrated or mesh-converged baseline. The data package is `data/3d_meb_all25_full_extract_20261031/`.

## Scope / lineage

The independent 3D `3D-Sun-SADDLE-V1 / Flat upper S/D` *working* device was swept in a separate `CMP_3D_COMPETITION_DBCAT24_48` SWB source project. Its original PP header calls this a *competition screening separate from core CMP*; treat it as a distinct 3D execution campaign. Do not mix absolute values with the frozen historical 2D lineage, and do not call it a paper-calibrated model. Model nominal: Lg20nm, Wfin17nm, Tox5nm, recess120nm, junction48nm, WF4.8eV, CurveGrid1, T300K, Hurkx ON except deliberately OFF in Mode6.

## Completed independent evidence validation

- 25 MEB levels, 24–48 nm in 1nm steps; each has 7 modes (2 Id–Vg, 3 Id–Vd, negative-Vg Hurkx ON/OFF): **175 original sweep CSV**, 175 valid node mappings, 175 endpoints, 175 terminal summaries.
- 175 SVisual spatial cases contain **4,900 ROI scalar records**, **700** four-ROI summaries, **700** native signed integration cross-checks, **700** original line CSV Cutlines, **175** field inventories.
- Native archive member hashes: **1,592/1,592** SHA-256 matches; KCL maximum relative all-points discrepancy **9.6331416733e-8**. Recovered numeric positive+negative identity residual max **1.39e-25 A**.
- V4 `Band2BandGeneration` native signed integral was mistakenly multiplied by 1e-12 although SVisual had already output s^-1. V5 recovery corrected the signed aggregate only; original per-case V4 `raw_rows.csv` remains incorrect and is **not** canonical; keep historical original offline. V5 corrected aggregate CSVs are canonical for numeric interpretation.
- The 5 unassigned historical native artifacts in `DC/WARNINGS.txt` were not silently mapped to the 175-case sweep.

## Representative model-internal 24→48 trends at 300K

- Vg=-0.7V/Vd=1.2V: Hurkx ON total drain ~95.16→24.38 fA (**−74.38%**); ON−OFF terminal excess ~89.80→19.04 fA (**−78.80%**).
- Vg=1.2V/Vd=1.2V: ON drain ~3.647→3.533 µA (**−3.14%**).
- Mode5 gate-side geometric ROI Emax 1.593→0.865 MV/cm (**−45.69%**); gate ROI positive-BTBT equivalent ~68.32→1.31 fA (**−98.08%**).
- Outer drain Emax remains high: 3.828→3.714 MV/cm (**−2.99%**). Thus the x≈60nm contact/boundary concern is not cleared by data-extraction QC.

These quantities describe a **Hurkx-model-dependent** terminal excess and volume-generation-equivalent source, not proved collected GIDL, numerical mesh convergence, Cgd, temperature-dependent retention, or a 3D optimum.

## Source provenance and storage

The original extraction review archive and native TDR/PLT/full extraction logs remain **external** under the Git D-005 storage policy. The source archive SHA-256 is in the new data README; source PP and SVisual full-log hashes are indexed by `EXTERNAL_SOURCE_SHA256.csv`. The GitHub staging package includes all exported sweep CSV and all 700 valid cutlines, but excludes 175 V4 historical `raw_rows.csv` and full proprietary software logs.

## Next gate — do not silently skip

**First:** one bounded geometrical/contact membership check for outer drain x≈60nm, then a targeted GIDL mesh sensitivity and signed four-terminal/BTBT attribution at 24/36/48 nm under a matched 300K Vd1.2V, Vg≈−0.7V ON/OFF protocol. **Only after qualifying this mechanism**, proceed to 3D Cgd, temperature, and 1T1C retention. Retention has NOT been executed in this checkpoint.

The repository root README and previously frozen historical studies should not be rewritten solely to reflect this extraction.
