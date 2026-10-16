# 2026-10-16 D_BCAT L1 2D Paper-Figure Reconstruction Checkpoint

This is **not** a new frozen production baseline. See [evidence and scientific interpretation](../../docs/progress/dbcat_paper_compare_l1_hurkx_nonlocal_20261016.md).

## Actual execution

- 300K, 2D PAPER-CAL-derived L1, 24/36/48 nm, gate WF4.8eV/Qf2.55e12/GCS2.3/GDB25nm.
- NonlocalPath: IDVG 3 + IDVD 9 completed, 3,612 source points.
- Hurkx: IDVG 36/48 only + IDVD all nine completed, 3,011 source points. Hurkx IDVG 24 nm is **failed, deliberately excluded**.
- [terminal_checkpoints.csv](terminal_checkpoints.csv): 38 actual measured bias/current checkpoints from completed collector PLT data; not a curve substitute.
- [idvd_vd2_meb_comparison.svg](../../assets/images/paper_cal/dbcat_20261016/idvd_vd2_meb_comparison.svg): **CMP only** at VD2, model/depth dependence of 3 fixed VG endpoints.
- [plot_dbcat_figure_2d_20261016.py](../../code/analysis/plot_dbcat_figure_2d_20261016.py): plot full curves from supplied extraction CSV once local evidence ZIPs are restored.
- Source ZIPs **not checked into this commit**: original PLT, PP-CMD, logs, TDR, full curve CSV, and user chat attachments remain external to GitHub; SHA-256 in progress report. Do not imply GitHub hosts the complete sources.
- Paper IDVG/IDVD figures from Sun et al 2022 are not available as numeric raw points. Earlier visual hand-anchor CSVs and interpolated preview curves are **not suitable for a quantitative paper-fit claim** and deliberately excluded from this folder.

## Full extracted CSV file hashes

| CSV | rows | SHA-256 |
|---|---:|---|
| `NONLOCAL_IDVG_24_36_48nm.csv` | 1803 | `41b02029c2f877e19cb8235f1d4ae49c77af7b9905ec4ff4e24b767bd4d38f8b` |
| `NONLOCAL_IDVD_9CURVES.csv` | 1809 | `4366ce2fe79e9f207a57f0752e56242e6073068d3117625ad035f3e88f38dc00` |
| `HURKX_IDVG_36_48nm.csv` | 1202 | `8f239b1bf76a1d36603d787572c1a42d45fe1e81405a26e8982c4ac7c3b399ea` |
| `HURKX_IDVD_9CURVES.csv` | 1809 | `862650581594bf96978ca54025e396773ac085e1970ec35fe55dad184a93363e` |

## Status

**CMP-EXECUTED terminal/source-QC; PROVISIONAL 2D model-to-paper validity; 3D bridge PROPOSED, not adopted.** Keep prior Run Sheet / HANDOFF freezes.
