# 3D temperature140 extraction/review scripts (2026-11-09)

This folder holds the extraction scripts used for the **140-condition** 3D BCAT review. It is a read-only analysis of previously executed Linux SWB/SDevice/SVisual T-2022.03 outputs; not a new TCAD simulation or an endorsed model/mesh change. The canonical extracted data and scientific limitations are documented in [data/3d_meb_temp140_partial_20261109/README.md](../../../../data/3d_meb_temp140_partial_20261109/README.md).

- `cmp_3d_temp140_extract_multisource.py`: original two-source version, strict endpoint QC; stopped after 26 successful cases on native partial `36nm/380K/Mode5/n1979`.
- `cmp_3d_temp140_extract_recover.py`: successful same-campaign recovery, `--continue-on-incomplete` to flag two partial endpoints while reusing verified successful cases. **Do not use this switch to call incomplete cases PASS.**
- `build_cmp_temp140_review.py`: independent numerical review from the user-provided ZIP; derived 20-case analytical table and figures. Paths refer to the local review archive and may need adjustment.

Example read-only dry-run: `python3 cmp_3d_temp140_extract_recover.py --project <temperature-SWB> --baseline-project <300K-SWB> --out <new-directory>`.

Do **not** commit native TDR/PLT, proprietary/manual files, full SWB PP decks and SDevice solver logs under D-005; keep them externally. The scripts require original native SWB results and SVisual installation to extract spatial data anew.
