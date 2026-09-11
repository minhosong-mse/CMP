# 3D-Sun-B0 SDevice decks

These decks belong to the dedicated literature-consistent 3-D baseline reconstruction used for `FB-BASELINE-01`.

## Decks

| Deck | Purpose | Status |
|---|---|---|
| `G0_bringup.cmd` | 300 K, Vd=0.05 V, Vg 0→1.2 V numerical / turn-on sanity run | PASS |
| `G1_highVd_full_idvg.cmd` | 300 K, Vd=1.2 V, Vg 0→2.0 V high-drain baseline comparison | PASS |
| `G2_lowVd_full_idvg.cmd` | 300 K, Vd=0.05 V, Vg 0→2.0 V low-drain curve for consistent DIBL extraction | launched; result pending ingestion |

SWB custom parameters are not required for these current decks; the bias, temperature, work function, and thread count are hard-coded, while `@tdr@`, `@plot@`, `@tdrdat@`, and `@log@` are SWB placeholders.

## Claim boundary

The current model deck uses `PhuMob`, `Enormal(Lombardi)`, high-field saturation with `GradQuasiFermi`, and `Band2Band(Hurkx)`. The Sun et al. paper names Philips unified mobility, Lombardi, Canali velocity saturation, and Hurkx tunneling. The T-2022.03 run log reports the present high-field implementation as Caughey-Thomas saturation with gradient quasi-Fermi potential; therefore this directory does **not** claim that the paper's Canali implementation has already been reproduced exactly.

## Upstream geometry / mesh source

The final F1 SDE build **checkpoint summary** is stored at:

- `data/baseline_3d_sun_b0/f1_sde_build_summary.txt`

The exact final SDE source command file itself was not available as a standalone uploaded artifact during this repository audit, so it is **not reconstructed from the execution log and presented as exact source**. Add the original SDE source file later when exported from the Sentaurus workspace.

Repository convention for this baseline follows the existing CMP pattern: keep executable decks, CSV results, compact summaries, and curated figures/docs in GitHub; full Sentaurus logs and native `.plt` files are workspace/debug evidence unless a later reproducibility need specifically requires them.

Primary documentation:

- `docs/evidence/feedback_baseline_3d_reconstruction_20260911.md`
- `docs/evidence/baseline_3d_evidence_manifest_20260912.md`
