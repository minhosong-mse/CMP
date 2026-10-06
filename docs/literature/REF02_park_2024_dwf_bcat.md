# REF02 — Novel Dual Work Function Buried Channel Array Transistor Process Design for Sub-17 nm DRAM

## 1. Bibliographic Information

- Authors: Dong-Sik Park et al.
- Journal: *IEEE Access*, Vol. 12, pp. 63049-63065, 2024
- DOI: `10.1109/ACCESS.2024.3371508`
- Verification: **full 17-page published PDF directly reviewed**
- License on the published PDF: **CC BY-NC-ND 4.0**

## 2. Why This Paper Matters to CMP

REF02 is a downstream DWF-BCAT process/device reference rather than a direct numerical baseline for the active `B0-2D-PAPER-CAL` single-WF lineage.

Its strongest CMP value is the experimentally grounded trade-off chain:

```text
gate material / gate-oxide / barrier process
→ gate-drain electric field and interface-trap environment
→ GIDL / refresh fail behavior
↔ tungsten word-line volume / Rwl / write behavior
```

This is highly relevant to future DWFG portability and to the claim boundary around geometry-only RWL proxies.

## 3. Device / Study Scope

- fabricated sub-17-nm DRAM using DWF-BCAT;
- W + highly P-doped poly-Si dual-work-function gate;
- 3D/cross-sectional device structure with buried contacts to cell capacitors;
- process-development study combining TCAD, non-patterned-wafer experiments, and actual DRAM electrical characterization.

## 4. Paper-Explicit Geometry / Materials

The paper reports:

| Item | Paper value |
|---|---:|
| BCAT height | 150 nm |
| poly-Si thickness | 25 nm |
| fin height | 30 nm |
| barrier thickness | 2 nm |
| BCAT width | 30 nm |
| gate-oxide thickness | 8 nm |
| n+ gate poly-Si P concentration | `5.0 × 10^17 cm^-3` |
| resulting poly-Si gate work function | 4.15 eV |

These values belong to REF02's sub-17-nm DWF structure and are **not** copied into the current CMP 20-nm single-WF baseline.

## 5. TCAD Model Set Explicitly Reported

The paper states that its TCAD simultaneously applied:

1. band-gap narrowing;
2. SRH recombination with doping and temperature dependence and Hurkx field enhancement;
3. nonlocal trap-assisted tunneling;
4. band-to-band tunneling using Hurkx;
5. doping-dependent mobility;
6. high-field saturation;
7. avalanche breakdown;
8. Auger recombination;
9. Fermi-Dirac statistics;
10. quantum confinement.

This is a literature model description, not executable Sentaurus syntax and not evidence that the current CMP model must use the same complete stack.

## 6. GIDL / Electric-Field Mechanism

The paper attributes GIDL to BTBT driven by high electric field and band bending in the gate-to-drain overlap region.

For the simulated DWF-BCAT, the reported field profile shows a lower maximum field than conventional BCAT in the GIDL-relevant region, although the W/poly-Si interface itself can introduce a local field increase.

The paper therefore provides a useful warning for CMP: a single interface-local field feature and the broader GIDL-critical field profile are not necessarily the same metric.

## 7. Word-Line / GIDL Trade-off

Increasing the poly-Si portion reduces W volume and can increase word-line resistance and write time. The paper therefore develops process changes that recover lateral W area while controlling oxide quality and GIDL.

This is directly relevant to future CMP DWFG discussions, but it does **not** turn the current geometry-derived RWL proxy into measured distributed word-line resistance.

## 8. IAI Gate-Oxide Process

REF02 compares conventional ALD/ISSG (AI) with ISSG/ALD/ISSG (IAI).

The reported process intent is to:
- scale sidewall oxide while preserving bottom oxide;
- reduce oxide impurities / interface traps;
- recover W gate area;
- improve the GIDL / Rwl process trade-off.

In mass-wafer comparison of roughly 2000 wafers, the paper reports:
- refresh fail bits lower by about 25% for IAI versus AI;
- Rwl lower by about 15%;
- word-line fail bits lower by about 10%.

These are paper-specific fabricated-device/process results and must not be reused as CMP percentage improvements.

## 9. PNOF Barrier

The paper introduces plasma nitridation treatment of oxide film (PNOF) to form a `W_xO_yN_z` barrier between W and poly-Si.

The barrier is intended to suppress:
- inter-diffusion;
- P diffusion;
- Kirkendall-type vacancy defects;
- excessive interface resistance.

The paper also shows that very high N concentration can degrade the Gox interface and worsen GIDL, so the process variable has a trade-off rather than a monotonic optimum that can be transferred to CMP.

At a common 10 ppm fail criterion, the paper reports about a 0.3 V gate-voltage-margin difference between no-PNOF and high-N PNOF groups.

## 10. HF Wet Strip

HF wet strip (HFWS) is used after PNOF to remove N/Ti contamination and etch by-products from the Gox-sidewall region.

The paper reports that optimized HFWS removes only a small oxide thickness (approximately 1 nm) while reducing contaminants and lowering measured GIDL.

Again, this is a process-specific result and not a CMP oxide-thickness tuning instruction.

## 11. What CMP Can Reuse

- DWF can reduce the GIDL-relevant field while introducing WL-resistance/write trade-offs.
- Gate material, oxide process, barrier integrity, and interface contamination all affect the observed leakage/retention behavior.
- Local interface field behavior should not be confused automatically with the complete GIDL-critical spatial field profile.
- Future DWFG validation should evaluate both leakage/retention-side and write/RWL-side guardrails.
- Fabricated-device evidence strengthens the physical motivation for a multi-objective design window.

## 12. What CMP Cannot Directly Reuse

Do not transfer the following directly into the active PAPER-CAL lineage:

- REF02 dimensions as the CMP 20-nm baseline;
- 4.15 eV as the current CMP gate work function;
- PNOF/IAI/HFWS process parameters as TCAD calibration knobs;
- the paper's full physics stack as mandatory CMP physics;
- the reported 25% / 15% / 10% improvements as CMP improvements;
- the 0.3 V margin as a CMP write/read criterion;
- the paper's DWF optimum as the CMP MEB optimum.

## 13. Connection to CMP

- **Current single-WF mainline:** physical / claim-boundary context only.
- **Future DWFG branch:** primary process/device reference.
- **Retention translation:** supporting evidence that GIDL/process changes can affect fabricated DRAM retention behavior, but it does not replace CMP 1T1C execution.
- **RWL:** measured process context that reinforces why the current geometry-derived CMP RWL quantity must remain labeled a proxy.
- **3D / production claims:** fabricated device evidence is paper-specific and does not make CMP 2D or selected-point 3D production-equivalent.

## 14. Evidence Locations

Key published-PDF locations:

- p. 1: abstract, bibliographic metadata, license.
- pp. 2-3: DWF structure, dimensions, TCAD model list.
- p. 4: simulated c-BCAT vs DWF-BCAT field profile.
- pp. 6-8: IAI process and mass-wafer GIDL/Rwl results.
- pp. 9-14: PNOF barrier and gate-margin / GIDL trade-off.
- pp. 14-16: HFWS contamination removal and GIDL behavior.
- p. 16: conclusion / fabricated sub-17-nm DRAM retention characterization.

## 15. Claim Discipline

REF02 supports a **literature-level** statement that DWF/process engineering can modify GIDL, WL resistance/write behavior, and fabricated DRAM retention-related characteristics.

It does not establish that the active CMP MEB sweep has already produced retention improvement, refresh reduction, a production optimum, or a robust process window.
