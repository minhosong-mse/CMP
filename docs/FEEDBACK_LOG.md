# CMP FEEDBACK LOG

> Purpose: track mentor / presentation / review feedback that cuts across multiple Runs.
> Feedback is **not forced into Run chronology**. Each item links to the affected Run(s), task(s), and final evidence location.

## 1. Why this file exists

CMP results are organized mainly by Run (`Run 0`, `Run 1`, ...), but presentation feedback often targets a method or interpretation spanning several Runs.

Example:

- a baseline-calibration comment affects Run 0–1,
- an electric-field extraction comment affects Run 3 / Run 5 / Run 6.5,
- a retention-definition comment affects Run 7 and downstream Run 8–9,
- an RC trade-off comment affects interpretation of the MEB design range rather than one single simulation Run.

Therefore the feedback layer is maintained separately and **references** Run documents rather than duplicating them.

---

## 2. Feedback lifecycle

```text
Feedback received
→ FEEDBACK_LOG entry
→ TASK_HUB action item
→ analysis / simulation / post-processing in the relevant Run
→ curated evidence
→ final interpretation / slide update
→ feedback item closed
```

When a feedback item is resolved, the numerical result belongs in the relevant Run progress/evidence document. This file keeps only the review question, affected scope, action, and resolution link.

---

## 3. Active feedback matrix

| Feedback ID | Source / context | Feedback / question | Affected Run(s) | Task | Status | Resolution target |
|---|---|---|---|---|---|---|
| FB-EFIELD-01 | Presentation feedback | If the actual GIDL hotspot is known, should electric field be measured near the hotspot instead of only on a fixed X/Y cut? | Run 3, Run 4, Run 5 | `T-EFIELD-01` | **In Progress** | 31/36/41 nm hotspot-following spatial E-field/BTBT validation + fixed-cut cross-check |
| FB-MESH-01 | Presentation feedback | If MEB depth changes hotspot position, is one common hotspot mesh still valid for every MEB? | Run 3, Run 4 | `T-MESH-01` | Pending after E-field extraction | 31/36/41 hotspot-coordinate + common-ROI margin audit; re-mesh only if coverage is insufficient |
| FB-BASELINE-01 | Presentation feedback | How closely does the simplified 2D B0 reproduce the literature 3D BCAT electrical characteristics? | Run 0–1 | `T-BASELINE-01` | Planned / handled in parallel chat | Paper vs B0-v1 vs recalibrated B0-v2 table + explicit model-scope statement |
| FB-RET-01 | Presentation feedback | What exactly is the 1T1C retention measurement definition? | Run 7; downstream Run 8–9 | `T-RET-01` | In Progress elsewhere | Write → floating Hold → VSN decay → pre-frozen retention criterion → optional Read |
| FB-RC-01 | Presentation feedback | Does deeper metal etch-back introduce a practical DRAM trade-off such as increased word-line resistance / RC delay? | Run 6.5 interpretation; downstream design-range conclusion | future design-range synthesis | Open / literature-supported consideration | keep as unmodeled practical trade-off unless explicitly simulated |

---

## 4. Current interpretation guardrails from feedback

Until corresponding evidence is complete, avoid the following claims:

```text
48 nm is the global optimum MEB.
51 nm is physically bad.
Cgd reduction directly proves GIDL reduction causality.
1T1C retention has already been validated.
Word-line resistance increase was directly simulated in the current model.
The literature 3D BCAT was fully reproduced electrically.
```

Use scoped wording instead:

- current baseline supports **relative MEB trend analysis** under a common simplified 2D model,
- Run 7 has verified **MixedMode/write feasibility**, not full retention,
- hotspot-based field extraction and mesh validity are being rechecked after presentation feedback,
- deeper MEB may carry WL resistance / RC trade-offs in practical DRAM, but that penalty is not yet directly calculated in the present model,
- the design objective is an **effective / defensible MEB design range**, not a single absolute optimum based only on the lowest GIDL endpoint.

---

## 5. Image / slide evidence rule for feedback

Feedback resolution often produces many intermediate screenshots. Use three levels:

### Level A — chat/local only

- raw SVisual screenshots,
- repeated MEB screenshots while the method is still changing,
- failed / abandoned extraction attempts,
- UI guidance images.

### Level B — candidate presentation evidence

Keep locally or in chat until the slide structure is decided:

- representative hotspot images,
- mesh overlay candidates,
- comparison plots,
- timing diagrams.

### Level C — committed evidence

Commit only selected material that supports a final claim or backup answer:

- curated 2–3 representative spatial images where enough,
- consolidated numeric tables / CSV,
- final comparison plots,
- images actually selected for main / backup slides,
- evidence required to reproduce a formal statement.

If all MEB screenshots are needed for audit, they may be committed as an evidence set. If the coordinate table proves the same point, prefer the table plus representative images to reduce repository noise.

---

## 6. Presentation-centric organization

Do not rewrite Run documents for every presentation.

For each major presentation / mentor review, add a small section here only if useful:

```text
## Review YYYY-MM-DD — <presentation / mentor session>
- feedback received
- affected Runs
- spawned TASK_HUB items
- final slide changes
- status / resolution
```

The actual scientific result still lives under the affected Run.

This preserves both views:

```text
Run view       → what the research did in chronological simulation order
Feedback view  → why a method / claim was later revisited
Task view      → what is currently unfinished and where to resume
```

---

## Review 2026-09-10 — 1차 주제발표 후 피드백 대응

### Review scope

This review cycle records the major questions raised after the first topic presentation. It is a **validation and interpretation layer**, not a replacement for the main research flow. Numerical results produced while resolving these items remain in the affected Run progress/evidence files.

### 1. E-field / BTBT hotspot validation

Observed issue from the existing 31–41 nm mechanism-correlation stage:

```text
MEB 31 → 41 nm
GIDL endpoint decrease   ≈ 60.42%
fixed-cut E_wall,max decrease ≈ 1.69%
```

The purpose of this feedback task is **not** to force an electric-field metric to reproduce the GIDL percentage change. The goal is to determine whether the much larger terminal-GIDL change can be explained plausibly by the spatial E-field / BTBT behavior in the actual GIDL-critical region.

The literature audit completed before extraction showed a common methodology pattern:

```text
physical GIDL / critical region
→ spatial E-field profile / distribution
→ representative scalar metric if needed
→ terminal leakage comparison
```

For the current feedback-level validation, use the formal representative set:

```text
MEB = 31 / 36 / 41 nm
36 nm = nominal literature-based reference
31 / 41 nm = ±5 nm shallow / deeper screening points
```

Phase-A protocol to be applied consistently:

1. confirm the dominant BTBT lobe lies inside the common drain-side analysis/refinement area;
2. automatically locate the Band2BandGeneration maximum for each MEB;
3. create a hotspot-following X-direction depth cut at each case-specific `Y_hot`;
4. compare `|ElectricField-X|`, `Abs(ElectricField-V)`, and `Band2BandGeneration` along the same cut;
5. record hotspot coordinates, `BTBT_max`, hotspot-cut `E_x,peak`, peak location, and a low-cost `|E|@BTBTmax` cross-check;
6. compare those results with the existing fixed-cut `E_wall,max` and terminal `|Idrain| @ VG=-0.7 V`.

BTBT-active width and E-field integral are **conditional Phase-B metrics**. They are added only if the Phase-A peak/profile evidence still cannot explain the large field-vs-GIDL sensitivity mismatch. If activated, the active-region criterion must be frozen before looking for the threshold that best matches GIDL.

This work remains supporting validation. It does not reopen the full 43–51 nm design-range search.

### 2. Mesh validity under hotspot movement

The existing Mesh-GIDL definition uses a common drain-side local refinement region:

```text
X = 0.032–0.070 um
Y = 0.112–0.133 um
```

The feedback question is whether that common refinement remains valid when MEB changes and the hotspot moves.

Current feedback-level requirement:

- extract the 31/36/41 nm hotspot coordinates,
- verify all three lie inside the common refinement ROI,
- record distance / margin to the ROI boundaries,
- trigger re-meshing or deeper convergence work only if a hotspot approaches/exits the refined region or the spatial result becomes numerically questionable.

This is a practical presentation-feedback validation, not an absolute proof of BTBT mesh independence.

### 3. Baseline validation / literature comparison

The current B0 is a literature-based **simplified 2-D BCAT model**, whereas key reference papers use calibrated or more complete 3-D BCAT structures. Presentation feedback therefore requires a clearer separation between:

- absolute baseline reproduction, which is currently limited,
- relative MEB trend comparison under one common simplified model, which is the present research use case.

The baseline task is handled in a parallel workflow and should produce:

```text
Paper nominal / 3-D reference
vs
current B0-v1
vs
recalibrated B0-v2 if executed
```

with Vth / SS / Ion / DIBL and explicit model-scope statements. Until that closes, do not state that the literature 3-D BCAT has been fully reproduced electrically.

### 4. 1T1C retention definition

Run 7 has established initial MixedMode / write feasibility only. The presentation feedback requires the retention measurement definition to be frozen before downstream MEB retention comparison.

Required methodology direction:

```text
Write
→ storage node release / floating Hold
→ VSN(t) decay
→ pre-frozen retention criterion
→ optional Read guardrail
```

The exact write, hold, voltage-window, and retention criteria remain in the dedicated Run-7 workflow. Until the full hold/retention protocol is verified, wording must remain limited to **1T1C MixedMode / write feasibility** rather than validated retention improvement.

### 5. Practical WL resistance / RC trade-off

Literature indicates that increasing MEB / upper low-WF-gate thickness can reduce the remaining metal-gate volume and may increase word-line resistance / RC delay. This provides a practical reason why the deepest or minimum-GIDL point should not automatically be promoted as the final device optimum.

However, the present simplified 2-D CMP model has **not directly simulated WL resistance or WL RC delay**. Therefore this point remains a literature-supported design consideration for the final effective-MEB-range discussion, not a verified simulation result.

### Review-cycle status

```text
E-field / BTBT methodology review : completed → Phase-A extraction pending
Mesh hotspot-ROI validation       : pending Phase-A coordinates
Baseline comparison                : in progress / parallel workflow
1T1C retention definition          : in progress / Run 7 workflow
WL R / RC trade-off                : literature-supported open consideration
```

The main research direction remains unchanged. These tasks strengthen the evidential basis of specific interpretation links before the next presentation and later thesis-level synthesis.
