# C7_4 Final-Freeze Validation Plan

> **Status:** Prepared / not yet executed  
> **Date:** 2026-10-05  
> **Selected candidate:** C7_4 / B_QF_HALF  
> **Freeze target:** `B0-2D-PAPER-CAL`

## 1. Selected candidate

```text
GateCouplingScale = 2.300
GateDepthBoost    = 0.025 um = 25 nm
Qf_Int            = 2.55e12 cm^-2
MEB / GateTop     = 36 nm
T                 = 300 K
```

Selection checkpoint:

```text
Vth @ 1.2 V        = 0.655558 V
SSquick @ 1.2 V    = 75.7652 mV/dec
DIBL 0.05→1.2      = 23.408 mV/V
Ion/Ioff (2.0/0)   = 2.6168e10
```

C7_4 is selected because it provides the best overall balance of Vth / SS / DIBL / Ion-Ioff and smooth three-bias behavior. No C8 calibration DOE is planned.

## 2. SWB parameter rule

Only one SWB parameter is used in the freeze projects:

```text
SDE parameter:
MeshLevel
```

```text
MeshLevel = 0 : C7_4 standard selection mesh
MeshLevel = 1 : standard mesh + one-step finer drain-side local refinement
```

Do **not** add GCS / GateDepthBoost / Qf as SWB parameters. They are fixed to the selected C7_4 values.

## 3. FZ-A — solver-path cross-check

```text
MeshLevel = 0
Vd        = 0.05 V
Vg        = 0→2 V
T         = 300 K
```

Run count: 1.

PASS:

- ΔVth ≤ 1 mV
- ΔSSquick ≤ 0.5 mV/dec
- ΔId(Vg=2) ≤ 1%
- valid bias / threshold extraction

## 4. FZ-B — DC mesh confirmation

```text
MeshLevel = 0 / 1
Vd        = 1.2 V
Vg        = 0→2 V
T         = 300 K
```

Run count: 2.

PASS:

- ΔVth ≤ 2 mV
- ΔSSquick ≤ 0.5 mV/dec
- ΔId(Vg=2) ≤ 1%
- ΔIon/Ioff ≤ 5%

## 5. FZ-C — GIDL / BTBT / local-E mesh confirmation

```text
MeshLevel = 0 / 1
Vd        = 1.2 V
Vg        = -0.7 V
T         = 300 K
BTBT      = Hurkx
```

Run count: 2.

PASS:

- endpoint reached for both meshes
- ΔGIDL ≤ 2%
- ΔBTBTmax ≤ 5%
- ΔEhot ≤ 2%
- ΔEmax ≤ 2%
- hotspot coordinate shift ≲ 2 nm preferred

## 6. Freeze gate

```text
FZ-A PASS
+ FZ-B PASS
+ FZ-C PASS
----------------
B0-2D-PAPER-CAL official freeze
```

Until that gate is passed, calibrated MEB / temperature production reruns are not started.

## 7. Prepared working-deck names

```text
CMP_C7_4_FINAL_FREEZE_SDE.cmd
CMP_C7_4_FZ_A_SOLVER_005_SDevice.cmd
CMP_C7_4_FZ_A_SOLVER_005_SVisual.cmd
CMP_C7_4_FZ_B_DC_12_SDevice.cmd
CMP_C7_4_FZ_B_DC_12_SVisual.cmd
CMP_C7_4_FZ_C_GIDL_SDevice.cmd
CMP_C7_4_FZ_C_GIDL_SVisual.cmd
```

Final source archive should use the corrected C7_4 metadata rather than the older common-C7 SVisual metadata.
