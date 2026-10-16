#!/usr/bin/env python3
"""Replot actual CMP L1 IDVG/IDVD (24/36/48 nm) without inventing paper data.

Usage:
  python3 code/analysis/plot_dbcat_figure_2d_20261016.py \
    --nl-idvg NONLOCAL_IDVG_24_36_48nm.csv \
    --nl-idvd NONLOCAL_IDVD_9CURVES.csv \
    --hk-idvg HURKX_IDVG_36_48nm.csv \
    --hk-idvd HURKX_IDVD_9CURVES.csv \
    --out ./dbcat_figures

Optional: --paper-idvg / --paper-idvd accepts manually and independently
digitized REAL figure-point CSV, not hand-guessed synthetic anchors.
Paper IDVG columns: DBCAT_nm,VG_V,Id_A_per_um.
Paper IDVD columns: DBCAT_nm,VG_fixed_V,VD_V,Id_A_per_um.
"""
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

p = argparse.ArgumentParser()
for key in ("nl-idvg", "nl-idvd", "hk-idvg", "hk-idvd"):
    p.add_argument("--" + key, required=True, type=Path)
p.add_argument("--paper-idvg", type=Path)
p.add_argument("--paper-idvd", type=Path)
p.add_argument("--out", type=Path, default=Path("dbcat_figures"))
a = p.parse_args()
a.out.mkdir(parents=True, exist_ok=True)

datasets = {
    "NonlocalPath": {
        "IDVG": pd.read_csv(a.nl_idvg),
        "IDVD": pd.read_csv(a.nl_idvd),
    },
    "Hurkx": {
        "IDVG": pd.read_csv(a.hk_idvg),
        "IDVD": pd.read_csv(a.hk_idvd),
    },
}
paper = {}
if a.paper_idvg:
    paper["IDVG"] = pd.read_csv(a.paper_idvg)
if a.paper_idvd:
    paper["IDVD"] = pd.read_csv(a.paper_idvd)

for typ in ("IDVG", "IDVD"):
    df = pd.concat([v[typ] for v in datasets.values()], ignore_index=True)
    assert df["Id_total_A_per_um"].notna().all()
    assert set(df.MEB_nm.unique()) <= {24, 36, 48}
    if typ == "IDVG":
        assert all(len(g) == 601 for _, g in df.groupby(["model", "MEB_nm"]))
    else:
        assert all(len(g) == 201 for _, g in df.groupby(["model", "MEB_nm", "VG_V"]))

# One transfer panel per MEB, with clear missing Hurkx 24nm.
fig, axs = plt.subplots(1, 3, figsize=(15, 4.6), sharex=True, sharey=True)
for ax, depth in zip(axs, [24,36,48]):
    for model in ("NonlocalPath","Hurkx"):
        sub = datasets[model]["IDVG"]
        sub = sub[sub.MEB_nm == depth].sort_values("VG_V")
        if not sub.empty:
            ax.semilogy(sub.VG_V, sub.Id_total_A_per_um.abs().clip(lower=1e-20),
                        lw=1.7, label=model)
    if "IDVG" in paper:
        pp = paper["IDVG"]
        sub = pp[pp.DBCAT_nm == depth].sort_values("VG_V")
        if not sub.empty:
            ax.semilogy(sub.VG_V, sub.Id_A_per_um, color="black", ls=":",
                        lw=1.3, label="Paper (digitized)")
    ax.set(title=f"MEB / D_BCAT = {depth} nm", xlabel="Gate Voltage [V]")
    ax.grid(alpha=.2, which="both")
    if depth == 24:
        ax.text(.03,.04,"Hurkx 24nm IDVG: not converged",transform=ax.transAxes,fontsize=8)
    ax.legend(fontsize=8)
axs[0].set_ylabel("|Drain Current| [A/um]")
fig.suptitle("300 K, VD=1.2 V | PAPER-CAL-derived L1 | 2D model comparison")
fig.tight_layout()
fig.savefig(a.out / "IDVG_3depth_2d_and_optional_paper.png",dpi=200)
plt.close(fig)

# One output panel per VG; three MEB colors, model line-style.
fig, axs = plt.subplots(1,3,figsize=(15,4.7),sharex=True,sharey=True)
colors = {24:"tab:blue",36:"tab:orange",48:"tab:green"}
for ax,vg in zip(axs,[.1,.6,1.2]):
    for depth in [24,36,48]:
        for model,ls in [("Hurkx","-"),("NonlocalPath","--")]:
            sub = datasets[model]["IDVD"]
            sub = sub[(sub.MEB_nm==depth)&np.isclose(sub.VG_V,vg)].sort_values("VD_V")
            if not sub.empty:
                ax.plot(sub.VD_V,sub.Id_total_A_per_um.abs(),ls=ls,lw=1.4,
                        color=colors[depth],label=f"{depth}nm {model}")
        if "IDVD" in paper:
            pp=paper["IDVD"]
            sub=pp[(pp.DBCAT_nm==depth)&np.isclose(pp.VG_fixed_V,vg)].sort_values("VD_V")
            if not sub.empty:
                ax.plot(sub.VD_V,sub.Id_A_per_um,ls=":",lw=1.1,color=colors[depth],
                        label=f"{depth}nm Paper digitized")
    ax.set(title=f"VG = {vg} V",xlabel="Drain Voltage [V]")
    ax.grid(alpha=.25)
    ax.legend(fontsize=6.5,ncol=2)
axs[0].set_ylabel("|Drain Current| [A/um]")
fig.suptitle("300 K | 2D L1 IDVD | optional paper only from traceable digitization")
fig.tight_layout()
fig.savefig(a.out / "IDVD_3vg_2d_and_optional_paper.png",dpi=200)
plt.close(fig)
print("Plots written to",a.out)
