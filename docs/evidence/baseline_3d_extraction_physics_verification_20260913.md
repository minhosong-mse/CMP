# 3D-Sun-B0 — extraction convention and high-field model verification

> Date: 2026-09-13  
> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Status: **verification checkpoint complete; reconstruction mismatch remains**

## 1. Purpose

After G1/G2 completion, two ambiguities were checked before changing the reconstructed device:

1. whether the large threshold-voltage mismatch could be mainly an artifact of the paper's `W/L` constant-current convention;
2. whether the SDevice log wording `Caughey-Thomas saturation model` means that the paper's stated Canali high-field mobility model was not actually activated.

No geometry, doping, work function, or mesh parameter was tuned during this verification.

## 2. Paper-explicit extraction facts

Sun et al. explicitly state:

```text
Vth criterion = 1e-7 A × W(channel width) / L(channel length)
ID-VG curves in Table 1: VDD = 1.2 V
reported drain current: normalized to channel width
baseline metrics:
  Vth      = 0.656 V
  SS       = 76 mV/dec
  Ion/Ioff = 3.4e10
  DIBL     = 23.6 mV/V
```

The paper does **not** explicitly publish:

- the exact numerical `W` convention used for the 3-D saddle-fin constant-current extraction;
- the exact low/high drain-voltage pair used to calculate the reported DIBL;
- numerical overrides for the high-field mobility model parameters.

Therefore strict paper-equivalent extraction cannot be claimed beyond the published information.

## 3. Threshold-width sensitivity check

The validated G1/G2 CSV curves were re-extracted with log-current interpolation at the constant-current crossing.

### 3.1 Primary reconstruction convention

Using the most direct interpretation:

```text
W = Wfin = 17 nm
L = Lgate = 20 nm
Icrit = 8.5e-8 A
```

results are:

```text
Vth_high @ Vd=1.20 V = 1.146593 V
Vth_low  @ Vd=0.05 V = 1.206103 V
DIBL_reconstruction  = 51.748 mV/V
```

### 3.2 Alternative larger saddle-fin width interpretation

As a sensitivity bound only, not as a paper definition, use a conventional three-surface fin-width expression:

```text
W = 2 Hfin + Wfin
  = 2×48 + 17
  = 113 nm

Icrit = 5.65e-7 A
```

This gives:

```text
Vth_high = 1.274101 V
Vth_low  = 1.365618 V
DIBL     = 79.580 mV/V
```

A larger width definition therefore shifts the extracted threshold **higher**, not toward the reported 0.656 V.

### 3.3 Can width convention explain the ~0.49 V threshold mismatch?

No.

At the paper nominal `Vg = 0.656 V`, the reconstructed G1 current is only approximately:

```text
Id(G1, Vg=0.656 V) ≈ 9.34e-13 A
```

If that current were forced to equal `1e-7 A × W/L` with `L=20 nm`, the implied width would be only about:

```text
W ≈ 1.87e-4 nm
```

which is not a physically meaningful channel-width interpretation for this structure.

Therefore:

> **The large Vth mismatch is not primarily an extraction-width-definition artifact.**

The exact paper width convention still matters for formal reporting, but it cannot plausibly account for the present threshold shift by itself.

Supporting data:

```text
data/baseline_3d_sun_b0/extraction_width_sensitivity_20260913.csv
assets/images/feedback/20260911_baseline/01_g1_g2_idvg_comparison.svg
```

## 4. DIBL extraction limitation

The reconstruction currently uses:

```text
Vd,low  = 0.05 V
Vd,high = 1.20 V
```

and obtains:

```text
DIBL_reconstruction ≈ 51.75 mV/V
```

The paper reports `23.6 mV/V`, but its text does not state the exact low/high drain-bias pair used for that reported number.

Therefore the current repository wording remains:

> **reconstruction-defined provisional DIBL = 51.75 mV/V**

and not a strict paper-equivalent DIBL error percentage.

## 5. Canali vs. Caughey-Thomas verification

The paper explicitly states that the Canali model was used for carrier velocity saturation.

The present SDevice run log reports:

```text
High-field mobility: Caughey-Thomas saturation model,
using gradient quasi-Fermi potential
```

At first this looked like a possible physics-model mismatch. The Sentaurus documentation/training evidence changes that interpretation:

- Sentaurus Training describes the built-in high-field saturation mobility as the **Canali** model and shows activation with `HighFieldSaturation(GradQuasiFermi)`.
- Sentaurus drift-diffusion examples use the carrier-specific `eHighFieldSaturation(GradQuasiFermi)` / `hHighFieldSaturation(GradQuasiFermi)` syntax used in this reconstruction.
- Sentaurus documentation also describes the default Canali implementation as being based on the **Caughey-Thomas** formulation.

Therefore:

> **The log label `Caughey-Thomas` is not evidence that the reconstruction selected a different high-field model family from the paper's Canali model.**

The previous `Canali vs. Caughey-Thomas` item is downgraded from a likely model mismatch to a **nomenclature / implementation-mapping issue that is resolved at model-family level**.

Remaining limitation:

- the paper does not provide its exact Sentaurus release or explicit high-field parameter overrides;
- therefore exact parameter-by-parameter equivalence still cannot be proven.

This is no longer treated as the leading explanation for the ~0.49 V threshold mismatch.

## 6. Revised mismatch diagnosis priority

After this verification, the likely mismatch causes are reprioritized.

### Lower priority now

- channel-width extraction convention as the main cause of the Vth mismatch;
- Canali/Caughey-Thomas naming as evidence of a different high-field model.

### Higher priority

1. unpublished **lateral S/D doping spread** — current reconstruction uses `GaussFactor=0.0`;
2. unpublished source/drain-side **3-D geometry / corner rounding**, which changes effective channel length;
3. exact paper extraction details for Ion/Ioff and DIBL;
4. electrical mesh convergence before any final baseline claim.

A later 2025 BCAT study from the same research group explicitly notes that rounding between the saddle fin and source/drain sidewall changes effective channel length, so geometry near that transition must remain a live reconstruction uncertainty rather than attributing the mismatch only to lateral doping.

## 7. Next simulation checkpoint

The next numerical test should be a **controlled source/drain reconstruction sensitivity study**, not work-function fitting.

Do not modify multiple items simultaneously.

Recommended order:

```text
Baseline: current GaussFactor = 0.0
→ first isolate lateral-doping sensitivity while keeping geometry fixed
→ then, only if needed, test source/drain-side rounding / effective-channel geometry
```

For the lateral-doping test, Sentaurus defines `Factor` as the lateral diffusion factor of the Gaussian analytical profile. Sentaurus training examples commonly use a nonzero factor such as `0.8`, but that value is an example and is **not** a Sun-2022 literature value.

Therefore any nonzero-factor run must be labeled a **sensitivity bracket**, not a calibration or reproduction parameter.

Before creating those SDE variants, archive/export the exact final F1 SDE source CMD from the current Sentaurus workspace so the baseline and each perturbation can be reproduced without reconstructing source code from logs.

## 8. Claim boundary after this checkpoint

Supported:

> The current 3-D reconstruction remains electrically mismatched to the Sun et al. nominal device. Threshold-width ambiguity cannot plausibly explain the large Vth shift, and the current high-field saturation setup is consistent with the Sentaurus Canali/Caughey-Thomas model family. The next reconstruction uncertainty to test is the unpublished source/drain lateral profile, followed by source/drain-side 3-D geometry if necessary.

Do not claim:

- exact paper-equivalent Vth extraction has been frozen;
- `51.75 mV/V` is the exact paper-equivalent DIBL;
- `GaussFactor=0.8` or any other nonzero factor is a literature value;
- lateral doping is already proven to be the mismatch cause;
- exact Canali parameterization is proven identical to the paper.
