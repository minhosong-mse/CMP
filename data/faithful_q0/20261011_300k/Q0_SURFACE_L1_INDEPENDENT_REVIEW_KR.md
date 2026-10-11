# CMP Faithful-Q0 Phase 1 — 표면 BTBT 핫스팟 국소 메시 보강 독립 분석

**기준일:** 2026-10-11 (KST)  
**입력 자료:** 사용자가 직접 실행·업로드한 `CMP_Q0_PHASE1_SPLIT6_15MEB_EVIDENCE.zip` (6개 SWB 프로젝트 × 15개 MEB, 300 K)  
**비교 자료:** 기존 Faithful-Q0 300 K 원본 ZIP 및 독립 검증 마스터 CSV  
**상태:** **원본 출처·추출·대응관계 QC 통과 / 수치 수렴성은 아직 미검증**  
**보존:** 기존 Faithful-Q0·PAPER-CAL freeze 및 GitHub 파일 변경 없음. 새 TCAD 실행 없음.

## 1. 어떤 실험이었는가?

기존 Faithful-Q0에서 MEB를 추종하는 GIDL Core refinement가 전역 BTBT 핫스팟(X≈2.34 nm, Y≈266.25 nm)을 충분히 포함하지 못한다는 가설에 대해, SDE 구조·물리 보정·SDevice 설정을 그대로 두고 **SurfaceRefineLevel=1**로 새 표면 국소 메시 영역을 추가했다. 관측 결과는 원래 계산값의 메시 민감도를 확인하는 실험이며, 새 메시가 물리적으로 옳거나 수렴했다고 검증하는 실험은 아직 아니다.

- Outer: X≈0–15 nm, Y≈258–276 nm.
- Core: X≈0–8 nm, Y≈263–270 nm.
- 실제 SDE diff (`SDE_36NM_MINIMAL_DIFF.patch`) 확인: 모델 구조·도핑·접촉·GCS=1·GateDepthBoost=0·Qf 미추가, 기존 MEB 추종 GIDL Core 불변. 추가된 것은 새 refinement placement 및 메시 출력 안내; 물리 모델 보정 없음.
- ON·OFF·SPATIAL 모두 같은 MEB에서 내용상 같은 SDE (일부 ON 파일의 끝 빈 줄 제외), 동일 300 K / Vd=1.2 V / Vg=−0.7 V / MeshLevel 2. SDevice Hurkx는 ON·SPATIAL에만 켜짐.

## 2. 원본 자료 독립 QC

- ZIP 내부 **총 1,201개 항목** = 원본 **1,197개** + 파생 파일 4개. **1,197 / 1,197** 원본 항목의 바이트 수와 SHA-256을 manifest와 독립 대조하여 일치.
- 깊이 `31,33,36,39,41,42,43,44 / 45,46,47,48,49,50,51 nm`. 전반부 8개, 후반부 7개 SWB 복사 프로젝트로 수집. 각 깊이의 ON/OFF/SPATIAL summary **45 / 45**, 실제 SDevice 종결 로그 **45 / 45** 확인. ON/OFF 최종 바이어스 도달, CurvePoints=222, 기본 terminal KCL 내부 검사 통과.
- 각 깊이에서 ON vs SPATIAL terminal Id는 사실상 동일. SDE 메시 삼각형 수도 ON/OFF/SPATIAL에서 일치.
- 36 nm 기존 메시 삼각형 15,000개 → 새 메시 16,564개 (**+10.43%**). 전체 15개에서 삼각형 수 약 **10.11~10.64% 증가**.
- **TDR·PLT** 원본 포함: 31/36/41/48 nm의 공간 SDevice TDR·메시 TDR, 그리고 같은 깊이의 ON/OFF/SPATIAL PLT. 다른 깊이의 TDR은 ZIP에서 확인되지 않음.
- 로그의 정상 종료는 수렴성과 전류 차분의 충분한 유효숫자를 자동 보장하지 않는다.

## 3. 새 메시 적용 전후 정량 비교

**범위:** Faithful-Q0 원래 Mesh L2 vs 동일 Faithful-Q0 + SurfaceRefineLevel 1. PAPER-CAL와 직접 결합된 결과가 아님.

| MEB (nm) | 총 drain Id 변화 | 전체 Si BTBT 적분 변화 | BTBTmax 변화 | E@BTBT 변화 | BTBT 핫스팟 X (nm) |
|---:|---:|---:|---:|---:|---|
| 31 | +53.55% | -6.98% | +62.32% | +96.36% | 29.30 → 2.34 |
| 36 | +47.66% | -17.68% | +1.80% | +25.37% | 2.34 → 2.34 |
| 41 | +42.85% | -37.92% | -32.71% | +25.04% | 2.34 → 2.34 |
| 48 | +37.79% | -75.81% | -54.33% | +18.83% | 2.34 → 2.34 |
| 51 | +36.01% | -83.47% | -59.36% | +18.75% | 2.34 → 2.34 |

세부 15개 전 조건(총 drain ON/OFF, 전류 차분, BTBT 전체 적분·최댓값, 핫스팟 XY, 국소 전계, 삼각형 개수·원본 노드 등)은 `ALL15_BEFORE_AFTER_INDEPENDENT.csv` 참조.

**주요 관찰:**

1. 총 drain Id는 **전 15개에서 증가**(+36.01~+53.55%). ON뿐 아니라 OFF도 거의 같은 비율로 증가. **이는 BTBT가 크게 증가했다는 뜻이 아니다.**
2. 전체 Si BTBT 적분은 **전 15개에서 감소**(31nm −6.98%, 36nm −17.68%, 41nm −37.92%, 48nm −75.81%, 51nm −83.47%). 깊은 MEB에서 국소 메시 민감도가 큼.
3. 31 nm의 **전역 BTBT 최대점 X가 29.30 → 2.34 nm로 바뀜**. 33–51 nm는 X≈2.34 nm 근처를 유지하나, Y는 과거 약 266.25 nm에서 새 메시의 약 267.42~267.66 nm로 이동. 이것이 실제 생성영역 변화인지 메시 노드에 따른 최대값 교체인지 더 정밀한 수렴성 검사가 필요.
4. 총 Id의 깊이별 순위는 여전히 단조 감소. 31→51 nm 감소 배율은 기존 약 **2,585.5×**, 신규 약 **2,918.9×**. 따라서 MEB 방향성은 유지되지만 **정량값 및 공간 BTBT 메커니즘의 수치 안정성은 확보되지 않음**.
5. 이번 두 메시 결과만으로 **수렴 완료**, **Q0가 실제 BCAT 특성과 일치**, **PAPER-CAL 결과가 반증/입증되었다**고 주장할 수 없음.

## 4. Phase 2의 중요한 단서: 전자/정공 분리 접촉 전류

원본 `nNN_des.log`의 최종 접촉 테이블에는 drain 전자·정공·합계 전류가 각각 출력되어 있다. 이 전자 성분을 별도로 뽑아 ON−OFF를 계산했다. 원본 로그는 전자·정공 성분을 약 4자리만 출력하므로 아래 값은 **근사치**다.

**36 nm (단위 A/μm):**

- ON 총 drain 전류: `1.46529363534e-9`.
- OFF 총 drain 전류: `1.46529262383e-9`.
- **총 ON−OFF**: `1.01151e-15`.
- 원본 공간 BTBT 적분을 현재 2D 폭 정규화로 환산한 `q∫G_BTBT dA`: 약 `1.137e-15`.
- **drain 전자 성분 ON−OFF**: 약 `1.135e-15` (**공간 BTBT 환산값과 약 0.15% 차이**).
- ON drain 정공 성분: 로그 기준 약 `1.465e-9`, 총 drain 전류 대부분 차지.

전체 15개 깊이에서도 `q∫G_BTBT`와 **drain 전자 성분의 ON−OFF 차이**가 로그 표시 정밀도 기준 **최대 약 1.59% 이내**로 일치했다. 한편 `q∫G_BTBT` / 전체 drain ON−OFF 비는 31nm 약 1.11 → 51nm 약 4.88로 증가한다. 이 점은 이전 적분-전체 전류 차이의 원인이 단순 적분 오류만이 아니라 **전자와 정공 단자 전류의 응답/상쇄**와 관련될 가능성을 지지한다.

**주의:** 해당 관찰은 BTBT 전자 생성과 drain 전자 전류 차이의 수치적 연관성을 보여주는 것이지, 정공이 흐르는 **구체적인 물리적 기원(SRH, 접합 경로, 기타 현상)을 확정하지 않는다.** 로그의 정공 전류 반올림 때문에 정공 성분의 미세한 ON−OFF 차이를 직접 정확히 뺄 수 없다. Causal/physical diagnosis는 후속 Phase 2에서 추가적으로 검증해야 한다.

## 5. 결론 및 다음 실행 우선순위

**판정:** `PHASE1_NEW_MESH_EXECUTED_AND_SOURCE_QC_PASS / MESH_CONVERGENCE_PENDING`.

**먼저 할 일:** 동일 프로젝트 복사본에서 **SurfaceRefineLevel=2**만 적용한 **31/36/48/51 nm** ON+OFF+SPATIAL 비교. 31nm는 핫스팟 최대점이 바뀌었고, 48/51nm는 깊은 MEB BTBT 적분의 메시 의존성이 특히 큼. 41nm는 PAPER-CAL BTBTmax 비단조 최대점을 비교할 기준점이므로 가능하면 함께 검증. 기존 결과를 덮어쓰지 않고, 원본 TDR/PLT/CMD/로그 모두 남길 것.

**검증 기준:** Level0→1과 Level1→2의 동일 지표 변화율을 비교한다. `BTBTmax`, `Xhot/Yhot`, `E@BTBT`, `∫BTBT`, 단자 ON/OFF, 작은 `ON−OFF`의 수치 정밀도, 메시 요소 수 및 실제 국소 크기를 함께 확인. Level1→2에서도 유의한 변화가 남으면 수렴 판정 보류·추가 refinement 또는 geometry/interface 분석.

**그다음 Phase 2:** SDevice `Digits=5`로 실행된 매우 작은 ON−OFF 전류 차분을 더 높은 수치 정확도로 검증하고, 접촉별 **전자/정공 분리 전류**, SRH 및 전류밀도/전위/밴드 정보를 확인하여 OFF 상태의 큰 정공 지배 누설을 설명. solver/plot 옵션 변경이 필요하면 설치 버전 공식 매뉴얼과 실행 부모 CMD를 대조한 후 진행.

**하지 않을 것:** 이번 Phase 1에서 Cgd 전체 재계산, DC 전 깊이 전면 재실행, PAPER-CAL freeze 변경, mesh difference를 물리적 맞음의 증거로 해석, retention 개선/48nm optimum 주장.

## 6. 첨부 구성

- `ALL15_BEFORE_AFTER_INDEPENDENT.csv` — 전 깊이 소스 기반 계산표 및 전자/정공 로그 지표.
- `SDE_36NM_MINIMAL_DIFF.patch` — 이전 SDE와 새 SDE의 실제 변경 비교.
- `01_TotalDrain_before_after.png` — 총 drain 전류 전후 비교.
- `02_IntegratedBTBT_before_after.png` — 공간 BTBT 적분 전후 비교.
- `03_Xhot_before_after.png` — 핫스팟 X좌표 전후 비교.
- `04_BTBTElectron_vs_TotalDelta.png` — 공간 BTBT 환산값/전자 ON−OFF/총 ON−OFF 관계.

**원본 ZIP 및 과거 Q0 결과의 재가공·위조 없음.**