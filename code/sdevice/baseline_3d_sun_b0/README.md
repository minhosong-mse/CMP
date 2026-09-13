# 3D-Sun-B0 SDevice decks

These decks belong to the dedicated literature-consistent 3-D baseline reconstruction used for `FB-BASELINE-01`.

## Decks

| Deck | Purpose | Status |
|---|---|---|
| `G0_bringup.cmd` | 300 K, Vd=0.05 V, Vg 0→1.2 V numerical / turn-on sanity run | PASS |
| `G1_highVd_full_idvg.cmd` | 300 K, Vd=1.2 V, Vg 0→2.0 V high-drain baseline comparison | PASS |
| `G2_lowVd_full_idvg.cmd` | 300 K, Vd=0.05 V, Vg 0→2.0 V low-drain curve for consistent DIBL extraction | PASS — returned curve ingested |

SWB custom parameters are not required for these current decks; the bias, temperature, work function, and thread count are hard-coded, while `@tdr@`, `@plot@`, `@tdrdat@`, and `@log@` are SWB placeholders.

## G2 extraction checkpoint

The returned G2 dataset reaches the full `Vg=2.0 V` endpoint and was ingested as:

- `data/baseline_3d_sun_b0/g2_idvg_lowvd_0p05V_to_2p0V.csv`
- `data/baseline_3d_sun_b0/g2_curve_validation_summary.txt`

Using the same **provisional** threshold convention already used for G1 (`W=Wfin=17 nm`, `L=Lgate=20 nm`) gives a reconstruction-defined DIBL of approximately `51.75 mV/V`. The paper reports `23.6 mV/V`, but its exact low/high drain-bias pair is not explicitly stated in the text, so this is not yet claimed as a strict paper-equivalent DIBL extraction.

## Post-G2 extraction / physics verification

Detailed checkpoint:

- `docs/evidence/baseline_3d_extraction_physics_verification_20260913.md`
- `data/baseline_3d_sun_b0/extraction_width_sensitivity_20260913.csv`
- `assets/images/feedback/20260911_baseline/01_g1_g2_idvg_comparison.svg`

Two issues were checked before modifying the reconstructed device:

1. **Threshold width convention:** using a larger saddle-fin width interpretation (`2Hfin + Wfin`) shifts the extracted Vth even higher. The current ~0.49 V Vth mismatch therefore cannot plausibly be explained by channel-width ambiguity alone.
2. **Canali / Caughey-Thomas wording:** Sentaurus documentation/training identifies its built-in velocity high-field saturation model as Canali while also describing the implementation in Caughey-Thomas terms. The present `eHighFieldSaturation(GradQuasiFermi)` / `hHighFieldSaturation(GradQuasiFermi)` activation is therefore treated as compatible with the Canali/Caughey-Thomas model family.

Exact paper-equivalent high-field parameterization is **not** claimed because Sun et al. do not publish their Sentaurus release or numerical model overrides.

## Current claim boundary

The current model deck uses `PhuMob`, `Enormal(Lombardi)`, carrier-specific high-field saturation with `GradQuasiFermi`, and `Band2Band(Hurkx)`. The Sun et al. paper names Philips unified mobility, Lombardi, Canali velocity saturation, and Hurkx tunneling.

Supported statement:

> The currently activated high-field model is consistent with the Sentaurus Canali/Caughey-Thomas model family. This resolves the earlier model-name mismatch concern at the model-family/activation level, but does not prove exact numerical parameter equivalence to the unpublished paper deck.

The electrical baseline still does not match the paper nominal metrics, so no exact-reproduction claim is made.

## Upstream geometry / mesh source

The final F1 SDE build **checkpoint summary** is stored at:

- `data/baseline_3d_sun_b0/f1_sde_build_summary.txt`

The exact final SDE source command file itself was not available as a standalone uploaded artifact during this repository audit, so it is **not reconstructed from the execution log and presented as exact source**.

The immediate prerequisite for the next controlled S/D reconstruction sensitivity study is therefore:

```text
export the original final F1 SDE source CMD from the Sentaurus workspace
```

Repository convention for this baseline follows the existing CMP pattern: keep executable decks, CSV results, compact summaries, and curated figures/docs in GitHub; full Sentaurus logs and native `.plt` files are workspace/debug evidence unless a later reproducibility need specifically requires them.

Primary documentation:

- `docs/evidence/feedback_baseline_3d_reconstruction_20260911.md`
- `docs/evidence/baseline_3d_evidence_manifest_20260912.md`
- `docs/evidence/baseline_3d_extraction_physics_verification_20260913.md`
