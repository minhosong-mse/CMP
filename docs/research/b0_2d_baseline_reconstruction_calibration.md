# B0-2D-PAPER-CAL — 2D BCAT Baseline Reconstruction & Calibration Log

> **Status:** In progress — C7 final selection 단계  
> **Checkpoint:** 2026-10-05  
> **Final freeze:** C7_1 / C7_4 / C7_5 rescue + 7-candidate comparison 후  
> **Target label after freeze:** `B0-2D-PAPER-CAL`

이 문서는 2차 발표(주차 피드백) 이후 다시 수행한 **20 nm급 BCAT 2D baseline 재구축 및 calibration 전 과정**을 다음 발표와 최종 연구 정리에 바로 재사용할 수 있도록 기록한 문서입니다.

기존 Run 0–7 결과는 삭제하거나 소급 수정하지 않습니다. 기존 simplified 2D 결과는 `B0-2D-Legacy`로 historical evidence를 유지하고, 이번 branch는 별도의 paper-grounded reconstruction / calibration branch로 관리합니다.

---

## 1. 전체 흐름

```text
기존 simplified 2D B0
  ↓
Sun et al. 기준 구조/전기지표 truth table 재확인
  ↓
3D-Sun-B0 reconstruction으로 2D-only 원인 여부 분리
  ↓
B0F faithful 2D control 구축
  ↓
domain / DC mesh / GIDL mesh / DIBL-bias sensitivity 검증
  ↓
physical-value arbitrary fitting을 피한 sensitivity audit
  ↓
missing 3D electrostatics를 reduced-order proxy로 분리
  ↓
C4/C5 coarse calibration
  ↓
C6 128-case local DOE
  ↓
C7 final candidate confirmation
  ↓
final B0-2D-PAPER-CAL freeze
```

현재 provisional best는 **C7_3 (`MID_AB`)**이며 최종 확정 전입니다.

---

## 2. 기준 논문에서 직접 가져온 구조와 지표

Primary baseline paper:

- M. Sun, H. W. Baac, C. Shin, **Simulation Study: The Impact of Structural Variations on the Characteristics of a Buried-Channel-Array Transistor (BCAT) in DRAM**, Micromachines 13, 1476 (2022).

### 2.1 Paper-explicit nominal structure

| Item | Nominal |
|---|---:|
| Gate length `Lgate` | 20 nm |
| BCAT recess depth `Drecess` | 120 nm |
| Gate oxide | 5 nm |
| DBCAT / metal-gate depth | 36 nm |
| Junction depth | 48 nm |
| Fin width | 17 nm |
| Fin fillet radius | 1 nm |
| Body doping | B, `1e17 cm^-3` |
| S/D peak doping | As, `1e20 cm^-3` |
| S/D profile | Gaussian |
| Gate material / work function | W / 4.8 eV |

Paper nominal metrics:

| Metric | Paper |
|---|---:|
| Vth | 0.656 V |
| SS | 76 mV/dec |
| Ion/Ioff | `3.4e10` |
| DIBL | 23.6 mV/V |

Vth는 paper의 constant-current rule을 따라

```text
Icrit = 1e-7 A × W/L
W = 17 nm
L = 20 nm
Icrit = 8.5e-8 A
```

로 비교했습니다.

Paper physics description에서 확인되는 핵심 모델은 Philips unified mobility, Lombardi interface mobility degradation, high-field saturation 계열, Hurkx tunneling입니다.

### 2.2 Supporting literature의 역할

- Yoon et al., Semicond. Sci. Technol. 40, 015010 (2025): 같은 연구 lineage의 saddle-fin / S-D curvature 및 calibration 중요성, `VDS=0.05/1.0 V` threshold 비교 precedent를 참고.
- DWF-BCAT / Gox literature: sidewall Gox와 bottom Gox의 역할이 다르고 gate-to-drain overlap / interface condition이 GIDL에 중요함을 확인.

Supporting paper의 값으로 Sun baseline의 미공개 parameter를 임의 대체하지 않았습니다.

---

## 3. 논문에 없는 값은 어떻게 처리했는가

Reference paper에는 exact reverse engineering에 필요한 모든 Sentaurus detail이 공개되어 있지 않습니다.

대표 미공개 / 불완전 공개 항목:

- exact 3D saddle-fin coordinate
- S/D curvature 및 lateral Gaussian detail
- exact contact extent / process-dependent boundary shape
- exact interface fixed-charge / trap condition
- SS의 exact fitting window
- Ion / Ioff의 exact gate-bias sampling rule
- DIBL의 exact low/high drain-bias pair
- process calibration detail

따라서 다음 원칙을 사용했습니다.

1. **Paper-explicit physical value는 calibration 목적으로 바꾸지 않는다.**
2. 미공개 값을 임의로 만들어서 **논문 값**이라고 부르지 않는다.
3. parameter fitting 전에 domain / mesh / bias endpoint / extraction issue를 먼저 닫는다.
4. 물리적 sensitivity로 설명되지 않는 mismatch는 별도의 reduced-order calibration coordinate로 분리한다.

예를 들어 `GaussFactor=0`은 reconstruction assumption이지 literature truth가 아닙니다.

---

## 4. 3D-Sun-B0가 준 결론

2D model만 보고 fitting하지 않기 위해 Sun paper 기반 3D reconstruction을 별도로 수행했습니다.

대표 electrical checkpoint:

```text
Vth_high @ Vd=1.20 V ≈ 1.14659 V
Vth_low  @ Vd=0.05 V ≈ 1.20610 V
SS high  ≈ 91.17 mV/dec
SS low   ≈ 92.83 mV/dec
DIBL reconstruction ≈ 51.75 mV/V
```

Paper nominal은 `Vth=0.656 V`, `SS=76 mV/dec`, `DIBL=23.6 mV/V`입니다.

즉 3D geometry fidelity를 높여도 absolute electrical mismatch가 남았습니다.

> **결론:** 현재 mismatch를 단순히 2D이기 때문이라고 설명하지 않으며, unpublished geometry / process / electrostatic calibration detail이 더 큰 원인일 수 있다고 판단했습니다.

`3D-Sun-B0`는 계속 **literature-consistent 3D validation anchor**로 사용하며 exact paper-calibrated deck이라고 부르지 않습니다.

---

## 5. B0F — faithful 2D control

Calibration proxy를 넣기 전에 paper-explicit physical values만 사용한 control을 새로 만들었습니다.

```text
Lgate        = 20 nm
Drecess      = 120 nm
DBCAT / MEB  = 36 nm
physical Tox = 5 nm
WF           = 4.8 eV
Body         = B 1e17 cm^-3
S/D peak     = As 1e20 cm^-3
Djunction    = 48 nm @ 1e17 cm^-3 criterion
S/D profile  = Gaussian
Qf           = 0
```

2D는 longitudinal / along-channel reduction으로 취급합니다. 3D `Rfillet`과 2D longitudinal rounding은 동일 physical object로 간주하지 않습니다.

### 5.1 Domain convergence

`DomainX=0.30 um`을 고정하고 `DomainY=0.32/0.40/0.48 um`을 비교했습니다.

- 0.40→0.48 um Vth 변화: sub-0.12 mV
- SS 변화: 약 0.13 mV/dec 이하

따라서 `DomainX=0.30 um`, `DomainY=0.48 um`을 faithful branch의 conservative domain으로 freeze했습니다.

### 5.2 Faithful ID–VG

| Vd | Vth | SSquick | SS1dec | SS2dec |
|---:|---:|---:|---:|---:|
| 0.05 V | 1.338343 | 97.3389 | 117.2959 | 112.5738 |
| 1.00 V | 1.244686 | 95.9594 | 107.7597 | 104.4644 |
| 1.20 V | 1.233484 | 95.7439 | 107.6668 | 104.2826 |

즉 paper-explicit 구조만으로는 absolute target과 큰 mismatch가 남았습니다.

### 5.3 DIBL bias sensitivity

Paper의 exact DIBL bias pair가 공개되지 않아 low-Vd를 `0.025/0.05/0.10 V`로 나눠 확인했습니다.

대표 result:

```text
0.05 → 1.20 V : ~91.18 mV/V
0.10 → 1.20 V : ~80.3 mV/V
0.05 → 1.00 V : ~98.6 mV/V
```

low-Vd 선택만으로 paper 23.6 mV/V mismatch를 설명할 수 없었기 때문에 추가 splitting은 중단했습니다.

---

## 6. Numerical convergence를 calibration보다 먼저 닫음

### 6.1 DC mesh

B0F `MeshLevel 0/1/2`에서 nominal 1.2 V ID–VG가 display precision 수준에서 동일했습니다.

대표 nominal:

```text
Vth      = 1.233484 V
SSquick  = 95.7439 mV/dec
Id@Vg1.2 = 3.0028e-6 A
Id@Vg2.0 = 1.9710e-4 A
```

따라서 absolute mismatch는 DC mesh artifact가 아니라고 판단했습니다.

### 6.2 Hurkx GIDL / local mesh

Reference paper physics와 맞추기 위해 faithful branch는 Hurkx를 사용했습니다.

Nominal 36 nm, `VD=1.2 V / VG=-0.7 V / 300 K`:

```text
Mesh0 GIDL = 9.64877588e-10 A
Mesh1 GIDL = 9.62500442e-10 A
Mesh2 GIDL = 9.60955543e-10 A
Mesh1→2 difference ≈ -0.161%
```

local BTBT / E-field extraction도 Mesh1/2에서 사실상 수렴했습니다.

> B0F는 paper absolute metric과는 맞지 않지만 numerical control로서는 안정적입니다.

---

## 7. Physical sensitivity audit

Calibration proxy 도입 전에 geometry / physics / S-D implementation sensitivity를 순차적으로 검사했습니다.

검사 항목:

- geometry / bottom rounding
- mobility / bandgap-related option
- OldSlotboom
- S/D setback
- Gaussian implementation / factor
- peak-position sensitivity

대표 관찰:

- rounded geometry는 방향성은 있었지만 paper target까지 닫지 못함
- OldSlotboom의 Vth 영향은 대략 `-13 mV` 규모
- S/D setback / Gaussian-factor 계열은 대체로 몇 mV 규모
- 약 0.5 V급 paper mismatch를 설명하기에는 부족

따라서 WF / physical doping / physical Tox / recess를 arbitrary fit하는 방식은 사용하지 않았습니다.

---

## 8. Reduced-order calibration coordinate

Faithful reconstruction과 sensitivity audit 후 missing 3D electrostatics를 2D에서 표현하기 위해 세 coordinate를 분리했습니다.

### GateCouplingScale

```text
ToxEff = 5 nm / GateCouplingScale
```

- stronger effective gate coupling을 나타내는 reduced-order coordinate
- sidewall / saddle-fin / surround-gate 효과를 2D에서 압축해 표현
- **실제 fabricated gate-oxide thickness가 아님**

### GateDepthBoost

```text
DrecessEff = 120 nm + GateDepthBoost
```

- missing 3D effective gate-control depth proxy
- **실제 paper recess를 변경했다는 뜻이 아님**

### Qf_Int

- threshold / electrostatic offset axis
- unknown interface/process condition을 calibration space에서 분리
- literature-explicit fixed-charge 값이라고 주장하지 않음

핵심 구분:

```text
paper physical values
≠
effective 2D calibration coordinates
```

---

## 9. C4 / C5 coarse calibration

Coarse DOE에서 각 axis 역할을 확인했습니다.

예시 `Qf=2.4e12 cm^-2`:

| GCS | DepthBoost | Vth | SSquick | internal DIBL |
|---:|---:|---:|---:|---:|
| 2.4 | 0 nm | 0.650963 | 75.6316 | ~30.45 |
| 2.4 | 5 nm | 0.656190 | 75.4996 | ~28.47 |
| 2.4 | 10 nm | 0.660994 | 75.3933 | ~26.74 |
| 2.4 | 15 nm | 0.665220 | 75.3060 | ~25.09 |
| 2.8 | 5 nm | 0.659853 | 73.54 | ~24.09 |

해석:

- GCS 증가 → SS/DIBL 개선, 단 과도하면 SS가 paper보다 낮아짐
- DepthBoost 증가 → DIBL 개선 경향 + Vth 증가
- Qf 증가 → Vth를 낮추는 tuning axis

이 결과로 C6 local search 영역을 좁혔습니다.

---

## 10. C6 — 128-case local DOE

```text
GateCouplingScale = 2.20 / 2.25 / 2.30 / 2.35
GateDepthBoost    = 0.020 / 0.025 / 0.030 / 0.035 um
Qf_Int            = 2.4e12 / 2.5e12 / 2.6e12 / 2.7e12 cm^-2
VD_Target         = 0.05 / 1.20 V
```

총 `4×4×4×2 = 128` case입니다.

High-Vd branch는 `RequestedVd=1.2`와 `BiasReached=1`을 만족해야 valid로 취급했습니다.

주요 candidate:

| Label | GCS | DepthBoost | Qf | Vth@1.2 | SSquick | DIBL proxy |
|---|---:|---:|---:|---:|---:|---:|
| A | 2.25 | 20 nm | 2.50e12 | 0.656418 | 76.1212 | ~25.41 |
| B | 2.30 | 25 nm | 2.60e12 | 0.650086 | 75.7617 | ~23.39 |
| C | 2.20 | 25 nm | 2.60e12 | 0.648124 | 76.3930 | ~24.63 |
| D | 2.35 | 30 nm | 2.50e12 | 0.664689 | 75.4106 | ~21.55 |

A는 Vth/SS가 가장 좋았고 B는 DIBL까지 포함한 balance가 좋았습니다.

일부 high-Vd case에서 continuation failure가 있어 C6 한 점만으로 freeze하지 않고 C7을 추가했습니다.

---

## 11. Hurkx ↔ NonlocalPath bridge

Legacy CMP의 historical GIDL chain은 NonlocalPath를 사용했지만 paper-grounded B0F는 Hurkx를 사용합니다.

Parameter switch 한 파일은 preprocessor issue 때문에 폐기하고 explicit project 두 개로 분리했습니다.

```text
B0F_BRIDGE_HURKX
B0F_BRIDGE_NONLOCAL
```

Nominal 36 nm, `VG=-0.7 V / VD=1.2 V`:

| Metric | Hurkx | NonlocalPath |
|---|---:|---:|
| terminal current | ~9.6488e-10 A | ~9.6488e-10 A |
| BTBTmax | ~5.19e20 | ~1.12e18 |
| hotspot X | ~0.00234 um | ~0.03574 um |
| E@BTBT | ~1.29e6 V/cm | ~6.96e5 V/cm |
| global Emax | ~3.53e6 V/cm | ~3.53e6 V/cm |

결론:

- terminal current만으로 spatial BTBT mechanism을 판단하지 않음
- model choice가 hotspot / generation distribution에 크게 영향을 줌
- faithful paper-calibration branch는 Hurkx 유지
- legacy NonlocalPath absolute result와 faithful Hurkx absolute result를 직접 혼합하지 않음

---

## 12. Faithful B0F의 MEB mechanism 재검증

Calibration 중에도 `31/36/41 nm`에서 trend가 유지되는지 확인했습니다.

### ID–VG @ 1.2 V

| MEB | Vth | SSquick | Id@Vg0 | Id@Vg2 |
|---:|---:|---:|---:|---:|
| 31 | 1.233450 | 95.8294 | 7.888e-11 | 1.985e-4 |
| 36 | 1.233484 | 95.7439 | 1.181e-11 | 1.971e-4 |
| 41 | 1.233531 | 95.7336 | 2.426e-12 | 1.951e-4 |

31→41에서 Vth/SS는 거의 유지되고 Ion은 약 -1.7%, off-current는 약 -96.9%였습니다.

### Hurkx GIDL

| MEB | GIDL | BTBTmax |
|---:|---:|---:|
| 31 | 1.155e-8 | 3.476e21 |
| 36 | 9.649e-10 | 5.192e20 |
| 41 | 1.147e-10 | 1.123e20 |

31→41에서 GIDL 약 -99.0%, BTBTmax 약 -96.8%입니다.

### Fixed common cut

공통 `Ycut=0.26625 um`에서:

```text
Ecut peak       +0.93%
integrated E    -6.97%
deep-side E     -13.4%
BTBT peak       -96.77%
integrated BTBT -98.65%
terminal GIDL   -99.01%
```

따라서 mechanism wording을 다음처럼 수정했습니다.

> **MEB 증가 → drain-side field spatial redistribution / deep-side·integrated field 감소 + tunneling-favorable region 변화 → BTBT collapse → GIDL suppression**

한 점의 peak E 감소만으로 GIDL을 설명하지 않습니다.

---

## 13. Temperature-edge pilot

Final calibrated model 전에 faithful B0F에서 `233/300/380 K` edge precheck를 수행했습니다.

| MEB | 233 K GIDL | 300 K GIDL | 380 K GIDL |
|---:|---:|---:|---:|
| 31 | 5.429e-10 | 1.155e-8 | 1.141e-7 |
| 36 | 1.833e-11 | 9.649e-10 | 1.928e-8 |
| 41 | 1.019e-12 | 1.147e-10 | 4.107e-9 |

31→41 suppression:

```text
233 K : ~99.81%
300 K : ~99.01%
380 K : ~96.40%
```

모든 온도에서 deeper-MEB 방향은 유지됐지만 고온에서 상대 benefit이 축소됐습니다.

> 이 데이터는 final calibrated-temperature result가 아니라 faithful-B0F pilot입니다. Final baseline freeze 후 `233/300/340/380 K`를 다시 계산합니다.

---

## 14. C7 — final candidate confirmation

C6의 high-Vd numerical failure를 분리하기 위해 C6 Pareto point와 interpolation / compensation point만 추려 final confirmation을 구성했습니다.

| C7 | Tag | GCS | DepthBoost | Qf |
|---:|---|---:|---:|---:|
| 1 | A_C6 | 2.250 | 20.0 nm | 2.50e12 |
| 2 | A_DEEP_COMP | 2.250 | 22.5 nm | 2.55e12 |
| 3 | MID_AB | 2.275 | 22.5 nm | 2.55e12 |
| 4 | B_QF_HALF | 2.300 | 25.0 nm | 2.55e12 |
| 5 | B_C6 | 2.300 | 25.0 nm | 2.60e12 |
| 6 | D_C6 | 2.350 | 30.0 nm | 2.50e12 |
| 7 | D_QF_HALF | 2.350 | 30.0 nm | 2.55e12 |

공통 조건:

```text
VD = 0.05 / 1.0 / 1.2 V
T = 300 K
nominal MEB = 36 nm
```

### 14.1 Robust continuation patch

C7_1 log에서 drain ramp 자체는 목표 bias에 도달했지만 low-Vg sweep이 약 `Vg≈0.07 V`에서 Newton oscillation 후 MinStep failure를 일으켰습니다.

C7_2에서도 같은 패턴이 시작돼 candidate-specific physics failure가 아닌 공통 continuation issue로 판단했습니다.

물리조건을 바꾸지 않고 gate continuation만:

```text
0 → 0.06 V
0.06 → 0.10 V
0.10 → 0.40 V
→ 기존 후속 gate sweep
```

으로 세분했습니다.

### 14.2 현재 완료 상태

정상 완료:

- C7_2
- C7_3
- C7_6
- C7_7

Rescue pending:

- C7_1
- C7_4
- C7_5

현재 completed set:

| Candidate | Vth@1.2 | SSquick | DIBL 0.05→1.0 | DIBL 0.05→1.2 |
|---|---:|---:|---:|---:|
| C7_2 | 0.652739 | 76.0904 | ~26.27 | ~24.71 |
| **C7_3** | **0.653142** | **75.9335** | **~25.92** | **~24.39** |
| C7_6 | 0.664688 | 75.4106 | ~22.98 | ~21.55 |
| C7_7 | 0.659342 | 75.4071 | ~22.96 | ~21.54 |

현재 provisional ranking:

```text
C7_3 > C7_2 > C7_7 > C7_6
```

C7_1 / C7_4 / C7_5 rescue 완료 전에는 final ranking으로 freeze하지 않습니다.

---

## 15. 현재 best C7_3와 reference paper 비교

C7_3:

```text
GateCouplingScale = 2.275
GateDepthBoost    = 22.5 nm
Qf_Int            = 2.55e12 cm^-2
```

Equivalent reduced-order coordinate:

```text
ToxEff     = 5 / 2.275 ≈ 2.198 nm
DrecessEff = 120 + 22.5 = 142.5 nm
```

이 두 값은 fabricated/paper dimension이 아니라 reduced-order calibration coordinates입니다.

| Metric | Paper | C7_3 | Difference |
|---|---:|---:|---:|
| Vth | 0.656 V | 0.653142 V | -2.858 mV, 약 -0.44% |
| SS headline | 76.0 | SSquick 75.9335 | -0.0665, 약 -0.09% |
| DIBL | 23.6 | 24.39* | +0.79, 약 +3.4% |
| Ion/Ioff | 3.4e10 | ~2.37e10** | 약 -30% |

`*` project internal `0.05→1.2 V` definition  
`**` `Id(Vg=2)/Id(Vg=0)` sampling

Alternative SS:

```text
SS_1dec = 79.4079 mV/dec
SS_2dec = 77.9298 mV/dec
```

따라서 현재 safe claim은:

> **A reduced-order 2D BCAT surrogate was calibrated against the nominal electrical characteristics of the reference 3D TCAD structure.**

다음 표현은 사용하지 않습니다.

> ~~The 3D reference BCAT was exactly reproduced in 2D.~~

---

## 16. C7 SVisual metadata 주의

Common SVisual 작성 과정에서 일부 screenshot의 metadata field가 C7_1 값으로 표시되는 문제가 확인됐습니다.

```text
CandidateCode = 1
GateCouplingScale = 2.25
GateDepthBoost = 20 nm
Qf = 2.5e12
```

처럼 보이더라도 candidate identity는 **project name + candidate-specific SDE/SDevice deck** 기준으로 판단합니다.

Final archive 전에는 common SVisual metadata hardcoding을 수정하고 final screenshot / CSV를 다시 검증해야 합니다.

---

## 17. Final selection gate

최종 candidate는 Vth 하나가 가장 가까운 점으로 고르지 않습니다.

1. **Numerical robustness:** `BiasReached=1`, `Vth_CC_Reached=1`, `Vth_CC_2D != -1`
2. **1.2 V paper benchmark:** Vth + SSquick + SS1dec + SS2dec
3. **Drain sensitivity:** DIBL `0.05→1.0`, `0.05→1.2` 둘 다 기록
4. **Current audit:** `Ion/Ioff @ Vg1.2/Vg0`, `Ion/Ioff @ Vg2/Vg0` 둘 다 기록
5. **Tie-breaker:** numerical stability → smaller proxy excursion → smooth multi-bias behavior

Paper exact SS/DIBL/Ion-Ioff definition이 공개되지 않은 항목은 exact-match claim 대신 benchmark로 사용합니다.

---

## 18. Final freeze 후 바로 이어갈 Run

C7 final candidate를 선택하면 paper metric을 맞추기 위한 추가 tuning은 중단합니다.

### 18.1 One-time nominal numerical confirmation

```text
MEB = 36 nm
T = 300 K
final candidate
standard mesh vs one-step finer mesh
```

DC + GIDL/BTBT/local field numerical consistency만 마지막으로 확인합니다.

### 18.2 Final MEB run

Calibration coordinate를 고정하고 **MEB만 변경**합니다.

```text
MEB = 31 / 36 / 41 nm
```

재추출:

- Vth / SS / Ion / Ioff
- GIDL
- BTBTmax / hotspot
- common fixed-cut
- integrated E / integrated BTBT
- shallow/deep same-coordinate E

### 18.3 Full temperature

```text
233 / 300 / 340 / 380 K
×
MEB 31 / 36 / 41
```

B0F temperature-edge pilot의 **방법과 trend만 승계**하고 absolute 숫자는 final baseline에서 다시 계산합니다.

### 18.4 1T1C retention

```text
MEB
→ GIDL / leakage
→ storage-node charge loss
→ retention
→ temperature-dependent effective MEB range
```

로 연결합니다.

---

## 19. 이전 Run에서 승계하는 것 / 다시 계산하는 것

### 그대로 승계

- domain-convergence 결론
- mesh design philosophy
- hotspot extraction method
- common-cut / active-region method
- fixed-cut + integrated E/BTBT method
- terminal current만으로 mechanism을 단정하지 않는 rule
- Hurkx / NonlocalPath 구분
- DIBL bias limitation
- temperature-edge experiment design
- 1T1C validation flow

### Final baseline에서 다시 계산

- Vth / SS / Ion / Ioff
- MEB별 GIDL / BTBT / E-field
- fixed-cut integral
- 233/300/340/380 K absolute result
- final retention
- effective MEB range

### 다시 하지 않는 dead-end exploration

- physical WF / doping arbitrary fit
- DomainY 0.32/0.40/0.48 재탐색
- DIBL low-Vd 계속 세분화
- setback / GaussFactor를 large calibration knob처럼 재탐색
- Hurkx↔NonlocalPath bridge 재수행
- mesh를 처음부터 다시 설계

---

## 20. Presentation / report wording guardrail

### 사용 가능

- paper-grounded faithful 2D control
- reduced-order 2D calibrated surrogate
- nominal electrical characteristics 기준 calibration
- internal DIBL proxy
- SS extraction-window sensitivity
- missing 3D electrostatics의 effective coordinate 보정
- final selection pending / provisional candidate

### 사용 금지

- exact 3D reproduction
- fabricated Tox = ToxEff
- actual recess = DrecessEff
- Qf가 paper explicit process value
- SSquick이 paper exact extraction
- 0.05→1.2 DIBL이 반드시 paper-equivalent
- C7_3가 이미 final baseline
- faithful B0F와 calibrated C7을 동일 physical model로 표현
- legacy NonlocalPath와 faithful Hurkx absolute value 직접 혼합

---

## 21. 2026-10-05 checkpoint

Completed:

- B0F faithful control
- domain convergence / DIBL bias sensitivity
- DC mesh / Hurkx GIDL mesh check
- MEB3 faithful trend / fixed-cut mechanism
- Hurkx / NonlocalPath bridge
- 233/380 K temperature-edge pilot
- C4/C5 calibration sensitivity
- C6 128-case local DOE
- C7_2 / C7_3 / C7_6 / C7_7 confirmation

Pending:

- C7_1 / C7_4 / C7_5 failure-log rescue
- 7-candidate final ranking
- final `B0-2D-PAPER-CAL` freeze
- one-time final mesh confirmation

다음 업데이트에서는 위 pending 항목을 이어서 기록하고 **final baseline을 이 문서에서 공식 freeze**합니다.

---

## 22. Related repository records

- [Main Run Sheet](../RUN_SHEET.md)
- [Model Scope](../MODEL_SCOPE.md)
- [Decisions](../DECISIONS.md)
- [Feedback Log](../FEEDBACK_LOG.md)
- [Post-Turn-02 Validation Roadmap](post_turn02_validation_roadmap.md)

## Naming rule

```text
B0-2D-Legacy
= historical simplified 2D dataset

B0F
= faithful paper-explicit 2D control

B0-2D-PAPER-CAL
= final reduced-order calibrated 2D surrogate
  (final name after C7 + mesh confirmation)
```

이 naming을 유지해 historical evidence와 새 calibration result가 섞이지 않도록 합니다.