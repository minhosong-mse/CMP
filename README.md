# CMP: GIDL–Retention Translation and Temperature-Dependent MEB Design Range in 20 nm-Class BCAT DRAM

> **Canonical research topic**  
> **20 nm급 BCAT DRAM에서 MEB 깊이에 따른 GIDL–Retention 전달 특성 및 온도 의존적 유효 설계 범위 도출**  
> **Temperature-Dependent Effective MEB Design Range Based on GIDL-to-Retention Translation in 20 nm-Class BCAT DRAM**
>
> **Project status:** R0–R6.5 transistor-level mainline completed; first-presentation feedback package substantially closed; Run 7 advanced cell-operation / retention-metric stage in progress  
> **Main DOE model:** B0 — 20 nm-class simplified 2D single-WF BCAT  
> **Validation anchor:** 3D-Sun-B0 — literature-consistent 3D BCAT reconstruction  
> **Tool:** Synopsys Sentaurus TCAD T-2022.03

```text
MEB Depth
→ Cgd / gate-drain coupling
→ hotspot-resolved E-field
→ BTBT / GIDL
→ 1T1C retention translation
→ write/read + structural guardrails
→ effective MEB design range
```

The project does **not** aim to select one minimum-GIDL point. The final target is a **usable MEB design range** that remains defensible when cell-level retention, write/read feasibility, temperature, word-line structural penalty, selected-point 3D validation, and—when executed—DWFG transferability are considered together.

---

## 1. Project Overview

CMP(Chips Master Program)는 첨단분야 혁신융합대학사업단과 숭실대학교 차세대반도체학과가 운영하는 장기 실무형 프로젝트입니다.

- **Activity period:** 2026.04–2027.01
- **Main area:** DRAM cell transistor / BCAT / TCAD / GIDL / retention / MEB design range
- **Current baseline gate scheme:** single-work-function W, 4.8 eV
- **Nominal B0 MEB:** 36 nm
- **Historical candidate P1:** 41 nm
- **Cell-validation handoff candidate P2:** 48 nm
- **Primary challenger:** 49 nm
- **Current research focus:** transistor-level MEB/GIDL benefit이 실제 1T1C storage-node behavior와 usable cell-level range로 얼마나 전달되는지 검증

Execution references:

- [TCAD CMD / Parameter Hub](CMD_HUB.md)
- [Current Run Sheet](docs/RUN_SHEET.md)
- [Master Parameter Table](docs/research/CMP_MASTER_PARAMETER_TABLE.md)
- [Model Scope](docs/MODEL_SCOPE.md)
- [Claim–Evidence Matrix](docs/research/CLAIM_EVIDENCE_MATRIX.md)

---

## 2. Research Evolution

### 2.1 Initial context

The project began from a broader HBM / DRAM reliability and advanced-memory context. The initial question space included high-density DRAM scaling, leakage, retention, and advanced integration.

### 2.2 Narrowing after the first topic cycle

To obtain a cleaner device-level causal chain and a controllable TCAD design variable, the scope was narrowed to BCAT and MEB-dependent GIDL.

The research flow became:

```text
MEB
→ Cgd
→ drain-side electric field
→ GIDL
→ 1T1C retention
```

R0–R6.5 then established the transistor-level framework and extended the MEB search from the initial 31–41 nm window into the 43–51 nm boundary region.

### 2.3 First-presentation feedback

The first formal presentation generated four major validation tasks:

1. **Hotspot–Mesh:** does one common Mesh-GIDL refinement remain valid if the BTBT hotspot moves with MEB?
2. **E-field method:** should E-field be measured in the actual BTBT/GIDL critical region instead of one historical fixed cut?
3. **Baseline validity / BCAT trade-off:** how close is the simplified 2D baseline to a literature-oriented 3D BCAT, and does deeper MEB introduce a word-line penalty?
4. **1T1C protocol:** what exactly is the write / hold / read / retention measurement definition?

Those tasks produced the current hotspot/mesh, spatial-field, 3D baseline, RWL-proxy, and Run-7 evidence packages.

### 2.4 Second-presentation feedback

The second presentation retained MEB as the central design variable but added three new downstream guardrails:

- **High-WL write-transfer issue:** the current B0 write normalization needs `VWL_ON=3.0 V` to bring `VSN` near 1 V.
- **Cold temperature:** add `233 K (-40 °C)` as a planned operating point.
- **DWFG:** after the single-WF MEB range is derived, test whether the same range transfers to a dual-work-function gate implementation.

The current roadmap is therefore **SG MEB range → temperature robustness → DWFG transferability → selected-point 3D validation**.

- [Presentation history](docs/presentations/README.md)
- [Feedback log](docs/FEEDBACK_LOG.md)
- [Post-Turn-02 roadmap](docs/research/post_turn02_validation_roadmap.md)

---

## 3. Core Research Question

> **How does MEB depth change gate–drain coupling, the drain-side BTBT-critical electric-field distribution, and terminal GIDL in a 20 nm-class BCAT; how much of that transistor-level leakage benefit transfers to 1T1C storage-node retention; and what MEB range remains usable after temperature and cell-performance guardrails are included?**

The post-Turn-02 extension adds two follow-up questions without replacing the main MEB study:

> Does the SG-derived MEB range remain valid from cold to hot operating conditions?

> Does that SG-derived range transfer to a literature-grounded DWFG implementation, or does the optimum/range shift?

---

## 4. Current Research Flow

### Phase 1 — Single-WF MEB design range

```text
20 nm-class single-WF BCAT
        ↓
MEB depth
        ↓
Cgd / coupling
        ↓
hotspot-resolved spatial E-field
        ↓
BTBT / GIDL
        ↓
1T1C retention
        ↓
write/read + RWL guardrails
        ↓
SG effective MEB candidate / range
```

### Phase 2 — Temperature robustness

```text
SG-selected MEB candidates
        ↓
233 / 300 / 340 / 380 K
        ↓
GIDL / direct-Hold / retention / write-transfer comparison
        ↓
temperature-robust MEB range
```

Status boundary:

- `300/340/380 K`: existing transistor-level evidence and B0 normalized-Hold evidence exist.
- `233 K`: **Planned**, not yet an executed CMP result.

### Phase 3 — DWFG transferability

```text
same 20 nm BCAT framework
        ↓
DWFG extension
        ↓
same SG-selected MEB candidates
        ↓
re-locate BTBT hotspot / re-check mesh ROI
        ↓
E-field redistribution
        ↓
GIDL / retention comparison
        ↓
common range OR optimum/range shift
```

Conceptually,

```text
R_final = R_SG ∩ R_temperature ∩ R_DWFG
```

is reported only if the executed evidence actually produces a meaningful overlap.

---

## 5. Model Hierarchy

### 5.1 B0 — simplified 2D main DOE model

| Parameter | B0 value |
|---|---:|
| Gate length | 20 nm |
| Recess depth | 120 nm |
| SiO₂ liner | 5 nm |
| Nominal MEB / gate-top depth | 36 nm |
| Junction depth | 48 nm |
| S/D lateral setback | 15 nm |
| Body doping | B, `1×10^17 cm^-3` |
| Source/Drain doping | As, `1×10^20 cm^-3` |
| Gate work function | 4.8 eV |
| Geometry | simplified 2D, single-WF, rectangular trench |

B0 is a controlled comparative model. MEB is represented by gate-top depth; the physical etch process is not simulated.

### 5.2 3D-Sun-B0 — validation anchor

A literature-consistent 3D BCAT reconstruction was built from the main structural parameters reported by Sun et al., including 20 nm gate length, 120 nm recess depth, 36 nm buried depth, 5 nm oxide, 17 nm fin width, 48 nm junction depth, and 4.8 eV gate work function.

Completed model-fidelity work includes:

- geometry / coordinates / contacts / doping freeze;
- source/drain junction checks;
- G0/G1/G2 electrical runs;
- sensitivity checks;
- DC electrical-mesh convergence;
- controlled simplified-2D ↔ 3D comparison.

The 3D model **does not exactly reproduce** the paper's absolute Vth / SS / DIBL calibration. It is therefore called a **literature-consistent reconstruction**, not an exact paper replica.

![3D baseline electrical comparison](assets/images/feedback/20260911_baseline/01_g1_g2_idvg_comparison.svg)

**Workflow decision:** use 2D for dense DOE; use 3D for model-fidelity and later selected-point trend validation.

---

## 6. Major Results So Far

### 6.1 DC / mesh / GIDL framework

- Run 1 froze project-internal Vth / SS / Ion / DIBL definitions.
- Run 2 selected `Mesh-DC = Medium / Mesh_Code 1`.
- Run 3 established a usable relative NonlocalPath BTBT/GIDL branch and `Mesh-GIDL = Mesh_Code 3`.

Formal GIDL condition:

```text
T = 300 K
VD = 1.2 V
VG = 0 → -0.7 V
Band2Band(Model=NonlocalPath)
metric = |Idrain| @ VG=-0.7 V
```

### 6.2 MEB screening

Run 4 formal 31 / 36 / 41 nm screening showed a clear direction:

| MEB | GIDL endpoint |
|---:|---:|
| 31 nm | `1.9624468e-14 A` |
| 36 nm | `1.3777737e-14 A` |
| 41 nm | `7.7683012e-15 A` |

31 → 41 nm reduces the internal GIDL endpoint by approximately **60.42%**.

### 6.3 Cgd / mechanism correlation

Run 5 established a five-level trend over 31 / 33.5 / 36 / 38.5 / 41 nm.

31 → 41 nm:

- `|Cgd|`: about **17.15% decrease**
- historical fixed `E_wall,max`: about **1.69% decrease**
- GIDL endpoint: about **60.42% decrease**

The correlation is descriptive mechanism evidence, not direct causal proof.

### 6.4 Temperature-dependent transistor behavior

At 300 / 340 / 380 K, the 31 > 36 > 41 nm total-current ranking remains.

For 41 nm relative to 36 nm:

| Temperature | GIDL reduction |
|---:|---:|
| 300 K | ~43.6% |
| 340 K | ~44.2% |
| 380 K | ~16.9% |

At 380 K, the BTBT-OFF/background contribution becomes much larger, compressing the observed total-current separation.

These are isothermal lattice-temperature comparisons, not self-heating simulations.

### 6.5 Extended MEB boundary

Run 6.5 expanded the set to:

```text
36 / 41 / 43 / 45 / 47 / 48 / 49 / 51 nm
```

The current roles are:

- **P1 = 41 nm:** historical initial screened-window candidate
- **P2 = 48 nm:** transistor-level electrostatic/GIDL candidate for cell validation
- **49 nm:** primary challenger / sensitivity point
- **51 nm:** low-current/background-sensitive boundary reference

P2 is **not** a final/global/production optimum.

---

## 7. First-Presentation Feedback: Resolved / Advanced Evidence

### 7.1 Hotspot–Mesh validation

The complete R6.5 MEB set was independently checked.

Observed over 36 → 51 nm:

```text
Xhot range              = 0.0515625–0.0539063 um
ΔXhot                   ≈ +2.344 nm
Yhot                    = 0.121875 um for 8/8 cases
ROI coverage            = 8/8 PASS
minimum nearest margin  = 9.875 nm
```

The same Mesh-Code 3 common ROI therefore supports **hotspot coverage and comparison consistency** across the tested R6.5 geometries.

This is not a universal absolute mesh-independence claim.

![R6.5 hotspot ROI coverage](assets/images/feedback/20260913_mesh/02_r65_hotspot_roi_coverage.svg)

### 7.2 E-field method: fixed point → spatial critical-region analysis

The old fixed metric `E_wall,max @ Y=0.116 um` was reproducible, but it was insufficient by itself to explain the much larger GIDL change.

The feedback-resolved method locates the actual BTBT hotspot and evaluates the spatial field / generation distribution.

For 31 → 41 nm:

| Metric | Change |
|---|---:|
| terminal GIDL | **-60.42%** |
| BTBTmax | **-52.43%** |
| hotspot-cut `|E|` peak | **-3.52%** |
| 20% BTBT-active width | **-12.68%** |
| 20% active-region `∫|E|dx` | **-14.68%** |
| full-cut 1-D `∫GBTBT dx` | **-57.74%** |
| 20% region `∫GBTBT dx` | **-58.40%** |

The 20% criterion is a representative CMP middle threshold; 10/20/50% sensitivity is retained.

![Hotspot / spatial metric trends](assets/images/feedback/20260911_efield/03_normalized_metric_trends.svg)

**Current interpretation:** MEB-dependent GIDL reduction is better discussed from the **BTBT-critical spatial E-field / generation distribution** than from one local peak-field scalar.

### 7.3 Word-line structural trade-off

A 3D geometry branch was used to extract remaining W cross-section and a normalized `1/A_W` RWL proxy.

Representative results:

| MEB | GIDL suppression vs 36 nm | RWL proxy penalty |
|---:|---:|---:|
| 47 nm | ~85.39% | ~16.70% |
| 48 nm | ~85.94% | ~18.50% |
| 49 nm | ~86.31% | ~20.36% |

The 47–49 nm region therefore shows **diminishing incremental GIDL return while the geometry-derived resistance proxy continues to rise**.

![GIDL vs RWL proxy](assets/images/feedback/20260913_tradeoff/01_gidl_rwl_tradeoff.svg)

This is not an actual distributed word-line resistance or RC-delay simulation.

---

## 8. Run 7 — 1T1C Cell Operation / Retention Metric

### 8.1 Executed reference condition

```text
B0 MEB      = 36 nm
AreaFactor  = 0.017
Ccell       = 10 fF
VBL_WRITE   = 1.2 V
VWL_ON      = 3.0 V
300 K Twrite ≈ 667 ns
VSN         ≈ 1.0 V
```

At 300 K, the current protocol has completed:

```text
Write-to-~1 V
→ direct floating Hold
→ independent Read transfer
→ integrated Write → Hold → Read
```

![Run-7 300 K write / hold](assets/images/run07/06_r7_A_n409_write_hold_overall_667ns.svg)

### 8.2 Temperature-normalized direct Hold

Write time was adjusted so each temperature begins Hold near 1 V:

| Temperature | Twrite | direct-Hold start |
|---:|---:|---:|
| 300 K | 667 ns | 1.000017733 V |
| 340 K | 258 ns | 1.000107421 V |
| 380 K | 126.54 ns | 1.000272165 V |

At 100 μs:

| T | ΔVSN |
|---:|---:|
| 300 K | 0.270195 μV |
| 340 K | 0.483889 μV |
| 380 K | 7.438961 μV |

The 380 K transient-equivalent leakage scale is approximately **27.5×** the 300 K value.

This is a **short-window direct-transient temperature trend**, not a measured physical retention time.

### 8.3 Integrated 300 K W→H→R

For the tested Hold windows, integrated 300 K operation retains an approximately **+35.625 mV** D1 bitline signal.

`VSN=0.8 V` still produces a positive D1 signal in the current read transfer, so 0.8 V is a comparison/retention-window criterion—not a demonstrated CMP read-failure threshold.

### 8.4 Run-7 items still open

- leakage-vs-V / final retention metric;
- retention-specific Mesh1 vs Mesh3 numerical check;
- formal MEB-to-cell retention comparison.

Until those close, MEB-dependent retention improvement is not reported as a completed result.

---

## 9. New Guardrail — 3 V WL to Reach ~1 V SN

The current `VSN≈1 V` write is feasible, but the required `VWL_ON=3.0 V` is itself a performance concern.

The project will therefore not use **“1 V reached”** as the only success criterion.

Planned selected-point diagnostics:

```text
VWL → VSN transfer
+ write time
+ Ion / Vth relationship
+ read margin
+ leakage / retention interaction
+ MEB dependence
```

This write-transfer check becomes part of the final effective-MEB-range guardrail.

---

## 10. Run / Milestone Progress

| Stage | Main result | Status |
|---|---|---|
| Run 0 | B0 baseline geometry / linkage / turn-on | Completed |
| Run 1 | DC metric freeze | Completed |
| Run 2 | DC mesh convergence | Completed |
| Run 3 | NonlocalPath BTBT/GIDL + Mesh-GIDL | Completed |
| Run 4 | Formal 31/36/41 nm MEB screening | Completed |
| Run 5A | Cgd extraction protocol | Completed |
| Run 5B | 5-level MEB–Cgd–field–GIDL correlation | Completed |
| Run 6 | 300/340/380 K transistor-level temperature comparison | Completed |
| Run 6.5 | Extended 36–51 nm boundary closure | Completed |
| Feedback: E-field | hotspot / active-region spatial analysis | Completed at presentation-feedback level |
| Feedback: Mesh | full R6.5 common-ROI audit | Completed at comparison-consistency level |
| Feedback: Baseline | 3D reconstruction + 2D fidelity close-out | Completed at model-fidelity level |
| Feedback: RWL | 3D W-area / normalized RWL proxy | Checkpoint complete; final synthesis waits for retention |
| Run 7 | 300 K W-H-R + 300/340/380 K normalized direct Hold | **In Progress — advanced checkpoint** |
| Phase 1 final | SG MEB retention-effective range | Planned after Run-7 metric freeze |
| Phase 2 | 233–380 K robustness | Planned; 233 K not yet executed |
| Phase 3 | DWFG transferability | Planned / downstream |
| 3D final check | selected candidate points | Planned / downstream |

Detailed stage criteria remain in [RUN_SHEET.md](docs/RUN_SHEET.md).

---

## 11. Feedback → Action Mapping

| Feedback | Action | Current status |
|---|---|---|
| E-field should follow the actual GIDL/BTBT critical region | hotspot localization + spatial E/BTBT + threshold sensitivity | Completed |
| MEB may move hotspot outside one common mesh | full R6.5 hotspot/ROI audit | Completed for coverage / comparison consistency |
| 2D baseline fidelity is unclear | literature-consistent 3D reconstruction + controlled parity comparison | Closed at model-fidelity level |
| deeper MEB may increase WL resistance / delay | W-area + normalized RWL proxy | Proxy checkpoint complete |
| retention definition was unclear | explicit 1T1C write / hold / read framework | Advanced; final retention metric open |
| 3 V WL required to reach ~1 V SN | promote to write-transfer performance guardrail | Planned analysis |
| consider -40 °C | add 233 K cold point | Planned |
| consider dual work-function gate | test SG-selected MEB candidates under DWFG | Planned / downstream |

---

## 12. Current Research Roadmap

```text
[Phase 1]
Single-WF 20 nm BCAT
→ freeze final Run-7 retention metric
→ MEB-to-cell retention comparison
→ combine GIDL + retention + write/read + RWL
→ SG effective MEB range

        ↓

[Phase 2]
233 / 300 / 340 / 380 K
→ selected MEB candidates
→ retention / write-transfer robustness
→ temperature-robust SG range

        ↓

[Phase 3]
DWFG extension on the same 20 nm framework
→ same MEB candidates
→ hotspot relocation / mesh-ROI recheck
→ E-field / GIDL / retention transferability
→ common range or optimum-range shift

        ↓

[selected-point validation]
3D baseline / candidate / boundary
→ trend-preservation and design-decision robustness
```

Important boundaries:

- DWFG does not replace the current 20 nm baseline.
- the 15 nm ICEIC structure is a literature mechanism/trade-off reference, not the new baseline.
- future DWFG analysis must re-search the hotspot rather than reuse the SG hotspot coordinate by assumption.
- a full `MEB × T × SG/DWFG` 3D factorial sweep is not the current plan.

---

## 13. Repository Structure

```text
CMP/
├─ README.md
├─ CMD_HUB.md
├─ CMP_소자공정_송민호(재발표).pdf
├─ docs/
│  ├─ RUN_SHEET.md
│  ├─ MODEL_SCOPE.md
│  ├─ DECISIONS.md
│  ├─ FEEDBACK_LOG.md
│  ├─ REFERENCES.md
│  ├─ TASK_HUB.md
│  ├─ presentations/
│  │  ├─ README.md
│  │  ├─ turn01/
│  │  └─ turn02/
│  ├─ evidence/
│  ├─ methodology/
│  ├─ progress/
│  ├─ research/
│  └─ archive/
├─ code/
│  ├─ sde/
│  ├─ sdevice/
│  └─ scripts/
├─ data/
│  ├─ baseline_3d_sun_b0/
│  ├─ run00/ ... run07/
│  └─ tradeoff/
└─ assets/images/
   ├─ run00/ ... run07/
   └─ feedback/
```

Repository evidence policy:

- GitHub: reusable code, conditions, validated CSV, compact summaries, decisions, selected figures;
- local/raw archive: large native TDR / PLT / full solver logs unless explicit repository evidence is needed.

---

## 14. Presentation / Documentation Index

- [Early topic re-presentation PDF](<CMP_소자공정_송민호(재발표).pdf>)
- [Presentation history / Turn notes](docs/presentations/README.md)
- [Turn 01 note](docs/presentations/turn01/README.md)
- [Turn 02 note](docs/presentations/turn02/README.md)
- [Feedback Log](docs/FEEDBACK_LOG.md)
- [Post-Turn-02 Validation Roadmap](docs/research/post_turn02_validation_roadmap.md)

---

## 15. Model Scope / Claim Guardrails

This repository is an academic TCAD study built for traceable **relative comparison and design reasoning**.

Do not read the current results as:

- exact production-cell current calibration;
- exact reproduction of Sun et al. absolute Vth / SS / DIBL;
- absolute BTBT calibration;
- universal mesh independence;
- measured physical retention time from the short direct-Hold window;
- actual distributed WL resistance / RC delay;
- completed 233 K result;
- completed DWFG result;
- SG/DWFG common MEB range;
- production optimum;
- measured refresh reduction.

The final effective range is frozen only after the corresponding evidence exists.

See [MODEL_SCOPE.md](docs/MODEL_SCOPE.md) and [CLAIM_EVIDENCE_MATRIX.md](docs/research/CLAIM_EVIDENCE_MATRIX.md).

---

## 16. References

Primary project references include:

- M. Sun, H. W. Baac, C. Shin, “Simulation Study: The Impact of Structural Variations on the Characteristics of a Buried-Channel-Array Transistor (BCAT) in DRAM,” *Micromachines*, 2022.
- S. K. Jang, S. Y. Kim, “Impact of Metal and Poly Gate Thickness on GIDL in DRAM Dual Work-Function Structures,” *ICEIC*, 2026.
- K. Y. Kim, K. K. Min, B.-G. Park, “Trap-Induced Data-Retention-Time Degradation of DRAM and Improvement Using Dual Work-Function Metal Gate,” *IEEE EDL*, 2021.
- Y. Liu et al., “Understanding Retention Time Distribution in BCAT Under Sub-20-nm DRAM Node,” *IEEE TED*, 2024.
- 방준해 외, “셀 트랜지스터 설계 최적화를 통한 1T1C DRAM 동작 검증,” 2025.

Full indexed bibliography and project roles:

- [REFERENCES.md](docs/REFERENCES.md)

---

## License / Usage Note

본 저장소는 학술 목적의 TCAD 연구 진행 과정을 기록합니다. Synopsys Sentaurus input deck은 교육·연구용 문서화 목적으로 포함되며, Synopsys software 및 proprietary model implementation은 각 라이선스 정책을 따릅니다.
