#!/usr/bin/env python3
"""CMP 2026-11-23 MEB53 scientific QC, source-based & terminal endpoint audit.

Requires NumPy, SWB export V3 source ZIP for MEB53 and accepted MEB54 reference.
No Sentaurus invocation. Reports all mapped conditions including failed traces.
Expected CLI: python qc_cmp_meb53_nov23.py --source ... --reference ... --out ...
"""
from __future__ import annotations
import argparse,csv,hashlib,io,json,re,zipfile
from pathlib import Path
import numpy as np

P=argparse.ArgumentParser()
P.add_argument('--source',type=Path,default=Path('/mnt/data/CMP_MAIN_MEB53_NOV23_20261123_192708.zip'))
P.add_argument('--reference',type=Path,default=Path('/mnt/data/CMP_MAIN_MEB54_NOV23_20261123_175736.zip'))
P.add_argument('--out',type=Path,default=Path('/mnt/data/CMP_NOV23_MEB53_QC'))
a=P.parse_args()
a.out.mkdir(parents=True,exist_ok=True)
SHA=lambda v:hashlib.sha256(v).hexdigest()
TEMPS=(233.15,300.,358.15,368.15)
MODES=(0,1,5,6,7)

def norm_sde(t):
 t='\n'.join(x for x in t.splitlines() if not x.lstrip().startswith(';'))
 t=re.sub(r'\(define\s+DBCAT_nm\s+[\d.]+\)','(define DBCAT_nm X)',t)
 t=re.sub(r'("n)\d+(")',r'\1X\2',t)
 return re.sub(r'\s+','',t)
def norm_dev(t):
 t='\n'.join(x for x in t.splitlines() if not x.lstrip().startswith('*'))
 t=re.sub(r'\bTemperature\s*=\s*[\d.]+','Temperature=X',t)
 t=re.sub(r'n\d+_','nX_',t)
 return re.sub(r'\s+','',t)

def readplt(z,filename):
 raw=z.read(filename).decode(errors='replace')
 ds=raw.split('datasets',1)[1].split('functions',1)[0]
 fields=re.findall(r'"([^"]+)"',ds)
 dat=re.search(r'Data\s*\{(.*?)\}',raw,re.S)
 if not(fields and dat):raise ValueError('bad PLT header/data')
 num=np.fromstring(dat[1],sep=' ')
 if not len(num)%len(fields)==0:raise ValueError('PLT width mismatch')
 return dict(zip(fields,num.reshape(-1,len(fields)).T))

def write(name,rows,headers=None):
 if not rows and not headers:return
 if headers is None:headers=list(dict.fromkeys(k for row in rows for k in row))
 with (a.out/name).open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=headers,extrasaction='ignore');w.writeheader();w.writerows(rows)

def cv(a,vd):
 mask=np.isclose(a['drain OuterVoltage'],vd,atol=1e-9,rtol=0)
 v=a['gate OuterVoltage'][mask];i=a['drain TotalCurrent'][mask]
 order=np.argsort(v,kind='stable');v=v[order];i=i[order]
 keep=np.r_[np.diff(v)>1e-12,True]
 return v[keep],i[keep]
def logi(v,i,g):
 if len(v)<2 or not v[0]<=g<=v[-1]:return None
 hits=np.where(np.isclose(v,g,atol=1e-12,rtol=0))[0]
 if len(hits):return float(i[hits[-1]])
 j=np.searchsorted(v,g)
 if np.min(i[j-1:j+1])>0:return float(10**np.interp(g,v[j-1:j+1],np.log10(i[j-1:j+1])))
 return float(np.interp(g,v,i))
def vth(v,i,target):
 ii=np.where((i[:-1]<target)&(i[1:]>=target)&(i[:-1]>0))[0]
 if len(ii)!=1:return None
 j=ii[0];return float(np.interp(np.log10(target),np.log10(i[j:j+2]),v[j:j+2]))

with zipfile.ZipFile(a.source) as z,zipfile.ZipFile(a.reference) as ref:
 assert z.testzip() is None
 names=set(z.namelist())
 raw=list(csv.DictReader(io.StringIO(z.read('NODE_MAPPING.csv').decode())))
 maps=[r for r in raw if int(float(r['MEB']))==53 and r['Category']=='NEW']
 assert len(maps)==20
 assert {(float(r['TempK']),int(r['RunMode'])) for r in maps}=={(t,m) for t in TEMPS for m in MODES}
 refmaps=[r for r in csv.DictReader(io.StringIO(ref.read('NODE_MAPPING.csv').decode())) if int(float(r['MEB']))==54 and r['Category']=='NEW']
 devref={}
 for m in MODES:
  rr=next(r for r in refmaps if int(r['RunMode'])==m)
  devref[m]=norm_dev(ref.read(f"{rr['Project']}/pp{rr['Node']}_des.cmd").decode())
 rr=refmaps[0];sderef=norm_sde(ref.read(f"{rr['Project']}/pp{rr['GridNode']}_dvs.cmd").decode())
 trees={}
 for proj in set(r['Project'] for r in maps):
  t=z.read(proj+'/gtree.dat').decode()
  trees[proj]={int(n):(int(level),int(par),v.strip()) for level,n,par,v in re.findall(r'^(\d+)\s+(\d+)\s+(\d+)\s+\{([^}]*)\}',t,re.M)}
 candidates=list(csv.DictReader(io.StringIO(z.read('CANDIDATES.csv').decode())))
 records=[];good={};dc=[];ivsn=[];metrics=[]
 for row in maps:
  m=int(row['RunMode']);t=float(row['TempK']);p=row['Project'];n=row['Node'];g=row['GridNode']
  pre=p+'/';dev=pre+f'pp{n}_des.cmd';sde=pre+f'pp{g}_dvs.cmd';sta=pre+f'n{n}_des.sta';log=pre+f'n{n}_des.log'
  plt=pre+(f'IVSN_0P8_TO_1P0_n{n}_ivsn_sys.plt' if m==7 else f'n{n}_des.plt')
  assert all(s in names for s in [dev,sde,sta,log,plt]),(p,n,'source missing')
  levels=trees[p];l4,pr,mode=levels[int(n)];l3,gr,tp=levels[pr];l2,dp,gv=levels[gr];l1,_,dv=levels[dp]
  assert (l4,l3,l2,l1)==(4,3,2,1) and mode==str(m) and float(tp)==t and int(float(dv))==53 and str(dp)==g,(n,'gtree')
  text=z.read(dev).decode();sd=z.read(sde).decode()
  gm=re.search(r'Grid\s*=\s*"n(\d+)_msh\.tdr"',text)
  tm=re.search(r'\bTemperature\s*=\s*([\d.]+)',text)
  dm=re.search(r'\(define\s+DBCAT_nm\s+([\d.]+)\)',sd)
  assert gm and gm[1]==g and tm and abs(float(tm[1])-t)<1e-6 and dm and float(dm[1])==53
  assert norm_sde(sd)==sderef,(p,n,'SDE model mismatch')
  assert norm_dev(text)==devref[m],(p,n,'Device model mismatch')
  hurkx='Recombination(Band2Band(Hurkx))' in '\n'.join(x for x in text.splitlines() if not x.lstrip().startswith('*'))
  assert hurkx==(m!=6)
  status=z.read(sta).decode();logger=z.read(log).decode(errors='replace')
  done='|done|' in status and 'Sentaurus Device simulation finished' in logger and 'Good Bye' in logger
  data=readplt(z,plt)
  finite=all(np.isfinite(x).all() for x in data.values())
  if m==7:
   end=float(data['v(sn)'][-1]);drain=None
   ep=abs(end-1.0)<1e-6
   ivok=(len(data['v(sn)'])==101 and np.allclose(data['v(sn)'],np.linspace(.8,1.,101),atol=1e-9,rtol=0) and
         np.allclose(data['v(bl)'],0) and np.allclose(data['v(wl)'],-.7) and np.all(data['i(cell,sn)']<0) and np.all(data['i(vsn,sn)']>0))
  else:
   end=float(data['gate OuterVoltage'][-1]);drain=float(data['drain OuterVoltage'][-1]);ivok=True
   ep=abs(end-({0:1.5,1:2.,5:-.7,6:-.7}[m]))<1e-6 and abs(drain-(.05 if m==0 else 1.2))<1e-6
  valid=bool(done and ep and ivok and finite)
  diag=[s for s in logger.splitlines() if 'converg' in s.lower() or 'minstep' in s.lower() or 'step-size less' in s.lower()]
  rec=dict(MEB_nm=53,Temp_K=t,RunMode=m,account='MAIN',project=p,node=n,grid=g,archive=a.source.name,
           status='PASS' if valid else 'RERUN',sta_done='|done|' in status,log_finished=('Good Bye' in logger and 'Sentaurus Device simulation finished' in logger),
           points=len(next(iter(data.values()))),endpoint_V=end,drain_endpoint_V=drain,expected_endpoint_V=(1 if m==7 else {0:1.5,1:2,5:-.7,6:-.7}[m]),
           endpoint_ok=bool(ep),iv_ok=bool(ivok),finite=bool(finite),SDE_template_verified=True,SDevice_template_verified=True,
           solver_warning=' | '.join(diag[-3:]) if not valid else '',plt_sha256=SHA(z.read(plt)),device_sha256=SHA(z.read(dev)),sde_sha256=SHA(z.read(sde)))
  records.append(rec)
  if valid:good[(53,t,m)]=(data,rec)
  else: print('INCOMPLETE',t,m,p,n,'last VG/VSN',end,'last VD',drain,'points',rec['points'],'log',rec['solver_warning'][-200:])
 for t in TEMPS:
  rr={m:good.get((53,t,m)) for m in MODES}
  row={'MEB_nm':53,'Temp_K':t,'valid_modes':sum(x is not None for x in rr.values()),'scope':'NEW'}
  for m,entry in rr.items():
   if entry is None:continue
   vals,rec=entry
   if m==7:
    v=vals['v(sn)'];i=vals['i(cell,sn)'];ivs=vals['i(vsn,sn)']
    fun=np.trapezoid if hasattr(np,'trapezoid') else np.trapz
    est=float(fun(1e-14/-i,v));kcl_abs=float(np.max(abs(i+ivs)));kcl_rel=float(np.max(abs(i+ivs)/abs(i)))
    row.update(t_est_s=est,Ieq_A=2e-15/est,IVSN_KCL_max_A=kcl_abs,IVSN_KCL_max_relative=kcl_rel,IVSN_QC='LOW_CURRENT_KCL_WARNING' if kcl_rel>.01 else 'PASS',retention_screen='PASS' if est>=(.032 if t==368.15 else .064) else 'FAIL')
    for j in range(len(v)):ivsn.append(dict(MEB_nm=53,Temp_K=t,project=rec['project'],node=rec['node'],**{k:float(x[j]) for k,x in vals.items()}))
   else:
    v,i=cv(vals,.05 if m==0 else 1.2)
    for j in range(len(v)):dc.append(dict(MEB_nm=53,Temp_K=t,RunMode=m,project=rec['project'],node=rec['node'],Vg_V=float(v[j]),Id_A=float(i[j])))
    if m==0:row['Vth_low_V']=vth(v,i,8.5e-8)
    elif m==1:
     row.update(Ion_A=logi(v,i,1.2),Ioff_A=logi(v,i,0),Vth_high_V=vth(v,i,8.5e-8))
     lo,hi=vth(v,i,1e-10),vth(v,i,1e-8)
     row['SS_mV_dec']=(hi-lo)*500 if lo is not None and hi is not None else None
    else:row[f'Id_Hurkx_{"ON" if m==5 else "OFF"}_A']=float(vals['drain TotalCurrent'][-1])
  if row.get('Vth_low_V') is not None and row.get('Vth_high_V') is not None:row['DIBL_mV_V']=(row['Vth_low_V']-row['Vth_high_V'])/1.15*1000
  if row.get('Id_Hurkx_ON_A') is not None and row.get('Id_Hurkx_OFF_A') is not None:row['Hurkx_excess_A']=row['Id_Hurkx_ON_A']-row['Id_Hurkx_OFF_A']
  metrics.append(row)
 write('MEB53_node_qc.csv',records);write('MEB53_six_metrics.csv',metrics);write('MEB53_DC_curves.csv',dc);write('MEB53_IVSN_curves.csv',ivsn)
 write('MEB53_selected_cases.csv',[dict(MEB_nm=53,Temp_K=r['Temp_K'],RunMode=r['RunMode'],account='MAIN',archive=a.source.name,project=r['project'],node=r['node'],grid=r['grid'],R1=False,data_sha256=r['plt_sha256']) for r in records if r['status']=='PASS'])
 write('MEB53_reruns.csv',[dict(Account='MAIN',MEB_nm=53,Temp_K=r['Temp_K'],RunMode=r['RunMode'],OriginalProject=r['project'],Node=r['node'],LastBias_V=r['endpoint_V'],RequestedBias_V=r['expected_endpoint_V'],Reason=r['solver_warning'] or 'Terminal bias not reached') for r in records if r['status']!='PASS'])
 info=dict(source_zip=a.source.name,source_sha256=SHA(a.source.read_bytes()),source_entries=len(names),source_integrity='PASS',selected_unique_conditions=len(maps),valid_count=len(good),incomplete_count=len(maps)-len(good),existing_recovery_candidates=len(raw)-len(maps),other_project_candidates=len(candidates),
           other_project_53_candidates=[dict(project=r['Project'],TempK=r['TempK'],RunMode=r['RunMode'],Selected=r['Selected'],PLT=r['PLT'],PLT_hash=r['PLT_hash']) for r in candidates if int(float(r['MEB']))==53],
           model_parent=a.reference.name,normalized_sde_sha256=SHA(sderef.encode()),normal_device_sha256={str(m):SHA(devref[m].encode()) for m in MODES},
           note='Source, PP and template equality verified; native binary mesh equality NOT verified. Incomplete traces excluded. Previous R1 recoveries are not re-counted.')
 (a.out/'source_manifest.json').write_text(json.dumps(info,indent=2,ensure_ascii=False),encoding='utf-8')
 assert len(good)==17 and {(r['Temp_K'],r['RunMode']) for r in records if r['status']=='RERUN'}=={(358.15,1),(358.15,5),(368.15,7)}
 print('FINAL MEB53',len(good),'/',len(maps),' DC ROWS',len(dc),'IVSN ROWS',len(ivsn))
 for r in metrics:print('METRIC',r)