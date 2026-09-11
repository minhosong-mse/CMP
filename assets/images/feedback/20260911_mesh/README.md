# Mesh / Hotspot Feedback Visual Evidence — 2026-09-11

This directory stores the curated visual evidence for `FB-MESH-01`.

Primary presentation layout:

- `01_mesh_feedback_6panel.jpg` — 31/36/41 nm BTBT-hotspot maps (top row) paired with the corresponding Run-4 Mesh-Code 3 zoom views (bottom row).

Backup evidence:

- `08_36nm_mesh_ultrazoom.jpg` — representative local-triangle detail near the nominal 36 nm hotspot.
- `09_31nm_mesh_full.jpg`
- `10_36nm_mesh_full.jpg`
- `11_41nm_mesh_full.jpg`

Source-case mapping:

| MEB | Run-4 mesh node | Points | Elements | BTBT hotspot (um) |
|---:|---|---:|---:|---|
| 31 nm | `n53_msh` | 5739 | 12063 | `(0.051562496, 0.121875)` |
| 36 nm | `n29_msh` | 5789 | 12175 | `(0.051562496, 0.121875)` |
| 41 nm | `n58_msh` | 5830 | 12273 | `(0.052343745, 0.121875)` |

Common refinement rule:

```text
Mesh_Code = 3
base mesh = Medium
ROI X = 0.032–0.070 um
ROI Y = 0.112–0.133 um
local max/min = 1.0 / 0.25 nm
```

Scope: this is common-ROI coverage / comparison-consistency evidence, not an absolute mesh-independence proof.
