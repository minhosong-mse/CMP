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

Do **not** commit every exploratory screenshot or click-level step. Promote material that must be reused, audited, cited, or presented.

---

## 2. Active / completed feedback tasks

| Task ID | Task | Source run / data | Status | Completed checkpoint | Next action | Final destination |
|---|---|---|---|---|---|---|
| T-EFIELD-01 | Literature-grounded hotspot E-field / BTBT validation | Run 4–5 formal 31/36/41 nm, 300 K GIDL ON | **Completed — feedback level** | Phase A + conditional Phase B completed; hotspot profiles, 10/20/50% threshold sensitivity, field / BTBT integrals and terminal-GIDL comparison recorded | Use curated figures/table for presentation; reopen only if thesis-level extension needs broader MEB or 2-D integration | [`docs/evidence/feedback_efield_hotspot_validation_20260911.md`](evidence/feedback_efield_hotspot_validation_20260911.md) + `data/run05/feedback_efield_20260911/` |
| T-MESH-01 | MEB-dependent hotspot / common-ROI validation | Run 3–4 Mesh-GIDL | **Completed — feedback level** | 31/36/41 BTBT hotspots all remain comfortably inside common Mesh-GIDL ROI; 41 nm hotspot shifts only ~0.781 nm in X | No re-mesh for this feedback set; reopen only if later cases approach/exit ROI or show numerical inconsistency | same E-field feedback evidence + hotspot-ROI figure |
| T-BASELINE-01 | Baseline recalibration / literature comparison | Run 0–1 | **In Progress elsewhere** | Existing B0 scope and limitations documented | Continue Paper vs B0-v1 vs recalibrated B0-v2 comparison in dedicated baseline workflow | Baseline validation slide + progress/decision update |
| T-RET-01 | 1T1C retention protocol freeze | Run 7 | **In Progress elsewhere** | MixedMode / write feasibility verified | Freeze Write → floating Hold → VSN decay → retention criterion before MEB retention sweep | Run 7 progress/evidence + methodology slide |

---

## 3. T-EFIELD-01 close-out checkpoint

### Why this task existed

Formal Run 5 showed:

```text
MEB 31 → 41 nm
GIDL endpoint decrease          ≈ 60.42%
fixed-cut E_wall,max decrease   ≈ 1.69%
```

The presentation question was whether the much larger terminal-GIDL sensitivity could be interpreted more defensibly from the actual GIDL / BTBT critical region rather than one fixed field peak.

This task was deliberately kept as a **supporting validation**, not a new main research axis and not a reopening of the 43–51 nm MEB design-range search.

### Frozen validation set / condition

```text
MEB       = 31 / 36 / 41 nm
Mesh_Code = 3
T         = 300 K
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2Band(Model=NonlocalPath)
terminal  = |Idrain| @ VG=-0.7 V
```

Coordinate convention:

```text
X = wafer depth
Y = source-to-drain lateral direction
```

Common Mesh-GIDL ROI:

```text
X = 0.032–0.070 um
Y = 0.112–0.133 um
```

### Completed protocol

For each 31/36/41 nm case:

1. full-Si `Band2BandGeneration` maximum automatically located;
2. `X_hot`, `Y_hot`, `BTBT_max` recorded;
3. hotspot coverage inside common Mesh-GIDL ROI checked;
4. hotspot-following X-cut generated at `Y_hot`;
5. `Band2BandGeneration`, `ElectricField-X`, and `Abs(ElectricField-V)` profiles exported;
6. profile / peak results compared with old `E_wall,max` and terminal GIDL;
7. because the directional field peak did not decrease with GIDL, conditional Phase B was activated;
8. `G/Gmax >= 10%, 20%, 50%` active-region width and `integral(|E| dx)` sensitivity were evaluated;
9. 1-D `integral(G_BTBT dx)` was retained as a spatial-generation trend cross-check, not as a terminal-current calculation.

All three extracted hotspots had:

```text
Y_hot = 0.121875 um
```

### Key close-out result

31 → 41 nm:

```text
GIDL endpoint                  -60.42%
BTBT_max                       -52.43%
1-D integrated BTBT            -57.74%
20% BTBT-active width          -12.68%
20% active-region int(|E| dx)  -14.68%
hotspot-cut |E| peak            -3.52%
old fixed E_wall,max            -1.69%
ElectricField-X peak            +8.16%
```

Supported interpretation:

> The large MEB-dependent GIDL reduction is not adequately represented by a single local E-field peak. Across 31/36/41 nm, BTBT-generation amplitude and active spatial extent decrease, and the field integrated over the BTBT-active region also decreases. The spatially integrated BTBT-generation trend is consistent with the terminal GIDL reduction. The mechanism is therefore more defensibly discussed from the **critical-region spatial E-field / BTBT distribution** than from one peak-field scalar.

Guardrails:

- do not claim the 20% threshold is a universal literature standard;
- do not claim the 1-D BTBT integral equals terminal current;
- do not claim absolute BTBT calibration or absolute mesh independence;
- do not promote this feedback validation into the main research objective;
- do not claim direct `Cgd → E-field → GIDL` causality from this result alone.

Evidence:

- [`docs/evidence/feedback_efield_hotspot_validation_20260911.md`](evidence/feedback_efield_hotspot_validation_20260911.md)
- `data/run05/feedback_efield_20260911/`
- `assets/images/feedback/20260911_efield/`

---

## 4. T-MESH-01 close-out checkpoint

Common ROI coverage was checked using the automatically extracted BTBT hotspots.

| MEB | Xhot (um) | Yhot (um) | X-low margin (nm) | X-high margin (nm) | Y-low margin (nm) | Y-high margin (nm) |
|---:|---:|---:|---:|---:|---:|---:|
| 31 | 0.051562496 | 0.121875 | 19.562 | 18.438 | 9.875 | 11.125 |
| 36 | 0.051562496 | 0.121875 | 19.562 | 18.438 | 9.875 | 11.125 |
| 41 | 0.052343745 | 0.121875 | 20.344 | 17.656 | 9.875 | 11.125 |

Conclusion for this feedback set:

- all hotspots remain comfortably inside the common refinement region;
- 41 nm moves only about `0.781 nm` deeper in X;
- no re-mesh is required for the present 31/36/41 presentation-feedback validation.

This is a **common-ROI coverage check**, not proof of absolute mesh-independent BTBT accuracy.

---

## 5. Cross-chat tasks still open

### T-BASELINE-01

Handled in a dedicated parallel workflow. Main issue:

```text
literature 3-D BCAT
vs
simplified 2-D B0
```

Need to separate absolute reproduction limits from the present use of a common model for relative MEB trends.

### T-RET-01

Handled in the Run-7 workflow. Current wording remains limited to:

```text
MixedMode / write feasibility : verified
floating hold                 : pending
retention criterion           : not yet frozen
full retention validation     : not yet complete
```

Required direction:

```text
Write → floating Hold → VSN(t) decay → pre-frozen retention criterion → optional Read
```

---

## 6. README integration rule

Do **not** update the project README for each individual feedback item. The final README synthesis is deferred until the main post-presentation feedback set is completed so that baseline, E-field/mesh, retention, and practical trade-off wording can be integrated consistently in one pass.

---

## 7. Task completion rule

When another feedback task closes:

1. move scientific results into the relevant `docs/progress/` and `docs/evidence/` files;
2. record interpretation-changing choices in `DECISIONS.md` when necessary;
3. update `RUN_SHEET.md` only if an official stage status / exit criterion changes;
4. mark the TASK_HUB row Completed and retain only a concise checkpoint / link.
