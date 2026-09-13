# Run 7 Progress Addendum — Complete 100 ns Hold Matrix

Date: 2026-09-13  
Scope: progress update **before** the later A/B/C/D follow-up simulation batches. Those in-flight batches are intentionally excluded from this addendum.

## Update

The previously partial Run-7 floating-storage-node Hold evidence has now been processed across the full 36-case screen.

```text
AreaFactor = 0.011 / 0.017 / 0.023
VWL_ON     = 1.5 / 2.0 / 2.5 / 3.0 V
Twrite     = 100 / 200 / 300 ns
Thold      = 100 ns
```

The Hold metric remains defined after write-edge settling:

```text
Hold start = Twrite + 2 ns
Hold end   = Hold start + 100 ns
```

## Result

```text
36 / 36 cases processed
maximum |DeltaVSN_100ns| ≈ 2.466e-10 V
maximum |fractional change| ≈ 2.548e-8 %
```

The complete matrix therefore supports the same interpretation as the earlier subset, now without the subset qualifier:

> **The floating storage node is numerically stable over the tested 100 ns Hold window for all 36 screened Write conditions.**

This remains short-Hold feasibility evidence only. No physical retention time is extracted.

Representative nominal-width case n209:

```text
AF               = 0.017
VWL_ON           = 3.0 V
Twrite           = 300 ns
VSN_hold_start   = 0.948118339190 V
VSN_hold_+100ns  = 0.948118339047 V
DeltaVSN         = 1.432e-10 V
```

## Repository evidence

- `docs/evidence/run07_hold100_complete_20260913.md`
- `data/run07/processed/hold100_complete.csv`

The older `run07_hold100_partial_20260911.md` and `hold100_partial.csv` remain as historical provenance.

## Scope boundary

This addendum intentionally does **not** include results or status from the later A/B/C/D batches that were configured after this checkpoint.
