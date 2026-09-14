# 3D-Sun-B0 / baseline-fidelity SDevice decks

These decks support `FB-BASELINE-01` and the final simplified-2D-vs-3-D fidelity check.

## Decks

| Deck | Purpose | Status |
|---|---|---|
| `G0_bringup.cmd` | 300 K, Vd=0.05 V, Vg 0→1.2 V numerical / turn-on sanity run | PASS |
| `G1_highVd_full_idvg.cmd` | 300 K, Vd=1.2 V, Vg 0→2.0 V 3-D high-drain baseline curve | PASS |
| `G2_lowVd_full_idvg.cmd` | 300 K, Vd=0.05 V, Vg 0→2.0 V 3-D low-drain baseline curve | PASS |
| `B0_2D_parity_highVd.cmd` | simplified 2-D B0 rerun with the 3-D baseline physics family at Vd=1.2 V | PASS |
| `B0_2D_parity_lowVd.cmd` | simplified 2-D B0 rerun with the 3-D baseline physics family at Vd=0.05 V | PASS |

No additional custom SWB parameters are required by these SDevice decks. `@tdr@`, `@plot@`, `@tdrdat@`, and `@log@` are SWB placeholders.

For the 2-D parity runs, the upstream Run-0 SDE branch keeps the existing:

```text
MEB_Depth = 0.036
```

with no additional SDevice parameter.

## Common 3-D / parity physics family

```text
Temperature = 300 K
Fermi
PhuMob
Enormal(Lombardi)
eHighFieldSaturation(GradQuasiFermi)
hHighFieldSaturation(GradQuasiFermi)
Band2Band(Hurkx)
Gate WF = 4.8 eV
```

This is consistent at model-family / activation level with the paper wording of Philips unified mobility, Lombardi, Canali velocity saturation, and Hurkx tunneling. Exact paper parameter overrides are not published and are not claimed to be reproduced.

## 3-D electrical checkpoint

```text
Vth_high @ Vd=1.20 V = 1.14659 V
Vth_low  @ Vd=0.05 V = 1.20610 V
SS_high                 ≈ 91.17 mV/dec
SS_low                  ≈ 92.83 mV/dec
reconstruction DIBL     ≈ 51.75 mV/V
```

The paper reports `Vth=0.656 V`, `SS=76 mV/dec`, `Ion/Ioff=3.4e10`, and `DIBL=23.6 mV/V`. Exact electrical reproduction is therefore not claimed.

## 2-D parity checkpoint

Using the original simplified 2-D B0 geometry and the same main SDevice physics / bias family:

```text
Vth_high,2D = 1.51879 V
SS_high,2D  ≈ 112.20 mV/dec
SS_low,2D   ≈ 114.29 mV/dec
```

The low-Vd 2-D curve does not reach the paper-style threshold criterion by `Vg=2.0 V`, so only a conservative lower bound is reported under the same reconstruction drain-bias pair:

```text
DIBL_2D > 418.4 mV/V
```

The very-low-current 2-D off-state region contains sign changes near the numerical floor, so a formal 2-D Ion/Ioff is not frozen from this parity sweep.

## Final modeling role

The final baseline-fidelity conclusion is:

> the simplified 2-D B0 is not an absolute reproduction of the literature-oriented 3-D BCAT, but remains useful as a controlled relative-trend / design-space model. Final design conclusions should be checked using selected-point 3-D validation.

The 3-D reconstruction itself remains a **literature-consistent reconstruction / validation anchor**, not an exact reverse-engineered Sun-2022 deck.

## Evidence

- `data/baseline_3d_sun_b0/b0_2d_parity_highvd.csv`
- `data/baseline_3d_sun_b0/b0_2d_parity_lowvd.csv`
- `data/baseline_3d_sun_b0/baseline_2d_3d_fidelity_summary_20260914.csv`
- `data/baseline_3d_sun_b0/f1_mesh_convergence_summary_20260914.csv`
- `docs/evidence/feedback_baseline_closeout_20260914.md`
- `docs/evidence/baseline_3d_evidence_manifest_20260912.md`

Repository convention remains unchanged: keep executable / controlled source decks, validated CSVs, compact summaries, curated figures, and evidence docs in GitHub. Full Sentaurus logs and native `.plt` files remain workspace/debug evidence unless specifically needed later.
