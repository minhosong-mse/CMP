# CMP Research Handoff

> Canonical session-handoff document.
>
> Read this after `AGENTS.md` at the start of a new CMP research session.
> Keep this file focused on the current state rather than accumulating full history.

**Last updated:** 2026-10-06

## 1. Canonical Research Topic

**20 nm급 BCAT DRAM에서 MEB 깊이에 따른 GIDL–Retention 전달 특성 및 온도 의존적 유효 설계 범위 도출**

Main design variable: **MEB depth**

---

## 2. Current Main Lineage

### Active production lineage

`B0-2D-PAPER-CAL`

Frozen baseline:

`C7_4 / B_QF_HALF`

Frozen calibration coordinates:

- `GateCouplingScale = 2.300`
- `GateDepthBoost = 25 nm`
- `Qf_Int = 2.55e12 cm^-2`
- nominal `MEB / GateTop = 36 nm`
- calibration reference temperature: `300 K`

### Historical / supporting lineages

- `B0-2D-Legacy` — historical R0–R7 development/evidence; preserve, do not convert into PAPER-CAL results.
- `3D-Sun-B0` — literature-consistent 3D fidelity / selected-point validation anchor; not exact Sun electrical calibration.
- Legacy GIDL mainline used `NonlocalPath`; paper-grounded calibration/revalidation lineage uses `Hurkx` where defined by the current branch.

Do not directly mix absolute GIDL / BTBT values across those physics/model lineages.

---

## 3. Current Stage

**Post-calibration production revalidation opened.**

The paper-grounded 2D calibration branch was closed and frozen on 2026-10-05.

Current sequence of record:

```text
P0 runtime-equivalence benchmark
→ P1 calibrated MEB 31 / 36 / 41 @ 300 K
→ P2 fixed-cut / BTBT mechanism extraction
→ P3 calibrated 233 / 300 / 340 / 380 K GIDL matrix
→ P4 temperature DC guardrails only where needed
→ P5 GIDL → 1T1C retention
→ P6 effective MEB design range
```

Calibration knobs are locked. This sequence is a production revalidation / translation stage, not another fitting stage.

---

## 4. Last Completed Work

### B0-2D-PAPER-CAL final freeze — PASS / CLOSED

Frozen candidate:

`C7_4 / B_QF_HALF`

Final validation:

- **FZ-A solver-path consistency:** PASS
- **FZ-B DC mesh convergence:** PASS
- **FZ-C GIDL / BTBT / local-E convergence:** PASS

Reference values under the standardized final solver:

- `Vth @0.05 V ≈ 0.682485 V`
- `Vth @1.20 V ≈ 0.65570 V`
- `SSquick @1.20 V ≈ 75.827 mV/dec`
- `DIBL 0.05→1.20 V ≈ 23.29 mV/V`

Frozen numerical policy:

- broad DC sweep → `MeshLevel 0`
- broad GIDL sweep → `MeshLevel 1`
- selected mechanism / final evidence → `MeshLevel 2`
- `Rescue V2` → reference / fallback solver
- global point `Emax` → secondary diagnostic, not a primary mechanism metric

No C8 micro-fitting is open.

---

## 5. Active / Blocked Work

### Active

Production revalidation is the next active research branch.

### Not yet executed in this stage

The immediate P0 runtime-equivalence benchmark has not yet been recorded as completed in the repository.

### Legacy retention state to preserve separately

The historical `B0-2D-Legacy` Run-7 branch already demonstrated:

- 300 K Write→Hold→Read operation under the tested protocol;
- approximately normalized 300 / 340 / 380 K direct-Hold comparison;
- short-window temperature-dependent Hold trend.

However:

- the final physical retention metric was not closed before the paper-calibrated lineage became the active production baseline;
- these Legacy results must not be presented as calibrated PAPER-CAL retention results.

---

## 6. Next Immediate Task

Run the **one-point runtime-equivalence benchmark** before bulk calibrated MEB revalidation.

Nominal benchmark:

- `MEB = 36 nm`
- `T = 300 K`
- `Vd = 1.2 V`
- `MeshLevel = 0`

Compare a relaxed **PROD-STANDARD** continuation against the frozen **Rescue V2** reference.

Acceptance criteria:

- `BiasReached = 1`
- `Vth_CC_Reached = 1`
- `|ΔVth| ≤ 1 mV`
- `|ΔSSquick| ≤ 0.3 mV/dec`
- `ΔId@Vg2 ≤ 2%`
- runtime preferably at least 2× faster

If PASS:

use PROD-STANDARD for routine production DC.

If FAIL:

use Rescue V2 for that branch before considering any other numerical change.

Do **not** retune `GateCouplingScale`, `GateDepthBoost`, or `Qf_Int`.

---

## 7. Frozen Items

Do not change without an explicit new research decision:

- `B0-2D-PAPER-CAL = C7_4 / B_QF_HALF`
- `GateCouplingScale = 2.300`
- `GateDepthBoost = 25 nm`
- `Qf_Int = 2.55e12 cm^-2`
- physical paper-explicit baseline values used by the reconstruction
- current extraction definitions
- current PAPER-CAL physics lineage
- final mesh policy described above

Runtime optimization is allowed only through validated numerical solver / mesh policy without changing the frozen physical calibration.

---

## 8. Do Not Reopen by Default

The following branches are closed unless new evidence creates a specific reason to reopen them:

- C6 / C7 calibration DOE
- C8 micro-fitting
- domain-size convergence sweep
- low-Vd DIBL splitting
- Hurkx ↔ NonlocalPath bridge
- GaussFactor / setback exploratory dead ends
- arbitrary WF / physical Tox / doping tuning to force paper agreement
- full Mesh2 production matrix

Do not repeat a closed study merely because a new session started.

---

## 9. Active Guardrails

- Paper physical values are not the same as reduced-order calibration coordinates.
- `GateCouplingScale` is not fabricated oxide thickness.
- `GateDepthBoost` is not a claimed physical recess increase.
- `Qf_Int` is not a literature-explicit interface-charge value.
- Do not mix Legacy NonlocalPath absolute values with PAPER-CAL Hurkx absolute values.
- A single local peak E-field is not sufficient to explain the complete GIDL mechanism.
- `global Emax` is secondary because of corner/interface mesh sensitivity.
- Transistor-level GIDL improvement does not yet equal calibrated 1T1C retention improvement.
- Short-time Hold results are not physical retention time.
- The geometry-derived RWL result is a proxy, not actual distributed WL-R/RC.
- `233 K`, DWFG transferability, and selected-point final 3D validation remain downstream until executed in the active lineage.

---

## 10. Read Next

### For the immediate production rerun

- `docs/research/b0_2d_production_revalidation_plan.md`
- `docs/research/b0_2d_final_freeze_plan.md`
- `docs/RUN_SHEET.md`

### For calibration provenance

- `docs/research/b0_2d_baseline_reconstruction_calibration.md`

### For parameters / execution lineage

- `docs/research/CMP_MASTER_PARAMETER_TABLE.md`
- `CMD_HUB.md`
- relevant `code/sde/` and `code/sdevice/` parent decks

### For claim boundaries

- `docs/MODEL_SCOPE.md`
- `docs/research/CLAIM_EVIDENCE_MATRIX.md`

### For historical Legacy retention

- `docs/progress/run07_1t1c_retention_feasibility.md`
- `docs/evidence/run07_cell_operation_checkpoint_20260920.md`
- `docs/evidence/run07_hold_temperature_normalized_20260921.md`
- `docs/evidence/run07_whr_temperature_normalized_20260923.md`

---

## 11. Next-Session Start Hint

A new session should normally be able to begin from:

```text
Read AGENTS.md
→ read HANDOFF.md
→ read only the documents required by the requested task
→ continue from "Next Immediate Task"
```
