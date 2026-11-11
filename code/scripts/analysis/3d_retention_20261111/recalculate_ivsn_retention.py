#!/usr/bin/env python3
"""Check and reproduce I_VSN 1.0 -> 0.8 V constant-C numerical retention estimates.

Only standard library is needed. This is an ANALYSIS script, not a Sentaurus solver
or a verified full cell retention transient.
"""
import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path

def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def estimate(points, capacitance):
    data = sorted((float(p["v_sn_V"]), float(p["i_cell_sn_A"])) for p in points)
    if len(data) != 101 or abs(data[0][0]-0.8)>1e-9 or abs(data[-1][0]-1.0)>1e-9:
        raise ValueError("Missing or unexpected 0.8->1.0 sweep / 101 samples")
    if any((not math.isfinite(v)) or (not math.isfinite(i)) or i >= 0 for v,i in data):
        raise ValueError("Nonfinite or nondischarge SN current")
    return sum((v1-v0)*0.5*(capacitance/-i0+capacitance/-i1)
               for (v0,i0),(v1,i1) in zip(data[:-1],data[1:]))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--data-dir",type=Path,default=Path(__file__).resolve().parents[4]/"data/3d_1t1c_retention_20261111")
    ap.add_argument("--capacitance",type=float,default=1e-14)
    args=ap.parse_args()
    path=args.data_dir
    rows=read_csv(path/"ivsn_all.csv")
    cases=read_csv(path/"case_metrics.csv")
    groups=defaultdict(list)
    for row in rows:
        groups[(int(row["MEB_nm"]),int(row["Temp_K"]))].append(row)
    expected={(int(r["MEB_nm"]),int(r["Temp_K"])):float(r["tret_IVSN_1to0p8_est_s"]) for r in cases}
    if len(groups)!=20 or len(expected)!=20:
        raise AssertionError("20/20 MEB/T mapping expected")
    max_rel=0.0
    for key,group in sorted(groups.items()):
        value=estimate(group,args.capacitance)
        relative=abs(value-expected[key])/expected[key]
        max_rel=max(max_rel,relative)
        print(f"MEB={key[0]:2d}nm T={key[1]}K: {value:.9g}s  relative_QC={relative:.3g}")
    print(f"Checked {len(groups)} cases, maximum relative deviation={max_rel:.3g}")
    if max_rel>1e-6:
        raise AssertionError("Saved estimates do not match direct IVSN integration")

if __name__=="__main__":
    main()
