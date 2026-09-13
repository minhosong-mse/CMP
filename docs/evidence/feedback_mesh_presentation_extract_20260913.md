# Mesh Feedback — Presentation Extract (R6.5)

Use this file as a copy-ready source for slides / Q&A.

## One-line result

> R6.5의 전체 MEB 조건(36/41/43/45/47/48/49/51 nm)에서 BTBT hotspot을 독립적으로 추출한 결과, 모든 hotspot이 동일 Mesh-Code 3 refinement ROI 내부에 최소 9.875 nm margin으로 포함되었으며 case-specific ROI 이동은 필요하지 않았다.

## Copy-ready table

| MEB (nm) | BTBTmax (cm^-3 s^-1) | Xhot (um) | Yhot (um) | Points | Elements | Nearest ROI margin (nm) | Result |
|---:|---:|---:|---:|---:|---:|---:|---|
| 36 | 8.41825e21 | 0.0515625 | 0.121875 | 5789 | 12175 | 9.875 | PASS |
| 41 | 5.55270e21 | 0.0523437 | 0.121875 | 5830 | 12273 | 9.875 | PASS |
| 43 | 3.92200e21 | 0.0523437 | 0.121875 | 5843 | 12303 | 9.875 | PASS |
| 45 | 2.95585e21 | 0.0531250 | 0.121875 | 5856 | 12333 | 9.875 | PASS |
| 47 | 1.90750e21 | 0.0531250 | 0.121875 | 5880 | 12385 | 9.875 | PASS |
| 48 | 1.42817e21 | 0.0539063 | 0.121875 | 5882 | 12393 | 9.875 | PASS |
| 49 | 1.17656e21 | 0.0539063 | 0.121875 | 5895 | 12423 | 9.875 | PASS |
| 51 | 5.94400e20 | 0.0539063 | 0.121875 | 5908 | 12453 | 9.875 | PASS |

## Numbers worth showing on a slide

```text
Common ROI             X = 0.032–0.070 um
                       Y = 0.112–0.133 um
Mesh-Code 3 local      max/min = 1.0 / 0.25 nm
Xhot range             0.0515625–0.0539063 um
Xhot shift, 36→51      +2.344 nm
Yhot                    0.121875 um (8/8 identical)
minimum ROI margin      9.875 nm
coverage                8/8 PASS
```

## Presentation-safe interpretation

1. MEB가 36→51 nm로 증가해도 BTBT hotspot 위치 변화는 작다.
2. X 방향 총 이동은 약 2.34 nm이고 Y 좌표는 모든 조건에서 동일하다.
3. 모든 hotspot은 동일한 common refinement ROI 안에 충분한 margin으로 유지된다.
4. 따라서 R6.5 비교에서 case마다 refinement window를 옮기지 않아도 hotspot coverage와 비교 일관성이 확보된다.

## Q&A boundary

Do not say `mesh independence proved`.

Use:

> 이번 검증은 hotspot coverage와 조건 간 mesh-policy consistency를 확인한 것이고, 절대적인 mesh independence를 주장하려면 별도 mesh-spacing convergence가 필요합니다.

## Source package

- Full evidence: `docs/evidence/feedback_mesh_run65_full_validation_20260913.md`
- Raw extract: `data/run06_5/feedback_mesh_20260913/r65_mesh_raw_extract.csv`
- ROI audit: `data/run06_5/feedback_mesh_20260913/r65_mesh_hotspot_coverage_summary.csv`
- Screenshot provenance: `data/run06_5/feedback_mesh_20260913/screenshot_manifest.csv`
