# Source/provenance manifest — complete 37-depth MEB DOE, 2026-11-23

**Archive maturity:** DATA ACQUISITION NUMERICALLY COMPLETE / SCIENTIFIC-PROVISIONAL. Original external native SWB ZIPs were generated through Sentaurus Workbench by the user. The analysis session executed no Sentaurus solver runs. Native ZIPs are **not committed** to GitHub under CMP D-005 because of size and original raw provenance.

## Incremental source ZIPs from the 37-depth and last-recovery steps

| Archive | SHA-256 | Accepted scope |
|---|---|---|
| `CMP_MAIN_MEB35_R1_RECOVERY_NOV23_20261123_213740.zip` | `77605aab6ef2311e120a763b544b21f6df8eeedf96344f2ad3b1ee1f2144af5b` | 20 newly passed 35 nm cases, five previously failing R1 recoveries; original 11 R1 appearances not re-counted |
| `CMP_MAIN_MEB53_R1_FINAL_NOV23_20261123_220510.zip` | `3be0f42ee8f4025cabcd8ee2af766bd682938fe9a63f839235755e47ffe14e32` | **only** three final 53 nm R1 recovery cases (358.15/M1, 358.15/M5, 368.15/M7) |

Final source ZIP size **55,341,641 bytes**, **214 entries**; ZIP `testzip()` clean. It also includes older `CMP_eeeeeeee` R1 cases and 17 unrun `CMP_final_Copy` placeholders for 53 nm. They were **not newly accepted**, not double-counted and not allowed to replace earlier native `CMP_3D_Temp_49-60_Copy_Copy` valid source records.

## Recovered 53 nm final source evidence

| Key MEB/TempK/RunMode | New project/node/grid | Native terminal value | Verification |
|---|---|---|---|
| `53/358.15/1` | `CMP_eeeeeeee_53`, n39, g128 | VD 1.2 V; VG 2.0 V | PP SDE/device, prior R1 solver template, tree, log/sta, 446 native samples |
| `53/358.15/5` | `CMP_eeeeeeee_53`, n40, g128 | VD 1.2 V; VG -0.7 V | PP SDE/device, prior R1 solver template, tree, log/sta, 446 native samples |
| `53/368.15/7` | `CMP_eeeeeeee_53`, n47, g128 | VSN 1.0 V | Same PP/log/tree and **101 IVSN points from 0.8 to 1.0 V**, source/sink sign check |

PP SDE normalized source of all three matches original 53 nm preprocessed SDE after node normalization. Mode-specific executed PP SDevice matches the original, independently successful numerical-only Recovery R1 solver **and differs from the older failed parent only in numerical solver continuation**. Original physical parameters, contact/temperature, 4.8 eV workfunction, Hurkx ON/Mode6 OFF, grid and bias goals were retained. **Source match is not a demonstration of binary-identical 3D meshes.**

Per-case native PP/SDE/PLT hashes are in [meb53_r1_native_provenance_3.csv](meb53_r1_native_provenance_3.csv); each accepted PLT SHA-256 is also in [meb53_r1_selected_sources_3.csv](meb53_r1_selected_sources_3.csv). The full [last ZIP machine manifest](meb53_r1_source_manifest.json) records archive counts.

## Historical source pointers (immutable)

- [36-depth source manifest](../3d_meb_jedec_36depth_20261123/SOURCE_MANIFEST.md): the original 53 nm ZIP `CMP_MAIN_MEB53_NOV23_20261123_192708.zip` SHA256 `691724181402bf429277cf6132f912263410375207c7d7f3c0667ea8dca17987`, 17 accepted and three **original** failed source logs.
- [37-depth parent source manifest](../3d_meb_jedec_37depth_20261123/SOURCE_MANIFEST.md): 35 nm + five previous R1, exactly 737/740 before current last three.
- [35-depth checkpoint](../3d_meb_jedec_35depth_20261123/SOURCE_MANIFEST.md): 47 nm initial failure and retained native source copy.
- [34-depth checkpoint](../3d_meb_jedec_34depth_20261123/SOURCE_MANIFEST.md): 41 nm from other account and matching 3D source.
- [33-depth checkpoint](../3d_meb_jedec_33depth_20261123/SOURCE_MANIFEST.md): main/other historical native ZIPs and eleven previously recovered R1 cases.
- Earlier 18/21-depth archives remain independent historical evidence, not overwritten.

## Merge policy and internal evidence limits

1. Parent canonical archive: `../3d_meb_jedec_37depth_20261123/node_qc_740.csv` and `six_metrics_148_conditions.csv`.
2. Replace **exactly three** prior status `RERUN` keys with the new R1 `PASS` source and native PLT hashes; other **737** valid source identities remain bytewise record-unchanged.
3. At `53/358.15`, use new Mode1 Ion/Ioff/Vth_high/SS and Mode5 Hurkx ON, retain the older *valid* Mode0 Vth_low, Mode6 Hurkx OFF and Mode7 IVSN. **Recompute DIBL and signed Hurkx excess** from the accepted modes.
4. At `53/368.15`, use the new Mode7 IVSN integration and KCL QC. Retain the already accepted Modes 0/1/5/6 metrics.
5. Final: 740 unique accepted `(MEB,TempK,mode)` keys, 148 all-mode-complete metric rows, 331 *incremental* Nov23 selected PLT records (including 19 R1); the historical source ledger extends back through earlier immutable folders and is not falsely described as 331 full-campaign sources.
6. Combined newly GitHub-archived curve **deltas** are 6,174 DC + 1,313 IVSN rows (from 35/five R1, 47 initial, 53 initial and 53 final R1). Earlier curves remain in original historical folders; native raw partial logs remain inside external ZIPs. Concatenate each numbered DC group dropping duplicate headers.

**Scientific caveats remain:** 25 cold low-current relative-KCL warnings; constant **assumed** 10 fF IVSN `t_est` integral is *not* directly measured physical 1T1C retention; signed Hurkx ON−OFF is *not* pure collected GIDL; no proven binary mesh equality, full SRH coverage, JEDEC compliance, production optimum or final design recommendation. Numerical data acquisition complete; interpretation and design-range conclusions **deferred**.
