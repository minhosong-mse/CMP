# External source archive manifest — Nov-22 increment

Original native ZIPs remain external per D-005. The supplemented SDE decks were necessary because the first extraction selected the level-2 SWB parent rather than the physical grid's level-1 node. Do not treat an unrelated project copy as its SDE source.

| Archive | Scope | SHA-256 |
|---|---|---|
| CMP_1MEB_MAIN_20261122_230245.zip | 60 nm, 20 unique targets | `7353a260aa8c00215f1f3ac44b7966a1061a13443649388e8f96e616e6175c0e` |
| CMP_2MEB_OTHER_20261122_230236(1).zip | 48, 59 nm, 40 unique targets | `ea63eea35ab06ed57085fbfc2a7aaca59b34c7e0c0588464d71f481e3e567e37` |
| CMP_60_SDE.zip | CMP_3D_Temp_49-60_Copy_Copy/pp3348_dvs.cmd | `04e40fe81bf23d3f55f570140eec49e06d21bd1418184e55d4a5652a69207a60` |
| CMP_48_59_SDE.zip | CMP_final/pp314_dvs.cmd; CMP_final_Copy/pp288_dvs.cmd | `5bb94975a1ba9161ff707366b4e9c4bc760857b3cc997d1fb458cfe2d7c8d194` |

20 duplicate 48 nm PLT/PP pairs in CMP_final_Copy2 are byte-identical to CMP_final. Select CMP_final with its own supplemental SDE. Other unexecuted project-copy rows are not counted as physical duplicates or additional targets.

| Extracted file (CRLF bytes) | SHA-256 |
|---|---|
| dc_curves_new.csv | `ff88cfd1a2fd1a296366527dbba484622b281c0275357aef182ee55f0476ec54` |
| ivsn_curves_new.csv | `b9385a4ccdce2b5c1a7687ff0205088c64f07a8dc26b7001d8e6e712ae9a6ad0` |
| node_qc_420.csv | `c38e9bb1647f657a5c53a5d8545fdae7acd42101769fa69685488884df12cd41` |
| node_qc_60_new.csv | `db8ecd81e443114cb2b39a3cedb72e2e3d745d3e3e59247e18b06252ba90e5cc` |
| six_metrics_12_new.csv | `75eb74acdb7578c74de59788c497cdfd785d68c4133e73adab7eeb773385b288` |
| six_metrics_84_conditions.csv | `5e52a57326a1b09019ecacf9a098692b86f4c04332e4e3bb6aa2333d66bd2172` |
