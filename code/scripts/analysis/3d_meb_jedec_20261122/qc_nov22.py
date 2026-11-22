"""Nov-22 incremental archive; run from workspace with original ZIPs in upload/.
Old 18-depth checkpoint is read-only. No simulation or reruns are performed."""
import argparse, csv, zipfile, re, collections, numpy as np
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument('--archive-dir',type=Path,default=Path('upload'))
parser.add_argument('--repo-root',type=Path,default=Path(__file__).resolve().parents[4])
args=parser.parse_args()
sources = [
    args.archive_dir/'CMP_1MEB_MAIN_20261122_230245.zip',
    args.archive_dir/'CMP_2MEB_OTHER_20261122_230236(1).zip',
]
supp = {}
for filename in [args.archive_dir/'CMP_60_SDE.zip',args.archive_dir/'CMP_48_59_SDE.zip']:
    with zipfile.ZipFile(filename) as z:
        for name in z.namelist():
            supp[name] = z.read(name).decode()
def norm_sde(s):
    s='\n'.join(l for l in s.splitlines() if not l.lstrip().startswith(';'))
    s=re.sub(r'\(define DBCAT_nm \d+\)', '(define DBCAT_nm X)',s)
    s=re.sub(r'("n)\d+(")',r'\1X\2',s)
    return re.sub(r'\s+','',s)
assert len(set(map(norm_sde,supp.values())))==1
assert len(supp)==3

def readplt(z, p):
    raw=z.read(p).decode()
    fields=re.findall(r'"([^"]+)"',raw.split('datasets')[1].split('functions')[0])
    return dict(zip(fields,np.array([float(v) for v in re.search(r'Data\s*\{(.*?)\}',raw,re.S)[1].split()]).reshape(-1,len(fields)).T))

allgood={}; allcases={}; candidates=collections.defaultdict(list)
for f in sources:
    z=zipfile.ZipFile(f); ns=set(z.namelist()); rows=list(csv.DictReader(z.read('NODE_MAPPING.csv').decode().splitlines())); print(f,len(rows),len(set((r['MEB'],r['TempK'],r['RunMode']) for r in rows)))
    c=collections.Counter(); issues=[]; good=collections.defaultdict(list); expected=set()
    for r in rows:
        if r['Project']=='CMP_final_Copy2':
            # Exact duplicate of CMP_final. The supplemental SDE belongs to
            # CMP_final, so validate the duplicate source but select the original.
            n=r['Node']; m=int(r['RunMode'])
            fn=f'IVSN_0P8_TO_1P0_n{n}_ivsn_sys.plt' if m==7 else f'n{n}_des.plt'
            for fn in (fn, f'pp{n}_des.cmd'):
                assert z.read('CMP_final/'+fn)==z.read('CMP_final_Copy2/'+fn)
            continue
        p=r['Project']+'/';n=r['Node'];m=int(float(r['RunMode']));k=(int(float(r['MEB'])),float(r['TempK']),m); expected.add(k)
        pl=p+(f'IVSN_0P8_TO_1P0_n{n}_ivsn_sys.plt' if m==7 else f'n{n}_des.plt'); sta=p+f'n{n}_des.sta'; log=p+f'n{n}_des.log';cmd=p+f'pp{n}_des.cmd'
        status=z.read(sta).decode().strip() if sta in ns else ''; done='|done|' in status; rec=dict(key=k,project=r['Project'],node=n,archive=f,status=status,plt=pl,valid=False,reason='absent')
        candidates[k].append(rec)
        if pl not in ns: c['absent']+=1; continue
        try: a=readplt(z,pl)
        except Exception as e: c['parse error']+=1; rec['reason']=str(e); continue
        end=a['v(sn)' if m==7 else 'gate OuterVoltage'][-1]; d=0 if m==7 else a['drain OuterVoltage'][-1]; lg=z.read(log).decode(errors='replace') if log in ns else ''; done=done and 'Sentaurus Device simulation finished' in lg and 'Good Bye' in lg; target={0:1.5,1:2,5:-.7,6:-.7,7:1}[m]; valid=done and abs(end-target)<1e-6 and (m==7 or abs(d-(.05 if m==0 else 1.2))<1e-6) and all(np.isfinite(v).all() for v in a.values())
        grid=None; deckok=False
        if cmd in ns:
            deck=z.read(cmd).decode(); g=re.search(r'Grid\s*=\s*"n(\d+)_msh\.tdr"',deck); t=re.search(r'Temperature\s*=\s*([\d.]+)',deck); grid=g[1] if g else ''; sd=p+f'pp{grid}_dvs.cmd'; sde=z.read(sd).decode() if sd in ns else supp.get(sd,''); depth=re.search(r'\(define DBCAT_nm\s+([\d.]+)\)',sde); physical='Recombination(Band2Band(Hurkx))' in '\n'.join(l for l in deck.splitlines() if not l.lstrip().startswith('*')); deckok=bool(t and float(t[1])==k[1] and depth and float(depth[1])==k[0] and physical==(m!=6))
            tree={int(b):(int(a),int(c),v) for a,b,c,v in re.findall(r'^(\d+)\s+(\d+)\s+(\d+)\s+\{([^}]*)\}',z.read(p+'gtree.dat').decode(),re.M)}
            nl,np_,nv=tree[int(n)]; tl,tp,tv=tree[np_]; gl,gp,gv=tree[tp]; dl,dp,dv=tree[gp]
            deckok=deckok and (nl,tl,gl,dl)==(4,3,2,1) and int(nv)==m and float(tv)==k[1] and int(dv)==k[0] and str(gp)==grid
        valid=valid and deckok
        if m==7 and valid:
            valid=len(a['v(sn)'])==101 and np.allclose(a['v(sn)'],np.linspace(.8,1,101),rtol=0,atol=1e-9) and np.allclose(a['v(bl)'],0) and np.allclose(a['v(wl)'],-.7) and np.all(a['i(cell,sn)']<0) and np.all(a['i(vsn,sn)']>0)
        rec.update(valid=valid,reason='PASS' if valid else f'endpoint={end}, done={done}, deck={deckok}',end=end,grid=grid,points=len(next(iter(a.values()))),data=a)
        c['valid' if valid else 'invalid']+=1
        if valid: good[k].append(rec)
        else: issues.append((k,r['Project'],n,rec['reason'],status[:80]))
    print('COUNTS',c,'unique valid',len(good),'duplicate keys',sum(len(v)>1 for v in good.values())); print('issues',issues); print('missing', sorted(expected-set(good)))
    for k in expected: allcases[k]=True
    for k,v in good.items():
        assert k not in allgood, k
        allgood[k]=v

print('TOTAL',len(allcases),len(allgood)); print('MISSING',sorted(set(allcases)-set(allgood)))
for k in sorted(allcases):
    if k not in allgood: print('FAILED CANDIDATES',k,[(r['project'],r['node'],r['reason'],r['status'].split('\n')[0]) for r in candidates[k]])

assert len(allcases)==60 and len(allgood)==58
assert set(allcases)-set(allgood)=={(48,368.15,7),(60,358.15,1)}
out=args.repo_root/'data/3d_meb_jedec_21depth_20261122'; out.mkdir(parents=True,exist_ok=True)
def writecsv(name, rows):
    with (out/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(dict.fromkeys(k for r in rows for k in r)));w.writeheader();w.writerows(rows)
selected={}; qc=[]; duplicate_conflicts=[]
for k in sorted(allcases):
    m,t,mode=k; pool=allgood.get(k,[])
    row=dict(MEB_nm=m,Temp_K=t,RunMode=mode,valid_candidates=len(pool))
    if pool:
        r=pool[0]
        for other in pool[1:]:
            if not (r['data'].keys()==other['data'].keys() and all(np.array_equal(v,other['data'][key]) for key,v in r['data'].items())):
                duplicate_conflicts.append((k,r['project'],other['project']))
        selected[k]=r
        row.update(status='PASS',archive=Path(r['archive']).name,project=r['project'],node=r['node'],grid=r['grid'],points=r['points'],endpoint_V=r['end'])
    else:
        r=next((x for x in candidates[k] if 'end' in x),next((x for x in candidates[k] if x['status']),candidates[k][0]))
        row.update(status='RERUN',archive=Path(r['archive']).name,project=r['project'],node=r['node'],grid=r.get('grid',''),points=r.get('points',''),endpoint_V=r.get('end',''),reason=r['reason'])
    qc.append(row)
print('DUPLICATE CONFLICTS',duplicate_conflicts)
assert not duplicate_conflicts
previous=out.parent/'3d_meb_jedec_18depth_20261121'
def norm_device(s):
    s='\n'.join(l for l in s.splitlines() if not l.lstrip().startswith('*'))
    s=re.sub(r'\bTemperature\s*=\s*[\d.]+','Temperature=X',s)
    s=re.sub(r'n\d+_', 'nX_',s)
    return re.sub(r'\s+','',s)
with (previous/'node_qc_360.csv').open(newline='') as f:
    parent=list(csv.DictReader(f))
refs={}
for mode in [0,1,5,6,7]:
    ref=next(r for r in parent if r['status']=='PASS' and int(r['RunMode'])==mode)
    with zipfile.ZipFile(args.archive_dir/ref['archive']) as z:
        refs[mode]=norm_device(z.read(ref['project']+'/pp'+ref['node']+'_des.cmd').decode())
        if mode==0:
            assert norm_sde(z.read(ref['project']+'/pp'+ref['grid']+'_dvs.cmd').decode())==norm_sde(next(iter(supp.values())))
for k,r in selected.items():
    with zipfile.ZipFile(r['archive']) as z:
        assert norm_device(z.read(r['project']+'/pp'+r['node']+'_des.cmd').decode())==refs[k[2]]
print('All 58 selected PP SDevice decks and three SDE decks match previous template after substitutions.')
writecsv('node_qc_60_new.csv',qc)

def curve(r,vd):
    a=r['data']; mask=np.isclose(a['drain OuterVoltage'],vd,rtol=0,atol=1e-9)
    v=a['gate OuterVoltage'][mask]; i=a['drain TotalCurrent'][mask]; ix=np.argsort(v,kind='stable'); v=v[ix];i=i[ix]
    # keep latest row at identical Vg (start of gate ramp can repeat the drain endpoint)
    keep=np.r_[np.diff(v)>1e-12,True]; return v[keep],i[keep]
def logi(v,i,g):
    if not(v[0]<=g<=v[-1]):return None
    idx=np.where(np.isclose(v,g,atol=1e-12,rtol=0))[0]
    if len(idx): return float(i[idx[-1]])
    j=np.searchsorted(v,g)
    return float(10**np.interp(g,v[j-1:j+1],np.log10(i[j-1:j+1]))) if min(i[j-1:j+1])>0 else float(np.interp(g,v,i))
def vg_at(v,i,target):
    ix=np.where((i[:-1]<target)&(i[1:]>=target)&(i[:-1]>0))[0]
    if len(ix)!=1: return None
    j=ix[0]; return float(np.interp(np.log10(target),np.log10(i[j:j+2]),v[j:j+2]))
metric=[]; iv=[]; dc=[]
for m,t in sorted(set((m,t) for m,t,mode in allcases)):
    rr={i:selected.get((m,t,i)) for i in [0,1,5,6,7]}; row=dict(MEB_nm=m,Temp_K=t,valid_modes=sum(x is not None for x in rr.values()));
    for mode,r in rr.items():
        if not r: continue
        a=r['data']
        if mode==7:
            v=a['v(sn)']; i=a['i(cell,sn)']; vs=a['i(vsn,sn)']; ret=float(np.trapezoid(1e-14/-i,v)); rel=float(np.max(abs(i+vs)/abs(i)))
            row.update(t_est_s=ret,Ieq_A=2e-15/ret,IVSN_KCL_max_A=float(np.max(abs(i+vs))),IVSN_KCL_max_relative=rel,IVSN_QC='LOW_CURRENT_KCL_WARNING' if rel>.01 else 'PASS',retention_screen='PASS' if ret>=(.032 if t==368.15 else .064) else 'FAIL')
            for j in range(len(v)): iv.append(dict(MEB_nm=m,Temp_K=t,node=r['node'],**{k:float(x[j]) for k,x in a.items()}))
        else:
            v,i=curve(r,.05 if mode==0 else 1.2)
            for j in range(len(v)): dc.append(dict(MEB_nm=m,Temp_K=t,RunMode=mode,node=r['node'],Vg_V=v[j],Id_A=i[j]))
            if mode==0: row['Vth_low_V']=vg_at(v,i,8.5e-8)
            elif mode==1:
                row.update(Ion_A=logi(v,i,1.2),Ioff_A=logi(v,i,0),Vth_high_V=vg_at(v,i,8.5e-8))
                lo,hi=vg_at(v,i,1e-10),vg_at(v,i,1e-8); row['SS_mV_dec']=(hi-lo)*500 if lo is not None and hi is not None else None
            elif mode in (5,6): row[f'Id_Hurkx_{"ON" if mode==5 else "OFF"}_A']=float(a['drain TotalCurrent'][-1])
    if row.get('Vth_low_V') is not None and row.get('Vth_high_V') is not None: row['DIBL_mV_V']=(row['Vth_low_V']-row['Vth_high_V'])/1.15*1000
    if all(k in row for k in ('Id_Hurkx_ON_A','Id_Hurkx_OFF_A')): row['Hurkx_excess_A']=row['Id_Hurkx_ON_A']-row['Id_Hurkx_OFF_A']
    metric.append(row)
writecsv('six_metrics_12_new.csv',metric);writecsv('ivsn_curves_new.csv',iv);writecsv('dc_curves_new.csv',dc)
# Append only the new depths to the immutable Nov-21 master; raw extracted
# curves are stored as a delta, to avoid duplicating the historical archive.
def merge(oldfile,newrows,name,keys):
    with (previous/oldfile).open(newline='') as f: old=list(csv.DictReader(f))
    def key(r): return tuple(float(r[k]) for k in keys)
    assert not set(map(key,old)) & set(map(key,newrows))
    writecsv(name, sorted(old+newrows,key=key))
merge('node_qc_360.csv',qc,'node_qc_420.csv',['MEB_nm','Temp_K','RunMode'])
merge('six_metrics_72_conditions.csv',metric,'six_metrics_84_conditions.csv',['MEB_nm','Temp_K'])
print('METRIC COUNTS',[(k,sum(r.get(k) is not None for r in metric)) for k in ('Ion_A','Ioff_A','SS_mV_dec','DIBL_mV_V','Hurkx_excess_A','t_est_s')]); print('FULL ROWS',sum(r['valid_modes']==5 for r in metric));print('RETENTION WARNINGS',[(r['MEB_nm'],r['Temp_K'],r['IVSN_KCL_max_relative']) for r in metric if r.get('IVSN_QC')=='LOW_CURRENT_KCL_WARNING'])
for r in metric:
    if r['Temp_K']==300: print('300K',r['MEB_nm'],r.get('Ion_A'),r.get('Ioff_A'),r.get('SS_mV_dec'),r.get('DIBL_mV_V'),r.get('Hurkx_excess_A'),r.get('t_est_s'))
