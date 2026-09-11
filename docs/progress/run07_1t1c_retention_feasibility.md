# CMP Run 7 — 1T1C Retention Feasibility: Interim Closure

Date: 2026-09-11  
Scope: **B0-v1 methodology feasibility** only. This document does **not** freeze a production baseline or final retention time.

## 1. Executive status

Current Run 7 has demonstrated the following chain at feasibility level:

```text
Write feasibility
→ floating-SN 100 ns short Hold
→ independent D0/D1 charge-sharing Read
```

This supports the scoped statement:

> **A first-pass 1T1C retention-operation feasibility validation was completed for B0-v1.**

The precise meaning is:

- D1 write behavior is reproducibly generated.
- After write-pulse termination and switching settling, the floating storage node remains numerically stable over a 100 ns short-hold window in the currently processed subset.
- Independent charge-sharing read tests distinguish D0 and D1 with opposite BL signal directions.

It does **not** yet mean:

- integrated `Write → Hold → Read` has been completed in a single transient,
- a physical retention time has been extracted,
- the final standby bias or final write condition has been frozen,
- a Liu-compatible `1.0 V → 0.8 V` retention time has been measured.

Documentation map:

- methodology traceability: [`../methodology/run07_methodology_traceability.md`](../methodology/run07_methodology_traceability.md)
- feedback-level checkpoint: [`../evidence/feedback_retention_operation_checkpoint_20260911.md`](../evidence/feedback_retention_operation_checkpoint_20260911.md)
- write evidence: [`../evidence/run07_write_screen_20260911.md`](../evidence/run07_write_screen_20260911.md)
- hold evidence: [`../evidence/run07_hold100_partial_20260911.md`](../evidence/run07_hold100_partial_20260911.md)
- read evidence: [`../evidence/run07_read_window_20260911.md`](../evidence/run07_read_window_20260911.md)
- evidence manifest: [`../evidence/run07_retention_manifest.md`](../evidence/run07_retention_manifest.md)

## 2. Fixed feasibility scope

```text
B0 MEB depth = 36 nm
T            = 300 K
Mesh_Code    = 1 for current write/hold/read feasibility work
Ccell        = 10 fF
Physics      = established CMP NonlocalPath chain
```

Run 7 remains a B0 protocol-definition stage. MEB-dependent cell comparison belongs to downstream Run 8 after the protocol is frozen.

## 3. R7B — Write screen

For the quantified nominal-width candidate block:

```text
AreaFactor = 0.017
VBL_WRITE  = 1.2 V
VWL_ON     = 1.5 / 2.0 / 2.5 / 3.0 V
VWL_HOLD   = -0.7 V
Twrite     = 100 / 200 / 300 ns
```

| node | VWL_ON [V] | Twrite [ns] | final VSN [V] |
|---:|---:|---:|---:|
| 182 | 1.5 | 100 | 0.157485 |
| 183 | 2.0 | 100 | 0.428389 |
| 184 | 2.5 | 100 | 0.675346 |
| 185 | 3.0 | 100 | 0.866426 |
| 194 | 1.5 | 200 | 0.190966 |
| 195 | 2.0 | 200 | 0.469623 |
| 196 | 2.5 | 200 | 0.723916 |
| 197 | 3.0 | 200 | 0.919497 |
| 206 | 1.5 | 300 | 0.209947 |
| 207 | 2.0 | 300 | 0.492115 |
| 208 | 2.5 | 300 | 0.750794 |
| 209 | 3.0 | 300 | **0.948118** |

Within the screened range, `VSN` increases monotonically with both `VWL_ON` and `Twrite`.

Current strongest screened condition:

```text
AreaFactor = 0.017
VWL_ON     = 3.0 V
Twrite     = 300 ns
VSN_final  = 0.948118 V
```

This is a **preliminary D1 candidate**, not a final write-condition freeze. The current screen has not reached 1.0 V.

Processed data:

- `data/run07/processed/write_screen_af0017.csv`

## 4. R7C — Floating storage-node Hold

Current short-hold branch:

```text
BL after write = 0 V
WL_HOLD        = -0.7 V
substrate      = 0 V
SN             = floating after Unset(sn)
Thold          = 100 ns
```

The hold metric is intentionally started after WL/BL falling-edge settling, near `Twrite + 2 ns`, so switching transient and genuine hold behavior are not conflated.

### Processed subset

| node | AF | VWL_ON [V] | Twrite [ns] | VSN hold-start [V] | VSN +100 ns [V] | Delta VSN [V] |
|---:|---:|---:|---:|---:|---:|---:|
| 179 | 0.011 | 2.0 | 100 | 0.400957143 | 0.400957143 | 5.860e-13 |
| 191 | 0.011 | 2.0 | 200 | 0.444792564 | 0.444792564 | 6.500e-13 |
| 203 | 0.011 | 2.0 | 300 | 0.468481043 | 0.468481043 | 6.470e-13 |
| 183 | 0.017 | 2.0 | 100 | 0.428387852 | 0.428387852 | 9.720e-13 |
| 194 | 0.017 | 1.5 | 200 | 0.190978612 | 0.190978612 | 5.970e-13 |
| 195 | 0.017 | 2.0 | 200 | 0.469644635 | 0.469644635 | 1.054e-12 |

Observed changes are only on the order of `1e-13 ~ 1e-12 V`. They are treated as **numerical-floor-level changes**, not as physically resolved retention decay.

Therefore this checkpoint establishes:

- floating-SN implementation: **PASS at feasibility level**
- 100 ns short-hold stability: **PASS for processed subset**
- retention time: **not extracted**

Processed data:

- `data/run07/processed/hold100_partial.csv`

The full 36-case Hold matrix is not claimed complete in this document until all raw outputs are processed.

## 5. R7E — Independent D0/D1 Read window

Current independent read test:

```text
AreaFactor = 0.017
Ccell      = 10 fF
CBL        = 45 fF
VBL_init   = 0.5 V
WL_OFF     = -0.7 V
WL_READ    = 3.0 V
Tread      = 10 ns
D0 VSN     = 0 V
D1 VSN     = 0.9481 V
```

D1 initial VSN maps to the strongest quantified write-screen state above.

| state | VSN init [V] | VBL init [V] | VSN final [V] | VBL final [V] | Delta VSN | Delta VBL | capacitor-charge error |
|---|---:|---:|---:|---:|---:|---:|---:|
| D0 (n136) | 0.000000 | 0.500000 | 0.324409 | 0.427884 | +324.41 mV | **-72.12 mV** | -0.0051% |
| D1 (n138) | 0.948100 | 0.500000 | 0.810658 | 0.530553 | -137.44 mV | **+30.55 mV** | +0.0014% |

Final D0/D1 BL separation:

```text
0.530553 - 0.427884 = 0.102669 V = 102.67 mV
```

Interpretation:

- D0 produces a negative BL shift.
- D1 produces a positive BL shift.
- Opposite signal directions provide an independent charge-sharing discrimination check.
- Capacitor-charge balance error below 0.01% supports a charge-redistribution interpretation.

This is **independent read feasibility**, not yet `Read-after-Hold`.

Processed data:

- `data/run07/processed/read_window.csv`

## 6. Method / literature mapping

The current methodology is deliberately split into distinct metrics rather than forcing unlike definitions into one number.

### Direct floating transient

```text
Write → SN floating → VSN(t)
```

Current result: 100 ns short-hold stability only.

### Synopsys-compatible secondary metric

The audited `Memory/SF_DRAM` example provides the methodology precedent:

```text
T_RET,5% = integral [ Ccell / |I_SN(VSN)| ] dVSN
```

over an approximately 5% storage-voltage window from `0.95*Vmax` to `Vmax`.

This metric has **not yet been executed for CMP**.

### Liu-compatible literature metric

Reserved name:

```text
t_1.0→0.8
```

Only report it if the CMP written state genuinely begins near 1.0 V. The current strongest screen is 0.948118 V, so no Liu-compatible retention time is claimed.

### Read-derived usability

Readability will eventually be checked after Hold using the CMP D0/D1 charge-sharing window. Literature thresholds such as Cho et al.'s read-derived value are retained as references, not imported as automatic CMP pass/fail thresholds.

Full source-to-method mapping is in `docs/methodology/run07_methodology_traceability.md`.

## 7. Physics continuity and bias boundary

Main R7 physics remains the established CMP chain:

```text
Fermi
EffectiveIntrinsicDensity(OldSlotboom)
Mobility(DopingDep HighFieldSaturation Enormal)
SRH(DopingDep)
Auger
Band2Band(Model=NonlocalPath)
```

The Synopsys example is used as a topology/methodology precedent only; its example-specific leakage physics is not copied into the CMP mainline.

The current short-hold bias:

```text
WL = -0.7 V
BL = 0 V
substrate = 0 V
SN = floating
```

is a **CMP-adapted feasibility bias** and must not be described as a literature-standard or production standby condition.

## 8. Presentation-safe wording

Allowed at this checkpoint:

> **B0 1T1C MixedMode에서 Write 후 floating storage node의 100 ns 단기 유지 안정성을 확인했고, 별도 D0/D1 read test에서 약 102.7 mV의 bitline separation을 확보하여 1차 retention-operation feasibility를 검증하였다.**

Do not claim yet:

- `Retention time = X`
- final retention validation complete
- full `Write → Hold → Read` validation complete
- production/calibrated retention behavior
- Liu-compatible `1.0 → 0.8 V` retention time

## 9. Next required closure

1. choose one representative written D1 state;
2. execute integrated `Write → Hold → Read` in one sequence;
3. extend Hold time beyond 100 ns;
4. track both `VSN(t)` and post-hold `DeltaVBL`;
5. execute the Synopsys-compatible `T_RET,5%` leakage integration;
6. later check Mesh1 vs Mesh3 and NonlocalPath ON/OFF attribution before full R7 close-out.

## 10. README integration state

**Do not update the main README yet.**

This checkpoint is intentionally staged in Run 7 progress/evidence and linked from `TASK_HUB` / `FEEDBACK_LOG`. Main README integration is deferred until the principal first-presentation feedback set is synthesized consistently.
