# Chips Master Program (CMP)
### 20 nm-Class BCAT DRAM | GIDL–Retention & MEB Depth Research

> **Research Topic**  
> **20 nm급 BCAT DRAM에서 MEB 깊이에 따른 GIDL–Retention 전달 특성 및 온도 의존적 유효 설계 범위 도출**  
> *Temperature-Dependent Effective MEB Design Range Based on GIDL-to-Retention Translation in 20 nm-Class BCAT DRAM*
>
> **Program:** Chips Master Program (CMP) · **Period:** 2026.04–2027.01  
> **Track:** AI 반도체 소자·공정 설계 · **Research Tool:** Synopsys Sentaurus TCAD

---

## 1. About CMP

**Chips Master Program (CMP)**은 첨단분야 혁신융합대학사업단 및 숭실대학교 차세대반도체학과에서 운영하는 프로젝트 프로그램입니다.

교과·비교과 과정에서 학습한 반도체 지식을 바탕으로, AI 반도체를 활용하거나 활용할 수 있는 제품의 기술적 요구사항과 문제점을 분석하고 **실제 설계 결과물 도출**까지 연결하는 것을 목표로 합니다. 프로젝트 수행 과정에는 멘토링, 단계별 발표·평가 및 산업 현장 이해를 위한 지원 프로그램이 포함됩니다.

본 저장소는 CMP 소자·공정 설계 분야에서 수행하는 **BCAT DRAM TCAD 연구의 진행 과정, 발표·피드백, 시뮬레이션 코드 및 검증 근거**를 관리합니다.

## 2. Research Overview

### Background & Objective

고집적 DRAM 셀의 BCAT(Buried Channel Array Transistor)는 매립 게이트 구조를 사용하며, 게이트와 드레인 인근의 전기적 특성이 셀 누설 및 데이터 유지 특성과 연결될 수 있습니다.

본 연구는 **MEB(Metal Etch-Back) 깊이**를 핵심 설계 변수로 설정하고, MEB 변화에 따른 gate–drain coupling, drain-side electric field 및 BTBT/GIDL 변화를 TCAD로 분석합니다. 나아가 소자 수준의 누설전류 변화가 **1T1C DRAM의 Write/Hold/Read 및 Retention 특성으로 실제로 전달되는지** 검증하고자 합니다.

최종 목표는 단일 최저 누설전류 조건을 선택하는 것이 아니라, **Retention·온도·셀 동작 성능을 함께 고려한 유효 MEB 설계 범위**를 도출하는 것입니다.

### Research Flow

**MEB Depth** → Gate–Drain Coupling / Cgd → Drain-side Spatial E-field → BTBT / GIDL → **1T1C Retention** → Temperature-dependent Effective MEB Range

> 위 흐름은 **검증할 연구 가설과 분석 순서**를 나타냅니다. Cgd·전계·누설전류 사이의 직접적인 인과관계나 Retention 개선이 모두 확립되었다는 의미는 아닙니다. 연구 모델에서 MEB는 실제 식각 공정의 재현이 아닌 *gate-top depth의 기하학적 표현*입니다.

## 3. Research Navigation

연구의 최신 상태는 `HANDOFF.md`, 주요 변천은 `PROJECT_TIMELINE.md`, 상세 결과는 각 Run 및 Evidence 문서에서 확인할 수 있습니다.

| Document | Description |
|---|---|
| [**TCAD CMD / Parameter Hub**](CMD_HUB.md) | SDE·SDevice 실행 코드, 파라미터 및 SWB 실행 기록 탐색 (개편 예정) |
| [**Current Handoff**](HANDOFF.md) | 현재 연구 모델, 검증 상태, 보류 사항 및 다음 작업 |
| [**Project Timeline**](PROJECT_TIMELINE.md) | 연구 방향 변경, Baseline 전환 및 주요 마일스톤 |
| [**Research Run Sheet**](docs/RUN_SHEET.md) | Run별 수행 범위, 검증 기준 및 단계별 상태 |
| [**Presentation Archive**](docs/presentations/README.md) | CMP 발표 자료와 발표별 연구 변화 |
| [**Feedback Log**](docs/FEEDBACK_LOG.md) | 피드백 질문, 대응 작업, 검증 자료 및 상태 |

## 4. Presentation & Research Journey

CMP 연구는 **주제 선정 → 연구 방향 구체화 → 1차 결과 발표와 피드백 → 검증 결과 재발표**의 흐름으로 발전했습니다.

### 01. 주제발표 — 연구 문제 탐색

AI 메모리와 DRAM 기술의 요구사항을 조사하고, 초기 HBM·Hybrid Bonding 관련 문제의식에서 출발하여 **소자 수준에서 변수를 통제하고 검증 가능한 TCAD 연구 과제**를 탐색했습니다.

- **핵심 변화:** 폭넓은 메모리 기술 주제에서 소자·공정 설계 문제로 연구 초점을 이동
- **기록:** 초기 발표 원본의 저장소 연결 및 정확한 날짜는 추후 정리

### 02. 1차 재발표 — BCAT / MEB 연구 방향 구체화

20 nm급 BCAT DRAM을 연구 대상으로 정하고, MEB 깊이에 따른 전계 및 GIDL 특성 분석을 중심으로 **연구 목적과 시뮬레이션 접근법**을 구체화했습니다.

- **핵심 변화:** BCAT 구조, MEB 설계 변수 및 TCAD 분석 방향을 명확히 설정
- **자료:** [주제 재발표 자료 (PDF)](<CMP_소자공정_송민호(재발표).pdf>)

### 03. 1차 CMP 발표 — 소자 수준 분석 및 피드백 수렴

기존 `B0-2D-Legacy` 모델에서 Run 0–6.5를 수행하여, MEB 변화에 따른 DC 특성, Cgd, 전계 및 GIDL의 관계와 온도별 소자 특성을 발표했습니다. 이 단계에서 **GIDL 저감이 실제 DRAM 셀 Retention 개선으로 이어지는가**를 후속 연구의 핵심 질문으로 설정했습니다.

- **주요 피드백:** Hotspot 위치와 전계 추출, MEB별 Mesh 적합성, 2D Baseline 타당성, 1T1C 검증, Word-line 저항·RC trade-off
- **후속 대응:** 단일 fixed-cut 전계 중심의 해석을 공간적 BTBT critical region 분석으로 확대하고, 3D 구조 비교 및 1T1C 검증 착수
- **기록:** [1차 CMP 발표 및 피드백](docs/presentations/turn01/README.md)

### 04. 2차 CMP 발표 — 피드백 검증 및 연구 방향 보완

1차 발표 이후 수행한 **Hotspot·Mesh 검증, 공간 전계/BTBT 분석, 3D-Sun-B0 모델 검토, 기하학적 RWL proxy 및 1T1C 동작 검증** 결과를 정리했습니다.

- **확인한 사항:** 공통 Mesh ROI 내 Hotspot coverage, 공간적 BTBT 분석의 필요성, 3D 재구성의 역할과 한계, Legacy 모델의 Write/Hold/Read feasibility
- **추가 피드백:** 높은 WL Write bias의 실효성, 233 K 저온 조건 확장, DWFG 적용 시 설계 범위의 이전 가능성
- **후속 연구:** 문헌 기반 2D Baseline 재구축·보정 및 새로운 모델 계열에서 MEB–GIDL–Retention 검증
- **기록:** [2차 CMP 발표 및 피드백](docs/presentations/turn02/README.md) · [후속 연구 로드맵](docs/research/post_turn02_validation_roadmap.md)

### Feedback-driven Research Development

| 검증 주제 | 연구에 반영한 변화 |
|---|---|
| E-field / BTBT Hotspot | 단일 peak 또는 fixed cut 외에 Hotspot 위치·활성 영역·공간 분포를 분석 |
| Mesh Consistency | MEB 변화에 따른 Hotspot 이동과 공통 refinement ROI의 coverage 점검 |
| 2D / 3D Baseline | 문헌 기반 3D 재구성의 적용 범위와 2D 모델의 한계를 명시 |
| RWL Trade-off | 잔여 금속 단면적에 근거한 상대 RWL proxy 평가 (실제 RC 시뮬레이션은 아님) |
| 1T1C Retention | Legacy 동작 가능성 검증과 현재 PAPER-CAL Retention 검증을 구분 |
| Write / Temperature / DWFG | 높은 WL bias 문제를 성능 제약으로 유지하고, 저온·DWFG는 후속 검증으로 분리 |

자세한 피드백별 완료 범위와 근거는 [Feedback Log](docs/FEEDBACK_LOG.md)를 참고합니다.

## 5. Current Research Progress

**Status snapshot — 2026.10.08**

기존 `B0-2D-Legacy / NonlocalPath` 연구와 발표 피드백 검증을 보존하면서, **문헌 기반 2D 재구성 및 보정 모델인 `B0-2D-PAPER-CAL`**로 현재 연구를 이어가고 있습니다. 서로 다른 모델 계열의 절대 수치를 동일 조건의 결과로 혼합하지 않습니다.

| Item | Current Status |
|---|---|
| 2D Baseline | `B0-2D-PAPER-CAL = C7_4 / B_QF_HALF` — 물리 보정 동결 |
| 300 K MEB Atlas | 31–51 nm 범위 15개 조건의 DC / Cgd / GIDL / 공간 분석 및 데이터 QC 완료 |
| Numerical Lineage | 최신 Atlas와 2026-10-05 FZ-C 실행 parent의 정확한 연결 검증 **진행 필요** |
| Temperature | 새 모델 계열에서 온도별 검증 예정; 233 K 확장은 계획 단계 |
| 1T1C Retention | 새 모델 계열의 Write/Hold/Read 및 Retention metric 검증 예정 |
| Final Design Range | **미확정** — Retention 및 성능 제약 검증 이후 판단 |

**Next research gate:** 최신 300 K Atlas와 동결된 FZ-C parent의 모델 계열 연결 관계를 확인한 뒤, 온도별 분석과 1T1C Retention 전달 검증을 진행합니다.

→ [Latest Handoff](HANDOFF.md) · [300 K Atlas Analysis](docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md) · [Project Timeline](PROJECT_TIMELINE.md)

## 6. Research Environment & Archive

**Environment:** Synopsys Sentaurus Workbench / Structure Editor / Device / Mesh / Visual (T-2022.03), Python, GitHub  
**Keywords:** DRAM · BCAT · MEB · TCAD · Cgd · Electric Field · BTBT/GIDL · 1T1C Retention

기존 Run 0–7 중심의 상세 README는 **[Legacy README Archive](README_LEGACY_ARCHIVE.md)**에 별도 보관합니다. 해당 문서는 이전 연구 단계의 해석과 결과를 보존하기 위한 *historical snapshot*이며, 현재 연구의 최신 상태는 본 README와 `HANDOFF.md`를 기준으로 확인합니다.

> 본 저장소의 TCAD 결과는 명시된 구조·물리 모델·바이어스·추출 기준 안에서 해석합니다. 최종 공정 최적값, 양산 DRAM의 절대 Retention/Refresh 개선, 3D 등가성은 별도 검증 없이는 주장하지 않습니다.