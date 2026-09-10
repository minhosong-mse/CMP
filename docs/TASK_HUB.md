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
| T-EFIELD-01 | Literature-grounded hotspot E-field / BTBT validation | Run 4–5 formal 31/36/41 nm, 300 K GIDL ON | **In Progress** | Five-paper methodology audit completed; feedback-level Measurement Protocol v1 scope frozen | Phase A: extract 31/36/41 nm BTBT hotspot coordinates and hotspot-following `|Ex|`, `|E|`, BTBT profiles; compare with old `E_wall,max` and terminal GIDL | Run 4/5 progress/evidence + presentation backup/main slide |
| T-MESH-01 | MEB-dependent hotspot / mesh validation | Run 3–4 Mesh-GIDL | **Pending after T-EFIELD-01 Phase A** | Common refinement ROI already defined | Verify 31/36/41 hotspot coordinates remain inside common ROI and record boundary margins; re-mesh only if coverage is insufficient | Run 4/5 evidence + mesh-validation backup slide |
| T-BASELINE-01 | Baseline recalibration / literature comparison | Run 0–1 | **In Progress elsewhere** | Existing B0 scope and limitations already documented | Continue Paper vs B0-v1 vs recalibrated B0-v2 comparison in the dedicated baseline workflow | Baseline validation slide + progress/decision update |
| T-RET-01 | 1T1C retention protocol freeze | Run 7 | **In Progress elsewhere** | MixedMode / write feasibility verified | Freeze Write → floating Hold → VSN decay → retention criterion before MEB retention sweep | Run 7 progress/evidence + methodology slide |

---

## 3. T-EFIELD-01 — Literature-grounded hotspot E-field / BTBT validation

### 3.1 Why this task exists

The formal Run 5 field metric was a reproducible fixed cut:

```text
Field    = Abs(ElectricField-V)
Cutline  = Y = 0.116 um
X range  = 0.032–0.070 um
Metric   = E_wall,max
```

Across MEB 31→41 nm, the existing formal results show approximately:

```text
GIDL endpoint decrease     ≈ 60.42%
fixed-cut E_wall,max drop  ≈ 1.69%
```

Presentation feedback raised two related questions:

1. should electric field be evaluated in the **actual GIDL / BTBT critical region** rather than only at one fixed wall cut?
2. if MEB changes the hotspot position, does the existing common Mesh-GIDL refinement remain valid?

The purpose of this task is **not** to find an electric-field metric that numerically matches the GIDL percentage change. The goal is to determine whether the much larger terminal-GIDL sensitivity can be explained plausibly by the spatial E-field / BTBT behavior in the actual GIDL-critical region.

This is a **supporting validation task**, not a new main research axis and not a reopening of the full 43–51 nm MEB search.

### 3.2 Literature-methodology checkpoint

A five-paper methodology audit was completed before restarting extraction. The recurring literature pattern was summarized as:

```text
physical GIDL / leakage critical region
→ spatial E-field profile / distribution
→ representative scalar metric if needed
→ terminal leakage / retention comparison
```

Important method-specific lessons carried forward:

- MEB / gate-structure changes can move or redistribute the electric-field peak, so a fixed spatial point alone may miss part of the mechanism.
- Peak field can remain similar while the BTBT-active spatial extent differs; width / integrated-field analysis is therefore a justified **conditional** follow-up when peak/profile evidence remains insufficient.
- Whole-device global Emax is not promoted as the formal GIDL mechanism metric.
- Automatic BTBT-maximum localization is a CMP reproducibility improvement, not claimed as a universal literature standard.

### 3.3 Feedback-level validation set

Use only the original formal three-level screening set:

```text
MEB = 31 / 36 / 41 nm
```

Rationale:

- `36 nm` = nominal literature-based reference,
- `31 nm` = shallow side (`-5 nm`),
- `41 nm` = deeper side (`+5 nm`).

These three cases were already executed under the same formal GIDL protocol and are sufficient for the present **mechanism / trend validation**. Extended 43–51 nm cases remain part of the later design-range analysis and are not reprocessed here unless a later thesis-level extension requires it.

### 3.4 Frozen source condition for Phase A

Use the existing formal 300 K GIDL-ON data:

```text
Mesh_Code = 3
T         = 300 K
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2Band(Model=NonlocalPath)
terminal  = |Idrain| @ VG=-0.7 V
```

The source decks store:

```text
ElectricField/Vector
Band2BandGeneration
```

Coordinate convention:

```text
X = wafer depth
Y = source-to-drain lateral direction
```

### 3.5 Common Mesh-GIDL region

Existing common local refinement ROI:

```text
X = 0.032–0.070 um
Y = 0.112–0.133 um
local max/min = 1.0 / 0.25 nm
```

This ROI was originally placed with margin around the observed drain-side BTBT-sensitive region.

Before using it as the formal hotspot search domain, confirm from the 31/36/41 spatial maps that the dominant drain-side BTBT lobe lies within the common refined region. Do **not** assign different manually chosen hotspot search windows to individual MEB cases.

The formal rule is:

```text
common search / refinement domain
→ case-specific automatically extracted hotspot coordinate
→ case-specific hotspot-following cut
```

### 3.6 Measurement Protocol v1 — Phase A

For each MEB = 31 / 36 / 41 nm:

1. inspect the drain-side `Band2BandGeneration` spatial map and confirm the dominant BTBT lobe is covered by the common ROI;
2. automatically extract:

```text
BTBT_max
X_hot
Y_hot
```

3. create an X-direction / wafer-depth cut at:

```text
Y = Y_hot
```

4. extract on the same cut:

```text
|ElectricField-X|(X)      = primary directional field profile
Abs(ElectricField-V)(X)   = supporting field-magnitude profile
Band2BandGeneration(X)    = BTBT spatial profile
```

5. record the minimum Phase-A scalar set:

```text
X_hot
Y_hot
BTBT_max
E_x,peak
X_at_E_x,peak
|E|@BTBTmax   (low-cost cross-check when available)
```

6. compare with the existing control / electrical metrics:

```text
old E_wall,max
terminal |Idrain| @ VG=-0.7 V
```

### 3.7 Phase-A decision gate

After the 31/36/41 profiles are available, stop and classify the result before adding more metrics.

#### Outcome A — profile evidence is sufficient

If E-field and BTBT spatial profiles show a clear, physically interpretable redistribution / weakening consistent with the GIDL direction, close the feedback-level mechanism validation without adding unnecessary integral metrics.

#### Outcome B — peak field still changes little, but BTBT spatial extent changes materially

Activate conditional Phase B based on the Pi-BCAT literature precedent:

```text
BTBT-active-region width
integral(|E_x| dx) over the frozen BTBT-active region
```

The active-region threshold must be fixed using a transparent sensitivity procedure and must **not** be selected afterward solely because it best matches the terminal-GIDL trend.

#### Outcome C — E-field and BTBT spatial evidence both fail to explain the terminal trend

Do not tune the metric to force agreement. Record the limited conclusion:

> the present local/spatial E-field evidence is insufficient by itself to explain the full 31→41 nm terminal-GIDL sensitivity.

### 3.8 Existing 36 nm exploratory checkpoint

A prior exploratory automatic BTBT hotspot extraction exists for one 36 nm dataset:

```text
Band2BandGeneration_max = 8.41825e21 cm^-3 s^-1
X_BTBT,max              = 0.0515625 um
Y_BTBT,max              = 0.1218750 um
```

This remains a useful checkpoint, but the formal 31/36/41 Phase-A table should use one consistent source set and one frozen procedure.

### 3.9 Phase-A output table

Create one consolidated table:

| MEB | X_hot | Y_hot | BTBT_max | E_x,peak | X_at_Epeak | |E|@BTBTmax | old E_wall,max | GIDL endpoint | ROI margin |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 31 | ... | ... | ... | ... | ... | ... | 871969.09 | 1.9624468e-14 | ... |
| 36 | ... | ... | ... | ... | ... | ... | 867936.60 | 1.3777737e-14 | ... |
| 41 | ... | ... | ... | ... | ... | ... | 857194.93 | 7.7683012e-15 | ... |

### 3.10 Current resume point

```text
Literature methodology audit : Completed
Protocol v1 scope             : Frozen for feedback-level Phase A
Formal extraction             : Not yet started
Next action                   : 31 nm hotspot / profile extraction
```

---

## 4. T-MESH-01 — Minimal hotspot / common-ROI audit

### 4.1 Scope

This is deliberately limited to the current presentation-feedback need.

For MEB 31 / 36 / 41 nm:

- record `X_hot`, `Y_hot`,
- confirm each hotspot lies inside the common Mesh-GIDL ROI,
- calculate margin to each ROI boundary,
- inspect whether the dominant BTBT lobe remains covered by the refined region.

Do not launch a new deep mesh-convergence study unless:

- a hotspot approaches or exits the refinement boundary,
- the profile is visibly clipped by the ROI,
- the extracted result shows a numerical inconsistency that makes the trend interpretation unreliable.

The conclusion from this task should be limited to **common refinement coverage for the feedback-validation set**, not absolute mesh-independent BTBT accuracy.

---

## 5. Cross-chat feedback tasks

### T-BASELINE-01

Handled in a dedicated parallel workflow. Key presentation issue:

```text
literature 3-D BCAT
vs
simplified 2-D B0
```

Need to separate absolute reproduction limits from the current use of a common model for relative MEB trends.

### T-RET-01

Handled in the dedicated Run-7 workflow. Current status remains:

```text
MixedMode / write feasibility : verified
floating hold                 : pending
retention criterion           : not yet frozen
full retention validation     : not yet complete
```

Required direction remains:

```text
Write → floating Hold → VSN(t) decay → pre-frozen retention criterion → optional Read
```

---

## 6. Presentation-image staging policy

Presentation work may require several screenshots. Keep them **in chat / local workspace first** while the extraction protocol is still being executed.

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

Do not upload many nearly identical raw screenshots simply because they were generated. Prefer a consolidated numeric table plus representative images when that preserves the same evidence.

---

## 7. Task completion rule

When a task closes:

1. move scientific results into the relevant `docs/progress/` and `docs/evidence/` files,
2. record any interpretation-changing choice in `DECISIONS.md`,
3. update `RUN_SHEET.md` only if an official stage status / exit criterion changes,
4. mark the TASK_HUB row Completed and retain only a concise checkpoint / link.
