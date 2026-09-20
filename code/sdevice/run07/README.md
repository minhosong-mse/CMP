# Run 7 SDevice / MixedMode Commands

Run 7 freezes the B0=36 nm 1T1C / retention protocol before any MEB-dependent cell comparison is performed.

## Current branch status

| Branch | Command / provenance | Purpose | Status |
|---|---|---|---|
| R7A/R7B | `bcat_1t1c_r7_write_screen.cmd` | AreaFactor + WL write feasibility screening | executed |
| R7A 1 V | local SWB extension of Write/Hold flow | 300 K Write-to-1 V normalization | PASS: 667 ns |
| R7C | `bcat_1t1c_r7_hold100_screen.cmd` | complete 36-case 100 ns floating-SN screen | PASS |
| R7C-direct | parameterized local SWB Hold variant | 300 K direct Hold: 100 ns–100 us | PASS / processed |
| R7D-ON | `bcat_retention_r7_ivsn_integral_on.cmd` | `Ileak(VSN)` with NonlocalPath ON | prepared / not yet used for closure |
| R7D-OFF | `bcat_retention_r7_ivsn_integral_off.cmd` | BTBT-OFF attribution reference | prepared / not yet executed |
| R7E | `bcat_1t1c_r7_read_window.cmd` | independent D0/D1 read | PASS |
| R7E-transfer | local SWB extension of Read-B | VSN-to-Read-margin transfer | PASS / processed |
| R7F W-H-R | parameterized local SWB integrated sequence | normalized 300 K Write→Hold→Read | PASS for 100 ns/1 us/10 us |
| R7T Write-cal | local SWB calibration matrix | 340/380 K Write-to-1 V normalization | PASS |
| R7T Hold-norm | local SWB direct-Hold matrix | 340/380 K normalized Hold | running; not registered as completed result |

Local Workbench projects remain the execution archive. GitHub records source commands where frozen, plus processed summaries, parameter snapshots and selected evidence.

## Current normalization anchors

```text
MEB_Depth = 0.036 um
Mesh_Code = 1
AreaFactor = 0.017
Ccell_F = 1.0e-14 F

300 K -> Twrite = 667 ns    -> VSN_start ≈ 1.000015 V
340 K -> Twrite = 258 ns    -> VSN_start ≈ 1.000099 V
380 K -> Twrite = 126.54 ns -> VSN_start ≈ 1.000092 V
```

## Read feasibility reference

```text
CBL_F = 4.5e-14 F
VBL_PRE = 0.5 V
WL_OFF = -0.7 V
WL_READ = 3.0 V
Tread = 10 ns
```

The independent Read-B sweep is retained separately from the integrated W-H-R test.

## Claim boundary

- 1 V is a comparison/normalization benchmark, not a universal operating voltage.
- Direct Hold results are transient stability/decay evidence, not a frozen physical retention time.
- `0.8 V` is not a CMP read-fail threshold.
- Mainline physics remains the established NonlocalPath chain.
- Main README integration remains deferred until the current feedback/retention block is closed.
