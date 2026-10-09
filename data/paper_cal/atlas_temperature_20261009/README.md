# 36nm temperature Atlas source and processed checkpoint (2026-10-09)

- `processed/MEB36_4TEMP_INTEGRATED_VALIDATED_DC.csv`: four temperature rows including DC (source + curve audited), prior GIDL ON/OFF/spatial, raw AC Cgd. It is **36 nm only**; it is not an all-depth finished temperature dataset.
- `raw_dc36/*.csv`: exact six one-row DC summary extracts from the source upload. GIDL/Cgd raw evidence and the six long DC Id–Vg curve CSVs are retained separately in the user's original local evidence and archived chat package.
- `qc/DC36_INDEPENDENT_QC.json`: SHA256, geometry/temperature mapping, count, scientific boundaries.
- Full reproducible local bundle in chat: `CMP_DC36_COMPLETE_RESEARCH_BUNDLE_20261009.zip`. Original DC user-upload ZIP SHA256: `e680122bcfca924bf60f7320efd39f685e2289bc8b89f963938ccdd5319b8262`.
- 300 K full 15-depth Atlas remains unchanged. The complete new-T 60-row DC table and all-source archival are **not** claimed here. Do not conflate GIDL total Id and DC Ioff.

Read `docs/progress/paper_cal_36nm_temperature_dc_qc_20261009.md` for data, check definitions, and next action.
