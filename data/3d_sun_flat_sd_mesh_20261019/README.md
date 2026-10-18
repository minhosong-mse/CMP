# Flat S/D nominal 3D BCAT: M1→M2D mesh QC (2026-10-18 to 2026-10-19)

**State: PAUSED / PROVISIONAL — SDE mesh quality not accepted. No production baseline freeze.**
Parent lineage: \`3D-Sun-SADDLE-V1\` (distinct from frozen 2D PAPER-CAL and historical 3D-Sun-B0).

- Full record: [2026-10-19 progress](../../docs/progress/3d_sun_saddle_v1_flat_sd_mesh_20261019.md).
- \`MESH_DIAGNOSTICS_M1_M2D.csv\`: independent analysis of **native TDR tetrahedron vertex connections**, deduplicating edges by vertex IDs. Blank values were not measured here.
- \`LOWVD_M1_M2A_NATIVE_QC.csv\`: low-Vd original Flat M1 and native 60-point M2A PLT extraction, both are executed data (no high-Vd validation for M2A).
- \`MESHCASE_0to6_PLANNED.csv\`: **unexecuted** SWB mesh-only experiments. The associated exact local source deck's Git blob SHA was verified; first test case 0 in separate project.
- \`SOURCE_SHA256.csv\`: externally retained native TDR/log files with sha256 (raw TDR files **are not committed**). Uploaded filename collision suffixes (1)/(2)/(3) are preserved in this manifest to avoid mismatching cases.
- \`code/sde/3d_sun_saddle_v1/flat_sd_mesh_20261019/\`: six exact Git-blob-SHA-verified source decks: Flat M1, M2A, M2B, M2C, M2D, planned MeshCase 0..6. **Source deck archival is not the same as independently proving equality to the executed preprocessed pp SDE deck** in every case. Actual node logs and TDR evidence are primary when available.
- \`code/scripts/analysis/audit_flat_sd_tdr_short_edges.py\`: native HDF5 TDR short-edge helper (reads only).

**Fixed dimensions:** ARgate=6, DBCAT=36 nm, JunctionRatio=0.4, Wfin=17 nm, RfilletFactor=1, Flat upper S/D, Hsaddle=48 nm, GaussFactor=0, Tox=5 nm, nominal GF0; no parameter fitting.
**M2B→M2D are SDE-only.** Neither an SDevice-field convergence conclusion nor a GIDL/retention/design-optimum claim.
**M2D content identity:** M2D's TDR *vertex coordinates and tetra connectivity* match M2C, even though whole-TDR file sha256 differs. CAD boundary geometry fixed across candidates as compared; binary file hashes can still differ due metadata.

**Next:** QA an independent SDE-only 7-case sweep (unrun) or directly inspect CAD curve/Boolean imprint; compare geometry, minimum edge, short-edge clusters, tetra quality and local resolution. Only after selecting two sufficiently resolved distinct grids: controlled LOWVD/DC spatial-E/BTBT and solver verification. The 0.1-nm short-edge threshold is a **diagnostic counter**, not a universal pass/fail physical specification.
