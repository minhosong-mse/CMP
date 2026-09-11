# CMP FEEDBACK LOG

> Purpose: track mentor / presentation / review feedback that cuts across multiple Runs.
> Feedback is **not forced into Run chronology**. Each item links to the affected Run(s), task(s), and final evidence location.

## 1. Why this file exists

CMP results are organized mainly by Run (`Run 0`, `Run 1`, ...), but presentation feedback often targets a method or interpretation spanning several Runs.

Examples:

- baseline calibration affects Run 0–1,
- E-field extraction affects Run 3–5,
- retention definition affects Run 7 and downstream Run 8–9,
- RC trade-off affects final MEB-range interpretation rather than one simulation Run.

The feedback layer therefore references the formal Run records rather than replacing them.

---

## 2. Feedback lifecycle

```text
Feedback received
→ FEEDBACK_LOG entry
→ TASK_HUB action item
→ analysis / simulation / post-processing
→ curated evidence
→ final interpretation / slide update
→ feedback item closed
```

---

## 3. Feedback matrix

| Feedback ID | Source / context | Feedback / question | Affected Run(s) | Task | Status | Resolution / target |
|---|---|---|---|---|---|---|
| FB-EFIELD-01 | First topic presentation | If the actual GIDL hotspot is known, should electric field be evaluated in the actual BTBT-critical region rather than only on the old fixed cut, and can spatial field / BTBT behavior explain the large GIDL-vs-field sensitivity mismatch? | Run 3, Run 4, Run 5 | `T-EFIELD-01` | **Resolved — feedback level** | 31/36/41 hotspot-following Phase A + conditional Phase B completed. Evidence: [`feedback_efield_hotspot_validation_20260911.md`](evidence/feedback_efield_hotspot_validation_20260911.md) |
| FB-MESH-01 | First topic presentation | If MEB changes hotspot position, is one common hotspot refinement region still valid? | Run 3, Run 4 | `T-MESH-01` | **Resolved — feedback level** | 31/36/41 hotspots all remain inside common ROI with comfortable margins; no re-mesh required for this validation set. Same evidence document + ROI figure |
| FB-BASELINE-01 | First topic presentation | How closely does the simplified 2-D B0 reproduce the literature 3-D BCAT electrical characteristics? | Run 0–1 | `T-BASELINE-01` | **In Progress elsewhere** | Paper vs B0-v1 vs recalibrated B0-v2 comparison + explicit model-scope statement |
| FB-RET-01 | First topic presentation | What exactly is the 1T1C retention measurement definition? | Run 7; downstream Run 8–9 | `T-RET-01` | **In Progress elsewhere** | Write → floating Hold → VSN decay → pre-frozen retention criterion → optional Read |
| FB-RC-01 | First topic presentation | Does deeper metal etch-back introduce a practical trade-off such as increased word-line resistance / RC delay? | Run 6.5 interpretation; downstream design-range conclusion | future synthesis | **Open / literature-supported consideration** | keep as an unmodeled practical trade-off unless directly simulated |

---

## 4. Resolved feedback — E-field / BTBT critical-region validation

### Original issue

Formal Run 5 showed:

```text
MEB 31 → 41 nm
GIDL endpoint decrease          ≈ 60.42%
fixed-cut E_wall,max decrease   ≈ 1.69%
```

The purpose of the feedback work was **not** to find a field metric that numerically reproduces the GIDL percentage. It was to test whether the terminal trend can be interpreted more defensibly from the spatial E-field / BTBT behavior in the actual GIDL-critical region.

### Literature-grounded method choice

Five BCAT / DRAM leakage papers were reviewed before extraction. The common analysis logic was summarized as:

```text
physical GIDL / leakage critical region
→ spatial E-field profile or map
→ representative peak / region metric when useful
→ terminal leakage / retention comparison
```

CMP-specific reproducibility additions:

- automatic `Band2BandGeneration`-maximum localization;
- common ROI + case-specific hotspot-following cut;
- normalized `G/Gmax = 10/20/50%` sensitivity if peak-only evidence is insufficient.

These CMP implementation choices are **not** claimed as universal literature standards.

### Frozen validation set

```text
MEB       = 31 / 36 / 41 nm
Mesh_Code = 3
T         = 300 K
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2Band(Model=NonlocalPath)
GIDL      = |Idrain| @ VG=-0.7 V
```

### Completed extraction

For all three cases:

- full-Si `BTBT_max`, `X_hot`, `Y_hot` automatically extracted;
- common Mesh-GIDL ROI coverage checked;
- X-direction cut created at case-specific `Y_hot`;
- `Band2BandGeneration`, `ElectricField-X`, `Abs(ElectricField-V)` profiles exported;
- profile / peak results compared with old `E_wall,max` and terminal GIDL.

All three cases produced:

```text
Y_hot = 0.121875 um
```

Phase B was activated because `ElectricField-X` peak did not decrease with GIDL.

### Main quantitative result

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

Threshold sensitivity:

- 10%, 20%, and 50% normalized BTBT criteria all retain the same decreasing active-width and integrated-field trend;
- the 20% criterion is retained only as a representative middle value, not a universal standard.

### Resolved interpretation

> The large MEB-dependent GIDL reduction is not adequately represented by a single local E-field maximum. Across 31/36/41 nm, BTBT-generation amplitude and active spatial extent decrease, and the field integrated over the BTBT-active region also decreases. The spatially integrated BTBT-generation trend is consistent with the terminal GIDL reduction. The mechanism is therefore more defensibly discussed from the **critical-region spatial E-field / BTBT distribution** than from one peak-field scalar.

Interpretation boundary:

- this does not prove a direct `Cgd → E-field → GIDL` causal law;
- the 1-D BTBT generation integral is not a terminal-current calculation;
- absolute BTBT calibration remains outside the current scope.

Evidence / reusable data:

```text
docs/evidence/feedback_efield_hotspot_validation_20260911.md

data/run05/feedback_efield_20260911/
  README.md
  efield_btbt_validation_summary.csv
  btbt_threshold_sensitivity.csv
  btbt_profiles_31_36_41.csv
  abse_profiles_31_36_41.csv
  ex_profiles_31_36_41.csv

assets/images/feedback/20260911_efield/
  01_btbt_profiles.svg
  02_abse_profiles.svg
  03_normalized_metric_trends.svg
  04_threshold_width_sensitivity.svg
  05_integrated_field_sensitivity.svg
  06_hotspot_roi_coverage.svg
```

---

## 5. Resolved feedback — common Mesh-GIDL ROI coverage

Existing local refinement ROI:

```text
X = 0.032–0.070 um
Y = 0.112–0.133 um
```

Extracted hotspot coordinates:

| MEB | Xhot (um) | Yhot (um) | X-low margin (nm) | X-high margin (nm) | Y-low margin (nm) | Y-high margin (nm) |
|---:|---:|---:|---:|---:|---:|---:|
| 31 | 0.051562496 | 0.121875 | 19.562 | 18.438 | 9.875 | 11.125 |
| 36 | 0.051562496 | 0.121875 | 19.562 | 18.438 | 9.875 | 11.125 |
| 41 | 0.052343745 | 0.121875 | 20.344 | 17.656 | 9.875 | 11.125 |

Feedback-level conclusion:

- all 31/36/41 hotspots remain comfortably inside the common local refinement region;
- hotspot movement is small over this set;
- no re-mesh is required for this presentation-feedback validation.

This remains a **coverage audit**, not proof of absolute BTBT mesh independence.

---

## 6. Feedback items still open

### Baseline validation

Need a clear separation between:

- absolute literature-3D reproduction, which is currently limited;
- relative MEB trend comparison under a common simplified 2-D model, which is the present use case.

Handled in the dedicated baseline workflow.

### 1T1C retention definition

Current status remains limited to MixedMode / write feasibility. Full feedback resolution requires:

```text
Write
→ floating Hold
→ VSN(t) decay
→ pre-frozen retention criterion
→ optional Read guardrail
```

Handled in the dedicated Run-7 workflow.

### Practical WL resistance / RC trade-off

Literature supports a possible practical trade-off from reduced remaining metal-gate volume as MEB becomes deeper. The present simplified 2-D model has not directly simulated WL resistance or RC delay, so this remains a literature-supported design consideration only.

---

## 7. Current interpretation guardrails

Avoid the following claims until their corresponding evidence exists:

```text
48 nm is the global optimum MEB.
51 nm is physically bad.
Cgd reduction directly proves GIDL reduction causality.
1T1C retention has already been validated.
Word-line resistance increase was directly simulated in the current model.
The literature 3-D BCAT was fully reproduced electrically.
```

Use scoped wording instead:

- current baseline supports relative MEB trend analysis under a common simplified 2-D model;
- Run 7 has verified MixedMode / write feasibility, not full retention;
- the completed E-field feedback validation supports critical-region spatial E-field / BTBT interpretation rather than one peak-field scalar;
- deeper MEB may carry WL resistance / RC trade-offs in practical DRAM, but that penalty is not directly calculated here;
- the design objective remains an **effective / defensible MEB design range**, not a single absolute optimum selected only from minimum GIDL.

---

## 8. README integration rule

Do **not** rewrite the main README after each individual feedback item. Final README integration is deferred until the principal first-presentation feedback set is complete so baseline, E-field/mesh, retention, and practical trade-off wording can be synthesized consistently in one pass.
