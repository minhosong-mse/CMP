# Run 4 Mesh / Hotspot Feedback Evidence — 2026-09-11

Purpose: preserve the numerical checkpoint used to answer `FB-MESH-01` for the formal 31/36/41 nm MEB comparison.

## Frozen rule

```text
Mesh_Code = 3
Base mesh = Medium
Common hotspot ROI:
  X = 0.032–0.070 um
  Y = 0.112–0.133 um
Local refinement max/min = 1.0 / 0.25 nm
```

## Files

- `mesh_hotspot_coverage_summary.csv` — node mapping, mesh counts, hotspot coordinates, ROI margins, and frozen refinement rule.

Visual evidence is stored under:

- `assets/images/feedback/20260911_mesh/`

Scientific interpretation / guardrails are documented in:

- `docs/evidence/feedback_mesh_common_roi_validation_20260911.md`

## Scope boundary

This evidence verifies common-ROI coverage and comparison consistency for 31/36/41 nm. It is not an absolute mesh-independence or full convergence proof.
