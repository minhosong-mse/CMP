# B0-2D-PAPER-CAL — Production Revalidation & Runtime Plan

> **Status:** Next execution stage  
> **Baseline:** `B0-2D-PAPER-CAL = C7_4 / B_QF_HALF`  
> **Calibration knobs:** frozen; no retuning

## 1. Runtime principle

Final validation intentionally used conservative Rescue-style continuation and extra mesh levels. Those settings are suitable for close-out but too expensive to duplicate across the full MEB / temperature matrix.

Physical model / extraction remain frozen; only validated numerical cost is reduced.

## 2. Mesh policy

### DC broad sweep — MeshLevel 0
FZ-B Mesh0↔1: ΔVth 0.011 mV, ΔSSquick 0.0006 mV/dec, ΔId@Vg2 0.09%.

### GIDL broad screening — MeshLevel 1
Against targeted Mesh2: ΔGIDL 0.424%, ΔBTBTmax 0.029%, ΔE@BTBT 1.69%, hotspot shift 0.293 nm.

### Final mechanism / selected points — MeshLevel 2
Use only for nominal anchor, final candidate, boundary/challenger, or anomalous cases.

## 3. Solver policy — benchmark before bulk rerun

Full Rescue V2 remains the numerical reference/fallback, not the automatic production default.

Run one nominal runtime-equivalence case:

- MEB = 36 nm
- T = 300 K
- Vd = 1.2 V
- MeshLevel = 0

Compare a relaxed PROD-STANDARD continuation with the frozen Rescue reference.

Acceptance:

- BiasReached = 1
- Vth_CC_Reached = 1
- |ΔVth| ≤ 1 mV
- |ΔSSquick| ≤ 0.3 mV/dec
- ΔId@Vg2 ≤ 2%
- runtime preferably at least 2× faster

If PASS, use PROD-STANDARD for routine DC. If FAIL, use Rescue V2 for that branch.

## 4. Calibrated MEB revalidation @300 K

Required DC:

- MEB = 31 / 36 / 41 nm
- Vd = 0.05 and 1.2 V
- T = 300 K

This yields Vth / SS, DIBL 0.05→1.2, and Ion/Ioff guardrails with **6 DC cases**.

Vd=1.0 V is secondary and is not repeated for every MEB point unless same-lineage comparison is needed.

Required GIDL:

- MEB = 31 / 36 / 41 nm
- Vd = 1.2 V
- Vg = -0.7 V
- T = 300 K
- MeshLevel = 1

Required GIDL cases: **3**.

## 5. Mechanism

From the three GIDL TDRs extract terminal GIDL, BTBTmax/distribution, hotspot, E@BTBT, common fixed-cut E, integrated E, integrated BTBT, and active width.

Confirm only final selected/boundary points with MeshLevel 2.

## 6. Production sequence

1. P0 runtime-equivalence benchmark
2. P1 31/36/41 @300 K: DC(0.05/1.2) + GIDL
3. P2 fixed-cut / BTBT mechanism
4. P3 233/300/340/380 K calibrated GIDL matrix
5. P4 temperature DC guardrail only where needed
6. P5 GIDL → 1T1C retention
7. P6 effective MEB design range

## 7. Do not repeat

- calibration DOE
- DomainY sweep
- low-Vd DIBL splitting
- Hurkx/Nonlocal bridge
- GaussFactor / setback dead ends
- full Mesh2 matrix
- 1.0-V IDVG at every MEB / temperature by default

## 8. Freeze rule

If a production point fails numerically: do not retune GCS/GDB/Qf; use Rescue fallback first, then inspect continuation/mesh. Physical calibration remains frozen.