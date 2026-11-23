# External native source — 47 nm incremental export

- Source ZIP: `CMP_MAIN_MEB47_NOV23_20261123_190950.zip`
- ZIP SHA-256: `53e363f581b188ccb22cede92437295c0c9db5864b088ce0cb162b2bf0c7ee42`
- ZIP integrity: `testzip() == None` (320 ZIP entries).
- MEB 47 in `NODE_MAPPING.csv`: 20 unique (temperature,RunMode) targets, from three selected main-account projects.
- Embedded earlier recovery candidates: 11; **not added again** to campaign totals.
- Executed PP SDE geometry: all selected grid `pp3322_dvs.cmd`, depth `(define DBCAT_nm 47)`, and normalized SDE SHA-256 `f81d0ce4cb2476f30b91c5e7f8a0d304240e39e234643c46ef0d85b6dbe8660b`, matched previous 40/41 nm SDE templates after depth substitution.
- Selected PP SDevice decks: each normalized SDevice template matched the previous 40 nm parent per mode (0/1/5/6/7); no geometry, Hurkx, WF, bias, or nominal model retuning.
- SWB `gtree.dat`: 4 levels, correct parent/temperature/depth and project-qualified node-to-mesh mapping verified; original grid TDR binary equivalence is not asserted.
- All 20 selected cases had source/log/PLT files. 19 had full target bias and acceptable IVSN protocol; 1 had premature Newton/MinStep termination.
- 368.15 K Mode 6: `CMP_3D_Temp_36-48_Copy1_Copy/n3346_des.plt` (accepted). Mode 7: `CMP_3D_Temp_36-48_Copy/IVSN_0P8_TO_1P0_n3347_ivsn_sys.plt` (accepted 101 points). Mode 5: `CMP_3D_Temp_36-48_Copy1/n3345_des.plt` (FAILED; 109 samples, final VG 0 V, VD 1.189584347 V).
- Accepted native PLT SHA-256 and identity for each of the 19 passing cases are in `selected_cases_286.csv`; incomplete 47/M5 remains in `node_qc_700.csv` and `remaining_reruns.csv`.
- Historical 34-depth master is immutable. The new 35-depth master has 695/700 completed cases; original 47 nm ZIP and curve deltas remain as external QC package.
