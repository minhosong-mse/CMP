# CMP Run 7 — 1T1C Retention Feasibility: Updated Checkpoint

Date: 2026-09-21  
Scope: **B0-v1 methodology feasibility** only.

## 1. Current closure status

Completed:

```text
300 K Write-to-~1 V normalization
→ 300 K direct Hold to 100 us
→ independent D0/D1 Read
→ VSN-to-Read-margin transfer
→ integrated 300 K Write→Hold→Read
→ 340/380 K Write-to-~1 V normalization
→ 300/340/380 K approximately normalized direct Hold
```

Still open:

```text
340/380 K integrated W-H-R
leakage-vs-V integration / final retention metric
Mesh1 vs Mesh3 retention check
MEB-dependent cell-level translation
```

## 2. Temperature-normalized direct Hold

Direct-Hold starting voltages:

```text
300 K: 1.000017733 V
340 K: 1.000107421 V
380 K: 1.000272165 V
```

100 us result:

| T | DeltaVSN | equivalent leakage scale |
|---:|---:|---:|
| 300 K | 0.270195 uV | ~2.70e-17 A |
| 340 K | 0.483889 uV | ~4.84e-17 A |
| 380 K | 7.438961 uV | ~7.44e-16 A |

The 380 K equivalent leakage scale is approximately 27.53x the 300 K value and 15.37x the 340 K value.

This establishes a clear B0 temperature dependence while preserving the claim boundary that direct short-window decay is not itself a retention-time measurement.

## 3. Existing 300 K cell-operation results

Integrated 300 K W-H-R remains:

```text
Thold = 100 ns / 1 us / 10 us
DeltaVBL ≈ +35.6251 mV
```

Independent Read transfer remains monotonic; VSN=0.8 V still produces a positive D1 signal and therefore is not a CMP read-fail threshold.

## 4. Claim boundary

- Report direct-Hold DeltaVSN and temperature ratios as measured transient results.
- Do not report a physical retention time from linear extrapolation.
- Describe the three-temperature Hold comparison as approximately 1 V-normalized.
- Do not claim MEB-depth retention improvement until downstream MEB cell comparison is executed.

## 5. Next step

```text
340/380 K normalized integrated Write→Hold→Read
→ leakage-vs-V integration if needed for t_1.0→0.8 or T_RET,5%
→ Mesh1/3 check
→ later MEB-depth cell translation
```

Documentation:
- `docs/evidence/run07_hold_temperature_normalized_20260921.md`
- `docs/evidence/run07_retention_manifest.md`
- `docs/evidence/run07_cell_operation_checkpoint_20260920.md`


---

## 6. Post-Turn-02 write-transfer guardrail

The current B0 write normalization demonstrates feasibility, but the required drive condition is itself a new performance question:

```text
VBL_WRITE = 1.2 V
VWL_ON    = 3.0 V
300 K Twrite ≈ 667 ns
VSN       ≈ 1.0 V
```

The project will therefore not use “1 V reached” as the only write-success condition.

Planned selected-point diagnostics:

- `VWL → VSN` transfer curve;
- time-to-target `VSN`;
- relation to Ion / Vth;
- read-margin impact;
- leakage / retention interaction;
- MEB dependence.

The same rule applies when the temperature and DWFG branches are activated.

## 7. Downstream temperature / gate-scheme validation

- Existing B0 cell evidence: approximately normalized direct Hold at `300/340/380 K`.
- Planned cold point: `233 K (-40 °C)`; not yet executed.
- DWFG: planned only after the SG MEB candidate/range is established.
- The 20 nm single-WF branch remains the reference/control branch.

See `docs/research/post_turn02_validation_roadmap.md`.
