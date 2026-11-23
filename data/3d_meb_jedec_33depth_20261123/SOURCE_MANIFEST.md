# Source manifest — 2026-11-23, 33-depth MEB DOE increment

**Native source SWB ZIP archives remain external** under CMP D-005. The GitHub repository contains extracted numerical CSVs, identity/QC, provenance, and source hashes; it does not duplicate native Sentaurus PLT/TDR/log files.

| User-supplied native ZIP | Source SHA-256 | Newly accepted scope |
|---|---|---|
| `CMP_MAIN_NOV23_20261123_173554.zip` | `eed37e4b5424998718978c8a062ee837a22324a884880cfdf7e77933c76a62c6` | main account 26/34/40/42/43/46/52/57/58 nm, plus old failed candidate copies |
| `CMP_OTHER_NOV23_20261123_173618.zip` | `14351183c7ea22d744e7ea2930255067461bbb59b0f59cc5b8ff2897329d4c0f` | other account 27 nm; 11 R1 recovered cases from `CMP_eeeeeeee` |
| `CMP_MAIN_MEB39_NOV23_20261123_175226.zip` | `5ca2d303ceb5cf466296e34b14cd06d3ecbf78292057fa43fc861292f136cc58` | main account 39 nm |
| `CMP_MAIN_MEB54_NOV23_20261123_175736.zip` | `daf8b1f4b300cc29193f3e89d2b0d10bc82f3ef5cb757f8a16eee63749134f87` | main account 54 nm |

SHA-256 digests checked against the four uploaded ZIPs in this session. Each source ZIP includes project-qualified SWB `gtree.dat`, `pp*_des.cmd`, grid-matched `pp*_dvs.cmd`, statuses, native curves, and source-identity mapping. Copies share node IDs but are not independent experiments; use (MEB, TempK, RunMode), native PLT digest, project name, and recovery provenance to deduplicate.

## Exact merge policy

- Parent frozen baseline: `../3d_meb_jedec_21depth_20261122/node_qc_420.csv`, `six_metrics_84_conditions.csv`; those files and earlier archives are not rewritten.
- New 12 depths: `26, 27, 34, 39, 40, 42, 43, 46, 52, 54, 57, 58`.
- 11 old failed/pending cases have accepted, independently executed *numerical R1* replacements, with both old failure and accepted recovery traceable in `node_qc_all_candidates.csv`.
- New 12-depth coverage is 236/240 valid; adding 11 recoveries to previous 409 valid yields `409 + 11 + 236 = 656` of 660 exported planned cases.
- `node_qc_660.csv` is the deduplicated full-grid status after recovery; `six_metrics_132_conditions.csv` merges recovery-only metric fields with preexisting valid modes, retaining earlier values for fields not rerun.
- New/recovery-only curves are append-only deltas. DC split into 3 CSV files to respect transfer size: concatenate in numbered order **dropping the repeated header** of parts 02 and 03; IVSN contains 50 valid × 101 points = 5,050 rows. Prior 21-depth curves live in their original Nov-19/21/22 folders and are not copied into this increment.
- No numerical physical model, geometry, SDE, Workfunction, or mesh-policy changes are asserted. R1 changed numerical continuation, not physical parameters; identical native binary mesh has **not** been proven.

## Remaining gaps

- Four unexported depths: `35, 41, 47, 53 nm` = 80 target nodes.
- Four exported but incomplete nodes, **all 358.15 K**: `27/M1` (other n409), `40/M1` (main n3156), `46/M1` (main n3312), `58/M7` (main n3315). Current R1 rerun CMD is prepared; these four recovery results have **not yet been received or verified**.
- 22 low-temperature (233.15 K) IVSN cases retain relative KCL residual warnings >1%; they remain numerically endpoint-complete with **QC caveats**.

All programmatic data carry CMP-EXECUTED provenance and SCIENTIFIC-PROVISIONAL interpretation; constant 10 fF `t_est` is an integral estimate and not directly measured retention, Hurkx ON–OFF difference is not a pure collected GIDL measurement, and the DOE does not establish production optimum or JEDEC compliance.
