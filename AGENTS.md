# CMP Repository Agent Instructions

> Purpose: define how AI/agent sessions read, modify, and hand off the CMP research repository.
>
> This file is an operating rulebook. It should remain relatively stable and must not be used as a running research log.

## 1. Canonical Research Topic

**20 nm급 BCAT DRAM에서 MEB 깊이에 따른 GIDL–Retention 전달 특성 및 온도 의존적 유효 설계 범위 도출**

The main design variable is **MEB depth**.

Current research logic:

```text
MEB depth
→ gate–drain electrostatics / project-internal coupling
→ drain-side spatial E-field
→ BTBT / GIDL
→ 1T1C Write / Hold / Read
→ storage-node charge loss / retention
→ temperature-dependent translation
→ effective MEB design range
```

Temperature, DWFG, and selected-point 3D work are downstream validation axes unless the current handoff explicitly says otherwise.

---

## 2. Session Start Rule

Every new meaningful CMP research session must begin by reading:

1. `AGENTS.md`
2. `HANDOFF.md`

Use `AGENTS.md` to recover operating rules.

Use `HANDOFF.md` to recover:

- current active research lineage;
- current stage;
- last completed work;
- active / blocked work;
- next immediate task;
- frozen items;
- do-not-reopen items;
- active guardrails;
- read-next references.

After that, read **only the sources needed for the requested task**.

Do not open literature originals or TCAD manuals merely because a new session started. They are task-triggered sources.

Do not re-scan or reinterpret the full repository at the start of every session unless the requested task actually requires a repository-wide audit.

---

## 3. Source Authority

### Current CMP research state

Use the live `main` branch.

For current-stage questions, prefer:

1. current freeze / validation / close-out document;
2. `docs/RUN_SHEET.md`;
3. latest relevant commits;
4. `HANDOFF.md` for session continuity;
5. linked evidence / progress documents.

`README.md` is an external-facing summary and is **not** the running-state source of truth.

### Numerical results

Prefer:

1. `data/` processed/raw numerical evidence;
2. `docs/evidence/`;
3. `docs/progress/`;
4. summary documents.

Before editing a document containing numbers, compare the values against the underlying CSV/evidence.

### Research decisions

Use:

- `docs/DECISIONS.md`;
- the current freeze / validation document when a later explicit freeze supersedes an older planning state.

### Claim boundaries

Use:

- `docs/MODEL_SCOPE.md`;
- `docs/research/CLAIM_EVIDENCE_MATRIX.md`.

### Physical / literature rationale

Primary authority is the original paper available in the ChatGPT CMP Project.

`docs/literature/` and `docs/REFERENCES.md` are navigation and interpretation aids, not replacements for the original paper.

### Sentaurus syntax

The official manual matching the installed Sentaurus version is the final authority for syntax, command availability, solver options, model keywords, defaults, and version-specific behavior.

However, the manual is an **on-demand technical verification source**, not a default onboarding source.

Before opening a manual:

1. identify the target lineage and frozen items;
2. inspect the closest executed CMP deck;
3. determine whether the requested change actually introduces a syntax / option / model / solver / mesh question.

Open the relevant manual section when at least one of the following applies:

- a new command, keyword, or option is being introduced;
- an argument meaning or default behavior is unclear;
- solver / continuation / transient / mesh behavior is being changed;
- a physics model is being added or changed;
- a syntax, convergence, or version-compatibility problem must be diagnosed;
- the closest executed parent does not provide an equivalent implementation pattern.

Routine same-deck reruns, already validated parameter substitutions, CSV analysis, literature interpretation, presentation wording, and GitHub state maintenance do not require re-reading the manual.

Use the Project Source `TCAD_MANUAL_INDEX.md` to route to the relevant manual section when manual verification is needed.

Do not invent executable syntax when it is not verified in the relevant manual.

Do not automatically apply syntax from another Sentaurus release.

### Existing implementation

Use the **closest executed CMP deck** as the implementation parent.

---

## 4. Information Provenance and Status

Keep the following meanings distinct.

### Provenance

- **LIT-EXPLICIT** — directly stated in an original paper.
- **CMP-EXECUTED** — directly obtained from executed CMP simulation/data.
- **CMP-CALIBRATED** — frozen after CMP calibration/validation.
- **CMP-PROTOCOL** — project-internal condition, comparison rule, extraction definition, or method.
- **INFERRED** — interpretation not directly measured.
- **PLANNED** — not yet executed.
- **UNKNOWN** — not supported by the currently available sources.

### Maturity / role

Use when useful:

- **FROZEN**
- **VALIDATED**
- **PROVISIONAL**
- **HISTORICAL**
- **CONDITIONAL**
- **NOT-DEMONSTRATED**

Do not silently promote PLANNED, PROVISIONAL, or INFERRED information into executed/frozen results.

---

## 5. Model Lineage Protection

Do not silently mix absolute numerical results from different model / simulation lineages.

At minimum distinguish:

- `B0-2D-Legacy`
- `B0-2D-PAPER-CAL`
- `3D-Sun-B0`
- single-WF
- DWFG
- NonlocalPath
- Hurkx

Before quantitative comparison, verify:

- geometry lineage;
- calibration lineage;
- physics;
- BTBT model;
- mesh policy;
- bias;
- extraction definition;
- temperature;
- solver lineage.

Without a controlled bridge or same-condition comparison, do not combine absolute values from different lineages into one result set.

Historical results remain valid inside their original scope even after a newer lineage is created.

---

## 6. Calibration Discipline

Paper-explicit physical values and reduced-order CMP calibration coordinates are not interchangeable.

In particular, parameters such as:

- `GateCouplingScale`;
- `GateDepthBoost`;
- `Qf_Int`;

must retain their documented reduced-order calibration meaning.

Do not reinterpret them as fabricated oxide thickness, physical recess change, or literature-explicit fixed charge unless a source explicitly supports that interpretation.

---

## 7. Claim Discipline

Literature evidence does not replace CMP execution evidence.

Do not state the following as established CMP conclusions without corresponding CMP evidence:

- final optimum;
- global optimum;
- production optimum;
- robust process window;
- calibrated production value;
- retention improvement;
- refresh reduction;
- direct causality;
- 3D-equivalent;
- production DRAM equivalent.

Additional guardrails:

- correlation is not automatically causality;
- transistor-level GIDL improvement is not automatically retention improvement;
- short-time Hold behavior is not physical retention time;
- geometry-derived RWL proxy is not actual distributed WL resistance or RC delay;
- selected-point 3D validation is not full 3D equivalence;
- literature values are not CMP-calibrated values merely because they are reused.

When a claim is important, check `CLAIM_EVIDENCE_MATRIX.md` and `MODEL_SCOPE.md` before wording it.

---

## 8. TCAD Code Modification Workflow

When creating or modifying SDE / SDevice / SMesh / SVisual / SWB-related code:

1. identify the target lineage;
2. identify the closest executed parent deck;
3. check relevant frozen parameters / decisions;
4. determine whether a **manual verification trigger** exists;
5. if triggered, use `TCAD_MANUAL_INDEX.md` and verify only the relevant section of the official manual for the installed version;
6. make the minimum necessary change;
7. distinguish numerical-solver changes from physical-model changes;
8. preserve provenance;
9. do not pre-write a scientific conclusion before execution results exist.

A close executed parent is the first implementation reference. The manual is used when the requested change needs technical verification, not automatically for every routine code-associated task.

Do not retroactively rewrite a completed historical Run deck simply to match a later method.

If a production point fails numerically, inspect validated continuation / solver / mesh fallback before retuning frozen physical calibration parameters.

---

## 9. GitHub Modification Rules

Preserve historical integrity.

- Do not delete historical evidence just because a newer result exists.
- Do not rewrite old evidence to make it look as if a later method was used originally.
- New calibration / validation / model branches must declare their lineage.
- Update underlying code/data/evidence/research documents before updating README.
- Respect explicit user freezes such as “do not update README yet”.
- Keep scientific meaning changes separate from pure formatting cleanup whenever practical.
- One commit should represent one logical purpose.

If sources conflict, do not silently reconcile them. Record:

- the conflicting sources;
- which source is newer/stronger and why;
- whether the conflict is historical, superseded, or requires repository synchronization.

---

## 10. HANDOFF.md Policy

`HANDOFF.md` is the canonical **session-handoff** document.

It is not a full history.

Keep it short and current.

It should contain at least:

- Last updated
- Current main lineage
- Current stage
- Last completed work
- Active / blocked work
- Next immediate task
- Frozen items
- Do-not-reopen items
- Active guardrails
- Read-next references

At the end of a meaningful work session, update `HANDOFF.md` when the current state or next action changed.

If work stopped midway, record exactly:

- what completed;
- what remains;
- where it failed or paused;
- the next first action.

Do not mark provisional work as completed/frozen.

---

## 11. PROJECT_TIMELINE.md Policy

`PROJECT_TIMELINE.md` records **major research transitions**, not session activity.

Add an entry only for events such as:

- research topic/direction change;
- new model lineage;
- baseline freeze;
- metric / mesh / physics freeze;
- major DOE completion;
- candidate selection;
- presentation / mentor feedback that changes methodology;
- validation close-out;
- research-stage handoff;
- major final result.

Do not add entries for:

- routine reruns;
- solver retries;
- single CSV additions;
- screenshots;
- typo fixes;
- formatting cleanup.

Prefer the actual execution / decision / presentation date.

Do not assume commit timestamp equals experiment date.

If the exact date is not recoverable, use an approximate period or `date unresolved` rather than inventing a date.

Suggested statuses:

- Completed
- In Progress
- Planned
- Conditional
- Historical / Superseded

---

## 12. Session End Rule

When the user asks to close a research session and synchronize GitHub, first classify the stopping state as **completed**, **paused**, **failed**, or **provisional**.

Then:

1. verify what was actually executed and what result was obtained;
2. update necessary code / data / evidence / progress documents first;
3. record a new scientific decision in the relevant decision/freeze document only when the work actually changes a scientific decision;
4. update `HANDOFF.md` when the current state, blocker, or next action changed;
5. update `PROJECT_TIMELINE.md` only if a major research transition occurred;
6. commit changes in logical units;
7. confirm that the final `HANDOFF.md` next immediate task is the real first action for the next session.

If the work stopped midway, record exactly what completed, what remains, where it paused/failed, and the next first action.

Do not mark provisional or incomplete work as completed/frozen.

Do not update `PROJECT_TIMELINE.md` merely because a session ended.

Routine literature indexing, source housekeeping, formatting cleanup, or an ordinary rerun does not by itself change the research stage.
