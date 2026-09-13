# R6.5 Mesh Feedback — Image / Figure Index

Scope: `36 / 41 / 43 / 45 / 47 / 48 / 49 / 51 nm`, 300 K, `Mesh_Code=3`.

## Presentation-ready figures committed here

- `01_r65_xhot_vs_meb.svg` — full R6.5 hotspot-X motion vs MEB
- `02_r65_hotspot_roi_coverage.svg` — all eight hotspots plotted inside the common ROI
- `03_r65_btbtmax_vs_meb.svg` — BTBTmax trend over the full R6.5 MEB sweep

These SVGs are generated directly from the validated numeric extraction table and can be inserted into slides without raster-quality loss.

## Raw screenshot archive

The original Sentaurus screenshots were captured for all eight R6.5 MEB cases with three evidence types per MEB:

```text
36nm_btbt_hotspot.png
36nm_mesh_full.png
36nm_mesh_zoom.png
41nm_btbt_hotspot.png
41nm_mesh_full.png
41nm_mesh_zoom.png
43nm_btbt_hotspot.png
43nm_mesh_full.png
43nm_mesh_zoom.png
45nm_btbt_hotspot.png
45nm_mesh_full.png
45nm_mesh_zoom.png
47nm_btbt_hotspot.png
47nm_mesh_full.png
47nm_mesh_zoom.png
48nm_btbt_hotspot.png
48nm_mesh_full.png
48nm_mesh_zoom.png
49nm_btbt_hotspot.png
49nm_mesh_full.png
49nm_mesh_zoom.png
51nm_btbt_hotspot.png
51nm_mesh_full.png
51nm_mesh_zoom.png
```

Exact source-node / chat-file provenance for these 24 originals is recorded in:

- `data/run06_5/feedback_mesh_20260913/screenshot_manifest.csv`

**Archive note:** the current GitHub connector supports text/SVG repository writes but does not expose a direct local-binary-file upload parameter for these PNG attachments. Therefore the 24 exact PNG binaries are retained in the project handoff package outside this directory rather than being falsely represented as committed files. The numeric tables, provenance manifest, validation document, and vector presentation figures are committed here.

## Numeric extraction / validation tables

- `data/run06_5/feedback_mesh_20260913/r65_mesh_raw_extract.csv`
- `data/run06_5/feedback_mesh_20260913/r65_mesh_hotspot_coverage_summary.csv`

## Scientific interpretation

- `docs/evidence/feedback_mesh_run65_full_validation_20260913.md`
- `docs/evidence/feedback_mesh_presentation_extract_20260913.md`

Presentation rule: use the committed SVGs for trend / ROI figures and use the exact original screenshot package whenever a raw Sentaurus view is required.
