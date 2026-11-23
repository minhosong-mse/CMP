# Source manifest — 41 nm increment, 2026-11-23

Original SWB ZIP is retained external to GitHub per CMP D-005; only extracted numeric/QC data, source hashes and code are versioned.

| Native source archive | SHA-256 | Recorded scope |
|---|---|---|
| `CMP_OTHER_MEB41_NOV23_20261123_185916.zip` | `d4b91404236eca70910c46991aa5438302007b8dc266d9602f07b0f7ea0b46a3` | OTHER account, project `CMP_final_Copy2`, MEB 41 nm, four temperatures × modes 0/1/5/6/7, selected grid node 132 |

- All **20** newly selected nodes have an executed `pp*_des.cmd`, `pp132_dvs.cmd`, SWB hierarchy, log/status, finite native PLT, required terminal bias and valid 101-point IVSN sampling at mode 7.
- Executed PP SDE normalized for depth/node identity matches the 40 nm main-account reference, and all five per-mode PP SDevice templates match after only temperature/identifying substitutions. These checks do **not** prove identical binary 3D mesh across depths or accounts.
- The ZIP contains **11 historic R1 recovery candidates** already selected and documented in the earlier Nov-23 archive. They are deliberately **not re-added** as new results. Other unexecuted/copy alternatives in candidate lists are not new physical experiments.
- `meb41_node_qc.csv` contains executed identifiers and SHA-256 of each accepted PLT and executed PP CMD/SDE.
- Parent is the immutable [33-depth manifest](../3d_meb_jedec_33depth_20261123/SOURCE_MANIFEST.md). New canonical node QC = previous 660 + 20 new; new canonical metric rows = previous 132 + 4 new. Historical 11 R1 recovered cases remain unchanged. Exactly 4 unresolved 358.15 K cases remain: 27/M1, 40/M1, 46/M1, 58/M7.
- 233.15 K low-current KCL maximum relative residual at MEB 41 nm is `0.04010767010484561`; record as warning while keeping terminal-bias pass.

External raw PLT/TDR/log and mesh must be rechecked for future scientific claims. `t_est` is based on assumed constant 10 fF, not true 1T1C retention; Hurkx ON−OFF is a model-dependent signed proxy.
