# MEB 53 externally executed source / dataset manifest — 2026-11-23

- Native ZIP: `CMP_MAIN_MEB53_NOV23_20261123_192708.zip` (main account).
- SHA-256: `691724181402bf429277cf6132f912263410375207c7d7f3c0667ea8dca17987`.
- ZIP integrity: testzip() clean, **310 entries**.
- Original MEB 53: 20 unique source-mapped conditions; 6 from `CMP_3D_Temp_49-60`, 14 from `CMP_3D_Temp_49-60_Copy_Copy`; 17 true endpoint PASS / 3 incomplete.
- The ZIP also includes 11 historic recovery candidates, **not** added to counts (canonical 11 R1 recovered already stored in earlier checkpoint).
- `CANDIDATES.csv` includes 80 project-level 53 nm candidates across 4 SWB copies; the failed three conditions have no alternative nonidentical complete PLT in other copies. Selected accepted 53 nm identities and native source PLT SHA-256 in [meb53_selected_cases.csv](meb53_selected_cases.csv).
- Mesh grid source: `pp3166_dvs.cmd` in corresponding original project; `(define DBCAT_nm 53)`. After depth/output normalization, SDE template SHA-256: `f81d0ce4cb2476f30b91c5e7f8a0d304240e39e234643c46ef0d85b6dbe8660b`, identical to earlier 54 nm executed template.
- Each selected preprocessed SDevice deck, by mode, matched the executed 54 nm deck template after temperature and node normalization; mode 6 omitted Hurkx and other modes retained it. SWB four-level tree, grid/T/depth, PP files, status, solver log, finite curves and terminal bias checked.
- Failed: **358.15 K mode 1 n3182** (VG 0.0014228319 V, VD 0.8886529545 V; 90 samples), **358.15 K mode 5 n3183** (VG 0 V, VD 0.8796529545 V; 82 samples), **368.15 K mode 7 n3191** (VSN 0.806 V; 4 samples). Newton nonconvergence and MinStep underflow in logs. Two modes marked SWB Done despite terminal failure.
- Selected new results: 1,503 DC curve points (only valid DC nodes) and 303 IVSN samples (3 validated 101-point mode 7 nodes). Incomplete traces remain only in original ZIP plus QC metadata, not in selected scientific curves.
- Frozen parent remains [35-depth checkpoint](../3d_meb_jedec_35depth_20261123/SOURCE_MANIFEST.md); no older evidence overwritten. Original native ZIP remains external per D-005. Native binary mesh equality remains **not demonstrated**.
- Measurement interpretation is provisional: `t_est_s` uses assumed constant 10 fF, Hurkx differential is a leakage proxy, not pure GIDL or directly measured DRAM retention.
