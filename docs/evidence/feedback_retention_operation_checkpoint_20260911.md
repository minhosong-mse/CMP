# Feedback Checkpoint — R7 1T1C Retention-Operation Feasibility

Date: 2026-09-11  
Updated: 2026-09-13 — complete 36-case 100 ns Hold screen processed  
Feedback item: `FB-RET-01`  
Task: `T-RET-01`

## Feedback question

> What exactly is the 1T1C retention measurement definition, and can the B0 cell operation be demonstrated beyond transistor-level GIDL only?

## Current checkpoint

The first-pass B0-v1 1T1C operating chain has been demonstrated at feasibility level:

```text
Write feasibility
→ floating-SN 100 ns short Hold
→ independent D0/D1 charge-sharing Read
```

The 100 ns Hold branch, which was previously documented only as a processed subset, is now complete across all 36 screened Write-condition combinations.

### Write

Nominal AreaFactor candidate `0.017` was quantified over `VWL_ON=1.5/2.0/2.5/3.0 V` and `Twrite=100/200/300 ns`.

Strongest screened nominal-width state:

```text
VWL_ON = 3.0 V
Twrite = 300 ns
VSN    = 0.948118 V
```

This checkpoint does not freeze a final Write condition.

### Floating Hold — complete 36-case screen

Complete matrix:

```text
AreaFactor = 0.011 / 0.017 / 0.023
VWL_ON     = 1.5 / 2.0 / 2.5 / 3.0 V
Twrite     = 100 / 200 / 300 ns
Thold      = 100 ns
```

Hold is evaluated after switching settling at approximately `Twrite + 2 ns`.

Results:

```text
36 / 36 cases processed
maximum |DeltaVSN_100ns| = 2.465920e-10 V
maximum |fractional change| = 2.548440e-8 %
```

Representative nominal-width n209:

```text
VSN_hold_start  = 0.948118339190 V
VSN_hold_+100ns = 0.948118339047 V
DeltaVSN        = 1.432444e-10 V
```

These changes remain at the numerical-floor scale for the tested window.

Checkpoint conclusion:

- floating-SN implementation: **PASS at feasibility level**
- complete 36-case 100 ns short-Hold stability: **PASS**
- physically resolved retention decay within 100 ns: **not observed**
- physical retention time: **not yet extracted**

### Independent Read

With `Ccell=10 fF`, `CBL=45 fF`, `VBL=0.5 V`, and a 10 ns read pulse:

```text
D0: DeltaVBL = -72.12 mV
D1: DeltaVBL = +30.55 mV
D0/D1 final BL separation = 102.67 mV
```

The opposite BL signal directions verify independent D0/D1 charge-sharing discrimination. Capacitor-charge balance error remains below 0.01% in both cases.

## Presentation-safe conclusion

> **B0 1T1C MixedMode에서 Write 후 floating storage node의 100 ns 단기 유지 안정성을 36개 전체 screening 조건에서 확인했고, 별도 D0/D1 read test에서 약 102.7 mV의 bitline separation을 확보하여 1차 retention-operation feasibility를 검증하였다.**

## What remains open

This feedback item is **not yet fully resolved** because final retention closure still requires:

1. a representative D1 write-condition freeze;
2. Hold extension beyond 100 ns;
3. integrated `Write → Hold → Read`;
4. Synopsys-compatible `T_RET,5% = ∫ C/|I| dV` extraction;
5. final retention-metric / standby-bias freeze;
6. Mesh1/3 and NonlocalPath ON/OFF confirmation before formal R7 close-out.

Later A/B/C/D follow-up batches are intentionally excluded from this update until their results are available and reviewed.

## Traceability

Main Run 7 progress:

- `docs/progress/run07_1t1c_retention_feasibility.md`
- `docs/progress/run07_hold100_completion_20260913.md`

Method source mapping:

- `docs/methodology/run07_methodology_traceability.md`

Detailed evidence:

- `docs/evidence/run07_write_screen_20260911.md`
- `docs/evidence/run07_hold100_partial_20260911.md` (historical partial snapshot)
- `docs/evidence/run07_hold100_complete_20260913.md` (current complete screen)
- `docs/evidence/run07_read_window_20260911.md`

Processed summaries:

- `data/run07/processed/write_screen_af0017.csv`
- `data/run07/processed/hold100_partial.csv` (historical)
- `data/run07/processed/hold100_complete.csv`
- `data/run07/processed/read_window.csv`

## README integration state

Main README update remains intentionally deferred. This checkpoint is staged for later synthesis with the baseline, E-field/mesh, retention, and practical-trade-off feedback items.
