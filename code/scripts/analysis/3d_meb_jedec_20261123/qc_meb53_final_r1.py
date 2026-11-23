#!/usr/bin/env python3
"""Native MEB53 R1 final-3 scientific audit; checks PP SDE/Device, executed
3 targets, logs, voltage endpoints, and IVSN 101-point protocol.
No Sentaurus execution, no physical rerouting, no measured retention claim.
Original 37-depth GitHub data is not modified by this script.
"""
from __future__ import annotations
import csv, hashlib, io, json, re, zipfile, argparse
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser()
p.add_argument('--source',type=Path,default=Path('/mnt/data/CMP_MAIN_MEB53_R1_FINAL_NOV23_20261123_220510.zip'))
p.add_argument('--original-53',type=Path,default=Path('/mnt/data/CMP_MAIN_MEB53_NOV23_20261123_192708.zip'))
p.add_argument('--reference-r1',type=Path,default=Path('/mnt/data/CMP_OTHER_NOV23_20261123_173618.zip'))
p.add_argument('--out',type=Path,default=Path('/mnt/data/CMP_MEB53_FINAL_R1_QC'))
a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
TARGET={(53,358.15,1),(53,358.15,5),(53,368.15,7)}
SHA=lambda b:hashlib.sha256(b).hexdigest()
def ns(s):
 s='\n'.join(x for x in s.splitlines() if not x.lstrip().startswith(';'))
 s=re.sub(r'\(define\s+DBCAT_nm\s+[\d.]+\)','(define DBCAT_nm X)',s)
 s=re.sub(r'("n)\d+("\)',r'\1X\2',s) if False else re.sub(r'("n)\d+(")',r'\1X\2',s)
 return re.sub(r'\s+','',s)
def nd(s):
 s='\n'.join(x for x in s.splitlines() if not x.lstrip().startswith('*'))
 s=re.sub(r'\bTemperature\s*=\s*[\d.]+','Temperature=X',s)
 s=re.sub(r'n\d+_','nX_',s)
 return re.sub(r'\s+','',s)
def readplt(z,filename):
 raw=z.read(filename).decode(errors='replace');ds=raw.split('datasets',1)[1].split('functions',1)[0]
 fields=re.findall(r'"([^"]+)"',ds);dat=re.search(r'Data\s*\{(.*?)\}',raw,re.S)
 assert fields and dat,filename
 arr=np.fromstring(dat.group(1),sep=' ')
 assert len(arr)%len(fields)==0,(filename,len(arr),len(fields))
 return dict(zip(fields,arr.reshape(-1,len(fields)).T))
def curve(x,vd):
 keep=np.isclose(x['drain OuterVoltage'],vd,rtol=0,atol=1e-9)
 v=x['gate OuterVoltage'][keep];i=x['drain TotalCurrent'][keep]
 idx=np.argsort(v,kind='stable');v=v[idx];i=i[idx]
 unique=np.r_[np.diff(v)>1e-12,True]
 return v[unique],i[unique]
def logi(v,i,g):
 if len(v)<2 or not(v[0]<=g<=v[-1]):return None
 k=np.where(np.isclose(v,g,atol=1e-12,rtol=0))[0]
 if len(k):return float(i[k[-1]])
 j=np.searchsorted(v,g)
 return float(10**np.interp(g,v[j-1:j+1],np.log10(i[j-1:j+1]))) if np.min(i[j-1:j+1])>0 else float(np.interp(g,v,i))
def vth(v,i,target):
 k=np.where((i[:-1]<target)&(i[1:]>=target)&(i[:-1]>0))[0]
 if len(k)!=1:return None
 j=k[0];return float(np.interp(np.log10(target),np.log10(i[j:j+2]),v[j:j+2]))
def write(fn,rows):
 hdr=list(dict.fromkeys(k for row in rows for k in row))
 with (a.out/fn).open('w',newline='',encoding='utf8') as f:
  w=csv.DictWriter(f,fieldnames=hdr);w.writeheader();w.writerows(rows)
with zipfile.ZipFile(a.source) as z,zipfile.ZipFile(a.original_53) as old,zipfile.ZipFile(a.reference_r1) as ref:
 assert z.testzip() is None
 nslist=set(z.namelist());source=list(csv.DictReader(io.StringIO(z.read('NODE_MAPPING.csv').decode())))
 chosen=[r for r in source if (int(r['MEB']),float(r['TempK']),int(r['RunMode'])) in TARGET]
 assert len(chosen)==3 and set((int(r['MEB']),float(r['TempK']),int(r['RunMode'])) for r in chosen)==TARGET
 assert all(r['Project']=='CMP_eeeeeeee_53' and r['Category']=='NEW' for r in chosen)
 assert {(float(r['TempK']),int(r['RunMode']),r['Node'],r['GridNode']) for r in chosen}=={(358.15,1,'39','128'),(358.15,5,'40','128'),(368.15,7,'47','128')}
 cand=list(csv.DictReader(io.StringIO(z.read('CANDIDATES.csv').decode())))
 oldmap=list(csv.DictReader(io.StringIO(old.read('NODE_MAPPING.csv').decode())))
 refmap=list(csv.DictReader(io.StringIO(ref.read('NODE_MAPPING.csv').decode())))
 old53=next(r for r in oldmap if int(r['MEB'])==53 and r['Category']=='NEW' and int(r['RunMode'])==0)
 sderef=ns(old.read(f"{old53['Project']}/pp{old53['GridNode']}_dvs.cmd").decode())
 tree={int(n):(int(l),int(p),v.strip()) for l,n,p,v in re.findall(r'^(\d+)\s+(\d+)\s+(\d+)\s+\{([^}]*)\}',z.read('CMP_eeeeeeee_53/gtree.dat').decode(),re.M)}
 rawrows=[];sel=[];dc=[];iv=[];metrics=[];xdata={};proven=[]
 for row in chosen:
  d=int(row['MEB']);t=float(row['TempK']);m=int(row['RunMode']);n=row['Node'];g=row['GridNode'];proj=row['Project'];base=proj+'/'
  lev,p_,mode=tree[int(n)];l3,pr,tv=tree[p_];l2,pg,_=tree[pr];l1,_,depth=tree[pg]
  assert (lev,l3,l2,l1)==(4,3,2,1) and int(mode)==m and float(tv)==t and float(depth)==d and str(pg)==g
  paths={k:base+v for k,v in {
   'sde':f'pp{g}_dvs.cmd','cmd':f'pp{n}_des.cmd','sta':f'n{n}_des.sta','log':f'n{n}_des.log',
   'plt':f'IVSN_0P8_TO_1P0_n{n}_ivsn_sys.plt' if m==7 else f'n{n}_des.plt'}.items()}
  assert all(v in nslist for v in paths.values()),(m,paths)
  sd=z.read(paths['sde']).decode();cmd=z.read(paths['cmd']).decode();sta=z.read(paths['sta']).decode();log=z.read(paths['log']).decode(errors='replace')
  assert ns(sd)==sderef,('SDE changed',m)
  assert re.search(r'\(define DBCAT_nm\s+53\)',sd) and re.search(r'Grid\s*=\s*"n'+g+r'_msh.tdr"',cmd)
  assert any(abs(float(k)-t)<1e-8 for k in re.findall(r'Temperature\s*=\s*([\d.]+)',cmd)),m
  assert ('Recombination(Band2Band(Hurkx))' in '\n'.join(s for s in cmd.splitlines() if not s.lstrip().startswith('*')))==(m!=6)
  assert re.search(r'Workfunction\s*=\s*4\.8\b',cmd)
  r1=next(r for r in refmap if r['Project']=='CMP_eeeeeeee' and int(r['RunMode'])==m)
  devref=ref.read(f"{r1['Project']}/pp{r1['Node']}_des.cmd").decode()
  assert nd(cmd)==nd(devref),('R1 template changed',m)
  original=next(r for r in oldmap if int(r['MEB'])==53 and float(r['TempK'])==t and int(r['RunMode'])==m and r['Category']=='NEW')
  assert nd(cmd)!=nd(old.read(f"{original['Project']}/pp{original['Node']}_des.cmd").decode()),('Not R1',m)
  done='|done|' in sta and 'Sentaurus Device simulation finished' in log and 'Good Bye' in log
  xx=readplt(z,paths['plt']);finite=all(np.isfinite(v).all() for v in xx.values())
  ep=float(xx['v(sn)'][-1]) if m==7 else float(xx['gate OuterVoltage'][-1])
  vd=None if m==7 else float(xx['drain OuterVoltage'][-1]);expect={1:2.,5:-.7,7:1.}[m]
  epok=abs(ep-expect)<1e-6 and (m==7 or abs(vd-1.2)<1e-6)
  if m==7:
   v=xx['v(sn)'];ivok=len(v)==101 and np.allclose(v,np.linspace(.8,1.,101),rtol=0,atol=1e-9)
   ivok=ivok and np.allclose(xx['v(bl)'],0) and np.allclose(xx['v(wl'] if 'v(wl' in xx else xx['v(wl)'],-.7)
   ivok=ivok and np.all(xx['i(cell,sn)']<0) and np.all(xx['i(vsn,sn)']>0)
   epok=epok and ivok
  assert done and finite and epok,(t,m,done,finite,epok,ep,vd)
  assert any(c['Project']==proj and c['Node']==n and c['Selected']=='1' and c['PLT']=='1' and c['STA_done']=='1' and c['Log_finished']=='1' for c in cand)
  qc=dict(MEB_nm=d,Temp_K=t,RunMode=m,valid_candidates=1,status='PASS',archive=a.source.name,project=proj,node=n,grid=g,points=len(next(iter(xx.values()))),endpoint_V=ep,reason='R1_NUMERICAL_ONLY')
  rawrows.append(qc);sel.append(dict(MEB_nm=d,Temp_K=t,RunMode=m,account='MAIN',archive=a.source.name,project=proj,node=n,grid=g,R1=True,data_sha256=SHA(z.read(paths['plt']))))
  proven.append(dict(MEB_nm=d,Temp_K=t,RunMode=m,project=proj,node=n,grid=g,sta_done=True,log_finished=True,final_endpoint_V=ep,drain_endpoint_V=vd,points=len(next(iter(xx.values()))),SDE_PP_hash=SHA(z.read(paths['sde'])),Device_PP_hash=SHA(z.read(paths['cmd'])),PLT_hash=SHA(z.read(paths['plt'])),R1_source_normalized_sha256=SHA(nd(cmd).encode())))
  xdata[m,t]=xx
  if m==7:
   for j in range(len(xx['v(sn)'])):iv.append(dict(MEB_nm=d,Temp_K=t,RunMode=m,project=proj,node=n,**{k:float(v[j]) for k,v in xx.items()}))
  else:
   v,i=curve(xx,1.2)
   for j in range(len(v)):dc.append(dict(MEB_nm=d,Temp_K=t,RunMode=m,project=proj,node=n,Vg_V=float(v[j]),Id_A=float(i[j])))
 for t in (358.15,368.15):
  row=dict(MEB_nm=53,Temp_K=t,valid_modes=sum((m,t) in xdata for m in (1,5,7)))
  if (1,t) in xdata:
   xx=xdata[1,t];v,i=curve(xx,1.2);lo,hi=vth(v,i,1e-10),vth(v,i,1e-8)
   row.update(Ion_A=logi(v,i,1.2),Ioff_A=logi(v,i,0),Vth_high_V=vth(v,i,8.5e-8),SS_mV_dec=(hi-lo)*500 if lo is not None and hi is not None else None)
  if (5,t) in xdata: row['Id_Hurkx_ON_A']=float(xdata[5,t]['drain TotalCurrent'][-1])
  if (7,t) in xdata:
   xx=xdata[7,t];v=xx['v(sn)'];i=xx['i(cell,sn)'];vs=xx['i(vsn,sn)']
   tm=float(np.trapezoid(1e-14/-i,v));kcl=float(np.max(abs(i+vs)/abs(i)))
   row.update(t_est_s=tm,Ieq_A=2e-15/tm,IVSN_KCL_max_A=float(np.max(abs(i+vs))),IVSN_KCL_max_relative=kcl,IVSN_QC='LOW_CURRENT_KCL_WARNING' if kcl>.01 else 'PASS',retention_screen='PASS' if tm>=(.032 if t==368.15 else .064) else 'FAIL')
  metrics.append(row)
 write('MEB53_R1_node_qc_3.csv',rawrows);write('MEB53_R1_selected_sources_3.csv',sel)
 write('MEB53_R1_metric_patches_2.csv',metrics)
 write('MEB53_R1_dc_curves.csv',dc);write('MEB53_R1_ivsn_curves.csv',iv)
 write('MEB53_R1_native_provenance_3.csv',proven)
 manifest={'archive':a.source.name,'archive_sha256':SHA(a.source.read_bytes()),'archive_bytes':a.source.stat().st_size,'archive_entries':len(z.namelist()),'native_zip_integrity':'PASS','mapped_entries':len(source),'R1_verified_node_keys':sorted(tuple(k) for k in TARGET),'R1_selected_nodes':{str((r['Temp_K'],r['RunMode'])):r['node'] for r in rawrows},'n_dc_points':len(dc),'n_ivsn_points':len(iv),'SDE_source_template_match':True,'R1_PP_device_template_match':True,'old_53_original_failed_preserved_external':True,'full_native_mesh_tensor_equivalence':'NOT VERIFIED','user_note':'Only three new R1 endpoints accepted; do not reuse old CMP_final_Copy none statuses for unrelated 17 source-mapped accepted MEB53 nodes.'}
 (a.out/'source_manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False))
 assert len(rawrows)==3 and len(metrics)==2 and len(iv)==101
 print('PASS 3/3 MEB53 isolated R1 endpoints. DC points',len(dc),'IVSN points',len(iv));print('archive SHA256',manifest['archive_sha256'])
 for row in rawrows:print('QC',row)
 for row in metrics:print('METRIC_PATCH',row)
