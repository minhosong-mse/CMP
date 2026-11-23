#!/usr/bin/env python3
"""Audit published 2026-11-23 33-depth CMP CSV snapshot; no Sentaurus required.

This checks archival integrity and internal endpoint/metric completeness.
It does NOT revalidate external native solver logs, device physics, or mesh.
"""
from __future__ import annotations

import collections
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "data/3d_meb_jedec_33depth_20261123"
TEMPS = (233.15, 300.0, 358.15, 368.15)
MODES = (0, 1, 5, 6, 7)
REMAINING = {(27, 358.15, 1), (40, 358.15, 1),
             (46, 358.15, 1), (58, 358.15, 7)}


def read(name):
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


qc = read("node_qc_660.csv")
metrics = read("six_metrics_132_conditions.csv")
selected = read("selected_cases.csv")
candidates = read("node_qc_all_candidates.csv")
reruns = read("remaining_reruns.csv")
depths = read("depth_status.csv")
ivsn = read("ivsn_curves_delta_and_recovery.csv")
parts = [
    read(f"dc_curves_delta_part0{i}.csv")
    for i in (1, 2, 3)
]

key3 = lambda r: (int(r["MEB_nm"]), float(r["Temp_K"]), int(r["RunMode"]))
key2 = lambda r: (int(r["MEB_nm"]), float(r["Temp_K"]))
depth_set = {int(r["MEB_nm"]) for r in qc}

assert len(depth_set) == 33
assert len(depths) == 37
assert depth_set == set(range(24, 61)) - {35, 41, 47, 53}
assert len(qc) == len({key3(r) for r in qc}) == 660
assert len(metrics) == len({key2(r) for r in metrics}) == 132

for d in depth_set:
    assert {(t, m) for dd, t, m in map(key3, qc) if dd == d} == {
        (t, m) for t in TEMPS for m in MODES
    }

passed = [r for r in qc if r["status"] == "PASS"]
failed = [r for r in qc if r["status"] != "PASS"]
assert len(passed) == 656
assert {key3(r) for r in failed} == REMAINING
assert len(reruns) == 4
assert {key3(r) for r in reruns} == REMAINING

counts = collections.Counter(key2(r) for r in passed)
for r in metrics:
    assert int(r["valid_modes"]) == counts[key2(r)]
assert sum(int(r["valid_modes"]) == 5 for r in metrics) == 128
assert all(int(r["valid_modes"]) == 5 for r in metrics if float(r["Temp_K"]) == 300.0)

required = ("Ion_A", "Ioff_A", "SS_mV_dec",
            "DIBL_mV_V", "Hurkx_excess_A", "t_est_s")
for r in metrics:
    if int(r["valid_modes"]) == 5:
        assert all(r.get(c) not in (None, "") for c in required), (key2(r), "metric missing")
        assert math.isfinite(float(r["t_est_s"])) and float(r["t_est_s"]) > 0

assert len(selected) == 247
assert len({key3(r) for r in selected}) == 247
assert sum(r["R1"] == "True" for r in selected) == 11
assert len(candidates) == 262
assert sum(r["valid"] == "True" and r["chosen"] == "True" for r in candidates) == 247

assert sum(map(len, parts)) == 22168
assert len(ivsn) == 5050
ivgrp = collections.defaultdict(list)
for r in ivsn:
    k = (int(r["MEB_nm"]), float(r["Temp_K"]), r["project"], r["node"])
    ivgrp[k].append(r)
assert len(ivgrp) == 50
for k, rows in ivgrp.items():
    assert len(rows) == 101, k
    vals = [float(r["v(sn)"]) for r in rows]
    assert all(math.isclose(v, .8 + .002 * i, abs_tol=1e-9)
               for i, v in enumerate(vals)), k
    assert all(float(r["i(cell,sn)"]) < 0 for r in rows), k

print("QC archive PASS: 33 depths; 656/660 endpoints; 128/132 complete")
print("Native source / mesh / cold-KCL warnings require separate evidence review")
