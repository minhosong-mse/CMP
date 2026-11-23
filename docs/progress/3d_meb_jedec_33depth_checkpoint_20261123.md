# 2026-11-23 — 33-depth BCAT MEB × 4T × 5-mode DOE checkpoint

**PAUSED / CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** User provided four native SWB ZIP exports from main and other Linux accounts. This session extracted and checked existing externally executed cases; **no new Sentaurus simulations were run during archival and no device physics/mesh/geometry parameters were changed**.

## New numerical scope

- Prior frozen 2026-11-22 campaign: 21/37 depths, 409/420 numerically target-complete, with 11 missing or incomplete original endpoints; 75/84 fully five-mode temperature rows.
- Newly exported depths: `26, 27, 34, 39, 40, 42, 43, 46, 52, 54, 57, 58 nm` = **12** depths × four T × five modes = 240 jobs.
- Newly exported valid cases: **236/240**; four have native curves/logs but target-bias endpoint incomplete.
- **11/11 previous failed/pending original cases recovered** from a separate other-account `CMP_eeeeeeee` project using the numerical-only R1 deck. Recovery versus original solver provenance is kept explicit; original partial records are not erased.
- Cumulative: **33/37 depths, 656/660 sampled endpoints** and **656/740 campaign endpoints**, **128/132** temperature × depth rows five-mode complete; all 33 acquired 300 K temperature rows have five modes.
- `node_qc_660.csv` and `six_metrics_132_conditions.csv` are the new cumulative masters; the 2026-11-22 420/84 originals remain unchanged. Source candidates, selected PLT SHA-256 hashes, DC (22,168 new/recovery rows), IVSN (5,050 new/recovery rows), source ZIP hashes and recovery log are in [data checkpoint](../../data/3d_meb_jedec_33depth_20261123/README.md).

## Exact outstanding items

| Account | Project | MEB nm | Temp K | Mode | Original node | Actual final bias | Required final bias |
|---|---|---:|---:|---:|---:|---:|---:|
| Other | `CMP_final_Copy1` | 27 | 358.15 | 1 | 409 | Vg 0.0394053 V | Vg 2.0 V |
| Main | `CMP_3D_Temp_36-48` | 40 | 358.15 | 1 | 3156 | Vg 0.0322977 V | Vg 2.0 V |
| Main | `CMP_3D_Temp_36-48_Copy1` | 46 | 358.15 | 1 | 3312 | Vg 0.0361195 V | Vg 2.0 V |
| Main | `CMP_3D_Temp_49-60_Copy` | 58 | 358.15 | 7 | 3315 | VSN 0.990 V | VSN 1.0 V |

Observed solver logs report Newton nonconvergence and step size below MinStep. Three failed mode-1 jobs were reported Done in SWB but are **not terminal-complete**. Mode 7 requires exactly 101 points at 0.8–1.0 V for acceptance.

**Still not exported:** MEB **35, 41, 47, 53 nm** = 80 target SDevice jobs. Together with the four incomplete above, **84/740** planned endpoints remain not yet validated. The four numerical reruns are PLANNED, **not yet executed/verified** in this checkpoint; use the existing numerical-only [R1 CMD](../../code/sdevice/3d_sun_saddle_v1/CMP_3D_JEDEC_RECOVERY_R1_des.cmd) in isolated copied SWB projects without changing SDE or physics, and map any new node IDs by condition.

## Technical checks and scientific limits

PP preprocessed SDE was explicitly extracted for each executed grid node; SWB project tree, PP SDevice grid/T/depth, Hurkx ON vs OFF, source status/log, native terminal curve finite values, DC end voltages and IVSN sign/101-point sweep were checked. Duplicate project copies do not multiply unique cases. Identical native mesh tensors were **not independently proved**.

There are **22** 233.15 K IVSN cases with KCL *relative* residual >1%. Keep numerically endpoint-complete but mark low-current QC warnings; they are not unqualified physical validation.

The six-metric protocol remains original: Ion, Ioff, SS, DIBL, signed Hurkx ON−OFF leakage proxy, and numerical t_est from a **fixed, assumed 10 fF** capacitor integrated across 0.8–1.0 V IVSN. The last is **not direct 1T1C retention or a JEDEC-compliance claim**. Hurkx difference is not independently collected pure GIDL. Omitted SRH, unverified full mesh convergence, external native archives and uncalibrated production interpretation remain limitations.

## Next first action

1. Obtain remaining MEB `35/41/47/53 nm` exports with grid-level PP SDE and native logs/curves, plus only four targeted R1 reruns.
2. Independently inspect rerun logs and endpoints, preserve originals and numerical-solver provenance, recompute metrics and expected 740-node master.
3. Only after data close-out screen temperature-specific MEB design range; no final physical optimum or production retention claim now.

Historical 2D, 18-depth and 21-depth files, the root README, and original R1 preparation document are deliberately untouched.
