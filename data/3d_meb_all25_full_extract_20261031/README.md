# 3D BCAT MEB 24–48 nm — 175-case extracted-data checkpoint (2026-10-31)

**Status:** `CMP-EXECUTED / EXTRACTION-QC-PASSED / SCIENTIFIC-PROVISIONAL`. This package documents **25 depths × 7 RunModes = 175** previously executed simulations in the independent `3D-Sun-SADDLE-V1 / Flat upper S/D` *working* lineage. **Not paper-calibrated, fully mesh-converged, or production validated.**

## Simulation scope and native-data provenance

- MEB / DBCAT: **24–48 nm inclusive (1 nm increments)**, nominal 36 nm; 300 K, Lg 20 nm, Wfin 17 nm, Tox 5 nm, nominal recess 120 nm, nominal junction depth 48 nm, gate WF 4.8 eV, Mesh A/CurveGrid1, Hurkx ON except explicit Mode 6 OFF control.
- Modes: `0` Id–Vg Vd=0.05 V; `1` Id–Vg Vd=1.2 V; `2` Id–Vd Vg=0.1 V; `3` Id–Vd Vg=0.6 V; `4` Id–Vd Vg=1.2 V; `5` negative-Vg sweep to -0.7 V at Vd=1.2 V, Hurkx ON; `6` same negative-Vg sweep, Hurkx OFF.
- The original PP header labels the executed `CMP_3D_COMPETITION_DBCAT24_48` campaign as a **separate competition screening**; do not silently blend these absolute values with 2D/frozen core CMP data.
- Original external ZIP: `CMP_3D_ALL175_GITHUB_REVIEW_V5_RECOVERED.zip`, SHA256 `52ec688b89bf850591439c81b376216a096bc01b7a9038d4dfb1f8363b53f4d6`; original source project and TDR retained on Linux, **not** reproduced in Git.
- The upstream SWB and its 3D native TDR/PLT files were not rerun or modified during extraction. `LOGS/` in the original review ZIP contains **SVisual extraction logs**, not a complete archive of native SDevice solver logs.
- **D-005 data policy:** native TDR/PLT and full logs remain in the original external storage. `EXTERNAL_SOURCE_SHA256.csv` records original PP, extraction-log, and historical intermediate checksums without publishing full logs or private machine paths.

## Counts and files retained in this Git review

| Artifact | Count or definition |
|---|---|
| `DC/curves/` | 175 full SVisual-exported DC CSV sweeps (25×7), original CSV bytes preserved |
| `DC/metrics/` | 175 mode endpoints + 25 provisional device metric rows |
| `TERMINAL_DERIVED/` | 175 all-points KCL/derivative summaries + 700 contact endpoints + native CSV field inventory |
| `SPATIAL/cutlines/` | 700 `line_*.csv` cutlines + 175 saved field-inventory text files |
| `SPATIAL/SPATIAL_RAW_ALL.csv` | 4,900 V5-corrected ROI numeric records |
| `SPATIAL/SPATIAL_ROI_SUMMARY.csv` | 700 ROI summary rows, across four geometric regions per case |
| `SPATIAL/HURKX_SPATIAL_ON_OFF_DELTA.csv` | 100 ROI rows pairing 25 depths × four ROIs, Mode 5 vs Mode 6 |
| `SPATIAL/SPATIAL_CASE_QC_PUBLIC.csv` | 175 cases, exact TDR hash and byte size but absolute user/server paths removed |
| `MEB_25DEPTH_REVIEW_METRICS.csv`, `figures/` | Research-use derived depth trends; not new simulations |

**Important exclusions:** The 175 historical `SPATIAL/cutlines/.../raw_rows.csv` files are **V4 pre-recovery intermediates** and still carry the signed BTBT ×10^-12 mistake. They must NOT be treated as authoritative. The V5-corrected canonical sources are `SPATIAL/SPATIAL_RAW_ALL.csv` and `SPATIAL/SPATIAL_ROI_SUMMARY.csv`. The historical original files are kept intact in the external ZIP and indexed by SHA256. The Git review bundle also omits 175 complete SVisual logs and 175 executed PP decks (seven representative PP source examples retained under `code/scripts/analysis/3d_all25_extract_20261031/`).

## V5 extraction recovery and numerical QC

- Validated 175/175 SVisual cases, **28 raw numeric records/case**, 4 ROIs/case, 700/700 native signed integral crosschecks and 700/700 original exported Cutlines. Original archive member manifest: 1,592/1,592 hashes validated.
- At SVisual T-2022.03, native `Band2BandGeneration` signed integral already has units of **s^-1**; V4 mistakenly multiplied that output by `10^-12`. V5 recovery multiplied **only the historical signed CSV** by `10^12` before combining. The user-derived positive/negative fields retain their correct integration conversion (µm³→cm³ = 10^-12). Derived positive + negative identity residual maximum: `1.389e-25` A.
- Four-terminal KCL on the exported sweeps: maximum all-points relative residual `9.633e-08`. All 175 required sweep endpoints were reached. These are **file/mapping/numerical consistency checks**, not physical mesh-convergence proof.
- Each native 175-curve `.plt.csv` contains an SVisual human-readable **second header row**; skip it when importing numeric sweeps (e.g. pandas `skiprows=[1]`). Cutline `line_*.csv` likewise has an SVisual units/selection header row after the field labels.

## Interpretation and claim limits

- `qGpositive = q * ∫max(Band2BandGeneration,0) dV` is a **volume-generation-equivalent current**, **not collected drain GIDL current**. `Hurkx ON−OFF drain current` is a model-dependent terminal excess, not pure terminal-collected GIDL by itself.
- ROI definitions: Gate–Drain x=15–30 nm; Mid Drain x=30–45 nm; Outer Drain x=45–60 nm; Full Silicon independent. Subvolume attribution remains geometrical; it does not establish physical contact membership or current collection fraction.
- The large E-field near **outer drain x≈60 nm** may be contact/boundary sensitive and remains an active caveat; its membership and mesh sensitivity still require targeted control before stronger physical claims.
- Device metrics are **provisional extraction proxies** and do not establish numerical equivalence with Sun et al. (2022) Table 1 or the historical frozen B0-2D protocols. `Charge` in `.plt.csv` is a terminal quantity, **not a demonstrated Cgd**. No new temperature dependence or 1T1C retention analysis was executed.
- There are 5 unassigned historical/quick-look native source files in `DC/WARNINGS.txt`; they are not mapped to one of the 175 production cases, and none is used to fabricate a depth assignment.

## GitHub archive scope

This directory is the **approved repository copy of the corrected extraction evidence**. Original native TDR/PLT binaries, full SDevice/SVisual logs, and V4 erroneous per-case `raw_rows.csv` remain in external immutable archives under D-005. The 175-case extraction and numerical QC checkpoint does not imply full physical validation. Repository root README is intentionally unchanged. See `docs/progress/3d_all25_full_extract_20261031.md` for claim boundaries and `HANDOFF.md` for the next action.
