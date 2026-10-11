# Faithful-Q0 300 K × 15 MEB — source-based cross-control and surface-hotspot mesh sensitivity

**Status:** CMP-EXECUTED; extraction/source QC PASS; numerical/mesh convergence **PENDING**; physical GIDL/BTBT calibration **NOT DEMONSTRATED**. Date: 2026-10-11.

## Numerical files
- `ALL15_Q0_L2_vs_PAPER_CAL.csv`: paper-dimension-based Q0 before added surface mesh vs PAPER-CAL Atlas L2; 15 depths; 31 nm Q0 Cgd absent.
- `ALL15_Q0_L2_vs_SURFACE_L1.csv`: 15 depths original Q0 vs added near-surface hotspot local mesh, ON/OFF/spatial/mesh counts plus electron-current log diagnostics.
- `ALL15_PAPER_Q0_L2_Q0_SURFACE_L1_MASTER.csv`: 15-depth comparison across all three branches; selected source-derived metrics rounded to ~12 significant digits.
- `Q0_L2_INDEPENDENT_REVIEW_KR.md`, `Q0_SURFACE_L1_INDEPENDENT_REVIEW_KR.md`: audited status/limitations.
- `SDE_Q0_SURFACE_HOTSPOT_PHASE1.cmd`: standalone edited SDE used in surface-refinement branch (only SDE mesh changes). Does not include SDevice/Hurkx decks; do not confuse it with PAPER-CAL or a re-frozen baseline.
- `SDE_SURFACE_HOTSPOT_README.md`: executed-parent / mesh-only change notes.

## Source archive provenance (user-supplied raw, originally local)
- `CMP_FAITHFUL_Q0_ALL15_4PROJECTS_EVIDENCE.zip`: SHA256 `ee2d6f2bcbb74491aabd4e07b2300c283949db381fe3df621910ff0e026f662c`; 1,518 archive entries (1,513 source entries audit-hashed); 60/60 SDevice done; 15 ON /15 OFF /15 spatial /14 Cgd; 31-nm Cgd SVisual missing.
- `CMP_Q0_PHASE1_SPLIT6_15MEB_EVIDENCE.zip`: SHA256 `3d033071591f6a7a218877df5c866135d741e811069c696bcd5d8e2b12ef3880`; 1,201 entries (1,197 source entries audit-hashed); split 8+7 × (ON/OFF/spatial); 45/45 SDevice done, 15/15 per metric; select 31/36/41/48-nm TDR/PLT present.

**Public privacy guardrail:** original archives may contain the author's SWB absolute project paths and machine names. Do not upload them verbatim to this public repository. Where archive link is absent, only processed source-derived CSV and reports are GitHub-backed; original raw ZIP SHA verifies matching local/owner-held evidence.

## Controlled comparison
300 K; `VD=1.2 V, VG=-0.7 V` GIDL endpoint, `Band2Band(Hurkx)` ON, identical bias OFF comparator, MEB 31/33/36/39/41/42/43/44/45/46/47/48/49/50/51 nm.
- Faithful-Q0: GCS=1, GDB=0, modeled Tox 5 nm, recess 120 nm, Qf=0 assumption; Atlas mesh L2.
- Q0 Surface-L1: **same geometry/physics/calibration**; additional near-surface local mesh ROI (Outer X0–15 nm,Y258–276 nm; Core X0–8 nm,Y263–270 nm) and `SurfaceRefineLevel=1`.
- PAPER-CAL Atlas L2: GCS=2.3, GDB=25 nm, Qf=2.55e12 cm^-2, **different reduced-order model lineage**; paper benchmark DC calibration only.

## Central observations (not a final physical model verdict)
- Both 2D branches: total drain current falls with deeper MEB, but Q0 absolute terminal total current is much higher.
- Q0 surface mesh relative to original: 36-nm total drain current **+47.66%**, whole-Si BTBT integral **−17.68%**; 48-nm **+37.79%/−75.81%**, respectively. 31-nm Xhot switches 29.30→2.34 nm.
- PAPER-CAL: integrated BTBT peaks **39 nm**, BTBTmax peaks **41 nm**, Xhot tracks GateTop. Q0: integrated BTBT decreases with MEB, near-surface Xhot≈2.34 nm; Hurkx ON−OFF fraction remains extremely small after mesh change.
- Q0 surface-L1 drain **electron** ON−OFF component approximately tracks spatial `q∫BTBT` at reported logfile precision; **hole current dominates total drain**, but its microscopic OFF generation path remains unresolved.
- **NO** Q0 surface-L1 Cgd/DC sweep; earlier Q0 AC Cgd 14/15 only, 31 nm not measured in summary.
- Two mesh choices are **not** mesh convergence; sensitivity is demonstrated and further control is needed. Do not claim either branch physically “correct”, `48 nm optimum`, 3D equivalence, or retention translation.

## Links
PAPER-CAL separate comparator (not overwritten): `data/paper_cal/atlas_300k_20261008/processed/MEB_300K_ATLAS_MASTER_VALIDATED.csv`.

Next gate: verify 36/48-nm Q0 surface mesh Level1→Level2 and ON−OFF numerical precision as bounded reliability check, run three-knob GCS/GDB/Qf causal sensitivity at nominal MEB, **move selected-point 3D mechanism bridge before broad new retention/temperature simulation**. Preserve frozen PAPER-CAL as DC-fitted surrogate; retain Q0 as conditional paper-dimension control.
