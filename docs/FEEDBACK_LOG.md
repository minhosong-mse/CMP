# CMP FEEDBACK LOG

> Purpose: track mentor / presentation / review feedback that cuts across multiple Runs.
> Feedback is **not forced into Run chronology**. Each item links to the affected Run(s), task(s), and final evidence location.

## 1. Feedback lifecycle

```text
Feedback received
→ FEEDBACK_LOG entry
→ TASK_HUB action item
→ analysis / simulation / post-processing
→ curated evidence
→ final interpretation / slide update
→ feedback item closed
```

## 2. First-topic-presentation feedback matrix

| Feedback ID | Feedback / question | Affected Run(s) | Task | Status | Resolution / target |
|---|---|---|---|---|---|
| `FB-EFIELD-01` | Should the E-field be evaluated in the actual BTBT/GIDL critical region, and can spatial E-field / BTBT behavior explain the large GIDL-vs-field sensitivity mismatch? | Run 3–5 | `T-EFIELD-01` | **Resolved — feedback level** | 31/36/41 hotspot-following Phase A + conditional Phase B completed. Evidence: [`feedback_efield_hotspot_validation_20260911.md`](evidence/feedback_efield_hotspot_validation_20260911.md) |
| `FB-MESH-01` | If MEB changes hotspot position, is the common Mesh-GIDL refinement still valid for each MEB case, and how should the per-MEB mesh-setting evidence be shown? | Run 3–4 | `T-MESH-01` | **In Progress — next task** | ROI-coverage checkpoint already obtained from E-field validation. Next: per-MEB mesh screenshots / refinement-setting evidence / presentation backup |
| `FB-BASELINE-01` | How closely does the simplified 2-D B0 reproduce the literature 3-D BCAT electrical characteristics? | Run 0–1 | `T-BASELINE-01` | **In Progress elsewhere** | Paper vs B0-v1 vs recalibrated B0-v2 comparison + explicit model-scope statement |
| `FB-RET-01` | What exactly is the 1T1C retention measurement definition? | Run 7; downstream Run 8–9 | `T-RET-01` | **In Progress elsewhere** | Write → floating Hold → VSN decay → pre-frozen retention criterion → optional Read |
| `FB-RC-01` | Does deeper metal etch-back introduce a practical DRAM trade-off such as increased word-line resistance / RC delay? | Run 6.5 interpretation; downstream synthesis | future synthesis | **Open / literature-supported consideration** | keep as an unmodeled practical trade-off unless directly simulated |

## 3. Resolved feedback — E-field / BTBT critical-region validation

### Original issue

Formal Run 5 showed:

```text
MEB 31 → 41 nm
GIDL endpoint decrease          ≈ 60.42%
fixed-cut E_wall,max decrease   ≈ 1.69%
```

The goal was **not** to force a new E-field metric to reproduce the GIDL percentage. The goal was to determine whether the GIDL trend can be explained more defensibly using spatial E-field / BTBT behavior in the actual critical region.

### Literature-grounded logic

Before extraction, five BCAT / DRAM leakage papers were reviewed. The common logic was:

```text
physical GIDL / leakage critical region
→ spatial E-field profile or map
→ representative peak / region metric when useful
→ terminal leakage / retention comparison
```

CMP-specific reproducibility additions:

- automatic `Band2BandGeneration` maximum localization;
- common ROI + hotspot-following X-cut;
- conditional `G/Gmax = 10/20/50%` sensitivity when peak-only evidence is insufficient.

These implementation choices are not claimed as universal literature standards.

### Validation set

```text
MEB       = 31 / 36 / 41 nm
Mesh_Code = 3
T         = 300 K
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2Band(Model=NonlocalPath)
GIDL      = |Idrain| @ VG=-0.7 V
```

### Completed flow

For all three cases:

1. full-Si `BTBT_max`, `X_hot`, `Y_hot` automatically extracted;
2. common Mesh-GIDL ROI coverage checked;
3. X-direction cut created at `Y_hot`;
4. `Band2BandGeneration`, `ElectricField-X`, `Abs(ElectricField-V)` profiles exported;
5. profile / peak behavior compared with old `E_wall,max` and terminal GIDL;
6. because directional peak field did not decrease with GIDL, Phase B was activated;
7. 10/20/50% normalized BTBT-active-region width and `int(|E| dx)` were checked;
8. 1-D `int(G_BTBT dx)` was used only as a spatial-generation trend cross-check.

All three cases returned:

```text
Y_hot = 0.121875 um
```

### Close-out result: 31 → 41 nm

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

Threshold sensitivity:

- 10%, 20%, and 50% criteria all preserve the decreasing active-width and integrated-field trend;
- 20% is retained only as a representative middle criterion.

### Resolved interpretation

> The MEB-dependent GIDL reduction is not adequately represented by one local E-field maximum. Across 31/36/41 nm, BTBT-generation amplitude decreases, the BTBT-active spatial extent narrows, and the field integrated over the active region also decreases. The spatially integrated BTBT-generation trend is consistent with terminal GIDL reduction. Therefore the supporting mechanism is better discussed from the **critical-region spatial E-field / BTBT distribution** than from one peak-field scalar.

Interpretation boundaries:

- no direct `Cgd → E-field → GIDL` causal law is proven;
- 1-D BTBT integral is not a terminal-current calculation;
- absolute BTBT calibration is not claimed;
- this remains a supporting validation, not the main research axis.

Evidence and reusable data:

```text
docs/evidence/feedback_efield_hotspot_validation_20260911.md
data/run05/feedback_efield_20260911/
assets/images/feedback/20260911_efield/
```

## 4. Mesh-feedback handoff checkpoint

The E-field validation already produced one useful preliminary mesh checkpoint:

```text
common Mesh-GIDL ROI
X = 0.032–0.070 um
Y = 0.112–0.133 um
```

| MEB | Xhot (um) | Yhot (um) | X-low margin (nm) | X-high margin (nm) | Y-low margin (nm) | Y-high margin (nm) |
|---:|---:|---:|---:|---:|---:|---:|
| 31 | 0.051562496 | 0.121875 | 19.562 | 18.438 | 9.875 | 11.125 |
| 36 | 0.051562496 | 0.121875 | 19.562 | 18.438 | 9.875 | 11.125 |
| 41 | 0.052343745 | 0.121875 | 20.344 | 17.656 | 9.875 | 11.125 |

This establishes only that all three extracted hotspots are comfortably inside the common refinement ROI. It **does not close the mesh-setting feedback** and is not proof of absolute mesh independence.

Next mesh-feedback work:

- collect / curate per-MEB mesh screenshots;
- show the common hotspot refinement window and local spacing;
- verify that the same refinement rule is applied consistently across 31/36/41 nm;
- prepare a concise explanation of why a common ROI is preferable for fair comparison;
- add case-specific refinement only if a hotspot leaves the common ROI or evidence shows numerical inconsistency.

## 5. Other feedback still open

### Baseline validation
Handled in the dedicated baseline workflow. Separate absolute 3-D reproduction limits from relative MEB-trend use of the common simplified 2-D model.

### 1T1C retention definition
Current wording remains limited to MixedMode / write feasibility. Required direction:

```text
Write → floating Hold → VSN(t) decay → pre-frozen retention criterion → optional Read
```

### Practical WL resistance / RC trade-off
Keep as a literature-supported practical consideration unless directly simulated.

## 6. Current guardrails

Avoid:

```text
48 nm is the global optimum MEB.
51 nm is physically bad.
Cgd reduction directly proves GIDL reduction causality.
1T1C retention has already been validated.
Word-line resistance increase was directly simulated.
The literature 3-D BCAT was fully reproduced electrically.
```

Use scoped wording:

- current baseline supports relative MEB-trend analysis under a common simplified 2-D model;
- completed E-field validation supports critical-region spatial E-field / BTBT interpretation rather than one peak-field scalar;
- ROI coverage is only a mesh-feedback checkpoint, not final mesh validation;
- the final objective remains an effective / defensible MEB design range.

## 7. README integration rule

Do **not** rewrite the main README after each individual feedback item. Final README integration is deferred until the principal first-presentation feedback set is complete so baseline, E-field/mesh, retention, and practical-trade-off wording can be synthesized consistently in one pass.
