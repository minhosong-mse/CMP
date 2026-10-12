# 2026-10-12 BTBT spatial / ROI / mesh evidence checkpoint

**상태: 중간 관측 기록 / 일부 후처리 완료 / 후속 검증 미실행. 결론·모델 채택·설계 최적화 판단 없음.**

## 1. 대상과 조건

- `B0-2D-PAPER-CAL` post-freeze Atlas L2: 300 K, 15 MEB (31–51 nm), Hurkx ON, Vd=1.2 V, Vg=-0.7 V, MeshLevel=2. Frozen effective calibration: GCS=2.3, GateDepthBoost=25 nm, Qf_Int=2.55e12 cm^-2, WF=4.8 eV. 기존 검증 원본: `data/paper_cal/atlas_300k_20261008/processed/MEB_300K_ATLAS_MASTER_VALIDATED.csv`.
- `B0-2D-FAITHFUL-Q0 Surface-L1`: 300 K, Hurkx ON, 같은 GIDL 바이어스; GCS=1, GateDepthBoost=0, Qf=0 모델 가정. 기존 원본/TDR 보존: `data/faithful_q0/20261011_300k/`. PAPER-CAL과 물리·메시 계열 구별.
- 별도 **340 K PAPER-CAL SVisual 화면** 3개에서 전역 BTBT 최대점을 확인했으나, 해당 원본 TDR/전처리 덱에 대한 이번 세션의 독립 QC는 없다.

## 2. PAPER-CAL 300 K: 기존 whole-Si 적분과 hotspot 재대조

전체 15 MEB [수치 CSV](../../data/btbt_roi_20261012/PAPER_CAL_300K_ATLAS_15MEB_HOTSPOT.csv), [추세 SVG](../../assets/images/paper_cal/btbt_roi_20261012/PAPER_CAL_300K_WHOLE_SI_BTBT.svg).

| MEB nm | whole Si signed BTBT integral | BTBTmax cm^-3 s^-1 | Xhot nm | Yhot nm |
|---:|---:|---:|---:|---:|
| 31 | 418379.463 | 2.9862e+22 | 32.812 | 254.297 |
| 33 | 527268.697 | 6.7707e+22 | 33.984 | 253.594 |
| 36 | 1151025.170 | 2.4609e+23 | 36.328 | 252.891 |
| 39 | 1682352.329 | 6.8755e+23 | 38.672 | 252.174 |
| 41 | 1551265.196 | 8.6813e+23 | 40.430 | 252.174 |
| 48 | 618401.525 | 6.6297e+23 | 47.461 | 252.174 |
| 51 | 347810.228 | 4.5812e+23 | 50.391 | 252.174 |

기존 추출 기준 **whole-Si signed BTBT integral**: 36/39/41 nm = **1,151,025.16951 / 1,682,352.32862 / 1,551,265.19607**. 전역 최대점은 GateTop 인근이며, 15개 Xhot 범위는 32.812–50.391 nm, Yhot 범위 252.174–254.297 nm. **본 세션에 PAPER-CAL 300 K의 영역별 ROI 적분 결과는 아직 없음.**

## 3. Q0 Surface-L1: 실제 300 K TDR 4개 ROI 재적분

기존 공개 복원 TDR의 Si `R.Body` 삼각형을 이용해 vertex Band2BandGeneration을 삼각형 내 선형 보간하고, 영역별 경계로 polygon clipping하여 적분한 수치. 전체 Si 적분은 원래 SVisual 값과 교차 검산했다.

**시험용 비중첩 영역, 좌표 μm:** Surface `X=[0,0.015], Y=[0.240,0.300]`; Gate-side `X=[0.015,0.065], Y=[0.240,0.300]`; Remaining = Silicon 전체 – 두 영역. **이는 생성 영역 측정용 ROI이며 실제 SDE refinement 창이나 확정된 물리 경계를 의미하지 않는다.**

| MEB nm | Whole signed | Surface signed | Gate-side signed | Surface % | Gate-side % |
|---:|---:|---:|---:|---:|---:|
| 31 | 60815.268199 | 6412.692780 | 54402.578432 | 89.455 | -0.000 |
| 36 | 7096.760869 | 771.589801 | 6325.171097 | 89.128 | -0.000 |
| 41 | 658.736520 | 116.675182 | 542.061333 | 82.288 | 0.000 |
| 48 | 23.381647 | 13.543978 | 9.837590 | 42.074 | 0.000 |

[정밀 수치·원본 대비 상대오차 CSV](../../data/btbt_roi_20261012/Q0_SURFACE_L1_300K_ROI4.csv) / [ROI 비중 SVG](../../assets/images/paper_cal/btbt_roi_20261012/Q0_SURFACE_L1_300K_ROI_SHARES.svg). 31/36/41/48 nm에서 원래 SVisual whole-Si 값 대비 각각 **-0.000052% / -0.000013% / +0.000052% / +0.000268%**; 9타일 합과 whole-Si 적분도 부동소수 오차 범위에서 일치. Signed와 positive-only 수치는 기존 분석에서 별도 계산했으며 본 표는 signed 기준.

보존 원본 TDR 멤버는 Q0 31 `raw/spatial/first8/n47_des.tdr`, 36 `n49_des.tdr`, 41 `n51_des.tdr`, 48 `raw/spatial/last7/n58_des.tdr`. 원본 source archive 및 복원 방법은 `data/faithful_q0/20261011_300k/README.md`를 따른다.

## 4. SVisual 사용자 화면에서 별도로 확인한 BTBT 최대점

- **Q0 Surface-L1 300 K**의 `MEB_GIDL_ON_2_Copy` 화면: 31/36/39/41/46/48/51 nm 전역 최대점 X≈2.34375 nm; 31/36/39/41의 Y≈267.656 nm, 46/48/51의 Y≈267.422 nm. [7노드 전사·마스터 대조 CSV](../../data/btbt_roi_20261012/Q0_SURFACE_L1_300K_SVISUAL_7NODES.csv).
- Q0 36 nm 전계 `Abs(ElectricField-V)` 화면 **전 영역 표시 최대** ≈2.13466×10^7 V/cm. 저장 마스터의 **BTBT 최대 좌표의 전계** ≈1.618469×10^6 V/cm로, 정의가 다른 두 값이다.
- **PAPER-CAL 340 K, `MEB_GIDL_ON` 사용자 화면:** 36/39/41 nm 각 `n66/n68/n70_des`의 BTBTmax≈1.11179×10^24 / 3.46715×10^24 / 4.20020×10^24 cm^-3 s^-1; Xhot≈35.742 / 38.672 / 40.430 nm, Yhot≈252.174 nm 공통. [화면 전사 CSV](../../data/btbt_roi_20261012/PAPER_CAL_340K_SCREENSHOT_HOTSPOT_3MEB.csv). 사용자 제공 온도 식별 340 K, 단 이번 세션의 pp/log/TDR QC 없음; **340 K의 영역별 적분도 미실행**.
- 이들 SVisual 캡처에는 Surface 인접 및 Gate-side 근처의 서로 다른 국소 생성 분포가 보이나, **표면 영역 자체의 국소 최대·적분값은 별도 수치 측정 전**이다.

## 5. 메시 이미지/SDE 내용 교차 확인

- 사용자 제공 `MEB-test` `n8_msh` 전체·확대 화면: SVisual status **15,279 elements / 7,384 points**. Gate-side 계면 부근에는 작은 삼각형, 상부 Drain/Surface 쪽에는 비교적 큰 삼각형이 관찰됨. 사진만으로 해당 노드의 전처리 parameter, 온도, 모델 결과를 확정하지 않음.
- 현행 [PAPER-CAL Atlas L2 SDE](../../code/sde/paper_cal/atlas_300k/CMP_B0_2D_PAPER_CAL_MEB_ATLAS_SDE.cmd): `GateTop=MEBDepth`; `RefWin.GIDLCore` X=`GateTop-0.004 .. GateTop+0.008` μm, Y=`YgR-0.0015 .. YoxR+0.0035` μm. 여기에서 `YoxR≈0.252174 μm`, `YdL≈0.267174 μm`. 15 MEB의 기존 전역 핫스팟 좌표는 해당 이동 Core 안에 포함됨.
- 현행 SDE에는 별도의 Surface Outer/Core refinement 창이 없다. Q0 Surface-L1의 기존 보강 구역은 Outer X=0..15 nm/Y=258..276 nm, Core X=0..8 nm/Y=263..270 nm로 **Q0 geometry 기준**이며, PAPER-CAL에 그대로 적용한 것은 아니다.
- 이전 Q0 original L2→Surface-L1 변경시 기존 repository report의 수치: 36 nm whole-Si BTBT integral -17.68%, total drain Id +47.66%; 48 nm -75.81% / +37.79%; 31 nm 전역 Xhot 29.30→2.34 nm. **이것은 메시 민감성 기록이고 mesh convergence 검증은 아님.**

## 6. 준비/미완료를 명시한 다음 작업

- [300 K 36/39/41 nm 재실행 파라미터·whole-Si 회귀 기준 CSV](../../data/btbt_roi_20261012/PAPER_CAL_300K_ROI_TARGETS.csv). `MEBDepth=0.036/0.039/0.041 um`, `MeshLevel=2`, `T=300 K`, Hurkx ON, `Vd=1.2,Vg=-0.7`; 다른 보정변수 및 geometry 변경하지 않음.
- 원래 300 K 공간 TDR이 다른 온도 실행으로 덮였다는 사용자 보고에 따라, 별도 SWB copy에서 같은 Atlas L2 300 K 계열을 재생성·검증하는 작업이 준비됐다. **신규 300 K TDR 및 해당 ROI CSV는 이 커밋에서 미수신·미검증.**
- PAPER-CAL의 표면 국소 hotspot 좌표와 영역별 signed integral을 추출한 뒤, GateTop-following GIDL 창은 보존하고 표면 쪽에만 국소 보강을 추가하는 별도 메시 비교가 논의됐다. 후보 Surface Outer (X0..15 nm, Y255..279 nm), Core (X0..8 nm, Y260..274 nm)는 **아직 검증하지 않은 제안 범위**이다. Surface-L1/L2, 15 MEB 재실행, 1T1C/3D는 이번 세션의 완료 결과가 아니다.
- **결정 보류:** 39 nm 적분 peak의 공간적 원인, 표면 메시 수렴, PAPER-CAL 주 모델 채택, 물리적 GIDL/Retention 해석은 이 기록에서 결론내리지 않는다.

## 7. 근거 위치와 보존 한계

원본 Atlas/ Q0 데이터는 이미 GitHub에 별도 보존되어 있으며 이 checkpoint에서는 수치와 필요한 파생 표/벡터 그래프만 새로 보존했다. 사용자 SVisual **스크린샷 원본 비트맵은 이번 커밋에 첨부하지 않았으므로**, 화면 전사값은 사후 원본 화면/ TDR 재검증 가능한 관찰 기록으로만 취급한다. 채팅에서 준비된 SVisual ROI 실행용 CMD는 **서버 실행 미검증**이므로 실행 성공 결과로 기록하지 않았다.

**상태: evidence captured / ROI validation in progress / no scientific conclusion or freeze change.**
