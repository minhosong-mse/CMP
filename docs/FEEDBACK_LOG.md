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
| FB-EFIELD-01 | Presentation feedback | If the actual GIDL hotspot is known, should electric field be measured near the hotspot instead of only on a fixed X/Y cut? | Run 3, Run 5, Run 6.5 | `T-EFIELD-01` | **In Progress** | hotspot-based `E@BTBTmax` + fixed-cut cross-check |
| FB-MESH-01 | Presentation feedback | If MEB depth changes hotspot position, is one common hotspot mesh still valid for every MEB? | Run 3, Run 6.5 | `T-MESH-01` | Pending after E-field extraction | hotspot-coordinate plot + common-ROI margin audit; case-specific mesh only if needed |
| FB-BASELINE-01 | Presentation feedback | How closely does the simplified 2D B0 reproduce the literature 3D BCAT electrical characteristics? | Run 0–1 | `T-BASELINE-01` | Planned | Paper vs B0-v1 vs recalibrated B0-v2 table + explicit model-scope statement |
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
