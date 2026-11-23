# 2026-11-23 — 34-depth BCAT 3D MEB DOE: other-account 41 nm increment

**PAUSED / CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** Native user-provided SWB export `CMP_OTHER_MEB41_NOV23_20261123_185916.zip` was checked as an append-only extension of the previous 33-depth snapshot, without executing Sentaurus or retuning geometry/mesh/physics.

## Verified new work

- Added **MEB 41 nm** (`CMP_final_Copy2`, grid PP `pp132_dvs.cmd`): 4 temperatures × 5 modes = **20/20** uniquely mapped, endpoint-complete, normal terminal-log/status cases. Source tree, executed `pp*_des.cmd`, SDE depth, grid/T/mode consistency, physical Hurkx branch, finite native PLT, and IVSN 101-point 0.8–1.0 V/sign conditions checked.
- Executed PP SDE and per-mode SDevice normalized templates agree with main-account MEB 40 nm reference. Native mesh binary equality still not established.
- Extracted: isolated 41 nm `meb41_node_qc.csv`, `meb41_six_metrics.csv`, 1,716 DC curve points, 404 IVSN points, with selected native SHA-256 hashes and [source manifest](../../data/3d_meb_jedec_34depth_20261123/SOURCE_MANIFEST.md).
- Cumulative: **34/37 MEB**, **676/680** exported numeric PASS, **676/740** overall, **132/136** fully five-mode MEB × T rows, 34/34 fully 300 K rows. Prior 11 R1 recoveries kept unchanged and not double-counted.
- Updated cumulative [node QC 680](../../data/3d_meb_jedec_34depth_20261123/node_qc_680.csv), [six metrics 136](../../data/3d_meb_jedec_34depth_20261123/six_metrics_136_conditions.csv), selection list 267, depth statuses and existing rerun list. All historical checkpoints are immutable.

## Exact remaining work

- **Not exported:** MEB **35, 47, 53 nm** × four T × five RunModes = **60** additional cases.
- **Exported but not converged to requested terminal bias:** **4** at 358.15 K: OTHER 27/M1 n409; MAIN 40/M1 n3156, 46/M1 n3312, 58/M7 n3315.
- Total outstanding = **64/740** target endpoints. Isolated numerical-only R1 reruns for these four are prepared but no new successful recovery evidence has been received.

## Limits and guardrails

41 nm/233.15 K mode-7 relative-KCL maximum residual `4.010767%` exceeds 1% warning; cumulative cold IVSN relative-KCL warnings **23**. This is a numerical endpoint PASS with a low-current interpretation caveat. `t_est` uses an *assumed* constant 10 fF and is not measured physical retention; signed Hurkx ON−OFF remains a proxy, not pure GIDL; SRH omitted; native mesh equivalence and process/production optimum not demonstrated. No changes to root README or historical data, no new model freeze.

**Next first action:** receive exported 35/47/53 nm and four isolated R1 run ZIPs, verify native endpoints/logs/PP SDE/PLT, then assemble final 37-depth 740-case master and perform temperature-dependent provisional design-range screening.
