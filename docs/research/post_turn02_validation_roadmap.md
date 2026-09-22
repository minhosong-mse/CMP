# Post-Turn-02 Validation Roadmap

> Date: 2026-09-22  
> Scope: research-direction synchronization after the second CMP presentation and mentor feedback.

## 1. Canonical research title

**20 nm급 BCAT DRAM에서 MEB 깊이에 따른 GIDL–Retention 전달 특성 및 온도 의존적 유효 설계 범위 도출**

**Temperature-Dependent Effective MEB Design Range Based on GIDL-to-Retention Translation in 20 nm-Class BCAT DRAM**

The main independent design variable remains **MEB depth**.

Cold temperature and DWFG are downstream validation axes. They are not promoted to completed results before execution.

## 2. Three-phase research hierarchy

### Phase 1 — Single-WF MEB design range

```text
20 nm-class single-WF BCAT
→ MEB depth
→ project-internal Cgd / coupling
→ hotspot-resolved spatial E-field
→ BTBT / GIDL
→ 1T1C retention translation
→ write/read + RWL guardrails
→ SG effective MEB candidate / range
```

The current 20 nm single-WF framework remains the baseline of record. Existing 2D results are not discarded when later DWFG validation is added.

### Phase 2 — Temperature robustness / translation

```text
Phase-1 MEB candidates
→ 233 / 300 / 340 / 380 K
→ GIDL / storage-node decay / retention / write-transfer comparison
→ temperature-robust SG MEB range
```

Status boundary:

- `300/340/380 K`: existing transistor-level data and B0 direct-Hold evidence exist.
- `233 K (-40 °C)`: **Planned**, not yet a completed CMP result.

Temperature remains a stress / transfer variable rather than a second primary optimization axis.

### Phase 3 — DWFG transferability

```text
same 20 nm BCAT framework
→ introduce a literature-grounded DWFG extension
→ reuse SG-selected MEB candidates
→ re-search the spatial BTBT hotspot
→ check E-field redistribution
→ compare BTBT / GIDL / retention
→ test whether an SG/DWFG common MEB range exists
```

The project does **not** replace the 20 nm baseline with the 15 nm ICEIC DWFG device. The ICEIC 2026 paper is used as the MEB/DWFG mechanism and trade-off reference.

If the SG and DWFG optimum regions do not overlap, the correct interpretation is **optimum-MEB shift under DWFG**, not a forced common window.

Conceptually:

```text
R_final = R_SG ∩ R_temperature ∩ R_DWFG
```

only when the evidence actually supports a non-empty intersection.

## 3. 3D role

3D is retained as a **selected-point validation layer**, not as the full-factorial DOE engine.

```text
2D dense DOE
→ SG MEB candidate range
→ temperature validation
→ DWFG selected-candidate validation
→ selected-point 3D verification
```

Do not plan a full `MEB × Temperature × SG/DWFG` 3D factorial sweep unless later evidence makes it necessary.

For DWFG selected-point 3D checks:

1. do not reuse the SG hotspot coordinate by assumption;
2. re-locate the global/spatial BTBT hotspot;
3. verify whether the current Mesh-GIDL ROI still covers it;
4. inspect field redistribution around the upper/lower work-function boundary;
5. only then perform quantitative selected-point comparison.

The current 3D-Sun-B0 is a literature-consistent validation anchor, not an exact calibrated reproduction of Sun et al.

## 4. High-WL write-transfer guardrail

The current 300 K write normalization uses approximately:

```text
AreaFactor = 0.017
Ccell      = 10 fF
VBL_WRITE  = 1.2 V
VWL_ON     = 3.0 V
Twrite     ≈ 667 ns
VSN start  ≈ 1.0 V
```

This closes write feasibility for the current B0 protocol, but it also exposes a new design question:

> Why is a `3.0 V` WL bias required to transfer the storage node to approximately `1 V`, and does MEB depth alter this write-transfer requirement?

Planned guardrails:

- `VWL → VSN` transfer characteristic;
- write time;
- Ion / Vth relationship;
- read margin;
- leakage / retention;
- MEB dependence.

A successful `VSN≈1 V` write is therefore no longer treated as sufficient by itself.

## 5. Final synthesis target

The final design conclusion should not be a single minimum-GIDL point.

The usable range must combine:

```text
GIDL suppression
+ 1T1C retention benefit
+ write/read feasibility
+ temperature robustness
+ geometry-derived word-line penalty
+ selected-point 3D trend validation
(+ DWFG transferability when completed)
→ effective / usable MEB design range
```

No production optimum, refresh reduction, actual WL resistance, or SG/DWFG common range is claimed before the corresponding evidence exists.
