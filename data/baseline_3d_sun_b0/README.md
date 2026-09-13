# 3D-Sun-B0 data / evidence index

This directory stores repository-safe evidence for the dedicated `FB-BASELINE-01` reconstruction.

## Directly browsable data

- `g0_idvg_lowvd_0p05V_to_1p2V.csv` — G0 low-Vd ID–VG bring-up curve
- `g1_idvg_highvd_1p2V_to_2p0V.csv` — G1 high-Vd ID–VG curve
- `g2_idvg_lowvd_0p05V_to_2p0V.csv` — G2 full low-Vd ID–VG curve used for consistent low/high threshold comparison
- `junction_source_C1.csv` — source vertical net-doping cut
- `junction_drain_C2.csv` — drain vertical net-doping cut

## Compact execution / validation evidence

- `f1_sde_build_summary.txt` — validated F1 SDE build / contact / doping / mesh checkpoint
- `g0_sdevice_run_summary.txt` — G0 model / sweep / completion checkpoint
- `g1_sdevice_run_summary.txt` — G1 model / sweep / completion checkpoint
- `g2_curve_validation_summary.txt` — returned G2 curve validation and provisional low/high-Vd threshold / DIBL extraction

Repository convention follows the existing CMP pattern: executable decks, validated CSV data, compact summaries, curated figures, and feedback/evidence documentation are committed by default. Full Sentaurus logs, native `.plt` files, temporary screenshots, and failed attempts remain chat/workspace evidence unless a later diagnosis or reproducibility requirement specifically needs them.

## Current G2 checkpoint

Returned G2 curve:

```text
T  = 300 K
Vd = 0.05 V
Vg = 0 → 2.0 V
Id @ Vg=2.0 V = 2.48569e-6 A
```

Using the same provisional constant-current convention currently used for G1 (`W=Wfin=17 nm`, `L=Lgate=20 nm`, `Icrit=8.5e-8 A`) and log-current interpolation:

```text
Vth_low  = 1.20610 V
Vth_high = 1.14659 V
reconstruction-defined DIBL = 51.75 mV/V
```

The paper nominal DIBL is 23.6 mV/V, but the exact low/high drain-bias pair used in the paper is not explicitly published in the text. Therefore the present DIBL comparison remains **provisional / reconstruction-defined**, not a strict paper-equivalent extraction.

## Related code / docs

- `code/sdevice/baseline_3d_sun_b0/`
- `docs/evidence/feedback_baseline_3d_reconstruction_20260911.md`
- `docs/evidence/baseline_3d_evidence_manifest_20260912.md`
- `assets/images/feedback/20260911_baseline/00_baseline_visual_contact_sheet.svg`

One source artifact still worth adding later is the original final F1 SDE source CMD exported directly from the Sentaurus workspace. Do not reconstruct it from a log and label it as exact source.
