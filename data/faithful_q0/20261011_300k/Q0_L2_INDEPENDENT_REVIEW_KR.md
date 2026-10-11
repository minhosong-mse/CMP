# CMP Faithful-Q0 300 K × 15-MEB 독립 검증 및 PAPER-CAL baseline 채택 판정

**분석일:** 2026-10-11  
**입력:** `CMP_FAITHFUL_Q0_ALL15_4PROJECTS_EVIDENCE.zip` (사용자 제공 원본, 읽기 전용)  
**비교 원본:** live GitHub `main`의 `data/paper_cal/atlas_300k_20261008/processed/MEB_300K_ATLAS_MASTER_VALIDATED.csv`, `AGENTS.md`, `HANDOFF.md`, `docs/research/b0_2d_baseline_reconstruction_calibration.md`, `docs/evidence/paper_cal_g0_parent_spatial_bridge_20261008.md`.  
**실행 상태:** 새로운 Sentaurus 계산은 하지 않았음. 기존 실행에서 나온 CSV·전처리 CMD·로그·상태 파일을 독립 감사함. 모든 숫자는 **해당 모델 내부 수치**이며 실험 측정값이 아님. GitHub 수정 없음.

## 0. 결론 (검증 범위 엄격 구분)

1. **Faithful-Q0의 지위: 논문 명시 치수를 반영한 2D `Qf=0` 구조 대조군으로 `CONDITIONAL / PROVISIONAL` 채택 가능.** 실행 데이터 및 기본 설정의 출처가 확인되었고, 300 K 총 drain leakage 감소·AC Cgd 감소라는 큰 방향은 PAPER-CAL Atlas와 재현된다. 단, `Qf=0`은 논문에 공개된 고정 전하의 실제값이 아니라 추가 고정 전하를 두지 않은 **연구 가정**이다.
2. **B0-2D-PAPER-CAL(기존 C7_4)의 대체 baseline 또는 spatial-BTBT/GIDL 메커니즘에 대한 독립적인 긍정 검증으로 채택: `NO / NOT DEMONSTRATED`.** 구체적인 핫스팟 위치와 BTBT 생성 경향이 크게 갈리며 Faithful-Q0의 ON−OFF 효과가 매우 작고 적분과 일치하지 않는다. 반대로 이 차이 자체가 2D surrogate 해석의 적용 범위를 표시하는 의미 있는 민감도/음성 대조 evidence이다.
3. **기존 PAPER-CAL freeze 유지.** 기존 nominal DC 지표 보정의 유효성과 300K Atlas 내부 QC는 역사적 범위에서 유지된다. 새 결과로 물리 모델을 retune하거나 3D equivalence, GIDL→retention 인과, 물리적 설계 최적을 보증할 수 없다.
4. **현재 Q0 결과의 내부 1차 데이터 감사:** GIDL terminal ON 15/15, OFF 15/15, ON spatial 15/15, Cgd 14/15. 31nm Cgd **SDevice run은 완료**되었으나 SVisual CSV 미수집. 메커니즘과 mesh-convergence 검증은 보류.

## 1. 독립 QC — 원본 provenance 기반

| 항목 | 확인 결과 | 판정 |
|---|---|---|
| 수집된 원본 파일(manifest) | **1,513/1,513** SHA-256 및 바이트 길이 일치 | PASS |
| SDevice 종료 상태 | 4프로젝트 × 15 = **60/60 `done`** | 실행 종료 확인 |
| SVisual 요약 | ON terminal 15, OFF terminal 15, ON spatial 15, Cgd **14** | Cgd 31nm 누락 |
| ON/OFF Id–Vg 원본 곡선 | 각 15개, 각각 **222행** | PASS |
| GIDL 바이어스 | ON/OFF `Vd=1.2 V`, `Vg=-0.7 V` | PASS |
| AC 바이어스 | 14건 `Vd=1.2 V`, `Vg=-0.7 V`, **1 MHz** | 14/14 PASS |
| SDE 36nm 4프로젝트 | 전처리 SDE **바이트 해시 완전 동일** | PASS |
| SDE 물리 수치 | GCS=1, GDB=0, 5nm Tox, 120nm recess, Jdepth=48nm, MeshLevel2 | PASS (정적 source) |
| SDevice 온도, Qf, Hurkx | 전부 300K, 추가 FixedCharge 없음; ON만 `Band2Band(Hurkx)` | PASS (실행 deck) |
| GIDL ON과 OFF 36nm device deck 차이 | Recombination의 Hurkx 블록 외 차이 없음 | PASS |
| SVisual ON terminal ↔ spatial Id | 최대 상대차 약 **1.54×10⁻⁹%** | PASS |
| KCL 상대잔차 | 최대 ON **3.38×10⁻¹²**, OFF **5.37×10⁻¹²** | PASS (전류 보존 진단) |
| AC reciprocity | 최악 **0.07581% (33nm)** | 양호한 수준, 저깊이 비교에서 주의 |
| 수치 mesh convergence | Level2 단일 mesh 실행, Level3/독립 ROI 검증 없음 | **NOT DEMONSTRATED** |
| TDR/AC PLT 원본 | 이 ZIP에는 없음(수집기 기본 제외) | 공간/AC 독립 재계산 불가 |

수집기 생성 `MASTER_CORE`를 정답으로 전제하지 않고 각 프로젝트의 원본 summary CSV에서 다시 조인·계산했다. 원본과 기존 수집기 계산상 최대 ON−OFF 차이는 `8.1×10⁻²⁸` 수준으로 반올림 범위에 불과함. `done` 및 작은 KCL 잔차는 **스텝 종료의 증거**이지 절대 물리 정확도·mesh 수렴을 보장하지 않음.

## 2. 대표 5개 깊이: 핵심 수치 대조

*단위: 누설 전류는 해당 deck/SVisual의 A/μm 표기, Cgd는 raw AC 행렬값(프로젝트 내부 정의). Q0와 PAPER-CAL은 GCS/GDB/Qf 전체 보정 패키지가 다른 **별도 lineage**이다.*

| MEB (nm) | Q0 총 Id ON | PAPER 총 Id ON | Q0/PAPER | Q0 ON−OFF | Q0 ON−OFF/ON | Q0 Cgd | PAPER Cgd |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 31 | 1.1810e−8 | 6.3377e−11 | 186.3× | 8.3747e−15 | 0.0000709% | **미수집** | 1.5857e−16 |
| 36 | 9.9236e−10 | 1.0886e−12 | 911.6× | 9.7581e−16 | 0.0000983% | 1.1495e−16 | 1.4244e−16 |
| 41 | 1.1794e−10 | 2.7258e−13 | 432.7× | 8.3582e−17 | 0.0000709% | 1.0342e−16 | 1.2614e−16 |
| 48 | 1.0649e−11 | 9.9516e−14 | 107.0× | 1.5311e−18 | 0.0000144% | 8.8993e−17 | 1.0817e−16 |
| 51 | 4.5678e−12 | 5.5836e−14 | 81.8× | 2.5064e−19 | 0.00000549% | 8.3401e−17 | 1.0163e−16 |

**비교 가능한 현상과 불가능한 결론**
- Q0 총 GIDL-bias drain current는 31→51nm에서 약 **2,585.5배 감소**; PAPER-CAL은 같은 구간 약 **1,135배 감소**한다. 방향성은 일치하지만 Q0 절대전류가 **약 82–912배 더 커** 동일한 누설 모델로 간주할 수 없다.
- Cgd는 31nm Q0가 없으므로 공통 구간 33→51nm에서 비교: Q0 **−31.87%**, PAPER-CAL **−33.20%**. Q0의 절대 Cgd는 주로 PAPER-CAL 대비 **80–82%** 정도다. 이 일치는 **전역 coupling 경향**의 제한적 강건성 근거이지, `Cgd 감소 → BTBT → GIDL` 인과 검증은 아니다.
- 48nm 구조 경계에서 Q0 drain-current 감소율은 47→48 **26.33%**, 48→49 **25.41%**, 49→50 **24.61%**, 50→51 **23.72%**로 평활하다. 양 모델 모두 이 데이터만으로 48nm electrical knee/최적은 입증되지 않는다.

## 3. 가장 중요한 불일치 — Hurkx ON−OFF와 공간 BTBT

- Q0 ON−OFF는 전체 15개에서 총 drain current의 **0.00000549%–0.00009833%**(fraction 약 `5.5×10⁻⁸–9.8×10⁻⁷`)뿐이다. 따라서 총 Id의 >99.9999%가 OFF에서도 남아 있는 **BTBT-OFF residual**이다. 이것은 원인 미확정 residual이며, '총 Id=GIDL BTBT 전류'라는 해석은 불가능하다.
- 대조적으로 PAPER-CAL Atlas ON−OFF 비중은 **31nm 0.105% / 36nm 16.94% / 41nm 91.19% / 48nm 99.57% / 51nm 99.81%**였다. 즉 물리 모델 ON/OFF에 대한 결과 의존성이 전혀 다르다.
- Q0 `∫BTBT`는 31nm **65,380.7 → 51nm 46.71**(약 **1,400배 감소**), 15개 전 범위에서 단조 감소. PAPER-CAL은 **39nm에서 최대**이고 비단조적. `BTBTmax`도 Q0는 31nm **2.91×10²¹ → 51nm 9.83×10¹⁸**, PAPER-CAL은 **41nm 최대**. 따라서 누설과 Cgd의 감소방향이 공통이라는 사실만으로 공간 메커니즘 동일성을 주장할 수 없다.
- 기존 PAPER-CAL 수치 convention을 **가정해** `q×(Q0 raw ∫BTBT)`를 계산하면 `(q∫BTBT)/(Id_ON−Id_OFF)`는 **31nm 1.25**, **36nm 1.42**, **41nm 2.03**, **48nm 10.1**, **51nm 29.9**로 악화한다. 반면 PAPER-CAL 기존 15-point 세트는 ON−OFF와 q∫BTBT가 대체로 잘 맞았다. 이 비교는 신호 전달·회수·정규화 또는 수치 정밀도의 차이를 가려내야 한다는 **경고**이며, q∫BTBT와 drain ON−OFF가 원리적으로 언제나 동일해야 한다는 증명은 아니다. 엄격한 단위/AreaFactor 및 TDR 기반 재적분은 별도 검증 필요.
- SDevice 사용 `Digits=5`이고 작은 ON−OFF는 **두 거대한 총 전류를 상쇄해 얻은 값**이므로, 우선 계산상 결과로 보고 `resolved microscopic Hurkx current`라고 단정하지 않는다. 작은 KCL만으로 ON−OFF의 유효숫자가 보장되지 않는다.

## 4. 공간 핫스팟: gate-edge hotspot이 아닌 별도 위치

- Q0 전역 BTBTmax는 **33–51nm 14/15개에서 정확히** `Xhot=0.002343750 μm (=2.34nm)`, `Yhot=0.266250014 μm`로 고정되어 있다. 31nm만 `Xhot=0.029296875 μm`, 같은 Y 위치. 반면 PAPER-CAL에서는 Xhot이 대체로 MEB 깊이를 따라 33nm 부근에서 34nm, 36nm에서 36.33nm, 51nm에서 50.39nm로 이동한다.
- 새 SDE의 좌표 체계는 **X=표면에서의 수직 깊이**, **Y=source→drain**, `YoxR≈0.255 μm`. 따라서 Q0 14개 점의 전역 최대값은 게이트 깊이 부근보다 **표면 가까운 drain 쪽**에 위치한다. 이러한 spatial migration은 공통 drain-current 경향과 별도로 해석해야 한다.
- 전처리 SDE의 `RefWin.GIDLOuter`는 X 하한 `GateTop−0.015μm`이고 Y 상한 `YoxR+0.010μm ≈0.265μm`. Q0 hot 위치는 **전 깊이에서 Y 방향으로 약 1.25nm 바깥**, 33–51nm는 X 방향으로도 ROI 하한 밖이다. 즉 hotspot이 '기존 gate-side 고정 정밀 mesh'가 의도한 핵심 영역 안에 있다고 주장할 수 없다. 다만 이 자체가 계산 오류의 증명은 아니다.
- 새 Q0 공통 Y-cut은 **Y=0.255100μm**. `BTBTcut_peak / BTBTmax`는 31nm **1.51×10⁻⁶**, 36nm **2.72×10⁻⁵**, 51nm **5.46×10⁻⁴**에 불과해 global hotspot 대표성이 낮다. cut 상의 Xpeak가 GateTop에 따라 움직이는 것과 전역 최댓값이 표면 near-drain에 고정되는 것은 서로 다른 물리적 부위다.
- Q0 E@BTBT 전역 hotspot은 31→51nm **8.23×10⁵→1.304×10⁶ V/cm**로 증가하지만 이는 PAPER-CAL과 **측정 좌표가 서로 다른 hot point**의 field다. 절대 field의 1:1 인과/정량 비교에 주의.
- ZIP에는 실제 TDR/grid 자료가 없어 물리 공간의 세부 분포를 **독립 재적분/시각 확인**하지 못했다. Layer 2 단일 mesh의 수렴성 검증도 없다.

## 5. 'Baseline 채택' 질문에 대한 역할별 판정

| 의도한 사용 | 판정 | 실제로 주장 가능한 내용 |
|---|---|---|
| Sun et al. 명시 구조 기반 2D 연구 control (Qf0 가정) | **조건부 채택** | 별도 lineage `B0-2D-FAITHFUL-Q0`의 구조 대조·sensitivity 결과 |
| Cgd/MEB 전역 경향의 모델 간 강건성 확인 | **제한적으로 지지** | 33–51nm Cgd 감소율 유사; 누설 총전류 감소 방향 공통 |
| Hurkx/BTBT가 총 누설을 지배하고 동일 hotspot을 만든다는 검증 | **불충족** | Q0는 OFF residual 지배, hotspot 위치가 다르며 적분·terminal 기여 일치 실패 |
| 기존 C7_4 보정 모델의 물리적/3D 정당성 입증 | **불충족** | 서로 다른 전체 calibration package의 2D 비교임. 독립 실험/3D truth가 아님 |
| 현재 PAPER-CAL freeze를 대체할 신규 주 baseline | **채택 권장하지 않음** | 기존 DC paper-benchmark matching 및 연구 lineage를 대체할 근거 없음 |
| Retention / 최적 MEB 설계 범위 | **현재 판단 불가** | 1T1C/thermal/selected 3D translation 검증 불포함 |

논문 명시 `Lgate=20nm`, `recess=120nm`, `Tox=5nm`, `junction=48nm`, `WF=4.8eV`를 사용했더라도 측정되지 않은 3D saddle-fin 및 S/D 상세·계면 상태는 그대로 미공개/축약이다. `Qf=0`은 nominal default **시뮬레이션 가정**이지 논문 공정 실측값이 아니다. PAPER-CAL의 GCS/GDB/Qf는 물리적 fabricated thickness/depth와 동등하지 않은 reduced-order calibration coordinate이므로, Q0↔CAL 차이를 '계면 전하만의 영향'이나 '물리 산화막 두께만의 영향'으로 분해하지 않는다.

## 6. 기존 B0F와의 관계

live GitHub baseline log의 역사적 B0F faithful control은 36nm/300K/Mesh2 Hurkx GIDL 약 `9.6096×10⁻¹⁰`으로 보고되며 이번 Q0의 36nm `9.9236×10⁻¹⁰`과 숫자 크기가 가깝다(차이 약 **+3.27%**). 이것은 소스 복제·구조 복원의 **정성적인 lineage 일관성 단서**이나, 과거 B0F 보고는 A로 기술된 곳이 있고 신규 값은 A/μm로 표기되므로 **AreaFactor/폭 정규화와 수치 mesh-family 동일성을 점검하지 않고 exact 재현이라고 주장하지 않는다.** B0F의 nominal DC mismatch(Vth≈1.233V vs paper 0.656V 등)는 이미 알려져 있으며 이번 GIDL/Cgd 전용 실행으로 해결되었다고 주장할 수 없다.

## 7. 향후 채택 gate — 이번 세션에서는 시행하지 않음

아래는 **남은 검증요건을 기록한 것**이며, 추가 코딩·실행 준비 작업을 시작하지 않았음.

1. Cgd **31nm SVisual 추출 누락**(AC SDevice는 `done`). 15-point 완전성은 이 값 회수 전까지 `14/15`로 유지.
2. Faithful-Q0의 실제 전체 Si hotspot에서 localized mesh convergence와 TDR 기반 위치/분포·적분 확인. 특히 전체 최대가 기존 GIDL outer ROI 바깥에 있다는 문제.
3. ON−OFF와 q∫BTBT 차이: 2D current normalization / integration domain / contact partition / numerical subtraction floor / 물리적 collection efficiency 차이를 구분. OFF residual의 미시적 전류 경로 규명.
4. Q0와 PAPER-CAL 구조 전체 보정 패키지를 바꾼 상태에서 인과성을 분리하는 민감도·3D 또는 원논문 추가 증거(필요 시) 확보.
5. 높은 수준의 GIDL/Retention 주장을 하기 전 PAPER-CAL Atlas L2 mesh lineage↔역사적 FZ-C 차이(+86.86% terminal, −64.64% integrated BTBT) 제약도 유지.

**정리:** Faithful-Q0 300K 데이터는 하나의 완결된(AC 31nm는 제외) **독립 2D 구조 대조 연구 결과**로 보존할 가치가 있지만, 이것을 '보정모델 신뢰성이 입증됐다'는 evidence로 승격시키면 안 된다. 오히려 **MEB–Cgd 및 총 누설의 방향성은 robust할 수 있으나, BTBT hotspot과 기여율은 calibration/geometry에 크게 의존한다**는 경계선을 제시한다.