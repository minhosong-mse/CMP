# Run 7 SDevice / MixedMode Commands

Run 7 freezes the B0=36 nm 1T1C / retention protocol before MEB-dependent cell comparison.

## Current branch status

| Branch | Purpose | Status |
|---|---|---|
| R7A/R7B | Write feasibility screen | executed |
| R7A 1 V | 300 K Write normalization | PASS: 667 ns |
| R7C | complete 100 ns floating-SN screen | PASS |
| R7C-direct | 300 K direct Hold to 100 us | PASS |
| R7E | independent D0/D1 Read | PASS |
| R7E-transfer | VSN-to-Read-margin transfer | PASS |
| R7F W-H-R | normalized 300 K Write→Hold→Read | PASS for 100 ns/1 us/10 us |
| R7T Write-cal | 340/380 K Write-to-1 V normalization | PASS |
| R7T Hold-norm | 300/340/380 K approximately normalized direct Hold | PASS / processed |
| R7D-ON/OFF | leakage-vs-V integration / attribution | pending |

## Normalization anchors

```text
300 K -> Twrite = 667 ns
340 K -> Twrite = 258 ns
380 K -> Twrite = 126.54 ns
```

Actual long-Hold settled starts are approximately 1.000018 / 1.000107 / 1.000272 V at 300/340/380 K.

## Temperature-Hold headline

At 100 us:

```text
300 K DeltaVSN = 0.270195 uV
340 K DeltaVSN = 0.483889 uV
380 K DeltaVSN = 7.438961 uV
```

Equivalent Ccell*DeltaV/DeltaT scale:

```text
~2.70e-17 / 4.84e-17 / 7.44e-16 A
380 K / 300 K ≈ 27.53 x
```

## Claim boundary

- Direct Hold is transient decay/stability evidence, not a frozen retention time.
- 0.8 V is not a CMP read-fail threshold.
- Temperature comparison is approximately normalized near 1 V.
- Mainline physics remains the established NonlocalPath chain.
- Main README integration remains deferred until the feedback/retention block is closed.
