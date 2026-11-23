#!/usr/bin/env python3
"""Audit 2026-11-23 37-depth complete CMP archive, no Sentaurus invocation.

This validates CSV consistency and checksum/provenance presence only. Actual
native SWB evidence was separately audited on receipt. No physical/Jedec claims.
"""
from __future__ import annotations
import csv, math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "data/3d_meb_jedec_37depth_complete_20261123"
TEMPS = (233.15, 300., 358.15, 368.15)
MODES = (0, 1, 5, 6, 7)
RECOVERED_FINAL = {(53,358.15,1):"39", (53,358.15,5):"40", (53,368.15,7):"47"}

def read(name):
    with (DATA / name).open(newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))
def key3(r):
    return int(r["MEB_nm"]),float(r["Temp_K"]),int(r["RunMode"])
def key2(r):
    return int(r["MEB_nm"]),float(r["Temp_K"])

qc = read("node_qc_740.csv")
met = read("six_metrics_148_conditions.csv")
sel = read("selected_cases_331.csv")
depth = read("depth_status_37.csv")
recovered = read("meb53_r1_node_qc_3.csv")
sources = read("meb53_r1_selected_sources_3.csv")
patches = read("meb53_r1_metric_patches_2.csv")

assert len(qc)==740 and len({key3(r) for r in qc})==740
assert {key3(r) for r in qc}=={(d,t,m) for d in range(24,61) for t in TEMPS for m in MODES}
assert all(r["status"]=="PASS" for r in qc)
assert len(depth)==37 and all(int(r["Validated_Jobs"])==20 for r in depth)
assert len(met)==148 and len({key2(r) for r in met})==148
assert all(int(r["valid_modes"])==5 for r in met)
assert len(sel)==331 and len({key3(r) for r in sel})==331
assert sum(r["R1"].lower()=="true" for r in sel)==19
assert len(recovered)==len(sources)==3 and len(patches)==2
assert {key3(r) for r in recovered}==set(RECOVERED_FINAL)
assert {key3(r) for r in sources}==set(RECOVERED_FINAL)
for r in qc:
    k=key3(r)
    if k in RECOVERED_FINAL:
        assert r["project"]=="CMP_eeeeeeee_53"
        assert r["node"]==RECOVERED_FINAL[k]
        assert r["reason"]=="R1_NUMERICAL_ONLY"
assert sum(float(r["Temp_K"])==233.15 and r["IVSN_QC"]=="LOW_CURRENT_KCL_WARNING" for r in met)==25
for r in met:
    for k in ("Ion_A","Ioff_A","SS_mV_dec","DIBL_mV_V","Hurkx_excess_A","t_est_s"):
        assert r[k] not in ("",None),(key2(r),k)
    assert math.isfinite(float(r["t_est_s"])) and float(r["t_est_s"])>0
    dibl=(float(r["Vth_low_V"])-float(r["Vth_high_V"]))/1.15*1000.
    assert math.isclose(float(r["DIBL_mV_V"]),dibl,rel_tol=1e-9),(key2(r),"DIBL")
    excess=float(r["Id_Hurkx_ON_A"])-float(r["Id_Hurkx_OFF_A"])
    assert math.isclose(float(r["Hurkx_excess_A"]),excess,rel_tol=1e-8,abs_tol=1e-23),(key2(r),"Hurkx excess")
    assert r["IVSN_QC"] in ("PASS","LOW_CURRENT_KCL_WARNING")

curve_sets={
    "MEB35+5 R1 DC":([f"meb35_and_five_r1_dc_part{i:02}.csv" for i in range(1,6)],2607),
    "MEB47 DC":([f"meb47_dc_part{i:02}.csv" for i in range(1,4)],1618),
    "MEB53 original DC":([f"meb53_original_dc_part{i:02}.csv" for i in range(1,4)],1503),
    "MEB53 final R1 DC":(["meb53_r1_dc_curves.csv"],446),
    "MEB35+5 R1 IVSN":(["meb35_and_five_r1_ivsn.csv"],505),
    "MEB47 IVSN":(["meb47_ivsn.csv"],404),
    "MEB53 original IVSN":(["meb53_original_ivsn.csv"],303),
    "MEB53 final R1 IVSN":(["meb53_r1_ivsn.csv"],101),
}
for name,(files,n) in curve_sets.items():
    count=sum(len(read(p)) for p in files)
    assert count==n,(name,count,n)
iv=read("meb53_r1_ivsn.csv")
assert len(iv)==101
for i,r in enumerate(iv):
    assert math.isclose(float(r["v(sn)"]),.8+.002*i,rel_tol=0,abs_tol=1e-9)
    assert float(r["i(cell,sn)"])<0 and float(r["i(vsn,sn)"])>0

print("PASS 37 MEB depths / 740 complete SDevice endpoints / 148 full metrics rows")
print("PASS 19 numerical-only R1 recoveries; final MEB53 3/3")
print("PASS 6,174 incremental DC and 1,313 incremental IVSN curve rows")
print("PASS 25 cold relative-KCL warnings preserved")
print("NOTE: native ZIPs remain external per D-005; binary mesh equivalence and physical retention are not proven")
