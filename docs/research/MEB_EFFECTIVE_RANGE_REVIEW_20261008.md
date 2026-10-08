# CMP MEB 유효 범위 — 문헌 MD 심층 검토 보고서 (2026-10-08)

> 상태: **INDEPENDENT REVIEW / NOT FROZEN**. 검토 대상: 사용자가 제공한 11편 통합 MD v1.0. 원문 PDF 11개 자체는 이번 대화에서 제공되지 않아, 모든 수치·그림의 독립 원문 대조는 수행하지 못했다. 일부 공개 출판사/대학 페이지로 서지·방법을 교차 확인했다. 본 문서는 새 연구 결정이나 최종 MEB 판정이 아니다.

## 1. 검토 결론

- 문헌별 `EXPLICIT DESIGN CONSTRAINT` / `REPORTED RESULT` / `EXTERNAL STANDARD`의 분리는 적절하다. 숫자의 출처와 재사용 조건이 명확하다.
- Retention `VSN:1.0→0.8 V`는 P09(Liu Part I)의 원문 확인을 보고한 MD에 근거한 **평가 종료 정의**이다. 실제 CMP Read Failure와는 별도다.
- 명시적 설계 제약의 예는 P06(Pi-BCAT: Ion=80% contour), P03(10 ns write+300 ms hold 이후 0.698 V read 판정), P05(4개 지표 min–max 균등 합산; **선정 규칙**이지 hard threshold 아님)이다.
- 온도별 MEB 최적화의 공통 수치 규격은 11편에서 확인되지 않았다. RT 25%, Ion 95%, W/R 10% 등의 예시는 **UNDECIDED**.
- 핵심 평가지표는 `Retention (1.0→0.8 V)` 1군; 필수 셀 기능 `Write`/`Read` 2군; `Ion/DC` 조건부 제약 1군; 해석용 누설·Hurkx sensitivity·Cgd·공간 E/BTBT 4군으로 나누는 방안이 타당하다. 그룹 수는 CMP에서의 구성 제안이지 일반 학술 규칙이 아니다.

## 2. 별도 확인이 필요한 과학적 위험

1. **GIDL 시험과 실제 Hold의 바이어스 불일치:** 현행 Atlas의 `Vd=1.2,Vg=-0.7`에서 얻은 전류를 1T1C floating storage node의 시변 Hold 누설전류로 바로 사용할 수 없다. P09의 leakage 성분 분해와 여러 VSN에서의 net loss-current 검증을 참조할 것.
2. **초기 Write 오염:** 얕거나 깊은 MEB에서 `VSN≈1.0 V` 도달 여부/소요 시간이 달라질 수 있다. forced-1.0-V 비교 Retention은 isolation test이고, operational Write→Hold→Read success를 대체하지 않는다. P03이 이 논리의 직접 선례.
3. **Read 판정:** 0.8 V는 논문/프로젝트 분석 endpoint이고 실제 read fail threshold로 보장되지 않는다. 같은 CBL, precharge, sensing time, ΔVBL 정의가 필수.
4. **비교 범위와 계보:** 새 300K Atlas는 내부 QC 검증되었으나 exact FZ-C parent bridge는 OPEN. Legacy NonlocalPath 1T1C나 3D 기하 RWL proxy의 절대값을 섞지 말 것.
5. **온도 Worst-case:** 동일 온도 36 nm에 대한 retention 비율과 각 온도의 절대 Retention·Write/Read success를 모두 기록. 상대 이득만으로 기능적 합격 판단하지 말 것.
6. **MEB 범위의 연속성:** 실측 MEB/T 이산 통과점 집합과 연속 nm 구간, 공정 편차에 의한 강건 공차 범위는 서로 다르다. 경계 추가점과 오차 확인 전에 연속 구간/양산 강건성을 주장하지 말 것.
7. **누설 성분:** total terminal drain current, signed Hurkx ON−OFF sensitivity, spatial q∫BTBT는 동일하지 않으며 GIDL 스트레스 결과만으로 Retention 개선을 결론내지 말 것.
8. **Model accuracy:** long-time 1.0→0.8 V 직접 transient 계산이 부담되면 I(VSN) 적분을 사용하되 Ceff, AreaFactor/current normalization, leakage sign, quasistatic 전제 및 selected-point transient의 교차 검증을 조건으로 할 것. short-window 선형 외삽 금지.

## 3. 원본 MD 품질 검토 및 공개 안전

- 표준화된 individual paper record P01–P11 **11개**와 통합 matrix, evidence index, bibliography 구조 확인.
- 원본 MD는 핵심 원문 **Park et al., 2024 (REF02)**가 제외됐음을 명시한다. 사용자 표현인 '핵심 9편 확보'와 실제 입력 분석 범위는 다르다. P04 서버급 ARM/DDR3 Guardband는 방법론 참고자료이며 BCAT TCAD 지표 빈도나 근거 비중을 과대평가하지 말 것.
- `§8`의 B/C feasible-set LaTeX에서 `m pass`, `m acceptable`로 깨진 문자열 발견. 공개용 준비 사본에서 연산자 이름으로 복구했으며 수치/판정 의미 변경은 없다.
- `§0`의 Windows `C:/Users/...` 사용자 경로는 공개 GitHub에 그대로 올리지 말 것. 준비 사본에서 상대 원본 목록과 SHA-256은 유지하고 해당 경로만 제거.
- 원문 PDF SHA-256 11개는 **Codex가 보고한 값**이다. PDF 파일 11개가 이번 대화에 없으므로 독립 재해시 검증으로 오해하지 말 것.
- MD에는 Figure/Table 충돌을 `AMBIGUOUS`로 적은 부분들이 있다(P03 read α 단위, P06 Ioff 감소율, P09 crossover, P10 식의 부호, P11 Table3). 임의 수정하지 말고 원문을 재검증할 것.

## 4. 프로토콜 협의에서 우선할 결정

| 우선 | 항목 | 현재 상태 | 근거/메모 |
|---|---|---|---|
| 1 | Retention endpoint 1.0→0.8 V | 기존 CMP 정의 유지 | P09 (§7), read failure와 별개 |
| 2 | Retention의 실제 계산방법 | 미정 | direct transient vs I(VSN) integral/censoring/mesh |
| 3 | Write 초기화 및 timing | 미정 | same forced initial vs operational end-write 분리 |
| 4 | Read circuit/판정 | 미정 | charge sharing, CBL, BL precharge, ΔVBL, sensing window |
| 5 | 비교 기준 | 동일 온도 36 nm를 우선 후보 | 36nm ratio 단독 합격 금지 |
| 6 | Ion/SS/DIBL/DC hard constraints | 수치 미정 | manuscript risk and power/operation requirements needed |
| 7 | RWL proxy status | qualitative penalty | 물리적 RWL/RC cap 아님 |
| 8 | 범위 합성 | T별 이산 feasible points→공통 집합 | 연속 보증·공정 수율·aging은 추가 검증 필요 |
| 9 | FZ-C exact parent bridge | OPEN | current GitHub HANDOFF 선결 이슈 |

## 5. 원문 보강 순서

1. **Park et al. 2024, REF02:** 실제 제조 DWF-BCAT에서 Word-line 저항, 누설, Write 성능과 공정 trade-off 확인. IEEE Access, DOI `10.1109/ACCESS.2024.3371508`.
2. **P09 원문:** Retention endpoint와 loss integration을 저자가 실제 어떻게 정의/계산했는지, 실제 SN Read Fail이 아닌 분석 가정이라는 표현 확인.
3. **P03 원문:** 0.698 V와 α 무차원 정의의 단위 충돌, BL/C_SN 조건, write/hold 표현과 결론 차이.
4. **P05 원문:** equal weights, min–max sample bounds, score sensitivity, compensation of body doping.

## 6. GitHub 보관 경로 / 변경 통제

- 공개 저장소: `minhosong-mse/CMP`.
- GitHub 저장 경로: `docs/research/MEB_EFFECTIVE_RANGE_LITERATURE_REFERENCE.md`.
- 원본 입력 MD는 불변으로 보존하고, **GitHub 게시 사본**에서는 §0의 개인 로컬 경로와 §8의 렌더 오류만 수정하는 최소 편집을 제안한다.
- 본 리뷰는 별도 문서로 보관할 수 있다: `docs/research/MEB_EFFECTIVE_RANGE_REVIEW_20261008.md`.
- 기존 `CMP_LITERATURE_MASTER`, `DECISIONS`, `RUN_SHEET`, `HANDOFF`, `README`, 코드/결과 파일을 수정하거나 새로운 허용 기준을 Freeze하지 말 것.
- 2026-10-08 사용자 승인에 따라 이 문서를 문헌 원본과 함께 GitHub에 보관한다. 본 문서는 수치 제약 또는 연구 Freeze를 확정하지 않는다.
