#!/usr/bin/env python3
"""Static SWB PP sanity checks for exact 3 failed MEB53 recovery cases.
It is NOT a Sentaurus solver or terminal-curve validator.
"""
import re, sys
from pathlib import Path

TARGETS={(358.15,1),(358.15,5),(368.15,7)}
TREENODE=re.compile(r'^\s*(\d+)\s+(\d+)\s+(\d+)\s+\{([^}]*)\}',re.M)

def main():
    if len(sys.argv)!=2:
        print('Usage: python3 cmp_meb53_r1_preflight.py /path/to/copied/SWB_project')
        return 2
    project=Path(sys.argv[1]).expanduser()
    gt=project/'gtree.dat'
    if not gt.is_file():
        raise SystemExit('Missing gtree.dat in '+str(project))
    tree={int(node):(int(level),int(parent),value.strip()) for level,node,parent,value in TREENODE.findall(gt.read_text(errors='replace'))}
    found={}
    for node,(level,parent,value) in tree.items():
        if level!=4: continue
        try:
            mode=int(value); l3,tparent,ts=tree[parent];l2,gparent,_=tree[tparent];l1,_,depth=tree[gparent]
            t=float(ts);d=float(depth)
        except (KeyError,ValueError): continue
        if (l3,l2,l1)!=(3,2,1) or d!=53.0 or (t,mode) not in TARGETS: continue
        key=(t,mode)
        pp=project/('pp%d_des.cmd'%node)
        if not pp.exists(): raise AssertionError('Preprocess missing: '+str(pp))
        sde=project/('pp%d_dvs.cmd'%gparent)
        if not sde.exists():raise AssertionError('SDE source missing: '+str(sde))
        src=sde.read_text(errors='replace');deck=pp.read_text(errors='replace')
        assert re.search(r'\(define\s+DBCAT_nm\s+53(?:\.0+)?\)',src),('SDE depth',key,node)
        assert 'Grid="n%d_msh.tdr"'%gparent in re.sub(r'\s*=\s*','=',deck),('grid',key,node)
        assert re.search(r'\bTemperature\s*=\s*'+str(t)+r'\b',deck),('temperature',key,node)
        assert re.search(r'\bWorkfunction\s*=\s*4\.8\b',deck),('WF',key,node)
        assert 'Recombination(Band2Band(Hurkx))' in deck,('Hurkx',key,node)
        assert '@' not in '\n'.join(s for s in deck.splitlines() if not s.lstrip().startswith('*')),('unexpanded placeholder',key,node)
        if mode in (1,5):
            for token in ('InitialStep=1.0e-4','Increment=1.15','MinStep=1.0e-9','MaxStep=5.0e-3','Extrapolate(MinStep=1.0e-5)','Coupled(Iterations=80)','Goal { Name="drain" Voltage=1.2 }'):
                assert token in deck,(key,node,'missing numerical/bias token',token)
            if mode==1:
                assert 'Goal { Name="gate" Voltage=2.0 }' in deck
            else:
                assert 'Goal { Name="gate" Voltage=-0.7 }' in deck
        else:
            for token in ('InitialStep=2.5e-4','MinStep=1e-12','MaxStep=0.005','Extrapolate(MinStep=1e-6)','Goal { Parameter=vsn.dc Value=1.0 }','CurrentPlot(Time=(Range=(0 1) Intervals=100))','capacitance=1e-14','dc=-0.7'):
                assert token in deck,(key,node,'missing numerical/bias token',token)
        if key in found:raise AssertionError('Duplicate selected key '+str(key))
        found[key]=node
        print('PASS: MEB=53 TempK=%s Mode=%s SWB_device_node=%s grid=%s PP=%s'% (t,mode,node,gparent,pp.name))
    if set(found)!=TARGETS:
        raise AssertionError('Expected %s; found %s. Preprocess/selection not yet complete.'%(sorted(TARGETS),sorted(found)))
    print('ALL THREE PREPROCESS CHECKS PASS (NOT numerical convergence).')
    return 0
if __name__=='__main__': sys.exit(main())
