# Feedback Checkpoint — R7 1T1C Retention-Operation Feasibility

Date: 2026-09-11  
Feedback item: `FB-RET-01`  
Task: `T-RET-01`

## Feedback question

> What exactly is the 1T1C retention measurement definition, and can the B0 cell operation be demonstrated beyond transistor-level GIDL only?

## Current checkpoint

The first-pass B0-v1 1T1C operating chain has now been demonstrated at feasibility level:

```text
Write feasibility
→ floating-SN 100 ns short Hold
→ independent D0/D1 charge-sharing Read
```

### Write

Nominal AreaFactor candidate `0.017` was quantified over `VWL_ON=1.5/2.0/2.5/3.0 V` and `Twrite=100/200/300 ns`.

Strongest screened state:

```text
VWL_ON = 3.0 V
Twrite = 300 ns
VSN    = 0.948118 V
```

The screen does not yet reach 1.0 V, so this state is preliminary rather than a final write freeze.

### Floating Hold

After `Unset(sn)`, the currently processed 100 ns Hold subset shows only `~1e-13–1e-12 V` VSN change after switching settling. This is interpreted as numerical-floor-level change rather than a resolved physical retention decay.

Checkpoint conclusion:

- floating-SN implementation: PASS at feasibility level
- 100 ns short-hold stability: PASS for processed subset
- physical retention time: not yet extracted

### Independent Read

With `Ccell=10 fF`, `CBL=45 fF`, `VBL=0.5 V`, and a 10 ns read pulse:

```text
D0: DeltaVBL = -72.12 mV
D1: DeltaVBL = +30.55 mV
D0/D1 final BL separation = 102.67 mV
```

The opposite BL signal directions verify independent D0/D1 charge-sharing discrimination. Capacitor-charge balance error remains below 0.01% in both cases.

## Presentation-safe conclusion

> **B0 1T1C MixedMode에서 Write 후 floating storage node의 100 ns 단기 유지 안정성을 확인했고, 별도 D0/D1 read test에서 약 102.7 mV의 bitline separation을 확보하여 1차 retention-operation feasibility를 검증하였다.**

## What remains open

This feedback item is **not yet fully resolved** because the following are still required for final retention closure:

1. integrated `Write → Hold → Read` in one sequence;
2. Hold extension beyond 100 ns;
3. Synopsys-compatible `T_RET,5% = ∫ C/|I| dV` extraction;
4. final retention-metric freeze;
5. Mesh1/3 and NonlocalPath ON/OFF confirmation before formal R7 close-out.

## Traceability

Main Run 7 progress:

- `docs/progress/run07_1t1c_retention_feasibility.md`

Method source mapping:

- `docs/methodology/run07_methodology_traceability.md`

Detailed evidence:

- `docs/evidence/run07_write_screen_20260911.md`
- `docs/evidence/run07_hold100_partial_20260911.md`
- `docs/evidence/run07_read_window_20260911.md`

Processed summaries:

- `data/run07/processed/write_screen_af0017.csv`
- `data/run07/processed/hold100_partial.csv`
- `data/run07/processed/read_window.csv`

## README integration state

Main README update remains intentionally deferred. This checkpoint is staged for the next presentation and for later synthesis with the baseline, E-field/mesh, and practical-trade-off feedback items.
