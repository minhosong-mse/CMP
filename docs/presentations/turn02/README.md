# Turn 02 Presentation Note

## Presentation

**20 nm급 BCAT DRAM에서 MEB 깊이에 따른 GIDL–Retention 전달 특성 및 온도 의존적 유효 설계 범위 도출**

This title is the current canonical CMP research title.

## Main feedback-response results reported

### Hotspot / mesh

- the complete R6.5 MEB set `36/41/43/45/47/48/49/51 nm` was rechecked;
- all independently extracted BTBT hotspots remained inside the same Mesh-Code 3 ROI;
- the minimum nearest ROI-edge margin remained `9.875 nm`;
- the common mesh policy therefore supports comparison consistency over the tested R6.5 set.

### E-field interpretation

The old historical field metric was:

```text
Y = 0.116 um fixed cut
E_wall,max
```

Post-feedback analysis moved the mechanism evidence to the actual BTBT critical region.

For `31 → 41 nm`:

```text
terminal GIDL                     -60.42%
BTBT_max                          -52.43%
hotspot-cut |E| peak               -3.52%
20% BTBT-active width             -12.68%
20% active-region int(|E| dx)     -14.68%
full-cut 1-D int(G_BTBT dx)       -57.74%
20% region int(G_BTBT dx)         -58.40%
```

The current interpretation therefore emphasizes **critical-region spatial E-field / BTBT distribution**, not one peak-field scalar.

### 3D baseline / model fidelity

A literature-consistent `3D-Sun-B0` reconstruction was built using the reported 20 nm-class BCAT geometry.

The reconstruction is useful as a higher-fidelity validation anchor, but it does **not** exactly reproduce the paper's absolute electrical calibration. The simplified 2D B0 is therefore retained for broad relative DOE, while final selected points are intended for 3D validation.

### Word-line trade-off

MEB-dependent remaining W cross-section was converted into a normalized `1/A_W` RWL proxy.

The `47–49 nm` region shows diminishing incremental GIDL return while the geometry-derived RWL proxy continues to rise. This is a trade-off checkpoint, not an actual distributed word-line resistance / RC-delay simulation.

### Run 7 1T1C

The Turn-02 presentation reported the transition from write feasibility to integrated cell-operation validation:

- `Ccell=10 fF`
- `AreaFactor=0.017`
- `VBL_WRITE=1.2 V`
- `VWL_ON=3.0 V`
- `Twrite≈667 ns` at 300 K for `VSN≈1 V`
- direct floating Hold
- independent Read transfer
- integrated `Write → Hold → Read` at 300 K

Subsequent committed Run-7 evidence additionally contains approximately normalized `300/340/380 K` direct-Hold comparisons.

## Post-Turn-02 open questions

The second-turn feedback created three additional validation questions:

1. **high WL bias / write-transfer issue** — reaching `VSN≈1 V` required `VWL_ON=3.0 V`; this is now a performance guardrail rather than a simple success condition;
2. **cold-temperature extension** — add `233 K (-40 °C)` as a planned cold operating point;
3. **DWFG transferability** — retain the verified 20 nm single-WF baseline, derive the SG MEB range first, then test whether that range transfers to a dual-work-function gate implementation.

See [Post-Turn-02 Validation Roadmap](../../research/post_turn02_validation_roadmap.md).
