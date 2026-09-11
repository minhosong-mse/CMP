# 3D-Sun-B0 data / evidence index

This directory stores repository-safe evidence for the dedicated `FB-BASELINE-01` reconstruction.

## Directly browsable data

- `g0_idvg_lowvd_0p05V_to_1p2V.csv` — G0 low-Vd ID–VG curve
- `g1_idvg_highvd_1p2V_to_2p0V.csv` — G1 high-Vd ID–VG curve
- `junction_source_C1.csv` — source vertical net-doping cut
- `junction_drain_C2.csv` — drain vertical net-doping cut

## Compact execution evidence

- `f1_sde_build_summary.txt` — validated F1 SDE build / contact / doping / mesh checkpoint
- `g0_sdevice_run_summary.txt` — G0 model / sweep / completion checkpoint
- `g1_sdevice_run_summary.txt` — G1 model / sweep / completion checkpoint

The full original SDE/SDevice logs and native `.plt` files remain preserved in the conversation/workspace evidence. During this repository audit, large binary/archive transfers through the connector were not retained as authoritative artifacts, so incomplete archive attempts were removed rather than left in the repository. The CSV curves and compact audit-relevant run summaries are the authoritative GitHub evidence at this checkpoint.

## G2

G2 low-Vd full ID–VG was launched but its completed result has not yet been returned and validated. Do not add a DIBL value or mark G2 PASS until the completed log / curve data are ingested.

## Related code / docs

- `code/sdevice/baseline_3d_sun_b0/`
- `docs/evidence/feedback_baseline_3d_reconstruction_20260911.md`
- `docs/evidence/baseline_3d_evidence_manifest_20260912.md`
- `assets/images/feedback/20260911_baseline/00_baseline_visual_contact_sheet.svg`
