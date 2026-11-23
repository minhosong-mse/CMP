# 2026-11-23 — 35-depth 3D BCAT MEB × 4T × 5-mode numerical checkpoint

**PAUSED / CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** The user provided an external MAIN-account 47 nm SWB ZIP collected from three copied projects. No Sentaurus runs or parameter changes were performed during extraction.

## Verification

- Parent [34-depth master](../../data/3d_meb_jedec_34depth_20261123/README.md): **676/680** PASS across 34 depths, 132/136 fully five-mode rows, previous R1 numerical recoveries **11/11** unchanged.
- New 47 nm mapping: **20 unique conditions** (233.15/300/358.15/368.15 K × 0/1/5/6/7). Every selected PP SDE deck uses grid node 3322 and defines DBCAT_nm=47. Executed SDE and SDevice templates match previous 40/41 nm sources after only depth/temperature/node normalization.
- New 47 nm endpoint/log QC: **19 PASS, 1 RERUN**. All selected native PLTs, logs and statuses are retained in the external ZIP. The new 47 nm 368.15 K Mode 6 comes from `CMP_3D_Temp_36-48_Copy1_Copy` n3346; 368.15 K Mode 7 comes from `CMP_3D_Temp_36-48_Copy` n3347, 101 valid VSN samples from 0.8–1.0 V.
- Incomplete 47 nm case: 368.15 K **Mode 5**, `CMP_3D_Temp_36-48_Copy1/n3345`. SWB says Done, but the log contains Newton nonconvergence and `Step-size less than MinStep`; last native PLT record `VG=0.0 V`, `VD=1.189584347 V`, compared with required `VG=-0.7 V`, `VD=1.2 V`. No other fully executed candidate in the provided ZIP. *Do not compute Hurkx ON−OFF metric for 47/368.15 K.*
- New 47 nm 233.15 K IVSN relative-KCL maximum residual **3.27%** → `LOW_CURRENT_KCL_WARNING`, cumulative **24** cold KCL warnings; numerical endpoint still PASS.

## Updated campaign totals

| Item | Total |
|---|---:|
| MEB depths with native exports | **35/37** |
| Sampled target conditions | **700/740** |
| Complete endpoint conditions | **695/700**, **695/740** overall |
| Complete five-mode MEB×T rows | **135/140** |
| Depths not yet exported | **35, 53 nm** = 40 target conditions |
| Existing incomplete endpoints | **5** |
| Remaining not-yet-valid targets | **45/740** |

Remaining recovery targets: other account 27/358.15K/M1 (n409); main account 40/358.15K/M1 (n3156), 46/358.15K/M1 (n3312), 58/358.15K/M7 (n3315), **47/368.15K/M5 (n3345)**. For 47/M5, the existing numerical-only R1 deck has a Mode 5 branch; use in an isolated copied SWB project without altering geometry, physics or mesh. All five reruns are **PLANNED**, not verified executed yet.

- [35-depth cumulative 700-node QC and 140-condition six metrics](../../data/3d_meb_jedec_35depth_20261123/README.md)
- [Native ZIP hash and multi-project source provenance](../../data/3d_meb_jedec_35depth_20261123/SOURCE_MANIFEST.md)
- [47 nm reproducible QC script](../../code/scripts/analysis/3d_meb_jedec_20261123/qc_meb47.py)

The 35-depth CSV master and source mapping are archived on GitHub. The original per-depth DC/IVSN curve deltas and native 47 nm ZIP are held in the conversation's external QC package and are not represented as GitHub-hosted native evidence. Earlier checkpoint CSVs and root README remain unchanged.

**Research limitations:** 10 fF constant assumed capacitance for integrated `t_est` is not measured physical DRAM retention; Hurkx ON−OFF is a leakage proxy not pure GIDL; SRH omitted, mesh-equivalence not proven, no production optimum, physical robustness, JEDEC-compliant retention or final freeze claim.

## Next action

Receive 35/53 nm native ZIPs and five isolated numerical R1 rerun results; verify actual terminal bias, solver logs and source provenance before selecting a complete 740-node data master and discussing temperature-specific effective MEB range.
