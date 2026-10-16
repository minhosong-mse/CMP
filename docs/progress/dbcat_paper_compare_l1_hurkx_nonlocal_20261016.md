# 2026-10-16 — L1 2D D_BCAT paper-figure comparison: Hurkx vs NonlocalPath

> **Status: CMP-EXECUTED, source-checked transfer/output curves; PROVISIONAL scientific interpretation. NO re-freeze.** Experimentally collected 2026-10-15–16; uploaded 2026-10-16. This checkpoint is a separate PAPER-CAL-derived L1 comparative run, not a replacement of the frozen `B0-2D-PAPER-CAL C7_4/B_QF_HALF` lineage.

## 1. Question and controlled setup

The user requested a direct paper-figure gate before proceeding to GIDL–Retention: compare Sun et al. (Micromachines 2022, 13, 1476, DOI 10.3390/mi13091476) at **D_BCAT=24/36/48 nm** to **matched 2D L1 Hurkx and NonlocalPath**. The input BCAT structural parameter is **nitride cap above tungsten / gate-top recession**, *not silicon oxide thickness*; in this reduced 2D representation `MEBDepth=0.024/0.036/0.048 um` is a structural analogue, **not automatic 3D equivalence**.

Common **CMP-calibrated effective coordinates**: GateCouplingScale 2.3; GateDepthBoost 0.025 um; Qf_Int +2.55e12 cm^-2; gate work function 4.8 eV; Jdepth 0.048 um; 300 K; same L1 SDE family, SDevice models swapped using `Band2Band(Model=Hurkx)` or `Band2Band(Model=NonlocalPath)`. NonlocalPath vs Hurkx comparison is controlled *within the newly provided figure-reproduction deck family*; do not assume byte identity with the historical 2026-10-08 Hurkx Atlas.

- **IDVG transfer (3 depths × 2 models intended):** V_D=+1.2 V, gate trajectory 0→−1→+2 V; nominal comparison curve −1→+2 V.
- **IDVD output (3 depths × 3 fixed VG × 2 models):** V_G = +0.1/+0.6/+1.2 V, drain 0→+2 V.
- **Actual completed:** NonlocalPath 3/3 IDVG + 9/9 IDVD = **12/12**, **3,612** terminal points; Hurkx 2/3 IDVG (36,48 nm only) + 9/9 IDVD = **11/12**, **3,011** terminal points.
- **Total usable 23/24 curves, 6,623 original terminal points**; the failed 24-nm Hurkx IDVG is excluded, including any partial transfer curve. All complete curves have source CMD/log/PLT in user-provided collection archives; matched transfer/output bias checkpoints were checked in the extraction pass.
- SWB project names: `MEB_nonlocal_IDVG`, `MEB_nonlocal_IDVD`; Hurkx project folders are collector-assigned `HK_IDVG` / `HK_IDVD` in the resulting archive. Original archive names and hashes below.

## 2. Direct CMP measurements (|total drain current|, A/um)

### Transfer, V_D=1.2 V

| model | MEB nm | VG −1 V | VG 0 V | VG +1.2 V | VG +2 V |
|---|---:|---:|---:|---:|---:|
| NonlocalPath | 24 | 3.2862822e-7 | 9.4085803e-11 | 2.1278090e-4 | 5.8575031e-4 |
| NonlocalPath | 36 | 7.7845983e-12 | 4.0464952e-14 | 2.1122205e-4 | 5.7306488e-4 |
| NonlocalPath | 48 | 2.4794814e-15 | 3.0869596e-14 | 2.0928816e-4 | 5.4998600e-4 |
| Hurkx | 24 | **FAILED** | **FAILED** | **FAILED** | **FAILED** |
| Hurkx | 36 | 8.4306099e-12 | 4.0706287e-14 | 2.1122205e-4 | 5.7306488e-4 |
| Hurkx | 48 | 2.9888298e-13 | 3.0882062e-14 | 2.0928816e-4 | 5.4998600e-4 |

### Output, V_D=+2.0 V; each cell |total drain current| (A/um)

| model | MEB nm | VG=0.1 V | VG=0.6 V | VG=1.2 V |
|---|---:|---:|---:|---:|
| NonlocalPath | 24 | 1.9795581e-7 | 2.0699693e-6 | 2.2109476e-4 |
| NonlocalPath | 36 | 3.5205947e-11 | 2.0761493e-6 | 2.2024646e-4 |
| NonlocalPath | 48 | 8.7732072e-13 | 2.1014444e-6 | 2.1908539e-4 |
| Hurkx | 24 | 1.9795647e-7 | 2.0699693e-6 | 2.2109476e-4 |
| Hurkx | 36 | 3.5224183e-11 | 2.0761493e-6 | 2.2024646e-4 |
| Hurkx | 48 | 8.9930412e-13 | 2.1014444e-6 | 2.1908539e-4 |

Refer to the separately committed checkpoint CSV for machine-readable numeric evidence; these are **specific bias checkpoints, not a replacement for the full 23 curves**.

## 3. Figure-to-figure interpretation and limits

- At positive/on gate, both models are nearly indistinguishable, because the tunneling model scarcely changes the high-current channel response. Example VG=1.2/VD=2.0: MEB **24 > 36 > 48** in both, like the order of the paper output panel.
- At VG=0.6 V and VD=2 V, the two models instead show **24 < 36 < 48**, opposing the visually inferred paper D_BCAT order. The magnitude of the differences is small, and paper curve values are not available as raw published points.
- At VG=0.1 V and VD=2 V, current falls very sharply as MEB deepens: 24 nm (~2e-7) >> 36 nm (~3.5e-11) > 48 nm (~9e-13). The paper depicts a much more closely grouped family. This is a **reduced-order 2D sensitivity discrepancy**, not a validated mechanism.
- In the negative-gate transfer region, **36-nm Hurkx and NonlocalPath are close** at VG−1, but at 48 nm Hurkx (~2.99e-13) >> NonlocalPath (~2.48e-15); the 24-nm Hurkx transfer curve has no complete evidence. This cannot support an overall model winner.
- **Critical source-quality distinction:** Previously shown `paper_idvg_approx_digitized.csv`, `paper_idvd_approx_digitized.csv`, and 3-way overlay PNGs came from manually drawn visual anchors and interpolation, **not measured/published paper numerical samples or systematic digitization**. They are **illustrations only** and deliberately **NOT deposited as quantitative literature evidence**. Original Sun Fig. 2/3 and publication explicit nominal numbers remain the real literature references. Precise 3-way quantitative goodness-of-fit is **NOT DEMONSTRATED**.
- Paper 3D nominal reference: Vth ~0.656 V; SS ~76 mV/dec; Ion/Ioff ~3.4e10; DIBL ~23.6 mV/V. Exact SS/current/low-VD DIBL extraction conventions and paper's own textual-versus-figure trend description need careful annotation; **do not force-fit** an internally unresolved paper label or bias discrepancy.

## 4. Hurkx 24-nm failure (separate numerical issue)

Hurkx `n78_des(1).log` (SDevice T-2022.03) explicitly identifies **Hurkx**. The drain ramp to VD1.2 and 0→−1-V gate sweep reached their endpoints, but during −1→+2-V continuation the solve stalled near **VG≈+0.0395 V** (last accepted total Id ~6.275e-11 A/um), repeated Newton and step reduction attempts exhausted MinStep. `simulation finished` in the log does **not** certify curve completion. A damped full-sweep and independent forward-only retry also user-reported failed; no successful 24-nm Hurkx transfer curve is claimed. This does not prove the physical geometry is wrong. Preserve this failure in any future evaluation; optional recovery only if needed for a specific comparison.

## 5. Proposed research pivot, not adopted/frozen

User suggested prioritizing runtime and 3D validation over forcing exact 3D paper numbers from an effective 2D model. **Scientifically defensible PROPOSAL**:

1. Reuse existing frozen `B0-2D-PAPER-CAL` and faster validated production mesh/solver for **2D MEB pre-screening** only. A *screening candidate range* is not a certified **effective MEB range**, especially while BTBT integral/total-drain-background and retention mechanisms are unresolved.
2. **Do not build 3D from zero**: existing `3D-Sun-B0` literature-consistent reconstruction and its F1 DC mesh comparison already exist (`data/baseline_3d_sun_b0/`, `code/sde/baseline_3d_sun_b0/`). That 3D model was itself **not electrically calibrated to paper exact numbers**.
3. Run a small **36-nm 2D↔3D bias/model/normalization bridge first**, ideally same measurement and comparable physical physics before attributing a change to dimensionality; then selected **24/48 nm or nominal/candidate/boundary** 3D sensitivity checks with actual same-bias curves and drain-side electrostatics/GIDL.
4. If 2D and 3D rank similarly on defensible quantities, use 2D for high-volume relative DOE and 3D for select-point mechanism checks. If trend diverges, report the 2D-to-3D non-transferability; do not force paper fitting, claim an optimum, or publish a physically validated range.
5. Only then continue 300/340/380 K GIDL → 1T1C Retention with explicit model dependence, collector mapping, ON−OFF/background accounting and 3D selected-point fidelity.

**Current stage: PROVISIONAL interpretation / 3D-bridge proposal; no official reranking, new baseline freeze, 3D reproduction claim, paper metric acceptance, effective-range selection, or retention benefit claim.** Prior `HANDOFF.md` and `docs/RUN_SHEET.md` milestones remain historical.

## 6. Evidence provenance and reproducibility

Authoritative user-delivered collector ZIPs (not yet stored as raw public GitHub attachments; preserved in ChatGPT project):

| Source | SHA-256 |
|---|---|
| `CMP_NONLOCAL_RESULTS_20261016.zip` | `f0cc9fc179c1e7abfb29f8c20d9fba4be26be22dd48e8557a6c8cb32dd590914` |
| `CMP_HURKX_RESULTS_20261016.zip` | `11bb41bdfb1b1b7e49ea1cd8ec654c344371e9b7c6617c8938a0740991079a7b` |
| `CMP_NONLOCAL_12NODE_EXTRACT_20261016.zip` | `d131daceea1034d9b281f262a3f5af3adaa31b39de8eb6e06fe9b9463e84e863` |
| `CMP_HURKX_11NODE_EXTRACT_20261016.zip` | `dd10177ff0ecc8143de9c3151ad056697cdd340f8a4b540f8905dd38cfa34e97` |

Full validated CSVs in extraction ZIP: `NONLOCAL_IDVG_24_36_48nm.csv` (1803 rows); `NONLOCAL_IDVD_9CURVES.csv` (1809); `HURKX_IDVG_36_48nm.csv` (1202); `HURKX_IDVD_9CURVES.csv` (1809). SHA-256 by file:

- NL IDVG: `41b02029c2f877e19cb8235f1d4ae49c77af7b9905ec4ff4e24b767bd4d38f8b`
- NL IDVD: `4366ce2fe79e9f207a57f0752e56242e6073068d3117625ad035f3e88f38dc00`
- HK IDVG: `8f239b1bf76a1d36603d787572c1a42d45fe1e81405a26e8982c4ac7c3b399ea`
- HK IDVD: `862650581594bf96978ca54025e396773ac085e1970ec35fe55dad184a93363e`

Repository index: [data checkpoint](../../data/dbcat_figure_2d_20261016/README.md) · [numerical checkpoints](../../data/dbcat_figure_2d_20261016/terminal_checkpoints.csv) · [replot script](../../code/analysis/plot_dbcat_figure_2d_20261016.py) · [compact evidence chart](../../assets/images/paper_cal/dbcat_20261016/idvd_vd2_meb_comparison.svg) · [previous dual-mesh DC dispatch](nonlocalpath_mesh_dc_dispatch_20261014.md) · [existing 3D model evidence](../../data/baseline_3d_sun_b0/README.md).

**README.md, DECISIONS.md, prior calibrated baseline and previous evidence unchanged.**
