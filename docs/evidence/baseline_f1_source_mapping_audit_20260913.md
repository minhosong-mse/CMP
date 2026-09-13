# FB-BASELINE-01 — F1 source / geometry-mapping audit (2026-09-13)

## Purpose

Audit the original final F1 SDE source before any further parameter sensitivity work. This checkpoint is intended to distinguish a true paper-reconstruction ambiguity from arbitrary parameter fitting.

## Exact source archived

The user-returned F1 source was archived as:

```text
code/sde/baseline_3d_sun_b0/F1_nominal.cmd
```

It is the original source content used for the current nominal 3D-Sun-B0 reconstruction. The duplicate pasted text supplied in the same handoff was line-for-line identical to the CMD source; only file encoding/line-ending bytes differed.

## Source facts confirmed

The source explicitly contains:

```text
Lgate = 0.020 um
Drecess = 0.120 um
DBCAT = 0.036 um
Tox = 0.005 um
Wfin = 0.017 um
Hfin = 0.048 um
Nbody = 1e17 cm^-3
NSD = 1e20 cm^-3
Djunction = 0.048 um
GaussFactor = 0.0
```

Current gate geometry mapping is:

```text
Rgate = 0.5 * Lgate = 10 nm
Router = Rgate + Tox = 15 nm
```

Thus the present reconstruction interprets the literature `Lgate = 20 nm` as the **metal-gate width**, producing a total oxide-outer recess width of 30 nm.

The source/drain analytical-profile windows terminate at `x = ±Router`, so their inner boundaries currently follow the **oxide-outer gate edge**.

## GaussFactor audit

Sentaurus analytical profiles use the `Factor` parameter for the lateral Gaussian distribution outside the primary reference window. The current value `GaussFactor = 0.0` sharply truncates the profile outside the S/D reference rectangle.

However, source-code geometry shows that simply increasing `GaussFactor` is not the cleanest first electrical sensitivity:

- source/drain windows already extend up to the oxide-outer gate edge (`±Router`);
- for depths shallower than the nominal 48 nm junction, the adjacent region outside the S/D window is predominantly gate stack / isolation rather than silicon;
- below the 48 nm junction, the primary As profile is already at or below the 1e17 cm^-3 body concentration.

Therefore `GaussFactor` alone is expected to have limited leverage on the electrically active source/drain boundary in this specific reconstruction. This is a source/geometry inference, not a substitute for a later sensitivity run if needed.

## Higher-priority mapping ambiguity: what does Lgate span?

Inspection of the paper schematics (Figure 1d / Figure 2a) raises a more consequential reconstruction ambiguity: the `Lgate` arrow visually spans the complete recessed gate-stack width, while the text separately states that the recessed region is surrounded by 5 nm gate oxide.

The current nominal SDE assumes:

```text
Interpretation A — current nominal
metal width = Lgate = 20 nm
oxide-outer recess width = 20 + 2*Tox = 30 nm
```

A defensible alternative interpretation is:

```text
Interpretation B — sensitivity only
oxide-outer recess width = Lgate = 20 nm
metal width = Lgate - 2*Tox = 10 nm
```

Under Interpretation B:

```text
Router = 10 nm
Rgate  = 5 nm
ZgateCenter = -110 nm
ZgateBottom = -115 nm
ZoxideBottom = -120 nm
```

Notably, the W-gate and oxide bottom depths remain consistent with the 120 nm recess while the lateral gate/recess width becomes substantially narrower. This directly shortens the lateral S/D separation and can materially change gate coupling / effective channel behavior, making it a higher-value diagnostic than arbitrary work-function or doping tuning.

## Next validation

Run one controlled **H1 gate-length-mapping sensitivity** before lateral-Gaussian fitting:

```text
Baseline A: current F1 nominal (already complete)
Sensitivity B: Lgate interpreted as oxide-outer recess width
```

Keep unchanged:

```text
Drecess, DBCAT, Tox, Wfin, Hfin
body and S/D concentrations
Djunction = 48 nm
GaussFactor = 0.0
contacts
F1 mesh policy
SDevice physics
T = 300 K
```

First electrical diagnostic for Interpretation B:

```text
Vd = 1.2 V
Vg = 0 -> 2.0 V
```

Extract only:

```text
gate OuterVoltage vs drain TotalCurrent CSV
```

Compare against current G1 on:

```text
Vth under the same provisional criterion
SS over the same current window
Id minimum / off-state shape
Id at Vg = 1.2 V and 2.0 V
```

Only if this geometry mapping materially improves the high-Vd baseline should the corresponding low-Vd G2 sweep be run for DIBL. If it does not, revert to the frozen nominal and continue with source/drain-side rounding / implant-mapping sensitivity.

## Claim guardrail

The alternative `Lgate` interpretation is a **reconstruction sensitivity**, not a literature-explicit correction. Do not replace the frozen nominal baseline until the geometry interpretation and electrical evidence are reviewed together.
