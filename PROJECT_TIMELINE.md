# CMP Project Timeline

> Purpose: preserve the major research transitions required to reconstruct why the CMP project reached its current state.
>
> This is **not** a session log. Routine reruns, solver retries, CSV additions, screenshots, and formatting changes do not belong here.
>
> Detailed numerical evidence remains in `data/`, `docs/evidence/`, and `docs/progress/`.

## Status Key

- **Completed** — executed / decided and closed within the stated scope
- **In Progress** — active research stage
- **Planned** — intended but not executed
- **Conditional** — activated only if evidence requires it
- **Historical / Superseded** — preserved for provenance but no longer the active mainline

---

## Research Timeline

| Date / period | Stage / event | Status | Model lineage | Main result / decision | Evidence / source | Effect on next stage |
|---|---|---|---|---|---|---|
| 2026-08~09 | Simplified 2D BCAT mainline established and Run 0–3 methodology built | Completed | `B0-2D-Legacy` | B0 geometry, DC metric definitions, DC mesh policy, and a usable relative GIDL/BTBT path were established | `docs/progress/run00_baseline.md` through `run03_btbt_gidl_feasibility.md`; `docs/RUN_SHEET.md` | Enabled formal MEB screening under one controlled Legacy model |
| 2026-08~09 | Formal MEB screening and mechanism correlation | Completed | `B0-2D-Legacy / NonlocalPath` | 31/36/41 nm screening established the deeper-MEB → lower project-internal GIDL direction; 5-level Cgd/field/GIDL correlation followed | `docs/progress/run04_meb_screening.md`; `docs/progress/run05_cov_gidl_correlation.md` | P1=41 nm became the initial screened-window candidate |
| 2026-08~09 | Elevated-temperature transistor-level validation | Completed | `B0-2D-Legacy / NonlocalPath` | 300/340/380 K GIDL/background/DC checks retained the MEB ranking while showing stronger high-T background sensitivity | `docs/progress/run06_temperature_robustness.md`; `docs/RUN_SHEET.md` | Motivated later temperature-dependent retention translation rather than a transistor-only conclusion |
| 2026-09 | Extended MEB boundary closure | Completed | `B0-2D-Legacy / NonlocalPath` | Sweep extended through 51 nm; P2=48 nm selected as transistor-level cell-validation candidate, 49 nm retained as challenger, 51 nm as floor-sensitive boundary reference | `docs/progress/run06_5_deeper_meb_boundary.md`; `docs/evidence/r65_evidence_manifest.md` | Removed the 41-nm search-boundary ambiguity and handed candidates toward 1T1C validation |
| 2026-09-11~14 | First feedback validation wave | Completed | Legacy + `3D-Sun-B0` | Hotspot-resolved E-field/BTBT analysis, common ROI mesh audit, 3D literature-consistent baseline fidelity study, and geometry-derived RWL proxy were closed at their stated scopes | `docs/evidence/feedback_efield_hotspot_validation_20260911.md`; `feedback_mesh_run65_full_validation_20260913.md`; `feedback_baseline_closeout_20260914.md`; `feedback_rwl_tradeoff_proxy_20260913.md` | Replaced peak-E-only interpretation with spatial critical-region interpretation; established selected-point 3D role and practical MEB trade-off proxy |
| 2026-09-14~23 | Legacy 1T1C operation / temperature checkpoint | Completed at feasibility level; final retention metric remained open | `B0-2D-Legacy` | 300 K write normalization, direct Hold, D0/D1 read, integrated W→H→R, and approximately normalized 300/340/380 K operation/Hold evidence were accumulated | `docs/evidence/run07_write_1v_calibration_20260914.md`; `run07_cell_operation_checkpoint_20260920.md`; `run07_hold_temperature_normalized_20260921.md`; `run07_whr_temperature_normalized_20260923.md` | Demonstrated cell-operation feasibility, but did not close a calibrated physical retention-time claim |
| 2026-09-22 | Post-Turn-02 research hierarchy formalized | Completed | Project-wide | Mainline was organized as single-WF MEB range → temperature robustness → DWFG transferability → selected-point 3D validation; 3.0 V WL requirement retained as an unresolved write-transfer guardrail | `docs/research/post_turn02_validation_roadmap.md`; `docs/FEEDBACK_LOG.md` | Preserved MEB as the central variable while defining downstream validation axes |
| 2026-10-04~05 | Literature-grounded 2D baseline reconstruction and reduced-order calibration | Completed | `B0-2D-PAPER-CAL` | Faithful paper-explicit 2D reconstruction showed substantial absolute electrical mismatch; after numerical/physical sensitivity checks, reduced-order calibration coordinates were introduced and C6/C7 were executed | `docs/research/b0_2d_baseline_reconstruction_calibration.md` | Created a new paper-grounded 2D lineage without rewriting Legacy evidence |
| 2026-10-05 | C7_4 final baseline freeze | Completed | `B0-2D-PAPER-CAL` | `C7_4 / B_QF_HALF` selected; FZ-A/B/C validation passed; calibration knobs frozen; C8 micro-fitting closed | `docs/research/b0_2d_final_freeze_plan.md`; `docs/RUN_SHEET.md` | Closed calibration and authorized production revalidation |
| 2026-10-05 onward | Calibrated production revalidation handoff | Historical planning / bridge still open | `B0-2D-PAPER-CAL` | Runtime-equivalence benchmark is the immediate gate before 31/36/41 nm calibrated DC/GIDL revalidation and later retention translation | `docs/research/b0_2d_production_revalidation_plan.md`; `HANDOFF.md` | Rebuild the main MEB/temperature/retention evidence on the frozen PAPER-CAL baseline |
| 2026-10-08 | New 300 K 15-point MEB Atlas + signed BTBT-ON/OFF/2D integration audit | Completed for within-branch data; lineage bridge open | `B0-2D-PAPER-CAL` post-freeze MeshLevel-2 branch | 15-point DC/Cgd/GIDL/spatial and OFF control were completed, all 1,036 independent checks passed, the signed ON−OFF current matched q∫BTBT to ≤0.62%, and shallow residual-current dominance was diagnosed; exact 2026-10-05 FZ-C parent identity remains unresolved | `data/paper_cal/atlas_300k_20261008/`; `docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md` | Preserve a validated internal atlas without asserting mesh-only identity; perform parent-lineage audit before promoting temperature/1T1C claims |

---

## Model-Lineage Transition Summary

```text
B0-2D-Legacy
  │
  ├─ Run 0–6.5 transistor-level method / MEB evidence
  ├─ Legacy Run-7 1T1C feasibility
  │
  └─ presentation-feedback validation
           ↓
      3D-Sun-B0 fidelity audit
           ↓
   faithful paper-grounded 2D control
           ↓
   reduced-order calibration
           ↓
          C6
           ↓
          C7
           ↓
B0-2D-PAPER-CAL = C7_4 / B_QF_HALF
           ↓
calibrated production revalidation
           ↓
GIDL → 1T1C retention translation
           ↓
temperature-dependent effective MEB range
           ↓
DWFG transferability / selected-point 3D validation
```

Historical Legacy results remain valid evidence within their original model and method scope.

They must not be relabeled as PAPER-CAL results.

---

## Current Forward Path

### Active

```text
300 K 15-point MEB Atlas → DATA-QC COMPLETE (post-freeze mesh branch)
→ exact 2026-10-05 FZ-C parent/deck lineage bridge or explicitly approved separate-branch status
→ selected 233/300/340/380 K transistor-level testing
→ new PAPER-CAL 1T1C Write/Hold/Read + retention-metric verification
→ effective MEB range, if cell and DC constraints justify it
```

### Planned downstream validation

- 233 K cold-point validation in the active lineage
- DWFG transferability
- selected-point 3D validation

### Conditional

- alternate leakage diagnosis if calibrated retention deviates from the GIDL trend
- local variation / robustness extension if needed to support the final range claim

---

## Timeline Update Rule

Add a new entry only when the event changes the research story, lineage, frozen method, candidate set, validation status, or next research stage.

For dates, prefer:

1. explicit execution / decision / presentation date in the source;
2. dated evidence / progress document;
3. decision date;
4. commit timestamp only as a repository-recording fallback.

Do not automatically treat a commit timestamp as the experiment date.

If the exact date cannot be established, use an approximate period or `date unresolved`.
