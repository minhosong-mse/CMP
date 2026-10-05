# C7_4 Final-Freeze Validation — CLOSED

> **Status:** PASS / CLOSED  
> **Date:** 2026-10-05  
> **Frozen baseline:** `B0-2D-PAPER-CAL = C7_4 / B_QF_HALF`

## 1. Frozen candidate

- GateCouplingScale = 2.300
- GateDepthBoost = 25 nm
- Qf_Int = 2.55e12 cm^-2
- MEB / GateTop = 36 nm
- T = 300 K

No additional C8 calibration DOE is permitted after this checkpoint.

## 2. FZ-A — solver-path consistency

| Metric | Original C7_4 | Rescue-style | Change |
|---|---:|---:|---:|
| Vth @0.05 | 0.682477 | **0.682485** | **+0.008 mV** |
| SSquick | 76.4115 | **76.3458** | **-0.0657** |
| Id@Vg2 | 9.5541e-5 | **9.2977e-5** | **-2.68%** |

Decision: Vth / SS consistency PASS; high-Vg current ~2–3% solver sensitivity recorded.

## 3. FZ-B — DC mesh convergence

| Metric | Mesh0 | Mesh1 | Change |
|---|---:|---:|---:|
| Vth | 0.655709 | **0.655698** | **-0.011 mV** |
| SSquick | 75.8267 | **75.8273** | **+0.0006** |
| Id@Vg2 | 6.62076e-4 | **6.62669e-4** | **+0.0896%** |
| Ion/Ioff 2/0 | 2.4922e10 | **2.5444e10** | **+2.10%** |

**FZ-B: PASS / CLOSED.**

## 4. FZ-C — GIDL / BTBT / local-E convergence

| Metric | Mesh1 | Mesh2 | Mesh1→2 |
|---|---:|---:|---:|
| GIDL | 5.8010e-13 | **5.8256e-13** | **+0.424%** |
| BTBTmax | 7.2656e23 | **7.2635e23** | **-0.029%** |
| E@BTBT | 1.1232e6 | **1.1423e6** | **+1.69%** |
| Xhot | 0.034570 um | **0.034863 um** | **+0.293 nm** |
| Yhot | 0.252174 um | **0.252174 um** | **0 nm** |
| global Emax | 1.19e7 | **2.30e7** | **+93%** |

Decision: GIDL / BTBT / hotspot-local E / hotspot location PASS. Global point Emax is a secondary interface/corner-sensitive diagnostic.

## 5. Official freeze

`B0-2D-PAPER-CAL = C7_4 / B_QF_HALF`

Reference under the standardized final solver:

- Vth @0.05 V ≈ 0.682485 V
- Vth @1.20 V ≈ 0.65570 V
- SSquick @1.20 ≈ 75.827 mV/dec
- DIBL 0.05→1.20 ≈ 23.29 mV/V

## 6. Frozen numerical policy

- DC broad sweep: MeshLevel 0
- GIDL broad sweep: MeshLevel 1
- selected mechanism / final evidence: MeshLevel 2 confirmation
- Rescue V2: reference/fallback solver
- global point Emax: not a primary mechanism metric

## 7. Handoff

Next: one-point runtime-equivalence benchmark, then calibrated MEB 31/36/41 revalidation.

→ [Production revalidation & runtime plan](b0_2d_production_revalidation_plan.md)