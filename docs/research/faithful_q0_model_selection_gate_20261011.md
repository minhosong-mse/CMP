# CMP model-selection credibility gate — 2026-10-11

**Decision status:** **PROVISIONAL STRATEGY REVIEW / NO BASELINE RE-FREEZE.** Not a new executed Sentaurus run. Discussion conducted after Q0 300 K 15-depth cross-model audit and Q0 surface-refinement Level-1 experiment. Source evidence: `data/faithful_q0/20261011_300k/`, `data/paper_cal/atlas_300k_20261008/`, historical `docs/research/b0_2d_baseline_reconstruction_calibration.md`, `docs/evidence/paper_cal_g0_parent_spatial_bridge_20261008.md`.

## Scientific question

We calibrated GCS=2.3, GateDepthBoost=25 nm, Qf_Int=2.55e12 cm^-2 to match the *paper DC benchmarks* (nominal Vth≈0.6557 V vs 0.656 V; SS≈75.83 vs 76 mV/dec; DIBL≈23.29 vs 23.6 mV/V; Ion/Ioff still differs). These are reduced-order **effective 2D electrostatic coordinates**, not physical fabricated oxide/recess/known measured interface charge. Matching channel DC curves does **not** establish predictive validity for high-drain, negative-gate local band-to-band tunneling.

## Executed evidence at 300 K (GIDL endpoint VD=1.2V, VG=-0.7V)

| Model | 36-nm total drain Id (A/um) | 36-nm Hurkx ON−OFF fraction | 36-nm integrated BTBT | BTBT peak/trend |
|---|---:|---:|---:|---|
| PAPER-CAL Atlas L2 | 1.08856e-12 | 16.9402% | 1.15103e6 | whole-Si integral maximum at 39 nm; hotspot travels with GateTop |
| Faithful-Q0 original L2 | 9.92365e-10 | 0.00009833% | 8.62068e3 | whole-Si integral decreases with deeper MEB; near-surface hotspot at X~2.34 nm after 33 nm |
| Faithful-Q0 Surface-L1 | 1.46529e-9 | 0.00006903% | 7.09676e3 | original Q0 structure unchanged; near-surface hotspot X~2.34 nm all 15 MEB |

The physical Hurkx model is **the same** in PAPER-CAL and Q0; effective electrostatic calibration / modeled geometry and mesh are different. Q0 Level0→SurfaceL1 changes 36-nm total drain Id +47.66%, integrated BTBT −17.68%, and 48-nm integrated BTBT −75.81%; Level1 mesh **has not been shown converged**. Q0 15-depth extracted source QC passed, but material validity did not. Q0 total Id remains >99.9999% BTBT-OFF residual in these conditions; SDevice log drain electron ON−OFF roughly matches `q∫BTBT` while drain-hole component dominates total; microscopic OFF residual source NOT identified.

Also PAPER-CAL's historical FZ-C Mesh2 vs later Atlas L2 are NOT numerically interchangeable (nominal 36-nm drain Id +86.86%, integrated BTBT −64.64% for Atlas); this confound may not be assigned exclusively to cell physics or mesh density. Comparisons must remain lineage-labeled.

## Evidence-supported vs unsupported claims

- **Supported within models:** deeper MEB lowers measured total GIDL-bias drain current and gate-drain coupling `|Cgd|` over the sampled 2D conditions. Original Q0 Cgd available 14/15 (31-nm SVisual summary missing); no Surface-L1 Cgd was executed.
- **Supported warning:** PAPER-CAL and faithful-dimension Q0 yield incompatible BTBT spatial maxima, integrated generation trend, Hurkx ON−OFF current sensitivity. Global total-drain current must not be labeled pure BTBT current.
- **Not yet established:** which 2D model is closer to real 3D BCAT, whether GCS/GDB/Qf alone cause the discrepancy, whether PAPER-CAL's 39-nm nonmonotonic spatial BTBT exists in a 3D reference, any retention gain, and an effective 48-nm optimum.
- **No automatic promotion:** good DC calibration is evidence of calibrated DC; faithful dimensions are evidence of dimensional fidelity, not of calibrated DC/GIDL. Neither alone is an experiment-calibrated 3D reference.

## Recommended staged research gate (PROPOSED; not run)

1. **Numerical floor with bounded cost:** Q0 Surface-L1→L2 at **36 and 48 nm** ON/OFF/spatial, include original TDRs, terminal electron/hole components, normalization/AreaFactor and solver precision. Add 31 nm only if hotspot switching must be qualified; 41/51 nm as boundary points if needed. Audit comparable PAPER-CAL Atlas L2 mesh family selectively. No automatic all-15 rerun.
2. **Direct attribution test:** at **36 nm**, control GCS, GDB, Qf independently, preferably full 2^3 combinations if interactions become material. Hold physically explicit Tox/junction/doping, mobility, Hurkx model and bias definition per lineage. Mesh coverage must follow actual hotspot for **each** combination; never alter frozen original PAPER-CAL history to make output agree.
3. **Earlier selected-point 3D bridge:** compare a literature-consistent `3D-Sun-B0` at **36/48 nm** for relative Id_ON, ON−OFF, drain electron/hole, spatial BTBT distribution and DC trends. This 3D model itself does **not** reproduce Sun paper's DC headline exactly (e.g., nominal high-Vd Vth≈1.1466 V), so it is a *higher-dimensional consistency anchor*, not experimental truth. A single 3D point cannot validate an MEB optimum.
4. **Choose follow-on 2D model only after gates:** use PAPER-CAL as DC-matched surrogate and Faithful-Q0 as dimensionally constrained control until the comparisons discriminate them. If neither 2D branch tracks 3D mechanism/ranking, keep the mechanistic claim unresolved and reconsider model scope; do not pick whichever curve resembles a preferred claim.
5. Only then resume PAPER-CAL or justified alternative model's 1T1C Write/Hold/Read and 233/300/340/380 K retention translation, including drain-bias dependence, read margin and structural RWL proxy constraints. Existing thermal/DC data preserved; new large-run sweep not first action.

## Session status and guardrails

`2026-10-11` data collection and source-QC **COMPLETE** for the cited 15-depth Q0 cases; model-selection / mesh convergence / retention mechanism **PAUSED—PROVISIONAL**. Existing `B0-2D-PAPER-CAL = C7_4/B_QF_HALF` remains FROZEN; legacy R0–R7 historical results unchanged. This memo is a proposal for research sequencing, **not an executed 3D, an approved re-calibration, or an adopted replacement baseline**.

Primary evidence: [Faithful-Q0 comparative data](../../data/faithful_q0/20261011_300k/README.md) and [PAPER-CAL Atlas](../../data/paper_cal/atlas_300k_20261008/processed/MEB_300K_ATLAS_MASTER_VALIDATED.csv).
