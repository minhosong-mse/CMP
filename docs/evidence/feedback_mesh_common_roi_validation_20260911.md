# FB-MESH-01 — Per-MEB Mesh / Hotspot Coverage Validation

Date: 2026-09-11  
Scope: first-topic-presentation feedback support  
Affected runs: Run 3 mesh development, Run 4 formal 31/36/41 nm MEB screening  
Status: **Resolved — feedback level**

## 1. Feedback question

The feedback question is not whether the present mesh is absolutely mesh-independent. The practical question is:

> If MEB changes, can the BTBT/GIDL hotspot move enough that a single common Mesh-GIDL refinement region becomes invalid, or is the same refinement rule still appropriate for a fair 31/36/41 nm comparison?

The validation therefore checks three things:

1. the same `Mesh_Code = 3` rule is used for all three MEB cases;
2. each independently extracted BTBT hotspot remains inside the same common refinement ROI with margin;
3. the actual Run-4 mesh images show that the hotspot region is refined in each case.

This is a **coverage / comparison-consistency validation**, not an absolute mesh-convergence proof.

## 2. Frozen mesh rule

Run 3 introduced `Mesh_Code = 3` as:

```text
base mesh = Medium
common drain-side BTBT-hotspot ROI:
  X = 0.032 .. 0.070 um
  Y = 0.112 .. 0.133 um
local refinement:
  max = 0.0010 um = 1.0 nm
  min = 0.00025 um = 0.25 nm
```

The same SDE mesh rule is used by the Run-4 31/36/41 nm screening cases. Geometry changes through `MEB_Depth`; the hotspot refinement policy itself is not retuned case-by-case.

Reference implementation:

- `code/sde/run03/bcat_baseline_sde_r3_meshgidl.cmd`
- `code/sde/run04/bcat_sde_r4_meb_screening_executed_snapshot.cmd`

## 3. Formal cases and actual mesh sizes

| MEB | Run-4 mesh node | Points | Elements |
|---:|---|---:|---:|
| 31 nm | `n53_msh` | 5739 | 12063 |
| 36 nm | `n29_msh` | 5789 | 12175 |
| 41 nm | `n58_msh` | 5830 | 12273 |

The element counts are not expected to be numerically identical because MEB changes the geometry and therefore the mesher topology. The important comparison-control condition is that the **same mesh rule and common refinement ROI** are used.

## 4. Independently extracted BTBT hotspots

The hotspot coordinates were obtained from the final GIDL-state data using full-Silicon `Band2BandGeneration` maximum extraction, not by manually choosing different search windows for each MEB.

| MEB | BTBTmax (cm^-3 s^-1) | Xhot (um) | Yhot (um) |
|---:|---:|---:|---:|
| 31 nm | 1.1673607e22 | 0.051562496 | 0.121875 |
| 36 nm | 8.4182472e21 | 0.051562496 | 0.121875 |
| 41 nm | 5.5526998e21 | 0.052343745 | 0.121875 |

Observed hotspot movement over 31→41 nm:

```text
Delta Xhot ≈ +0.781 nm
Delta Yhot = 0 nm at the extracted mesh-node resolution
```

The hotspot motion is therefore small compared with the dimensions and margins of the common refinement ROI.

## 5. ROI-margin audit

Common ROI:

```text
X = 0.032–0.070 um
Y = 0.112–0.133 um
```

| MEB | X-low margin (nm) | X-high margin (nm) | Y-low margin (nm) | Y-high margin (nm) | Nearest edge margin (nm) |
|---:|---:|---:|---:|---:|---:|
| 31 | 19.562 | 18.438 | 9.875 | 11.125 | 9.875 |
| 36 | 19.562 | 18.438 | 9.875 | 11.125 | 9.875 |
| 41 | 20.344 | 17.656 | 9.875 | 11.125 | 9.875 |

All three hotspots are comfortably inside the common ROI; none is near an ROI boundary.

## 6. Visual evidence layout

The preferred presentation / backup-slide layout is a 2×3 comparison:

```text
              31 nm                 36 nm                 41 nm
Top row   BTBT hotspot map      BTBT hotspot map      BTBT hotspot map
Bottom    Run-4 mesh zoom       Run-4 mesh zoom       Run-4 mesh zoom
```

Combined evidence figure:

- `assets/images/feedback/20260911_mesh/01_mesh_feedback_6panel.png`

Per-case hotspot / mesh images:

- `02_31nm_btbt_hotspot.png`
- `03_31nm_mesh_zoom.png`
- `04_36nm_btbt_hotspot.png`
- `05_36nm_mesh_zoom.png`
- `06_41nm_btbt_hotspot.png`
- `07_41nm_mesh_zoom.png`

Additional backup evidence:

- `08_36nm_mesh_ultrazoom.png` — representative local-triangle detail near the nominal 36 nm hotspot
- `09_31nm_mesh_full.png`
- `10_36nm_mesh_full.png`
- `11_41nm_mesh_full.png`

## 7. Supported conclusion

> The 31/36/41 nm cases use the same `Mesh_Code = 3` policy: Medium base mesh plus one common drain-side BTBT-hotspot refinement ROI. The independently extracted BTBT hotspots remain inside that ROI with at least about 9.875 nm distance to the nearest ROI edge, and the Run-4 mesh screenshots confirm that the corresponding physical region is locally refined for each MEB. Therefore, for the present 31–41 nm feedback-validation set, a common refinement ROI is a defensible and fair comparison rule; case-specific re-meshing is not required by the observed hotspot motion.

## 8. Interpretation guardrails

Do **not** state:

- “mesh independence has been proven”;
- “0.25 nm is the universally converged BTBT mesh size”;
- “the mesh error is zero”;
- “case-specific remeshing can never be required outside 31–41 nm.”

Use scoped wording:

- common-ROI **coverage** is verified for 31/36/41 nm;
- the same refinement rule supports comparison consistency;
- the observed hotspot motion does not require case-specific ROI relocation in this set;
- a separate convergence study would be required for an absolute mesh-independence claim;
- if later MEB cases approach/leave the ROI or show numerical inconsistency, the mesh strategy should be reopened.

## 9. Relation to the E-field feedback

This mesh evidence reuses the hotspot coordinates extracted during `FB-EFIELD-01`, but answers a different question.

- `FB-EFIELD-01`: is peak field alone sufficient to interpret GIDL, or is critical-region spatial behavior needed?
- `FB-MESH-01`: does the common local mesh continue to cover that critical region across MEB cases?

Keeping these claims separate prevents the mesh check from being overstated as a mechanism proof or convergence proof.

## 10. README integration

No main-README rewrite is performed at this stage. Final README synthesis remains deferred until the principal presentation-feedback set is completed.
