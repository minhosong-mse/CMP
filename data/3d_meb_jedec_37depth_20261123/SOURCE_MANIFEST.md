# Source manifest — 2026-11-23 final-depth export and five R1 recoveries

**CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** This record documents external Sentaurus data already executed by the user; archive/QC did not run Sentaurus. Native SWB ZIPs are retained outside GitHub per D-005.

## Source identity

- Native ZIP: `CMP_MAIN_MEB35_R1_RECOVERY_NOV23_20261123_213740.zip`
- SHA-256: `77605aab6ef2311e120a763b544b21f6df8eeedf96344f2ad3b1ee1f2144af5b`
- ZIP: **919 entries**; `testzip() == None`; size ~149.68 MB.
- Native export contains `NODE_MAPPING.csv` (131 selected mappings) and `CANDIDATES.csv` (274 entries) plus native SWB source trees, PP SDE, PP SDevice, statuses, logs, PLT and mesh-related evidence. Existing recovered 11 cases in the ZIP are already incorporated from prior checkpoint and **not counted again**.
- Source parent for normal 35 nm physics/template: previous executed `CMP_MAIN_MEB54_NOV23_20261123_175736.zip` (54 nm).
- Source parent for the *numerical-only R1* solution: previous accepted `CMP_OTHER_NOV23_20261123_173618.zip` 11-case R1 recovery, mode-matched normalized executed PP decks.
- The source was checked using `/mnt/data/cmp_meb35_five_r1_extract_qc.py`, a standalone native ZIP parser included with this session's downloadable QC package (requires NumPy and the three external ZIPs).

## Newly accepted 35 nm — 20/20

MEB=35 nm: 4 temperatures (233.15/300/358.15/368.15 K) × modes 0/1/5/6/7. Selected `CMP_final_Copy1_Copy` and `CMP_final_Copy1_Copy_Copy` projects via full qualified project and node IDs. All 20 have terminal target bias, finished log/Done status, finite native curves, identity-consistent four-level SWB source tree and grid-level executed PP SDE. For RunMode7 all four have 101 samples over VSN 0.8–1.0 V, correct current signs/conditions. After parameter substitutions, 35 nm SDE matches executed 54 nm SDE normalization and mode-specific PP SDevice templates match existing 54 nm executed source. This checks **source equivalent**, not bit-identical native mesh.

## Newly recovered five exact failed targets — 5/5

| MEB nm | Temp K | Mode | New selected project | New node | End-bias QC |
|---:|---:|---:|---|---:|---|
| 27 | 358.15 | 1 | `CMP_eeeeeeee_Copy` | 39 | VD=1.2 V, VG=2.0 V |
| 40 | 358.15 | 1 | `CMP_eeeeeeee_Copy` | 302 | VD=1.2 V, VG=2.0 V |
| 46 | 358.15 | 1 | `CMP_eeeeeeee_Copy` | 328 | VD=1.2 V, VG=2.0 V |
| 47 | 368.15 | 5 | `CMP_eeeeeeee_Copy` | 387 | VD=1.2 V, VG=−0.7 V |
| 58 | 358.15 | 7 | `CMP_eeeeeeee_Copy` | 357 | VSN=1.0 V; 101 samples |

All selected R1 PP SDevice normalized execution templates matched mode-equivalent accepted **prior executed numerical R1 sources**. The same modeled SDE/physical conditions and native grid source identity were independently checked. R1 changed numerical continuation only. Old incomplete cases remain in immutable 36-depth master; the successor's `node_qc_740.csv` selects the new source for the five keys.

- `accepted_node_qc_25.csv` and `selected_sources_25.csv` give project-qualified new evidence and source PLT SHA256.
- `metrics_delta_9rows.csv` contains four full new 35 nm temperature rows and five recovery-only affected rows. For recovered mode 1 cases, update Ion/Ioff/Vth_high/SS and **recompute DIBL from the previously valid Vth_low**; for recovered mode 5 recompute signed Hurkx ON−OFF from prior mode 6; for recovered mode 7 update IVSN estimate and QC. Do not replace unrelated valid old modes.
- New accepted raw curve delta: **2,607 DC** points and **505 IVSN** points (five 101-point trajectories); retained in the downloadable QC package associated with this source ZIP. Earlier GitHub archived curves are not overwritten. Source CSV file count and curve identity validated.
- For new MEB 35, relative 233.15 K IVSN KCL residual is ~**0.0271%**, below 1% warning criterion. Prior cumulative low-current 233.15 K warnings remain **25**.

## Aggregate coverage

- Parent immutable 36-depth checkpoint: **712/720** endpoint-complete, eight incomplete, one depth not yet exported.
- New 35 depth adds 20 PASS, and original five R1 failures add 5 PASS: **712 + 20 + 5 = 737**.
- All **37/37** depths have native exports, **740/740** target keys mapped, **737/740** endpoint-complete; **146/148** MEB×temperature rows have all five modes.
- Only **three** 53 nm incomplete nodes: `53/358.15/M1 n3182`, `53/358.15/M5 n3183`, `53/368.15/M7 n3191`, all from original `CMP_3D_Temp_49-60_Copy_Copy`; numerical-only R1 three-node kit is **prepared**, not yet independently re-verified executed/complete.
- 35/36/older checkpoints are not modified. Exact native 3D mesh equivalence and production-level device calibration are not proved.

**Claim bounds:** `t_est_s` integrates an assumed fixed 10 fF over IVSN 0.8–1.0 V; not measured retention or JEDEC compliance. Hurkx ON−OFF current is a signed leakage proxy, not isolated physically collected GIDL. SRH omitted, low-current KCL warnings remain, no production optimum/design-window claims are established.
