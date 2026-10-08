# CMP TCAD CMD / Parameter Hub

> **Current 2D research branch:** `B0-2D-PAPER-CAL / C7_4 / B_QF_HALF`; post-freeze 300 K MEB Atlas (working production MeshLevel 2).  
> **Legacy history:** 기존 `B0-2D-Legacy / NonlocalPath` Run 0–7 인덱스는 아래에 내용 변경 없이 보존합니다.  
> **Research status:** [HANDOFF](HANDOFF.md) · [PROJECT_TIMELINE](PROJECT_TIMELINE.md) · [Atlas Evidence](docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md)

## 1. Current 2D Baseline SDE — PAPER-CAL 300 K Atlas

**[검토 완료 · 주석 정리 SDE CMD](code/sde/paper_cal/atlas_300k/CMP_B0_2D_PAPER_CAL_MEB_ATLAS_SDE.cmd)**

| Item | Implemented condition |
|---|---|
| Model lineage | `B0-2D-PAPER-CAL` reduced-order calibration, C7_4 / B_QF_HALF |
| SWB split | `MEBDepth = 31/33/36/39/41/42/43/44/45/46/47/48/49/50/51 nm` |
| SDE fixed | `MeshLevel = 2`, `GateCouplingScale = 2.300`, `GateDepthBoost = 0.025 um` |
| SDevice controls | `Qf_Int = 2.55e12 cm^-2`, Gate WF = 4.8 eV |
| Geometry / doping | Rounded buried W gate & SiO2, Gaussian source/drain |
| Mesh | Global + interface + compact S/D shoulder + GIDL Outer/Mid/Core |

- 위 SDE는 대화에서 검토·승인한 **주석 정리본**입니다. 실행 구문, 조건문, 메시 수치 및 QA 출력은 수정하지 않았습니다.
- **Provenance gate OPEN:** `2026-10-05 FZ-C`에서 실행한 정확한 parent SDE/SDevice/SVisual과 현재 Atlas 작업 계열의 mesh-only 동일성은 검증되지 않았습니다. SDE를 기록한 것이 곧 계보 검증 완료를 의미하지 않습니다.
- 300 K Atlas의 15-point DC/Cgd/GIDL/spatial 분석 및 QC는 **동일 작업 계열 내부에서 완료**. PAPER-CAL 온도·1T1C Retention과 최종 MEB 설계 범위는 아직 미완료입니다.

## 2. 2D PAPER-CAL Calibration / Validation Stages

아래 표는 **단계별 검증 흐름과 관련 기록**입니다. 원본 CMD 파일들은 이전 연구 대화에서 식별했으나, 현재 소스 파일 접근 장애 때문에 **원본 주석 보존을 검증한 GitHub 등록은 아직 완료하지 못했습니다.** 따라서 등록되지 않은 CMD로 연결하는 링크는 만들지 않았습니다.

| Stage | Verification purpose | Source of record |
|---|---|---|
| C5 — Global DOE | 2D reduced-order calibration 후보 탐색 | [Baseline Calibration](docs/research/b0_2d_baseline_reconstruction_calibration.md) |
| C6 — Local DOE | 128-case local calibration | [Baseline Calibration](docs/research/b0_2d_baseline_reconstruction_calibration.md) |
| C7 — Candidate confirmation | C7_4 / B_QF_HALF 결정 | [Baseline Calibration](docs/research/b0_2d_baseline_reconstruction_calibration.md) |
| FZ-A / FZ-B / FZ-C | Solver path, DC mesh, GIDL·BTBT·local-E freeze validation | [Freeze Plan](docs/research/b0_2d_final_freeze_plan.md) |
| Post-freeze mesh revalidation | NEW-MESH v1, L2/L3 comparison; exact-parent bridge OPEN | [Mesh Revalidation](docs/progress/b0_2d_paper_cal_mesh_revalidation_20261007.md) |
| H1–H1.5 historical debug | Local mesh debugging, **not validated production lineage** | [Mesh Debug Checkpoint](docs/progress/b0_2d_paper_cal_mesh_revalidation_20261007.md) |
| 300 K Atlas | DC005/DC12, 1 MHz Cgd, Hurkx ON/OFF, spatial BTBT, signed terminal extraction | [Atlas Evidence](docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md) |

**Pending original-comment CMD archive:** C5/C6/C7 SDE·SDevice·SVisual; C7_4 FZ-A/B/C decks; NEW-MESH Level-2/3 and H1 historical debugging; Atlas DC005/DC12/Cgd/GIDL ON/OFF SDevice·SVisual, corrected Cgd extractor and P2 v3. These files must be read in full and added **without deleting comments**; do not recreate their contents from descriptions. The explicitly unexecuted `CMP_MANUAL_OPT_MESH_SDE_v3.cmd` is **not** an executed validation source.

---

## 3. Historical B0-2D-Legacy — Original Run 0–7 CMD Hub

> 아래 본문은 이전 `CMD_HUB.md`의 Run 0–7 자료를 그대로 유지한 역사적 인덱스입니다. Run 7 Legacy 1T1C feasibility를 현재 PAPER-CAL의 Retention 검증으로 해석하지 않습니다.

## Run Index

| Run | Main scope | SDE | SDevice branches |
|---|---|---|---|
| Run 0 | B0 baseline | Baseline geometry | Baseline Id–Vg |
| Run 1 | DC metric freeze | Run 0 geometry reuse | Id–Vg metric freeze / Id–Vd output |
| Run 2 | DC mesh convergence | Mesh_Code 0 / 1 / 2 | DC mesh comparison |
| Run 3 | BTBT/GIDL feasibility | Mesh-GIDL construction | precheck / final BTBT ON / final BTBT OFF |
| Run 4 | Formal MEB 3-level screening | 31 / 36 / 41 nm, Mesh1/3 | GIDL screening / DC guardrail |
| Run 5A | Cgd extraction validation | Run 4 parameterized SDE reuse | AC smoke / bias-frequency sensitivity |
| Run 5B | 5-level correlation | 31 / 33.5 / 36 / 38.5 / 41 nm | Cgd / GIDL / DC guardrail |
| Run 6 | Temperature robustness | Run 4 parameterized SDE reuse | GIDL ON / BTBT OFF / thermal DC |
| Run 6.5 | Extended MEB boundary | 36–51 nm extended SDE | 300 K GIDL / Cgd / DC / thermal ON-OFF-DC |
| **Run 7** | **1T1C / retention feasibility & metric freeze** | **Run 6.5 parameterized SDE reuse; B0=36 nm** | **300 K W→H→R PASS; 300/340/380 K normalized direct Hold complete; final retention metric / Mesh1-3 checks pending** |

The raw SWB `pp*.cmd` node expansions remain in the local TCAD archive. GitHub keeps the reusable source/representative command for each reported branch, while the actual SWB split is recorded below.

---

<details>
<summary><strong>Run 0 — B0 Baseline</strong></summary>

### SDE

- [`code/sde/run00/bcat_baseline_sde_r0_v1.cmd`](code/sde/run00/bcat_baseline_sde_r0_v1.cmd)

### SDevice

- [`code/sdevice/run00/bcat_idvg_r0_verify.cmd`](code/sdevice/run00/bcat_idvg_r0_verify.cmd)

### Parameters

| Item | Value |
|---|---|
| Formal B0 MEB / GateTop | 36 nm |
| Gate length | 20 nm |
| Recess depth | 120 nm |
| Oxide liner | 5 nm |
| Gate work function | 4.8 eV |
| Temperature | 300 K |
| Baseline DC | `VD=0.05 V`, `VG=0→1.5 V` |

The retained early SWB project also contains a 31/36/41 nm MEB parameterization development check. The formal Run 0 baseline is 36 nm.

</details>

<details>
<summary><strong>Run 1 — DC Metric Freeze</strong></summary>

### SDE

Run 1 reuses the Run 0 B0 geometry:

- [`code/sde/run00/bcat_baseline_sde_r0_v1.cmd`](code/sde/run00/bcat_baseline_sde_r0_v1.cmd)

### SDevice — Id–Vg metric freeze

- [`code/sdevice/run01/bcat_idvg_r1_lowvd.cmd`](code/sdevice/run01/bcat_idvg_r1_lowvd.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 31 / 36 / 41 nm retained project parameterization |
| `VD_Target` | 0.05 / 1.0 V |
| `VG_MaxStep` | 0.010 / 0.005 V retained histories |
| Temperature | 300 K |
| BTBT | OFF |

The formal metric definitions are referenced to B0=36 nm.

### SDevice — Id–Vd output characteristic

- [`code/sdevice/run01/bcat_idvd_r1.cmd`](code/sdevice/run01/bcat_idvd_r1.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 36 nm |
| `VG_Bias` | 0.9 / 1.1 / 1.3 / 1.5 V |
| `VD_Target` | 1.0 V |
| Temperature | 300 K |
| BTBT | OFF |

</details>

<details>
<summary><strong>Run 2 — DC Mesh Convergence</strong></summary>

### SDE

- [`code/sde/run02/bcat_baseline_sde_r2_meshdc.cmd`](code/sde/run02/bcat_baseline_sde_r2_meshdc.cmd)

### SDevice

- [`code/sdevice/run02/bcat_idvg_r2_meshdc.cmd`](code/sdevice/run02/bcat_idvg_r2_meshdc.cmd)

### SWB matrix

| Parameter | Values |
|---|---|
| `MEB_Depth` | 36 nm |
| `Mesh_Code` | 0 / 1 / 2 |
| `VD_Target` | 0.05 / 1.0 V |
| `VG_MaxStep` | 0.010 V |
| Temperature | 300 K |
| BTBT | OFF |

`Mesh_Code=1` was selected as the formal Mesh-DC.

</details>

<details>
<summary><strong>Run 3 — BTBT/GIDL Feasibility and Mesh-GIDL</strong></summary>

### SDE — Mesh-GIDL

- [`code/sde/run03/bcat_baseline_sde_r3_meshgidl.cmd`](code/sde/run03/bcat_baseline_sde_r3_meshgidl.cmd)

### SDevice — initial precheck

- [`code/sdevice/run03/bcat_gidl_r3_precheck.cmd`](code/sdevice/run03/bcat_gidl_r3_precheck.cmd)
- [`code/sdevice/run03/bcat_gidl_r3_nonlocal.cmd`](code/sdevice/run03/bcat_gidl_r3_nonlocal.cmd)

| Parameter | Initial value |
|---|---|
| `MEB_Depth` | 36 nm |
| `Mesh_Code` | 1 |
| `VD_Target` | 1.0 V |
| `VG_Min` | -0.4 V |
| Temperature | 300 K |

### SDevice — final formal GIDL ON/OFF attribution

- BTBT ON: [`code/sdevice/run03/bcat_gidl_r3_final_nonlocal_on_executed_snapshot.cmd`](code/sdevice/run03/bcat_gidl_r3_final_nonlocal_on_executed_snapshot.cmd)
- BTBT OFF: [`code/sdevice/run03/bcat_gidl_r3_final_nonlocal_off_executed_snapshot.cmd`](code/sdevice/run03/bcat_gidl_r3_final_nonlocal_off_executed_snapshot.cmd)

| Parameter | Final value |
|---|---|
| `MEB_Depth` | 36 nm |
| `Mesh_Code` | 3 |
| `VD_Target1` | 1.2 V |
| `VG_Min1` | -0.7 V |
| Temperature | 300 K |
| Requested gate output | 5 mV spacing, 141 points |
| ON branch | `Band2Band(Model=NonlocalPath)` |
| OFF branch | NonlocalPath removed |

</details>

<details>
<summary><strong>Run 4 — Formal MEB 3-Level Screening</strong></summary>

### SDE

- [`code/sde/run04/bcat_sde_r4_meb_screening_executed_snapshot.cmd`](code/sde/run04/bcat_sde_r4_meb_screening_executed_snapshot.cmd)

The same parameterized SDE source is used with `Mesh_Code=3` for GIDL and `Mesh_Code=1` for DC.

### SDevice — GIDL

- [`code/sdevice/run04/bcat_gidl_r4_meb_screening_executed_snapshot.cmd`](code/sdevice/run04/bcat_gidl_r4_meb_screening_executed_snapshot.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 31 / 36 / 41 nm |
| `Mesh_Code` | 3 |
| `VD_Target1` | 1.2 V |
| `VG_Min1` | -0.7 V |
| Temperature | 300 K |
| BTBT | NonlocalPath ON |

### SDevice — DC guardrail

- [`code/sdevice/run04/bcat_dc_r4_meb_screening_executed_snapshot.cmd`](code/sdevice/run04/bcat_dc_r4_meb_screening_executed_snapshot.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 31 / 36 / 41 nm |
| `Mesh_Code` | 1 |
| `VD_Target` | 0.05 / 1.0 V |
| `VG_MaxStep` | 0.005 V |
| Temperature | 300 K |
| BTBT | OFF |

</details>

<details>
<summary><strong>Run 5 — Cgd Validation and 5-Level Correlation</strong></summary>

### SDE

Run 5 reuses the parameterized Run 4 / Mesh-GIDL-capable SDE source. The repository provenance note is:

- [`code/sde/run05/README.md`](code/sde/run05/README.md)
- source: [`code/sde/run04/bcat_sde_r4_meb_screening_executed_snapshot.cmd`](code/sde/run04/bcat_sde_r4_meb_screening_executed_snapshot.cmd)

### Run 5A — Cgd extraction validation

- AC smoke test: [`code/sdevice/run05/bcat_cov_r5a_ac_smoketest.cmd`](code/sdevice/run05/bcat_cov_r5a_ac_smoketest.cmd)
- `VD=1.2 V`, `VG=0 V`: [`code/sdevice/run05/bcat_cov_r5a_vd1p2_vg0_ac.cmd`](code/sdevice/run05/bcat_cov_r5a_vd1p2_vg0_ac.cmd)
- formal `VG≈-0.7 V`: [`code/sdevice/run05/bcat_cov_r5a_vd1p2_vgm0p7_ac.cmd`](code/sdevice/run05/bcat_cov_r5a_vd1p2_vgm0p7_ac.cmd)
- 100 kHz sensitivity: [`code/sdevice/run05/bcat_cov_r5a_vd1p2_vgm0p7_100khz.cmd`](code/sdevice/run05/bcat_cov_r5a_vd1p2_vgm0p7_100khz.cmd)
- 10 MHz sensitivity: [`code/sdevice/run05/bcat_cov_r5a_vd1p2_vgm0p7_10mhz.cmd`](code/sdevice/run05/bcat_cov_r5a_vd1p2_vgm0p7_10mhz.cmd)

Formal Cgd condition:

| Parameter | Value |
|---|---|
| `MEB_Depth` | 36 nm |
| `Mesh_Code` | 1 |
| `VD` | 1.2 V |
| `VG` | approximately -0.70 V |
| AC frequency | 1 MHz |
| BTBT | OFF |

### Run 5B — 5-level Cgd

- [`code/sdevice/run05/bcat_cov_r5b_parametric_ac.cmd`](code/sdevice/run05/bcat_cov_r5b_parametric_ac.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 31 / 33.5 / 36 / 38.5 / 41 nm |
| `Mesh_Code` | 1 |
| `VD_AC` | 1.2 V |
| `VG_START` | -0.71 V |
| `VG_END` | -0.69 V |
| `AC_Freq` | 1 MHz |

### Run 5B — 5-level GIDL

- [`code/sdevice/run05/bcat_gidl_r5b_5level_parametric.cmd`](code/sdevice/run05/bcat_gidl_r5b_5level_parametric.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 31 / 33.5 / 36 / 38.5 / 41 nm |
| `Mesh_Code` | 3 |
| `VD_Target1` | 1.2 V |
| `VG_Min1` | -0.7 V |
| Temperature | 300 K |
| BTBT | NonlocalPath ON |

### Run 5B — DC guardrail

- [`code/sdevice/run05/bcat_dc_r5b_intermediate_guardrail.cmd`](code/sdevice/run05/bcat_dc_r5b_intermediate_guardrail.cmd)

| Parameter | Values |
|---|---|
| new intermediate `MEB_Depth` | 33.5 / 38.5 nm |
| `Mesh_Code` | 1 |
| `VD_Target` | 0.05 / 1.0 V |
| `VG_MaxStep` | 0.005 V |
| Temperature | 300 K |
| BTBT | OFF |

31/36/41 nm formal DC values are inherited from the Run 4 protocol.

</details>

<details>
<summary><strong>Run 6 — Elevated-Temperature Robustness</strong></summary>

### SDE

Run 6 does not create a new geometry generator.

- provenance: [`code/sde/run06/README.md`](code/sde/run06/README.md)
- source: [`code/sde/run04/bcat_sde_r4_meb_screening_executed_snapshot.cmd`](code/sde/run04/bcat_sde_r4_meb_screening_executed_snapshot.cmd)

### R6A — GIDL ON temperature matrix

- [`code/sdevice/run06/bcat_gidl_r6a_temperature_on_parametric.cmd`](code/sdevice/run06/bcat_gidl_r6a_temperature_on_parametric.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 31 / 36 / 41 nm |
| `Mesh_Code` | 3 |
| `Temp_K` | 300 / 340 / 380 K |
| `VD_Target1` | 1.2 V |
| `VG_Min1` | -0.7 V |
| BTBT | NonlocalPath ON |

### R6B — BTBT-OFF background control

- [`code/sdevice/run06/bcat_gidl_r6b_temperature_off_parametric.cmd`](code/sdevice/run06/bcat_gidl_r6b_temperature_off_parametric.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 36 / 41 nm |
| `Mesh_Code` | 3 |
| `Temp_K` | 300 / 340 / 380 K |
| `VD_Target1` | 1.2 V |
| `VG_Min1` | -0.7 V |
| BTBT | OFF |

### R6C — DC thermal guardrail

- [`code/sdevice/run06/bcat_dc_r6c_temperature_guardrail.cmd`](code/sdevice/run06/bcat_dc_r6c_temperature_guardrail.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 36 / 41 nm |
| `Mesh_Code` | 1 |
| `Temp_K` | 340 / 380 K |
| `VD_Target` | 0.05 / 1.0 V |
| `VG_MaxStep` | 0.005 V |
| BTBT | OFF |

The formal 300 K DC values are reused from the Run 4/5 DC path.

</details>

<details>
<summary><strong>Run 6.5 — Extended MEB Boundary Closure</strong></summary>

### SDE

- [`code/sde/run06_5/bcat_sde_r65_deeper_meb_boundary.cmd`](code/sde/run06_5/bcat_sde_r65_deeper_meb_boundary.cmd)

### 300 K extended GIDL ON

- [`code/sdevice/run06_5/bcat_gidl_r65_deeper_meb_300k.cmd`](code/sdevice/run06_5/bcat_gidl_r65_deeper_meb_300k.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 36 / 41 / 43 / 45 / 47 / 48 / 49 / 51 nm |
| `Mesh_Code` | 3 |
| `Temp_K` | 300 K |
| `VD_Target1` | 1.2 V |
| `VG_Min1` | -0.7 V |
| BTBT | NonlocalPath ON |

### 300 K extended Cgd

- [`code/sdevice/run06_5/bcat_cgd_r65_deeper_meb_300k_1mhz.cmd`](code/sdevice/run06_5/bcat_cgd_r65_deeper_meb_300k_1mhz.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 36 / 41 / 43 / 45 / 47 / 48 / 49 / 51 nm |
| `Mesh_Code` | 1 |
| `VD_AC` | 1.2 V |
| `VG_START` | -0.71 V |
| `VG_END` | -0.69 V |
| `AC_Freq` | 1 MHz |
| BTBT | OFF |

### 300 K DC guardrail

- [`code/sdevice/run06_5/bcat_dc_r65_300k_guardrail.cmd`](code/sdevice/run06_5/bcat_dc_r65_300k_guardrail.cmd)

| Parameter | R6.5 reporting values |
|---|---|
| `MEB_Depth` | 48 / 49 / 51 nm |
| `Mesh_Code` | 1 |
| `VD_Target` | 0.05 / 1.0 V |
| `VG_MaxStep` | 0.005 V |
| Temperature | 300 K |
| BTBT | OFF |

### BTBT-OFF diagnostic

- [`code/sdevice/run06_5/bcat_gidl_r65_temperature_off_parametric.cmd`](code/sdevice/run06_5/bcat_gidl_r65_temperature_off_parametric.cmd)

| Purpose | MEB | Temperature |
|---|---|---|
| extended 300 K boundary control | 36 / 41 / 47 / 48 / 49 / 51 nm | 300 K |
| thermal background control | 36 / 41 / 48 / 49 nm | 300 / 340 / 380 K |

Common settings: `Mesh_Code=3`, `VD_Target1=1.2 V`, `VG_Min1=-0.7 V`, NonlocalPath removed.

### 48/49 nm elevated-temperature GIDL ON

- [`code/sdevice/run06_5/bcat_gidl_r65_temperature_on_parametric.cmd`](code/sdevice/run06_5/bcat_gidl_r65_temperature_on_parametric.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | retained project: 31 / 36 / 41 / 48 / 49 nm |
| `Mesh_Code` | 3 |
| `Temp_K` | 300 / 340 / 380 K |
| `VD_Target1` | 1.2 V |
| `VG_Min1` | -0.7 V |
| BTBT | NonlocalPath ON |

### Thermal DC guardrail

- [`code/sdevice/run06_5/bcat_dc_r65_temperature_guardrail.cmd`](code/sdevice/run06_5/bcat_dc_r65_temperature_guardrail.cmd)

| Parameter | Values |
|---|---|
| `MEB_Depth` | 36 / 41 / 48 / 49 nm |
| `Mesh_Code` | 1 |
| `Temp_K` | 340 / 380 K |
| `VD_Target` | 0.05 / 1.0 V |
| `VG_MaxStep` | 0.005 V |
| BTBT | OFF |

</details>

<details>
<summary><strong>Run 7 — 1T1C / Retention Feasibility & Metric Freeze</strong></summary>

> Status: **In Progress — 300 K integrated Write→Hold→Read completed; ~1 V-normalized 300/340/380 K direct Hold completed; final retention metric and numerical close-out pending.**  
> Run 7 remains a B0 protocol-freeze stage. Formal MEB cell comparison begins after the retention metric is sufficiently frozen.

### SDE provenance

Run 7 creates no new geometry generator.

- Run-specific provenance note: [`code/sde/run07/README.md`](code/sde/run07/README.md)
- inherited parameterized source: [`code/sde/run06_5/bcat_sde_r65_deeper_meb_boundary.cmd`](code/sde/run06_5/bcat_sde_r65_deeper_meb_boundary.cmd)

Formal R7 SDE use:

| Parameter | Value / role |
|---|---|
| `MEB_Depth` | `0.036 um` fixed |
| `Mesh_Code` | `1` smoke/write/read; `3` final hold/retention check |

### SDevice branch index

- branch/readme: [`code/sdevice/run07/README.md`](code/sdevice/run07/README.md)
- R7A/R7B AreaFactor + write screening: [`code/sdevice/run07/bcat_1t1c_r7_write_screen.cmd`](code/sdevice/run07/bcat_1t1c_r7_write_screen.cmd)
- R7C write → floating-SN hold: [`code/sdevice/run07/bcat_1t1c_r7_cell_transient.cmd`](code/sdevice/run07/bcat_1t1c_r7_cell_transient.cmd)
- R7D `Ileak(VSN)` NonlocalPath ON: [`code/sdevice/run07/bcat_retention_r7_ivsn_integral_on.cmd`](code/sdevice/run07/bcat_retention_r7_ivsn_integral_on.cmd)
- R7D BTBT-OFF reference: [`code/sdevice/run07/bcat_retention_r7_ivsn_integral_off.cmd`](code/sdevice/run07/bcat_retention_r7_ivsn_integral_off.cmd)
- R7E BL/SN charge-sharing read: [`code/sdevice/run07/bcat_1t1c_r7_read_guardrail.cmd`](code/sdevice/run07/bcat_1t1c_r7_read_guardrail.cmd)
- retention integral postprocess: [`code/scripts/extraction/run07_retention_integral.py`](code/scripts/extraction/run07_retention_integral.py)

### Latest Run-7 synchronization — 2026-09-22

Executed reference anchors:

```text
AreaFactor = 0.017
Ccell      = 10 fF
VBL_WRITE  = 1.2 V
VWL_ON     = 3.0 V
300 K Twrite ≈ 667 ns → VSN ≈ 1 V
340 K Twrite ≈ 258 ns → VSN ≈ 1 V
380 K Twrite ≈ 126.54 ns → VSN ≈ 1 V
```

The high `VWL_ON=3.0 V` requirement is now an explicit write-transfer guardrail. Do not interpret “VSN reached 1 V” as a complete write-performance validation.

Latest evidence:
- `docs/evidence/run07_write_1v_calibration_20260914.md`
- `docs/evidence/run07_cell_operation_checkpoint_20260920.md`
- `docs/evidence/run07_hold_temperature_normalized_20260921.md`

### Circuit mapping

```text
source -> BL
drain  -> SN
gate   -> WL
substrate -> reference
SN -> Ccell -> reference
```

### Staged SWB matrix

Run 7 is not a full-factorial DOE. Execute the branches sequentially.

| Branch | Fixed | Split / candidate |
|---|---|---|
| R7A Scaling | B0, 300 K, Mesh1 | `AreaFactor=0.011/0.017/0.023` |
| R7B Write | `Ccell=10 fF`, Mesh1 | `VWL_ON=1.5/2.0/2.5/3.0 V`; `VBL_WRITE=1.2 V`; `Twrite=10 ns` reviewed, `100 ns` follow-up prepared |
| R7C Hold | selected write condition | `Mesh_Code=1/3`; staged `HoldTime`; `HoldMaxStep` set per stage |
| R7D Retention | Mesh3, `VSN=0.8→1.0 V` | NonlocalPath ON / OFF paired decks |
| R7E Read | `Ccell=10 fF`, `CBL=45 fF`, `VBL_READ=0.5 V` candidates | `VSN_INIT=0.0/0.8/1.0 V` |
| R7F Repeatability | final nominal protocol | repeat selected final node(s) |

### Parameter status during execution

| Parameter | Status | Current value / role |
|---|---|---|
| `MEB_Depth` | Freeze | `0.036 um` |
| Temperature | Freeze | `300 K` |
| Gate WF | Freeze | `4.8 eV` |
| base physics | Freeze | existing CMP NonlocalPath-compatible B0 physics |
| `AreaFactor` | In progress | nominal candidate `0.017`; `0.011/0.023` one-time sensitivity; final numeric freeze pending |
| `Ccell_F` | Candidate baseline | `1.0e-14 F` |
| `VBL_WRITE` | Candidate | `1.2 V` |
| `VWL_ON` | 10 ns screened range | `1.5/2.0/2.5/3.0 V` |
| `Twrite` | In progress | `1.0e-8 s` reviewed; `1.0e-7 s` follow-up matrix prepared locally |
| `VWL_HOLD` | Candidate | `-0.7 V`, GIDL-consistent project stress |
| `CBL_F` | Read diagnostic | `4.5e-14 F` reference only |
| `VBL_READ` | Read candidate | `0.5 V` |
| `VSN_INIT` | Read states | `0.0/0.8/1.0 V` |
| retention window | Primary candidate | `RT_1p0_0p8`: 1.0 → 0.8 V |
| Cho threshold | Reference only | `0.698 V`, not CMP production calibration |

### Executed write-feasibility snapshot

Visually reviewed 10 ns write nodes:

| AreaFactor | `VWL_ON` | Local result node | Status |
|---:|---:|---|---|
| 0.011 | 1.5 V | `n71` | reviewed |
| 0.011 | 2.0 V | `n153` | reviewed |
| 0.011 | 2.5 V | `n162` | reviewed |
| 0.011 | 3.0 V | `n171` | reviewed |
| 0.017 | 1.5 V | `n134` | reviewed |
| 0.017 | 2.0 V | `n156` | reviewed |
| 0.017 | 2.5 V | `n165` | reviewed |
| 0.017 | 3.0 V | `n174` | reviewed |

Verified qualitative behavior:

- MixedMode transient converges with the intended BL/SN/WL mapping.
- BL and WL pulses are generated as requested.
- `VSN(t)` charges smoothly in the intended direction.
- Increasing `VWL_ON` strengthens the 10 ns charging response in both reviewed AreaFactor blocks.
- All reviewed 10 ns cases remain below the candidate `VSN≈1.0 V` D1 level; the write condition is therefore not frozen.
- Exact `VSN_write` extraction and the full 3-level AreaFactor comparison remain pending.

Local follow-up prepared:

```text
Twrite = 100 ns
AreaFactor = 0.011 / 0.017 / 0.023
VWL_ON = 1.5 / 2.0 / 2.5 / 3.0 V
```

This 12-node follow-up matrix is not treated as analyzed evidence until completion/export is checked.

Detailed evidence/provenance:

- [`docs/evidence/run07_write_feasibility_interim_20260903.md`](docs/evidence/run07_write_feasibility_interim_20260903.md)
- [`docs/progress/run07_1t1c_retention_feasibility.md`](docs/progress/run07_1t1c_retention_feasibility.md)

### Output prefix / SVisual note

The write deck uses:

```text
NewCurrentPrefix="R7_WRITE_"
```

so transient system waveforms are stored as:

```text
R7_WRITE_n<node>_sys_des.plt
```

The unprefixed `n<node>_sys_des.plt` can contain only the initial `t=0` coupled records. Use the prefixed system plot for write-transient review/export.

### Remaining Run 7 work

- finish/export 100 ns write matrix;
- freeze nominal AreaFactor and write condition;
- execute first floating-SN hold;
- Mesh1/3 hold/retention comparison;
- `Ileak(VSN)` and `RT_1p0_0p8,int`;
- NonlocalPath ON/OFF cell attribution;
- read charge-sharing guardrail;
- final repeatability close-out.

</details>

---

## Recording Rule

- `code/sde/` and `code/sdevice/` store the reusable source or representative executed command.
- `CMD_HUB.md` records the SWB split used or prepared for the reported Run.
- Node-expanded `pp*.cmd`, `.tdr`, `.plt`, full logs, and jobs remain in the local TCAD archive unless a specific provenance issue requires them.
- If a later Run reuses an earlier source unchanged, the Hub either links the inherited source directly or keeps a Run-specific representative copy when that improves auditability.
- A completed Run result is not added to the Hub as evidence unless its source command and parameter condition can be traced to the TCAD archive or an already committed source.
- Historical prepared decks remain documented for provenance. Current committed evidence now includes 300 K integrated Write→Hold→Read and approximately normalized 300/340/380 K direct Hold; final leakage-vs-V retention metric and retention Mesh1/3 close-out remain pending.
