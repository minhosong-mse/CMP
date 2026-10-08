# MEB Effective Range — Literature-Based Evaluation Reference

## 0. Document Status and Source Inventory

**상태: 문헌 근거 정리 완료 / 평가 프로토콜 후보 / NOT FROZEN.** 버전 1.0, 2026-10-08. 목적은 후속 온도별 TCAD·1T1C 실험 전에 방어 가능한 지표와 선정 방법을 마련하는 것이다. 최적 MEB, 최소 개선율, 허용 페널티 및 합격 구간은 확정하지 않는다.

원문 PDF 11개, 총 85쪽을 식별하고 전체 텍스트와 렌더링을 검토했다. 수치·축·표·수식은 원본 렌더링과 대조했다. P04는 텍스트 인코딩이 깨져 4쪽 모두 이미지로 읽었다. P11의 첫 PDF 쪽은 표지다. 라이선스 페이지는 연구 근거로 세지 않는다. 원자료·코드·Freeze·기존 문서는 수정하지 않았으며 TCAD 실행, commit/push를 수행하지 않았다. 이 문서 한 개만 최종 산출물이다.

**입력 목록 불일치:** 예상 핵심 9편 중 “Novel Dual Work Function Buried Channel Array Transistor Process Design for Sub-17 nm DRAM”은 제공되지 않았다. 대신 P05 Fin Height 논문이 있다. 따라서 실제 구성은 예상 핵심 8편 + P05 + 추가 P01/P04다. 미제공 논문을 읽은 것으로 계산하지 않는다. 추가 원문은 §14에 명시한다.

PDF 원본 로컬 보관 경로는 공개 문서에서 제외했다. PDF 파일명과 SHA-256은 아래 Inventory에 보존한다. 각 원본 PDF는 저장소에 포함하지 않는다.

| ID | 실제 원제목 | 연도 | 기존 REF | PDF 쪽수 | 원문 상태 |
|---|---|---|---|---:|---|
| P01 | Compact Modeling of Temperature-Dependent Gate-Induced Drain Leakage Including Low-Field Effects | 2019 | — | 6 | 접근·전체 읽기·렌더링 대조 완료 |
| P02 | Impact of Metal and Poly Gate Thickness on GIDL in DRAM Dual Work-Function Structures | 2026 | REF03 | 5 | 접근·전체 읽기·렌더링 대조 완료 |
| P03 | Impact of Non-Ideal Wordline Etch Slopes on Read/Write Degradation in BCAT-Based DRAM | 2026 | REF09 | 11 | 접근·전체 읽기·렌더링 대조 완료 |
| P04 | Measuring and Exploiting Guardbands of Server-Grade ARMv8 CPU Cores and DRAMs | 2018 | — | 4 | 접근·전체 읽기·렌더링 대조 완료 |
| P05 | Optimization of Fin Height in Saddle-Fin BCAT Structured DRAMs | 2026 | — | 8 | 접근·전체 읽기·렌더링 대조 완료 |
| P06 | Partial Isolation Type Buried Channel Array Transistor (Pi-BCAT) for a Sub-20 nm DRAM Cell Transistor | 2020 | REF13 | 15 | 접근·전체 읽기·렌더링 대조 완료 |
| P07 | Simulation Study: The Impact of Structural Variations on the Characteristics of a Buried-Channel-Array Transistor (BCAT) in DRAM | 2022 | REF01 | 9 | 접근·전체 읽기·렌더링 대조 완료 |
| P08 | Trap-Induced Data-Retention-Time Degradation of DRAM and Improvement Using Dual Work-Function Metal Gate | 2021 (온라인 2020) | REF05 | 4 | 접근·전체 읽기·렌더링 대조 완료 |
| P09 | Understanding Retention Time Distribution in Buried-Channel-Array-Transistors (BCAT) Under Sub-20-nm DRAM Node—Part I: Defect-Based Statistical Compact Model | 2024 | REF06 | 7 | 접근·전체 읽기·렌더링 대조 완료 |
| P10 | Understanding Retention Time Distribution in Buried-Channel-Array-Transistors (BCAT) Under Sub-20-nm DRAM Node—Part II: PBTI Aging and Optimization | 2024 | REF07 | 7 | 접근·전체 읽기·렌더링 대조 완료 |
| P11 | Variation-aware analysis of buried-channel-array transistors (BCATs) in scaled DRAM: insights from 3D quasi-atomistic simulations | 2025 (온라인 2024) | REF10 | 9 | 접근·전체 읽기·렌더링 대조 완료 |

정확한 저자·저널·DOI는 Appendix B에 전수 수록한다. 아래 파일명은 공통 원본 폴더에 대한 상대 경로다.

| ID | PDF 파일명 | SHA-256 |
|---|---|---|
| P01 | `Compact_Modeling_of_Temperature-Dependent_Gate-Induced_Drain_Leakage_Including_Low-Field_Effects.pdf` | `35ddc25c536e3a43806078c9abe55141a386dbaa38cd17432c54b9372469e1d4` |
| P02 | `Impact_of_Metal_and_Poly_Gate_Thickness_on_GIDL_in_DRAM_Dual_Work-Function_Structures.pdf` | `9d0c5bc7401e138e9a2d15747c6135b4f1dd4aa1d526273cc9373eab4b7c5f88` |
| P03 | `Impact_of_Non-Ideal_Wordline_E.pdf` | `923776a2c2af12862786e7bf921d31831fbf4ac7468c08fdad3af2a4ab33d293` |
| P04 | `Measuring_and_Exploiting_Guardbands_of_Server-Grade_ARMv8_CPU_Cores_and_DRAMs.pdf` | `4813c6d488b16a80e7b0833c5131491f388fc372fa90001d28158e7a3971cbbd` |
| P05 | `Optimization_of_Fin_Height_in_Saddle-Fin_BCAT_Structured_DRAMs.pdf` | `84e9c3eabda4d2737e08d48d731c2c8cf20f03a96b7bee629ad15c7d8aa1669a` |
| P06 | `Partial_Isolation_Type_Buried_.pdf` | `70cdbfe9ee23d1ec9b588f8a5f688bc1e061b5203fabe2a6e2e00b8a576782da` |
| P07 | `Simulation_Study_The_Impact_o.pdf` | `8d3eeb985872f72457715ed20dfbaf2cf9c7cabf873bccd5cb89cf152eef9f53` |
| P08 | `Trap-Induced_Data-Retention-Time_Degradation_of_DRAM_and_Improvement_Using_Dual_Work-Function_Metal_Gate.pdf` | `1f0aef2e62a1273146eb622a29f0963db0030e9e6a508f60f51075ba43213c78` |
| P09 | `Understanding_Retention_Time_Distribution_in_Buried-Channel-Array-Transistors_BCAT_Under_Sub-20-nm_DRAM_NodePart_I_Defect-Based_Statistical_Compact_Model.pdf` | `a567e3570cc6bf501df25b7f8e4efa203c4d0b613fdb7d5e23a16c1ea8ba5d54` |
| P10 | `Understanding_Retention_Time_Distribution_in_Buried-Channel-Array-Transistors_BCAT_Under_Sub-20-nm_DRAM_NodePart_II_PBTI_Aging_and_Optimization.pdf` | `586e110ad246d18e045600a28643ec34959be9d971694621b83642f9ed4263f0` |
| P11 | `Yoon_2025_Semicond._Sci._Technol._40_015010.pdf` | `a12741cae6c7940312c81757a9249bf5823f2b1d8f0cc5c2f22f4664ee3d4ec4` |

### 읽기·분류 규칙

인용 `P09 PDF 6 / 4467, Fig. 10`은 파일의 여섯째 쪽과 인쇄 4467쪽을 뜻한다. P03/P06/P07의 본문은 PDF와 인쇄 쪽번호가 같다. P02는 PDF 쪽만 사용한다. P11은 PDF 쪽에서 1을 빼면 본문 쪽이다. 아래 각 논문 A에는 전체 쪽 대응을 적는다.

| 표기 | 의미 |
|---|---|
| LIT-EXPLICIT | 원문에 직접 명시된 조건·수치·방법 |
| LIT-DERIVED | 명시 수치로 계산; 계산 과정 병기 |
| PAPER-INFERRED | 논문 결과에서 해석한 의미; 저자의 직접 명시와 구분 |
| CMP-PROPOSED | 이번 문서의 신규 평가 제안; NOT LITERATURE EXPLICIT |
| CMP-EXISTING | live main의 현행 또는 명시한 역사적 CMP 프로토콜 |
| UNKNOWN | 근거 부족 |
| NOT REPORTED | 원문에 재현에 필요한 정보가 제시되지 않음 |
| NOT VERIFIED | 해당 원문·실험에 접근하여 검증하지 못함 |
| AMBIGUOUS | 문장·그림·단위 또는 해석이 불명확/충돌 |

**EXPLICIT DESIGN CONSTRAINT / REPORTED RESULT / EXTERNAL STANDARD**는 근거의 용도 분류다. LIT-EXPLICIT라는 이유만으로 설계 제약이 되는 것은 아니다. 예컨대 직접 보고한 51% 개선은 LIT-EXPLICIT이지만 REPORTED RESULT다. 이하 논문별 A–F의 출처가 붙은 사실은 별도 표기가 없으면 LIT-EXPLICIT이고, G의 적용 판단은 PAPER-INFERRED 또는 CMP-PROPOSED다. 열거하지 않은 원시 곡선의 점은 디지털화하거나 추정하지 않았다.

### CMP 상태 확인에 사용한 live GitHub main

`AGENTS.md` → `HANDOFF.md` 순서로 읽은 뒤 관련 문서를 선택해 확인했다. 아래는 열람한 파일 blob SHA다. **main 전체의 단일 commit SHA를 뜻하지 않는다.** 논문 사실은 PDF, 프로젝트 현황은 최신 HANDOFF/Atlas를 우선한다.

| 문서 | 확인한 blob SHA | 용도 |
|---|---|---|
| [AGENTS.md](https://github.com/minhosong-mse/CMP/blob/main/AGENTS.md) | `10a37fa8436d9b83abe3d41423d764c13bcd522b` | 작업·근거 규칙 |
| [HANDOFF.md](https://github.com/minhosong-mse/CMP/blob/main/HANDOFF.md) | `0664d7ce3e26298922bca7d4510c07ec3d6cb54e` | 현행 분기와 미해결 항목 |
| [REFERENCES](https://github.com/minhosong-mse/CMP/blob/main/docs/REFERENCES.md) | `391789e3ad64720da8ba70cb7ce7a058796ba520` | 기존 REF 매핑 |
| [MODEL_SCOPE](https://github.com/minhosong-mse/CMP/blob/main/docs/MODEL_SCOPE.md) | `f78634aee755db7c56d4e39781b0e6906390c54a` | 모델 범위, 역사적 조건 |
| [CLAIM_EVIDENCE_MATRIX](https://github.com/minhosong-mse/CMP/blob/main/docs/research/CLAIM_EVIDENCE_MATRIX.md) | `8b8aa9a68383cbdc0f95b830097b3269cf60cc76` | 주장 경계, 구분 필요 |
| [300 K Atlas](https://github.com/minhosong-mse/CMP/blob/main/docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md) | `cdc618594262ee4adc8de66c44522ad44f2ea0a1` | 최신 15점 관찰 결과 |

`docs/literature/README.md`도 읽었다. 별도의 Literature Master 본문은 검색에서 찾지 못했으므로 NOT VERIFIED이며 분석을 이에 의존하지 않았다. 링크의 main은 이후 변경될 수 있어 위 식별자를 함께 보존한다.

## 1. CMP Research Objective and Claim Boundaries

연구 질문은 **20 nm급 single-WF BCAT에서 MEB가 누설 경로를 어떻게 바꾸며, 그 변화가 실제 1T1C Retention 및 온도별 사용 가능한 설계 집합으로 얼마나 전달되는가**이다. 구조 → electrostatics/coupling → 공간 전계·generation → terminal leakage → write/hold/read → retention → 온도별 제약 판정 순서로 검증한다. 앞 단계의 개선만으로 뒷 단계 성공을 대체하지 않는다.

현행은 `B0-2D-PAPER-CAL`, C7_4/B_QF_HALF 동결 물리 조건이다: GateCouplingScale 2.300, GateDepthBoost 25 nm, Qf_Int 2.55×10¹² cm⁻², WF 4.8 eV, 명목 MEB 36 nm, 300 K. 이는 CMP-EXISTING이며 문헌의 제작 공정 파라미터와 동일하다는 뜻이 아니다. `B0-2D-Legacy`, `3D-Sun-B0`와 섞지 않는다.

Atlas는 MEB 31, 33, 36, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51 nm의 15점이다. production mesh2/reference mesh3의 같은 수치 분기 내 1,036 QC checks 통과 및 archive 201개(90 summary + 105 curve + metadata)는 프로젝트 보고 내용이다. 이 문헌 작업에서 원시 CSV를 재계산한 것은 아니다. 근거 commit은 프로젝트 문서에 `b40c63299917419e789ac41f2f87c637ff3ebcdb`로 기록돼 있다. **10월 5일 FZ-C 실행 부모와의 정확한 bridge는 OPEN**이다. 따라서 mesh만 바꿔 동결 부모를 정확히 재현했다고 주장할 수 없다.

| 현재 관찰(CMP-EXISTING) | 조건·해석 한계 |
|---|---|
| 총 drain 누설 31→51 nm에서 약 1,135배, 36→51에서 19.50배 감소 | VD=1.2 V, VG=−0.7 V, 300 K; pure BTBT current가 아님 |
| project-internal \|Cgd\| 약 35.91% 감소 | 31→51 nm, 1 MHz, 같은 누설 바이어스, BTBT off; 생산 DRAM overlap capacitance로 해석 불가 |
| Ion 변화 −1.30%(@VG=1.2 V), −6.46%(@VG=2 V) | 31→51 nm; 선택한 on bias에 따라 페널티가 다름 |
| DIBL +0.459 mV/V, quick SS +0.069 mV/dec | 관찰 결과이지 합격 제약 아님; DC VD=0.05/1.2 V |
| whole-Si BTBT 적분과 E@BTBT peak 약 39 nm, BTBTmax 약 41 nm | 총 누설의 단조 감소와 다른 형태 |
| Hurkx 민감도 약 0.105%(31), 16.94%(36), 74.10%(39), 91.19%(41), 99.57%(48), 99.81%(51) | ON/OFF 토글의 수치 민감도; 미시적 성분 비율의 정확한 측정 아님 |

signed ON−OFF와 q∫GdA 비교 오차는 31 nm에서 최대 약 0.62%, 36–51 nm에서 0.01% 미만으로 보고됐다. 작은 차이의 상쇄·부호·2D 정규화를 확인해야 한다. shallow MEB의 drain–substrate 잔여 경로는 아직 미해결이다. 고정 Y=0.252174 μm cut은 shallow hotspot을 놓칠 수 있어 전체 Si 적분·공간 위치를 함께 본다. 48 nm GateTop≈junction은 모델 구조 경계이며 knee가 아니다. 51 nm는 탐색 끝점이지 최적점이 아니다.

현행 분기의 온도별 MEB retention 및 write/hold/read 검증은 미수행이다. Legacy의 C=10 fF, AreaFactor=0.017, WL=3 V, BL=1.2 V, 약 667 ns write 및 100 μs hold 결과를 현행 분기의 검증으로 재사용하지 않는다. 이전 47–49 nm 후보/48 nm 논의를 이번 유효 범위로 복원하지 않는다. 별도 3D 형상의 RWL proxy는 실제 분포 저항·RC delay가 아니다.

## 2. Executive Findings

1. **VSN 1.0→0.8 V의 직접 출처는 P09**다. 10 fF와 데이터 손실 가정, 회로 변동 제외 조건을 갖는 compact/statistical retention 평가다. 실제 read failure가 보편적으로 0.8 V라는 검증은 아니다(P09 PDF 5–6/4466–4467, §IV).
2. **명시적인 Ion 80% 조건은 P06에 있다.** 같은 gate depth의 asymmetric BCAT에 대한 등비 조건이며, CMP의 Ion 95%를 뒷받침하지 않는다(P06 PDF/인쇄 11–12, Fig.16/Table1).
3. **P03은 10 ns write 후 300 ms hold에서 VSN≥0.698 V를 판정에 사용한다.** 회로 전하 공유식에 근거하지만 전체 C와 sense 조건이 없어 CMP에 숫자를 이식할 수 없다(P03 7–8, Eq.1–2/Fig.12).
4. **P05는 네 지표를 정규화해 합산하고 fin height 12 nm를 선택한다.** 실제 다목적 점수화 사례지만 hard constraint, Pareto 최적화 또는 연속 MEB 유효 범위는 아니다(P05 PDF7/143324, §III-E/Fig.16).
5. **P02는 PEB로 목표 Ion을 맞춘 후 MEB를 조절하는 순차 설계 논리를 제공한다.** RWL/RC는 논의하며 정량 한계를 계산하지 않는다(P02 PDF4, Figs.5–7/결론).
6. **낮은 전계의 TAT·고온의 junction/diffusion 성분을 무시할 수 없다.** P01/P09의 근거는 총 GIDL-bias current=BTBT라는 등식을 지지하지 않는다(P01 PDF2–5; P09 PDF3/4464, Figs.2–4).
7. **분포의 중심과 weak tail은 서로 다른 평가 대상이다.** P08의 CP=10⁻⁶%와 P10의 CDF=10⁻⁶은 100배 다른 확률이다. 보고된 개선율을 최소 합격률로 바꿀 수 없다(P08 PDF3/40, Fig.4; P10 PDF6/4474, Fig.12).
8. **온도 의존 retention은 선행연구에 있다.** 그러나 계획한 233/300/340/380 K에서 single-WF MEB별 write/read/DC 제약을 결합한 범위 이동은 이 11편에서 확인되지 않았다(P09 Fig.10 등; §13).
9. **기준 소자 대비 상대 이득과 절대 동작 성공은 함께 봐야 한다.** 같은 온도 36 nm 분모와 절대 write/read 조건을 결합하는 것은 CMP-PROPOSED이며 문헌의 동결된 공통 공식이 아니다.
10. **연속 유효 범위와 강건 범위는 아직 주장할 수 없다.** 이산 통과점, 공정 분산, 온도 최악값은 서로 다른 증거다. bridge 해결 후 초기화·read 판정·제약값을 정하고 추가 측정해야 한다.

## 3. Literature Comparison Matrix

| ID | 대상·방법 | 변화 변수 | 최종/핵심 평가 | 선정 형태와 CMP 거리 |
|---|---|---|---|---|
| P01 | FinFET compact+TCAD+측정 | bias, T | GIDL model fit, BTBT/TAT | 모델 정확도; BCAT 설계 최적화 아님 |
| P02 | 15 nm 3D dual-WF DRAM | MEB/PEB/poly thickness | leakage 관련 E-field, IV | Ion 우선→MEB 조정; 수치 feasible set 없음 |
| P03 | 1y 2D BCAT mixed-mode | etch angle, rounding, BOX depth | write/hold VSN와 read 가능 조건 | fixed-window pass/fail |
| P04 | 실제 ARMv8 서버/DDR3 | voltage/frequency/refresh/T/workload | BER/ECC, power, performance | 시험 조건별 guardband; 소자 MEB와 거리 큼 |
| P05 | 1z 3D saddle-fin dual-WF | Hfin, 보정 body doping/metal depth | DIBL/GIJL/PGE/1-RD | min–max 합산 점수 단일점 12 nm |
| P06 | 3D Pi-BCAT | Lin, film, gate depth | Ioff, Ion=80% | 조건부 구조 선택/contour; MEB window 아님 |
| P07 | 20 nm 3D single-WF | DBCAT, junction, AR, Wfin, fillet | Vth, SS, DIBL, Ion/Ioff | deterministic sensitivity; 주력 형상 참고 |
| P08 | 20 nm 3D+statistical model | traps, upper WF, T | retention CDF/weak tail | 구조 비교; direct 1T1C transient 아님 |
| P09 | sub20 3D+측정+compact MC | trap count/location/energy, T | retention CDF, leakage components | 분포·온도 모델; 공통 합격값 없음 |
| P10 | P09 companion+PBTI 측정 | aging, WF, oxide, metal thickness | tail retention vs Idsat | trade-off와 aging; 전 온도 MEB range 없음 |
| P11 | 20 nm 3D surface variation | roughness, curvature | DC 평균·SD | 150 samples/case; yield threshold 없음 |

## 4. Individual Paper Evidence Records

각 C 표의 역할은 P(성과/목적), C(제약), M(메커니즘), V(검증)이다. 비교 기준·선택 이유·한계를 함께 적었다. 반복되는 미보고 사항도 B/F에 명시한다. 아래 표에 없는 §5의 지표는 해당 논문에서 계산한 지표로 취급하지 않는다.

### P01 — Temperature-dependent GIDL compact model

#### A. 서지·목적

Dabhi, Roy, Chauhan(2019), IEEE TED 66(7), DOI 10.1109/TED.2019.2918332. 정확한 원제목·저자 표기는 Appendix B. PDF 1–6=인쇄 2892–2897. 낮은 전계까지 설명하는 temperature-dependent BTBT+TAT compact model을 제안하고 TCAD 및 산업 FinFET 측정과 비교한다. 새로운 BCAT 설계나 셀 retention 실험은 아니다.

#### B. 구조·조건

PDF 3/2894 §II-B의 TCAD single-fin은 L=25 nm, Wfin=15 nm, HfO₂ EOT=1.6 nm. Hurkx BTBT 및 TAT를 고려한다. 측정 대상은 sub-20-nm n/p FinFET이며 공개된 정확한 측정 소자 node·도핑·WF·전체 형상은 NOT REPORTED. Gate depth/MEB/PEB 변수는 없다. DC bias와 온도를 바꾸며 상세 mesh 및 convergence study는 NOT REPORTED. n/p 측정 GIDL은 a.u.로 표시되므로 절대 BCAT A 또는 A/μm 비교는 불가하다. 기존 BSIM BTBT-only 모델이 저전계에서 어긋나는 것이 비교 기준이다(PDF 1/2892 Fig. 1).

#### C. 실제 지표

| 지표·정의 | 조건·단위·비교 | 역할·선택 이유·한계 | 원문 위치 |
|---|---|---|---|
| IGIDL=Wq∬(GBTBT+GTAT)dxdy | drain/gate bias, T; 측정 곡선 a.u. | P/V: 저전계까지 모델 일치; fit tolerance 수치 없음 | PDF 2/2893 Eq.1; PDF 5/2896 Figs.5–6 |
| GBTBT=(A/B)F^σD exp(−B/F), σ=2 | local field; generation cm⁻³s⁻¹ | M: field-driven generation; terminal current와 구분 | PDF 2 Eq.2; PDF 3 Fig. 3 |
| GTAT=Γ(F)GSRH | Vdg=0.5 V의 표면 아래 1 nm cut; cm⁻³s⁻¹ | M: 저전계 TAT; 특정 FinFET에서의 공간 근사 | PDF 2 Eq.3; PDF 3 Fig. 3 |
| Fmax=(εox/εsi)(αVdg²−βVdg−γ)/Tox | Vdg 약 0.4–1.2 V; MV/cm | M/V: analytic approximation 검증; peak-only 모델의 BCAT 보편성 없음 | PDF 2 Eq.5; PDF 3 Fig. 4 |
| IBTBT=W(A/B)Fmax²exp(−B/Fmax) | compact approximation | M/P: 적분을 peak 기반 식으로 근사; 공간 형상 전제 필요 | PDF 3 Eq.6 |
| ITAT=ATAT W ni(T)Γmax; Vdb³/(CGIDL+Vdb³) 보정 | Vdb=0에서 총 GIDL→0 | M/P: 온도 및 body-bias 의존성 반영; 계수 전용 추출 필요 | PDF 4–5/2895–2896 Eqs.11–32 및 최종식 |
| temperature-dependent measured/model GIDL | −40, 25, 100 °C; n/p FinFET | V: 여러 T의 fit; retention나 최악 T 합격 기준 아님 | PDF 5 Figs.5–6 |

Retention, VSN, Ion/Ioff 설계 제약, Vth/SS/DIBL 설계 비교, Cgd, write/read, RWL, process yield는 NOT REPORTED. 물리식의 전계·bandgap·ni는 모델 변수이며 독립적인 설계 합격 지표가 아니다.

#### D. 정량 기준

**NO EXPLICIT THRESHOLD.** 온도 세 점·Vdg sweep·공간 cut 위치는 분석 조건이다. 모델 일치를 보여 주지만 허용 오차 또는 leakage 감소 최소율을 정하지 않는다.

#### E. 선정 방식

compact formulation의 정확도를 검증한다. 구조 단일 최적점, feasible region, Pareto, knee 또는 manufacturing window 선정은 없다.

#### F. 온도·Retention

−40/25/100°C는 233.15/298.15/373.15 K로 환산된다(LIT-DERIVED, K=°C+273.15). 계획 233/300/380 K와 정확히 같은 점은 아니다. bandgap·intrinsic carrier concentration 및 TAT 강화의 온도 의존성을 반영한다. VSN 초기값·종료값·floating node·hold·retention integration·read failure는 모두 NOT REPORTED.

#### G. 적용성

**MECHANISM / BACKGROUND ONLY:** 낮은 전계에서 TAT를 고려할 필요성과 단순 BTBT fit의 한계. **ADAPTABLE WITH CONDITIONS:** 모델 ON/OFF 및 온도 비교를 통한 메커니즘 검증. **NOT TRANSFERABLE:** FinFET compact 계수·Fmax 근사를 CMP BCAT에 그대로 적용. CMP shallow residual이 TAT라는 결론은 이 논문으로 확정할 수 없다. 누설 성분 모델링 자체는 선행연구에 있다.

### P02 — MEB/PEB in dual-WF DRAM

#### A. 서지·목적

SeKyoung Jang, SoYoung Kim(2026), ICEIC, DOI 10.1109/ICEIC69189.2026.11386251. PDF 5쪽, 별도 인쇄 쪽번호 없음. 15 nm dual-WF 구조에서 metal/poly 두께와 drain 쪽 전계를 TCAD로 비교한다. MEB를 직접 다루므로 가까운 선행연구지만 CMP single-WF와 구조·깊이 원점이 다르다.

#### B. 구조·조건

3D, 하부 TiN/W WF=4.6 eV와 상부 n⁺ poly. **MEB와 PEB는 Si 표면에서 각각 metal과 poly 시작 위치까지의 깊이**, poly thickness=MEB−PEB. 명목 MEB/PEB/thickness=82/57/25 nm(PDF 2 Fig. 1). interface trap density=10×10¹⁰ cm⁻². 전체 doping profile의 재현 가능한 수치 세트는 NOT REPORTED. WL1/2와 PWL1/2=−0.2 V, SN1/2=1 V, BL=0.5 V, body=−0.7 V. calibration IV에는 BL=0, SN=1 V 조건이 별도로 사용된다. 모델은 PhuMob, high-field saturation, Slotboom, doping/field-dependent SRH, Hurkx BTBT, FN gate leakage. 온도·mesh convergence는 NOT REPORTED. 선행 TEM/IV와의 log/linear 전류 비교는 있지만 본 연구의 새 제작 데이터로 취급하지 않는다(PDF 2 Fig. 2).

#### C. 실제 지표

| 지표·정의 | 조건·단위·비교 | 역할·이유·한계 | 원문 위치 |
|---|---|---|---|
| transfer ID–VG, Ion/Vth/SS 일치 | calibration, I=A; 추출식·오차수치 NR | V: 구조 모델 적합성; numerical acceptance 아님 | PDF 2 Fig. 2 |
| GIDL/GIJL의 위치와 leakage 관련 전계 | 상부/하부 drain-side peak 구분 | M/P: 상·하부 누설 경로 설명; 생성률 전체 적분으로 단자 성분 분해하지 않음 | PDF 3 Figs.3–4 |
| doping/potential spatial profile | doping cm⁻³, potential a.u. | M: overlap/접합과 field의 관계 | PDF 3 Fig. 4 |
| E-field maximum/profile vs thickness | MV/cm, distance/thickness nm; MEB=72/82/92/102 nm 고정 sweep | P/M: PEB 변화에 따른 경쟁 효과; absolute leakage→retention 정량 전달 미계산 | PDF 4 Fig. 5 |
| E-field vs MEB, fixed PEB | PEB=67/57/47/37 nm; MEB 증가 시 field 감소·포화 | P/M: 순차 설계 방향; 포화점을 hard boundary로 선언하지 않음 | PDF 4 Fig. 6 |
| MEB–PEB 비교 | MEB=52,62,72,82,92,102 nm; PEB sweep | P: 두 공정 변수의 결합; 독립 MEB-only와 다름 | PDF 4 Fig. 7 |

Ion은 선행 목표로 논의되지만 **정량 target Ion은 NOT REPORTED**. RWL/RC 증가도 논의 수준이며 실제 저항·delay 곡선, Cgd, retention, VSN decay, write/read transient, BTBT whole-volume integral 및 온도 sweep은 제시되지 않는다.

#### D. 정량 기준

**NO EXPLICIT NUMERICAL THRESHOLD.** “PEB를 target Ion에 맞춘 뒤 MEB 조정”은 명시된 설계 순서다. target Ion의 값·분모·온도, 허용 RWL/RC 상한 및 최소 GIDL 감소율은 NOT REPORTED(PDF 4 결론). 나열한 깊이는 sweep 범위이지 제조 합격 범위가 아니다.

#### E. 선정 방식

Ion 요구와 leakage/RC trade-off를 고려한 순차 설계, field 감소의 saturation 관찰. 수치 feasible set, Pareto front, 단일 정량 optimum 또는 온도별 연속 유효 구간은 제시하지 않는다.

#### F. 온도·Retention

온도·Ccell·VSN 초기/종료·floating hold·retention 계산·read failure는 NOT REPORTED. standby bias의 leakage 해석을 1T1C 검증으로 바꾸지 않는다.

#### G. 적용성

**ADAPTABLE WITH CONDITIONS:** Ion 유지 조건과 구조 변수를 분리하고 깊이에 따른 두 field peak를 비교하는 방법. **NOT TRANSFERABLE:** 82/57 nm 등의 깊이, dual-WF 효과, RWL 수치 추정. 동일 MEB 명칭만으로 CMP 36 nm와 직접 대응시키지 않는다. MEB 증가–drain field/GIDL 관계 자체의 신규성은 제한된다.

### P03 — Non-ideal wordline etch and write/hold criterion

#### A. 서지·목적

Cho, Kim, Baek(2026), Electronics 15(6),1152, DOI 10.3390/electronics15061152. PDF 1–10=본문 1–10, PDF 11 이용조건. 비이상적인 WL etch slope가 write를 열화시키는 경로와 BOX 보완 구조를 2D TCAD/mixed-mode로 분석한다. 실제 제작·측정 검증은 제시하지 않는다.

#### B. 구조·조건

1y BCAT, Silvaco DeckBuild 5.2.17.R/DevEdit 2.8.26.R. AWL 및 FPWL 포함. PDF 3 Tables1–2: DSi=245, DSTI=195, DBL=83, DCAP=58, DAWL=65, DFPWL=95, DPoly=25, WWL=12, WAct=23, Tox,side/bottom=8/6, Tsub=5 nm. WL ON/OFF=3/−0.2 V, body=−0.6 V, BL standby/read=0.5 V. 정확한 도핑·WF·물리 모델 옵션·온도·mesh/convergence·C_SN/C_BL는 NOT REPORTED. θ=90–92.4°와 WL rounding r=6→0 nm가 함께 바뀌며 bottom geometry는 고정되므로 순수 θ 단독 효과로 분리하기 어렵다(PDF 4). BOX depth 22/18/14/10/6 nm 비교. DAWL/DFPWL은 해당 구조 깊이이며 CMP MEB와 자동 등치하지 않는다.

#### C. 실제 지표

| 지표·정의 | 조건·단위·비교 | 역할·이유·한계 | 원문 위치 |
|---|---|---|---|
| ID–VG, Ion/SS 변화 | AWL sweep; A, V; ideal θ=90° 대비 | V/M: gate control 감소; 정량 허용 SS/Ion 없음 | PDF 5 Fig. 6 |
| SN write waveform | D1 write; ns, V; θ sweep | P: 동일 pulse에서 초기 충전 부족 확인; 누설 악화와 구분 | PDF 5 Fig. 7 |
| BOX에 따른 IV/Vth 변화 | DBOX sweep; A,V | M/V: electrostatics 보완; Vth 허용 범위 NR | PDF 6 Figs.8–10 |
| write+hold VSN | 10 ns write, 300 ms hold; V | P/C: fixed-window 기능 판정; crossing-time tRET와 다름 | PDF 7–8 §4/Fig. 12 |
| αmin charge-sharing condition | αmin=(ΔVBL/Vcc)(C_BL+C_SN)/C_SN+1/2 | C: 요구 read signal에서 SN 조건 도출; α 무차원과 voltage 표기 혼용 | PDF 7–8 Eqs.1–2 |
| VSN≥0.698 V | 위 window 종료; capacitance/ΔVBL 상세값 NR | C: paper-specific pass/fail; 실제 sense amplifier 판정 독립 검증 아님 | PDF 8 Fig. 12/본문 |

θ=90.8° no-BOX hold 약 0.71 V, θ=91.6° write 직후 0.62 V, θ=92.4° 0.43 V; DBOX=18 nm, θ=91.6°에서 write/hold 약 0.77/0.72 V가 본문에 제시된다(PDF 8). 결론의 0.67→0.84 V(write), 0.62→0.79 V(hold) 등과 조건 연결이 불명확하므로 통합 대표값으로 채택하지 않는다. DIBL, Cgd, RWL, BTBT 적분, temperature sweep, retention CDF는 NOT REPORTED.

#### D. 정량 기준

**EXPLICIT DESIGN CONSTRAINT:** 위 0.698 V, 10 ns/300 ms 조건. baseline은 ideal/no-BOX와 각 etch/BOX 조합이며 온도는 NR. 저자 rationale은 Eq.1–2의 BL charge sharing과 read 가능성. **EXTERNAL STANDARD(논문 인용):** 64 ms refresh 관련 JEDEC 언급. 이번 작업에서 표준 원문·적용 제품군은 NOT VERIFIED. 300 ms는 저자가 Gaussian 분포의 median을 고려해 택한 평가 가정이며 JEDEC 요구값이 아니다. 측정된 VSN 및 개선율은 REPORTED RESULT다.

#### E. 선정 방식

지정 write/hold 시간 이후 threshold 통과 여부를 구조별로 판정한다. retention 최대화보다 초기 write 성공이 주요 병목이다. θ와 BOX의 통과 사례가 있어도 CMP MEB의 연속 범위·Pareto front·공정 yield는 도출되지 않는다.

#### F. 온도·Retention

T는 NR. SN initial은 실제 write waveform으로 형성되며 1 V를 강제로 시작하는 방식과 다르다. hold 중 감소량보다 write 직후 충전량 차이가 결과를 크게 좌우한다(PDF 8). VSN 1.0→0.8 V 정의는 없다. floating node의 정확한 회로 연결·누설 소자 목록과 sense 조건은 재현에 충분히 보고되지 않았다. ΔVSN와 fixed-time 판정을 tRET으로 부르지 않는다.

#### G. 적용성

**DIRECTLY REUSABLE METHOD:** 초기 write 전압과 hold 손실을 따로 기록하는 평가 논리. **ADAPTABLE WITH CONDITIONS:** 실제 CMP BL capacitance/read pulse에 맞춰 charge sharing margin을 계산. **NOT TRANSFERABLE:** 0.698 V, 300 ms, θ/BOX 합격값. 단순 retention 개선이 write/read 성공을 보장하지 않는다는 선행 근거다.

### P04 — Server CPU/DRAM guardband experiment

#### A. 서지·목적

Tovletoglou 외(전체 저자 Appendix B), DSN-W 2018, 6–9, DOI 10.1109/DSN-W.2018.00013. PDF 1–4=인쇄 6–9. 실제 서버의 voltage/frequency/refresh 여유를 workload와 온도에 따라 측정하여 전력을 줄인다. TCAD 또는 BCAT 구조 최적화가 아니다.

#### B. 구조·조건

X-Gene2 ARMv8 8 cores, 2.4 GHz, CPU 28 nm; TTT/TFF/TSS 세 process-category chip. 32 GB DDR3, 72 DRAM chips. DRAM node·gate scheme·도핑·WF·MEB·cell capacitor·소자 leakage 모델·mesh는 해당 없음/NOT REPORTED. Raspberry Pi/PID thermal adapters로 온도 제어; 설정값 최대 오차 <1°C는 측정 제어 성능이다(PDF 2/7). ECC CE/UE 및 golden execution과 비교한 SDC, random/all-zero/all-one/checkerboard pattern, HPC workloads를 사용한다. 파워 W, voltage mV, refresh ms/s, BER 무차원.

#### C. 실제 지표

| 지표·정의 | 조건·단위·비교 | 역할·이유·한계 | 원문 위치 |
|---|---|---|---|
| Vmin/frequency/실행 성공 | workload·TTT/TFF/TSS; nominal 980 mV | P/C: tested workload에서 오류 없는 동작; 모든 프로그램 보증 아님 | PDF 2–3/7–8 Figs.4–7 |
| CPU power/performance trade-off | baseline 대비 %; 12.8% 절감/성능 손실 없음, 38.8% 절감/25% 성능 손실 등 | P: 실제 비용; CMP 허용 손실로 전용 불가 | PDF 3 Fig. 5 |
| DRAM BER와 ECC CE/UE | 50/60 °C, refresh 확장, data pattern/workload | P/C: raw errors와 correction 가능성을 구별 | PDF 3–4/8–9 Fig. 8/Table 1 |
| refresh interval | nominal 64 ms→2.283 s, 논문 표기 35× | P: 전력 대 오류; single-cell tRET가 아님 | PDF 3–4 |
| bank별 error locations | 50 °C: 180,213,228,230,163,198,204,208; 60 °C: 3358,3610,3641,3842,3293,3448,3601,3540 | V: 공간/온도 변동; 시험 길이·모수 없이 BCAT yield로 환산 불가 | PDF 4/9 Table 1 |
| DRAM power savings/workload dependence | 최대 27.3%(nw), 9.4% kmeans,10.4% backprop,10.3% srad; BER workload간 약 2.5× | P/V: pattern coverage 필요 | PDF 3–4 Fig. 8/본문 |
| server power | Jammer 4 parallel, PMD930/SoC920 mV; 31.1→24.8 W,20.2% | P: 실측 시스템 이득; process-independent 기준 아님 | PDF 4 |

온도별 Fig. 8 BER 축은 50°C에서 10⁻⁹, 60°C에서 10⁻⁷ scale이므로 같은 축으로 읽지 않는다. 테스트에서 ≤60°C의 관찰 오류가 ECC-correctable이었다는 결과는 raw error=0이 아니다. VSN waveform, GIDL/BTBT, Cgd, Ion/Vth/SS/DIBL, RWL은 측정하지 않는다.

#### D. 정량 기준

error detection과 동작 성공에 기반한 guardband 탐색은 명시되어 있으나 CMP용 수치 성능 제약은 **NO EXPLICIT THRESHOLD**. 64 ms는 nominal refresh baseline이고, universal MEB retention 합격 시간이 아니다. 2.283 s, 전력 개선율, Vmin은 REPORTED RESULT. 35×64 ms=2.240 s이므로 2.283 s와는 정확히 일치하지 않는다(LIT-DERIVED); 원문 숫자를 임의 보정하지 않는다.

#### E. 선정 방식

실험으로 오류 경계를 찾고 전력/성능을 비교하는 system guardband 방법. 공정·워크로드별 다른 경계를 보여준다. MEB feasible region 또는 single-cell robust optimization은 아니다.

#### F. 온도·Retention

DRAM 50/60 °C=323.15/333.15 K(LIT-DERIVED). refresh 확장에 따른 error behavior를 확인하며 1.0→0.8 V crossing이나 leakage integration은 없다. retention 분포를 SN 전압에서 직접 측정하지 않는다. 주어진 두 온도·워크로드 통과로 380 K 또는 저온 동작을 보장하지 않는다.

#### G. 적용성

**ADAPTABLE WITH CONDITIONS:** 실패 정의·시험 coverage·온도별 기준을 먼저 정하는 방법. **MECHANISM / BACKGROUND ONLY:** 시스템 guardband의 조건 의존성. **NOT TRANSFERABLE:** refresh interval, Vmin, ECC 허용 결과, power%를 TCAD MEB 제약으로 변환. 이는 소자 수치를 제공하는 논문이 아니라 검증 철학의 근거다.

### P05 — Fin height multi-objective score

#### A. 서지·목적

Damin Kim, Min-Woo Kwon(2026), IEEE Access14,143318–143325, DOI 10.1109/ACCESS.2026.3733420. PDF 1–8=인쇄 143318–143325. 3D TCAD로 fin scaling에 따른 DIBL/GIJL/PGE/1-row disturbance trade-off를 평가한다. 예상 입력 목록의 Park process 논문과 다른 문헌이다.

#### B. 구조·조건

1z nm saddle-fin BCAT, poly/W dual-WF 구조, Sentaurus. PDF 2/143319 Table 1: WL=10.6 nm, active=21.2 nm, channel=30 nm, DBCAT=132 nm, top metal depth=33 nm, bottom metal depth=60.3 nm, oxide side/bottom=7/5.3 nm, Hfin=19 nm. S/D=10²⁰, body 기준=10¹⁷, poly=10²¹ cm⁻³. 정확한 WF는 NR. Hfin 19→1 nm(1 nm step)에 맞춰 body doping을 낮추고 bottom metal depth도 변한다. 따라서 Hfin 단독 변경과 보정된 구조 변화의 결과를 구분한다. Vth=0.54 V(VD=1 V, constant current 100 nA)로 보정; 오차 <1.3 mV는 보정 결과다. PhuMob/high-field/Enormal, SRH/TAT/BTBT. 온도·mesh convergence·독립 측정 calibration 상세는 NR. nominal Hfin=19 nm가 비교 기준이다.

#### C. 실제 지표

| 지표·정의 | 조건·단위·비교 | 역할·이유·한계 | 원문 위치 |
|---|---|---|---|
| Vth/Ion/IGIDL | Vth=.54 V 보정; Ion/IGIDL normalized a.u. | V: on/GIDL을 유사하게 유지; 별도 Ion 허용율 없음 | PDF 2–3/143319–143320 Figs.2–3 |
| DIBL, SS | Vth VD=.05/1 V, FPWL off; SS@VD1; mV/V,mV/dec | P/M: control loss; Hfin19→1에서 DIBL+19%,SS 약+10 mV/dec는 결과 | PDF 3 Fig. 4 |
| GIJL 및 E-field | FPWL floating, VD1, VAWL=.9, Vsub0→−12 V; pA,MV/cm | P/M: field crowding; −12 V stress 결과를 normal hold로 전용 불가 | PDF 3–4 Figs.5–6/8 |
| GIJL 변화 분리 | 결합 87% 감소, body만 53%, Hfin만 61% | M/P: 공변 변수 비교; 합산 가능한 독립 성분 아님 | PDF 4/143321 Fig. 8 |
| PGE=FPWL3/−.2 V에서 ΔVth | body−.7, VD1; .346→.447 V(약 29%) | P/M: passing-gate coupling; AWL만 54%악화/FPWL만 13%개선 | PDF 4–5 Figs.7/9 |
| channel potential/capacitive network | φch=VFPWL/(1+Ceq1/Ceq2); Cox,b/Cox,w/Csi/Csti | M: coupling 설명; Cgd AC 추출 아님 | PDF 5 Figs.10–11 |
| 1-RD SN waveform/pulse endurance | D0, C=8 fF; FPWL3/−.2 V, period60 ns, 10 pulses | P: disturb immunity; conventional 약 6000 pulses calibration 및 +92% endurance 결과 | PDF 6–7 Figs.12–15/17 |
| 네 지표 normalized score | DIBL/GIJL/PGE/1-RD 각 best=1,worst=0, 합산 | P: 균형점 Hfin12 nm 선택; 정규화 끝점·동일 가중치 의존 | PDF 7/143324 §III-E, Fig. 16 |

1-RD는 D0 SN 전압 증가를 포함한 disturbance 평가이며 static hold retention이 아니다. 실제 failure voltage 및 10-pulse waveform에서 수천 회까지 이어지는 환산 상세는 NOT REPORTED. Cgd/RWL/absolute read margin/온도별 retention CDF는 없다.

#### D. 정량 기준

**EXPLICIT OPTIMIZATION RULE:** 네 지표 min–max 정규화 후 동일 단위 가중 합산. **NO EXPLICIT HARD THRESHOLD:** 각 지표의 허용 상한, 최소 retention 개선율, yield 조건은 없다. Vth=.54 V는 구조 sweep의 calibration target이고, ±1.3 mV는 결과; 성능 합격 오차가 아니다. Hfin12 nm, +19/+29/−87/+92%는 REPORTED RESULT다.

#### E. 선정 방식

실제 multi-objective scalar score로 **단일점**을 선택한다. Pareto front 또는 제약 기반 연속 feasible region을 산출하지 않는다. 점수의 좋은 항목이 나쁜 항목을 보상할 수 있으므로 CMP에서는 필수 기능 통과 후 선호 순위를 비교하는 데 한정하는 것이 타당하다(CMP-PROPOSED).

#### F. 온도·Retention

온도는 NR. pulse-driven SN 변화와 disturbance endurance를 평가하며 VSN1→.8 hold tRET는 없다. body stress GIJL은 정상 hold 누설과 바이어스가 다르다. 6000–8000 pulse 산업 맥락은 MEB retention 기준이 아니다.

#### G. 적용성

**ADAPTABLE WITH CONDITIONS:** 지표 간 trade-off 및 보정 변수 분리, 점수 민감도 분석. **NOT TRANSFERABLE:** Hfin12 nm, equal weights, 정규화 끝점, −12 V 누설 감소율. **MECHANISM / BACKGROUND ONLY:** adjacent-gate coupling과 field crowding. 다목적 설계 평가 자체는 신규성이 아니나 CMP의 기능 제약 기반 MEB 범위는 별도 검증 대상이다.

### P06 — Pi-BCAT and explicit Ion constraint

#### A. 서지·목적

Lee 외(2020), Electronics9,1908, DOI 10.3390/electronics9111908. PDF 1–14=본문 1–14, PDF 15 이용조건. storage-node 쪽 partial buried insulator로 Ioff를 줄이는 Pi-BCAT을 3D Sentaurus로 제안한다. 실제 retention 측정 연구가 아니다.

#### B. 구조·조건

비교는 saddle RFinFET/Pi-RFinFET/asymmetric BCAT/long-junction BCAT/Pi-BCAT. BCAT gate depth80 nm, recess150 nm, peak doping1.45×10²⁰ cm⁻³, short junction82–92/long134–141 nm. RFinFET recess120 nm, peak1.05×10²⁰. Gaussian profiles. Pi-BCAT nominal Lin6 nm, silicon film60 nm, insulator end145 nm(PDF 2–3 Figs.1–2). **Lin은 gate oxide와 insulator 사이 거리**, film은 SN 표면부터 insulator까지 Si 두께, gate depth는 위쪽 contact에서 buried gate top까지의 깊이로 recess와 다르다. 비교 gate depth70/80/90 nm. WF·body 전체 도핑·구체 모델 옵션·온도·mesh/convergence·실측 calibration은 NR. Hurkx 문헌 인용만으로 전체 simulation model configuration을 확정하지 않는다.

#### C. 실제 지표

| 지표·정의 | 조건·단위·비교 | 역할·이유·한계 | 원문 위치 |
|---|---|---|---|
| Ion/Ioff와 IV | Ion VG1,VD.1; Ioff VG−.5,VD1.2; A | P/C: leakage–drive trade-off; 후반 일부 legend VD1.2/axis.1 충돌 | PDF 4 Fig. 3; PDF 11–12 Fig. 16/Table 1 |
| gm,max/SS | VD.1; A/V,mV/dec | V/M: on control 확인; 허용 상한 없음 | PDF 5 Fig. 5 |
| Vth/DIBL | V,mV/V; Vth extraction current NR | V/M: short-channel 비교 | PDF 6 Fig. 6 |
| potential drop width | 1.2→0 V spatial width | M: peak가 같아도 폭이 달라짐 | PDF 7 Fig. 8 |
| Ez, GBTBT spatial profile | oxide에서 1 nm cut; V/cm,cm⁻³s⁻¹ | M: field/generation 영역 변화; whole-device 적분과 다름 | PDF 7 Fig. 9 |
| Lin/film/gate-depth response | Lin6 vs12; film 약 60 nm 전후; gate70/80/90 | P/M: trade-off와 plateau; 제조 공차 보장 아님 | PDF 6–11 Figs.7–15 |
| Ion ratio=80% contour와 선택 Ioff | 각 gate depth의 asymmetric baseline | C/P: 같은 drive 손실에서 leakage 비교 | PDF 11–12 Fig. 16/Table 1 |

Table 1의 gate70/80/90 nm 선택값은 Lin5/5.5/5.75 nm, film50/60/70 nm, Ion2.21/2.25/2.31 μA, Ioff5.44×10⁻¹⁴/1.98×10⁻¹⁴/7.50×10⁻¹⁴ A, Ioff ratio38/33/38%다. SS(asym)=65/65.4/66, SS(Pi)=66.225/66.475/66.725 mV/dec; DIBL(asym)=1.81/3.63/4.73, Pi=.45/.95/1.45 mV/V. gm(asym)=7.22/7.40/7.64 μA/V, Pi=5.74/6.00/6.16 μA/V. 모두 REPORTED RESULT이며 80% 조건 외 공통 hard limits가 아니다.

#### D. 정량 기준

**EXPLICIT DESIGN CONSTRAINT:** Ion(Pi)/Ion(asymmetric)=0.80를 **동일 gate depth**에서 맞추어 Lin/film을 고르고 Ioff를 비교한다. 논문의 사용은 등비 contour이며 모든 구조에 대한 보편적 “≥80%” 규격이 아니다. Ion bias는 위 표를 따른다. T=NR. 이유는 drive 손실을 통제한 leakage 비교. 33–38% Ioff ratio는 결과이며 최소 저감률 조건이 아니다. PDF 3의 5.95×10⁻¹⁴→2.54×10⁻¹⁴ A는 비율 42.7%, 감소 57.3%(LIT-DERIVED). abstract의 “43% lower”와 상충한다.

#### E. 선정 방식

저자 표현에 effective parameter range가 있고 다차원 구조 contour를 제시하지만, 최종 Table 1은 정해진 gate depth별 80% Ion 선택점이다. 이를 **온도별 MEB 연속 합격 구간**이라고 확대할 수 없다. leakage 단독 최소화도 아니다.

#### F. 온도·Retention

T sweep, cell capacitor, 초기/종료 VSN, floating hold, direct transient 및 read 판정은 NOT REPORTED. Ioff 저감이 cell leakage에 유리하다는 기대와 실제 retention 검증을 구분한다.

#### G. 적용성

**DIRECTLY REUSABLE METHOD:** 같은 조건 baseline과 비교해 성능 손실을 통제하는 논리. **ADAPTABLE WITH CONDITIONS:** Ion 제약 contour와 다른 지표 검증. **NOT TRANSFERABLE:** 80%, Lin/film 수치, 70–90 nm 깊이. CMP에는 insulator와 동일 물리 구조가 없다. 공간 field width의 중요성은 peak 하나로 누설을 설명하지 말아야 하는 근거다.

### P07 — Structural variation in 20 nm single-WF BCAT

#### A. 서지·목적

Sun, Baac, Shin(2022), Micromachines13,1476, DOI 10.3390/mi13091476. PDF 1–8=본문 1–8, PDF 9 이용조건. 3D deterministic TCAD로 BCAT 구조 변수의 DC 영향을 조사한다. 현행 CMP의 형상 계열과 가깝지만 동일 calibration·2D 물리 분기는 아니다.

#### B. 구조·조건

Sentaurus 3D, single W gate WF4.8 eV, Lgate20 nm, recess120 nm, tox5 nm, body B10¹⁷/S-D As10²⁰ cm⁻³ Gaussian. nominal junction48 nm(N=10¹⁷ cm⁻³로 정의), Wfin17 nm,Hfin48 nm, DBCAT36 nm. **DBCAT은 Si top에서 W까지의 nitride thickness/gate burial depth**이며 전체 recess120 nm와 다르다(PDF 2–4 Figs.1–2/Table 1). AR5/6/7, DBCAT24/36/48, Wfin11/17/23, Rfillet .4/.7/1 비교. junction sweep은 설명의 recess30–50%와 Table 1/Fig. 3의 27/40/53%가 상충한다. 물리 모델 Philips unified, Lombardi, Canali; “Hurkx trap-assisted tunnelling model”과 “band-to-band”를 연결한 문구는 정확한 BTBT/TAT 설정이 AMBIGUOUS. T·mesh convergence는 NR. 측정 직접 fit보다 기존 문헌 DC 값과의 plausibility 비교다.

#### C. 실제 지표

| 지표·정의 | 조건·단위·비교 | 역할·이유·한계 | 원문 위치 |
|---|---|---|---|
| ID–VG/ID–VD | transfer VD1.2 V, output 여러 VG; A/μm | P/V: nominal 대비 구조 민감도; endpoints 상세 재현 정보 제한 | PDF 4–6 Table 1/Fig. 3 |
| Vth constant current | I=10⁻⁷ A×W/L; V | P/V: nominal .656 V, gate control | PDF 5–6/Fig. 3 |
| SS | mV/dec, nominal76 | P: short-channel control; fit window NR | PDF 5–6 |
| Ion/Ioff | 무차원, nominal3.4×10¹⁰ | P: drive/leakage balance; on/off VG 정의 완전한 명시 부족 | PDF 5–6 |
| DIBL | mV/V, nominal23.6 | P: barrier sensitivity; 두 VD의 상세 조건은 재현 시 재확인 필요 | PDF 5–6 |
| structural sensitivity | DBCAT,junction,AR,Wfin,Rfillet | P/M: 설계 trade-off; stochastic yield 아님 | PDF 6 Fig. 3 |

E-field/BTBT 공간 적분, Cgd, 실제 cell retention, write/read, RWL 수치, 온도 sweep은 제시되지 않는다. 공정 AR의 void/bending 위험은 논의되지만 정량 제조 합격 구간은 아니다.

#### D. 정량 기준

**NO EXPLICIT DESIGN THRESHOLD.** Vth≈.7 V, SS<90 mV/dec, Ion/Ioff≈10¹⁰, DIBL<약 50 mV/V의 문헌 비교는 모델 plausibility 맥락이다. 이 논문이 각 sweep point에 적용한 pass/fail 표로 사용하지 않았다. Rfillet 효과 <5%도 관찰 결과다. 임의로 Vth/SS/DIBL CMP guardrail을 이식하지 않는다.

#### E. 선정 방식

각 변수의 DC trade-off와 sensitivity 분석. DBCAT을 깊게 할 때 gate control과 leakage의 균형을 논의하지만 절대 retention·온도별 optimum·다중 제약 feasible set은 없다.

#### F. 온도·Retention

T, 1T1C/Ccell/VSN endpoint/hold/read는 NR. GIDL 관련 논의가 직접 retention 증명은 아니다.

#### G. 적용성

**ADAPTABLE WITH CONDITIONS:** 구조 정의·constant-current Vth·normalized current 비교. **NOT TRANSFERABLE:** nominal DC 수치가 2D PAPER-CAL 검증이라는 주장. single-WF20 nm gate depth의 DC 영향 자체는 선행연구에 있고, 그 이후의 공간 generation–cell retention 연결이 CMP 검증 과제다.

### P08 — Trap-induced retention distribution and dual-WF

#### A. 서지·목적

Kyoung Yeon Kim, Kyung Kyu Min, Byung-Gook Park, EDL42(1),38–41(2021; online2020), DOI 10.1109/LED.2020.3037640. PDF 1–4=38–41. interface traps 때문에 생기는 retention tail을 TCAD+statistical 계산으로 설명하고 upper low-WF gate로 개선한다.

#### B. 구조·조건

20 nm 3D saddle/recessed BCAT, TiN 기반 SW/DW 비교. SW WF4.66 eV, upper M2=4.1/4.3/4.5/4.66 eV. 정확한 CMP MEB 대응값 및 전체 doping/mesh convergence는 NR. leakage component Isub+Itrap, field-enhanced SRH와 trap count/location/energy 분포를 사용한다(PDF 2/39 Eqs.1–6). VD1.5, VG−.2, VBB−.8 V. C_s=10 fF, Vcc1.5 V, Et center−.15 eV, σEt=.025 eV, Nit=.8×10¹⁰ cm⁻²(PDF 3 Fig. 3). 50/60 nm 문헌 데이터와 비교한 모델 타당성이 곧 20 nm same-device 측정 calibration은 아니다.

#### C. 실제 지표

| 지표·정의 | 조건·단위·비교 | 역할·이유·한계 | 원문 위치 |
|---|---|---|---|
| Ileak=Isub+Itrap, Itrap=−ΣU(rj,Ej)(Gn+Gp) | field-enhanced SRH/statistical trap model | M: trap leakage의 분포; 전체 terminal BTBT 분해와 다름 | PDF 2/39 Eqs.1–3 |
| trap number/location/energy | Poisson/spatial/Gaussian distributions | M/V: weak tail 기원 | PDF 2 Eqs.4–6 |
| transfer/leakage IV and E-field | VD1.5,VG−.2,VBB−.8; A,MV/cm | M/V: DW가 drain field를 낮춤; IV는 retention transient 아님 | PDF 2–3 Figs.2/4 |
| retention CDF | s, cumulative probability %; T298/328/358 K | P: tail과 center 분리; termination voltage NR | PDF 3/40 Fig. 3 |
| density-dependent CDF | Nit8×10⁹/5×10⁹/10⁹/10⁸ cm⁻² | P/M: density 감소가 center와 tail에 다른 영향 | PDF 3 Fig. 3 |
| weak-tail RT at CP=10⁻⁶% | SW .29 s; WF4.5/.4.3/4.1에서 .36/.42/.44 s | P: 각각 24/45/51% 개선 보고; CP는 10⁻⁸ probability | PDF 3 Fig. 4(e) |
| Vth/Ion 변화 | DW/SW IV 비교, Vth 거의 유지·Ion 증가 | V: trade-off 확인; minimum Ion ratio 없음 | PDF 3 Fig. 4 |

Cgd, SS/DIBL 설계 제약, RWL, write/read transient 및 공정 yield pass criterion은 없다. Fig. 4의 RT 비교 온도를 Fig. 3의 한 온도로 임의 지정하지 않는다(NOT REPORTED/명시 불충분).

#### D. 정량 기준

**NO EXPLICIT PERFORMANCE THRESHOLD.** CP=10⁻⁶%는 평가 위치이며 양품 비율 요구가 아니다. .44 s 및 51%는 REPORTED RESULT. “>50% 개선”을 CMP 최소 retention 이득으로 사용할 수 없다. CP를 CDF10⁻⁶과 동일시하지 않는다: 10⁻⁶%=10⁻⁸(LIT-DERIVED).

#### E. 선정 방식

WF와 trap parameter에 따른 분포·tail 비교. low-WF 구조의 유리함을 보이지만 MEB sweep, 연속 feasible range 또는 동시 read/write/RWL 제약을 풀지는 않는다.

#### F. 온도·Retention

298/328/358 K가 독립 변수이며 분포가 온도와 trap에 따라 달라진다. TCAD leakage를 이용한 통계 계산이고 직접 write/hold/read transient가 아니다. VSN1→.8 V, 종료 실패 전압, 초기 write 및 floating node circuit 상세는 NR. P09의 endpoint를 이 논문에도 있었다고 소급하지 않는다.

#### G. 적용성

**ADAPTABLE WITH CONDITIONS:** CDF의 비교 확률과 온도를 맞추는 방법. **MECHANISM / BACKGROUND ONLY:** trap/tail와 dual-WF field 개선. **NOT TRANSFERABLE:** 4.1 eV 및 51%/0.44 s. Nominal single-cell CMP는 별도 통계 모델 없이 weak-cell tail 개선을 주장할 수 없다.

### P09 — Retention distribution Part I

#### A. 서지·목적

Liu 외 16인(2024), TED71(8),4462–4468, DOI 10.1109/TED.2024.3409510. PDF 1–7=4462–4468. BCAT leakage를 trap/non-trap 및 온도에 따라 모델링하고 defect-based Monte Carlo로 retention distribution을 설명한다. 700,000 parallel BCAT/Keithley4200A 측정과 3D TCAD를 결합한다.

#### B. 구조·조건

PDF 2/4463 TableI: WL recess156 nm, metal depth65 nm, STI280 nm, side/bottom oxide6.8/5.6 nm, finH23/W28 nm, top/bottom metal thickness40/74 nm. **baseline의 두 metal WF는 모두 4.54 eV**다. dual-metal 형상을 곧 WF contrast로 해석하지 않는다. SC1 V, BL.5 V, WL−.2 V, substrate−.7 V. 비대칭 SC/BL doping은 contour로 보이지만 전 profile 수치는 NR. Fermi, inversion/accumulation mobility/high-field saturation, Old Slotboom, doping-dependent SRH+Hurkx field enhancement, Hurkx BTBT. mesh/convergence 상세 NR. normalized ISC(a.u.)–VWL를 T300/325/350/375 K에서 measurement와 비교한다(Fig. 1). metal depth65 nm는 CMP36 nm와 다른 구조다.

#### C. 실제 지표

| 지표·정의 | 조건·단위·비교 | 역할·이유·한계 | 원문 위치 |
|---|---|---|---|
| terminal electron/hole currents, G–R/DD 성분 | bias별 sign/path; current normalized a.u. | M/V: GIDL/GIJL/subthreshold/diffusion/gate leakage 식별 | PDF 3/4464 TableII/Fig. 2 |
| SRH spatial rate 및 bias 분리 | cm⁻³s⁻¹; VSC−VWL=0 등으로 GIDL 억제 | M: GIJL와 GIDL 분리 추출; 같은 bias에서 자동 pure decomposition 아님 | PDF 3 Fig. 3 |
| Arrhenius activation energy | GIDL/GIJL≈.6 eV, DD≈1.3 eV | M: T별 지배 성분 설명; crossover 온도 일반화 금지 | PDF 3 Fig. 4 |
| Itotal=Inontrap+ΣΔIIT; Inontrap=IGIDL+IGIJL+IDD | compact equations; trap Et,Xi,E,T 의존 | M/P: 분포 예측; fitted coefficients 필요 | PDF 4–5/4465–4466 Eqs.3–15 |
| single-trap ΔIIT, spatial weighting, ΔEa/B(E) | aA, nm, eV; 300–375 K,25 K step | M/V: location/energy dependence | PDF 4–5 Figs.5–8 |
| retention CDF | C=10 fF, VSC1.0→.8 V; ms, probability | P: assumed data-loss endpoint; other circuit variation ignored | PDF 5–6 §IV/Fig. 9 |
| trap MC/statistics | 5×10⁷ runs,약 5.5σ; Poisson mean3, Nit5×10¹⁰ cm⁻² | P/M: rare-tail estimation; sampled/model-dependent | PDF 5–6 §IV/Fig. 9 |
| T-dependent RT head/center/tail | T300/325/350/375/400/425 K; CDF1/.5/2×10⁻⁸ | P/M: tail의 서로 다른 온도 응답 | PDF 6/4467 Fig. 10 |

trap position은 Si/IL 0–195 nm와 Si/STI 0–280 nm의 uniform distribution, Et는 Gaussian center −.15 eV/σ=.025 eV다. Head Ea는 낮은 T에서 .625/high T에서 1.184 eV, center .79, tail .6 eV다(PDF 6 Fig. 10). 모두 fitted/reported 결과이며 기준값이 아니다. high>50 aA, medium1.5–2 aA, low<.1 aA의 trap group은 해석용 분류(PDF 5 Fig. 8)이며 허용 leakage 조건이 아니다.

#### D. 정량 기준

**EXPLICIT EVALUATION ENDPOINT:** VSC1.0→0.8 V를 데이터 손실로 가정, C=10 fF. **NO EXPLICIT MEB DESIGN THRESHOLD:** 최소 tRET, Ion, RWL, yield 합격값은 없다. CDF 위치와 5.5σ coverage는 분석 조건이다. introduction의 <64 ms weak cell 맥락을 모든 BCAT 설계의 보편 규격으로 채택하지 않는다.

#### E. 선정 방식

모델 calibration 및 retention 분포 설명이 목적이다. trap 통계와 온도 민감도는 다루지만 MEB별 feasible range 또는 design Pareto를 산출하지 않는다.

#### F. 온도·Retention

**원문 확인:** §IV에 10 fF, initial VSC1 V, .8 V까지 감소하면 data loss라고 가정함이 명시된다(PDF 5–6/4466–4467). 기본 분석 300 K, Fig. 10은 300–425 K. 이 결과는 compact leakage/statistical 계산이며 direct transient write/hold/read 및 sense amplifier의 실패 검증으로 제시하지 않는다. 원문에 상세 numerical integration implementation이 명시되지 않아 후술 ∫C/I 식을 저자 구현이라고 단정하지 않는다. 고온 DD 증가로 head/center/tail의 activation energy가 달라진다. 본문의 110°C와 결론의 120 °C crossover 표현 차이는 §14에 남긴다. 동일 온도에서 trap 조건 비교는 있으나 “36 nm 동일 T” protocol은 CMP 제안이다.

#### G. 적용성

**DIRECTLY REUSABLE METHOD:** 평가 endpoint를 명시하고 scalar RT와 CDF를 구별하는 방법. **ADAPTABLE WITH CONDITIONS:** 온도·trap·leakage components와 compact-to-transient 교차 검증. **NOT TRANSFERABLE:** 0.8 V=실제 CMP read failure, 특정 Ea/crossover, double-metal 통계 모델의 숫자. 1→.8 V 정의의 문헌 근거는 확보됐지만 물리적 read 정당성은 별도다.

### P10 — Retention distribution Part II / PBTI

#### A. 서지·목적

Liu 외(2024), TED71(8),4469–4475, DOI 10.1109/TED.2024.3409512. PDF 1–7=4469–4475. P09의 companion으로 PBTI-generated interface traps와 구조 최적화의 fresh/aged trade-off를 측정·3D TCAD·compact MC로 분석한다.

#### B. 구조·조건

기본 BCAT/physics/retention 모델은 Part I을 참조한다. 이 문서에서 1→.8 V의 독립적인 새 출처를 주장하지 않는다. 700,000 parallel BCAT stress–measure 및 charge pumping. Fig. 1 온도 298/343/373 K. 정확한 모든 stress voltage/time protocol은 재현에 충분히 명시되지 않아 NOT REPORTED로 둔다. 작동 Vpp≈3 V 언급을 accelerated stress voltage로 대체하지 않는다. gate top/bottom WF4.04/4.29/4.54/4.79/5.04 eV sweep; side oxide5.8/6.8/7.8 nm 등 oxide variation; top metal thickness20/30/40/50 nm. fresh 구조 비교 RT는 300 K(PDF 5). mesh convergence NR. RDF는 sIFM/ΔVSC 분포로 반영.

#### C. 실제 지표

| 지표·정의 | 조건·단위·비교 | 역할·이유·한계 | 원문 위치 |
|---|---|---|---|
| ΔGIDL/ΔGIJL, charge-pumping current, Ea | stress duration,T298/343/373; current,Ea≈.65 eV | M/V: aging trap 기원; GIJL 증가가 더 큼 | PDF 2/4470 Fig. 1 |
| saddle-fin field/generated trap location | thin oxide region 비교 | M: PBTI localization; gate geometry 의존 | PDF 3/4471 Figs.2–4 |
| trap energy spectrum | dual-Gaussian model/측정 | M/V: stress-induced distribution | PDF 4/4472 Fig. 5 |
| aged retention CDF | base Nit3.22×10¹⁰ cm⁻²; ΔNit/Nit1/5/10 | P: aging weak tail; 10배에서 CDF10⁻⁹≈6σ 약 20%감소는 결과 | PDF 4 Fig. 6 |
| Itotal=Ifresh+Iaging, ΔA/ΔE parameters | compact update | M/V: aging model; sign/식 전사 주의 | PDF 4–5 Eqs.1–5/Figs.7–8 |
| WF/oxide/top-metal RT 변화 | 300 K, baseline 대비 | P/M: geometry/electrostatics trade-off | PDF 5/4473 Figs.9–10 |
| RDF에 따른 RT tail | sIFM; −6σ 근처 약 20% 열화 | P/V: variability cost; universal yield bound 아님 | PDF 6/4474 Fig. 11 |
| ΔRTtail vs ΔIdsat | tail CDF10⁻⁶, baseline 대비 % | P: 두 성능 동시 개선을 선호 | PDF 6 Fig. 12 |
| optimized fresh/aged comparison | top WF4.54 vs4.1 eV | P/M: fresh improvement와 relative aging sensitivity 비교 | PDF 6 Figs.13–14 |

Cgd, RWL delay, 직접 write/read margin, 온도별 MEB optimization은 없다. ΔIdsat 추출의 전체 on-bias 세트는 명확하지 않아 CMP Ion@VG1.2/2 V와 동일시하지 않는다.

#### D. 정량 기준

**EXPLICIT DESIGN PREFERENCE:** Fig. 12에서 ΔRTtail>0 및 ΔIdsat>0 영역을 바람직하게 본다. 엄격한 전체 조건 pass/fail feasible region 또는 제조 수율 보장은 아니다. CDF10⁻⁶은 tail 비교 위치다. aging/RDF 약 20% 열화는 REPORTED RESULT이지 허용 한계가 아니다. **NO EXPLICIT NUMERICAL PENALTY CAP:** Ion95%,RT25%,RC10% 등의 기준은 없다.

#### E. 선정 방식

retention–drive trade-off plot과 fresh/aged 설계 비교. 수학적 Pareto frontier 알고리즘, knee 탐색, 온도 최악 조건의 MEB 연속 구간을 보고하지 않는다. top metal thickness 증가는 경계를 위로 이동시키는 조건이므로 P02의 fixed-PEB에서 MEB를 깊게 해 poly를 늘리는 경우와 다르다.

#### F. 온도·Retention

PBTI temperature dependence와 300 K geometry optimization을 구분한다. Part I endpoint를 상속한 모델이며 independent cell write/read transient가 아니다. optimized structure의 상대 aging degradation이 크다고 해서 aged absolute RT가 반드시 baseline보다 나쁘다고 단정하지 않는다. 초기 절대 RT와 degradation ratio를 함께 봐야 한다(PDF 6 Fig. 14).

#### G. 적용성

**ADAPTABLE WITH CONDITIONS:** retention과 drive를 같은 baseline으로 비교하고 fresh/aged를 나누는 방법. **MECHANISM / BACKGROUND ONLY:** PBTI·RDF의 tail 영향. **NOT TRANSFERABLE:** WF optimum, metal thickness trend의 단순 MEB 대응, 상대 aging loss를 절대 열화로 바꾸기. 현재 CMP에 aging 모델이 없으므로 reliability robustness는 향후 별도 주장이다.

### P11 — Variation-aware 3D BCAT

#### A. 서지·목적

Seokchan Yoon, Jaehyuk Lim, Changhwan Shin, SST40,015010(2025; published2024-12-11), DOI 10.1088/1361-6641/ad98bb. PDF 1 표지, PDF 2–9=본문 1–8. surface roughness와 systematic curvature가 DC 평균·분산에 미치는 영향을 3D quasi-atomistic 형상/TCAD로 분석한다. full atomistic transport 계산이라는 뜻은 아니다.

#### B. 구조·조건

Sentaurus+MATLAB. L20,tox5,Hfin48,Wfin17,recess120,buried depth36 nm; body B10¹⁷,S/D As10²⁰ cm⁻³(PDF 5/본문 4 Table 1). WF 값은 NR. SRH, doping-dependent/Enormal/high-field mobility, Old Slotboom, Hurkx BTBT. surface ACVF에 σ, ξ20/50 nm, α=1, θ 사용; source/drain과 fin의 공정 차이를 반영한 두 ACVF 및 네 random noise sequence로 8 surfaces를 구성(PDF 3–4/본문 2–3 Eq.1/Figs.2–6). σ=.2/.5/.8, R=0/5/10, A=.3/.7/1의 변화; σ/R의 수치 단위 표기가 충분치 않은 부분은 AMBIGUOUS로 보존한다. reference σ=.5,R0,A1. 총 7 cases,150 samples/case. 측정 saddle-fin IV와 VD=.5 V에서 비교하지만 문헌의 sub40-nm 측정을 동일 20-nm 제작 검증으로 간주하지 않는다(PDF 5 Fig. 7). sample transfer plot VD=.05 V. 온도·mesh convergence·각 saturation extraction 전체 bias는 NR.

#### C. 실제 지표

| 지표·정의 | 조건·단위·비교 | 역할·이유·한계 | 원문 위치 |
|---|---|---|---|
| random surface/ACVF | σ,ξ,α,θ,R,A | M: variability input; distribution assumed | PDF 3–4/본문 2–3 Eq.1/Figs.2–6 |
| calibrated/sample ID–VG | measurement VD.5, sample VD.05; A/A per μm 구분 | V: nominal fit와 sample scatter | PDF 5/본문 4 Fig. 7 |
| VT,sat/VT,lin mean/SD | constant current10⁻⁷A×W/L; V/SD mV | P: threshold distribution; tolerance 미설정 | PDF 6–7/본문 5–6 Tables2–4/Figs.8–10 |
| ID,sat/ID,lin mean/SD | μA/μm, SD 및 상대% | P: drive variability; full bias NR | 동일 |
| Ioff mean/SD | pA/μm | P: leakage variability; retention CDF 아님 | 동일 |
| SS/DIBL mean/SD | mV/dec,mV/V | P: short-channel variability | 동일 |

σ=.2→.8에서 DIBL SD1.04→16.69 mV/V, Ioff SD.02→.17 pA/μm는 Table 2의 관찰값이며 합격 기준이 아니다. Table 3은 IDsat 행 중복/IDlin pA 표기 등 지표명·단위 충돌이 있어 추정 수정하지 않는다. Cgd/E-field/BTBT spatial integral, retention, write/read, RWL, temperature sweep은 없다.

#### D. 정량 기준

**NO EXPLICIT THRESHOLD.** 150 samples, roughness/curvature set, 평균·SD는 분석 설계와 결과다. ±σ 범위 또는 특정 yield를 합격으로 채택하지 않는다. 150개 표본은 rare 6σ tail 실증이 아니다.

#### E. 선정 방식

random+systematic variation의 sensitivity 및 mean/SD 비교. stochastic robust optimization과 공정 허용 범위 선정은 수행하지 않는다. nominal 평균의 유리함과 분산 확대가 다른 결과임을 보인다.

#### F. 온도·Retention

온도와 cell retention은 NR. DC current variation만으로 tRET 분포를 계산하거나 read 실패를 주장하지 않는다. thermal robustness와 process robustness는 구별해야 한다.

#### G. 적용성

**ADAPTABLE WITH CONDITIONS:** 같은 구조의 반복 표본과 평균·SD를 함께 제시하는 방법. **NOT TRANSFERABLE:** σ/R 단위 추정, SD를 허용치로 변환,150 samples로 weak-tail yield 주장. **MECHANISM / BACKGROUND ONLY:** nominal MEB 결과만으로 공정 강건성을 보장할 수 없다는 근거.

## 5. Cross-Paper Metric Frequency and Role Matrix

P=최종 성능 평가/최적화 목적, C=명시 제약, M=메커니즘, V=검증/보조, —=계산·추출·제시 없음, ?=근거 불명확. **논의만 한 지표는 실제 추출로 세지 않는다.** 예컨대 P02의 RWL/RC 언급과 P05의 equivalent coupling을 각각 실측 RWL/Cgd로 세지 않는다. 온도 열의 P/V는 별도의 온도 합격 조건을 뜻하지 않는다. 공정 변수 deterministic sweep과 stochastic variation을 열 안에서 구별한다.

| ID | Retention time | VSN/charge | GIDL/total/Ioff | BTBT/trap leakage | Cgd/G–D coupling | Drain E | Ion/ratio | Vth |
|---|---|---|---|---|---|---|---|---|
| P01 | — | — | P/V | M | — | M/V | — | — |
| P02 | — | — | M/V | M | — | P/M | V | V |
| P03 | — | P/C | V | — | — | — | V | V |
| P04 | — | — | — | — | — | — | — | — |
| P05 | — | P/M | V | M | — | M | V | V |
| P06 | — | — | P | M | — | M | C/P | V |
| P07 | — | — | P | ? | — | — | P | P |
| P08 | P | — | M/V | M | — | M | V | V |
| P09 | P | M | M/V | M | — | M | — | — |
| P10 | P | M | M/V | M | — | M | P | — |
| P11 | — | — | P | — | — | — | P | P |

| ID | SS | DIBL | Write | Read/margin | RWL/RC | Temperature | Process/statistical variation | Reliability/weak/distribution |
|---|---|---|---|---|---|---|---|---|
| P01 | — | — | — | — | — | V/M | — | — |
| P02 | V | — | — | — | — | — | — | — |
| P03 | V | — | P/C | C | — | — | P(deterministic) | — |
| P04 | — | — | — | — | — | P/V | V(chip categories) | P/C(errors/ECC) |
| P05 | V | P | — | — | — | — | P(deterministic) | P(1-RD) |
| P06 | V | V | — | — | — | — | P(deterministic) | — |
| P07 | P | P | — | — | — | — | P(deterministic) | — |
| P08 | — | — | — | — | — | P/M | P/M(trap statistics) | P(CDF) |
| P09 | — | — | — | — | — | P/M | P/M(trap statistics) | P(CDF) |
| P10 | — | — | — | — | — | M/V | P/V(traps/RDF) | P(aging/CDF) |
| P11 | P | P | — | — | — | — | P(random+systematic) | — |

P09/P10의 VSN은 retention model endpoint/variation 입력이며 direct transient waveform이 아니다. P04의 retention-related refresh/BER는 tRET 열에 넣지 않았다. P03의 read는 charge-sharing criterion이며 sense amplifier read waveform을 실제 추출했다는 뜻이 아니다. P05의 adjacent gate capacitive mechanism은 G–D coupling 열의 범위 밖이다. P07의 Hurkx 표기는 §14의 모호성 때문에 ?다. P11이 BTBT model을 켰다는 사실만으로 BTBT generation metric을 사용했다고 세지 않는다.

위 표 기준 실제 사용 편수(P/C/M/V 중 하나 이상; ? 제외)는 다음과 같다. 넓은 묶음이므로 빈도가 높아도 필수성이나 같은 정의를 뜻하지 않는다.

| 지표군 | 편수/11 | 해석 |
|---|---:|---|
| Retention time | 3 | P08–P10의 통계 모델; direct cell transient 논문은 없음 |
| VSN/charge | 4 | P03/P05 waveform과 P09/P10 model 입력은 다름 |
| GIDL/total/Ioff | 10 | 서로 다른 leakage·정규화·bias를 한 이름으로 합치면 안 됨 |
| BTBT/trap leakage | 7 | 주로 메커니즘; terminal Ioff 목적과 중복되지만 역할 다름 |
| Cgd/G–D coupling 실제 추출 | 0 | 문헌 빈도가 낮아도 CMP의 causal hypothesis 검증에는 조건부 가치 있음 |
| Drain E | 7 | 자주 사용한 물리 지표; max 하나로 integral current 대체 불가 |
| Ion/ratio | 8 | drive 확인·trade-off에 흔함; 공통 보존율 없음 |
| Vth | 7 | calibration/성능/variation 역할 혼재 |
| SS / DIBL | 6 / 4 | control 지표; 모든 연구에 필수는 아님 |
| Write / Read criterion | 1 / 1 | P03의 fixed window; CMP 질문 때문에 별도 검증 필요 |
| RWL/RC 실제 추출 | 0 | P02는 penalty 논의만; 미제공 Park PDF에서의 여부는 UNKNOWN |
| Temperature | 5 | P01/P04/P08/P09/P10; 같은 T set이나 worst-case optimization 아님 |
| Process/statistical variation | 9 | deterministic sweep까지 포함; 제조 yield는 별도 문제 |
| Reliability/weak/distribution | 5 | P04/P05/P08–P10; 서로 다른 failure modes |

최종 목적만 보면 leakage/Ioff를 P로 쓰는 P01/P06/P07/P11, Ion을 P/C로 쓰는 P06/P07/P10/P11이 각 4편이고 retention P는 3편이다. 물리 보조로는 leakage decomposition과 E-field가 자주 동반된다. Ion–Ioff–Vth/SS/DIBL, retention CDF–trap statistics–temperature, field–generation의 조합이 반복된다. Ion/Ioff ratio는 두 원값을 감추고, Vth/SS/DIBL은 모두 gate control과 관련되어 일부 중복된다. Emax, E@BTBT, Gmax, ∫G는 각각 위치·peak·부피 정보가 달라 완전히 중복되지 않는다. 표본이 작고 연구 목적이 달라 빈도 순위만으로 CMP 필수 지표를 결정하지 않는다(PAPER-INFERRED).

추가 실제 지표: P04 power/performance/BER/ECC/Vmin, P05 GIJL/PGE/1-RD/score, P06 gm/potential drop width, P09 Ea/spatial weighting, P10 charge pumping/PBTI/ΔNit, P11 mean/SD. 이들은 §4 C에 기록했고 본 목적에서 필요 여부를 §11에 평가한다.

## 6. Explicit Threshold and Constraint Evidence

| ID | Metric | Explicit threshold/rule | Reference/baseline | Bias/T/calculation | Author rationale | Source location | Classification / CMP transferability |
|---|---|---|---|---|---|---|---|
| P01 | model fit | NO EXPLICIT THRESHOLD | TCAD/measurement vs compact | T−40/25/100 °C | low-field까지 설명 | PDF 5/2896 Figs.5–6 | 수치 fit 허용치 NR |
| P02 | target Ion, RWL | NO EXPLICIT NUMERICAL THRESHOLD | calibrated dual-WF 구조 | standby bias §4 B; T NR | PEB로 Ion 우선, MEB로 leakage 조정 | PDF 4 Figs.5–7/결론 | LIT-EXPLICIT qualitative rule; 숫자 이식 불가 |
| P03 | VSN pass | ≥0.698 V after10 ns write+300 ms hold | ideal/no-BOX vs etch/BOX | WL3/−.2,body−.6,BL.5; T NR; Eq.1–2 | read charge sharing signal 확보 | PDF 7–8 Eqs.1–2/Fig. 12 | EXPLICIT DESIGN CONSTRAINT; 회로 조건 재설정 필요 |
| P03 | refresh reference | 64 ms(인용),300 ms(평가 가정) | JEDEC 언급/분포 median | 표준 원문 NOT VERIFIED | 장기 hold 판정 | PDF 7–8 §4 | EXTERNAL STANDARD 언급과 author assumption 분리 |
| P04 | system correctness | CE/UE/SDC 및 workload 성공으로 boundary 탐색; 공통 수치 cap 없음 | nominal voltage/64 ms refresh | workload,T50/60 °C | 오류/전력 trade-off | PDF 2–4/7–9 | 명시 검사 방법; CMP numerical threshold 아님 |
| P05 | calibration | Vth=.54 V | Hfin sweep의 공변 doping/geometry 보정 | VD1,100 nA; T NR | 비교에서 Vth 유지 | PDF 2/143319 Fig. 2 | calibration target; <1.3 mV는 REPORTED RESULT |
| P05 | design score | 4 metrics best1/worst0,동일 가중 합산 | 19→1 nm sweep extrema | DIBL/GIJL/PGE/1-RD,각 bias 다름 | 상충 효과 균형 | PDF 7/143324 §III-E/Fig. 16 | EXPLICIT OPTIMIZATION RULE; hard threshold 없음 |
| P06 | Ion ratio | IonPi/IonAsym=80% | 같은 gate depth asymmetric BCAT | Ion@VG1 VD.1; T NR; 후반 legend 충돌 주의 | drive 손실을 통제해 Ioff 비교 | PDF 11–12 Fig. 16/Table 1 | EXPLICIT DESIGN CONSTRAINT; 비율 방법 조건부,80% 이식 불가 |
| P07 | DC plausibility | NO EXPLICIT DESIGN THRESHOLD | 문헌 Vth≈.7,SS<90,ratio≈10¹⁰,DIBL<약 50 | nominal VD1.2; T NR | model plausibility | PDF 5–6 | 외부 비교값; pass/fail 조건으로 사용 아님 |
| P08 | weak-tail location | CP=10⁻⁶%=10⁻⁸ probability | SW4.66 vs upper low-WF | VD1.5,VG−.2,body−.8; Fig. 4 T NR | rare tail 비교 | PDF 3/40 Fig. 4 | EXPLICIT ANALYSIS LOCATION; performance/yield threshold 없음 |
| P09 | RT endpoint | C10 fF, VSC1→.8 V | 동일 BCAT compact model | standby SC1/BL.5/WL−.2/sub−.7; default300 K | data loss를 가정 | PDF 5–6/4466–4467 §IV | EXPLICIT EVALUATION DEFINITION; actual read threshold 미검증 |
| P09 | tail coverage | 5×10⁷ MC,약 5.5σ; Fig. 10 tailCDF2×10⁻⁸ | Poisson/Gaussian trap model | T300–425 K | head/center/tail 분리 | PDF 5–6 Figs.9–10 | analysis condition; minimum yield 아님 |
| P10 | two-objective preference | ΔRTtail>0,ΔIdsat>0 선호 | fresh baseline design | CDF10⁻⁶,300 K; full Idsat bias NR | retention과 drive 동시 향상 | PDF 6/4474 Fig. 12 | EXPLICIT PREFERENCE; formal all-condition constraint 아님 |
| P11 | variability | NO EXPLICIT THRESHOLD | σ=.5,R0,A1 reference |150 samples/case,T NR | mean/SD 민감도 비교 | PDF 6–7/본문 5–6 Tables2–4 | SD tolerance 또는 yield 요구 없음 |

다음 숫자는 **REPORTED RESULT**이며 기준으로 사용하지 않는다: P05 Hfin12 nm와 GIJL87%/1-RD92%; P06 Ioff33–38%; P08 RT51%; P10 aging/RDF 약 20% 손실; P11 DC SD 값. 논문별 조건·원문 위치는 §4와 Appendix A에 있다. **Retention≥25% 개선, Ion≥95%, Write/Read≤10% 페널티, RWL cap, 45–49 nm 유효 범위는 이 문서에서 동결하지 않는다.** 제공된 문헌이 공통 수치로 정당화하지 않으며 기존 논의 예시를 제약값으로 승격할 수 없다.

서로 다른 .8 V(P09)와.698 V(P03)는 모순되는 보편 threshold가 아니다. capacitor, supply, BL sharing, 시뮬레이션 목적이 다르다. P06의 80%와 P10의 positive ΔIdsat도 평균내어 합칠 수 없다. 논문별 분모·node·bias·normalization·온도를 유지한다.

## 7. Retention Time Definition and Verification

| 문헌 | 실제 retention 관련 방법 | 초기/종료·C·조건 | direct transient/read 검증 여부 |
|---|---|---|---|
| P03 | 10 ns write 후 300 ms hold VSN 판정 | 실제 write로 형성된 초기 VSN; 종료≥.698 V; C ratio 상세 NR | mixed-mode SN transient; charge-sharing criterion, sense amplifier 독립검증 NR |
| P04 | refresh interval 증가 후 BER/ECC | 64 ms baseline; cell VSN/C NR | 실제 시스템 오류 시험; voltage-crossing tRET 아님 |
| P05 | repeated FPWL pulse 중 D0 SN/disturb endurance |8 fF,60 ns period; exact bit-flip V NR | disturbance transient; static retention 아님 |
| P08 | trap leakage 기반 retention CDF |10 fF,Vcc1.5; termination V NR | statistical model; write/hold/read sequence NR |
| P09 | leakage compact/MC retention CDF |10 fF,1.0→.8 V,other circuit variation ignored | direct full cell transient/read failure 검증 아님 |
| P10 | P09 모델의 fresh/aged CDF | Part I 상속; geometry comparison300 K | independent endpoint source 아님 |

**현재 CMP 정의(CMP-EXISTING):** tRET는 VSN이 1.0 V에서.8 V로 내려가는 데 걸리는 시간. P09가 같은 endpoint를 직접 명시한다. 논문 정의와 CMP 운영 정의가 대응한다는 사실은 확보됐지만, 모든 MEB/T에서 실제 write가 1 V까지 되는지, .8 V에서 BL read가 실패하는지는 미검증이다. .8 V는 평가 종료 전압으로 유지하고 실제 read failure threshold를 별도 측정하는 것이 적절하다(CMP-PROPOSED).

다음 식은 일반 charge conservation에 근거한 **CMP-PROPOSED / NOT LITERATURE EXPLICIT AS CMP PROTOCOL**이다. 이 11편에서 아래와 같은 전체 CMP 절차를 그대로 사용한 사례는 확인하지 못했다.

\[
t_{\rm RET}^{(1\to0.8)}=t[V_{SN}=0.8]-t[V_{SN}=1.0],\qquad
\frac{dQ_{SN}}{dt}=-I_{\rm net}(V_{SN},M,T).
\]

준정적이고 동일 경로를 따르며 순손실 전류가 양수이면,

\[
t_{\rm RET}=\int_{0.8}^{1.0}\frac{C_{\rm eff}(V,M,T)}{I_{\rm net}(V,M,T)}\,dV.
\]

Ceff=dQ/dV가 V에 의존할 수 있다. 단일 bias에서 CΔV/I를 쓰는 것은 I와 C가 해당 구간에서 일정하다는 추가 근사다. 절대전류를 임의로 더해 net loss로 쓰지 않는다. direct transient에는 junction/gate/subthreshold/BTBT 등 모든 활성 경로와 회로 상태가 포함되므로 정적 integration과 차이가 날 수 있다. 별도의 slow trap kinetics가 있으면 준정적 경로 가정도 검증해야 한다.

후속 실험은 두 자료를 함께 남기는 후보가 타당하다: (i) 동일 write pulse로 형성되는 실제 VSN,endwrite 및 동작 기반 hold/read 성능, (ii) 비교용 1.0→.8 crossing. 초기 1 V를 달성하지 못한 구조는 forced-initialization 결과만으로 usable이라 판정하지 않는다. 시작 시점/settling 정의와 write bias를 고정한다. crossing을 못 찾으면 simulation horizon까지의 **하한/censored** 결과로 표시하고 임의 extrapolation하지 않는다. 비단조 VSN이면 first crossing/settling 처리 규칙을 먼저 정한다.

read 검증에는 같은 VBL,precharge, CBL, pulse timing, sense load에서 ΔVBL(tread), 판정 시간 및 요구 signal을 정의해야 한다. P03 Eq.1–2를 구조에 맞춰 적용할 수 있지만 .698 V를 복사하지 않는다. 온도와 MEB에 따라 write가 다른 초기 Q를 만들면 retention ratio의 물리적 뜻도 달라져 초기화 방식별 결과를 구별한다.

## 8. Temperature Evaluation and Robustness

| ID | 온도와 용도 | baseline/비교 | 현재 질문에 남는 한계 |
|---|---|---|---|
| P01 |−40/25/100 °C, compact fit 검증 |같은 FinFET의 measured/model curves | 계획 K와 정확한 동일점 아님; no cell retention |
| P04 |DRAM50/60 °C, error/power |nominal refresh/workload별 |server-level 결과, lowT/380 K 검증 없음 |
| P08 |298/328/358 K, retention distribution |같은 trap/structure model |same-temperature MEB36 baseline 아님 |
| P09 |300–425 K,25 K step, head/center/tail |동일 BCAT/compact trap set |nominal과 tail의 T response 다름; no full W/R |
| P10 |298/343/373 K aging measurement; geometry RT300 K |fresh/aged와 baseline |aging T와 MEB optimization T 혼동 금지 |
| 나머지 |NOT REPORTED |— |300 K였다고 추정하지 않음 |

문헌은 온도에 따른 leakage·retention 변화의 필요성을 지지하지만 **233/300/340/380 K를 모두 평가하고 그 교집합으로 MEB 범위를 선택한 사례는 이 11편에서 확인되지 않았다**. 계획 온도는 CMP-EXISTING 계획이며 worst-case 선정 규칙은 CMP-PROPOSED다. 저온 mobility/threshold/write 및 고온 leakage를 함께 확인해야 하므로 380 K를 자동 유일 최악값으로 지정하지 않는다. P09의 head/tail Ea 차이도 단일 Ea 외삽의 한계를 보여준다.

### 세 평가 방식 후보

아래 식은 모두 **CMP-PROPOSED / NOT LITERATURE EXPLICIT**. M0=36 nm, T∈{233,300,340,380} K. 미결정 기호는 수치 threshold를 대신 채운 것이 아니다.

**A — 같은 온도 상대 비교**

\[
R_{\rm RET}(M,T)=\frac{t_{\rm RET}(M,T)}{t_{\rm RET}(36,T)},\qquad
G_{\rm RET}=R_{\rm RET}-1.
\]

P06의 same-geometry comparator, P08/P10의 baseline 상대 비교가 방법상의 근거다. T와 초기화/bias를 맞추면 온도 자체의 공통 감소를 분리하기 쉽다. 그러나 baseline이 매우 짧으면 ratio가 커도 기능은 실패할 수 있고, 분모가 미측정/censored/초기 write 실패이면 유효한 ratio가 아니다. A 단독으로 usable 판정하지 않는다. 최소 GRET는 **UNDECIDED**.

**B — 절대 조건**

\[
S_B(T)=\{M: t_{\rm RET}(M,T)\ge\tau_{\min}(T),\ \operatorname{WritePass}(M,T),\ \operatorname{ReadPass}(M,T)\}.
\]

P03의 fixed-window 기준 및 P04의 실제 오류 검사가 근거다. 실제 cell 동작과 연결되지만 τmin,write/read 실패 정의, 목표 operating condition을 정해야 한다. P03의 300 ms/.698 V 또는 P04의 64 ms/2.283 s를 직접 이식할 수 없다.

**C — 다중 제약**

\[
S_C(T)=\{M: \operatorname{RetentionAcceptable}(M,T),\ \operatorname{WritePass}(M,T),\ \operatorname{ReadPass}(M,T),\ d_j(M,T)\le b_j\},
\quad S_{\rm all-T}=\bigcap_T S_C(T).
\]

P06의 drive constraint, P10의 retention–Idsat trade-off, P05의 다목적 score가 관련 근거다. 그러나 위 집합/교집합 및 threshold bj는 이 논문들의 공통 규칙이 아니다. mandatory W/R와 목적에 맞는 DC guardrail을 먼저 정하고, 정보가 부족한 실제 RC를 proxy로 hard constraint하지 않는 방식이 후보이다. temperature-specific set과 all-T set을 모두 표시하면 range 이동과 robust 공통점이 구분된다. 수치나 연속 구간은 현재 미정이다.

thermal robustness(고정 구조에서 T 변경), process robustness(형상·도핑·traps 표본), aging robustness(시간·stress)는 서로 다른 축이다. P11의 150samples SD나 P10의 PBTI를 nominal T sweep의 검증으로 대체하지 않는다. 공정 강건 주장에는 각 T×process case의 기능 성공 및 불확실성 정보가 추가로 필요하다.

## 9. GIDL–Cgd–E-field–BTBT Mechanism Mapping

| 연결 | 원문에 직접 있는 근거 | CMP에 남는 검증/주장 경계 |
|---|---|---|
| gate geometry→electrostatics/field | P02 Figs.3–7; P06 Figs.8–9; P10 Figs.9–10 | 구조/WF/접합 깊이 고정과 동일 원점 확인 |
| Cgd→spatial drain E | 제공 11편에서 같은 MEB의 AC Cgd와 field를 함께 정량 검증한 사례 없음 | CMP의 co-variation은 상관; 인과를 단독 입증하지 않음 |
| field→BTBT/TAT | P01 Eqs.2–3/Fig. 3–4; P06 Fig. 9; P09 Figs.3–8 | field magnitude/location/volume·trap·T가 중요 |
| generation→terminal leakage | P01 Eq.1; P09 TableII/component extraction | net terminal current에 다른 경로·부호·수집 영향 포함 |
| leakage→retention | P08/P09 compact CDF; P03 실제 SN waveform | steady bias 감소가 실제 cell tRET 개선으로 그대로 전달되는지 추가검증 |
| retention→read success | P03 Eq.1–2/Fig. 12, P04 systemerrors | endpoint voltage만으로 실제 read success 대체 불가 |

E@BTBT는 maximum generation 위치의 전계이고 Emax는 전계 자체 peak다. BTBTmax는 local generation peak, BTBT spatial integral은 생성 부피/면적을 반영한다. 서로 다른 MEB에서 위치·폭이 이동하면 peak 순서와 integral/terminal current 순서는 달라질 수 있다(P06 Fig. 9와 CMP Atlas). **PAPER-INFERRED:** 고정 cut line만으로 shallow current 경로를 비교하면 중요한 영역을 놓칠 수 있다. 원문에 “CMP39/41 nm peak 원인”이 이미 증명됐다는 뜻은 아니다.

Hurkx ON/OFF 비교는 동일 모델에서 해당 옵션을 토글한 민감도 실험이다. off 상태는 carrier/potential solution도 바꾸므로 difference를 정확한 미시적 BTBT terminal component라고 이름 붙이지 않는다. signed difference, electron/hole currents, q∫G와의 단위/AreaFactor/2D width 일치, charge conservation, 공간 origin을 확인하는 후보가 타당하다(CMP-PROPOSED). 같은-bias total ID를 “GIDL-related total leakage”로 유지한다.

Project Cgd는 현재 특정 AC bias/frequency/model의 terminal coupling 지표다. 생산 array overlap capacitance, CBL 또는 SN effective capacitance를 대표한다고 주장할 수 없다. Cgd 감소가 write/read transfer에 미치는 영향을 말하려면 circuit node charge 및 동일 waveform을 검증해야 한다. 논문들에 Cgd가 없다는 이유만으로 제거할 필요도 없지만, retention primary outcome으로 승격할 근거는 없다.

우선적인 검증 순서 후보는 bridge → 동일 terminal/bias normalization → whole-Si spatial/path checks → 여러 VSN에서 net loss 확인 → direct cell retention → 실제 read margin이다. shallow residual을 trap 모델이 없는 분기에서 TAT로 명명하거나 drain–substrate로 확정하지 않는다. 전류 유입·유출과 source/body terminal까지 확인한 뒤 메커니즘 이름을 정한다.

## 10. Multi-Objective Optimization and Usable Range

| 선정 방법 | 실제 문헌 사례 | 범위/한계 |
|---|---|---|
| leakage–drive constraint | P06 Ion=80% contour/Table 1 | 조건부 구조점; universal80% 및 MEB window 아님 |
| 순차 설계 | P02 PEB→target Ion→MEB | field saturation/RC 논의; 정량 feasible set 없음 |
| fixed-window pass/fail | P03 VSN .698 V | 그회로/시간 조건의 통과; tRET optimum 아님 |
| weighted/min–max score | P05 four-metric sum,12 nm | 단일 best; 가중치·극값 의존; hard failure 상쇄 가능 |
| trade-off plane | P10 ΔRTtail vsΔIdsat | positive quadrant 선호; formalPareto front 아님 |
| statistical distribution | P08/P09/P10 CDF, P11 mean/SD | weak-tail/sensitivity; 제조 robustMEB region 아님 |
| worst-case T feasible intersection | NOT FOUND IN REVIEWED 11 PAPERS | 이번 CMP 제안; 신규성은 broader literature search 필요 |

질문별 답변은 다음과 같다. (1) MEB/DBCAT은 P02/P07에서 sweep·trade-off를 설명하며, 수치 optimum 정의가 충분하지 않다. (2) 누설만으로 선정하는 공통 관행은 없다. P06 drive constraint와 P05 다중 score가 반례다. (3) Ion은 실제 제약 사례가 있으나 SS/DIBL은 대개 성능·진단, RWL은 P02 논의 수준이다. (4) P08–P10에서 retention이 최종 목적이고 P03에서 셀 SN 기능이 판단에 포함되지만 MEB-only full cell 평가가 아니다. (5) T별 retention은 P09가 검증하나 T별 MEB optimum 이동은 확인되지 않았다. (6) P06의 effective parameter 표현/contour를 이산 데이터만으로 CMP 연속 MEB 구간에 대응할 수 없다. (7) P11은 구조 변동의 mean/SD, P10은 RDF/aging를 평가하나 W/R을 포함한 robust MEB window는 없다. (8) 수치 기준의 근원은 baseline 비교(P06), 회로식/저자 가정(P03), 모델 endpoint(P09), 내부 score(P05), 외부 plausibility(P07)로 서로 다르다.

**CMP-PROPOSED / NOT LITERATURE EXPLICIT:** 필수 기능·선정된 DC 제약을 통과한 **검증된 이산 집합**에서 Pareto-dominated 점을 표시하고, 선호 가중치는 사후 민감도 분석으로 다룬다. Score만으로 필수 기능 실패를 숨기지 않는다. knee를 쓰려면 변수/축 normalization, noise/mesh 민감도, slope-change 정의, endpoint 효과를 명시해야 한다. 현행 48 nm 구조 경계나 51 nm 끝점은 knee 증거가 아니다.

연속 범위를 주장하려면 통과/실패 경계 사이를 adaptive refinement하고, 정의한 수치 오차 내 response의 연속성·비단조 가능성·기능 조건을 검증해야 한다. 보간은 탐색 도구이며 미측정 영역의 합격 증거가 아니다. 공정 tolerance 범위를 말하려면 구조 공차와 확률/보수적 corner 선정, parameter interaction까지 검증해야 한다. 현재 결과는 후보점과 미검증 간격을 표시하는 수준이다.

## 11. Recommended CMP Evaluation Framework

아래 분류·개수는 **CMP-PROPOSED / NOT LITERATURE EXPLICIT**이며 문헌에 필수 지표 개수 규칙이 있다는 뜻이 아니다. 권장은 **Primary 1개 지표군**, **mandatory guardrail 2개 지표군(write/read)** 및 **conditional DC guardrail 1개 지표군**, **diagnostic 4개 지표군**이다. 한 지표군 안의 여러 추출값을 독립적인 목적함수로 중복 세지 않는다. 온도는 모든 지표의 평가 축이다.

| 지표 | 문헌 사용/근거 | 권장 역할·필요성·우선순위 | 중복/비용/제거 가능성 | 현재 주장 가능 범위·수치 상태 |
|---|---|---|---|---|
| Retention time(absolute+same-T ratio) | P08–P10; endpoint P09 | Primary, 필수; 연구 질문의 직접 결과 | transient 비용 높음; ratio는 같은 원값에서 파생; 제거 불가 | PAPER-CAL 미검증; threshold 미정 |
| GIDL-related total leakage | P01/P02/P06–P10 | Diagnostic①, 필수; terminal loss 관찰 | DC 비용 낮음; retention 대체 불가 | 특정 bias total ID; pure BTBT 주장 불가 |
| Hurkx ON/OFF sensitivity | P01/P09의 component 접근 관련; 동일 CMP 토글 사례는 없음 | Diagnostic②, 현재 불일치 해석에 필수 | 추가 DC 비용 중간; 경로 해결 후 일부 보조 자료로 이동 가능 | 옵션 민감도; 미시적 fraction으로 단정 불가 |
| Cgd | 제공 11편에 실제 AC 추출 없음 | Diagnostic③, 조건부; coupling 가설 검증 | AC 비용 중간; cell 결과 변화에 무관하면 보조 자료로 이동 가능 | project-internal terminal coupling; 공정 capacitance 검증 없음 |
| E@BTBT | P01/P06 field–generation 연계 | Diagnostic④ 공간 묶음, 유지 | spatial data 비용 낮음/분석 중간; Emax와 위치 비교 | hotspot local field; total current 단독 설명 불가 |
| BTBT spatial integral | P01 적분, P06 profile, P09 rate | Diagnostic④, 현재 핵심 | E/peak와 완전 중복 아님; whole Si 필요 | width/AreaFactor/단위를 맞춘 generation; terminal 수집 별도 |
| Ion | P06 constraint, P07/P10 trade-off | Conditional DC guardrail, 높음 | 이미 DC sweep에 포함; write 검증과 중복 가능 | bias별 drive 변화; 허용 보존율 미정 |
| Vth | P03/P05/P07/P11 | DC 묶음 validation, 중간 | control/초기 write와 연관; final objective로 중복 셀 필요 없음 | 고정 추출 정의에서 shift; 허용 범위 미정 |
| SS | P03/P05–P07/P11 | DC 묶음 diagnostic/조건부 guardrail | Vth/DIBL과 일부 중복; mechanism 본문 또는 보조 자료 가능 | fit window 명시 필요; limit 미정 |
| DIBL | P05/P06/P07/P11 | DC 묶음 diagnostic/조건부 guardrail | 두 VD 추가; SS와 연관되지만 동일 정보 아님 | bias-defined barrier response; limit 미정 |
| Write time/end voltage | P03 | mandatory guardrail①, 필수 | mixed-mode 비용 높음; tRET 초기 조건과 공유 | write 불충분을 가려낼 핵심; 시간/전압 조건 미정 |
| Read margin/success | P03 criterion, P04 실제 error | mandatory guardrail②, 필수 | 회로 load/timing 정의 비용 높음; 제거하면 usable 주장 불가 | .8 V와 actual failure 구분; threshold 미정 |
| RWL proxy | P02 RC 논의; 미제공 Park 미검증 | conditional structural validation, 낮음/별도 | 현재 별도 3D 기하 proxy; hard cap 설정 불가 | geometry trend 한정; 실제 RC 추가 모델 필요 |
| Temperature dependence | P01/P04/P08–P10 | 모든 primary/guardrail의 축, 필수 | 4 T로 비용 증가; single T로 대체 불가 | 현행 300 K 이외 미검증; worst T 미정 |

four diagnostics는 terminal leakage, model sensitivity, AC coupling, spatial field/generation의 네 묶음이다. Vth/SS/DIBL은 독립 목적을 과도하게 늘리기보다 gate-control validation 묶음에 둔다. Ion을 필수 hard threshold로 둘지 실제 write/read 통과 후 보조로 둘지는 연구자의 기능 요구에 따라 결정해야 한다. 현행 Atlas의 작은 DC변화만으로 무해하다고 확정하지 않는다.

Conditional validation에는 (i) 실제 WL RC를 주장할 경우 분포 resistance/load 모델, (ii) statistical weak cell을 주장할 경우 trap/process samples, (iii) aged robustness를 주장할 경우 PBTI를 추가한다. 이번 단계에서 모두 필수로 늘리면 연구 질문과 실행 비용이 확장된다. nominal 소자의 온도별 usable range를 연구 범위로 정하면 이러한 확장은 별도 과제로 둘 수 있다. 현재 질문을 완성하는 최소 검증은 **direct cell retention + write/read + 같은 T의 baseline + 현행 branch 계보 검증**이다.

## 12. Candidate Evaluation Protocol — NOT FROZEN

아래 전체 절차는 **CMP-PROPOSED / NOT LITERATURE EXPLICIT**. 실행 승인을 대신하거나 물리 모델/Freeze를 변경하는 문서가 아니다.

1. **계보부터 확인:** FZ-C→Atlas bridge와 mesh2/mesh3 비교 조건을 해결한다. 동일 physical deck·geometry definition·normalization·bias를 기록한다. Legacy 결과로 대신하지 않는다.
2. **고정 조건 표를 마련:** MEB 원점/의미, L/recess/junction/WF/doping/Qf, capacitor와 AreaFactor, model options, DC/AC/hold/write/read bias, floating node 연결, timing, extraction windows, mesh/convergence 및 failure/censoring rules를 결정한다. 현행 Freeze 변경 여부는 별도 연구 결정이다.
3. **36 nm를 각 T의 baseline으로 먼저 측정:** 233/300/340/380 K에서 같은 write pulse와 hold/read 조건을 적용한다. write 후 VSN, Q, settling과 현재 tRET endpoint를 확인한다. baseline이 실패하면 ratio의 usable 해석을 보류한다.
4. **MEB 후보의 write→hold→read 평가:** 동일 pulse의 write 성공/end VSN → direct hold waveform과 1→.8 crossing → 지정 시점의 read signal 순서다. forced 1 V test와 operation-initialized test를 구분한다. 미교차 결과는 하한으로 기록한다.
5. **절대값·상대값·진단값 연결:** 같은 T의 36 nm 기준 RT/Ion/write/read 변화와 절대값을 함께 표시한다. total leakage를 VSN 구간에서도 확인하고 Hurkx sensitivity/spatial generation/Cgd가 cell 결과를 설명하는지 검토한다.
6. **수치 guardrail 검토 후 판정:** write/read는 필수다. DC/구조 guardrail의 필요성과 근거를 먼저 정한 후 값을 선택한다. P06의 80%나 기존 95% 예시를 자동 채택하지 않는다. retention 최소 이득도 아직 미정이다.
7. **이산 집합 먼저 제시:** 각 T별 pass/fail/unknown/censored를 기록한다. UNKNOWN을 pass로 취급하지 않는다. T별 집합과 all-T 교집합을 분리하고 boundary 주변을 추가 탐색한다.
8. **범위·강건성 표현:** 검증한 점들과 미검증 gap을 표시한다. 연속 범위는 refinement와 response 검증 후에만 주장한다. statistical/aging 강건성은 해당 추가 실험이 있는 경우에만 서술한다.

최소 결과표 후보:

| MEB/T | lineage/QC | VSN,endwrite/QSN | tRET(abs,censor) | ratio vs36same T | write success/time | ΔVBL/read success | Ion/Vth/SS/DIBL | totalID/sensitivity/∫G/E@G/Cgd | verdict/reason |
|---|---|---|---|---|---|---|---|---|---|
| 후보점 | 검증 상태 | 측정 예정 | 측정 예정 | 유효 분모일 때 | 조건 미정 | 회로 조건 미정 | 추출 정의 고정 필요 | 같은 조건및단위 | NOT YET EVALUATED |

실험 전 미결정 사항은 Ccell·AreaFactor/2D width, 실제 write pulse/BL, hold floating 상태, read precharge/CBL/load/timing, tRET 초기화·censoring, 절대 τmin, DC 허용값, 공통 T 조건과 각 T 조건의 선택, boundary refinement 기준이다. 현행 조건을 바꾸기 전 기존 Freeze/bridge 근거와 호환성을 검토한다. 본문은 이 값을 임의로 채우지 않았다.

## 13. Research Novelty and Literature Boundary

평가는 제공 11편에 한정한다. NOT FOUND는 세계 최초를 뜻하지 않는다.

| 주장요소 | 분류 | 원문근거·경계 |
|---|---|---|
| MEB/gate depth와 GIDL 관계 | ALREADY DEMONSTRATED IN LITERATURE | P02 Figs.5–7, P07 Fig.3; single/dual 구조는 다름 |
| gate 구조→drain 전계 변화 | ALREADY DEMONSTRATED IN LITERATURE | P02 Figs.3–7, P06 Fig.9, P10 Figs.9–10 |
| leakage–Ion trade-off | ALREADY DEMONSTRATED IN LITERATURE | P06 Fig.16/Table1, P10 Fig.12 |
| 온도에 따른 retention 분포 변화 | ALREADY DEMONSTRATED IN LITERATURE | P08 Fig.3, P09 Fig.10 |
| BCAT 구조 변동성과 DC 성능 | ALREADY DEMONSTRATED IN LITERATURE | P07 Fig.3, P11 Tables2–4 |
| single-WF 20 nm MEB별 공간 BTBT/누설 mapping | PARTIALLY ADDRESSED | P07 geometry/DC와 P06 공간 기전 존재; CMP 분기의 상세 mapping는 추가 검증 |
| total leakage와 BTBT spatial generation 불일치의 원인 | CMP VALIDATION REQUIRED | P01/P09 다성분 누설은 선행; CMP shallow 잔여 경로 미해결 |
| MEB에 의한 leakage reduction→실제 1T1C retention 전달 | CMP VALIDATION REQUIRED | P08–P10 compact RT, P03 cell write; 동일 CMP MEB 직접 검증 없음 |
| T별 MEB retention 이득 유지/변화와 optimum 이동 | NOT FOUND IN REVIEWED 11 PAPERS | 온도와 구조 각각의 연구는 있음; 계획 4 T×MEB cell 결합 검증 필요 |
| W/R/DC 제약을 함께 고려한 single-WF MEB 유효 집합 | NOT FOUND IN REVIEWED 11 PAPERS | P06 drive constraint/P03 cell criterion/P05 score의 각 요소는 선행; CMP 결합 검증 필요 |

잠재 기여는 **같은 소자/수치 분기에서 구조–공간 generation–terminal leakage–cell 기능을 연결하고 그 전달률과 제약의 온도 의존성을 검증하는 것**이다(CMP-PROPOSED). 현재 300 K Atlas만으로 retention 증가, temperature-robust range, weak-cell yield, 양산 RC 개선은 주장할 수 없다. novelty 문장은 bridge 및 cell 검증 후 실제 관찰 범위에 맞춰 다시 작성한다. 미제공 Park 논문 및 추가 검색 없이는 전체 문헌 공백을 확정할 수 없다.

## 14. Conflicts, Unknowns, and Missing Evidence

| 종류 | 원문/프로젝트 근거 | 처리와 영향 |
|---|---|---|
| 입력 목록 불일치 | 예상 Park process 논문 없음; P05 fin height 추가 | 제공 11편만 분석; 예상 핵심 9편 완료로 표기하지 않음 |
| P03 α/voltage | Eq.2의 무차원 α와 본문의 .698 V 표현(PDF7–8) | AMBIGUOUS; 회로값 없는 threshold 재현 보류 |
| P03 waveform/결론 수치 | PDF8 Fig.12 조건과 PDF9 결론의 .67→.84/.62→.79 등 | 같은 조건으로 합치지 않음; 대표 개선율 선택 보류 |
| P04 refresh 배수 | 2.283 s 및 35×와 64 ms 기준(PDF3–4) | 정확한 배수 불일치; 숫자 보존, 합격 기준 전용 금지 |
| P05 figure numbering | §III-E의 score Fig.16/endurance Fig.17과 본문 호출 혼동(PDF7) | 실제 그림 제목/축 우선; 번호 혼동 명시 |
| P06 Ioff reduction | abstract의 43% lower와 5.95→2.54×10⁻¹⁴ A, Fig.3의 약57%(PDF1/3/4) | 42.7% remaining/57.3% reduction 계산 병기; 43% lower 채택 보류 |
| P06 depth/bias/caption | Fig.7 end depth85와 구조145; Fig.14 caption90와 plot70; 후반 Ion VD1.2 legend와 .1 axis | AMBIGUOUS; 추정 교정하지 않고 Table1 조건의 정확한 재현은 보류 |
| P06 field integral unit | PDF7 Fig.9 관련 1.29/1.51×10⁻² V/μm 표기 | 차원 모호; 물리적 전계 적분 단위로 임의 수정 금지 |
| P07 model/junction | Hurkx TAT/BTBT 문구; 30–50%와27/40/53%(PDF3–4/6) | exact deck 없이 모델/범위 확정 불가 |
| P08 tail probability | CP10⁻⁶%와 일반 CDF10⁻⁶ | 1e-8과1e-6 분리; Fig.4 온도 NR |
| P09 crossover | §II 본문110°C와 결론120°C(PDF3/6) | 근사 조건의 표현 차이; universal crossover 설정 금지 |
| P09 equation notation | Eq.8의 Et+Ei와 prose의 Et−Ei(PDF4) | AMBIGUOUS; 식을 그대로 CMP model에 구현하지 않음 |
| P10 equation sign | Eq.5 DD의 positive exponent 표기와 Part I의 negative 형태(PDF4) | 구현에 사용 시 별도 검증; 본 MD는 새 model을 구현하지 않음 |
| P11 table label/unit | Table3의 IDsat 중복/IDlin pA 표기(PDF6/본문5) | 추정 행 수정 금지; raw curve로 추가 검증 필요 |
| P11 percentage/context | Table2 IDsat SD1.88(2.84%) 등(PDF6) | 같은 mean 없는 % 재계산 보류; yield 해석 금지 |
| CMP 상태 문서 세대 | Sept22 MODEL_SCOPE/CLAIM의 Legacy47–49 nm와 Oct8 Atlas PAPER-CAL | 최신 HANDOFF/Atlas 우선; legacy 결과를 현행 증거로 승격 금지 |
| CMP branch 계보 | FZ-C exact-parent bridge OPEN | 같은 분기 QC와 parent 재현성을 분리 |
| 누락 정보 | 여러 논문의 T/mesh/convergence/SS window/full bias/circuit load NR | 재현성 한계; 없는 정보 추정 금지 |

추가 PDF 필요: **“Novel Dual Work Function Buried Channel Array Transistor Process Design for Sub-17 nm DRAM”**, Park(2024), 기존 REF02, DOI [10.1109/ACCESS.2024.3371508](https://doi.org/10.1109/ACCESS.2024.3371508). 이 DOI/매핑은 CMP REFERENCES의 목록 정보이며 원문 내용은 **NOT VERIFIED**. 전체 저자·process/RWL 평가 여부·constraint는 미제공 원문 없이 확정하지 않는다. 제공 11편의 분석은 완료했지만 예상 핵심 9편 coverage와 process/RC 논의를 완성하려면 이 원문이 필요하다.

JEDEC 원문이나 각 논문이 참조한 외부 calibration 논문의 전체 내용은 이번 입력에 없고 독립 검증하지 않았다. 외부 표준의 정확한 제품 범위와 원시험 조건을 보편 기준으로 선언하지 않는다. P09 endpoint는 직접 확인했고 P08 endpoint는 NR이라는 구분을 유지한다. 미검증 사항은 주장을 제한하는 정보 공백이다.

## 15. Decision Preparation for ChatGPT Review

### 근거가 충분한 결정 후보

같은 T/초기화/bias의 baseline을 사용하고 절대 RT와 ratio를 함께 보고한다. write 초기 충전과 hold 손실을 분리한다. .8 V endpoint와 read failure를 구분한다. terminal total leakage/Hurkx sensitivity/spatial generation을 각 이름으로 유지한다. 필수 기능과 mechanism diagnostics를 분리하고 이산 검증 집합부터 제시한다. P03/P06/P08–P10과 현재 Atlas의 불일치에 근거한 방법 제안이며 수치 동결은 아니다.

### 근거가 부족한 결정 후보

최적 MEB/연속 범위, 25% RT·95% Ion·10% W/R 한계, actual RC cap, 0.8 V actual failure, 380 K 유일 worst case, nominal 소자로 weak-tail/yield 보장, shallow residual의 정확한 성분은 현재 확정할 수 없다. 문헌 수치의 평균이나 score 가중치로 공백을 메우지 않는다.

| 경쟁 방법 | 장점 | 한계 | 검토 결정 |
|---|---|---|---|
| A same-T relative | 구조의 상대 이득 분리, baseline 추적 | 낮은 절대 성능/실패 분모를 감춤 | primary 표현에 사용하되 단독 usable 판정 금지 |
| B absolute | cell 사용 조건과 연결 | 제품/회로 요구와 τmin 필요 | 실제 W/R 조건 및 endpoint 검증 먼저 |
| C multi-constraint | 기능·성능 trade-off 명시 | threshold 선택과 측정 비용; 미검증 gap | 필수 기능 통과 후 DC 조건 필요성 결정 |
| scalar score | 한 점 선호 순위 간단 | weight/extrema 의존, hard failure 상쇄 | 선택 보조/민감도 분석에 한정 |
| Pareto+all-T intersection | trade-off와 공통 T 집합이 투명 | 불확실성/연속성 별도 검증 필요 | 후속 data 충족 후 적용 후보 |

후속 논의 우선순위는 다음이다.

1. FZ-C bridge 해결 상태 및 현행 branch 조건 확인.
2. operational write 초기화와 forced 1 V test의 역할, Ccell/2D normalization 확정.
3. read circuit/CBL/precharge/timing 및 실패 정의 선정.
4. 절대 τmin이 필요한 연구 주장인지, 상대 RT gain 보고까지 할지 결정.
5. Ion/Vth/SS/DIBL 중 hard guardrail이 필요한 항목과 허용값의 근거 논의.
6. T별 집합과 all-T 공통 집합의 보고 방식, 이산→연속 검증 절차 결정.
7. 미제공 Park 원문 확보 후 process/RC 및 novelty 경계 추가 검토.

이 문서는 후속 결정을 위한 근거 문서이며 실험 실행·물리 조건 변경·최종 판정 규칙을 승인하거나 동결하지 않는다.

## Appendix A. Complete Evidence Index

아래 색인은 이 문서의 주요 수치·방법·구조·제약·충돌을 찾기 위한 주장 색인이다. 그림의 모든 raw point를 전사한 데이터 테이블은 아니다. 쪽 열은 PDF/인쇄를 함께 적는다. LIT-EXPLICIT 결과를 design constraint로 오해하지 않도록 요약에 용도를 명시한다. CMP 제안의 출처는 해당 본문 절이며 문헌에 명시된 공식으로 표시하지 않는다.

| Paper ID | Claim/Metric | PDF Page / 인쇄 | Section | Figure/Table/Equation | Evidence Summary | Classification |
|---|---|---|---|---|---|---|
| P01 | 저전계 model mismatch |1/2892 |I |Fig. 1 |BTBT-only vs measured GIDL,a.u. |LIT-EXPLICIT |
| P01 | current integral |2/2893 |II |Eq.1 |Wq∬(GBTBT+GTAT) |LIT-EXPLICIT |
| P01 | BTBT/TAT models |2/2893 |II |Eqs.2–3 |field-driven BTBT/field-enhanced SRH |LIT-EXPLICIT |
| P01 | Fmax approximation |2–3/2893–2894 |II |Eq.5/Fig. 4 |Vdg polynomial/EOT relationship |LIT-EXPLICIT |
| P01 | TCAD geometry |3/2894 |II-B |본문 |25nmL,15nmfin,EOT1.6 nm |LIT-EXPLICIT |
| P01 | spatial generation |3/2894 |II-B |Fig. 3 |Vdg.5V,oxide 1 nm cut,cm⁻³s⁻¹ |LIT-EXPLICIT |
| P01 | peak compact BTBT |3/2894 |II |Eq.6 |W(A/B)Fmax²exp(−B/Fmax) |LIT-EXPLICIT |
| P01 | TAT/final bias correction |4–5/2895–2896 |II |Eqs.11–32/final식 |ni(T),Γ,F/Vdbdependencies |LIT-EXPLICIT |
| P01 | temperatures |5/2896 |III |Figs.5–6 |−40/25/100°Cfit |LIT-EXPLICIT |
| P01 | Kconversion |5/2896 |본문→§4F |— |+273.15=233.15/298.15/373.15 K |LIT-DERIVED |
| P02 | depth definition |2/쪽없음 |structure |Fig. 1 |MEB82/PEB57/poly25 nm |LIT-EXPLICIT |
| P02 | bias/physics/calibration |2/쪽없음 |simulation |Fig. 2/본문 |standby terminals,model options,IV fit |LIT-EXPLICIT |
| P02 | upper/lower field peaks |3/쪽없음 |results |Figs.3–4 |GIDL/GIJLregions,doping/potential |LIT-EXPLICIT |
| P02 | fixed-MEB sweep |4/쪽없음 |results |Fig. 5 |72/82/92/102 nm,MV/cm |LIT-EXPLICIT |
| P02 | fixed-PEB sweep |4/쪽없음 |results |Fig. 6 |67/57/47/37 nm,field fall/saturation |LIT-EXPLICIT |
| P02 | sequential design |4/쪽없음 |conclusion |Fig. 7/본문 |target Ion first,RWL/RCqualitative |LIT-EXPLICIT |
| P03 | geometry/bias |3/3 |2 |Tables1–2 |2DBCATdimensions,WL/BL/body |LIT-EXPLICIT |
| P03 | correlated etch |4/4 |3 |geometryfigures |θ90–92.4°,r6→0 nm |LIT-EXPLICIT |
| P03 | IV/write |5/5 |3 |Figs.6–7 |drive/initialSNdegradation |LIT-EXPLICIT |
| P03 | BOXsweep |6/6 |3 |Figs.8–10 |22/18/14/10/6 nm |LIT-EXPLICIT |
| P03 | read-sharing criterion |7–8/7–8 |4 |Eqs.1–2 |αmincircuitcondition |LIT-EXPLICIT |
| P03 | pass window |8/8 |4 |Fig. 12 |.698V,10nswrite+300mshold |LIT-EXPLICIT |
| P03 | 64/300msdistinction |7–8/7–8 |4 |본문 |standardmentionvsauthorassumption |LIT-EXPLICIT |
| P03 | VSNcases/conflict |8–9/8–9 |4/conclusion |Fig. 12/결론 |condition matching unclear |UNKNOWN |
| P04 | hardware/thermal |1–2/6–7 |II |setupfigures/본문 |ARMv8/DDR3,PID<1°Cdeviation |LIT-EXPLICIT |
| P04 | correctnessdetection |2–3/7–8 |II–III |본문/Figs.4–7 |ECC/SDC/goldenworkload |LIT-EXPLICIT |
| P04 | CPUpower trade-off |3/8 |III |Fig. 5 |12.8%/38.8%reported |LIT-EXPLICIT |
| P04 | DRAM BER/T/power |3–4/8–9 |III |Fig. 8/본문 |50/60 °C,pattern/workloaddependency |LIT-EXPLICIT |
| P04 | refresh values |3–4/8–9 |III |본문 |64 ms→2.283s,35×reported |LIT-EXPLICIT |
| P04 | refresh arithmetic |3–4/8–9 |§4D/§14 |— |35×64 ms=2.240s |LIT-DERIVED |
| P04 | error locations |4/9 |III |Table 1 |8bankcountsforbothT |LIT-EXPLICIT |
| P04 | server power |4/9 |III |본문 |31.1→24.8W,20.2% |LIT-EXPLICIT |
| P05 | geometry/calibration |2/143319 |II |Table 1/Fig. 2 |H19→1,Vth.54,100nA,co-adjusted doping |LIT-EXPLICIT |
| P05 | Ion/GIDL |3/143320 |III-A |Fig. 3 |normalized nearly constant |LIT-EXPLICIT |
| P05 | SS/DIBL |3/143320 |III-A |Fig. 4 |VD.05/1,SS+약 10,DIBL+19% |LIT-EXPLICIT |
| P05 | GIJL/Efield |3–4/143320–143321 |III-B |Figs.5–6/8 |−12Vdiagnostic,87/53/61%results |LIT-EXPLICIT |
| P05 | PGE |4–5/143321–143322 |III-C |Figs.7/9 |.346→.447V,AWL/FPWLcomparisons |LIT-EXPLICIT |
| P05 | capacitiveexplanation |5/143322 |III-C |Figs.10–11 |φchnetwork,notCgd |LIT-EXPLICIT |
| P05 | 1RD |6–7/143323–143324 |III-D |Figs.12–15/17 |8 fF/60 ns/10pulse,92%reported |LIT-EXPLICIT |
| P05 | score/12 nm |7/143324 |III-E |Fig. 16 |min–maxfour metric sum,single optimum |LIT-EXPLICIT |
| P06 | geometry/depthmeaning |2–3/2–3 |2 |Figs.1–2 |Lin/film/recess/gatedepthdistinct |LIT-EXPLICIT |
| P06 | Ioffbaseline |3–4/3–4 |3 |Fig. 3/본문 |5.95→2.54×10⁻¹⁴A |LIT-EXPLICIT |
| P06 | reductioncalculation |3–4/3–4 |§4D |— |2.54/5.95=.427,1−ratio=.573 |LIT-DERIVED |
| P06 | gm/SS/Vth/DIBL |5–6/5–6 |3 |Figs.5–6 |auxiliaryDC metrics |LIT-EXPLICIT |
| P06 | potential/field/generation |7/7 |3 |Figs.8–9 |width/peakregion,oxide 1 nm cut |LIT-EXPLICIT |
| P06 | film/gatedepthsensitivity |8–11/8–11 |3 |Figs.10–15 |plateau/trade-off,notMEBfeasibility |LIT-EXPLICIT |
| P06 | Ion80%constraint |11–12/11–12 |3 |Fig. 16/Table 1 |same gate depthasymmetric comparator |LIT-EXPLICIT |
| P06 | selected numeric results |12/12 |3 |Table 1 |Lin5/5.5/5.75,film50/60/70,Ioff33–38% |LIT-EXPLICIT |
| P07 | singleWFgeometry |2–4/2–4 |2 |Figs.1–2/Table 1 |20 nm/4.8 eV/DBCAT36 nm |LIT-EXPLICIT |
| P07 | modelambiguity |4/4 |2 |본문 |Hurkx TAT/BTBT wording |UNKNOWN |
| P07 | nominal DC |5–6/5–6 |3 |Fig. 3/본문 |.656V,76 mV/dec,3.4e10,23.6 mV/V |LIT-EXPLICIT |
| P07 | variation/benchmark |5–6/5–6 |3 |Fig. 3/본문 |structuralsweep/literatureplausibility |LIT-EXPLICIT |
| P08 | trapmodel |2/39 |II |Eqs.1–6 |current/trapcount/location/energy |LIT-EXPLICIT |
| P08 | bias/IV |2–3/39–40 |II–III |Figs.2–4 |VD1.5/VG−.2/VBB−.8 |LIT-EXPLICIT |
| P08 | RT/Tparameters |3/40 |III |Fig. 3 |10 fF/298,328,358 K/Et/Nit |LIT-EXPLICIT |
| P08 | tail RT/WF |3/40 |III |Fig. 4e |.29→.36/.42/.44s,24/45/51% |LIT-EXPLICIT |
| P08 | CP unit conversion |3/40 |§4D |Fig. 4e |10⁻⁶%=10⁻⁸probability |LIT-DERIVED |
| P09 | geometry/calibration |2/4463 |II |TableI/Fig. 1 |dualmetal both WF4.54,T300–375 |LIT-EXPLICIT |
| P09 | terminals/physics |3/4464 |II |TableII/Figs.2–3 |leakagepaths/signs/SRH,bias isolation |LIT-EXPLICIT |
| P09 | Ea/crossover |3/4464 |II |Fig. 4 |.6/1.3 eV,약 110 °C |LIT-EXPLICIT |
| P09 | compacttrapmodel |4–5/4465–4466 |III |Eqs.3–15/Figs.5–8 |Et/Xi/E/T,single-trap aA |LIT-EXPLICIT |
| P09 | RT definition |5–6/4466–4467 |IV |본문/Fig. 9 |10 fF,1→.8assumed loss,variation excluded |LIT-EXPLICIT |
| P09 | MC/trapparameters |5–6/4466–4467 |IV |Fig. 9/본문 |5e7/mean3/Nit5e10/Et−.15±.025 |LIT-EXPLICIT |
| P09 | T/head/tail Ea |6/4467 |IV |Fig. 10 |300–425 K,CDFhead/center/tail,Ea |LIT-EXPLICIT |
| P10 | agingmeasurement |2/4470 |II |Fig. 1 |298/343/373 K,CP/leakage Ea약 .65 |LIT-EXPLICIT |
| P10 | generatedtraplocation |3/4471 |II |Figs.2–4 |saddle-fin thin oxide |LIT-EXPLICIT |
| P10 | spectrum/agingCDF |4/4472 |III |Figs.5–6 |dual Gaussian,ΔNit1/5/10,tail20%result |LIT-EXPLICIT |
| P10 | compact updates |4–5/4472–4473 |III |Eqs.1–5/Figs.7–8 |fresh+aging,ΔA/ΔE |LIT-EXPLICIT |
| P10 | geometry/WFoptimization |5/4473 |IV |Figs.9–10 |WF4.04–5.04,metal20–50 nm,T300 |LIT-EXPLICIT |
| P10 | RDF |6/4474 |IV |Fig. 11 |sIFM/−6σtaildegradationresult |LIT-EXPLICIT |
| P10 | two objectives |6/4474 |IV |Fig. 12 |CDF10⁻⁶ΔRTtailvsΔIdsat |LIT-EXPLICIT |
| P10 | fresh/aged comparison |6/4474 |IV |Figs.13–14 |topWF4.54vs4.1,relativeagingdifference |LIT-EXPLICIT |
| P11 | surfacevariation |3–4/2–3 |2 |Eq.1/Figs.2–6 |ACVF/8surfaces/random+systematic |LIT-EXPLICIT |
| P11 | geometry/calibration |5/4 |2 |Table 1/Fig. 7 |20 nm/36buried/150samples,IVVD.5 |LIT-EXPLICIT |
| P11 | mean/SDmetrics |6–7/5–6 |3 |Tables2–4/Figs.8–10 |VT/ID/Ioff/SS/DIBLdistributions |LIT-EXPLICIT |
| P11 | roughness SD results |6/5 |3 |Table 2 |DIBL1.04→16.69,Ioff.02→.17SD |LIT-EXPLICIT |
| P11 | tableambiguity |6/5 |3 |Table 3 |duplicate label/unit conflict |UNKNOWN |
| CMP | livecurrent state |— |§0–1 |HANDOFF/Atlas |PAPER-CAL/15points/bridgeOPEN |CMP-EXISTING |
| CMP | metricselection |— |§11 |frameworktable |primary1/W-R2/DCconditional/diagnostic4 |CMP-PROPOSED |
| CMP | retentionintegration |— |§7 |proposedequations |chargeconservation,quasi-static conditions |CMP-PROPOSED |
| CMP | T/rangeformulas |— |§8/10/12 |A/B/C/setintersection |same-T 36,absolute/multiconstraint,discrete set |CMP-PROPOSED |
| CMP | noveltyboundary |— |§13 |claimmatrix |reviewed 11 only,validation required |PAPER-INFERRED |

## Appendix B. Bibliography

### P01

Chetan Kumar Dabhi; Ananda S. Roy; Yogesh Singh Chauhan. **Compact Modeling of Temperature-Dependent Gate-Induced Drain Leakage Including Low-Field Effects**. IEEE Transactions on Electron Devices 66(7), 2892–2897, 2019. DOI: [10.1109/TED.2019.2918332](https://doi.org/10.1109/TED.2019.2918332).

원본: `Compact_Modeling_of_Temperature-Dependent_Gate-Induced_Drain_Leakage_Including_Low-Field_Effects.pdf`. PDF 6쪽; 인쇄 쪽: 2892–2897. 기존 CMP ID: —.

### P02

SeKyoung Jang; SoYoung Kim. **Impact of Metal and Poly Gate Thickness on GIDL in DRAM Dual Work-Function Structures**. International Conference on Electronics, Information, and Communication (ICEIC), 2026. DOI: [10.1109/ICEIC69189.2026.11386251](https://doi.org/10.1109/ICEIC69189.2026.11386251).

원본: `Impact_of_Metal_and_Poly_Gate_Thickness_on_GIDL_in_DRAM_Dual_Work-Function_Structures.pdf`. PDF 5쪽; 인쇄 쪽: 별도 인쇄 쪽번호 없음. 기존 CMP ID: REF03.

### P03

Yeongmyeong Cho; Gyu-Beom Kim; Myung-Hyun Baek. **Impact of Non-Ideal Wordline Etch Slopes on Read/Write Degradation in BCAT-Based DRAM**. Electronics 15(6), 1152, 2026. DOI: [10.3390/electronics15061152](https://doi.org/10.3390/electronics15061152).

원본: `Impact_of_Non-Ideal_Wordline_E.pdf`. PDF 11쪽; 인쇄 쪽: 본문 1–10; PDF 11은 이용조건. 기존 CMP ID: REF09.

### P04

Konstantinos Tovletoglou; Lev Mukhanov; Georgios Karakonstantis; Athanasios Chatzidimitriou; George Papadimitriou; Manolis Kaliorakis; Dimitris Gizopoulos; Zacharias Hadjilambrou; Yiannakis Sazeides; Alejandro Lampropulos; Shridhar Das; Phong Vo. **Measuring and Exploiting Guardbands of Server-Grade ARMv8 CPU Cores and DRAMs**. 48th Annual IEEE/IFIP International Conference on Dependable Systems and Networks Workshops (DSN-W), 6–9, 2018. DOI: [10.1109/DSN-W.2018.00013](https://doi.org/10.1109/DSN-W.2018.00013).

원본: `Measuring_and_Exploiting_Guardbands_of_Server-Grade_ARMv8_CPU_Cores_and_DRAMs.pdf`. PDF 4쪽; 인쇄 쪽: 6–9. 기존 CMP ID: —.

### P05

Damin Kim; Min-Woo Kwon. **Optimization of Fin Height in Saddle-Fin BCAT Structured DRAMs**. IEEE Access 14, 143318–143325, 2026. DOI: [10.1109/ACCESS.2026.3733420](https://doi.org/10.1109/ACCESS.2026.3733420).

원본: `Optimization_of_Fin_Height_in_Saddle-Fin_BCAT_Structured_DRAMs.pdf`. PDF 8쪽; 인쇄 쪽: 143318–143325. 기존 CMP ID: —.

### P06

Jin-sung Lee; Jin-hyo Park; Geon Kim; Hyun Duck Choi; Myoung Jin Lee. **Partial Isolation Type Buried Channel Array Transistor (Pi-BCAT) for a Sub-20 nm DRAM Cell Transistor**. Electronics 9, 1908, 2020. DOI: [10.3390/electronics9111908](https://doi.org/10.3390/electronics9111908).

원본: `Partial_Isolation_Type_Buried_.pdf`. PDF 15쪽; 인쇄 쪽: 본문 1–14; PDF 15는 이용조건. 기존 CMP ID: REF13.

### P07

Minjae Sun; Hyoung Won Baac; Changhwan Shin. **Simulation Study: The Impact of Structural Variations on the Characteristics of a Buried-Channel-Array Transistor (BCAT) in DRAM**. Micromachines 13(9), 1476, 2022. DOI: [10.3390/mi13091476](https://doi.org/10.3390/mi13091476).

원본: `Simulation_Study_The_Impact_o.pdf`. PDF 9쪽; 인쇄 쪽: 본문 1–8; PDF 9는 이용조건. 기존 CMP ID: REF01.

### P08

Kyoung Yeon Kim; Kyung Kyu Min; Byung-Gook Park. **Trap-Induced Data-Retention-Time Degradation of DRAM and Improvement Using Dual Work-Function Metal Gate**. IEEE Electron Device Letters 42(1), 38–41, 2021 (온라인 2020). DOI: [10.1109/LED.2020.3037640](https://doi.org/10.1109/LED.2020.3037640).

원본: `Trap-Induced_Data-Retention-Time_Degradation_of_DRAM_and_Improvement_Using_Dual_Work-Function_Metal_Gate.pdf`. PDF 4쪽; 인쇄 쪽: 38–41. 기존 CMP ID: REF05.

### P09

Yong Liu; Da Wang; Pengpeng Ren; Jie Li; Zheng Qiao; Maokun Wu; Yichen Wen; Longda Zhou; Zixuan Sun; Zirui Wang; Qinghua Han; Blacksmith Wu; Kanyu Cao; Runsheng Wang; Zhigang Ji; Ru Huang. **Understanding Retention Time Distribution in Buried-Channel-Array-Transistors (BCAT) Under Sub-20-nm DRAM Node—Part I: Defect-Based Statistical Compact Model**. IEEE Transactions on Electron Devices 71(8), 4462–4468, 2024. DOI: [10.1109/TED.2024.3409510](https://doi.org/10.1109/TED.2024.3409510).

원본: `Understanding_Retention_Time_Distribution_in_Buried-Channel-Array-Transistors_BCAT_Under_Sub-20-nm_DRAM_NodePart_I_Defect-Based_Statistical_Compact_Model.pdf`. PDF 7쪽; 인쇄 쪽: 4462–4468. 기존 CMP ID: REF06.

### P10

Yong Liu; Da Wang; Pengpeng Ren; Jie Li; Zheng Qiao; Maokun Wu; Yichen Wen; Longda Zhou; Zixuan Sun; Zirui Wang; Qinghua Han; Blacksmith Wu; Kanyu Cao; Runsheng Wang; Zhigang Ji; Ru Huang. **Understanding Retention Time Distribution in Buried-Channel-Array-Transistors (BCAT) Under Sub-20-nm DRAM Node—Part II: PBTI Aging and Optimization**. IEEE Transactions on Electron Devices 71(8), 4469–4475, 2024. DOI: [10.1109/TED.2024.3409512](https://doi.org/10.1109/TED.2024.3409512).

원본: `Understanding_Retention_Time_Distribution_in_Buried-Channel-Array-Transistors_BCAT_Under_Sub-20-nm_DRAM_NodePart_II_PBTI_Aging_and_Optimization.pdf`. PDF 7쪽; 인쇄 쪽: 4469–4475. 기존 CMP ID: REF07.

### P11

Seokchan Yoon; Jaehyuk Lim; Changhwan Shin. **Variation-aware analysis of buried-channel-array transistors (BCATs) in scaled DRAM: insights from 3D quasi-atomistic simulations**. Semiconductor Science and Technology 40, 015010, 2025 (온라인 2024). DOI: [10.1088/1361-6641/ad98bb](https://doi.org/10.1088/1361-6641/ad98bb).

원본: `Yoon_2025_Semicond._Sci._Technol._40_015010.pdf`. PDF 9쪽; 인쇄 쪽: PDF 1 표지; PDF 2–9 = 본문 1–8. 기존 CMP ID: REF10.

