# R7 Methodology Traceability — Source → Equation/Method → CMP Mapping

Date: 2026-09-11

This file preserves the exact reasoning chain used for later presentation / README integration.

## 1. Synopsys Applications Library: `Memory/SF_DRAM`

Audited reference files:

- `sdevice_mixedmode_des.cmd`
- `retention_des.cmd`
- `RH_des.cmd`
- `Plot_Write_vis.tcl`
- `Plot_RT_vis.tcl`
- `greadme.pdf`

### 1.1 Floating storage node

Official example pattern:

```text
Set(storage node)
→ establish initial/write state
→ Unset(storage node)
→ transient with floating storage node
```

CMP mapping:

```text
Synopsys sc → CMP sn
Set(sn=0)   → initial storage-node condition
Unset(sn)   → floating SN
Ccell       → 10 fF
```

CMP observables:

- `v(sn)`
- `i(cell,sn)`
- `i(Ccell,sn)`
- `VSN_hold_start`
- `VSN_hold_100ns`

### 1.2 Synopsys write endpoint

`Plot_Write_vis.tcl` assigns the variable named `Vmax` from the **last value of v(sc)**. It is not a mathematical `max(v(sc))` operation.

CMP naming therefore uses explicit terms such as:

- `VSN_write_end`
- post-switch-settling `VSN`

and does not infer a mathematical maximum from the Synopsys variable name.

### 1.3 Synopsys-compatible retention metric

The SF_DRAM retention example sweeps storage-node voltage over approximately `0.95*Vmax → Vmax` and post-processes:

```text
T_RET,5% = ∫ [ Ccell / |I_SN(VSN)| ] dVSN
```

CMP mapping:

- `Ccell = 10 fF`
- future extraction uses CMP BCAT geometry and CMP physics
- metric name: `T_RET,5%`
- current status: **not yet executed for CMP**

Important boundary:

- do not replace the established CMP `Band2Band(Model=NonlocalPath)` mainline merely to copy the Synopsys example;
- the Synopsys project is a **methodology / numerical precedent**, not a numerical calibration target.

## 2. Liu et al. — DRAM retention-time distribution, Part I

Previously audited literature method:

- storage capacitor: 10 fF
- temperature: 300 K
- data-loss criterion: storage-node voltage `1.0 V → 0.8 V`

CMP mapping:

```text
metric name = t_1.0→0.8
```

Only report this metric when the CMP written state truly starts near 1.0 V.

Current strongest screened CMP write state:

```text
VWL_ON = 3.0 V
Twrite = 300 ns
VSN    ≈ 0.948118 V
```

Therefore a Liu-compatible retention time is **not currently claimed**.

## 3. Cho et al. — BCAT read/write degradation

Literature use:

- write / hold / read methodology reference
- charge-sharing-based usable-state threshold reference

CMP mapping:

- use the paper as a read/hold guardrail only;
- do not import a literature read threshold as an automatic CMP pass/fail threshold;
- derive the CMP read window from its own `Ccell`, `CBL`, `VSN` and `VBL` transients.

Current independent CMP read result:

```text
D0 DeltaVBL = -72.12 mV
D1 DeltaVBL = +30.55 mV
final BL separation = 102.67 mV
```

## 4. BCAT GIDL / retention-bias literature

Audited BCAT GIDL literature commonly uses a representative data-1 retention state near:

```text
WL   = -0.2 V
SN   = 1.0 V
BL   = 0.5 V
body = -0.7 V
```

Current CMP short-hold branch uses:

```text
WL_HOLD   = -0.7 V
BL_HOLD   = 0 V
substrate = 0 V
SN        = floating
```

Therefore the current branch is described as a **CMP-adapted smoke / feasibility bias**, not as a literature-standard standby condition.

## 5. Current CMP evidence mapping

| Physical / methodological item | CMP observable | Current status |
|---|---|---|
| D1 write feasibility | `VSN_final` vs `VWL_ON`, `Twrite` | PASS |
| floating storage node | `Unset(sn)` + `Ccell` | PASS |
| short-hold stability | `VSN_hold_start → VSN_hold_100ns` | PASS for processed subset |
| D0/D1 read discrimination | `DeltaVBL_D0`, `DeltaVBL_D1` | PASS |
| charge-sharing sanity | Ccell/CBL charge balance | PASS |
| integrated Write→Hold→Read | one sequential transient | NOT YET |
| direct long-retention decay | long `VSN(t)` | NOT YET |
| Synopsys `T_RET,5%` | `∫ C/|I| dV` over 5% V window | NOT YET |
| Liu `t_1.0→0.8` | absolute threshold crossing | NOT YET |

## 6. Current metric naming rule

Keep the following distinct:

```text
T_RET,5%   = Synopsys-compatible 5% voltage-loss metric
t_0.8V     = absolute VSN=0.8 V crossing
t_1.0→0.8 = Liu-compatible metric
t_READ     = read-usable threshold crossing
DeltaVSN(t)= direct floating-SN voltage loss
```

Do not conflate these metrics in plots or presentation wording.

## 7. Safe terminology

Use:

- `R7 1T1C retention-operation feasibility`
- `100 ns floating-Hold stability`
- `independent D0/D1 charge-sharing read window`
- `preliminary / B0-v1`

Avoid until later:

- `final retention time`
- `production retention`
- `full Write-Hold-Read validation`
- `Liu-compatible retention time`
