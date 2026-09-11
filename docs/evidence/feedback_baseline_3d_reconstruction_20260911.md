# FB-BASELINE-01 — 3D BCAT baseline reconstruction checkpoint

> Date: 2026-09-11  
> Last synchronized: 2026-09-12  
> Status: **In Progress — G2 launched / result pending ingestion**  
> Scope: feedback item `FB-BASELINE-01` / task `T-BASELINE-01`

## 1. Purpose

The original feedback asks how closely the simplified CMP baseline reproduces the literature 3-D BCAT electrical characteristics. To answer that question without over-claiming, a separate literature-consistent 3-D baseline reconstruction is being built and validated before any comparison is made against the simplified 2-D CMP model.

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

All parameters and conclusions are separated into three categories.

### 2.1 Literature-explicit facts

The paper explicitly states the following nominal baseline values:

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

The paper also reports nominal electrical metrics:

```text
Vth       = 0.656 V
SS        = 76 mV/dec
Ion/Ioff  = 3.4e10
DIBL      = 23.6 mV/V
```

The reported transport / leakage-model set includes Philips unified mobility, Lombardi interface mobility, Canali velocity-saturation treatment, and Hurkx tunneling.

### 2.2 Reconstruction assumptions

The following are **not stated directly in the paper** and are therefore tracked as reconstruction assumptions:

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

The exact STI depth interpretation, terminal-contact face definitions, lateral Gaussian straggle, and full 3-D process geometry are not provided by the paper and therefore cannot be presented as paper-explicit facts.

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
| G1 | High-Vd paper-condition ID–VG | **PASS** |
| G2 | Low-Vd full ID–VG for DIBL | **LAUNCHED / RESULT PENDING INGESTION** |

Geometry / contacts / doping are frozen. F1 mesh is intentionally **not** yet frozen because final acceptance requires an electrical mesh-convergence study.

---

## 4. Geometry checkpoint

The frozen geometry uses the literature-explicit dimensions while keeping the uncertain mapping explicit.

Key vertical coordinates:

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

- along-channel B–B′ cut: buried gate / nitride / oxide / recess geometry checked;
- across-fin A–A′ cut: 17 nm saddle-fin width and rounded cap checked;
- top XY view: active and word-line directions cross at 90°;
- geometry overlap check returned empty overlap;
- SDE model save completed successfully.

The semi-circular fin cap is a reconstruction of `Rfillet = 1`; it is not claimed as an exact reverse-engineering of the unpublished CAD geometry.

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

SDevice later recognized all four electrode names correctly, including the gate with `WorkFunction = 4.8 eV`.

Exact contact-face selection is a reconstruction choice because the paper does not publish Sentaurus contact-face IDs or boundary definitions.

---

## 6. Doping checkpoint

Implemented doping:

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

Vertical source and drain cuts were exported and the signed net-doping zero crossing was checked.

Results:

```text
Source metallurgical junction = 48.0 nm
Drain metallurgical junction  = 48.0 nm
Target                         = 0.40 × 120 nm = 48.0 nm
```

Both sides therefore satisfy the nominal vertical `Djunction` criterion used for the reconstruction.

Important limitation:

> Passing the 48 nm vertical junction criterion does **not** validate the unpublished lateral S/D diffusion profile. `GaussFactor = 0.0` remains an explicit reconstruction assumption.

---

## 7. Mesh checkpoint

### 7.1 F0 — doping QA mesh

Purpose: verify doping fields and junction depth, not final electrical accuracy.

Observed scale in SVisual:

```text
Elements ≈ 1.125 M
Points   ≈ 183 k
```

### 7.2 F1 — nominal electrical mesh

Refinement priorities:

- active saddle-fin / channel;
- Si/oxide interface;
- source/drain junction bands;
- source/drain-side gate-edge high-field regions;
- coarser deep bulk.

Observed scale:

```text
SVisual display:
  Elements ≈ 2.90 M
  Points   = 473,004

SDevice load:
  grid points   = 473,004
  tetrahedrons  = 2,773,380
```

SDevice completed both G0 and G1 on this mesh. The mesh remains a **candidate**, not a convergence-frozen production mesh.

Mesh-quality note from SDevice:

- non-Delaunay elements were extremely few relative to total elements;
- a substantial obtuse-element fraction exists;
- current DD runs converge, but later local E-field / GIDL use still requires a dedicated convergence check.

---

## 8. G0 — SDevice bring-up result

Purpose: prove that the reconstructed 3-D structure, contacts, doping, mesh, and physics can solve through equilibrium and transistor turn-on before paper-metric comparison.

Conditions:

```text
T       = 300 K
WF      = 4.8 eV
Vs      = 0 V
Vsub    = 0 V
Vd      = 0 → 0.05 V
Vg      = 0 → 1.2 V
```

Physics enabled in the current deck:

- Fermi statistics;
- Philips unified mobility (`PhuMob`);
- Lombardi normal-field mobility degradation;
- electron / hole high-field saturation using `GradQuasiFermi`;
- Hurkx band-to-band tunneling.

Result:

```text
G0 numerical bring-up = PASS
Id @ Vg=1.2 V, Vd=0.05 V = 7.769e-8 A
provisional SS ≈ 91.3 mV/dec
```

This SS value is **sanity-check only** because G0 was not the final paper-condition extraction run.

---

## 9. G1 — high-Vd ID–VG result

Conditions:

```text
T       = 300 K
WF      = 4.8 eV
Vs      = 0 V
Vsub    = 0 V
Vd      = 1.2 V
Vg      = 0 → 2.0 V
```

Run status:

```text
Numerical convergence = PASS
Full gate sweep        = PASS
Final Id @ Vg=2.0 V    = 1.063e-5 A
```

The run finished without fatal error after approximately 1 h 30 min, with peak memory around 18.1 GB.

### 9.1 Provisional electrical extraction

From the exported high-Vd ID–VG curve:

```text
Id @ Vg≈0 V         ≈ 1.33e-14 A
minimum Id           ≈ 3.50e-15 A
minimum-Id location  ≈ Vg 0.379 V
Id @ Vg=1.2 V        ≈ 2.10e-7 A
Id @ Vg=2.0 V        = 1.063e-5 A
provisional SS        ≈ 91.2 mV/dec
max(Id)/min(Id)       ≈ 3.04e9
```

The last ratio is only a provisional max/min ratio and is **not yet claimed to be identical to the paper’s Ion/Ioff extraction convention**.

### 9.2 Provisional threshold check

The paper defines threshold by the constant-current criterion:

```text
Icrit = 1e-7 A × W/L
```

If, provisionally, `W = Wfin = 17 nm` and `L = Lgate = 20 nm` are used:

```text
Icrit ≈ 8.5e-8 A
Vth_high, provisional ≈ 1.147 V
```

This is far above the reported paper nominal `Vth = 0.656 V`.

Because the exact 3-D BCAT channel-width convention used in the paper’s extraction is not fully documented in the text, this threshold is retained as **provisional**, not final.

---

## 10. Current mismatch relative to paper nominal

Current high-Vd reconstruction versus paper nominal:

| Metric | 3D-Sun-B0 current checkpoint | Paper nominal | Status |
|---|---:|---:|---|
| `Vth` | ~1.147 V* | 0.656 V | mismatch; extraction definition still under review |
| `SS` | ~91.2 mV/dec | 76 mV/dec | mismatch |
| `Ion/Ioff` | ~3.04e9* | 3.4e10 | mismatch; current value is provisional max/min |
| `DIBL` | pending G2 | 23.6 mV/V | not yet evaluated |

`*` = provisional extraction, not yet treated as exact paper-equivalent metric.

This is an important result: the 3-D deck is numerically healthy, but **electrical reproduction is not yet demonstrated**.

---

## 11. Off-state current observation

At the end of the high-drain ramp with approximately `Vg = 0 V`, the drain current is on the order of `1.3e-14 A`. The source current is much smaller while the substrate current balances most of the drain current.

This indicates that, in this reconstructed deck and bias condition, the initial high-Vd off-state current is dominated by a drain/body leakage path rather than normal source-to-drain channel conduction.

This observation helps explain why the high-Vd ID–VG curve first decreases to a minimum before normal MOS turn-on dominates.

No stronger causal statement is made at this checkpoint.

---

## 12. Physics-model mapping issue still open

The paper explicitly describes a Canali velocity-saturation model.

The current Sentaurus T-2022.03 log reports the activated high-field mobility as:

```text
Caughey-Thomas saturation model, using gradient quasi-Fermi potential
```

Therefore the repository must **not** state that the paper’s Canali model has already been reproduced exactly. The mapping between the paper wording and the specific T-2022.03 keyword / implementation remains an open verification item.

---

## 13. Leading reconstruction hypothesis — not yet a conclusion

One plausible source of the high Vth / degraded SS is the current lateral S/D reconstruction:

```text
GaussFactor = 0.0
```

This creates no intentional lateral Gaussian spread beyond the selected implant footprint. If the unpublished paper geometry had stronger lateral diffusion toward the recessed gate, the current reconstruction could have a longer effective electrical channel.

This is **only a hypothesis** at this stage.

Do not tune work function, doping concentration, or geometry merely to force agreement before the remaining extraction and mapping checks are completed.

---

## 14. G2 launched — result pending ingestion

Purpose:

> obtain a full low-drain ID–VG curve using the same frozen geometry, doping, mesh, physics, and extraction flow so that DIBL can be evaluated consistently.

Conditions:

```text
T       = 300 K
WF      = 4.8 eV
Vs      = 0 V
Vsub    = 0 V
Vd      = 0.05 V
Vg      = 0 → 2.0 V
```

The G2 job was launched, but no completed G2 log / PLT / CSV has yet been returned to this workflow. Until those files are ingested and checked, G2 must not be marked `PASS` and no DIBL value is claimed.

After G2 evidence is returned:

1. validate numerical completion and the full low-Vd sweep;
2. extract low-Vd threshold using the same criterion as G1;
3. calculate DIBL from low- and high-drain thresholds;
4. compare against `23.6 mV/V` paper nominal;
5. freeze a consistent extraction definition;
6. only then diagnose the remaining electrical mismatch;
7. separately verify the Canali / high-field model mapping;
8. later perform coarse / nominal / fine electrical mesh convergence.

---

## 15. Repository evidence package

The baseline-feedback artifacts produced up to G1 are now committed separately from this interpretation document.

Evidence manifest:

```text
docs/evidence/baseline_3d_evidence_manifest_20260912.md
```

Curated visual archive:

```text
assets/images/feedback/20260911_baseline/baseline_visual_evidence_20260911.zip
```

The visual archive contains the selected 3-D geometry overview, XZ/YZ validation cuts, contact view, doping/junction-cut view, F1 mesh view, and source/drain junction-depth profile screenshots.

Raw log/data archive:

```text
data/baseline_3d_sun_b0/baseline_raw_text_data_20260911.zip
```

Directly browsable CSV evidence:

```text
data/baseline_3d_sun_b0/g0_idvg_lowvd_0p05V_to_1p2V.csv
data/baseline_3d_sun_b0/g1_idvg_highvd_1p2V_to_2p0V.csv
data/baseline_3d_sun_b0/junction_source_C1.csv
data/baseline_3d_sun_b0/junction_drain_C2.csv
```

The raw archive also contains the G0/G1 full SDevice logs and F1 SDE build log available from the completed workflow. G2 is deliberately excluded until a completed G2 result is returned and validated.

---

## 16. Feedback-level interpretation at this checkpoint

The baseline feedback is **not closed yet**.

Current defensible statement:

> A literature-consistent 3-D BCAT reconstruction has been completed through frozen geometry, contacts, and vertical doping validation. The nominal electrical mesh successfully supports 3-D SDevice operation, and both low-Vd bring-up and high-Vd full ID–VG simulations converge. However, the first high-Vd electrical extraction does not yet reproduce the Sun et al. nominal Vth, SS, and Ion/Ioff values. DIBL is pending ingestion and validation of the launched G2 low-Vd full sweep. The remaining mismatch is therefore being treated as a reconstruction / extraction / physics-mapping problem rather than hidden by parameter fitting.

This result is directly useful to the original feedback question because it establishes a clean distinction between:

```text
literature-explicit 3-D baseline
vs.
reconstructed 3-D implementation
vs.
existing simplified 2-D CMP baseline
```

Only after the 3-D reconstruction metrics are stabilized should the simplified 2-D B0 be judged against it.

---

## 17. Guardrails

Do not claim:

```text
The Sun 2022 device has been exactly reproduced.
The current 3-D deck already matches the paper electrically.
Vth = 1.147 V is final before the width convention is frozen.
3.04e9 is necessarily the paper-equivalent Ion/Ioff.
GaussFactor = 0 is a paper value.
The current high-field keyword is proven to be exactly Canali.
The F1 mesh is convergence-frozen.
The lateral doping assumption is proven to be the cause of the mismatch.
G2 is complete before its returned result files are ingested and checked.
```

Use:

- “literature-consistent reconstruction”;
- “reconstruction assumption” where geometry/process details are unpublished;
- “provisional extraction” until metric definitions are frozen;
- “numerically validated / converged” separately from “electrically reproduced.”

---

## 18. README integration rule

This evidence is intentionally stored under the feedback/evidence workflow first.

The main README should **not** be rewritten yet. Baseline, E-field/mesh, retention, and practical-trade-off feedback should be integrated into the README together after the principal feedback set is closed.
