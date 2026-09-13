# 3D-Sun-B0 data / evidence index

This directory stores repository-safe evidence for the dedicated `FB-BASELINE-01` reconstruction.

## Directly browsable data

- `g0_idvg_lowvd_0p05V_to_1p2V.csv` — G0 low-Vd ID–VG bring-up curve
- `g1_idvg_highvd_1p2V_to_2p0V.csv` — G1 high-Vd ID–VG curve
- `g2_idvg_lowvd_0p05V_to_2p0V.csv` — G2 full low-Vd ID–VG curve
- `junction_source_C1.csv` — source vertical net-doping cut
- `junction_drain_C2.csv` — drain vertical net-doping cut
- `extraction_width_sensitivity_20260913.csv` — threshold-width interpretation check
- `h1_idvg_highvd_lgate_outer20nm.csv` — H1 alternative Lgate-mapping ID–VG curve
- `h2_gaussfactor0p8_idvg_highvd.csv` — H2 lateral-Gaussian sensitivity ID–VG curve
- `h1_h2_sensitivity_summary_20260913.csv` — nominal/H1/H2 metric comparison and decisions

## Compact execution / validation evidence

- `f1_sde_build_summary.txt` — validated nominal F1 SDE build / contact / doping / mesh checkpoint
- `g0_sdevice_run_summary.txt` — G0 model / sweep / completion checkpoint
- `g1_sdevice_run_summary.txt` — G1 model / sweep / completion checkpoint
- `g2_curve_validation_summary.txt` — G2 curve validation and reconstruction-defined low/high-Vd threshold / DIBL extraction
- `h1_lgate_mapping_validation_summary.txt` — H1 structural/electrical decision summary

Repository convention follows the existing CMP pattern: executable or controlled source definitions, validated CSV data, compact summaries, curated figures, and feedback/evidence documentation are committed by default. Full Sentaurus logs, native `.plt` files, temporary screenshots, and failed attempts remain chat/workspace evidence unless a later diagnosis or reproducibility requirement specifically needs them.

## Current electrical checkpoint

Nominal G1/G2 reconstruction:

```text
Vth_high @ Vd=1.20 V = 1.14659 V
Vth_low  @ Vd=0.05 V = 1.20610 V
SS_high                 ≈ 91.17 mV/dec
SS_low                  ≈ 92.83 mV/dec
reconstruction-defined DIBL = 51.75 mV/V
```

The paper nominal DIBL is 23.6 mV/V, but the exact low/high drain-bias pair used in the paper is not explicitly published in the text. Therefore the present DIBL comparison remains reconstruction-defined rather than a strict paper-equivalent extraction.

## H1 / H2 sensitivity checkpoint

```text
H1 Lgate mapping:
  Vth_high = 1.24248 V
  decision = reject as mismatch explanation

H2 GaussFactor 0.8:
  Vth_high = 1.14634 V
  decision = reject as main mismatch cause
```

The active next step is Coarse / Nominal / Fine electrical mesh convergence. F1C and F1F have been launched; their Points/Elements and ID–VG CSVs will be added after completion.

## Related code / docs

- `code/sde/baseline_3d_sun_b0/F1_nominal.cmd`
- `code/sde/baseline_3d_sun_b0/VARIANTS.md`
- `code/sdevice/baseline_3d_sun_b0/`
- `docs/evidence/feedback_baseline_3d_reconstruction_20260911.md`
- `docs/evidence/baseline_3d_evidence_manifest_20260912.md`
- `docs/evidence/baseline_3d_h1_h2_sensitivity_20260913.md`
- `docs/evidence/baseline_3d_mesh_convergence_plan_20260913.md`
- `assets/images/feedback/20260911_baseline/00_baseline_visual_contact_sheet.svg`
