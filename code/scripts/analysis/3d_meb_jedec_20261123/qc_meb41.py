"""CMP 41 nm 2026-11-23 incremental scientific QC and append-only merge.

Reads the user-provided 41nm SWB native export ZIP and 52nm reference. Does
not change any existing archive/GitHub/canonical 21-depth checkpoint.
"""
from __future__ import annotations
import collections, csv, hashlib, io, json, re, zipfile
from pathlib import Path
import numpy as np

ROOT=Path('/mnt/data')
ZPATH=ROOT/'CMP_OTHER_MEB41_NOV23_20261123_185916.zip'
REFERENCE=ROOT/'CMP_MAIN_NOV23_20261123_173554.zip'
PREV=ROOT/'CMP_NOV23_MEB54_QC'
OUT=ROOT/'CMP_NOV23_MEB41_QC';OUT.mkdir(exist_ok=True)
MEB=41
MODES=(0,1,5,6,7)
TEMP=(233.15,300.,358.15,368.15)


def sha(raw): return hashlib.sha256(raw).hexdigest()

def readplt(z,p):
    raw=z.read(p).decode();parts=raw.split('datasets',1)
    fields=re.findall(r'"([^"]+)"',parts[1].split('functions',1)[0])
    vals=np.fromstring(re.search(r'Data\s*\{(.*?)\}',raw,re.S).group(1),sep=' ')
    assert fields and len(vals)%len(fields)==0,(p,len(vals),len(fields))
    a=vals.reshape(-1,len(fields)).T
    return dict(zip(fields,a))

def norm_sde(s):
    s='\n'.join(l for l in s.splitlines() if not l.lstrip().startswith(';'))
    s=re.sub(r'\(define DBCAT_nm\s+[\d.]+\)','(define DBCAT_nm X)',s)
    s=re.sub(r'("n)\d+(")',r'\1X\2',s)
    return re.sub(r'\s+','',s)

def norm_dev(s):
    s='\n'.join(l for l in s.splitlines() if not l.lstrip().startswith('*'))
    s=re.sub(r'\bTemperature\s*=\s*[\d.]+','Temperature=X',s)
    s=re.sub(r'n\d+_','nX_',s)
    return re.sub(r'\s+','',s)

def write(name,rows):
    if not rows: return
    cols=list(dict.fromkeys(k for r in rows for k in r))
    with (OUT/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)

def load(path):
    with path.open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))

def curve(a,vd):
    mask=np.isclose(a['drain OuterVoltage'],vd,atol=1e-9,rtol=0)
    v=a['gate OuterVoltage'][mask];i=a['drain TotalCurrent'][mask]
    ix=np.argsort(v,kind='stable');v=v[ix];i=i[ix]
    keep=np.r_[np.diff(v)>1e-12,True]
    return v[keep],i[keep]

def current_at(v,i,g):
    if not(v[0]<=g<=v[-1]): return None
    ix=np.where(np.isclose(v,g,atol=1e-12,rtol=0))[0]
    if len(ix):return float(i[ix[-1]])
    j=np.searchsorted(v,g)
    if np.min(i[j-1:j+1])>0:
        return float(10**np.interp(g,v[j-1:j+1],np.log10(i[j-1:j+1])))
    return float(np.interp(g,v,i))

def vth(v,i,target):
    ix=np.where((i[:-1]<target)&(i[1:]>=target)&(i[:-1]>0))[0]
    if len(ix)!=1:return None
    j=ix[0]
    return float(np.interp(np.log10(target),np.log10(i[j:j+2]),v[j:j+2]))

with zipfile.ZipFile(ZPATH) as z, zipfile.ZipFile(REFERENCE) as ref:
    assert z.testzip() is None
    names=set(z.namelist())
    mapping=list(csv.DictReader(io.StringIO(z.read('NODE_MAPPING.csv').decode())))
    new=[r for r in mapping if int(r['MEB'])==MEB and r['Category']=='NEW']
    assert len(new)==20,len(new)
    assert len({(float(r['TempK']),int(r['RunMode'])) for r in new})==20
    assert all(r['Project']=='CMP_final_Copy2' for r in new)
    refrows=list(csv.DictReader(io.StringIO(ref.read('NODE_MAPPING.csv').decode())))
    baseline={}
    for r in refrows:
        if int(r['MEB'])==40 and r['Category']=='NEW' and r['Project']=='CMP_3D_Temp_36-48':
            k=int(r['RunMode']);p=r['Project']+'/pp'+r['Node']+'_des.cmd'
            baseline[k]=norm_dev(ref.read(p).decode())
    assert set(baseline)==set(MODES)
    ref_sde=next(r for r in refrows if int(r['MEB'])==40 and r['Project']=='CMP_3D_Temp_36-48')
    refsd=norm_sde(ref.read(ref_sde['Project']+'/pp'+ref_sde['GridNode']+'_dvs.cmd').decode())
    trees={}
    for proj in set(r['Project'] for r in new):
        st=z.read(proj+'/gtree.dat').decode()
        trees[proj]={int(b):(int(a),int(c),v.strip()) for a,b,c,v in re.findall(r'^(\d+)\s+(\d+)\s+(\d+)\s+\{([^}]*)\}',st,re.M)}

    records=[];selected={};sde_hashes=set();dev_hashes=collections.defaultdict(set)
    for r in new:
        n=r['Node'];d=int(r['MEB']);t=float(r['TempK']);m=int(r['RunMode']);g=r['GridNode'];p=r['Project']+'/'
        pl=p+(f'IVSN_0P8_TO_1P0_n{n}_ivsn_sys.plt' if m==7 else f'n{n}_des.plt')
        sd=p+f'pp{g}_dvs.cmd';dev=p+f'pp{n}_des.cmd';sta=p+f'n{n}_des.sta';log=p+f'n{n}_des.log'
        assert all(x in names for x in [sd,dev,sta,log]),(t,m,n,'core source absent')
        tree=trees[r['Project']];lev,par,mo=tree[int(n)];lt,pt,tv=tree[par];lg,pg,_=tree[pt];ld,pd,dv=tree[pg]
        assert (lev,lt,lg,ld)==(4,3,2,1) and mo==str(m) and float(tv)==t and int(float(dv))==d and str(pg)==g,(t,m,n,'tree mismatch')
        cmd=z.read(dev).decode();sdetxt=z.read(sd).decode();st=z.read(sta).decode();ll=z.read(log).decode(errors='replace')
        grid=re.search(r'Grid\s*=\s*"n(\d+)_msh\.tdr"',cmd)
        temp=re.search(r'Temperature\s*=\s*([\d.]+)',cmd)
        depth=re.search(r'\(define\s+DBCAT_nm\s+([\d.]+)\)',sdetxt)
        assert grid and grid[1]==g and temp and abs(float(temp[1])-t)<1e-6 and depth and float(depth[1])==d
        assert norm_sde(sdetxt)==refsd,('SDE template mismatch',t,m)
        assert norm_dev(cmd)==baseline[m],('DEVICE template mismatch',t,m)
        phys='Recombination(Band2Band(Hurkx))' in '\n'.join(l for l in cmd.splitlines() if not l.lstrip().startswith('*'))
        assert phys==(m!=6),('physics',m)
        done='|done|' in st and 'Sentaurus Device simulation finished' in ll and 'Good Bye' in ll
        a=readplt(z,pl) if pl in names else None
        finite=bool(a is not None and all(np.isfinite(x).all() for x in a.values()))
        if a is not None and finite:
            if m==7:
                end=float(a['v(sn)'][-1]);drain=None
                ep=abs(end-1)<1e-6
                ivok=(len(a['v(sn)'])==101 and np.allclose(a['v(sn)'],np.linspace(.8,1,101),atol=1e-9,rtol=0) and np.allclose(a['v(bl)'],0) and np.allclose(a['v(wl)'],-.7) and np.all(a['i(cell,sn)']<0) and np.all(a['i(vsn,sn)']>0))
            else:
                end=float(a['gate OuterVoltage'][-1]);drain=float(a['drain OuterVoltage'][-1])
                ep=abs(end-{0:1.5,1:2,5:-.7,6:-.7}[m])<1e-6 and abs(drain-(.05 if m==0 else 1.2))<1e-6;ivok=True
        else:end=None;drain=None;ep=False;ivok=False
        valid=bool(done and ep and ivok and finite)
        sde_hashes.add(sha(norm_sde(sdetxt).encode()));dev_hashes[m].add(sha(norm_dev(cmd).encode()))
        record={'MEB_nm':d,'Temp_K':t,'RunMode':m,'project':r['Project'],'node':n,'grid':g,
                'status':st.split('|')[2] if len(st.split('|'))>2 else st,'done':bool(done),
                'endpoint_V':end,'drain_endpoint_V':drain,'target_reached':bool(ep),'IVSN_protocol':bool(ivok),
                'finite':bool(finite),'samples':len(next(iter(a.values()))) if a is not None else None,
                'QC':'PASS' if valid else 'FAIL','plt_sha256':sha(z.read(pl)) if pl in names else '',
                'device_sha256':sha(z.read(dev)),'sde_sha256':sha(z.read(sd)),
                'SDE_template_match':True,'SDevice_template_match':True}
        records.append(record)
        if valid:selected[(d,t,m)]={'data':a,'record':record}
    print('41 nm QC',collections.Counter(r['QC'] for r in records))
    assert len(sde_hashes)==1 and all(len(s)==1 for s in dev_hashes.values())
    metrics=[];dc=[];ivsn=[]
    for t in TEMP:
        rr={m:selected.get((MEB,t,m)) for m in MODES}
        row=dict(MEB_nm=MEB,Temp_K=t,valid_modes=sum(x is not None for x in rr.values()),scope='NEW')
        for m,s in rr.items():
            if s is None:continue
            a=s['data'];record=s['record']
            if m==7:
                v=a['v(sn)'];i=a['i(cell,sn)'];ivs=a['i(vsn,sn)']
                fn=np.trapezoid if hasattr(np,'trapezoid') else np.trapz
                tm=float(fn(1e-14/-i,v));kcl_abs=float(np.max(abs(i+ivs)));kcl_rel=float(np.max(abs(i+ivs)/abs(i)))
                row.update(t_est_s=tm,Ieq_A=2e-15/tm,IVSN_KCL_max_A=kcl_abs,IVSN_KCL_max_relative=kcl_rel,IVSN_QC='LOW_CURRENT_KCL_WARNING' if kcl_rel>.01 else 'PASS',retention_screen='PASS' if tm>=(.032 if t==368.15 else .064) else 'FAIL')
                for j in range(len(v)):ivsn.append(dict(MEB_nm=MEB,Temp_K=t,project=record['project'],node=record['node'],**{k:float(x[j]) for k,x in a.items()}))
            else:
                v,i=curve(a,.05 if m==0 else 1.2)
                for j in range(len(v)):dc.append(dict(MEB_nm=MEB,Temp_K=t,RunMode=m,project=record['project'],node=record['node'],Vg_V=float(v[j]),Id_A=float(i[j])))
                if m==0:row['Vth_low_V']=vth(v,i,8.5e-8)
                elif m==1:
                    row.update(Ion_A=current_at(v,i,1.2),Ioff_A=current_at(v,i,0),Vth_high_V=vth(v,i,8.5e-8))
                    lo,hi=vth(v,i,1e-10),vth(v,i,1e-8)
                    row['SS_mV_dec']=(hi-lo)*500 if lo is not None and hi is not None else None
                else:row['Id_Hurkx_'+('ON' if m==5 else 'OFF')+'_A']=float(a['drain TotalCurrent'][-1])
        if row.get('Vth_low_V') is not None and row.get('Vth_high_V') is not None:row['DIBL_mV_V']=(row['Vth_low_V']-row['Vth_high_V'])/1.15*1000
        if 'Id_Hurkx_ON_A' in row and 'Id_Hurkx_OFF_A' in row:row['Hurkx_excess_A']=row['Id_Hurkx_ON_A']-row['Id_Hurkx_OFF_A']
        metrics.append(row)
    write('MEB41_node_qc.csv',records)
    write('MEB41_six_metrics.csv',metrics)
    write('MEB41_DC_curves.csv',dc)
    write('MEB41_IVSN_curves.csv',ivsn)
    manifest=dict(source_zip=ZPATH.name,source_zip_sha256=sha(ZPATH.read_bytes()),source_size_bytes=ZPATH.stat().st_size,
                  new_mapped=len(new),new_endpoint_pass=len(selected),new_failed=[r for r in records if r['QC']=='FAIL'],
                  selected_project=new[0]['Project'],sde_grid_node=new[0]['GridNode'],sde_template_sha256=next(iter(sde_hashes)),
                  reference_40_source=REFERENCE.name,reference_40_sde_template_sha256=sha(refsd.encode()),
                  new_41_device_template_sha256={str(k):next(iter(s)) for k,s in dev_hashes.items()},
                  recovery_candidates_archived=len(mapping)-len(new),
                  dedup_note='11 recovery candidates in this ZIP are ignored: their canonical post-R1 results were already incorporated from prior Nov23 ZIPs; no overwriting.')
    (OUT/'source_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    for r in metrics:print('METRIC',r['Temp_K'],'Ion_uA',r.get('Ion_A',0)*1e6,'Ioff_fA',r.get('Ioff_A',0)*1e15,'SS',r.get('SS_mV_dec'), 'DIBL',r.get('DIBL_mV_V'),'Hurkx_fA',r.get('Hurkx_excess_A',0)*1e15,'IVSN_ms',r.get('t_est_s',0)*1e3,'KCL_ratio',r.get('IVSN_KCL_max_relative'))

    # Merge delta into existing Nov23 incremental data only. Existing files immutable.
    for name,newrows in [('selected_cases.csv',[{'MEB_nm':r['MEB_nm'],'Temp_K':r['Temp_K'],'RunMode':r['RunMode'],'account':'OTHER','archive':ZPATH.name,'project':r['project'],'node':r['node'],'grid':r['grid'],'R1':False,'data_sha256':r['plt_sha256']} for r in records if r['QC']=='PASS']),('six_metrics_new_and_recovery.csv',metrics),('dc_curves_selected.csv',dc),('ivsn_curves_selected.csv',ivsn)]:
        old=load(PREV/('UPDATED_'+name))
        if name=='selected_cases.csv': ident=lambda r:(int(r['MEB_nm']),float(r['Temp_K']),int(r['RunMode']))
        elif name=='six_metrics_new_and_recovery.csv': ident=lambda r:(int(r['MEB_nm']),float(r['Temp_K']))
        elif name=='dc_curves_selected.csv': ident=lambda r:(int(r['MEB_nm']),float(r['Temp_K']),int(r['RunMode']),float(r['Vg_V']))
        else:ident=lambda r:(int(r['MEB_nm']),float(r['Temp_K']),float(r['v(sn)']))
        assert not (set(map(ident,old)) & set(map(ident,newrows))),('duplicate keys',name)
        write('UPDATED_'+name,old+newrows)
    status=load(PREV/'UPDATED_DEPTH_STATUS.csv')
    for r in status:
        if r['MEB_nm']==str(MEB):r.update(Status='EXPORTED_NEW',Validated_Jobs=str(len(selected)))
    write('UPDATED_DEPTH_STATUS.csv',status)
    rerun=load(PREV/'UPDATED_REMAINING_RERUNS.csv')
    rerun.extend([{'Account':'OTHER','MEB_nm':MEB,'Temp_K':r['Temp_K'],'RunMode':r['RunMode'],'OriginalProject':r['project'],'Node':r['node'],'LastBias_V':r['endpoint_V'],'RequestedBias_V':1 if r['RunMode']==7 else {0:1.5,1:2,5:-.7,6:-.7}.get(r['RunMode']), 'Reason':'FAILED_ENDPOINT'} for r in records if r['QC']=='FAIL'])
    write('UPDATED_REMAINING_RERUNS.csv',rerun)
    prev_candidates=load(PREV/'UPDATED_node_qc_all_candidates.csv')
    cols=prev_candidates[0].keys()
    additions=[]
    for r in records:
        x={'archive':ZPATH.name,'account':'OTHER','project':r['project'],'node':r['node'],'grid':r['grid'],'MEB_nm':r['MEB_nm'],'Temp_K':r['Temp_K'],'RunMode':r['RunMode'],'kind':'NEW','valid':r['QC']=='PASS','reason':r['QC'],'pp_verified':True,'physics_verified':True,'done':r['done'],'solver_R1':False,'n_samples':r['samples'],'drain_endpoint':r['drain_endpoint_V'],'endpoint':r['endpoint_V'],'endpoint_ok':r['target_reached'],'iv_ok':r['IVSN_protocol'],'plt_sha256':r['plt_sha256']}
        additions.append(x)
    write('UPDATED_node_qc_all_candidates.csv',prev_candidates+additions)
    summary={'MEB_depths_exported':sum(r['Status']!='NOT_EXPORTED' for r in status),'depths_total':37,'MEB41_valid':len(selected),'MEB41_total':20,'all_selected_VALID':sum(int(x['Validated_Jobs']) for x in status),'total_campaign':740,'not_yet_valid':740-sum(int(x['Validated_Jobs']) for x in status),'not_exported_MEB':[int(x['MEB_nm']) for x in status if x['Status']=='NOT_EXPORTED'],'unresolved_reruns':rerun,'source_sha256':manifest['source_zip_sha256']}
    (OUT/'UPDATED_SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
    print('SUMMARY',json.dumps({k:v for k,v in summary.items() if k!='unresolved_reruns'}))
