# CMP TASK HUB

> Purpose: track **where cross-chat work is currently paused and what the next concrete action is**.
> This file is a lightweight checkpoint layer. It is not a replacement for `RUN_SHEET.md`, `DECISIONS.md`, `CMD_HUB.md`, or formal `docs/progress/` / `docs/evidence/` records.

## 1. Operating rule

Use each layer for a different purpose:

- **Chat / local workspace**: exploratory work, screenshots, failed attempts, UI steps, temporary measurements.
- **TASK_HUB**: current task state, frozen method, completed checkpoint, next action.
- **RUN_SHEET**: official research-stage status and exit criteria.
- **DECISIONS**: decisions that change interpretation, metrics, scope, or downstream work.
- **progress / evidence**: finalized scientific results and curated evidence.

Do **not** commit every exploratory screenshot or click-level step. Promote only material that must be reused, audited, cited, or presented.

---

## 2. Active tasks

| Task ID | Task | Source run / data | Status | Completed checkpoint | Next action | Final destination |
|---|---|---|---|---|---|---|
| T-EFIELD-01 | Hotspot-based E-field validation | Run 6.5, 300 K GIDL ON | **In Progress** | 36 nm BTBT hotspot automatically extracted | Measure `E@BTBTmax` at 36 nm, then repeat 41→43→45→47→48→49→51 nm | Run 6.5 progress/evidence + presentation backup/main slide |
| T-MESH-01 | MEB-dependent hotspot / mesh validation | Run 6.5 Mesh-GIDL | **Pending after T-EFIELD-01** | Common refinement ROI is already defined | Plot hotspot coordinates vs MEB and verify all points remain inside common ROI with margin | Run 6.5 evidence + mesh-validation backup slide |
| T-BASELINE-01 | Baseline recalibration / literature comparison | Run 0–1 | Planned | Existing B0 scope and limitations already documented | Compare Paper vs B0-v1 vs recalibrated B0-v2 after new simulation is available | Baseline validation slide + progress/decision update |
| T-RET-01 | 1T1C retention protocol freeze | Run 7 | In Progress elsewhere | MixedMode write feasibility verified | Freeze write/hold/retention criterion before MEB retention sweep | Run 7 progress/evidence + methodology slide |

---

## 3. T-EFIELD-01 — Hotspot-based electric-field validation

### 3.1 Why this task exists

The earlier formal Run 6.5 field metric was a reproducible fixed cut:

```text
Field    = Abs(ElectricField-V)
Cutline  = Y = 0.116 um
X range  = 0.032–0.070 um
Metric   = E_wall,max
```

Presentation feedback raised the question whether electric field should instead be measured **at the actual GIDL/BTBT hotspot**, especially because hotspot position may shift with MEB depth.

The fixed-cut result remains a reproducibility / cross-check metric. This task adds a hotspot-based metric rather than deleting the old metric.

### 3.2 Source data

Use the already executed **Run 6.5 / 300 K / GIDL ON** final SDevice TDRs.

```text
Mesh_Code = 3
T         = 300 K
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2Band(Model=NonlocalPath)
```

SWB node mapping:

| MEB | Node |
|---:|---:|
| 36 nm | n119 |
| 41 nm | n120 |
| 43 nm | n121 |
| 45 nm | n122 |
| 47 nm | n123 |
| 48 nm | n124 |
| 49 nm | n125 |
| 51 nm | n126 |

No new simulation is required unless the later mesh audit shows the existing local refinement is insufficient.

### 3.3 Common BTBT hotspot search domain

Use SVisual:

```text
Tools → Minimum/Maximum Field Value
Field     = Band2BandGeneration
Function  = Maximum
Domain constraints:
  X = 0.032–0.070 um
  Y = 0.112–0.133 um
```

This search domain matches the existing common drain-side Mesh-GIDL refinement window.

For each MEB, record:

```text
BTBTmax
X_BTBT,max
Y_BTBT,max
```

### 3.4 Final formal hotspot E-field metric

**Formal metric:**

```text
E@BTBTmax = Abs(ElectricField-V)
            evaluated at the exact (X_BTBT,max, Y_BTBT,max) coordinate
```

Use SVisual Probe / `probe_field` at the exact automatically extracted BTBT maximum coordinate.

Reason for this definition:

- Manual color-map clicking was tested and rejected because it is operator dependent.
- A hotspot-centered fixed-size ROI maximum was also tested, but the E-field maximum landed on the ROI boundary in the first 36 nm trial, showing dependence on the arbitrary ROI size.
- Therefore the final metric is the electric field **at the automatically identified BTBT maximum coordinate**, which minimizes manual and ROI-size arbitrariness.

The old `E_wall,max` remains available as an independent fixed-location cross-check.

### 3.5 36 nm checkpoint

Automatic BTBT hotspot extraction completed for `MEB=36 nm / n119`:

```text
Band2BandGeneration_max = 8.41825e21 cm^-3 s^-1
X_BTBT,max              = 0.0515625 um
Y_BTBT,max              = 0.1218750 um
```

Still pending for 36 nm:

```text
Probe Abs(ElectricField-V)
at X=0.0515625 um, Y=0.1218750 um
→ record E@BTBTmax
```

### 3.6 Remaining MEB sequence

```text
36 nm : BTBT hotspot done → E@BTBTmax pending
41 nm : pending
43 nm : pending
45 nm : pending
47 nm : pending
48 nm : pending
49 nm : pending
51 nm : pending
```

### 3.7 After all MEB cases are measured

Create one consolidated table:

| MEB | X_BTBT,max | Y_BTBT,max | BTBTmax | E@BTBTmax | E_wall,max | mesh ROI margin |
|---:|---:|---:|---:|---:|---:|---:|
| 36 | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... |

Then evaluate:

1. hotspot movement vs MEB,
2. whether every hotspot remains inside the common Mesh-GIDL ROI,
3. whether hotspot-based field and fixed-cut field show the same directional trend,
4. whether the mechanism statement should be strengthened or narrowed.

Do not claim `Cgd → E-field → GIDL` as a proven direct causal chain unless the new spatial evidence supports that interpretation.

---

## 4. Presentation-image staging policy

Presentation work may require many screenshots per MEB. Keep them **in chat / local workspace first** while the extraction protocol is still changing.

Promote images to GitHub only when one of the following is true:

- selected for a main or backup slide,
- needed to prove hotspot location or mesh coverage,
- needed for a formal evidence manifest,
- needed to reproduce a published numerical claim.

Suggested later destination after curation:

```text
assets/images/feedback/<review-date-or-topic>/
docs/evidence/<matching_manifest>.md
```

Do not upload eight nearly identical raw screenshots simply because they were generated. Prefer a curated set plus a numeric coordinate table when that preserves the same evidence.

---

## 5. Task completion rule

When a task closes:

1. move scientific results into the relevant `docs/progress/` and `docs/evidence/` files,
2. record any interpretation-changing choice in `DECISIONS.md`,
3. update `RUN_SHEET.md` only if an official stage status / exit criterion changes,
4. mark the TASK_HUB row Completed and retain only a concise checkpoint / link.
