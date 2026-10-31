# 2026-10-31 3D full extraction utilities (25 depths × 7 modes)

This folder preserves the exact V5.1 recovery / full-data extraction utilities used for the audit. In the original execution, V4 produced native ROI, lines and logs; V5 recovered the incorrectly scaled native signed BTBT integral without changing the upstream SDevice TDR. `repair_v4_spatial_results.py` is historical recovery logic, not a new SDevice simulation command. Read the sibling data package README for limitations.

Input and output paths reference the user's external Linux project and must be updated to local context before rerun. Public GitHub does not contain native TDR/PLT, full logs or historical raw_rows.csv. Review the official Sentaurus Visual T-2022.03 manual for any new syntax/model changes.
