# R6.5 Mesh / BTBT Hotspot Feedback Data — 2026-09-13

Purpose: close the mesh-feedback question across the **full Run 6.5 MEB set**, rather than only the earlier 31/36/41 nm representative set.

## Frozen comparison conditions

```text
Run       = R6.5
MEB       = 36 / 41 / 43 / 45 / 47 / 48 / 49 / 51 nm
T         = 300 K
Mesh_Code = 3
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2BandGeneration maximum in full Silicon domain
```

Common Mesh-GIDL refinement rule:

```text
ROI X = 0.032–0.070 um
ROI Y = 0.112–0.133 um
local max/min = 1.0 / 0.25 nm
```

## Files

- `r65_mesh_raw_extract.csv`
  - values transcribed directly from Sentaurus Visual hotspot / mesh screenshots
  - includes MEB, SDevice node, mesh node, BTBTmax, Xhot, Yhot, Points, Elements
- `r65_mesh_hotspot_coverage_summary.csv`
  - adds four ROI-edge margins, nearest-edge margin, and PASS/FAIL coverage audit
- `screenshot_manifest.csv`
  - canonical screenshot names / node mapping for the raw evidence pack

## Result

All eight R6.5 MEB cases pass the common-ROI coverage audit.

```text
Yhot = 0.121875 um for all eight cases
Xhot range = 0.0515625–0.0539063 um
Delta Xhot, 36→51 nm ≈ +2.344 nm
minimum nearest ROI-edge margin = 9.875 nm
ROI coverage = PASS for 8/8 cases
```

The mesh element / point counts vary gradually with MEB because geometry changes, while the same `Mesh_Code=3` refinement rule is retained.

## Claim boundary

Supported:

> Across the full R6.5 MEB set, independently extracted BTBT hotspots remain inside the same common Mesh-GIDL refinement ROI with at least 9.875 nm nearest-edge margin. The common mesh policy therefore provides hotspot coverage and case-to-case comparison consistency across the R6.5 geometry sweep.

Do not claim:

- absolute mesh independence;
- zero numerical mesh error;
- `0.25 nm` as a universal converged BTBT mesh size.

Absolute mesh-independence would require a separate convergence study.
