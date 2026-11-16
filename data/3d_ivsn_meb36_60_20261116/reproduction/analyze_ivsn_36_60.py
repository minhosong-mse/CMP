from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import csv, hashlib, math, re, json, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
SRC = ROOT/"upload/CMP_IVSN_MISSING_6MEB_EXPORT_20261116_180122.zip"
OUT = ROOT/"CMP_IVSN_36_60_RESULTS_20261116"
OUT.mkdir(exist_ok=True)
FIG = OUT/"figures"
FIG.mkdir(exist_ok=True)
temps = [233,300,340,380]
mapping = {37:[112,873,1428,1983],38:[113,888,1443,1998],39:[114,903,1458,2013],
           40:[115,918,1473,2028],58:[594,1188,1743,2298],59:[610,1203,1758,2313]}
C=1e-14
def readcsv(path):
    with open(path, newline="", encoding="utf-8-sig") as f: return list(csv.DictReader(f))
def writecsv(path, rows):
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def calc(v,i,vs):
    z=C/(-i)
    # Two numerical quadratures, independent of source summary.
    trap=float(np.sum(np.diff(v)*(z[:-1]+z[1:])*0.5))
    simp=float((v[-1]-v[0])/100/3*(z[0]+z[-1]+4*z[1:-1:2].sum()+2*z[2:-1:2].sum()))
    residual=abs(i+vs)
    return trap,abs(trap-simp)/trap,float(residual.max()),float((residual/abs(i)).max())

new=[]; curves=[]; normalized=set()
with ZipFile(SRC) as z:
    assert z.testzip() is None
    names=z.namelist()
    tree={}
    for l in z.read("gtree.dat").decode().splitlines():
        m=re.match(r"^(\d+)\s+(\d+)\s+(\d+)\s+\{([^}]*)\}",l)
        if m: tree[int(m[2])]=(int(m[1]),int(m[3]),m[4])
    for meb, nodes in mapping.items():
        for T,n in zip(temps,nodes):
            plt_file=f"IVSN_0P8_TO_1P0_n{n}_ivsn_sys.plt"
            cmd=f"pp{n}_des.cmd"
            assert names.count(plt_file)==names.count(cmd)==1
            deck=z.read(cmd).decode()
            grid=int(re.search(r'Grid="n(\d+)_msh\.tdr"',deck)[1])
            assert int(re.search(r'Temperature=(\d+)',deck)[1])==T
            assert "capacitance=1e-14" in deck and "dc=-0.7" in deck and "Band2Band(Hurkx)" in deck
            assert 'BCAT cell ("source"=bl "drain"=sn "gate"=wl "substrate"=0)' in deck
            assert "AreaFactor" not in deck
            sde=z.read(f"pp{grid}_dvs.cmd").decode()
            assert int(re.search(r'\(define DBCAT_nm (\d+)\)',sde)[1])==meb
            assert f'(sde:build-mesh "snmesh" "" "n{grid}")' in sde
            p=n; ancestors={}
            while p in tree:
                lv,pnext,val=tree[p];ancestors[lv]=(p,val);p=pnext
            assert ancestors[1]==(grid,str(meb)) and ancestors[3][1]==str(T) and ancestors[4][1]=="1e-14" and ancestors[5][1]=="-0.7"
            normalized.add(re.sub(r'\bn\d+(?=_)','nNODE',re.sub(r'Temperature=\d+','Temperature=T',deck)))
            log=z.read(f"n{n}_des.log").decode(errors="replace")
            sta=z.read(f"n{n}_des.sta").decode()
            assert "|done|" in sta and "Curve trace finished." in log and "Sentaurus Device simulation finished" in log
            raw=z.read(plt_file).decode()
            fields=re.findall(r'"([^"]+)"',raw.split("datasets")[1].split("functions")[0])
            assert fields==["v(sn)","v(bl)","v(wl)","i(cell,sn)","i(cell,bl)","i(vsn,sn)"]
            data=np.array([float(x) for x in re.search(r'Data\s*\{(.*?)\}',raw,re.S)[1].split()]).reshape(-1,6)
            v,bl,wl,i,ibl,vs=data.T
            assert data.shape==(101,6) and np.isfinite(data).all()
            assert np.allclose(v,np.linspace(.8,1,101),rtol=0,atol=1e-10)
            assert np.max(abs(bl))<1e-12 and np.max(abs(wl+.7))<1e-12 and np.all(i<0) and np.all(vs>0)
            t,quad,kcl,krel=calc(v,i,vs)
            status="PASS_LOW_CURRENT_KCL_WARNING" if krel>.01 else "PASS"
            new.append(dict(MEB_nm=meb,Temp_K=T,grid_node=grid,device_node=n,points=len(v),
                            VSN_start=v[0],VSN_end=v[-1],I_SN_0p8_A=i[0],I_SN_0p9_A=i[50],I_SN_1p0_A=i[-1],
                            t_est_s=t,simpson_relative_difference=quad,KCL_max_A=kcl,KCL_max_relative=krel,
                            qc_status=status,log_status="done",source_file=plt_file))
            for row in data:
                curves.append(dict(MEB_nm=meb,Temp_K=T,device_node=n,v_sn_V=row[0],v_bl_V=row[1],v_wl_V=row[2],
                                   i_cell_sn_A=row[3],i_cell_bl_A=row[4],i_vsn_sn_A=row[5]))
    assert len(normalized)==1, len(normalized)
assert len(new)==24 and len(curves)==2424
writecsv(OUT/"IVSN_24_new_case_QC.csv",new)
writecsv(OUT/"IVSN_24_new_curves.csv",curves)
prior=readcsv(ROOT/"Retention_combined_36_41to57_60_seconds.csv")
oldqc={(int(r["MEB_nm"]),int(r["Temp_K"])):r for r in readcsv(ROOT/"IVSN_68_case_node_map_and_QC.csv")}
oldend={(int(r["MEB_nm"]),int(r["Temp_K"])):r for r in readcsv(ROOT/"case_metrics.csv")}
endcurves=readcsv(ROOT/"ivsn_historic_endpoints.csv")
endqc={}
for m in (36,60):
    for T in temps:
        es=sorted([r for r in endcurves if int(r["MEB_nm"])==m and int(r["Temp_K"])==T],key=lambda r:float(r["v_sn_V"]))
        vv,ii,vs=[np.array([float(r[k]) for r in es]) for k in ("v_sn_V","i_cell_sn_A","i_vsn_sn_A")]
        assert len(es)==101
        endqc[m,T]=calc(vv,ii,vs)
        assert abs(endqc[m,T][0]-float(oldend[m,T]["tret_IVSN_1to0p8_est_s"]))/endqc[m,T][0]<1e-10
newmap={(r["MEB_nm"],r["Temp_K"]):r for r in new}
oldmap={(int(r["MEB_nm"]),T):float(r[f"{T}K_t_est_s"]) for r in prior for T in temps}
assert set(newmap).isdisjoint(oldmap) and len(oldmap)==76
merged=[]
for m in range(36,61):
    for T in temps:
        key=m,T
        if key in newmap:
            r=newmap[key]; g,n,t,stat,src=r["grid_node"],r["device_node"],r["t_est_s"],r["qc_status"],"2026-11-16 upload (Nov-13 run)"
        elif key in oldqc:
            r=oldqc[key]; g,n,t,stat,src=r["grid_node"],r["device_node"],oldmap[key],r["qc_status"],"2026-11-13 Git 68-case"
        else:
            r=oldend[key];g,n,t,src=r["grid_node"],r["node"],oldmap[key],"2026-11-11 Git source"
            stat="PASS_LOW_CURRENT_KCL_WARNING" if endqc[key][3]>.01 else "PASS"
        merged.append(dict(MEB_nm=m,Temp_K=T,grid_node=g,device_node=n,t_est_s=t,qc_status=stat,source=src))
assert len(merged)==100
writecsv(OUT/"RETENTION_100_CASE_MASTER.csv",merged)
lookup={(r["MEB_nm"],r["Temp_K"]):r["t_est_s"] for r in merged}
matrix=[dict(MEB_nm=m,**{f"{T}K_t_est_s":lookup[m,T] for T in temps}) for m in range(36,61)]
writecsv(OUT/"RETENTION_MATRIX_SECONDS.csv",matrix)
writecsv(OUT/"RETENTION_MATRIX_READABLE.csv",[dict(MEB_nm=m,**{f"{T}K_t_est_{'s' if T==233 else 'ms'}":lookup[m,T]*(1 if T==233 else 1000) for T in temps}) for m in range(36,61)])
rel=[dict(MEB_nm=m,**{f"{T}K_vs36_ratio":lookup[m,T]/lookup[36,T] for T in temps}) for m in range(36,61)]
writecsv(OUT/"RELATIVE_RETENTION_VS36.csv",rel)
inc=[dict(MEB_from_nm=m-1,MEB_to_nm=m,**{f"{T}K_gain_pct_per_nm":(lookup[m,T]/lookup[m-1,T]-1)*100 for T in temps}) for m in range(37,61)]
writecsv(OUT/"INCREMENTAL_GAIN_PER_NM.csv",inc)
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False,"figure.dpi":140})
colors=["#2563eb","#0f766e","#b45309","#be123c"]
x=list(range(36,61))
def finish(fig,name):
    fig.tight_layout();fig.savefig(FIG/(name+".svg"),bbox_inches="tight");fig.savefig(FIG/(name+".png"),bbox_inches="tight");plt.close(fig)
def style(ax):
    ax.set_xlabel("MEB depth (nm)");ax.set_xticks(range(36,61,2));ax.grid(alpha=.22)
fig,ax=plt.subplots(figsize=(8,4.8))
for T,c in zip(temps,colors):
    ax.plot(x,[lookup[m,T] for m in x],color=c,marker="o",ms=3,label=f"{T} K"+(" (QC caution)" if T==233 else ""))
ax.set_yscale("log");ax.set_ylabel("Estimated retention (s, log scale)");ax.legend();style(ax)
ax.set_title("3D BCAT: estimated 1.0-to-0.8 V retention");finish(fig,"01_retention_log")
fig,axs=plt.subplots(2,2,figsize=(10,6.5))
for T,c,ax in zip(temps,colors,axs.flat):
    factor=1 if T==233 else 1000
    ax.plot(x,[lookup[m,T]*factor for m in x],marker="o",ms=3,color=c)
    ax.scatter(list(mapping),[lookup[m,T]*factor for m in mapping],s=33,facecolors="none",edgecolors="#111827",label="Newly extracted")
    style(ax);ax.set_ylabel("Estimated retention ("+("s" if T==233 else "ms")+")")
    ax.set_title(f"{T} K"+(" (low-current QC caution)" if T==233 else ""))
    ax.legend(fontsize=8)
finish(fig,"02_retention_by_temperature")
fig,ax=plt.subplots(figsize=(8,4.8))
for T,c in zip(temps,colors):
    ax.plot(x,[lookup[m,T]/lookup[36,T] for m in x],marker="o",ms=3,color=c,label=f"{T} K")
style(ax);ax.set_ylabel("Retention / retention at 36 nm");ax.legend();ax.set_title("Relative estimated retention");finish(fig,"03_relative_retention_vs36")
fig,axs=plt.subplots(2,2,figsize=(10,6.5))
for T,c,ax in zip(temps,colors,axs.flat):
    ax.plot(x[1:],[(lookup[m,T]/lookup[m-1,T]-1)*100 for m in x[1:]],marker="o",ms=3,color=c)
    ax.axhline(0,color="black",lw=.8);style(ax);ax.set_ylabel("Increase per 1 nm (%)");ax.set_title(f"{T} K")
finish(fig,"04_incremental_gain")
fig,ax=plt.subplots(figsize=(7.5,4.6))
for m,c in zip([36,41,48,54,60],["#64748b",*colors]):
    ax.plot(temps,[lookup[m,T] for T in temps],marker="o",color=c,label=f"{m} nm")
ax.set_yscale("log");ax.set_xlabel("Temperature (K)");ax.set_ylabel("Estimated retention (s)");ax.grid(alpha=.22);ax.legend()
ax.set_title("Temperature dependence at representative depths");finish(fig,"05_temperature_dependence")
fig,ax=plt.subplots(figsize=(7.5,4.6))
for m,c in zip([36,41,48,54,60],["#64748b",*colors]):
    ax.plot([1000/T for T in temps],[math.log(lookup[m,T]) for T in temps],marker="o",color=c,label=f"{m} nm")
ax.set_xlabel("1000/T (K⁻¹)");ax.set_ylabel("ln(estimated retention / s)");ax.grid(alpha=.22);ax.legend()
ax.set_title("Arrhenius-style diagnostic (no activation-energy fit)");finish(fig,"06_arrhenius_diagnostic")
stats={"new_cases":len(new),"new_raw_points":len(curves),"previous_cases":len(oldmap),"total_cases":len(merged),
       "new_warning_count":sum(r["qc_status"]!="PASS" for r in new),
       "new_max_KCL_A":max(r["KCL_max_A"] for r in new),"new_max_KCL_relative":max(r["KCL_max_relative"] for r in new),
       "new_max_simpson_difference":max(r["simpson_relative_difference"] for r in new),
       "source_zip_sha256":hashlib.sha256(SRC.read_bytes()).hexdigest(),"normalized_new_device_deck_count":len(normalized),
       "temperature_summary":[dict(Temp_K=T,t36_s=lookup[36,T],t60_s=lookup[60,T],gain=lookup[60,T]/lookup[36,T],
                                  increasing_intervals=sum(lookup[m,T]>lookup[m-1,T] for m in x[1:]),
                                  max_step=max(inc,key=lambda r:r[f"{T}K_gain_pct_per_nm"])["MEB_to_nm"]) for T in temps]}
(OUT/"QC_SUMMARY.json").write_text(json.dumps(stats,indent=2),encoding="utf-8")
print(json.dumps(stats,indent=2))
print("NEW:")
for r in new: print(r["MEB_nm"],r["Temp_K"],r["t_est_s"],r["KCL_max_relative"],r["qc_status"])
