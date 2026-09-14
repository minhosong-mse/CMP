# 3D-Sun-B0 data / evidence index

This directory stores repository-safe evidence for `FB-BASELINE-01`.

Current status: **baseline fidelity feedback resolved at model-fidelity level (2026-09-14)**.

The conclusion is not that Sun et al. was exactly reproduced. The conclusion is that the literature-consistent 3-D reconstruction is structurally defensible and DC-mesh-stable, while the existing simplified 2-D B0 does not reproduce its absolute electrical behavior and should therefore be used as a relative-trend / design-space model.

## Core 3-D data

- `junction_source_C1.csv` — source vertical net-doping cut; nominal junction ~48 nm
- `junction_drain_C2.csv` — drain vertical net-doping cut; nominal junction ~48 nm
- `g0_idvg_lowvd_0p05V_to_1p2V.csv` — G0 low-Vd bring-up curve
- `g1_idvg_highvd_1p2V_to_2p0V.csv` — G1 high-Vd ID-VG curve
- `g2_idvg_lowvd_0p05V_to_2p0V.csv` — G2 full low-Vd ID-VG curve
- `extraction_width_sensitivity_20260913.csv` — threshold-width interpretation check

## Reconstruction sensitivity data

- `h1_idvg_highvd_lgate_outer20nm.csv` — H1 alternative Lgate-mapping curve
- `h1_lgate_mapping_validation_summary.txt` — H1 structural/electrical decision
- `h2_gaussfactor0p8_idvg_highvd.csv` — H2 lateral-Gaussian sensitivity curve
- `h1_h2_sensitivity_summary_20260913.csv` — nominal/H1/H2 extracted comparison

H1 and H2 were both rejected as explanations of the large paper/reconstruction electrical mismatch.

## Electrical mesh-convergence data

- `f1c_coarse_idvg_highvd.csv` — Coarse high-Vd ID-VG
- `g1_idvg_highvd_1p2V_to_2p0V.csv` — Nominal reference
- `f1f_fine_idvg_highvd.csv` — Fine high-Vd ID-VG
- `f1_mesh_convergence_summary_20260914.csv` — Points/Elements/Vth/SS/Id comparison

Key result:

```text
Nominal -> Fine
Delta Vth     ≈ -1.18 mV
Delta SS      ≈ -0.071 mV/dec
Delta Id(2 V) ≈ +0.046%
```

Therefore F1 is frozen for the present **DC ID-VG / Vth / SS baseline-fidelity comparison**. This does not extend to a universal convergence claim for all local E-field / BTBT quantities.

## Simplified 2-D B0 parity data

The original Run-0 electrical sanity deck was not used directly because its physics and sweep conditions differed from the stabilized 3-D baseline.

Parity reruns use the original simplified 2-D geometry (`MEB_Depth=0.036`) with the same main SDevice physics family and high/low drain-bias sweep used by the 3-D reconstruction.

- `b0_2d_parity_highvd.csv` — `Vd=1.2 V`, `Vg=0->2.0 V`
- `b0_2d_parity_lowvd.csv` — `Vd=0.05 V`, `Vg=0->2.0 V`
- `baseline_2d_3d_fidelity_summary_20260914.csv` — final paper / 3-D / 2-D metric comparison

Key comparison:

```text
                         2-D B0            3D-Sun-B0
Vth high-Vd              1.51879 V         1.14659 V
SS high-Vd               112.20            91.17 mV/dec
SS low-Vd                114.29            92.83 mV/dec
Id @ 2 V, high-Vd        4.936e-5 A/um     6.255e-4 A/um equivalent
Id @ 2 V, low-Vd         3.741e-6 A/um     1.462e-4 A/um equivalent
```

The 2-D low-Vd sweep does not reach the paper-style threshold criterion by `Vg=2.0 V`; under the same reconstruction drain-bias pair the conservative result is:

```text
DIBL_2D > 418.4 mV/V
```

No formal 2-D Ion/Ioff is frozen because the very-low-current 2-D region contains sign changes near the numerical floor.

## Final workflow decision

Use:

```text
2-D -> broad MEB / temperature / process-window exploration
3-D -> selected-point validation of the final design conclusion
```

The 2-D model is a **controlled comparative model**, not an absolute literature-reproduction model.

The 3-D model is a **literature-consistent reconstruction / validation anchor**, not an exact reverse-engineered Sun-2022 deck.

After the final effective MEB range is selected, rerun only a small representative set in 3-D (for example baseline / main candidate / boundary-challenger) to verify that the key 2-D trend survives in 3-D.

## Evidence manifest

- `baseline_feedback_manifest_20260914.csv` — compact index of baseline source/data/doc artifacts
- `docs/evidence/feedback_baseline_closeout_20260914.md` — final scientific close-out and claim boundaries
- `docs/evidence/baseline_3d_evidence_manifest_20260912.md` — synchronized full baseline manifest

## Related source decks

- `code/sde/baseline_3d_sun_b0/F1_nominal.cmd`
- `code/sde/baseline_3d_sun_b0/VARIANTS.md`
- `code/sdevice/baseline_3d_sun_b0/G0_bringup.cmd`
- `code/sdevice/baseline_3d_sun_b0/G1_highVd_full_idvg.cmd`
- `code/sdevice/baseline_3d_sun_b0/G2_lowVd_full_idvg.cmd`
- `code/sdevice/baseline_3d_sun_b0/B0_2D_parity_highVd.cmd`
- `code/sdevice/baseline_3d_sun_b0/B0_2D_parity_lowVd.cmd`

Repository convention remains unchanged: commit executable/controlled decks, validated CSV data, compact summaries, curated figures, and evidence documentation. Full Sentaurus logs, native `.plt` files, temporary screenshots, and failed attempts remain workspace/debug evidence unless a later diagnosis specifically requires them.
