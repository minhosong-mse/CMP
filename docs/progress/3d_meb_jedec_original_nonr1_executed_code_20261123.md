# 2026-11-23 — Original non-R1 executed SDE / SDevice archive

**Code provenance: CMP-EXECUTED PP RECONSTRUCTION / scientific interpretation remains PROVISIONAL.** This entry archives the **original 3D MEB×temperature DOE solver source**, *not* the later numerical-only R1 recovery commands. No Sentaurus execution or physical-model retuning was performed in this documentation step.

## Canonical reusable SWB sources

- [Original 3D SDE, comment-cleaned](../../code/sde/3d_sun_saddle_v1/CMP_3D_MEB_DOE_ORIGINAL_dvs.cmd)
- [Original 5-RunMode SDevice, comment-cleaned](../../code/sdevice/3d_sun_saddle_v1/CMP_3D_MEB_DOE_ORIGINAL_des.cmd)

These contain **source-level SWB placeholders** (`@DBCAT_nm@`, `@node@`, `@TempK@`, `@RunMode@`, etc.), not node-specific PP snapshots. Retaining `#if`, `#elif`, `#else`, and `#endif` in SDevice is mandatory: they are executable SWB preprocessing branches, **not disposable comments**. SDE `display` and save-model/build-mesh calls are executable and were likewise preserved; any inherited stale text in diagnostic `display` output is not a present research-status assertion.

## Actual DOE parameters

| Parameter | Executed value / range |
|---|---|
| Geometry/model lineage | `3D-Sun-SADDLE-V1 / Flat upper S/D` |
| `DBCAT_nm` | **24–60 nm** step 1, 37 MEB depths |
| `TempK` | **233.15, 300, 358.15, 368.15 K** |
| `RunMode` | **0, 1, 5, 6, 7** (five modes) |
| SDE `ARgate`, `Wfin_nm` | **6.0**, **17** |
| SDE `JunctionRatio`, `RfilletFactor` | **0.4**, **1.0** |
| SDE `MeshCase`, `CadSeamCase`, `CurveGrid` | **0**, **3**, **1** |
| SDE `GaussFactor` | **0.0** |
| Gate workfunction | **4.8 eV** |
| Hurkx | ON for modes 0/1/5/7; **OFF for mode 6** |
| Original SDevice `NumberOfThreads` | **32** in both DC and Mode-7 branches |
| Original DC solver | `Digits=5`, `Iterations=30`, `InitialStep=1e-3`, `Increment=1.30`, `MinStep=1e-6`, `MaxStep=1e-2` |
| Original IVSN solver | `Digits=7`, `Iterations=50`, `MinStep=1e-10`, `MaxStep=0.01`, 101-point 0.8–1.0 V sweep |
| IVSN circuit | `Ccell=1e-14 F` (assumed 10 fF), `WL=-0.7 V` |

The source retains the original simulation configuration, not the smaller-step `Extrapolate(MinStep=...)` and other R1 numerical recovery controls. The earlier prepared [5-mode development file](../../code/sdevice/3d_sun_saddle_v1/CMP_3D_JEDEC_5MODE_des.cmd) used **8** threads and carried historical `PLANNED` comments; **it is not the exact executed source**. The archive linked here is preferred when describing *what actually ran*.

## Evidence audit — non-R1 original, excluding recovery nodes

### SDE independent cross-depth check

The same parameterized executable SDE content was reconstructed from these native original PP sources:

| Native ZIP | Project | Depth | Actual original PP SDE |
|---|---|---:|---|
| `CMP_MAIN_MEB35_R1_RECOVERY_NOV23_20261123_213740.zip` | `CMP_final_Copy1_Copy` | 35 nm | `pp601_dvs.cmd` (normal source, **not R1**) |
| `CMP_MAIN_NOV23_20261123_173554.zip` | `CMP_3D_Temp_36-48` | 40 nm | `pp3140_dvs.cmd` |
| `CMP_MAIN_MEB53_NOV23_20261123_192708.zip` | `CMP_3D_Temp_49-60` | 53 nm | `pp3166_dvs.cmd` |
| `CMP_MAIN_MEB54_NOV23_20261123_175736.zip` | `CMP_3D_Temp_49-60_Copy_Copy1` | 54 nm | `pp3192_dvs.cmd` |

Scheme comment removal is **quote-aware** (semicolons in strings retained). Only the approved original SWB substitution parameters and output mesh node name were restored to placeholders. After re-expanding, each SDE reproduces its native executable PP content **exactly**, apart from removed comments; the normalized executable SDE was identical across these four original projects.

### SDevice five-branch check

Native non-R1 sample: `CMP_MAIN_MEB53_NOV23_20261123_192708.zip`, project `CMP_3D_Temp_49-60`, TempK=233.15, MEB=53, grid `3166`:

| Mode | Original native executed PP | Verification |
|---:|---|---|
| 0 | `pp3169_des.cmd` | Exact preprocessed executable content match |
| 1 | `pp3170_des.cmd` | Exact match, including mode-1 spatial Plot |
| 5 | `pp3171_des.cmd` | Exact match, Hurkx ON |
| 6 | `pp3172_des.cmd` | Exact match, Hurkx OFF |
| 7 | `pp3173_des.cmd` | Exact match, 101-point IVSN circuit and targets |

For this comparison, all SWB placeholders and conditional branches were expanded, then whitespace and initial `*` comment lines were ignored. Five out of five executable branches matched the actual original PP examples **with NumberOfThreads=32**. These are source-equivalence checks; they do **not** establish native binary mesh equality.

## Separation from numerical R1 repairs

- The **original DOE** is archived in the two non-R1 CMD files above, unchanged in executable meaning.
- Failed individual endpoints were independently repaired afterward using [numerical Recovery R1](../../code/sdevice/3d_sun_saddle_v1/CMP_3D_JEDEC_RECOVERY_R1_des.cmd) and the [MEB53 targeted R1](../../code/sdevice/3d_sun_saddle_v1/CMP_MEB53_R1_ONLY_des.cmd). These controls **must not** be described as having been used for the initial sweep.
- The complete [740-endpoint master](../../data/3d_meb_jedec_37depth_complete_20261123/README.md) includes selected original and R1-recovered numerical outcomes; their source identities remain individually recorded. No original failed execution was retroactively modified.

## Claim limits

The 740/740 result indicates numerical terminal endpoint completion for the planned 37×4×5 grid; it does **not** establish production DRAM accuracy, physically measured retention, JEDEC compliance, independent pure GIDL extraction or binary mesh-equivalence. The constant-10 fF IVSN integral remains a model-qualified estimate. No final optimum or MEB design window is selected here.
