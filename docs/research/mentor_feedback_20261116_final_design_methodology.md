# 2026-11-16 멘토 피드백 및 최종 MEB 설계 범위 도출 방법론

> **상태: 멘토 피드백 기록 / CMP-PROTOCOL 제안(PLANNED, NOT FROZEN).** 2026-11-16 사용자 전달 내용에 근거. 이번 변경은 후속 연구 우선순위와 평가 방법을 정리하는 문서 작성뿐이며, SDE/SDevice 모델·수치·물리 조건·기존 원본을 수정하거나 새로운 시뮬레이션을 실행하지 않았다.

## 1. 피드백 원문 요지

1. 주차별 Master Parameter Table: 2D 초기 수치 → 2D 수정/보정 → 3D 초기 최적화 수치 → 현재 3D 구조 및 수치. 변화 이유와 구조 그림을 함께 제시. 마지막에 현 baseline의 최종 파라미터 표와 구조를 나란히 배치.
2. Baseline 점검: VDD 고정, 저장노드 VSN에 따른 역산 방식은 타당한 접근. Subthreshold (SS-related channel leakage), GIDL 및 junction leakage 등의 전체 누설전류를 고려하여 retention time을 역산. 또는 특정 retention time(사용자 전달 예시 64 ns)의 허용 누설전류를 역산해 비교. 시간 단위 및 목표의 의미는 확인 필요.
3. 온도: 233K/300K는 유지하고 고온 조건은 JEDEC 관련 DRAM 동작온도 범위를 근거로 재선정하는 것이 바람직.
4. Ion: 이동도, 캐리어 밀도와 채널 전류밀도 등 기여를 확인.
5. 최종 판단: 300K BEST 조건을 확정하고 Ion, Ioff, DIBL, GIDL, SS, Retention t 6개 축에 성능 저하율을 정규화하여 육각형(radar)으로 표시. 지표별 허용 저하 기준을 점선으로 표기. 모든 MEB × 온도에 대해 P/NP 판정표를 구축.
6. 온도 확장 데이터: X=MEB, Y=temperature, 등고선/색상=관심 물리량 또는 전류. 이를 바탕으로 온도 의존적 유효 MEB 설계 범위를 제시.

## 2. 현재 데이터와 연구 범위

- 현재 주 lineage: `3D-Sun-SADDLE-V1 / Flat upper S/D`, Hurkx ON working baseline. 기존 2D, 3D 초기 lineage는 역사적 근거로 보존.
- [100-case IVSN archive](../../data/3d_ivsn_meb36_60_20261116/README.md): 36–60nm 1nm × 233/300/340/380K. Ccell=10fF, WL=-0.7V, BL/body=0V, SN=0.8–1.0V, 101 points, t_est 계산. 100/100 complete numerical estimates, **25 cold KCL warnings** at 233K. 16개 기존의 100ns short Hold는 초기 기울기 검증만 수행; 직접 0.8V crossing 없음.
- [175-case 300K DC/GIDL](../../data/3d_meb_all25_full_extract_20261031/README.md): 24–48nm 1nm, 7 modes; 36/41/48nm 300K의 Ion, DIBL 및 Hurkx excess가 [5×4 temperature DC data](../../data/3d_meb_temp140_partial_20261109/MEB_5x4_TEMPERATURE_METRICS_PARTIAL.csv)와 수치 일치. 모든 DC 지표 정의/mesh/physics까지 자동 등가로 간주하지 않음; SS window와 Ioff 추출 조건의 차이가 있으므로 동일 정의로 재추출/QC.
- DC/온도 138/140 target complete. 54nm/340K Mode1 n1686(+0.108V에서 중단) → Ion/Ioff/high-Vd SS/DIBL 결손; 36nm/380K Mode5 n1979(-0.66372928V에서 중단) → GIDL ON/Hurkx excess 결손. 4개의 short Hold 실패(36/380, 54/380, 60/380, 48/233)는 별도.
- 기존 300K exploratory 44–55nm는 interpolation 기반의 NOT FROZEN 후보. 최신 36–48nm 정밀 자료에서는 43nm부터 36nm 대비 Hurkx excess 50% 감소와 retention 2배 조건을 함께 만족하지만, 새 방법론의 최종 BEST, 허용치, P/NP 또는 설계 범위가 확정된 것은 아님.

## 3. Master Parameter Table 및 구조 변천 기록 (병행 작업)

주차/단계별 표: stage, date/week, model lineage, paper reference, physical geometry (Lg, Wfin, Tox, recess, saddle geometry, MEB/DBCAT, junction depth), gate WF, doping, physics/BTBT, mesh policy/AreaFactor, bias, Vth/SS/Ion/Ioff/DIBL, 구조 그림·commit·증거 링크, 변경 이유, validation status.

권장 흐름: B0-2D-Legacy → B0-2D-PAPER-CAL (C7_4/B_QF_HALF) 및 필요시 faithful Q0 control → 초기 3D-Sun-B0 → 3D-Sun-SADDLE-V1/Flat upper S/D → 최종 working baseline 및 검증 상태. 실제 발표 주차와 수치는 당시 PPT/커밋/evidence 기준으로 매핑하고 추정으로 채우지 않는다. 논문 명시값, CMP 직접 실행값, 보정 좌표(GateCouplingScale/GateDepthBoost/Qf), 가정값 구분; 좌표 값을 실제 산화막 두께 등으로 재해석 금지. 현재 최종 물리 파라미터 표에는 구조 단면과 함께 출처/판정 상태 표기. 같은 행/그림에서 서로 다른 모델의 절대 전류를 무단 연결하지 않는다.

## 4. 최우선: Retention 프로토콜 확정

### A. 비교 조건 (후보, NOT FROZEN)

- 공급전압 VDD(예: 기존 1.2V)와 실제 Hold WL/BL/body bias를 명시해 모든 MEB/T에서 동일하게 유지. VDD와 VSN 초기 전압은 별개 변수; 기존 VSN 1.0→0.8V를 동일한 absolute loss window로 유지할지, 실제 write 결과/판독 margin에서 새 window를 정의할지 먼저 검토.
- 기존 `Ccell=10 fF`, `VWL_HOLD=-0.7V`는 CMP 비교 가정(negative-gate stress), production spec 아님. 대표점에서 Ceff(V,T)/current scaling(3D explicit geometry; 2D AreaFactor 전이 금지), 회로 및 전압·전류 부호 확인. 필요시 WL sensitivity.
- `I_loss(VSN,T)=-I_cell_SN(VSN,T)` (현재 회로의 discharge sign)로 직접 총 SN 방전전류를 측정. 실제로 활성화된 leakage physics 및 terminal path만 포함됨. 기존 PLT는 이를 측정하지만 junction SRH generation, TAT, capacitor dielectric leakage 등 모든 실소자 누설이 자동 포함되는 것은 아님.
- Mentor 요청: subthreshold channel current + GIDL 관련 전류 + junction leakage (+ 기타 기여가 있다면)를 **동일한 Hold bias와 동일 VSN에서** 구분 검증. SS는 slope의 지표이지 전류가 아님. 기존 Ioff(Vg=0,Vd=1.2V), GIDL proxy(Vg=-0.7,Vd=1.2V)를 서로 다른 bias에서 더하면 안 되며, total SN current에 이미 포함된 branch를 다시 더하지 않는다.
- Signed SN/BL/body terminal electron & hole currents, terminal KCL, matched Hurkx ON/OFF 및 junction-generation control을 이용해 기여를 진단. ON−OFF는 model sensitivity이지 독립 물리 경로의 정확한 분해라고 단정 금지. Carrier continuity와 generation/collection의 차이를 확인; 성분 합과 total SN current의 closure 및 overlap 검증. 물리 모델 추가 시 current working baseline과 분리해 대표점 bridge 수행. 실제 SDevice PP와 T-2022.03 공식 manual(Model 및 Plot 옵션)을 필요한 부분만 확인한 뒤 변경; 미검증 syntax 작성 금지.
- 저전류 233K KCL floor 및 외측 drain x≈60nm/Face91, 실제 contact/mesh 동일성 문제를 대표점(QC=36/48/54nm, 필요시 60nm; 300K/233K/고온 경계)에서 먼저 점검.

### B. 계산 경로

Primary: `t_est = integral_{Vcrit}^{Vinit} C_eff(V,T)/I_loss(V,T) dV`. 기존 101-point trapezoid 1.0→0.8V, 10fF는 current method candidate. Constant C에서 평균 누설 비교 `I_eq=Ccell*(Vinit−Vcrit)/t_est`. 단일 bias 근사 `t≈Ccell*DeltaV/I_loss(Vinit)`는 V 의존 무시한 별도 diagnostic, primary integral과 구분.

Target-time inverse check: `I_budget=Ccell*DeltaV/t_target`. 10fF, 0.2V 가정에서 64ns는 31.25nA, 64ms는 31.25fA, 32ms는 62.5fA, 16ms는 125fA. 64ns는 멘토 전달 그대로 기록하되 ns/ms 확인 전 채택 금지. 64/32/16ms는 DDR4 refresh-window reference이며 단일 cell의 실제 retention 또는 모든 DRAM의 공정 사양과 동일하지 않음. 필요 시 target time을 기준으로 comparable I_eq 또는 VSN(t_target) 비교.

Validation: 대표점에서 실제 floating Hold 초기 slope 확인, 가능한 범위의 장시간 및 0.8V crossing/Q(V) 일치 검증; write/read 판독 조건 점검. 100ns 초기-rate agreement만으로 ms/s retention 검증했다고 주장하지 않는다. 계속 실패하는 값은 NA/QC warning으로 관리; 수치 수렴과 과학적 검증 별도.

## 5. JEDEC 관련 operating-temperature 재설계 (후보)

JEDEC 원문 공식 사이트 직접 접근 제한이 있어 현 시점은 발행 제조사 DDR4 datasheet 근거의 proposal. 선택할 target(예: DDR4 JESD79-4, industrial/extended temp product)과 문서 revision/temperature basis(Tcase vs simulator device lattice temperature)를 확정해야 한다.

| 검토 온도 (K) | °C | 의미 |
|---:|---:|---|
| 233 (기존), 또는 233.15 | -40.15 / -40 | 저온/industrial reference |
| 300 | 26.85 | 기존 상온 BEST 비교 기준 |
| 340 (기존) | 66.85 | 중간 추세용; 삭제하지 않음 |
| 358.15 | 85 | DDR4 일반 refresh 경계 reference |
| 368.15 | 95 | extended DDR4 경계 reference |
| 378.15 (조건부) | 105 | 해당 grade 지원 시 확장 검토 |
| 380 (기존) | 106.85 | 기존 stress data; 새 표준 기반 온도에 덮어쓰지 않음 |

근거: Micron 8Gb DDR4 SDRAM datasheet, Features — 8192-cycle refresh windows 64ms at -40 to 85°C, 32ms at >85 to 95°C, 16ms at >95 to 105°C (해당 product grade). https://www.mouser.com/catalog/specsheets/Micron_8gb_ddr4_sdram.pdf ; manufacturer DDR4 part catalog https://www.micron.com/products/memory/dram-components/ddr4-sdram/part-catalog . JEDEC 표준 문서/JESD79-4 revision 및 적용 제품 범위는 별도 최종 확인. Tcase의 등가 lattice 온도 가정은 명시. 233K/300K 기존값 유지, 358.15/368.15K를 core 후보로, 340K 중간해상도와 378.15K 옵션은 목표에 맞춰 선택. 64ms/32ms refresh frame ≠ cell retention threshold ≠ per-command tREFI.

## 6. DOE 우선순위와 re-run 전략

| 순서 | 작업 | 종료 gate |
|---:|---|---|
| P1 | Retention total-leakage 정의, VDD/hold bias/VSN window/Ceff/physics 선택 및 inverse target 검토 | metric/physics/bias 명확히 문서화, representative validation plan 승인 |
| P2 | JEDEC 관련 온도 grade/수치/refresh-reference 확정 | 새 T grid와 Tcase 가정 승인 |
| P3 | 대표 36/48/54nm의 300K, 233K, 고온 경계 bridge 및 필요한 model/mesh/solver 검증 | 기존 SN-IV 대비 동일 조건 비교, component closure, signed/KCL QC |
| P4 | 고정된 protocol로 36–60nm × 확정 T의 DC/GIDL/IVSN matched sweep | 모든 6지표의 공통 case table; PASS/NA/QC warning을 보존 |
| P5 | Ion mechanism: n, mobility, current density/field/transport | 균일한 비교 ROI와 동일 bias, representative values |
| P6 | 300K BEST 조건 선택 및 reference/allowance freeze | 기준 MEB와 6개 지표의 허용 저하 근거 기록 |
| P7 | radar, P/NP table, MEB–T contour 및 최종 범위/limitations | noninterpolated P/NP, 후보 범위 및 QC boundary |

Master table/주차별 구조 정리는 P1–P5와 병행. full new sweep는 변경된 physics/voltage/mesh/extraction에 따라 실행 여부를 판단: 새 protocol이 변경된 경우 old 100 estimates와 DC archive는 historical comparator로 보존, 대표 bridge 통과 후 필요한 matrix를 새 lineage로 생성. 동일 protocol이면 기존 valid condition을 재사용하고 missing T/depth/failed cases만 추가. 이전 2개 실패 n1686/n1979는 기존 340/380K를 새 평가점으로 유지할 경우 recover; 새 grid에서 제외되어도 historical failure 기록 보존. 모든 시뮬레이션을 무조건 재실행하기 전에 대표검증으로 같은 오류가 새 DOE 전체에 확대되지 않도록 한다.

## 7. Ion mechanism 검증

동일 `Vg=1.2V, Vd=1.2V` 비교, 동일 channel region/position 및 실제 좌표·단면 설정으로 36/43/48/54/60nm 등의 대표점에서 온도별 electron concentration, effective electron mobility, current-density vector와 longitudinal transport, channel quasi-Fermi potential gradient, effective channel/body geometry를 함께 비교. Spatial maps + fixed cutline/cross-section + 정량 지표(ROI volume-weighted n, mobility 및 channel cross-section integrated electron current) 사용. Drift component q*n*mu*E 개념은 해석 보조; diffusion/quasi-Fermi gradient 및 field-dependent mobility 등 drift-diffusion 해석을 무시한 단순 곱을 total Ion이라고 주장하지 않음. 실제 available plot fields/units/axis는 deck/manual에서 검증. 구조 차이/temperature 변화 시 같은 위치와 정의의 비교 가능성 확인.

## 8. 300K BEST reference와 여섯 축 normalized loss (계속 구체화)

### Reference 선정

- 하나의 **실제 실행된** MEB(300K)를 reference로 선택. 각 축의 개별 best가 조합된 비실재 ideal point와 구분한다.
- 설계 목적 및 허용치를 먼저 합의(예: retention 최대화 subject to Ion/SS/DIBL/Ioff/GIDL guardrails; Pareto 후보 또는 knee 확인). 36nm nominal vs baseline guardrails는 exploratory prior일 뿐. 최종 BEST는 새 matched data/정의 확인 후 선택; 43–54nm 후보, 48nm or 54nm 등을 현재 미확정 상태로 유지.
- 선택된 하나의 BEST(300K)의 6개 reference 값을 모든 MEB/T에 고정하여 온도 변화의 실제 relative penalty를 보이도록 함. Reference 개선 방향(negative loss)은 저장. 필요하면 same-temperature baseline/온도만의 변화도 보조 view로 별도 계산; 두 normalization을 혼용하지 않음.

### Metric directions and draft loss definitions

| metric | 선호 | degradation % (m=case, ref=300K BEST) |
|---|---|---|
| Ion | 높음 | 100*(ref-m)/ref |
| Ioff | 낮음 | 100*(m-ref)/ref |
| DIBL | 낮음 | 100*(m-ref)/ref |
| GIDL (definition to freeze) | 낮음 | 100*(m-ref)/ref |
| SS | 낮음 | 100*(m-ref)/ref |
| t_est / validated t_ret | 높음 | 100*(ref-m)/ref |

Metric-specific allowable loss L_i in percent; zero/near-zero reference 및 floor-sensitive leakage는 absolute or log-ratio guardrail을 별도 정의해야 함. Permissible SS/DIBL 변화는 % 대신 absolute mV/dec, mV/V 기준도 검토. 참조 36nm 300K의 과거 예시(Ion >=90%, SS <= +3mV/dec, DIBL <= +5mV/V, Hurkx excess <=50%, t_est >=2x)는 탐색 proposal이지 새 BEST 기준의 허용치가 아니다.

Radar: six axes, per-axis loss-budget ratio r_i=max(0, loss_i / allowed_i); dashed regular hexagon r=1 (각 허용치의 100% 사용), inner is pass, outer is exceed. Negative loss (improvement)는 시각화 시 0으로 표시하되 원시 signed value를 별도 표에 보존. 일률적인 percent 비교를 원하면 각 축 signed/positive loss 및 metric-specific dashed threshold를 표시하는 별도 raw-loss radar도 가능. 최종 선택은 멘토와 논의. 6축 허용치에 대한 근거(공학적 guardrail, 문헌/제품 참고, 계산 sensitivity)와 단위, version을 함께 기록하며 임의 확정 금지.

Master P/NP table: `MEB_nm, TempK, 6_metrics, ref_MEB_300K, 6_signed_losses, 6_allowances, 6_loss_budget_ratios, 6_P/NP, qc_tag, all_pass, limiting_metric, t_target, source, protocol_version`. Case-level P iff **all six** metrics satisfy agreed limits and required QC; NP if a valid metric exceeds threshold; missing/not QC-approved result is NA/QC-REVIEW (not automatic NP, not pass). No imputation for P/NP; interpolated boundaries may be shown separately as exploratory visualization only. Any claim of a contiguous usable interval requires valid actual samples across it and MEB/temperature scope stated. Candidate ranges can differ by temperature; intersection over required temperatures is separate stricter result, including uncertainty if cold not validated.

## 9. 최종 그림과 결과 서술

- Raw metric maps (Ion, Ioff, DIBL, GIDL, SS, retention): X=MEB, Y=temperature, color/contour=metric; leakage/retention log scale when orders differ. Use actual grid nodes/dots; mask missing/QC cells; interpolation for presentation only, never for P/NP. Mark 85/95°C boundaries only if chosen as protocol. Add P/NP matrix/contour with 6-metric constraint intersection and limiting metric.
- Radar at 300K BEST/selected representative cases and temperatures, dashed threshold. Use same definitions/radius limits across comparable panels; label lower-is-better loss-budget representation.
- Final results: chronological baseline parameter/structure explanation → total leakage & retention-validation method → MEB×T six metrics and mechanism → 300K reference → threshold/P/NP matrix → temperature-dependent feasible range and supporting contour; limitations (cold numerical floor, Ceff, direct Hold, junction/outer-drain attribution, 3D mesh and product-spec scope).
- No final BEST/threshold/physical retention/production design-window claim yet, and no root README change before approval.

## 10. Immediate next session

P1: compare existing IVSN deck's actual enabled transport/recombination and hold bias with required total leakage mechanism; decide how to implement/validate junction and subthreshold/GIDL attribution at same SN bias. Resolve whether the mentor's time target is 64ns or 64ms before using it as a criterion; choose target temperature grade in P2. Then propose minimal representative runs, not blanket DOE. Existing complete-data archive and prior failures remain intact.
## 11. Retention target-time inversion discussion and deferred BTBT model comparison (2026-11-16)

**Status: PROPOSED / NOT FROZEN.** No deck or simulation change. The mentor additionally requested Hurkx versus NonlocalPath under identical conditions; user directs it to be kept as **deferred follow-up validation**, not on the current critical path. Compare matched geometry/mesh/temp/bias/other physics/extraction on representative depths, after current total leakage/temperature/decision workflow stabilizes. Model-specific tuning or syntax/mesh changes are not part of the current plan.

### Proposed DDR4-reference procedure

- JEDEC JESD79-4C normal/extended industrial temperature range and Micron 8Gb DDR4 SDRAM data sheet: https://studylib.net/doc/27820321/ddr4-spec-jesd79-4c ; https://www.alldatasheet.co.kr/html-pdf/2170300/MICRON/MT40A1G8SA-075%3AG/260/1/MT40A1G8SA-075%3AG.html . Manufacturer-stated 8192-cycle refresh windows: 64 ms for -40..85°C inclusive, 32 ms >85..95°C, 16 ms >95..105°C when the specific grade supports it. This is a **refresh-reference engineering screening target**, not a direct single-cell JEDEC retention requirement or tREFI.
- Proposed core anchors 233K historical low-temperature stress (-40.15°C; exact -40°C=233.15K), 300K reference, 340K intermediate historical, 358.15K (85°C, 64ms), 368.15K (95°C, 32ms). 378.15K/105°C/16ms conditional extension. Prior 380K old data is stress outside 105°C grade and must not be relabelled. If thermal crossover needs refinement, add intermediate temperatures under identical protocol; do not interpolate P/NP. Device lattice T vs Tcase assumption to be documented.
- Preserve a fixed supply/write reference VDD (candidate 1.2V), hold WL/BL/body and absolute VSN comparison window. VSN is not necessarily VDD. Pending validation, Ccell=10fF and 1.0→0.8V (ΔQ=2fC) give I_budget=ΔQ/t_target: 31.25fA (64ms), 62.50fA (32ms), 125fA (16ms). 64ns would instead be 31.25nA; do not treat it as 64ms without noting the unit correction.
- Measure **signed total SN discharge current at each VSN** for same bias and all implemented leakage mechanisms. Integrate Ceff/(-I_SN), then compute equivalent mean discharge I_eq=ΔQ/t_est. Use both t_est ≥ t_target and I_eq ≤ I_budget; mathematically equivalent under same positive ΔQ. Do not add separately biased Ioff and GIDL or double count transport mechanisms; instantaneous I_SN(Vinit) is not I_eq. If using fixed-time transient, test VSN(t_target)≥Vcrit; when only current sweeps are available, integrate to threshold, do not invent VSN beyond sweep. Absolute target and separate relative 300K six-metric loss allowance are distinct.
- Pilot screen on archived 100-case estimates (legacy assumptions only, no new validated physical retention): at 300K 25/25 satisfy proposed 64ms, t_est 67.161–233.837ms, I_eq goes 29.779→8.553fA with MEB increasing. At 340K 0/25 satisfy 64ms, t_est 10.112–18.647ms, I_eq 197.777→107.255fA. At 233K nominal 25/25 satisfy 64ms but all 25 carry low-current KCL warnings and 233K is a stress approximation; mark QC-REVIEW, not a physical pass. 380K not in proposed grade, no standard-derived P/NP assigned. 358.15/368.15/378.15 K values are not yet simulated under this protocol. Source: ../../data/3d_ivsn_meb36_60_20261116/RETENTION_MATRIX_SECONDS.csv.
- If pilot predicts no window at a required temperature even at deepest MEB, report that result transparently; do not tune thresholds or models simply to force a pass. Validate total leakage/mesh/Ceff and temperature-specific threshold first; if no feasible window is supported, discuss trade-off and necessary redesign. This criterion is not frozen and must not be used to claim product compliance.


## 12. Bounded retention verification: actual executed model check (2026-11-16)

**CMP-EXECUTED evidence review; SRH pilot PLANNED / NOT FROZEN.** User approves a short verification only, with fallback to model-qualified IVSN estimation if the pilot is blocked; prioritize JEDEC-reference temperature sweep afterward.

- Inspected the external Nov-13 PP and solver log `pp873_des.cmd / n873_des.log` (37nm, 300K), also 59nm current data. The deck connects drain=SN, source=BL, gate=WL, substrate=ground; BL/body=0V, WL=-0.7V, ideal forced SN 0.8→1.0V, Ccell=10fF. It solves Poisson/electron/hole/contact/circuit. The log explicitly reports `Without SRH-Recombination`, with Silicon-specific `With Band-to-Band Tunneling / Hurkx model`. Existing signed terminal current therefore includes enabled transport and Hurkx BTBT, but not SRH contribution to junction generation. Not all physical leakage mechanisms are represented. Do not sum independent-bias Ioff/GIDL on top of total SN current.
- 300K control 37nm (n873): t_est=76.210764ms, I_SN(1V)=-38.481332fA; 59nm (n1203): t_est=228.008261ms, I_SN(1V)=-11.831760fA. At 340K 59nm (n1758): t_est=18.460525ms. Existing 16 short Hold initial-rate checks are consistent within 0.0766%, not full threshold crossings.
- Sentaurus Device User Guide T-2022.03 Ch.16 pp.474–479 verifies explicit SRH activation and DopingDependence/TempDependence lifetime options. Minimal separate pilot: retain all parent physics, bias, geometry, mesh and solver; change only `Recombination(Band2Band(Hurkx))` to `Recombination(SRH(DopingDependence TempDependence) Band2Band(Hurkx))`. Built-in lifetimes are not calibrated to this DRAM. Use a separate SWB branch/project; preserve original runs. No TAT, NonlocalPath, mesh or lifetime retuning in this pilot.
- Run only 37nm/300K and 59nm/300K, then 59nm/340K if first two converge (existing matched controls). Check full 0.8–1.0V range, 101 finite points, discharge sign, KCL and actual log model activation; integrate same C and compare t_est/I_eq/64ms screening classification. If meaningful impact, carry the new explicitly labelled model into the temperature campaign; if no material impact, document it and retain a consistent chosen physics; if blocked after one minimal retry, keep historical Hurkx-only t_est qualified as modeled leakage estimate and proceed without broad detours. No measured cell-retention claim. No new SDevice execution as of this note.
- After pilot: use 300K anchor and JEDEC-reference core 233.15/358.15/368.15K, keep 340K intermediate if useful, 378.15K only for selected 105°C grade; old 233/380K retained as historical. Final grid/model and six-metric thresholds remain decisions pending pilot. No full direct 64ms transient or manual leakage component partition required for this bounded stage.


## 13. User-approved fast-track DOE (2026-11-16; supersedes the priority in §12)

**Protocol selected / source prepared / external execution PENDING.** User explicitly directs postponement of the SRH pilot and additional physical calibration to prioritize the six-metric temperature-dependent MEB design-range result. Preserve §12 as historical proposal, not an active requirement. Hurkx ON (except paired mode 6 OFF), unchanged 3D-Sun-SADDLE-V1 Flat upper S/D, WF 4.8 eV, original SDE and solver lineages. No physical retention calibration claim.

- DBCAT_nm: every integer 36 through 60 (25), TempK: 233.15 / 300 / 340 / 358.15 / 368.15 (5), RunMode: 0 / 1 / 5 / 6 / 7 (5). **125 MEB×T conditions, 625 SDevice target nodes**; 25 depth meshes (upstream of T/mode, if copied tree permits). 378.15 K optional grade and 380 K historical stress excluded. Set both TempK and RunMode before the independent SDevice solve. Do not cascade SDevice instances. No output-current modes 2/3/4.
- Copy existing `CMP_3D_Temp` into a separate SWB project, e.g. `CMP_3D_JEDEC_36_60`. Keep SDE unchanged. Replace SDevice original source (not pp file) with [CMP_3D_JEDEC_5MODE_des.cmd](../../code/sdevice/3d_sun_saddle_v1/CMP_3D_JEDEC_5MODE_des.cmd). Add mode 7 for IVSN. Enable modes 0/1/5/6/7 only; ensure all five temperatures and integer depths. Preprocess one depth/temperature across each mode first and check pp grid, temperature, physics, goal, and output filenames; then queue full selected DOE. Prioritize 300K to obtain BEST reference; no need to wait for unrelated validation. Keep earlier projects untouched.
- The integrated source was reconstructed from actual executed 300-K DC examples (pp74/136/236/261) and actual IVSN pp873. Static branch expansion reproduces all five parent decks ignoring whitespace/comments and the intentional mode-1 output-only additions. All 25 T×mode static expansion checks passed; not native SWB preprocessing or SDevice runtime verification. SWB conditional preprocessing per Synopsys Workbench User Guide Appendix A (#if/#elif); exact Ion spatial Plot schedule verified SDevice T-2022.03 pp.178–179. New mode-1 Plot output eMobility/eCurrent/Vector plus existing eDensity at normalized gate ramp t=0.6 (Vg=1.2, Vd=1.2) permits later transport analysis without a separate simulation. Keep full Vg=2V endpoint. Confirm bias in TDR/log rather than assume filename alone.
- Modes 0/1: Id–Vg low/high Vd=0.05/1.2V, gate end 1.5/2.0V. Ion: high Vd Id at Vg=1.2V; Ioff: high Vd Id at Vg=0V; SS: high Vd log-current interpolation Vg at 1e-10 and 1e-8 A, voltage difference/2 decades; DIBL=(Vth_low−Vth_high)/1.15 in V/V, Vth at 8.5e-8 A using log-current interpolation. Same existing 3D extraction proxies.
- Modes 5/6: Vd=1.2 V, Vg=-0.7 V, Hurkx ON/OFF; GIDL proxy = signed drain current ON−OFF. Retain both absolute endpoint currents and QC; do not relabel as pure collected GIDL.
- Mode 7: unchanged actual mixed-mode IVSN with SN=1.0→0.8 V discharge integral, 101 samples sweeping 0.8→1.0 V, fixed 10 fF, WL=-0.7V, BL/body=0V. t_est=trapezoid integral C/(-I_SN); retain signed current and KCL. Compute I_eq=2e-15 C/t_est; for 64 ms and 32 ms target windows corresponding budgets 31.25 and 62.5 fA. No physical model additions, no manual sum of unrelated Ioff/GIDL; label omitted SRH and assumed Ccell. 233.15/300/340/358.15K targets 64ms; 368.15K target 32ms, engineering screen referenced to refresh windows (§11), not JEDEC compliance. 
- Export target endpoint PLT/log and PP for each node plus gtree.dat/gvars.dat, exact IVSN prefixed system PLTs, and mode-1 ION_VG1P2 TDR or extracted spatial fields. Preserve failed/partial data, require complete endpoints and adequate KCL, keep QC warnings (cold 233.15 K in particular) and do not silently fill them. Reuse older 300/340 K numerical evidence only after same geometry/mesh/physics/bias/solver/source comparability confirmed; no mixing by temperature label alone. 625 is full target count, not number newly executed.
- Next: launch external sweep; then join on exact (DBCAT_nm,TempK) into 125-row master table; 300 K BEST, allowed loss / P-NP, maps. If a mode fails, retain valid others and selectively rescue only required failed nodes. No new simulations executed by this code-preparation checkpoint.
