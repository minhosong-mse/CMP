#!/usr/bin/env python3
"""Selective native SWB audit/extraction for 2026-11-23 MEB35+5 recovery ZIP.
Assumes 53nm R1 results NOT present. Requires numpy and external native SWB
ZIPs: current MEB35/R1, previously executed 54nm and old 11 R1 reference.
No Sentaurus execution, no physical parameter changes.
"""
import csv, hashlib, io, re, zipfile, argparse
from pathlib import Path
import numpy as np

P=argparse.ArgumentParser()
P.add_argument('--source',type=Path,default=Path('/mnt/data/CMP_MAIN_MEB35_R1_RECOVERY_NOV23_20261123_213740.zip'))
P.add_argument('--reference-54',type=Path,default=Path('/mnt/data/CMP_MAIN_MEB54_NOV23_20261123_175736.zip'))
P.add_argument('--reference-r1',type=Path,default=Path('/mnt/data/CMP_OTHER_NOV23_20261123_173618.zip'))
P.add_argument('--out',type=Path,default=Path('/mnt/data/CMP_NOV23_MEB35_5R1_QC'))
a=P.parse_args();a.out.mkdir(exist_ok=True,parents=True)
T=(233.15,300.,358.15,368.15);M=(0,1,5,6,7)
R={(27,358.15,1),(40,358.15,1),(46,358.15,1),(47,368.15,5),(58,358.15,7)}
TARGET={(35,t,m) for t in T for m in M}|R

def write(name,rows):
 cols=list(dict.fromkeys(k for r in rows for k in r))
 with (a.out/name).open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)

def norm_sde(s):
 s='\n'.join(v for v in s.splitlines() if not v.lstrip().startswith(';'))
 s=re.sub(r'\(define\s+DBCAT_nm\s+[\d.]+\)','(define DBCAT_nm X)',s)
 s=re.sub(r'("n)\d+(")',r'\1X\2',s)
 return re.sub(r'\s+','',s)

def norm_dev(s):
 s='\n'.join(v for v in s.splitlines() if not v.lstrip().startswith('*'))
 s=re.sub(r'\bTemperature\s*=\s*[\d.]+','Temperature=X',s)
 s=re.sub(r'n\d+_', 'nX_',s)
 return re.sub(r'\s+','',s)

def plt(z,n):
 s=z.read(n).decode(errors='replace')
 fields=re.findall(r'"([^"]+)"',s.split('datasets',1)[1].split('functions',1)[0])
 dat=np.fromstring(re.search(r'Data\s*\{(.*?)\}',s,re.S).group(1),sep=' ')
 assert len(fields)>0 and len(dat)%len(fields)==0,(n,len(dat),len(fields))
 return dict(zip(fields,dat.reshape(-1,len(fields)).T))

def curve(x,vd):
 sel=np.isclose(x['drain OuterVoltage'],vd,atol=1e-9,rtol=0)
 v=x['gate OuterVoltage'][sel];i=x['drain TotalCurrent'][sel]
 ix=np.argsort(v,kind='stable');v=v[ix];i=i[ix]
 keep=np.r_[np.diff(v)>1e-12,True]
 return v[keep],i[keep]

def logi(v,i,g):
 if len(v)<2 or not(v[0]<=g<=v[-1]):return None
 ix=np.where(np.isclose(v,g,atol=1e-12,rtol=0))[0]
 if len(ix):return float(i[ix[-1]])
 j=np.searchsorted(v,g)
 if min(i[j-1:j+1])>0:
  return float(10**np.interp(g,v[j-1:j+1],np.log10(i[j-1:j+1])))
 return float(np.interp(g,v,i))

def vth(v,i,target):
 ix=np.where((i[:-1]<target)&(i[1:]>=target)&(i[:-1]>0))[0]
 if len(ix)!=1:return None
 j=ix[0]
 return float(np.interp(np.log10(target),np.log10(i[j:j+2]),v[j:j+2]))

with zipfile.ZipFile(a.source) as z,zipfile.ZipFile(a.reference_54) as zr,zipfile.ZipFile(a.reference_r1) as zo:
 assert z.testzip() is None
 names=set(z.namelist())
 rows=list(csv.DictReader(io.StringIO(z.read('NODE_MAPPING.csv').decode())))
 target_rows=[r for r in rows if (int(r['MEB']),float(r['TempK']),int(r['RunMode'])) in TARGET]
 assert len(target_rows)==25 and len(set((int(r['MEB']),float(r['TempK']),int(r['RunMode'])) for r in target_rows))==25
 cand=list(csv.DictReader(io.StringIO(z.read('CANDIDATES.csv').decode())))
 refrows=list(csv.DictReader(io.StringIO(zr.read('NODE_MAPPING.csv').decode())))
 oldrows=list(csv.DictReader(io.StringIO(zo.read('NODE_MAPPING.csv').decode())))
 ref54={m:next(r for r in refrows if int(r['MEB'])==54 and int(r['RunMode'])==m and r['Category']=='NEW') for m in M}
 oldr1={m:next(r for r in oldrows if int(r['RunMode'])==m and r['Project']=='CMP_eeeeeeee' and r['Category']=='RECOVERY') for m in (1,5,7)}
 sderef=norm_sde(zr.read(f"{ref54[0]['Project']}/pp{ref54[0]['GridNode']}_dvs.cmd").decode())
 trees={}
 for project in set(r['Project'] for r in target_rows):
  t=z.read(project+'/gtree.dat').decode()
  trees[project]={int(node):(int(level),int(parent),value.strip()) for level,node,parent,value in re.findall(r'^(\d+)\s+(\d+)\s+(\d+)\s+\{([^}]*)\}',t,re.M)}
 selected={};qc=[];selectedrows=[];dc=[];iv=[]
 for r in target_rows:
  d=int(r['MEB']);t=float(r['TempK']);m=int(r['RunMode']);key=(d,t,m)
  project=r['Project'];node=r['Node'];grid=r['GridNode'];prefix=project+'/'
  tree=trees[project];l4,p4,mv=tree[int(node)];l3,p3,tv=tree[p4];l2,p2,_=tree[p3];l1,_,dv=tree[p2]
  assert (l4,l3,l2,l1)==(4,3,2,1) and int(mv)==m and float(tv)==t and float(dv)==d and str(p2)==grid,(key,'tree')
  sd=prefix+f'pp{grid}_dvs.cmd'; dev=prefix+f'pp{node}_des.cmd';sta=prefix+f'n{node}_des.sta';log=prefix+f'n{node}_des.log'
  fn=prefix+(f'IVSN_0P8_TO_1P0_n{node}_ivsn_sys.plt' if m==7 else f'n{node}_des.plt')
  assert all(v in names for v in (sd,dev,sta,log,fn)),(key,'missing raw evidence')
  sde=z.read(sd).decode();deck=z.read(dev).decode()
  assert re.search(r'\(define\s+DBCAT_nm\s+'+str(d)+r'\)',sde)
  assert norm_sde(sde)==sderef,(key,'SDE reference mismatch')
  assert re.search(r'Grid\s*=\s*"n'+grid+r'_msh.tdr"',deck)
  assert any(abs(float(v)-t)<1e-6 for v in re.findall(r'\bTemperature\s*=\s*([\d.]+)',deck))
  assert ('Recombination(Band2Band(Hurkx))' in '\n'.join(l for l in deck.splitlines() if not l.lstrip().startswith('*')))==(m!=6)
  rr=ref54[m] if d==35 else oldr1[m]
  rrzip=zr if d==35 else zo
  assert norm_dev(deck)==norm_dev(rrzip.read(f"{rr['Project']}/pp{rr['Node']}_des.cmd").decode()),(key,'source template mismatch')
  sta_txt=z.read(sta).decode(errors='replace');log_txt=z.read(log).decode(errors='replace')
  done='|done|' in sta_txt and 'Sentaurus Device simulation finished' in log_txt and 'Good Bye' in log_txt
  x=plt(z,fn);finite=all(np.isfinite(a).all() for a in x.values())
  end=float(x['v(sn)'][-1]) if m==7 else float(x['gate OuterVoltage'][-1])
  vdr=None if m==7 else float(x['drain OuterVoltage'][-1])
  endok=abs(end-{0:1.5,1:2,5:-.7,6:-.7,7:1}[m])<1e-6 and (m==7 or abs(vdr-(.05 if m==0 else 1.2))<1e-6)
  if m==7:
   v=x['v(sn)']
   endok=endok and len(v)==101 and np.allclose(v,np.linspace(.8,1.,101),rtol=0,atol=1e-9)
   endok=endok and np.allclose(x['v(bl)'],0) and np.allclose(x['v(wl)'],-.7)
   endok=endok and np.all(x['i(cell,sn)']<0) and np.all(x['i(vsn,sn)']>0)
  assert done and finite and endok,(key,'not actually complete',done,finite,endok,end,vdr)
  assert any(c['Project']==project and c['Node']==node and c['Selected']=='1' for c in cand),(key,'candidate mismatch')
  n_samples=len(next(iter(x.values())))
  selected[key]=x
  qc.append(dict(MEB_nm=d,Temp_K=t,RunMode=m,valid_candidates=sum(c['MEB']==str(d) and float(c['TempK'])==t and int(c['RunMode'])==m and c['STA_done']=='1' and c['Log_finished']=='1' for c in cand),status='PASS',archive=a.source.name,project=project,node=node,grid=grid,points=n_samples,endpoint_V=end,reason='R1_NUMERICAL_ONLY' if d!=35 else ''))
  selectedrows.append(dict(MEB_nm=d,Temp_K=t,RunMode=m,account='MAIN',archive=a.source.name,project=project,node=node,grid=grid,R1=(d!=35),data_sha256=hashlib.sha256(z.read(fn)).hexdigest()))
  if m==7:
   for j in range(n_samples):iv.append(dict(MEB_nm=d,Temp_K=t,RunMode=m,project=project,node=node,**{k:float(v[j]) for k,v in x.items()}))
  else:
   vg,ii=curve(x,.05 if m==0 else 1.2)
   for j in range(len(vg)):dc.append(dict(MEB_nm=d,Temp_K=t,RunMode=m,project=project,node=node,Vg_V=float(vg[j]),Id_A=float(ii[j])))
 metric=[]
 for d,t in sorted(set((k[0],k[1]) for k in selected)):
  rows={m:selected.get((d,t,m)) for m in M};row=dict(MEB_nm=d,Temp_K=t,valid_modes=sum(x is not None for x in rows.values()))
  for m,x in rows.items():
   if x is None:continue
   if m==7:
    v=x['v(sn)'];i=x['i(cell,sn)'];vs=x['i(vsn,sn)'];dt=float(np.trapezoid(1e-14/-i,v))
    rel=float(np.max(abs(i+vs)/abs(i)))
    row.update(t_est_s=dt,Ieq_A=2e-15/dt,IVSN_KCL_max_A=float(np.max(abs(i+vs))),IVSN_KCL_max_relative=rel,IVSN_QC='LOW_CURRENT_KCL_WARNING' if rel>.01 else 'PASS',retention_screen='PASS' if dt>=(.032 if t==368.15 else .064) else 'FAIL')
   else:
    v,i=curve(x,.05 if m==0 else 1.2)
    if m==0:row['Vth_low_V']=vth(v,i,8.5e-8)
    elif m==1:
     lo,hi=vth(v,i,1e-10),vth(v,i,1e-8)
     row.update(Ion_A=logi(v,i,1.2),Ioff_A=logi(v,i,0),Vth_high_V=vth(v,i,8.5e-8),SS_mV_dec=(hi-lo)*500 if lo is not None and hi is not None else None)
    else:row['Id_Hurkx_'+('ON' if m==5 else 'OFF')+'_A']=float(x['drain TotalCurrent'][-1])
  if row.get('Vth_low_V') is not None and row.get('Vth_high_V') is not None:row['DIBL_mV_V']=(row['Vth_low_V']-row['Vth_high_V'])/1.15*1000
  if row.get('Id_Hurkx_ON_A') is not None and row.get('Id_Hurkx_OFF_A') is not None:row['Hurkx_excess_A']=row['Id_Hurkx_ON_A']-row['Id_Hurkx_OFF_A']
  metric.append(row)
 write('new_qc_25.csv',qc);write('new_selected_25.csv',selectedrows);write('new_metrics_9rows.csv',metric)
 write('new_dc_curves_2607.csv',dc);write('new_ivsn_curves_505.csv',iv)
 assert len(qc)==25 and len(metric)==9 and len(dc)==2607 and len(iv)==505
 print('PASS 25/25; MEB35 20/20; five R1 5/5; DC',len(dc),'IVSN',len(iv),'rows')
 print('MEB35 metrics:')
 for r in metric:
  if r['MEB_nm']==35:print(' Temp',r['Temp_K'],'Ion(uA)',r['Ion_A']*1e6,'SS',r['SS_mV_dec'],'DIBL',r['DIBL_mV_V'],'t_est(s)',r['t_est_s'],'KCL rel',r['IVSN_KCL_max_relative'])
