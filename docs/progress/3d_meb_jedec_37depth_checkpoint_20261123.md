# 2026-11-23 — 37-depth 3D BCAT MEB campaign, 35 nm export and five R1 recoveries

**Status: PARTIAL / CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** All **37 depths** have now been exported, but the campaign is **not yet fully validated**: 3 SDevice endpoints at MEB53 remain incomplete. No new Sentaurus simulation was performed by this analysis agent.

## Evidence and new execution scope

- [Previous immutable 36-depth checkpoint](3d_meb_jedec_36depth_checkpoint_20261123.md): 36/37 MEB, 712/720 endpoint PASS; eight incomplete, MEB35 not exported.
- [New native source manifest](../../data/3d_meb_jedec_37depth_20261123/SOURCE_MANIFEST.md): main-account `CMP_MAIN_MEB35_R1_RECOVERY_NOV23_20261123_213740.zip`, SHA-256 `77605aab6ef2311e120a763b544b21f6df8eeedf96344f2ad3b1ee1f2144af5b`, 919 archived entries, ZIP integrity verified. Native source retained outside GitHub per D-005.
- 35 nm across all 4 temperatures × 5 modes: **20/20 PASS** with project-qualified SWB tree/SDE grid/PP device/PLT/status/log/true bias-endpoint checks. New 35 nm 358/368 K subsets were split across SWB copies, without duplicate counting.
- Five recovered previous failures accepted **once each** using numerical-only R1: `27/358.15/M1` new MAIN n39, `40/358.15/M1` n302, `46/358.15/M1` n328, `47/368.15/M5` n387, `58/358.15/M7` n357; all in `CMP_eeeeeeee_Copy`. Mode7 reached VSN 1.0 V with exactly 101 samples. The normalized executed PP decks match the previous successful 11-case R1 recovery source by RunMode.
- For all 25 selected cases, depth and temperature parameters, SWB four-level identity, grid PP SDE, mode-specific Hurkx physics, native finite PLT, completed log and bias endpoint were checked. After depth/node normalization, new 35 nm source model matches executed 54 nm source. Native binary 3D mesh equality **is not proven**.
- 25/25 selected new/recovered PASS. **2,607 new selected DC points**, **505 new selected IVSN points** (5 × 101); raw curve deltas and extractor available in session QC ZIP. Historical source ZIPs and previous GitHub snapshots remain unmodified.

## Actual updated master state

| Metric | After selected 25 additions |
|---|---:|
| Exported depths | **37 / 37** |
| Unique mapped target SDevice nodes | **740 / 740** |
| Endpoint/log/PP PASS | **737 / 740** |
| Numerically incomplete nodes | **3** (all MEB53) |
| Depth × temperature rows, 5 modes complete | **146 / 148** |
| Existing numerical R1 recoveries accepted before this archive | **11**, unchanged |
| Newly recovered numerical R1 source cases | **5** |
| 233.15 K low-current IVSN relative-KCL warnings | **25**, unchanged |

Full cumulative source-based master: [740 node QC](../../data/3d_meb_jedec_37depth_20261123/node_qc_740.csv), [148-row six metrics](../../data/3d_meb_jedec_37depth_20261123/six_metrics_148_conditions.csv), [328 Nov-23 selected-source ledger](../../data/3d_meb_jedec_37depth_20261123/selected_cases_328.csv) (not all 737 historical nodes). [Reproducible CSV consistency validator](../../code/scripts/analysis/3d_meb_jedec_20261123/validate_37depth.py); internal CSV checks do **not** substitute for native PP/log/PLT execution evidence.

Five old incomplete failures are preserved in the immutable 36-depth snapshot, while the current successor selects their new PP/log/PLT-verified R1 completions. Ion/Ioff/SS/Vth_high were refreshed for modes 1 and DIBL recomputed against preserved valid Vth_low; Mode5 signed Hurkx ON−OFF was recomputed using previously valid Mode6; Mode7 IVSN t_est was refreshed. No unrelated prior accepted modes were intentionally replaced.

## Remaining exact three-node blocker

| MEB nm | Temp K | Mode | Original project | Original failed node |
|---:|---:|---:|---|---:|
| 53 | 358.15 | 1 | `CMP_3D_Temp_49-60_Copy_Copy` | 3182 |
| 53 | 358.15 | 5 | `CMP_3D_Temp_49-60_Copy_Copy` | 3183 |
| 53 | 368.15 | 7 | `CMP_3D_Temp_49-60_Copy_Copy` | 3191 |

53 nm has **3/5 valid modes** at 358.15 K and **4/5** at 368.15 K. Do not calculate unobserved partial-derived final metrics or mark these conditions complete. The [53 nm three-node R1 recovery kit](3d_meb53_r1_selective_rerun_20261123.md) is prepared; no *new* verified native outputs from that kit have yet been received.

## 35 nm metrics and caveats

| T (K) | Ion (µA) | SS (mV/dec) | DIBL (mV/V) | 10 fF t_est |
|---:|---:|---:|---:|---:|
| 233.15 | 3.48161 | 62.25998 | 26.28464 | 21.8746 s |
| 300.00 | 3.63632 | 79.08200 | 21.70605 | 0.0594715 s |
| 358.15 | 3.77964 | 94.57846 | 21.48471 | 0.00403726 s |
| 368.15 | 3.80534 | 97.41193 | 21.59449 | 0.00261354 s |

35 nm at 233.15 K has relative IVSN KCL residual ~0.0271% (not warned at 1% threshold); preexisting 25 cold low-current warnings remain. The constant 10 fF IVSN integral estimate is **not measured DRAM retention**, signed Hurkx ON−OFF is a model-dependent proxy **not pure collected GIDL**, SRH remains omitted, exact 3D mesh equivalence unverified. No production/JEDEC certification, process window, final optimum, or final campaign freeze.

**Next action:** Receive a separate native ZIP with the three **53 nm** recovery cases; verify actual completed bias sweep, 101-point mode7 IVSN protocol, R1 source lineage, and add the resulting fields only after passing terminal/log/source checks. Then finalize 740/740 master and cautiously screen the relative MEB design range.
