#!/usr/bin/env python3
"""Check published 37-depth (2026-11-23) CMP CSV checkpoint.
This checks internal CSV consistency only. Native PLT/log/source validation
is documented separately; not a physical retention/JEDEC verification.
"""
from pathlib import Path
from collections import Counter
import csv, math

ROOT=Path(__file__).resolve().parents[4]
DATA=ROOT/"data/3d_meb_jedec_37depth_20261123"
MODES={0,1,5,6,7};TEMPS={233.15,300.,358.15,368.15}
REMAIN={(53,358.15,1),(53,358.15,5),(53,368.15,7)}
RECOV={(27,358.15,1),(40,358.15,1),(46,358.15,1),
       (47,368.15,5),(58,358.15,7)}
def read(name):
    with (DATA/name).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))
def k3(r):return int(r["MEB_nm"]),float(r["Temp_K"]),int(r["RunMode"])
def k2(r):return int(r["MEB_nm"]),float(r["Temp_K"])
qc=read("node_qc_740.csv")
mt=read("six_metrics_148_conditions.csv")
sources=read("selected_cases_328.csv")
delta=read("accepted_node_qc_25.csv")
mdelta=read("metrics_delta_9rows.csv")
sdelta=read("selected_sources_25.csv")
remaining=read("remaining_reruns_3.csv")
depth=read("depth_status_37.csv")
assert len(qc)==740 and len({k3(x) for x in qc})==740
assert {k3(r) for r in qc}=={(d,t,m) for d in range(24,61) for t in TEMPS for m in MODES}
assert sum(r["status"]=="PASS" for r in qc)==737
assert {k3(r) for r in qc if r["status"]!="PASS"}==REMAIN
assert len(remaining)==3 and {k3(r) for r in remaining}==REMAIN
assert len(depth)==37 and all(0<=int(d["Validated_Jobs"])<=20 for d in depth)
assert sum(int(r["Validated_Jobs"]) for r in depth)==737
assert all(int(r["Validated_Jobs"])==20 for r in depth if int(r["MEB_nm"])!=53)
assert len(mt)==148 and len({k2(r) for r in mt})==148
passes=Counter(k2(r) for r in qc if r["status"]=="PASS")
assert all(int(r["valid_modes"])==passes[k2(r)] for r in mt)
assert sum(r["valid_modes"]=="5" for r in mt)==146
assert all(r["valid_modes"]=="5" for r in mt if float(r["Temp_K"])==300)
for r in mt:
    n=int(r["valid_modes"])
    if n==5:
        for k in ["Ion_A","Ioff_A","SS_mV_dec","DIBL_mV_V","Hurkx_excess_A","t_est_s"]:
            assert r[k] not in ("",None),(k2(r),k)
        assert math.isfinite(float(r["t_est_s"])) and float(r["t_est_s"])>0
    if r["Vth_low_V"] and r["Vth_high_V"]:
        dv=(float(r["Vth_low_V"])-float(r["Vth_high_V"]))/1.15*1000
        assert math.isclose(dv,float(r["DIBL_mV_V"]),rel_tol=5e-10)
    if r["Id_Hurkx_ON_A"] and r["Id_Hurkx_OFF_A"]:
        dx=float(r["Id_Hurkx_ON_A"])-float(r["Id_Hurkx_OFF_A"])
        assert math.isclose(dx,float(r["Hurkx_excess_A"]),rel_tol=1e-10,abs_tol=1e-25)
assert len(delta)==len(sdelta)==25 and len(mdelta)==9
assert {k3(r) for r in delta}=={(35,t,m) for t in TEMPS for m in MODES}|RECOV
assert all(r["status"]=="PASS" for r in delta)
assert len(sources)==328 and len({k3(r) for r in sources})==328
assert {k3(r) for r in sdelta}=={k3(r) for r in delta}
assert sum(r["R1"].lower()=="true" for r in sdelta)==5
assert all(r["status"]=="PASS" for r in qc if k3(r) in RECOV)
print("PASS: 37 depths, 737/740 endpoints, 146/148 complete MEBxT rows")
print("Remaining: 53nm / 358.15K modes 1,5; 368.15K mode 7")
print("Native ZIPs, raw solver terminal traces and binary mesh are external.")
