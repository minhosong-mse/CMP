# CMP Research Workflow Playbook

> Purpose: provide repeatable task-by-task operating workflows for CMP research sessions.
>
> This document complements `AGENTS.md`.
>
> - `AGENTS.md` = repository rules, source authority, lineage/claim protection
> - `HANDOFF.md` = current state and next immediate task
> - `PROJECT_TIMELINE.md` = major research transitions
> - **this file** = how to execute common research tasks consistently
>
> This is a stable workflow guide, not a running-state document. Current numerical values, active stage, and frozen parameters must be read from live GitHub sources.

---

## 1. Universal CMP Task Flow

For every meaningful CMP research task, use the following sequence.

```text
1. Read AGENTS.md
2. Read HANDOFF.md
3. Identify the exact task and target lineage
4. Read only the task-relevant GitHub sources
5. If coding is required, inspect the closest executed parent deck
6. If syntax/model/solver behavior is involved, check the official manual
7. State what is frozen and what may change
8. Perform the minimum necessary work
9. Validate the result against same-lineage evidence
10. Separate observation from interpretation
11. Update code/data/evidence/progress if the result is worth preserving
12. Update HANDOFF.md if the current state or next action changed
13. Update PROJECT_TIMELINE.md only for a major research transition
14. Commit in logical units when requested
```

Do not start a task by rebuilding the research context from README alone.

---

## 2. Task Scoping Before Work

Before executing any simulation, analysis, or code edit, answer the following internally.

### 2.1 What is the task?

Examples:

- new simulation
- production rerun
- numerical debugging
- mesh validation
- physical-model validation
- CSV/result analysis
- E-field / BTBT spatial analysis
- 1T1C / retention analysis
- literature comparison
- presentation / report preparation
- GitHub research close-out

### 2.2 What is the target lineage?

At minimum distinguish:

- `B0-2D-Legacy`
- `B0-2D-PAPER-CAL`
- `3D-Sun-B0`
- single-WF
- DWFG
- NonlocalPath
- Hurkx

If the lineage is unclear, resolve it before comparing absolute values or writing code.

### 2.3 What is frozen?

Check:

- `HANDOFF.md`
- current freeze / validation document
- `docs/DECISIONS.md`
- `docs/research/CMP_MASTER_PARAMETER_TABLE.md`

A numerical problem is not permission to retune a frozen physical calibration parameter.

### 2.4 What evidence will close the task?

Define before running:

- required outputs
- comparison reference
- pass/fail or acceptance criteria
- whether the result is exploratory, provisional, validated, or freeze-worthy

---

## 3. New Simulation / Production Rerun

Use this workflow when starting a new controlled simulation or production rerun.

```text
HANDOFF
→ current run / validation plan
→ frozen parameters
→ closest executed parent deck
→ official manual for the required feature
→ minimal deck change
→ run
→ numerical sanity
→ metric extraction
→ same-lineage comparison
→ evidence / decision
```

### Required checks before execution

Confirm:

- geometry lineage
- calibration lineage
- physics model
- BTBT model
- mesh level/policy
- bias
- temperature
- extraction definition
- solver lineage

### Code-edit rule

Do not write a fresh deck from memory when a close executed parent exists.

Prefer:

```text
executed parent
+ minimum required change
= new candidate deck
```

### Before interpreting the result

Verify:

- target bias was reached;
- solver completed as intended;
- requested outputs exist;
- no unexpected model/parameter substitution occurred;
- extraction uses the intended definition.

A converged run is not automatically a scientifically valid comparison.

---

## 4. TCAD Code Creation / Modification

Use this workflow for SDE, SDevice, SMesh, and SVisual-related code.

### 4.1 Authority order

```text
Research condition / frozen value
→ live GitHub

Existing implementation pattern
→ closest executed CMP deck

Syntax / option / model behavior
→ official manual for the installed version

Physical rationale
→ literature + CMP evidence
```

### 4.2 Required coding sequence

1. identify target lineage;
2. locate the closest executed parent deck;
3. identify frozen and editable parameters;
4. identify the exact feature that requires manual verification;
5. read only the relevant manual section;
6. make the minimum change;
7. explain the change as:
   - unchanged;
   - numerical-only change;
   - physical-model change;
   - extraction/output change;
8. do not predict a final scientific conclusion before execution.

### 4.3 Manual coverage

The intended CMP Project manual set currently includes:

- SDE
- SDevice
- SMesh
- SVisual

A separate manual index will map common CMP tasks to the relevant manual sections after the manuals are added to the Project.

If the necessary syntax is not covered by an available official manual:

- do not invent it;
- use an already executed CMP pattern only when the context is equivalent;
- otherwise mark the syntax as **needs verification**.

### 4.4 Historical code protection

Do not modify completed historical decks in place to make them look like the current method.

If a historical deck must be adapted:

```text
historical parent
→ new clearly named derived deck
→ preserve parent
```

---

## 5. Numerical Debugging / Convergence Failure

When a simulation fails, separate numerical failure from physical-model failure.

### First-pass diagnosis

Check:

1. exact failure point in the log;
2. whether requested bias was reached;
3. Newton / continuation / MinStep behavior;
4. whether the failure is candidate-specific or common;
5. whether the same physics succeeded in the parent/reference deck;
6. current approved fallback solver policy.

### Modification order

Prefer:

```text
continuation / stepping
→ solver fallback already validated in the lineage
→ mesh review if evidence points to mesh
→ model/syntax review
→ physical parameter change only with a scientific reason
```

Do not use a physical calibration parameter as a numerical convergence knob.

### Result classification

A solver workaround is:

- **numerical change** if physics/geometry/calibration remain unchanged;
- **physical-model change** if model equations, mobility, BTBT, recombination, geometry, doping, or calibrated electrostatics change.

Keep these categories separate in documentation and commits.

---

## 6. Result / CSV Analysis

Do not start by plotting everything.

First build a comparison identity.

### 6.1 Comparison identity

Record:

- run / stage;
- model lineage;
- geometry / MEB;
- temperature;
- bias;
- physics / BTBT model;
- mesh;
- solver branch;
- extraction definition;
- source file / node if available.

Only then compare cases.

### 6.2 Numerical result priority

Use:

```text
processed/raw CSV
→ curated evidence
→ progress document
→ summary
```

If a summary disagrees with the CSV, do not silently preserve the summary value.

### 6.3 Analysis output structure

Separate:

**CMP-EXECUTED**
- directly measured/extracted result

**CMP-CALIBRATED / CMP-PROTOCOL**
- frozen calibration/protocol fact if relevant

**INFERRED**
- interpretation

**NOT YET SUPPORTED**
- tempting but unproven conclusion

Example:

```text
CMP-EXECUTED:
31→41 nm GIDL decreased under the tested lineage.

INFERRED:
The change is consistent with redistribution of the tunneling-favorable field region.

NOT YET SUPPORTED:
This proves the same percentage improvement in 1T1C retention.
```

---

## 7. Electric-Field / BTBT / GIDL Spatial Analysis

Do not reduce the mechanism to one local peak field unless the evidence explicitly supports that simplification.

Recommended CMP analysis sequence:

```text
terminal leakage
→ Band2BandGeneration distribution
→ hotspot location
→ E-field at / around the BTBT-critical region
→ common-cut comparison when needed
→ active-region width / integrated quantities when needed
→ same-lineage mechanism wording
```

### Required distinctions

Keep separate:

- terminal current;
- `BTBTmax`;
- hotspot coordinates;
- `E@BTBT`;
- fixed-cut field;
- global `Emax`;
- integrated field / integrated BTBT proxy.

One quantity is not automatically interchangeable with another.

### Current interpretation guardrail

A local point `Emax` or fixed-cut peak alone must not be used to claim complete direct causality for terminal GIDL.

Spatial redistribution and the tunneling-favorable region must be considered when the evidence requires it.

---

## 8. Mesh Validation

Mesh validation must match the claim being made.

### Coverage / comparison-consistency claim

Requires evidence that:

- the same mesh policy is applied across compared cases;
- the relevant critical region remains covered;
- hotspot motion does not leave the refinement domain.

### Absolute mesh-convergence claim

Requires an explicit convergence comparison.

Do not upgrade a common-ROI coverage audit into proof of universal mesh independence.

### Mesh work sequence

```text
identify target metric
→ identify critical region
→ compare mesh policy / spacing as required
→ quantify metric sensitivity
→ freeze only within the tested scope
```

---

## 9. 1T1C / Retention Work

Keep transistor-level and cell-level conclusions separate.

### Required hierarchy

```text
device leakage behavior
→ circuit connection / operation feasibility
→ Write
→ floating Hold
→ Read
→ retention metric
→ MEB-to-retention comparison
→ temperature-dependent translation
```

Do not skip directly from GIDL suppression to a retention-improvement claim.

### Short-Hold guardrail

Short-time `VSN(t)` decay may be used as a transient trend / sanity check.

It must not be extrapolated into a physical retention time unless a validated retention methodology supports that conversion.

### Before comparing retention

Confirm:

- same cell topology;
- same capacitance / AreaFactor policy;
- same write normalization logic;
- same hold definition;
- same retention criterion;
- same numerical convergence policy;
- same active model lineage.

---

## 10. Literature Review Workflow

The original paper is the authority for paper-specific claims.

For each paper, extract in this order:

1. bibliographic identity;
2. device / node / structure;
3. geometry and simulation conditions that are explicitly stated;
4. physics / models explicitly stated;
5. main result;
6. direct CMP relevance;
7. reusable methodology or trend;
8. non-transferable values / assumptions;
9. claim boundary for CMP;
10. pages / figures / tables supporting important facts.

Label paper-derived information as **LIT-EXPLICIT** only when directly supported by the source.

Do not infer unpublished TCAD syntax, calibration, bias, geometry, or process conditions from a figure alone unless clearly marked as inference.

The planned `LITERATURE_MASTER.md` should serve as the high-level AI literature map; individual detailed literature notes can remain backend references.

---

## 11. Literature-to-CMP Comparison

Before using a paper result in CMP, compare:

- technology node;
- geometry;
- gate scheme;
- doping;
- work function;
- oxide;
- BTBT / transport physics;
- dimensionality;
- bias;
- extraction definition;
- temperature;
- calibration status.

Classify the reuse as one of:

- **physical rationale**
- **methodology precedent**
- **qualitative trend comparison**
- **numerical target / calibration anchor**
- **novelty boundary**
- **claim boundary**

Do not transfer an absolute optimum or production value merely because a trend is similar.

---

## 12. Presentation / Report Preparation

Do not build a scientific slide or report section from README alone.

Recommended source flow:

```text
current evidence / data
→ claim-evidence matrix
→ model scope
→ current research direction
→ literature context
→ presentation wording
```

Each important slide/section should make clear what is:

- CMP executed result;
- literature context;
- CMP interpretation;
- planned work.

### Safe wording discipline

Use language consistent with evidence maturity.

Prefer:

- “under the current CMP model”
- “within the tested range”
- “supports”
- “is consistent with”
- “candidate”
- “effective/usable range” only when corresponding guardrails are actually evaluated

Avoid unsupported escalation to:

- final/global/production optimum;
- robust process window;
- direct causality;
- calibrated production retention;
- production-equivalent 3D behavior.

---

## 13. Decision Recording

Create or update a research decision only when the work changes one of the following:

- frozen parameter;
- accepted methodology;
- metric definition;
- model lineage;
- solver/mesh policy with continuing effect;
- candidate selection;
- claim boundary;
- downstream research direction.

Do not create a formal decision merely because a run completed.

A decision should record:

- question;
- options considered;
- evidence;
- decision;
- scope;
- effect on future work.

---

## 14. Evidence Packaging

A result worth preserving should be traceable.

Prefer an evidence package that includes as applicable:

- exact source deck or generator;
- node/run provenance;
- raw or processed CSV;
- extraction method;
- compact numerical summary;
- figure used for communication;
- interpretation and scope boundary.

Do not rely on screenshots alone when a numerical source exists.

Do not delete superseded evidence; mark it historical or superseded when appropriate.

---

## 15. GitHub Synchronization at Task End

When a task is completed or paused:

### If the task is still incomplete

Update only what is justified.

```text
executed code/data/evidence if worth preserving
→ HANDOFF active/blocked state
→ next immediate action
→ commit if requested
```

Do not mark the task completed or add a timeline milestone.

### If the task is completed

```text
verify result
→ code/data/evidence/progress
→ decision/freeze if scientifically necessary
→ HANDOFF
→ PROJECT_TIMELINE only if milestone
→ logical commits
```

### README rule

README is not the research notebook.

Update it only when the underlying evidence/research documentation is already synchronized and the current user-defined freeze allows it.

---

## 16. Session Start / End Prompts

### Standard session start

```text
CMP에서 [작업명] 진행할 거야.
AGENTS.md와 HANDOFF.md를 읽고 현재 상태를 파악한 뒤
이번 작업에 필요한 자료만 추가로 읽어서 준비해.
아직 수정/실행하지 말고 target lineage, frozen items,
필요 자료, 진행 순서를 먼저 정리해.
```

### Resume interrupted work

```text
CMP 연구 이어갈 거야.
AGENTS.md와 HANDOFF.md를 읽고 직전 중단 지점부터 준비해.
```

### Code-work start

```text
CMP에서 [SDE/SDevice/SMesh/SVisual] 코드 작업할 거야.
AGENTS/HANDOFF에서 target lineage와 frozen items를 확인하고,
closest executed parent와 Project의 공식 manual을 확인한 뒤
최소 변경안을 먼저 제시해.
```

### Pause incomplete work

```text
오늘은 여기까지.
미완료 상태로 실제 완료된 것, 실패/보류된 것,
다음 첫 작업을 정리하고 필요한 evidence와 HANDOFF를 업데이트해.
milestone이 아니면 PROJECT_TIMELINE은 수정하지 마.
```

### Complete a task

```text
이번 작업은 완료로 정리하자.
결과 재검증 → 필요한 code/data/evidence/progress 정리
→ 새 scientific decision이 있으면 반영
→ HANDOFF 갱신
→ milestone이면 PROJECT_TIMELINE 추가
→ 논리 단위별 commit까지 진행해.
```

---

## 17. Stop Conditions

Stop and request verification rather than guessing when:

- target lineage is ambiguous;
- relevant source values conflict without a clear authority;
- exact paper detail is absent from the literature source;
- syntax is not verified in an available official manual;
- the proposed change would reopen a frozen calibration without explicit authorization;
- the available evidence cannot support the requested claim;
- a numerical failure would require an unplanned physical-model change.

Uncertainty should remain explicit rather than being silently filled with general knowledge.
