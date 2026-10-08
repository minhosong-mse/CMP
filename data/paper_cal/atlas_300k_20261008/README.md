# 2026-10-08 PAPER-CAL 300 K MEB Atlas evidence

Status: **DATA-VALIDATED; FZ-C exact-parent/lineage bridge OPEN**.

## Source and integrity

- Public source archive: [CMP_MEB_ATLAS_300K_EVIDENCE_PUBLIC.zip](./CMP_MEB_ATLAS_300K_EVIDENCE_PUBLIC.zip)
- SHA256 of public ZIP: `7707a2ed1375a0fa193c3bb94bce9e55ecbc41e1aa2eb0f2fafa7c7d09a401ea`
- Original user-provided ZIP SHA256: `4e1fb4180da2a3bd18ab1883521d48cf90d0a6f2167d7cc2eab46e839c11b5bd`
- Archive contains **unchanged numeric bytes** for all **90 raw summary CSV + 105 curve CSV**, source manifest, collector QC, and provisional master. Only absolute TCAD-home paths in metadata/source manifest were redacted for public repository hygiene.
- Independently recomputed master: [MEB_300K_ATLAS_MASTER_VALIDATED.csv](./processed/MEB_300K_ATLAS_MASTER_VALIDATED.csv).
- Independent audit: [QC text](./qc/independent_qc_report.txt), [QC JSON](./qc/summary.json).
- Reproduction script: [validate_paper_cal_meb_atlas_300k.py](../../../code/scripts/analysis/validate_paper_cal_meb_atlas_300k.py); run with `--archive <public_zip_path> --out <output_folder>`.
- Human analysis: [Interim evidence review](../../../docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md).
- Figures: `assets/images/paper_cal/atlas_300k/01..10.svg`.

## Measured scope

MEB nm: `31/33/36/39/41/42/43/44/45/46/47/48/49/50/51`.
Working mesh: Level 2. T=300 K. GIDL terminal endpoint: VD=1.2 V, VG=-0.7 V. Cgd AC: 1 MHz, BTBT OFF. DC: Vd=0.05/1.2 V.

## Interpretation constraints

- Current 15-point atlas establishes **within-branch** behavior and a signed ON/OFF–BTBT-integral consistency check.
- Does **not** prove identical physical/numerical lineage with frozen 2026-10-05 C7_4/FZ-C parent; preserve historical data and do not label this an official mesh-only re-freeze.
- OFF-current mechanism and PAPER-CAL 1T1C retention remain unvalidated.
- No optimum, production, refresh, 3D parity, physical retention, or exact Cgd→E→GIDL causality claim is established.
