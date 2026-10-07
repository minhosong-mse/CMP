# CMP Research Handoff

> Canonical session-handoff document.
>
> Read this after `AGENTS.md` at the start of a new CMP research session.
> Keep this file focused on the current state rather than accumulating full history.

**Last updated:** 2026-10-08

## 1. Canonical Research Topic

**20 nm급 BCAT DRAM에서 MEB 깊이에 따른 GIDL–Retention 전달 특성 및 온도 의존적 유효 설계 범위 도출**

Main design variable: **MEB depth**

Current main chain:

```text
MEB depth
→ gate–drain electrostatics / project-internal Cgd coupling
→ drain-side spatial E-field / BTBT distribution
→ terminal GIDL
→ temperature dependence
→ 1T1C Write / Hold / Read
→ retention translation
→ effective MEB design range
```

---

## 2. Current Main Lineage

### Active production lineage

`B0-2D-PAPER-CAL`

Frozen physical / calibration baseline:

`C7_4 / B_QF_HALF`

Frozen calibration coordinates:

- `GateCouplingScale = 2.300`
- `GateDepthBoost = 25 nm`
- `Qf_Int = 2.55e12 cm^-2`
- nominal `MEB / GateTop = 36 nm`
- calibration reference temperature: `300 K`
- PAPER-CAL BTBT lineage: `Hurkx`

These physical calibration coordinates remain locked.

### Historical / supporting lineages

- `B0-2D-Legacy` — historical R0–R7 evidence; preserve, do not convert absolute values into PAPER-CAL results.
- `3D-Sun-B0` — literature-consistent selected-point 3D fidelity anchor.
- Legacy main GIDL used `NonlocalPath`; active PAPER-CAL production uses `Hurkx`.

Do not mix absolute values across those lineages without a controlled bridge.

---

## 3. Current Stage

**300 K PAPER-CAL MEB Atlas — IN PROGRESS**

The previous mesh-debug loop has been closed for current production work.

A new common mesh family was executed and compared at 31 / 36 / 41 nm. The working production choice is:

- **MeshLevel 2 = production mesh**
- **MeshLevel 3 = finer convergence/reference mesh**
- no Level 4 planned

This mesh decision applies to the new 300 K MEB atlas. It does **not** retroactively rewrite the historical 2026-10-05 FZ-A/FZ-B/FZ-C freeze.

The current 300 K atlas is intended to close the transistor-level evidence before temperature and PAPER-CAL 1T1C work.

---

## 4. Last Completed Work

### 4.1 New mesh revalidation / production choice

The new mesh family uses:

- moderate global mesh;
- Si/SiO2 interface-following refinement;
- compact source/drain shoulder refinement;
- nested drain-side GIDL Outer / Mid / Core windows;
- MEB-following local windows rather than one fixed hotspot box.

Observed mesh sizes:

- Level 2 example: about `15,279 elements / 7,384 points`
- Level 3 example: about `18,333 elements / 8,869 points`
- Level 3 therefore costs about **20% more elements** than Level 2.

Level 2 → Level 3 numerical sensitivity:

| MEB | ΔGIDL | ΔBTBTmax | ΔE@BTBT | hotspot shift |
|---:|---:|---:|---:|---:|
| 31 nm | about -2.44% | about +3.56% | about +0.52% | about 0.29 nm |
| 36 nm | about -0.65% | about -1.20% | about -0.13% | 0 nm |
| 41 nm | about -0.52% | about -1.20% | about -0.22% | 0 nm |

Interpretation:

- 36 / 41 nm are clearly stable between Level 2 and Level 3.
- 31 nm terminal GIDL exceeds the earlier internal 2% guardrail slightly, but spatial metrics are stable.
- The extra ~20% element cost of Level 3 gives only small changes in the quantities relevant to the current MEB trend.
- For the current study, Level 2 is accepted as the **working production mesh**, with Level 3 retained as convergence evidence.

### 4.2 300 K MEB range expanded

The formal current sweep is:

```text
31 / 33 / 36 / 39 /
41 / 42 / 43 / 44 / 45 /
46 / 47 / 48 / 49 / 50 / 51 nm
```

Total: **15 MEB points**

Reason:

- preserve one shallow point below nominal;
- retain nominal / nearby reference points;
- resolve the deeper-MEB behavior densely;
- map the `GateTop ≈ Jdepth = 48 nm` model-internal boundary at 1 nm resolution;
- defer optional 0.5 nm / 0.1 nm refinement around the 48-nm neighborhood until the coarse atlas is analyzed.

Do not assume “deeper is always optimal.” The dense deep-MEB sweep is intended to identify plateau / knee / reversal / floor-sensitivity behavior.

### 4.3 Production simulation packages prepared

A common production SDE was prepared with:

- `MEBDepth` as the only SWB sweep parameter;
- `MeshLevel = 2` hard-coded;
- frozen PAPER-CAL geometry/calibration coordinates.

Four current 300 K simulation branches:

1. **DC-low**
   - `VD = 0.05 V`
   - `VG = 0 → 1.2 V`
   - outputs: Vth / SS / low-Vd current anchors

2. **DC-high**
   - `VD = 1.20 V`
   - `VG = 0 → 2.0 V`
   - outputs: Vth / SS / Id samples / Ion-Ioff
   - DIBL will be formed from DC-low + DC-high Vth

3. **GIDL / spatial**
   - `T = 300 K`
   - `VD = 1.20 V`
   - `VG = 0 → -0.70 V`
   - `Hurkx`
   - outputs: terminal GIDL, BTBTmax, Xhot, Yhot, E@BTBT
   - TDR stores `ElectricField/Vector` and `Band2BandGeneration` for later P2 post-processing

4. **Cgd / ACExtract**
   - `T = 300 K`
   - `VD = 1.20 V`
   - `VG = -0.71 → -0.69 V`, center `-0.70 V`
   - `f = 1 MHz`
   - BTBT OFF by frozen Cgd protocol
   - primary: `|c(g,d)|`
   - cross-check: `|c(d,g)|`
   - treat as a project-internal gate–drain small-signal coupling metric, not calibrated production-cell Cov

### 4.4 Execution status at session close

- **DC-low 15-point run:** launched by user; results pending
- **DC-high 15-point run:** launched by user; results pending
- **GIDL 15-point package:** prepared; execution/result return pending
- **Cgd 15-point package:** prepared; execution/result return pending

No 300 K atlas conclusion has been frozen yet because the batch results have not been returned/analyzed.

---

## 5. Active / Blocked Work

### Active work

Wait for the 15-point 300 K batch results, then build one unified MEB master table.

Required combined columns:

- MEB
- Vth @ 0.05 V
- Vth @ 1.20 V
- DIBL
- SS
- Ion / Ioff
- terminal GIDL
- Cgd raw metric
- BTBTmax
- Xhot / Yhot
- E@BTBT

Then add the P2 spatial metrics from the saved GIDL TDRs:

- integrated BTBT / spatial BTBT measure;
- 20%-criterion active width / area;
- common fixed-cut E-field profile / integral.

The current new PAPER-CAL result already shows that terminal GIDL can decrease while BTBT peak and E@BTBT increase, so peak-only interpretation is not sufficient.

### Provenance / documentation gap

The exact 2026-10-05 executed C7_4/FZ-C parent archive was not recovered into canonical GitHub during this session.

Therefore:

- do not rewrite the historical freeze as if the new mesh were the original FZ-C mesh;
- preserve the historical final-freeze record;
- record the new Level-2 mesh as a **new post-freeze production mesh branch** derived under the frozen PAPER-CAL calibration;
- synchronize code/evidence/HANDOFF after the current atlas results are available.

This is now a provenance/documentation gap rather than a reason to retune physical calibration.

---

## 6. Next Immediate Task

First action next session:

1. collect the completed **DC-low / DC-high / GIDL / Cgd** 15-point outputs;
2. verify all endpoint / bias / AC-point sanity flags;
3. merge the four branches into a single 300 K MEB table;
4. compute:
   - DIBL;
   - normalized GIDL and Cgd;
   - local MEB-to-MEB slope / knee behavior;
   - reciprocity error for Cgd;
5. run SVisual post-processing on saved GIDL TDRs for:
   - BTBT integral / distribution;
   - 20% active width / area;
   - common fixed-cut E profile / integral;
6. analyze the 48-nm neighborhood and decide whether a later 0.5 nm or 0.1 nm local MEB sweep is actually justified.

Only after the 300 K MEB atlas is closed:

```text
300 K MEB atlas
→ selected temperature GIDL/DC validation
→ PAPER-CAL 1T1C Write/Hold/Read
→ MEB × temperature × retention
→ effective MEB design range
```

---

## 7. Frozen / Working-Frozen Items

Do not change without an explicit new decision:

### Physical / calibration

- `B0-2D-PAPER-CAL = C7_4 / B_QF_HALF`
- `GateCouplingScale = 2.300`
- `GateDepthBoost = 25 nm`
- `Qf_Int = 2.55e12 cm^-2`
- Gate WF = `4.8 eV`
- active PAPER-CAL Hurkx lineage
- calibration reference `300 K`

### Numerical / protocol

- **working production mesh = MeshLevel 2**
- **fine reference = MeshLevel 3**
- current 15-point MEB set above
- GIDL: `VD=1.2 V`, `VG=-0.7 V`, Hurkx
- Cgd: `VD=1.2 V`, `VG=-0.70 V`, `1 MHz`, BTBT OFF
- Cgd primary metric = `|c(g,d)|`, cross-check = `|c(d,g)|`
- global point `Emax` remains secondary; do not use it as the sole mechanism metric

---

## 8. Do Not Reopen by Default

Unless new evidence specifically requires it, do not reopen:

- C6 / C7 calibration DOE
- C8 micro-fitting
- arbitrary physical Tox / WF / doping tuning
- Hurkx ↔ NonlocalPath switching
- Level 4 mesh refinement
- full-device over-refinement for the sake of a lower numerical delta
- Legacy absolute-value reuse in PAPER-CAL
- 3D / DWFG / refresh claims before the active 2D PAPER-CAL chain is closed

---

## 9. Active Guardrails

- The new mesh decision is a **numerical production choice**, not a new physical calibration.
- `GateCouplingScale`, `GateDepthBoost`, and `Qf_Int` retain reduced-order calibration meaning.
- Do not call Cgd a directly calibrated physical Cov.
- A single BTBT peak or E-field peak does not explain terminal GIDL by itself.
- 48 nm is a model-internal `GateTop≈Jdepth` boundary, not automatically a process optimum.
- The lowest terminal GIDL point is not automatically the final design optimum.
- Transistor-level GIDL improvement does not yet establish retention improvement.
- Legacy 1T1C results remain historical until PAPER-CAL 1T1C is executed.
- Short-time Hold is not physical retention time.
- Temperature and 1T1C are downstream of the current 300 K transistor-level atlas.

---

## 10. Read Next

At the next session start:

1. `AGENTS.md`
2. this `HANDOFF.md`
3. returned 300 K atlas outputs / CSVs
4. only if needed:
   - `docs/research/b0_2d_production_revalidation_plan.md`
   - `docs/research/b0_2d_final_freeze_plan.md`
   - `docs/progress/b0_2d_paper_cal_mesh_revalidation_20261007.md`
   - `docs/research/b0_2d_baseline_reconstruction_calibration.md`
   - `docs/MODEL_SCOPE.md`
   - `docs/research/CLAIM_EVIDENCE_MATRIX.md`

For syntax changes only, route through `TCAD_MANUAL_INDEX.md` to the matching T-2022.03 official manual section.

---

## 11. Next-Session Start Hint

```text
Read AGENTS.md
→ read HANDOFF.md
→ ingest completed 15-point DC / GIDL / Cgd outputs
→ build 300 K MEB master table
→ close P1/P2 transistor-level mechanism
→ decide whether 48-nm local refinement is needed
→ then move to temperature
```
