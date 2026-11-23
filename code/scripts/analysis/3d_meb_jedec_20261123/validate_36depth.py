#!/usr/bin/env python3
"""CMP 2026-11-23 36-depth archival CSV consistency validator.

Internal dataset checks only; native solver/source inspection is separate.
Run from any directory: python code/scripts/analysis/3d_meb_jedec_20261123/validate_36depth.py
"""
from __future__ import annotations
import collections
import csv
import math
from pathlib import Path

DATA = Path(__file__).resolve().parents[4] / "data/3d_meb_jedec_36depth_20261123"
TEMPS = (233.15, 300.0, 358.15, 368.15)
MODES = (0, 1, 5, 6, 7)
PENDING = {
    (27, 358.15, 1), (40, 358.15, 1), (46, 358.15, 1),
    (47, 368.15, 5), (53, 358.15, 1), (53, 358.15, 5),
    (53, 368.15, 7), (58, 358.15, 7),
}

def read(name):
    with (DATA / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def key3(row):
    return (int(row["MEB_nm"]), float(row["Temp_K"]), int(row["RunMode"]))

def key2(row):
    return (int(row["MEB_nm"]), float(row["Temp_K"]))

qc = read("node_qc_720.csv")
metrics = read("six_metrics_144_conditions.csv")
selected = read("selected_cases_303.csv")
pending = read("remaining_reruns.csv")
depths = read("depth_status.csv")
only = read("meb53_node_qc.csv")
m53 = read("meb53_six_metrics.csv")
dc = read("meb53_dc_curves.csv")
ivsn = read("meb53_ivsn_curves.csv")

assert len(qc) == len(set(map(key3, qc))) == 720
assert len(metrics) == len(set(map(key2, metrics))) == 144
assert len(selected) == len(set(map(key3, selected))) == 303
assert len(pending) == 8 and set(map(key3, pending)) == PENDING
assert len(depths) == 37 and [int(x["MEB_nm"]) for x in depths if x["Status"] == "NOT_EXPORTED"] == [35]
exported = set(range(24, 61)) - {35}
assert {int(r["MEB_nm"]) for r in qc} == exported
assert {key3(r) for r in qc if r["status"] != "PASS"} == PENDING
assert sum(r["status"] == "PASS" for r in qc) == 712
assert sum(int(r["Validated_Jobs"]) for r in depths) == 712
assert len(only) == 20 and sum(r["status"] == "PASS" for r in only) == 17
assert {key3(r) for r in only if r["status"] != "PASS"} == {
    (53, 358.15, 1), (53, 358.15, 5), (53, 368.15, 7)}
assert len(m53) == 4 and sum(int(r["valid_modes"]) == 5 for r in m53) == 2
assert len(dc) == 1503 and len(ivsn) == 303
assert sum(r["R1"] == "True" for r in selected) == 11
assert sum(int(r["valid_modes"]) == 5 for r in metrics) == 137

count = collections.Counter(key2(r) for r in qc if r["status"] == "PASS")
for row in metrics:
    assert int(row["valid_modes"]) == count[key2(row)]
    if int(row["valid_modes"]) == 5:
        for column in ("Ion_A", "Ioff_A", "SS_mV_dec", "DIBL_mV_V",
                       "Hurkx_excess_A", "t_est_s"):
            assert row[column] != "", (key2(row), column)
            assert math.isfinite(float(row[column]))
assert all(int(r["valid_modes"]) == 5 for r in metrics if float(r["Temp_K"]) == 300)
for temp in (233.15, 300, 358.15):
    rows = [r for r in ivsn if float(r["Temp_K"]) == temp]
    assert len(rows) == 101
    for j, row in enumerate(rows):
        assert math.isclose(float(row["v(sn)"]), 0.8 + j * 0.002, abs_tol=1e-9)
        assert float(row["i(cell,sn)"]) < 0
    assert all(int(r["MEB_nm"]) == 53 for r in rows)
assert all(int(r["MEB_nm"]) == 53 for r in dc)
print("PASS: 36/37 depths; 712/720 terminal-complete; 137/144 five-mode rows; 8 reruns")
print("Source PP/PLT/log verified separately by qc_meb53.py against external SWB ZIPs")
