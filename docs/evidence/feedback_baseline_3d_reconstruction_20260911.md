# FB-BASELINE-01 — 3D BCAT baseline reconstruction checkpoint

> Date: 2026-09-11  
> Last synchronized: 2026-09-13  
> Status: **In Progress — G2 complete; post-G2 extraction / model-mapping stage**  
> Scope: feedback item `FB-BASELINE-01` / task `T-BASELINE-01`

## 1. Purpose

The original feedback asks how closely the simplified CMP baseline reproduces the literature 3-D BCAT electrical characteristics. To answer that question without over-claiming, a separate literature-consistent 3-D baseline reconstruction is being built and validated before any final comparison is made against the simplified 2-D CMP model.

This reconstruction is named:

```text
3D-Sun-B0
```

Reference baseline:

- M. Sun, H. W. Baac, C. Shin, “Simulation Study: The Impact of Structural Variations on the Characteristics of a Buried-Channel-Array Transistor (BCAT) in DRAM,” *Micromachines*, 13, 1476 (2022).
- DOI: 10.3390/mi13091476

The goal is **literature-consistent reconstruction**, not an undocumented claim of exact reproduction.

---

## 2. Claim discipline

All parameters and conclusions are separated into three categories:

1. literature-explicit facts;
2. reconstruction assumptions;
3. simulation / validation results.

### 2.1 Literature-explicit nominal inputs

| Parameter | Literature value |
|---|---:|
| Physical gate length, `Lgate` | 20 nm |
| Recess depth, `Drecess` | 120 nm |
| `ARgate = Drecess/Lgate` | ~6 |
| Gate material | W |
| Gate work function | 4.8 eV |
| Gate oxide thickness | 5 nm |
| `DBCAT` | 36 nm |
| Body/substrate | B, `1e17 cm^-3` |
| Source/drain | As, `1e20 cm^-3` |
| Doping profile | Gaussian |
| Nominal `Djunction` | `0.40 × Drecess = 48 nm` |
| `Djunction` definition | depth where doping reaches `1e17 cm^-3` |
| `Wfin` | 17 nm |
| `Hfin` | 48 nm |
| `Rfillet` | 1.0, semi-circular saddle-fin shape |

Paper nominal electrical metrics:

```text
Vth       = 0.656 V
SS        = 76 mV/dec
Ion/Ioff  = 3.4e10
DIBL      = 23.6 mV/V
```

Reported transport / leakage models include Philips unified mobility, Lombardi interface mobility, Canali velocity saturation, and Hurkx tunneling.

### 2.2 Reconstruction assumptions

The paper does not publish enough detail to reverse-engineer an exact Sentaurus deck. The following are therefore tracked explicitly as reconstruction assumptions:

```text
Coordinate system:
  x = source ↔ drain / along-channel
  y = word-line / across-fin
  z = vertical, top surface = 0, depth = negative z

Simulation domain:
  Xhalf = 60 nm
  Yhalf = 30 nm
  Zbody = 180 nm

Hfin mapping:
  top-to-fin/bulk merge depth = 48 nm

Rfillet = 1 reconstruction:
  semi-circular fin cap with radius Wfin/2 = 8.5 nm

Source implant footprint:
  x = -60 to -15 nm
  y = -8.5 to +8.5 nm

Drain implant footprint:
  x = +15 to +60 nm
  y = -8.5 to +8.5 nm

Gaussian lateral factor:
  GaussFactor = 0.0
```

Exact STI-depth interpretation, terminal-contact faces, lateral Gaussian straggle, full 3-D process geometry, and the exact DIBL low/high drain-bias pair are not explicitly published by the paper.

---

## 3. Reconstruction / validation phase status

| Phase | Content | Status |
|---|---|---|
| A | Literature truth table | **DONE** |
| B | Coordinate system | **PASS / FROZEN** |
| C | 3-D geometry v05 | **PASS / FROZEN** |
| D0/D1 | Contact mapping + contacts | **PASS / FROZEN** |
| E | Body + Gaussian S/D doping | **PASS / FROZEN** |
| F0 | Doping verification mesh | **PASS** |
| F1 | Nominal electrical mesh | **BUILD PASS / CANDIDATE** |
| G0 | SDevice bring-up, low-Vd sanity sweep | **PASS** |
| G1 | High-Vd full ID–VG | **PASS** |
| G2 | Low-Vd full ID–VG | **PASS — returned curve ingested** |

Geometry / contacts / doping remain frozen. F1 mesh is intentionally **not** yet frozen because final acceptance still requires an electrical mesh-convergence study.

---

## 4. Geometry checkpoint

Key vertical coordinates in the frozen reconstruction:

```text
z = 0 nm        : top reference
z = -36 nm      : W-gate top / DBCAT boundary
z = -48 nm      : reconstructed fin-to-bulk merge depth
z = -105 nm     : rounded gate/oxide bottom-center
z = -115 nm     : W-gate bottom
z = -120 nm     : oxide/recess bottom
z = -180 nm     : simulation-domain bottom
```

Validation performed:

- B–B′ along-channel XZ cut: buried gate / nitride / oxide / recess checked;
- A–A′ across-fin YZ cut: 17 nm saddle-fin width and rounded cap checked;
- top XY view: active and word-line directions checked;
- geometry overlap check returned empty overlap;
- SDE model save completed successfully.

The semi-circular fin cap is a reconstruction of `Rfillet = 1`; it is not claimed as an exact unpublished CAD geometry.

---

## 5. Contact checkpoint

Four terminals are defined:

```text
source
drain
gate
substrate
```

Mapping:

- source: end face at `x = -Xhalf`;
- drain: end face at `x = +Xhalf`;
- substrate: bottom Si face;
- gate: W-gate body converted to a gate contact boundary.

SDevice recognized all four electrode names and the `4.8 eV` gate work function.

Exact contact-face selection is a reconstruction choice because the paper does not publish Sentaurus face IDs or terminal-boundary definitions.

---

## 6. Doping checkpoint

Implemented body / S-D doping:

```text
Body:
  BoronActiveConcentration = 1e17 cm^-3

Source / Drain:
  ArsenicActiveConcentration
  PeakVal      = 1e20 cm^-3
  ValueAtDepth = 1e17 cm^-3
  Depth        = 0.048 um
  Gaussian
  lateral Factor = 0.0   [reconstruction assumption]
```

### 6.1 Quantitative junction QA

Vertical source and drain net-doping cuts give:

```text
Source metallurgical junction = 48.0 nm
Drain metallurgical junction  = 48.0 nm
Target                         = 0.40 × 120 nm = 48.0 nm
```

This validates the nominal **vertical** junction criterion only. It does not validate the unpublished lateral S/D diffusion profile.

---

## 7. Mesh checkpoint

### F0 — doping-QA mesh

```text
Elements ≈ 1.125 M
Points   ≈ 183 k
```

Purpose: doping / junction-depth QA only.

### F1 — nominal electrical mesh

Refinement priorities:

- active saddle-fin / channel;
- Si/oxide interface;
- source/drain junction bands;
- source/drain-side gate-edge high-field regions;
- coarser deep bulk.

Observed scale:

```text
SVisual:
  Elements ≈ 2.90 M
  Points   = 473,004

SDevice:
  grid points  = 473,004
  tetrahedrons = 2,773,380
```

G0, G1, and G2 curves all solve on this nominal mesh, but F1 remains a **candidate**, not a convergence-frozen production mesh. The known obtuse-element / tiny-edge quality caveat remains open for later mesh-convergence and high-field validation.

---

## 8. G0 — numerical bring-up

Conditions:

```text
T       = 300 K
WF      = 4.8 eV
Vs      = 0 V
Vsub    = 0 V
Vd      = 0 → 0.05 V
Vg      = 0 → 1.2 V
```

Physics currently active in the reconstruction:

- Fermi statistics;
- Philips unified mobility (`PhuMob`);
- Lombardi normal-field mobility degradation;
- electron / hole high-field saturation using `GradQuasiFermi`;
- Hurkx band-to-band tunneling.

Result:

```text
G0 = PASS
Id @ Vg=1.2 V, Vd=0.05 V = 7.769e-8 A
provisional SS ≈ 91.3 mV/dec
```

G0 is a numerical / turn-on sanity run and is not used as the final paper-metric comparison.

---

## 9. G1 — high-drain ID–VG

Conditions:

```text
T       = 300 K
WF      = 4.8 eV
Vs      = 0 V
Vsub    = 0 V
Vd      = 1.2 V
Vg      = 0 → 2.0 V
```

Result:

```text
G1 = PASS
Id @ Vg=2.0 V = 1.063365e-5 A
Id @ Vg≈0 V    ≈ 1.33e-14 A
minimum Id      ≈ 3.50e-15 A @ Vg≈0.379 V
SS, 1e-13~1e-10 A fit ≈ 91.17 mV/dec
max(Id)/min(Id) ≈ 3.04e9
```

The max/min ratio remains a provisional curve ratio and is not yet claimed to be identical to the paper’s exact Ion/Ioff extraction convention.

### 9.1 Provisional threshold criterion

The paper defines threshold using:

```text
Icrit = 1e-7 A × W/L
```

Current reconstruction interpretation:

```text
W = Wfin  = 17 nm
L = Lgate = 20 nm
Icrit     = 8.5e-8 A
```

Using log-current interpolation between adjacent sweep points:

```text
Vth_high @ Vd=1.20 V = 1.14659 V
```

This is far above the reported paper nominal `Vth = 0.656 V`, but the value remains **provisional** because the paper does not fully document its 3-D channel-width convention.

---

## 10. G2 — low-drain full ID–VG

Returned SVisual dataset / CSV:

```text
IdVg_LowVd_Full_n5_des
X = gate OuterVoltage
Y = drain TotalCurrent
```

Conditions:

```text
T       = 300 K
WF      = 4.8 eV
Vs      = 0 V
Vsub    = 0 V
Vd      = 0.05 V
Vg      = 0 → 2.0 V
```

Curve-level validation:

- full gate sweep reaches `2.0 V`;
- no truncation is visible in the exported CSV;
- current evolves smoothly through subthreshold and strong inversion.

Quantitative checkpoints:

```text
minimum Id = 1.0147335e-17 A @ Vg=0.1395599 V
Id @ Vg=2.0 V = 2.48569e-6 A
SS, 1e-13~1e-10 A fit ≈ 92.83 mV/dec
G2 curve ingestion = PASS
```

Using the same provisional threshold criterion and log-current interpolation:

```text
Vth_low @ Vd=0.05 V = 1.20610 V
```

### 10.1 Reconstruction-defined DIBL

With the G1/G2 drain biases:

```text
DIBL = (Vth_low - Vth_high)/(1.20 - 0.05)
     = (1.20610 - 1.14659)/1.15
     ≈ 51.75 mV/V
```

Paper nominal:

```text
DIBL = 23.6 mV/V
```

Important limitation:

> The paper text reports the nominal DIBL value but does not explicitly publish the exact low/high drain-bias pair used for DIBL extraction. Therefore `51.75 mV/V` is retained as a **reconstruction-defined provisional DIBL**, not yet a strict paper-equivalent value.

---

## 11. Current electrical mismatch relative to paper nominal

| Metric | 3D-Sun-B0 current checkpoint | Paper nominal | Status |
|---|---:|---:|---|
| `Vth_high` | 1.14659 V* | 0.656 V | large mismatch; width convention still provisional |
| `SS_high` | 91.17 mV/dec | 76 mV/dec | mismatch |
| `Ion/Ioff` | ~3.04e9* | 3.4e10 | mismatch; current value is provisional max/min |
| `DIBL` | 51.75 mV/V** | 23.6 mV/V | mismatch under reconstruction bias pair |

`*` = provisional extraction definition.  
`**` = reconstruction-defined using `Vd=0.05 / 1.20 V`; exact paper bias pair not explicitly published.

This checkpoint therefore supports:

> the 3-D deck is numerically operational, but electrical reproduction of the Sun et al. nominal baseline has **not** yet been demonstrated.

---

## 12. Off-state current observation

At high drain bias and approximately `Vg=0 V`, the drain current is on the order of `1.3e-14 A`; the source current is much smaller while the substrate current balances most of the drain current.

This supports only the limited observation that the reconstructed high-Vd off-state current is dominated by a drain/body leakage path rather than ordinary source-to-drain channel conduction. No stronger causal statement is made at this checkpoint.

---

## 13. Physics-model mapping issue still open

The paper explicitly describes a Canali velocity-saturation model.

Current Sentaurus T-2022.03 logs report:

```text
Caughey-Thomas saturation model, using gradient quasi-Fermi potential
```

Therefore the repository must **not** state that the paper’s Canali implementation has been reproduced exactly. The mapping between the paper wording and the specific T-2022.03 implementation remains an open verification item.

---

## 14. Leading reconstruction hypothesis — not yet a conclusion

One plausible source of the high Vth / degraded SS is the current lateral S/D reconstruction:

```text
GaussFactor = 0.0
```

If the unpublished paper geometry had stronger lateral diffusion toward the recessed gate, the current reconstruction could have a longer effective electrical channel.

This is **only a hypothesis**. Do not tune work function, doping concentration, or geometry merely to force agreement before extraction-definition, physics-mapping, and sensitivity checks are completed.

---

## 15. Repository evidence checkpoint

Repository convention follows the existing CMP pattern rather than storing full simulator logs by default.

Committed data / summaries:

```text
data/baseline_3d_sun_b0/g0_idvg_lowvd_0p05V_to_1p2V.csv
data/baseline_3d_sun_b0/g1_idvg_highvd_1p2V_to_2p0V.csv
data/baseline_3d_sun_b0/g2_idvg_lowvd_0p05V_to_2p0V.csv
data/baseline_3d_sun_b0/junction_source_C1.csv
data/baseline_3d_sun_b0/junction_drain_C2.csv
data/baseline_3d_sun_b0/f1_sde_build_summary.txt
data/baseline_3d_sun_b0/g0_sdevice_run_summary.txt
data/baseline_3d_sun_b0/g1_sdevice_run_summary.txt
data/baseline_3d_sun_b0/g2_curve_validation_summary.txt
```

Executable SDevice decks:

```text
code/sdevice/baseline_3d_sun_b0/G0_bringup.cmd
code/sdevice/baseline_3d_sun_b0/G1_highVd_full_idvg.cmd
code/sdevice/baseline_3d_sun_b0/G2_lowVd_full_idvg.cmd
```

Curated visual evidence:

```text
assets/images/feedback/20260911_baseline/00_baseline_visual_contact_sheet.svg
```

Full Sentaurus logs, native `.plt`, temporary screenshots, and failed attempts remain workspace/debug evidence unless a later diagnosis specifically requires them.

One source artifact still worth adding later is the original final **F1 SDE source CMD** exported directly from Sentaurus. It must not be reconstructed from a log and mislabeled as exact source.

---

## 16. Remaining work before `FB-BASELINE-01` closes

1. freeze / document the paper-equivalent Vth and Ion/Ioff extraction convention and the DIBL bias-pair limitation;
2. verify the paper `Canali` wording against the exact T-2022.03 high-field implementation;
3. test sensitivity to the unpublished lateral S/D Gaussian assumption (`GaussFactor=0.0`) without arbitrary fitting;
4. perform coarse / nominal / fine electrical mesh convergence before freezing F1;
5. compare the stabilized `3D-Sun-B0` metrics directly with the simplified 2-D CMP B0;
6. archive the original final F1 SDE source CMD once exported from Sentaurus.

---

## 17. Resume point

Next session should **not** rerun G2.

Resume from:

```text
G2 curve validation                         DONE
provisional low/high Vth + DIBL             DONE
paper-equivalent extraction definition      OPEN
Canali / high-field implementation mapping  OPEN
lateral Gaussian sensitivity                OPEN
mesh convergence                             OPEN
2-D vs stabilized 3-D fidelity comparison   OPEN
```

---

## 18. Feedback-level interpretation

The baseline feedback is **not closed yet**.

Current defensible statement:

> A literature-consistent 3-D BCAT reconstruction has been completed through frozen geometry, contacts, and vertical-doping validation, and G0/G1/G2 ID–VG operation has been obtained on the nominal electrical mesh. Under the current provisional constant-current interpretation, the reconstruction gives `Vth_high ≈ 1.1466 V`, `Vth_low ≈ 1.2061 V`, `SS ≈ 91–93 mV/dec`, and a reconstruction-defined DIBL of about `51.75 mV/V`. These values do not yet reproduce the Sun et al. nominal electrical metrics. The remaining discrepancy is being treated as an extraction-definition / physics-mapping / lateral-doping / mesh-convergence problem rather than hidden by parameter fitting.

The final answer to `FB-BASELINE-01` will compare:

```text
literature nominal 3-D metrics
↔ stabilized 3D-Sun-B0 reconstruction
↔ simplified 2-D CMP baseline
```

Only then should the role and limits of the simplified 2-D model be stated in the final presentation / README.

---

## 19. Guardrails

Do not claim:

```text
The Sun 2022 device has been exactly reproduced.
The current 3-D deck already matches the paper electrically.
Vth ≈ 1.1466 V is final before the width convention is frozen.
3.04e9 is necessarily the paper-equivalent Ion/Ioff.
51.75 mV/V is necessarily the paper-equivalent DIBL.
GaussFactor = 0 is a paper value.
The current high-field keyword is proven to be exactly Canali.
The F1 mesh is convergence-frozen.
The lateral doping assumption is proven to be the cause of the mismatch.
```

Use:

- “literature-consistent reconstruction”;
- “reconstruction assumption” where geometry/process details are unpublished;
- “provisional extraction” until metric definitions are frozen;
- “reconstruction-defined DIBL” for the current `0.05 / 1.20 V` pair;
- “numerically validated / operational” separately from “electrically reproduced.”

---

## 20. README integration rule

This evidence remains under the feedback/evidence workflow first. The main README should **not** be rewritten yet. Baseline, E-field/mesh, retention, and practical-trade-off feedback should be integrated together after the principal feedback set is closed.
