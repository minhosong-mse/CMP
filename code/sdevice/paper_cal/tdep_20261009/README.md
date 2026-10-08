# 2026-10-09 temperature-MEB SWB execution provenance

**Purpose:** index the temperature command package actually supplied and user-reported SWB matrix; this is NOT a substitute for inspecting 45-condition preprocessed CMD or source data.

- Baseline: B0-2D-PAPER-CAL C7_4 / B_QF_HALF with distinct Atlas MeshLevel 2 policy.
- SWB SDE parameter: MEBDepth (um), 15 values 0.031..0.051 as individually enumerated in docs/progress/paper_cal_temperature_atlas_15x4_dispatch_20261009.md.
- SWB SDevice parameter: Temp_K = 233, 340, 380 K; 300 K original Atlas reused.
- Full 36-nm prepared bundle: CMP_36NM_TEMPERATURE_FULL_CMD_READY_20261008.zip, SHA256 6d53718390b1be33697e103c95ceac616141420eefc7e0091fa7657909684d34.
- It contains five new template SDevice files whose executable difference from each executed 300 K parent is Temperature=300 to Temperature=@Temp_K@; six unchanged SVisual extraction templates and an unchanged SDE template.
- Files were locally prepared and ZIP checked, but are not yet stored as independent tracked GitHub CMD files. Keep source ZIP and SWB project files unchanged; import exact execution artifacts under separate code/evidence commit only after verifying actual pp*_des.cmd and temperature/depth mapping. Do not reconstruct or invent a different temperature deck.
- Planned/expected: 45 condition pairs × five SDevice branches and six SVisual outputs (two from GIDL_ON). No new temperature-result CSV/log has been validated yet.
- Evidence collector supplied separately: CMP_collect_TDEP_45_all_branches.py (read-only). SHA256 0e0120aa9e9e0987ccee65f8a0b1f641596b5e9807eba0b80a4baa17494dc5d6. First next action is capture and upload ZIP, not new TCAD simulation.

No old freeze, prior experiment, or source CMD was overwritten in this checkpoint.
