#!/usr/bin/env python3
"""CMP independent 3D 5-MEB x 4-temperature x 7-mode (140 cases) extractor.

Resumable incomplete-native-curve recovery; derived from the already-executed 2026-11-06 standalone 49–60 nm extraction tool.
Strict SDE/PP provenance, no node numbering assumptions, resumable, archival ZIP; no GitHub checkout.

No SDevice runs. SWB input is read-only. Does not push to GitHub.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import importlib.util
import json
import math
import re
import shutil
import subprocess
import sys
import zipfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DEPTHS = (36, 41, 48, 54, 60)
TEMPS = (233, 300, 340, 380)
MODES = range(7)
Q = 1.602176634e-19
ROIS = ('GATE_DRAIN','MID_DRAIN','OUTER_DRAIN','FULL_SILICON')
METRIC_FIELDS = [
    'DBCAT_nm','Vth_high_proxy_V','SS_high_quick_proxy_mVdec','DIBL_proxy_V_per_V',
    'Id_Vg1p2_Vd1p2_A','GIDL_ON_Id_Vgneg0p7_A','GIDL_OFF_Id_Vgneg0p7_A',
    'Hurkx_ON_minus_OFF_A','Emax_GATE_DRAIN_MV_per_cm','qGpositive_GATE_DRAIN_A',
    'Emax_OUTER_DRAIN_MV_per_cm','qGpositive_OUTER_DRAIN_A',
    'Emax_FULL_SILICON_MV_per_cm','qGpositive_FULL_SILICON_A',
    'source_status','source_campaign','SDevice_case_nodes','QC_notes']
PAT_SDE = re.compile(r'pp(\d+)_dvs\.cmd$')
PAT_DEV = re.compile(r'pp(\d+)_des\.cmd$')
PAT_DEPTH = re.compile(r'\(define\s+DBCAT_nm\s+([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*\)')
PAT_GRID = re.compile(r'\bGrid\s*=\s*["\']?n(\d+)_msh\.tdr',re.I)
PAT_PLOT = re.compile(r'\bPlot\s*=\s*["\'](n\d+_des\.tdr)["\']',re.I)
PAT_CURRENT = re.compile(r'\bCurrent\s*=\s*["\'](n\d+_des\.plt)["\']',re.I)
PAT_GOAL = re.compile(r'Goal\s*\{\s*Name\s*=\s*["\'](gate|drain)["\']\s*Voltage\s*=\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*\}',re.I)
PAT_TEMP = re.compile(r'\bTemperature\s*=\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?)', re.I)
PAT_HURKX = re.compile(r'\bBand2Band\s*\(\s*(?:Model\s*=\s*)?Hurkx\s*\)',re.I)


def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def readcsv(p):
    with p.open('r',encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))

def writecsv(p,rows,columns=None):
    p.parent.mkdir(parents=True,exist_ok=True)
    columns = columns or list(rows[0])
    with p.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,columns,extrasaction='ignore')
        w.writeheader();w.writerows(rows)

def q(s):
    return '{'+str(s).replace('\\','/').replace('}','\\}')+'}'

def not_comments(s):
    return '\n'.join(x for x in s.splitlines() if not x.lstrip().startswith(('*','#','//',';')))

def near(v,t,eps=1e-4):
    return abs(v-t)<=eps

def identify_mode(s):
    g=[(x.lower(),float(v)) for x,v in PAT_GOAL.findall(s)]
    has=bool(PAT_HURKX.search(s))
    if len(g)!=2: return None,'Expected exactly 2 Goal statements, got '+str(g)
    if g[0][0]=='drain' and g[1][0]=='gate':
        if near(g[0][1],.05) and near(g[1][1],1.5):return 0,''
        if near(g[0][1],1.2) and near(g[1][1],2.0):return 1,''
        if near(g[0][1],1.2) and near(g[1][1],-.7):return (5 if has else 6),''
    if g[0][0]=='gate' and g[1][0]=='drain' and near(g[1][1],1.2):
        for m,vg in [(2,.1),(3,.6),(4,1.2)]:
            if near(g[0][1],vg):return m,''
    return None,'Unrecognized Goal sequence '+str(g)

def unique_native_files(project):
    """Index native filenames once; duplicate same names are flagged, never chosen arbitrarily."""
    tdrs=defaultdict(list);plts=defaultdict(list)
    for p in project.rglob('*'):
        if not p.is_file() or p.is_symlink():continue
        if re.fullmatch(r'n\d+_des\.tdr',p.name):tdrs[p.name].append(p)
        elif re.fullmatch(r'n\d+_des\.plt',p.name):plts[p.name].append(p)
    return tdrs,plts



def discover(project):
    """Prove each (MEB, T, mode) from executed PP SDE+SDevice files, not SWB node arithmetic."""
    sde={}; errors=[]
    for p in sorted(project.rglob('pp*_dvs.cmd')):
        mat=PAT_SDE.fullmatch(p.name)
        if not mat or not p.is_file() or p.is_symlink():continue
        text=not_comments(p.read_text(encoding='utf-8',errors='replace'))
        m=PAT_DEPTH.search(text)
        if not m:continue
        d=float(m.group(1));n=int(mat.group(1))
        if not d.is_integer():errors.append('Noninteger DBCAT_nm: '+str(p));continue
        if n in sde:errors.append('Duplicate SDE node '+str(n));continue
        sde[n]={'depth':int(d),'path':p,'sha':sha(p)}
    tdrs,plts=unique_native_files(project)
    records=[]
    for p in sorted(project.rglob('pp*_des.cmd')):
        mat=PAT_DEV.fullmatch(p.name)
        if not mat or not p.is_file() or p.is_symlink():continue
        n=int(mat.group(1));s=not_comments(p.read_text(encoding='utf-8',errors='replace'))
        mg=PAT_GRID.search(s)
        if not mg:continue
        grid=int(mg.group(1))
        if grid not in sde:continue
        d=sde[grid]['depth']
        if d not in DEPTHS:continue
        issues=[]
        tempvals=[float(x) for x in PAT_TEMP.findall(s)]
        if not tempvals:
            temp=None;issues.append('No numeric Temperature in PP deck')
        elif any(abs(v-tempvals[0])>1e-6 for v in tempvals):
            temp=None;issues.append('Contradictory temperatures: '+str(tempvals))
        else:
            temp=tempvals[0]
            if abs(temp-round(temp))>1e-6:
                issues.append('Noninteger temperature: '+str(temp))
            temp=int(round(temp))
            if temp not in TEMPS:issues.append('Unexpected TempK '+str(temp))
        mode,note=identify_mode(s)
        if mode is None:issues.append(note)
        pt=PAT_PLOT.search(s);pc=PAT_CURRENT.search(s)
        if not pt or pt.group(1)!=f'n{n}_des.tdr':issues.append('Plot filename/node mismatch')
        if not pc or pc.group(1)!=f'n{n}_des.plt':issues.append('Current filename/node mismatch')
        if not re.search(r'\bWorkfunction\s*=\s*4\.8(?:0*)\b',s,re.I):
            issues.append('Workfunction not verified at 4.8 eV')
        if mode is not None and bool(PAT_HURKX.search(s)) != (mode!=6):
            issues.append('Unexpected Hurkx activation')
        tlist=tdrs.get(f'n{n}_des.tdr',[]);plist=plts.get(f'n{n}_des.plt',[])
        if len(tlist)!=1:issues.append(f'TDR file matches {len(tlist)} (expect 1)')
        if len(plist)!=1:issues.append(f'PLT file matches {len(plist)} (expect 1)')
        tr=tlist[0] if len(tlist)==1 else None
        pl=plist[0] if len(plist)==1 else None
        if tr and tr.stat().st_size==0:issues.append('Empty native TDR')
        if pl and pl.stat().st_size==0:issues.append('Empty native PLT')
        records.append(dict(DBCAT_nm=d,TempK=temp if temp is not None else '',RunMode=mode if mode is not None else '',
            SDE_node=grid,SDevice_node=n,PP_path=str(p.resolve()),SDE_PP_path=str(sde[grid]['path'].resolve()),
            TDR_path=str(tr.resolve()) if tr else '',PLT_path=str(pl.resolve()) if pl else '',
            PP_SHA256=sha(p),SDE_PP_SHA256=sde[grid]['sha'],
            TDR_size_bytes=tr.stat().st_size if tr else '',PLT_size_bytes=pl.stat().st_size if pl else '',
            TDR_mtime_ns=tr.stat().st_mtime_ns if tr else '',PLT_mtime_ns=pl.stat().st_mtime_ns if pl else '',
            status='READY' if not issues else 'BLOCKED',notes=';'.join(issues)))
    count=defaultdict(int)
    for r in records:count[(r['DBCAT_nm'],r['TempK'],r['RunMode'])]+=1
    expected={(d,t,m) for d in DEPTHS for t in TEMPS for m in MODES}
    found=set(count)
    missing=sorted(expected-found)
    duplicate=sorted(x for x,n in count.items() if n>1)
    unexpected=sorted(found-expected,key=str)
    qc={'expected_cases':len(expected),'found_cases':len(records),'missing':missing,'duplicate':duplicate,
        'unexpected':unexpected,'blocked':[{'depth':r['DBCAT_nm'],'TempK':r['TempK'],
        'RunMode':r['RunMode'],'node':r['SDevice_node'],'notes':r['notes']} for r in records if r['status']!='READY'],
        'sde_nodes_found':len(sde),'sde_provenance_errors':errors,
        'valid':len(records)==len(expected) and not (missing or duplicate or unexpected or errors) and
             all(r['status']=='READY' for r in records),
        'comment':'Preflight verifies PP source, T/geometry/mode, and existence of native PLT/TDR; no numerical validation until --run.'}
    records.sort(key=lambda r:(r['DBCAT_nm'],r['TempK'] if isinstance(r['TempK'],int) else -1,
                               r['RunMode'] if isinstance(r['RunMode'],int) else -1))
    return records,qc


def discover_combined(project, baseline_project=None):
    """Preserve SWB provenance across independent temperature and existing 300-K campaigns.

    All PP/SDE/native files are resolved within the project that owns the case;
    node IDs may collide between projects without mixing geometries or native TDRs.
    Prefer the temperature project when a condition exists in both; use a
    separate baseline project only to fill absent *300 K* combinations.
    """
    primary, primary_qc = discover(project)
    for r in primary:
        r['source_project'] = str(project)
        r['source_role'] = 'temperature_project'
    if baseline_project is None:
        primary_qc['sources'] = [{'role': 'temperature_project', 'project': str(project),
                                  'selected_cases': len(primary)}]
        return primary, primary_qc

    historical, historical_qc = discover(baseline_project)
    primary_keys = {(r['DBCAT_nm'], r['TempK'], r['RunMode']) for r in primary}
    baseline_fill = []
    duplicates_skipped = []
    for r in historical:
        if r['TempK'] != 300:
            continue  # Historical project is a controlled 300-K fallback only.
        k = (r['DBCAT_nm'], r['TempK'], r['RunMode'])
        if k in primary_keys:
            duplicates_skipped.append(k)
        else:
            r['source_project'] = str(baseline_project)
            r['source_role'] = 'baseline_300K_fallback'
            baseline_fill.append(r)

    records = primary + baseline_fill
    counts = defaultdict(int)
    for r in records:
        counts[(r['DBCAT_nm'], r['TempK'], r['RunMode'])] += 1
    expected = {(d, t, m) for d in DEPTHS for t in TEMPS for m in MODES}
    found = set(counts)
    errors = (['Temp project: ' + e for e in primary_qc['sde_provenance_errors']] +
              ['Baseline project: ' + e for e in historical_qc['sde_provenance_errors']])
    qc = {
        'expected_cases': len(expected),
        'found_cases': len(records),
        'missing': sorted(expected - found),
        'duplicate': sorted(k for k,v in counts.items() if v > 1),
        'unexpected': sorted(found - expected, key=str),
        'blocked': [{'depth': r['DBCAT_nm'], 'TempK': r['TempK'], 'RunMode': r['RunMode'],
                     'node': r['SDevice_node'], 'project': r['source_project'], 'notes': r['notes']}
                    for r in records if r['status'] != 'READY'],
        'sde_nodes_found': primary_qc['sde_nodes_found'] + historical_qc['sde_nodes_found'],
        'sde_provenance_errors': errors,
        'sources': [
            {'role': 'temperature_project', 'project': str(project),
             'selected_cases': len(primary)},
            {'role': 'baseline_300K_fallback', 'project': str(baseline_project),
             'selected_cases': len(baseline_fill)},
        ],
        'baseline_duplicates_skipped': len(duplicates_skipped),
        'comparison_guardrail': ('The fallback 300-K campaign must be from the same physical '
                                '3D geometry, mesh policy, physics and bias protocol as the '
                                'temperature project. Preflight confirms PP dimensions/temperature, '
                                'not full cross-project geometry equivalence.'),
        'comment': ('Per-case provenance is independently resolved within the SWB owning project. '
                    'Only missing 300-K combinations are filled from baseline; '
                    'no SDevice rerun or numerical result fabrication.'),
    }
    qc['valid'] = (len(records) == len(expected) and not (
        qc['missing'] or qc['duplicate'] or qc['unexpected'] or qc['blocked'] or errors))
    records.sort(key=lambda r:(r['DBCAT_nm'], r['TempK'] if isinstance(r['TempK'],int) else -1,
                               r['RunMode'] if isinstance(r['RunMode'],int) else -1))
    return records, qc

# Embedded unchanged 2026-10-31 SVisual T-2022.03 extraction logic,
# reconstructed from the executed GitHub 24–48 nm V5 extractor.
# This makes the 49–60 nm runner independent of a local Git checkout.
ROI={'GATE_DRAIN':(.015,.030), 'MID_DRAIN':(.030,.045), 'OUTER_DRAIN':(.045,.060)}
YMIN,YMAX,ZMIN,ZMAX=-.200,.200,-.200,.200

def tcl_script(tdr, dest, depth,mode,n, do_lines):
    lines=[
        '# Generated for Sentaurus Visual T-2022.03. Read-only device TDR.',
        'set rawout [open '+q(dest/'raw_rows.csv')+' w]',
        'puts $rawout "depth_nm,mode,node,roi,metric,value,x_um,y_um,z_um,status"',
        'proc emit {f d m n roi metric value coords status} {',
        '  set xx ""; set yy ""; set zz ""',
        '  if {[llength $coords] > 0} {set xx [lindex $coords 0]}',
        '  if {[llength $coords] > 1} {set yy [lindex $coords 1]}',
        '  if {[llength $coords] > 2} {set zz [lindex $coords 2]}',
        '  puts $f [join [list $d $m $n $roi $metric $value $xx $yy $zz $status] ","]',
        '}',
        'proc record_integral {f ds d m n roi metric field win} {',
        '  if {[catch {set v [integrate_field -plot $ds -field $field -materials {Silicon} -window $win]} err]} {',
        '    puts stderr "CMP_FIELD_ERROR depth=$d mode=$m node=$n roi=$roi metric=$metric : $err"',
        '    emit $f $d $m $n $roi $metric "" {} ERROR',
        '  } else {',
        '    # Native SVisual Band2BandGeneration integrate_field is already in [s^-1].',
        '    # The two user-derived minmax fields need 1e-12 um^3 -> cm^3.',
        '    if {$metric eq "G_BTBT_POS_integral_per_s" || $metric eq "G_BTBT_NEG_integral_per_s"} {set v [expr {double($v)*1.0e-12}]}',
        '    emit $f $d $m $n $roi $metric $v {} OK',
        '  }',
        '}',
        'proc record_max {f ds d m n roi metric field xa xb} {',
        '  # Exact -points/-bottom/-top syntax is from SVisual T-2022.03, p.254.',
        '  set pts [list [list $xa -0.2 -0.2] [list $xb -0.2 -0.2] [list $xb 0.2 -0.2] [list $xa 0.2 -0.2]]',
        '  if {[catch {set v [extract_value -plot $ds -field $field -materials {Silicon} -max -type z -bottom -0.2 -top 0.2 -points $pts]} err]} {',
        '    puts stderr "CMP_MAX_ERROR depth=$d mode=$m node=$n roi=$roi metric=$metric : $err"',
        '    emit $f $d $m $n $roi $metric "" {} ERROR',
        '  } else {emit $f $d $m $n $roi $metric [lindex $v 0] [lindex $v 1] OK}',
        '}',
        'set before [list_datasets -dim 3]',
        'if {[catch {set file_id [load_file '+q(tdr.resolve())+' -alldata]} err]} {',
        '  puts stderr "CMP_LOAD_ERROR $err"; close $rawout; exit 2',
        '}',
        'set after [list_datasets -dim 3]',
        'set newly_loaded {}',
        'foreach cand $after {if {[lsearch -exact $before $cand] < 0} {lappend newly_loaded $cand}}',
        'puts "CMP_LOAD_RETURN=<$file_id>"',
        'puts "CMP_3D_DATASETS=<$after>"',
        'puts "CMP_NEW_3D_DATASETS=<$newly_loaded>"',
        'if {[llength $newly_loaded] == 0} {',
        '  puts stderr "CMP_NO_3D_DATASET: No new 3D dataset loaded"',
        '  close $rawout; exit 2',
        '}',
        'set candidates {}',
        'foreach cand $newly_loaded {',
        '  if {[catch {set flds [list_fields -dataset $cand]} ferr]} {',
        '    puts stderr "CMP_FIELD_LIST_ERROR dataset=<$cand>: $ferr"',
        '    continue',
        '  }',
        '  puts "CMP_FIELDS dataset=<$cand> : $flds"',
        '  if {[lsearch -exact $flds Band2BandGeneration] >= 0} {lappend candidates $cand}',
        '}',
        'if {[llength $candidates] != 1} {',
        '  puts stderr "CMP_AMBIGUOUS_SPATIAL_DATASET: candidates=<$candidates> count=[llength $candidates]. Need unique 3D dataset with Band2BandGeneration."',
        '  close $rawout; exit 2',
        '}',
        'set ds [lindex $candidates 0]',
        'puts "CMP_SELECTED_DATASET=<$ds>"',
        'if {[catch {set plot [create_plot -dataset $ds -name CMP_PLOT_3D]} perr]} {',
        '  puts stderr "CMP_CREATE_PLOT_ERROR dataset=<$ds> : $perr"',
        '  close $rawout; exit 3',
        '}',
        'puts "CMP_SELECTED_PLOT=<$plot>"',
        'set inv [open '+q(dest/'field_inventory.txt')+' w]',
        'puts $inv "DATASET=$ds"',
        'puts $inv "AVAILABLE_FIELDS=[list_fields -dataset $ds]"',
        'close $inv',
        'set fields_ready 1',
        'if {[catch {create_field -name CMP_BTBT_POS -plot $plot -function "minmax(<Band2BandGeneration>,0,1e100)"} err]} {',
        '  puts stderr "CMP_CREATE_POS_ERROR $err"; set fields_ready 0',
        '}',
        'if {[catch {create_field -name CMP_BTBT_NEG -plot $plot -function "minmax(<Band2BandGeneration>,-1e100,0)"} err]} {',
        '  puts stderr "CMP_CREATE_NEG_ERROR $err"; set fields_ready 0',
        '}',
        'if {!$fields_ready} {close $rawout;exit 3}',
    ]
    for name,(xa,xb) in list(ROI.items())+[('FULL_SILICON',(-.200,.200))]:
        win='{%.6f %.6f %.6f %.6f %.6f %.6f}'%(xa,YMIN,ZMIN,xb,YMAX,ZMAX)
        lines.append('set win '+win)
        for metric,field in [('G_BTBT_SIGNED_integral_per_s','Band2BandGeneration'),
                             ('G_BTBT_POS_integral_per_s','CMP_BTBT_POS'),
                             ('G_BTBT_NEG_integral_per_s','CMP_BTBT_NEG'),
                             ('Si_volume_um3','__DOMAIN__')]:
            if field=='__DOMAIN__':
                lines.extend([
                    'if {[catch {set v [integrate_field -plot $plot -field Band2BandGeneration -materials {Silicon} -window $win -returndomain]} err]} {',
                    '  puts stderr "CMP_VOLUME_ERROR depth=%d mode=%d node=%d roi=%s : $err"'%(depth,mode,n,name),
                    '  emit $rawout %d %d %d %s Si_volume_um3 "" {} ERROR'%(depth,mode,n,name),
                    '} else {emit $rawout %d %d %d %s Si_volume_um3 $v {} OK}'%(depth,mode,n,name)
                ])
            else:
                lines.append('record_integral $rawout $plot %d %d %d %s %s %s $win'%(depth,mode,n,name,metric,field))
        for metric,field in [('EABS_max_V_per_cm','Abs(ElectricField-V)'),
                             ('G_BTBT_max_per_cm3_s','Band2BandGeneration'),
                             ('G_BTBT_POS_max_per_cm3_s','CMP_BTBT_POS')]:
            lines.append('record_max $rawout $plot %d %d %d %s %s {%s} %.6f %.6f'%(depth,mode,n,name,metric,field,xa,xb))
    if do_lines:
        for y in [0.,.0075]:
            for z in [-.048,-.025]:
                nm='line_y%s_z%s'%(str(y).replace('.','p'),str(z).replace('-','m').replace('.','p'))
                path=dest/(nm+'.csv')
                lines.extend([
                    'if {[catch {',
                    '  set cut [create_cutline -plot $plot -type free -points {0.010 %.6f %.6f 0.060 %.6f %.6f}]'%(y,z,y,z),
                    '  export_variables -dataset $cut -filename '+q(path)+' -overwrite',
                    '} err]} {puts stderr "CMP_CUTLINE_ERROR '+nm+' : $err"} else {puts "CMP_CUTLINE_OK '+nm+'"}',
                ])
    lines.extend(['close $rawout','puts "CMP_SPATIAL_TCL_DONE depth=%d mode=%d node=%d"'%(depth,mode,n),'exit'])
    return '\n'.join(lines)+'\n'

def numerical_qc(rows, d, m):
    ours=[r for r in rows if int(r['depth_nm'])==d and int(r['mode'])==m]
    notes=[]
    if len(ours)!=28:notes.append('ROW_COUNT_NOT_28')
    if any(r['status']!='OK' for r in ours):notes.append('SVISUAL_OPERATION_ERROR')
    for name,span in list(ROI.items())+[('FULL_SILICON',(-.200,.200))]:
        vals={r['metric']:r for r in ours if r['roi']==name and r['status']=='OK'}
        try:
            sn=float(vals['G_BTBT_SIGNED_integral_per_s']['value'])
            pos=float(vals['G_BTBT_POS_integral_per_s']['value'])
            neg=float(vals['G_BTBT_NEG_integral_per_s']['value'])
            volume=float(vals['Si_volume_um3']['value'])
            emax=float(vals['EABS_max_V_per_cm']['value'])
            xemax=float(vals['EABS_max_V_per_cm']['x_um'])
            if volume<=0:notes.append(name+'_NONPOSITIVE_VOLUME')
            if pos< -1e-5 or neg>1e-5:notes.append(name+'_GENERATION_SIGN_ERROR')
            if abs(sn-(pos+neg))>max(1e-5,1e-3*max(abs(sn),abs(pos),abs(neg))):notes.append(name+'_SIGN_IDENTITY_FAIL')
            if emax<0:notes.append(name+'_E_MAG_NEGATIVE')
            if xemax<span[0]-1e-5 or xemax>span[1]+1e-5:notes.append(name+'_EMAX_OUTSIDE_ROI')
        except (ValueError,TypeError,KeyError):notes.append(name+'_MISSING_NUMERIC_OR_COORD')
    return notes

def terminal_tcl(plt,dest):
    """T-2022.03 load_file, list_datasets, export_variables (official SVisual guide)."""
    return '\n'.join([
        '# CMP native PLT export. Source read-only.',
        'set before [list_datasets -dim 1]',
        'if {[catch {load_file '+q(plt)+' -alldata} err]} {puts stderr "CMP_PLT_LOAD_FAIL $err";exit 2}',
        'set after [list_datasets -dim 1]',
        'set newer {}',
        'foreach candidate $after {if {[lsearch -exact $before $candidate] < 0} {lappend newer $candidate}}',
        'if {[llength $newer] != 1} {puts stderr "CMP_PLT_AMBIGUOUS $newer";exit 3}',
        'set ds [lindex $newer 0]',
        'if {[catch {export_variables -dataset $ds -filename '+q(dest)+' -overwrite} err]} {puts stderr "CMP_PLT_EXPORT_FAIL $err";exit 4}',
        'puts "CMP_PLT_EXPORT_PASS dataset=$ds"',
        'exit',
        ''])

def run_visual(script,output_log,svisual):
    with output_log.open('w',encoding='utf-8') as f:
        p=subprocess.run([svisual,'-batch',str(script)],stdout=f,stderr=subprocess.STDOUT,check=False)
    return p.returncode

def numeric_curves(csvpath):
    with csvpath.open(encoding='utf-8-sig',newline='') as f:
        rdr=csv.DictReader(f)
        required={'gate OuterVoltage','drain OuterVoltage','drain TotalCurrent','source TotalCurrent','gate TotalCurrent','substrate TotalCurrent'}
        if not required.issubset(set(rdr.fieldnames or [])):raise ValueError('Missing fields: '+str(sorted(required-set(rdr.fieldnames or []))))
        vals=[]
        for row in rdr:
            try:
                z={k:float(row[k]) for k in required}
                if all(math.isfinite(v) for v in z.values()):vals.append(z)
            except (ValueError,KeyError,TypeError):continue  # SVisual second header row
    return vals

def curve_metrics(curve,d,m):
    targets={0:(1.5,.05),1:(2.0,1.2),2:(.1,1.2),3:(.6,1.2),4:(1.2,1.2),5:(-.7,1.2),6:(-.7,1.2)}
    tg,td=targets[m]
    if not curve:raise ValueError('Empty curve')
    end=curve[-1]
    if abs(end['gate OuterVoltage']-tg)>1e-5 or abs(end['drain OuterVoltage']-td)>1e-5:
        raise ValueError(f'Endpoint not reached: expected ({tg},{td}), got ({end["gate OuterVoltage"]},{end["drain OuterVoltage"]})')
    terms=['source TotalCurrent','drain TotalCurrent','gate TotalCurrent','substrate TotalCurrent']
    max_rel=0
    for pt in curve:
        vals=[pt[k] for k in terms]
        residual=abs(sum(vals))/max(sum(abs(x) for x in vals),1e-22)
        max_rel=max(max_rel,residual)
    if max_rel>1e-4:raise ValueError(f'KCL relative {max_rel:.3g} > 1e-4')
    output={'DBCAT_nm':d,'RunMode':m,'n_points':len(curve),'last_Vg':end['gate OuterVoltage'],
            'last_Vd':end['drain OuterVoltage'],'last_Id_A':end['drain TotalCurrent'],
            'KCL_relative_max':max_rel,'status':'EXTRACTED'}
    if m in [0,1]:
        points=[(r['gate OuterVoltage'],r['drain TotalCurrent']) for r in curve if abs(r['drain OuterVoltage']-td)<1e-4]
        points=sorted(points)
        for val,name in [(0.,'Id_Vg0_A'),(1.2,'Id_Vg1p2_A')]:
            for (x0,y0),(x1,y1) in zip(points,points[1:]):
                if x0<=val<=x1 and x0!=x1:
                    output[name]=y0+(y1-y0)*(val-x0)/(x1-x0);break
        if len(points)<2:raise ValueError('No Vg ramp samples')
        # Matches the Git V5 24/36/48-nm Vth proxies exactly: Icrit=1e-7*(17/20) A,
        # logarithmic current interpolation, not linear-current interpolation.
        icrit=8.5e-8
        for (x0,y0),(x1,y1) in zip(points,points[1:]):
            if x1>x0 and y0>0 and y1>0 and y0<=icrit<=y1:
                output['Vth_proxy_V']=x0+(x1-x0)*(math.log(icrit)-math.log(y0))/(math.log(y1)-math.log(y0))
                break
        if 'Vth_proxy_V' not in output:raise ValueError('Constant-current threshold not reached')
    return output



# Notes: The embedded Tcl 'raw_rows.csv' intentionally records d,mode,node only.
# Temperature is added to the consolidated rows from source-provenance mapping.

def ss_local_window(curve, mode):
    """Independent exploratory SS definition, not historical SS quick protocol.
    Use log(I_D) interpolation for Vg at 1e-10 and 1e-8 A (2 decades).
    """
    vd={0:.05,1:1.2}[mode]
    pts=sorted((p['gate OuterVoltage'],p['drain TotalCurrent']) for p in curve
               if abs(p['drain OuterVoltage']-vd)<1e-4)
    def gate_at(icrit):
        hits=[]
        for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
            if x1>x0 and y0>0 and y1>0 and y0<=icrit<=y1 and y0!=y1:
                v=x0+(x1-x0)*(math.log(icrit)-math.log(y0))/(math.log(y1)-math.log(y0))
                hits.append(v)
        return hits[0] if len(hits)==1 else None
    lo=gate_at(1e-10);hi=gate_at(1e-8)
    if lo is None or hi is None or hi<=lo:return ''
    return (hi-lo)*500.0


def consolidate_spatial(raw_rows):
    by=defaultdict(dict)
    for r in raw_rows:
        if r.get('status')=='OK':
            k=(int(r['DBCAT_nm']),int(r['TempK']),int(r['RunMode']),r['roi'])
            by[k][r['metric']]=r
    rows=[]
    for (d,t,m,roi),vals in sorted(by.items()):
        a={'DBCAT_nm':d,'TempK':t,'RunMode':m,'roi':roi}
        for metric,v in vals.items():
            a[metric]=float(v['value'])
            if metric in ('EABS_max_V_per_cm','G_BTBT_max_per_cm3_s','G_BTBT_POS_max_per_cm3_s'):
                for axis in 'xyz':
                    a[metric+'_'+axis+'_um']=float(v[axis+'_um']) if v.get(axis+'_um') else ''
        a['qG_positive_A']=Q*a['G_BTBT_POS_integral_per_s']
        a['qG_signed_A']=Q*a['G_BTBT_SIGNED_integral_per_s']
        a['qG_negative_A']=Q*a['G_BTBT_NEG_integral_per_s']
        a['qG_identity_abs_residual_A']=abs(a['qG_signed_A']-a['qG_positive_A']-a['qG_negative_A'])
        rows.append(a)
    expected={(d,t,m,roi) for d in DEPTHS for t in TEMPS for m in MODES for roi in ROIS}
    found={(a['DBCAT_nm'],a['TempK'],a['RunMode'],a['roi']) for a in rows}
    if found!=expected:
        raise ValueError(f'Spatial ROI count {len(found)}, expected {len(expected)}; missing {sorted(expected-found)[:8]}')
    return rows


def depth_temp_metrics(terms,space):
    tm={(int(r['DBCAT_nm']),int(r['TempK']),int(r['RunMode'])):r for r in terms}
    sm={(int(r['DBCAT_nm']),int(r['TempK']),int(r['RunMode']),r['roi']):r for r in space}
    output=[]
    for d in DEPTHS:
        for t in TEMPS:
            k=lambda m:tm[(d,t,m)]
            vthlow=k(0)['Vth_proxy_V']; vthhigh=k(1)['Vth_proxy_V']
            on=k(5)['last_Id_A'];off=k(6)['last_Id_A']
            ron=k(1);ion=ron['Id_Vg1p2_A'];ioff=ron.get('Id_Vg0_A','')
            a=dict(DBCAT_nm=d,TempK=t,Vth_low_proxy_V=vthlow,Vth_high_proxy_V=vthhigh,
                   DIBL_proxy_mV_per_V=(vthlow-vthhigh)/1.15*1000,
                   SS_low_window_1e10_1e8_mV_dec=k(0).get('SS_1e10_1e8_mV_dec',''),
                   SS_high_window_1e10_1e8_mV_dec=k(1).get('SS_1e10_1e8_mV_dec',''),
                   Ion_Vg1p2_Vd1p2_A=ion,Ioff_Vg0_Vd1p2_A=ioff,
                   Ion_over_Ioff_proxy=(abs(ion)/abs(ioff) if ioff and abs(ioff)>0 else ''),
                   GIDL_ON_Id_Vgneg0p7_A=on,GIDL_OFF_Id_Vgneg0p7_A=off,
                   Hurkx_ON_minus_OFF_A=on-off,
                   scientific_status='CMP-EXTRACTED-PROVISIONAL',
                   caveat='SS: new fixed-current 1e-10..1e-8 A local proxy (not legacy SS quick). '+
                          'Hurkx terminal excess is not proven collected GIDL. '+
                          'Global outer drain x~0.060 um may be boundary/contact sensitive.')
            for roi in ('GATE_DRAIN','OUTER_DRAIN','FULL_SILICON'):
                s=sm[(d,t,5,roi)]
                a['Emax_'+roi+'_MV_per_cm']=s['EABS_max_V_per_cm']/1e6
                a['qGpositive_'+roi+'_A']=s['qG_positive_A']
                a['Emax_'+roi+'_x_um']=s['EABS_max_V_per_cm_x_um']
            output.append(a)
    return output


def thermal_relative(rows):
    by={(r['DBCAT_nm'],r['TempK']):r for r in rows}
    keys=['Vth_low_proxy_V','Vth_high_proxy_V','DIBL_proxy_mV_per_V',
          'Ion_Vg1p2_Vd1p2_A','Ioff_Vg0_Vd1p2_A','GIDL_ON_Id_Vgneg0p7_A',
          'GIDL_OFF_Id_Vgneg0p7_A','Hurkx_ON_minus_OFF_A',
          'Emax_GATE_DRAIN_MV_per_cm','qGpositive_GATE_DRAIN_A',
          'Emax_OUTER_DRAIN_MV_per_cm','qGpositive_OUTER_DRAIN_A']
    out=[]
    for d in DEPTHS:
        base=by[(d,300)]
        for t in TEMPS:
            here=by[(d,t)]
            for key in keys:
                a=here.get(key,'');b=base.get(key,'')
                if a=='' or b=='':delta='';pct=''
                else:
                    delta=a-b;pct=100*(a/b-1) if b!=0 else ''
                out.append({'DBCAT_nm':d,'TempK':t,'metric':key,'value':a,
                            'baseline_300K':b,'delta_from_300K':delta,'pct_from_300K':pct})
    return out


def spatial_on_off_delta(space):
    s={(r['DBCAT_nm'],r['TempK'],r['RunMode'],r['roi']):r for r in space}
    rows=[]
    cols=('qG_positive_A','qG_signed_A','qG_negative_A','EABS_max_V_per_cm','G_BTBT_POS_max_per_cm3_s')
    for d in DEPTHS:
        for t in TEMPS:
            for roi in ROIS:
                a=s[(d,t,5,roi)];b=s[(d,t,6,roi)]
                row={'DBCAT_nm':d,'TempK':t,'roi':roi}
                for c in cols:
                    row[c+'_ON']=a[c];row[c+'_OFF']=b[c]
                    row[c+'_ON_minus_OFF']=a[c]-b[c]
                rows.append(row)
    return rows


def label(r):
    return f"DBCAT_{int(r['DBCAT_nm']):02d}_T{int(r['TempK'])}_mode{int(r['RunMode'])}_n{int(r['SDevice_node'])}"


def artifact_paths(out,r):
    labelstr=label(r)
    d=int(r['DBCAT_nm']);t=int(r['TempK']);m=int(r['RunMode'])
    sub=out/'SPATIAL_cutlines'/f'DBCAT_{d:02d}'/f'T{t}'/f'mode{m}'
    return dict(base=labelstr,curve=out/'DC_curves'/(labelstr+'.plt.csv'),
                folder=sub,raw=sub/'raw_rows.csv',done=out/'CASE_DONE'/(labelstr+'.json'),
                terminal_script=out/'SVisual_scripts'/(labelstr+'_terminal.tcl'),
                spatial_script=out/'SVisual_scripts'/(labelstr+'_spatial.tcl'),
                terminal_log=out/'logs'/(labelstr+'_terminal.log'),
                spatial_log=out/'logs'/(labelstr+'_spatial.log'))


def get_completed(r,paths,do_lines):
    if not paths['done'].exists():return None
    try:
        proof=json.loads(paths['done'].read_text(encoding='utf-8'))
        for k in ('PP_SHA256','SDE_PP_SHA256','TDR_size_bytes','PLT_size_bytes',
                  'TDR_mtime_ns','PLT_mtime_ns'):
            if str(proof.get(k,''))!=str(r.get(k,'')):return None
        curve=numeric_curves(paths['curve'])
        term=curve_metrics(curve,int(r['DBCAT_nm']),int(r['RunMode']))
        raw=readcsv(paths['raw'])
        if numerical_qc(raw,int(r['DBCAT_nm']),int(r['RunMode'])):return None
        if len(raw)!=28:return None
        if do_lines and len(list(paths['folder'].glob('line_*.csv')))!=4:return None
        return term,raw
    except (OSError,ValueError,KeyError,TypeError,json.JSONDecodeError):return None


def extract_case(r,out,args):
    paths=artifact_paths(out,r)
    if args.resume:
        cached=get_completed(r,paths,not args.no_cutlines)
        if cached is not None:
            print('SKIP (verified)',paths['base'],flush=True)
            return cached
    paths['done'].unlink(missing_ok=True)
    paths['folder'].mkdir(parents=True,exist_ok=True)
    shutil.copyfile(r['PP_path'],out/'PP_DECKS'/(paths['base']+'_pp_des.cmd'))
    # Distinct T branch paths prevent same-node-name collisions across two SWB projects.
    sdep=out/'PP_DECKS'/(f"DBCAT_{int(r['DBCAT_nm'])}_T{int(r['TempK'])}_SDE_n{int(r['SDE_node'])}_pp_dvs.cmd")
    if not sdep.exists():shutil.copyfile(r['SDE_PP_path'],sdep)
    paths['terminal_script'].write_text(terminal_tcl(r['PLT_path'],paths['curve']),encoding='utf-8')
    rc=run_visual(paths['terminal_script'],paths['terminal_log'],args.svisual_bin)
    if rc or not paths['curve'].is_file():
        raise RuntimeError(paths['base']+f' PLT export failed; rc={rc}; log='+str(paths['terminal_log']))
    cv=numeric_curves(paths['curve']);term=curve_metrics(cv,int(r['DBCAT_nm']),int(r['RunMode']))
    paths['spatial_script'].write_text(tcl_script(Path(r['TDR_path']),paths['folder'],
                                  int(r['DBCAT_nm']),int(r['RunMode']),int(r['SDevice_node']),
                                  not args.no_cutlines),encoding='utf-8')
    rc2=run_visual(paths['spatial_script'],paths['spatial_log'],args.svisual_bin)
    if rc2 or not paths['raw'].is_file():
        raise RuntimeError(paths['base']+f' Spatial export failed; rc={rc2}; log='+str(paths['spatial_log']))
    raw=readcsv(paths['raw'])
    notes=numerical_qc(raw,int(r['DBCAT_nm']),int(r['RunMode']))
    nc=len(list(paths['folder'].glob('line_*.csv')))
    if len(raw)!=28 or notes or (not args.no_cutlines and nc!=4):
        raise RuntimeError(paths['base']+f': spatial QC failed; rows={len(raw)}; notes={notes}; cutlines={nc}')
    proof={k:r[k] for k in ('PP_SHA256','SDE_PP_SHA256','TDR_size_bytes',
                             'PLT_size_bytes','TDR_mtime_ns','PLT_mtime_ns')}
    proof.update({'label':paths['base'],'verified_at_UTC':datetime.now(timezone.utc).isoformat(),
                  'terminal_points':len(cv),'roi_raw_rows':len(raw),'cutlines':nc})
    paths['done'].write_text(json.dumps(proof,indent=2)+'\n',encoding='utf-8')
    print('PASS',paths['base'],flush=True)
    return term,raw


def package(out,records,args):
    terminals=[];allspatial=[];cases=[]
    for r in records:
        paths=artifact_paths(out,r)
        cached=get_completed(r,paths,not args.no_cutlines)
        if cached is None:raise RuntimeError('Cannot finalize: incomplete or invalid '+paths['base'])
        term,raw=cached
        term.update({'SDevice_node':int(r['SDevice_node']),'TempK':int(r['TempK'])})
        if int(r['RunMode']) in (0,1):
            term['SS_1e10_1e8_mV_dec']=ss_local_window(numeric_curves(paths['curve']),int(r['RunMode']))
        terminals.append(term)
        for v in raw:allspatial.append({'DBCAT_nm':int(r['DBCAT_nm']),'TempK':int(r['TempK']),
                                        'RunMode':int(r['RunMode']),'SDevice_node':int(r['SDevice_node']),**v})
        cases.append({'DBCAT_nm':r['DBCAT_nm'],'TempK':r['TempK'],'RunMode':r['RunMode'],
                      'source_role':r.get('source_role',''), 'source_project':r.get('source_project',''),
                      'node':r['SDevice_node'],'terminal_status':'EXTRACTED',
                      'spatial_status':'QC_PASS','cutlines':len(list(paths['folder'].glob('line_*.csv')))})
    # Important: in raw_rows.csv the inherited T-2022.03 Tcl uses depth_nm,mode,node;
    # on aggregation, avoid trusting extra metadata embedded in the legacy Tcl rows.
    for v in allspatial:
        if int(v['depth_nm'])!=int(v['DBCAT_nm']) or int(v['mode'])!=int(v['RunMode']) or int(v['node'])!=int(v['SDevice_node']):
            raise ValueError('Spatial row node/depth/mode provenance mismatch')
    sp=consolidate_spatial(allspatial)
    metrics=depth_temp_metrics(terminals,sp)
    writecsv(out/'TERMINAL_140_QC.csv',terminals,sorted(set().union(*(r.keys() for r in terminals))))
    writecsv(out/'SPATIAL_RAW_140.csv',allspatial,list(allspatial[0]))
    writecsv(out/'SPATIAL_ROI_560.csv',sp,list(dict.fromkeys(k for r in sp for k in r)))
    writecsv(out/'CASE_QC_140.csv',cases)
    writecsv(out/'MEB_5x4_TEMPERATURE_METRICS.csv',metrics,list(metrics[0]))
    relative=thermal_relative(metrics)
    writecsv(out/'METRICS_DELTA_vs_300K.csv',relative)
    delta=spatial_on_off_delta(sp)
    writecsv(out/'HURKX_SPATIAL_ON_OFF_DELTA_80.csv',delta,list(delta[0]))
    status={'lineage':'3D-Sun-SADDLE-V1 / Flat upper S/D working baseline',
            'scientific_status':'EXTRACTION-QC-PASSED / SCIENTIFIC-PROVISIONAL',
            'DBCAT_nm':list(DEPTHS),'TempK':list(TEMPS),'RunMode':list(MODES),
            'expected_cases':140,'verified_terminal_cases':len(terminals),'spatial_raw_rows':len(allspatial),
            'spatial_roi_rows':len(sp),'cutline_files':sum(c['cutlines'] for c in cases),
            'model_scope':['thermal DC/BTBT trends, not direct 1T1C retention',
                           'Hurkx ON-minus-OFF is not pure collected terminal GIDL',
                           'qGpositive = q*positive BTBT volume-generation integral, not collected current',
                           'x~60nm drain boundary/contact effect not resolved',
                           'mesh convergence and 233K low-temperature model validity not demonstrated',
                           'SS fixed current 1e-10..1e-8 A is a new exploratory definition; legacy SS not comparable'],
            'temperature_branch_provenance':'Preprocessed PP temperature numeric, validated per native node',
            'sources':sorted(set(str(r.get('source_project','')) for r in records)),
            'cross_project_geometry_equivalence':'REQUIRES INDEPENDENT PHYSICAL DECK REVIEW', 
            'cutline_equivalent':not args.no_cutlines}
    (out/'EXTRACTION_STATUS.json').write_text(json.dumps(status,indent=2)+'\n',encoding='utf-8')
    (out/'README_REVIEW.txt').write_text(
        'CMP 3D independent MEB x Temperature 140-case SVisual extraction.\n'
        'Counts 140 terminal sweeps, 3920 raw ROI records, 560 ROI summaries, 560 cutlines.\n'
        'No physical retention time/1T1C simulated by this exporter.\n'
        'IMPORTANT: Native signed SVisual BTBT integral already has units s^-1.\n'
        'Only user-derived positive/negative max/min integrals multiply by 1e-12 (um^3 -> cm^3).\n'
        'Hurkx ON-OFF terminal current is a model-dependent excess, NOT pure collected GIDL.\n'
        'Outlet drain x~60 nm remains contact/boundary sensitive.\n'
        'Original native TDR/PLT omitted from ZIP; review contains PP and SVisual scripts/logs, local paths.\n',
        encoding='utf-8')
    path=out/'CMP_3D_MEB_TEMP140_EXTRACTION_REVIEW.zip'
    if path.exists():path.unlink()
    with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(out.rglob('*')):
            if p.is_file() and p!=path and p.suffix.lower() not in ('.tdr','.plt'):
                z.write(p,p.relative_to(out).as_posix())
    print(f"EXTRACTION_QC_PASS {len(terminals)}/140 terminal; {len(sp)}/560 ROI; {status['cutline_files']} cutlines")
    print('REVIEW_ZIP',path)
    return path




def partial_curve_issue(out,r,error):
    """Only keep incomplete native curves as explicitly INCOMPLETE, never interpolate
    the missed -0.7 V endpoint or use that case's final TDR as target-bias evidence.
    """
    p=artifact_paths(out,r)
    if not p['curve'].is_file():
        raise RuntimeError('Cannot document partial case without native exported curve: '+p['base'])
    curve=numeric_curves(p['curve'])
    if not curve:
        raise RuntimeError('Partial case has no finite curve points: '+p['base'])
    end=curve[-1]
    terms=['source TotalCurrent','drain TotalCurrent','gate TotalCurrent','substrate TotalCurrent']
    kcl=max(abs(sum(x[k] for k in terms))/max(sum(abs(x[k]) for k in terms),1e-22)
            for x in curve)
    target={0:(1.5,.05),1:(2.0,1.2),2:(.1,1.2),3:(.6,1.2),
            4:(1.2,1.2),5:(-.7,1.2),6:(-.7,1.2)}[int(r['RunMode'])]
    return dict(DBCAT_nm=int(r['DBCAT_nm']),TempK=int(r['TempK']),
                RunMode=int(r['RunMode']),SDevice_node=int(r['SDevice_node']),
                source_role=r.get('source_role',''),native_points=len(curve),
                target_Vg_V=target[0],target_Vd_V=target[1],
                last_Vg_V=end['gate OuterVoltage'],last_Vd_V=end['drain OuterVoltage'],
                last_Id_A=end['drain TotalCurrent'],KCL_relative_max=kcl,
                issue='PARTIAL_ENDPOINT' if error.startswith('Endpoint not reached:')
                       else 'METRIC_NOT_AVAILABLE',
                error=error,
                scientific_use='DO NOT compare partial point to target bias; no -0.7 V ON/OFF delta',
                raw_curve_file=str(p['curve'].relative_to(out)))


def consolidate_spatial_available(rows):
    """Keep only fully verified spatial ROI values for successful full-bias cases."""
    by=defaultdict(dict)
    for r in rows:
        if r.get('status')!='OK':
            raise ValueError('Non-OK spatial raw row in completed-case collection')
        k=(int(r['DBCAT_nm']),int(r['TempK']),int(r['RunMode']),r['roi'])
        by[k][r['metric']]=r
    output=[]
    for (d,t,m,roi),vals in sorted(by.items()):
        a={'DBCAT_nm':d,'TempK':t,'RunMode':m,'roi':roi}
        if len(vals)!=7:
            raise RuntimeError(f'Incomplete ROI fields at {(d,t,m,roi)}: {list(vals)}')
        for metric,v in vals.items():
            a[metric]=float(v['value'])
            if metric in ('EABS_max_V_per_cm','G_BTBT_max_per_cm3_s','G_BTBT_POS_max_per_cm3_s'):
                for axis in 'xyz':
                    a[metric+'_'+axis+'_um']=float(v[axis+'_um']) if v.get(axis+'_um') else ''
        a['qG_positive_A']=Q*a['G_BTBT_POS_integral_per_s']
        a['qG_signed_A']=Q*a['G_BTBT_SIGNED_integral_per_s']
        a['qG_negative_A']=Q*a['G_BTBT_NEG_integral_per_s']
        a['qG_identity_abs_residual_A']=abs(a['qG_signed_A']-a['qG_positive_A']-a['qG_negative_A'])
        output.append(a)
    return output


def metrics_available(terms,space):
    """20 rows exactly, with missing values BLANK and documented missing modes."""
    tm={(int(r['DBCAT_nm']),int(r['TempK']),int(r['RunMode'])):r for r in terms}
    sm={(int(r['DBCAT_nm']),int(r['TempK']),int(r['RunMode']),r['roi']):r for r in space}
    result=[]
    for d in DEPTHS:
        for t in TEMPS:
            get=lambda m:tm.get((d,t,m),{})
            lo=get(0).get('Vth_proxy_V','');hi=get(1).get('Vth_proxy_V','')
            on=get(5).get('last_Id_A','');off=get(6).get('last_Id_A','')
            ron=get(1);ion=ron.get('Id_Vg1p2_A','');ioff=ron.get('Id_Vg0_A','')
            okm=[m for m in MODES if (d,t,m) in tm]
            a=dict(DBCAT_nm=d,TempK=t,completed_modes=len(okm),
                   missing_modes=','.join(str(m) for m in MODES if m not in okm),
                   status='COMPLETE' if len(okm)==7 else 'PARTIAL_CONDITIONS',
                   Vth_low_proxy_V=lo,Vth_high_proxy_V=hi,
                   DIBL_proxy_mV_per_V=(lo-hi)/1.15*1000 if lo!='' and hi!='' else '',
                   SS_low_window_1e10_1e8_mV_dec=get(0).get('SS_1e10_1e8_mV_dec',''),
                   SS_high_window_1e10_1e8_mV_dec=get(1).get('SS_1e10_1e8_mV_dec',''),
                   Ion_Vg1p2_Vd1p2_A=ion,Ioff_Vg0_Vd1p2_A=ioff,
                   Ion_over_Ioff_proxy=(abs(ion)/abs(ioff) if ion!='' and ioff!='' and abs(ioff)>0 else ''),
                   GIDL_ON_Id_Vgneg0p7_A=on,GIDL_OFF_Id_Vgneg0p7_A=off,
                   Hurkx_ON_minus_OFF_A=(on-off if on!='' and off!='' else ''),
                   scientific_status='CMP-EXTRACTED-PROVISIONAL',
                   caveat='Blank means no valid target-bias estimate. Not pure collected GIDL or physical retention.')
            for roi in ('GATE_DRAIN','OUTER_DRAIN','FULL_SILICON'):
                s=sm.get((d,t,5,roi),{})
                e=s.get('EABS_max_V_per_cm','')
                a['Emax_'+roi+'_MV_per_cm']=e/1e6 if e!='' else ''
                a['qGpositive_'+roi+'_A']=s.get('qG_positive_A','')
                a['Emax_'+roi+'_x_um']=s.get('EABS_max_V_per_cm_x_um','')
            result.append(a)
    return result


def on_off_delta_available(space):
    s={(r['DBCAT_nm'],r['TempK'],r['RunMode'],r['roi']):r for r in space}
    result=[]
    cols=('qG_positive_A','qG_signed_A','qG_negative_A','EABS_max_V_per_cm','G_BTBT_POS_max_per_cm3_s')
    for d in DEPTHS:
        for t in TEMPS:
            for roi in ROIS:
                a=s.get((d,t,5,roi));b=s.get((d,t,6,roi))
                rr={'DBCAT_nm':d,'TempK':t,'roi':roi,
                    'comparison_status':'PAIRED' if a and b else 'MISSING_ON_OR_OFF'}
                for key in cols:
                    rr[key+'_ON']=a.get(key,'') if a else ''
                    rr[key+'_OFF']=b.get(key,'') if b else ''
                    rr[key+'_ON_minus_OFF']=a[key]-b[key] if a and b else ''
                result.append(rr)
    return result


def package_partial(out,records,args,incomplete):
    terms=[];raw_rows=[];cases=[];failed=[]
    for r in records:
        k=(int(r['DBCAT_nm']),int(r['TempK']),int(r['RunMode']))
        paths=artifact_paths(out,r)
        cached=get_completed(r,paths,not args.no_cutlines)
        if cached is None:
            err=incomplete.get(k)
            if err is None:
                raise RuntimeError('Unaccounted incomplete case: '+paths['base'])
            failed.append(err)
            cases.append({'DBCAT_nm':k[0],'TempK':k[1],'RunMode':k[2],
                          'source_role':r.get('source_role',''),
                          'source_project':r.get('source_project',''),
                          'node':r['SDevice_node'],'terminal_status':err['issue'],
                          'spatial_status':'NOT_VALID_AT_TARGET_BIAS',
                          'cutlines':0,'actual_last_Vg_V':err['last_Vg_V'],
                          'target_Vg_V':err['target_Vg_V']})
            continue
        term,raw=cached
        term.update({'SDevice_node':int(r['SDevice_node']),'TempK':int(r['TempK'])})
        if int(r['RunMode']) in (0,1):
            term['SS_1e10_1e8_mV_dec']=ss_local_window(numeric_curves(paths['curve']),int(r['RunMode']))
        terms.append(term)
        for v in raw:
            row={'DBCAT_nm':k[0],'TempK':k[1],'RunMode':k[2],
                 'SDevice_node':int(r['SDevice_node']),**v}
            if int(row['depth_nm'])!=k[0] or int(row['mode'])!=k[2] or int(row['node'])!=int(r['SDevice_node']):
                raise RuntimeError('Spatial raw provenance mismatch at '+paths['base'])
            raw_rows.append(row)
        cases.append({'DBCAT_nm':k[0],'TempK':k[1],'RunMode':k[2],
                      'source_role':r.get('source_role',''),
                      'source_project':r.get('source_project',''),
                      'node':r['SDevice_node'],'terminal_status':'EXTRACTED',
                      'spatial_status':'QC_PASS',
                      'cutlines':len(list(paths['folder'].glob('line_*.csv'))),
                      'actual_last_Vg_V':term['last_Vg'],
                      'target_Vg_V':''})
    assert len(cases)==140
    sp=consolidate_spatial_available(raw_rows)
    assert len(sp)==len(terms)*4
    metrics=metrics_available(terms,sp)
    rel=thermal_relative(metrics)
    delta=on_off_delta_available(sp)
    writecsv(out/'TERMINAL_AVAILABLE_QC.csv',terms,sorted(set().union(*(r.keys() for r in terms))))
    writecsv(out/'SPATIAL_RAW_AVAILABLE.csv',raw_rows,list(raw_rows[0]))
    writecsv(out/'SPATIAL_ROI_AVAILABLE.csv',sp,list(dict.fromkeys(k for r in sp for k in r)))
    writecsv(out/'CASE_QC_140.csv',cases)
    writecsv(out/'INCOMPLETE_CASES.csv',failed)
    writecsv(out/'MEB_5x4_TEMPERATURE_METRICS_PARTIAL.csv',metrics,list(metrics[0]))
    writecsv(out/'METRICS_DELTA_vs_300K_PARTIAL.csv',rel)
    writecsv(out/'HURKX_SPATIAL_ON_OFF_DELTA_PARTIAL.csv',delta,list(delta[0]))
    status={'lineage':'3D-Sun-SADDLE-V1 / Flat upper S/D working baseline',
            'scientific_status':'PARTIAL-NUMERICAL-EXTRACTION / SCIENTIFIC-PROVISIONAL',
            'expected_cases':140,'complete_target_bias_cases':len(terms),
            'incomplete_cases_count':len(failed),
            'incomplete_cases':[{k:r[k] for k in ('DBCAT_nm','TempK','RunMode','SDevice_node','target_Vg_V','last_Vg_V','issue')} for r in failed],
            'spatial_raw_rows':len(raw_rows),'spatial_roi_rows':len(sp),
            'cutline_files':sum(x['cutlines'] for x in cases),
            'model_scope':['Partial endpoint cases EXCLUDED from target-bias metrics, spatial and paired ON/OFF statistics',
                           'Native partial DC curves are archived as evidence only',
                           'No interpolation/extrapolation to Vg=-0.7 V',
                           'Hurkx ON-minus-OFF is NOT measured collected GIDL',
                           '233K model validity, outer-drain boundary attribution, and mesh convergence unverified',
                           'No 1T1C retention simulated'],
            'sources':sorted(set(str(r.get('source_project','')) for r in records)),
            'cross_project_geometry_equivalence':'REQUIRES INDEPENDENT PHYSICAL DECK REVIEW'}
    (out/'EXTRACTION_STATUS.json').write_text(json.dumps(status,indent=2)+'\n',encoding='utf-8')
    (out/'README_REVIEW.txt').write_text(
        'CMP 3D MEB x Temperature extraction with INCOMPLETE native SDevice cases.\n'
        'See INCOMPLETE_CASES.csv for exact temperature/depth/mode, achieved voltage and reason.\n'
        'Only available fully endpoint-QC-passed data go into target-bias metrics/ROI.\n'
        'Never call a -0.6637 V terminal current the -0.7 V GIDL result.\n'
        'Existing successful cases were reused without re-running SDevice or modifying SWB.\n'
        '300 K historical data require cross-project physical-deck equivalence check.\n',
        encoding='utf-8')
    zpath=out/'CMP_3D_MEB_TEMP140_PARTIAL_REVIEW.zip'
    if zpath.exists():zpath.unlink()
    with zipfile.ZipFile(zpath,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(out.rglob('*')):
            if p.is_file() and p!=zpath and p.suffix.lower() not in ('.tdr','.plt'):
                z.write(p,p.relative_to(out).as_posix())
    with zipfile.ZipFile(zpath) as z:
        bad=z.testzip()
    if bad:raise RuntimeError('Partial ZIP CRC failed: '+bad)
    print(f'PARTIAL_EXTRACTION_QC {len(terms)}/140 complete; '
          f'{len(failed)} incomplete; {len(sp)} valid ROI; {status["cutline_files"]} cutlines',flush=True)
    for err in failed:
        print(f'NEEDS_NATIVE_SDEVICE_REVIEW DBCAT={err["DBCAT_nm"]} T={err["TempK"]} '
              f'mode={err["RunMode"]} node={err["SDevice_node"]} '
              f'actualVg={err["last_Vg_V"]} targetVg={err["target_Vg_V"]}',flush=True)
    print('PARTIAL_REVIEW_ZIP',zpath,flush=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--project',type=Path,required=True,help='SWB temperature project (e.g. 233/340/380 K)')
    ap.add_argument('--baseline-project',type=Path,help='Optional separate original 300-K SWB project; supplies only missing 300-K cases')
    ap.add_argument('--out',type=Path,required=True,help='Dedicated output directory outside source project')
    ap.add_argument('--run',action='store_true',help='Run read-only SVisual extraction of all 140 cases')
    ap.add_argument('--resume',action='store_true',help='Reuse previously QC-complete per-case extracts after interruptions')
    ap.add_argument('--svisual-bin',default='svisual',help='SVisual batch binary name or absolute path')
    ap.add_argument('--no-cutlines',action='store_true',help='Skip 4 cutlines/case (exploratory; not full equivalent)')
    ap.add_argument('--continue-on-incomplete',action='store_true',help='Continue after numerical endpoint/threshold omissions; report partial results, NEVER fabricate target bias')
    args=ap.parse_args()
    project=args.project.resolve();out=args.out.resolve()
    baseline=args.baseline_project.resolve() if args.baseline_project else None
    if not project.is_dir():ap.error('SWB project directory missing: '+str(project))
    if baseline is not None and not baseline.is_dir():ap.error('Baseline project directory missing: '+str(baseline))
    if baseline == project:ap.error('--baseline-project must be distinct from --project')
    for src in (project, baseline):
        if src is not None and (out==src or src in out.parents or out in src.parents):
            ap.error('--out must be outside both SWB source projects (and not their ancestor)')
    if out.exists() and any(out.iterdir()) and args.run and not args.resume:
        ap.error('Output exists. Use --resume to safely continue from preflight or interrupted extraction.')
    if out.exists() and any(out.iterdir()) and not args.resume and not args.run:
        ap.error('Output exists. Use --resume for repeated preflight.')
    records,qc=discover_combined(project,baseline)
    out.mkdir(parents=True,exist_ok=True)
    if args.resume and (out/'SOURCE_MAPPING_140.csv').is_file():
        prior=readcsv(out/'SOURCE_MAPPING_140.csv')
        old={(str(r['DBCAT_nm']),str(r['TempK']),str(r['RunMode'])):(r['PP_SHA256'],r['SDE_PP_SHA256'],r['TDR_size_bytes'],r['PLT_size_bytes']) for r in prior}
        new={(str(r['DBCAT_nm']),str(r['TempK']),str(r['RunMode'])):tuple(str(r[k]) for k in ('PP_SHA256','SDE_PP_SHA256','TDR_size_bytes','PLT_size_bytes')) for r in records}
        if old!=new:ap.error('Mapping/source provenance changed since prior run. Use a NEW output directory; existing results kept intact.')
    cols=list(records[0]) if records else ['DBCAT_nm','TempK','RunMode']
    writecsv(out/'SOURCE_MAPPING_140.csv',records,cols)
    (out/'SOURCE_QC.json').write_text(json.dumps(qc,indent=2)+'\n',encoding='utf-8')
    print('SOURCE_QC',json.dumps({'expected_cases':140,'found_cases':qc['found_cases'],'valid':qc['valid'],
                                   'blocked_count':len(qc['blocked']),'missing_count':len(qc['missing']),
                                   'sources':qc.get('sources',[])}),flush=True)
    if not qc['valid']:
        print('BLOCKED: Inspect '+str(out/'SOURCE_QC.json')+'; no guessed/partial extraction',file=sys.stderr)
        return 3
    if not args.run:
        print('DRY_RUN: 140/140 mapping PASS; no SVisual calls made.')
        return 0
    if not shutil.which(args.svisual_bin):ap.error('svisual not found: '+args.svisual_bin)
    for folder in ['DC_curves','SPATIAL_cutlines','SVisual_scripts','logs','PP_DECKS','CASE_DONE']:
        (out/folder).mkdir(exist_ok=True)
    try:
        incomplete={}
        for i,r in enumerate(records,1):
            print(f'CASE {i}/140 {label(r)}',flush=True)
            try:
                extract_case(r,out,args)
            except ValueError as e:
                message=str(e)
                explicitly_incomplete=(message.startswith('Endpoint not reached:') or
                                       message.startswith('Constant-current threshold not reached') or
                                       message.startswith('No Vg ramp samples'))
                if not (args.continue_on_incomplete and explicitly_incomplete):
                    raise
                issue=partial_curve_issue(out,r,message)
                incomplete[(int(r['DBCAT_nm']),int(r['TempK']),int(r['RunMode']))]=issue
                print('INCOMPLETE (native SDevice data; not treated as target-bias result)',
                      label(r),message,flush=True)
        if incomplete:
            package_partial(out,records,args,incomplete)
        else:
            package(out,records,args)
    except Exception as e:
        print('EXTRACTION_FAILED:',str(e),file=sys.stderr)
        print('SAFE_TO_RESUME: inspect case errors; --resume preserves valid completed cases',file=sys.stderr)
        return 4
    return 0

if __name__=='__main__':sys.exit(main())
