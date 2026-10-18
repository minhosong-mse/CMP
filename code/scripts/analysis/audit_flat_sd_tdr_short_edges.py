#!/usr/bin/env python3
"""Read-only native mesh HDF5 audit. Requires h5py/numpy. Sentaurus TDR HDF5 geometry only."""
import sys,h5py,numpy as np
if len(sys.argv)!=2: raise SystemExit('python3 audit_tdr_short_edges.py nXX_msh.tdr')
f=h5py.File(sys.argv[1]);g=f['collection/geometry_0'];v=g['vertex'][:];xyz=np.column_stack([v['x'],v['y'],v['z']]);pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3));unique={};nT=0
for key in g.keys():
 if not key.startswith('region_'):continue
 region=g[key]
 if int(region.attrs.get('type',-1)) != 0:continue
 for k in region.keys():
  if not k.startswith('elements_'):continue
  arr=region[k][:]
  if len(arr)%5:continue
  cells=arr.reshape(-1,5)
  if not np.all(cells[:,0]==5):continue
  t=cells[:,1:];nT+=len(t)
  for a,b in pairs:
   node=t[:,[a,b]]; ds=np.linalg.norm(xyz[node[:,0]]-xyz[node[:,1]],axis=1)*1000
   for q in np.flatnonzero(ds<0.1):
    pair=tuple(sorted(map(int,node[q])));unique[pair]=min(unique.get(pair,float('inf')),float(ds[q]))
print('vertex count:',len(xyz),'tetrahedra:',nT,'min edge nm:',min(unique.values(),default=float('nan')))
for limit in [0.001,0.005,0.01,0.05,0.1]:print('unique edges <',limit,'nm:',sum(v<limit for v in unique.values()))
