#!/usr/bin/env python3
"""CMP 3D full existing-results extraction v4; Python 3.8+, read-only SWB inputs. Modes 0..6, source traceability.

Source: main AGENTS/HANDOFF 2026-10-25, SVisual T-2022.03 pp. 224,229,249,254,296.
Patch after T-2022.03 logs: create a 3D plot before create_field; preserve the real SVisual smoke gate.
Use --run to invoke installed svisual -batch; otherwise safe dry-run discovery only.
"""
import argparse, csv, hashlib, json, re, shutil, subprocess, sys, tempfile, zipfile
from datetime import datetime, timezone
from pathlib import Path

MODES={0:'IDVG_LOW',1:'IDVG_HIGH',2:'IDVD_VG0p1',3:'IDVD_VG0p6',4:'IDVD_VG1p2',5:'GIDL_HURKX_ON',6:'GIDL_HURKX_OFF'}
ROI={'GATE_DRAIN':(.015,.030), 'MID_DRAIN':(.030,.045), 'OUTER_DRAIN':(.045,.060)}
Q=1.602176634e-19
# Full y/z window is intentionally wider than nominal 3D Silicon. Unit: micrometers.
YMIN,YMAX,ZMIN,ZMAX=-.200,.200,-.200,.200
GRID_RE=re.compile(r'\bGrid\s*=\s*["\']?([^"\'\s}\r\n]+)',re.I)
PLOT_RE=re.compile(r'\bPlot\s*=\s*["\']([^"\']+)["\']',re.I)
HURKX_RE=re.compile(r'\bBand2Band\s*\(\s*(?:Model\s*=\s*)?Hurkx\s*\)',re.I)

def node(depth,mode):
    return 2*depth+2 if mode==0 else 100+depth+25*(mode-1)

def sha256(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def q(s):
    return '{'+str(s).replace('\\','/').replace('}','\\}')+'}'

def writecsv(path, rows, names):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=names,extrasaction='ignore');w.writeheader();w.writerows(rows)

def tcl_script(tdr, dest, depth,mode,n, do_lines):
    # The only writes by this script are within dest (a newly created output directory).
    # No interaction with source SWB/project files beyond load_file.
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
        # SVisual Tcl-Library 2022.03: load_file return is not always a valid geometry
        # dataset handle for multi-geometry/state TDR. Resolve actual loaded 3D datasets.
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
        '# A TDR may contain multiple geometries/states; never silently choose one.',
        '# Multiple eligible datasets are logged and cause a guarded exit.',
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
        for metric,field in [ ('G_BTBT_SIGNED_integral_per_s','Band2BandGeneration'),('G_BTBT_POS_integral_per_s','CMP_BTBT_POS'),('G_BTBT_NEG_integral_per_s','CMP_BTBT_NEG'),('Si_volume_um3','__DOMAIN__')]:
            if field=='__DOMAIN__':
                lines.extend([
                    'if {[catch {set v [integrate_field -plot $plot -field Band2BandGeneration -materials {Silicon} -window $win -returndomain]} err]} {',
                    '  puts stderr "CMP_VOLUME_ERROR depth=%d mode=%d node=%d roi=%s : $err"'%(depth,mode,n,name),
                    '  emit $rawout %d %d %d %s Si_volume_um3 "" {} ERROR'%(depth,mode,n,name),
                    '} else {emit $rawout %d %d %d %s Si_volume_um3 $v {} OK}'%(depth,mode,n,name)
                ])
            else:
                lines.append('record_integral $rawout $plot %d %d %d %s %s %s $win'%(depth,mode,n,name,metric,field))
        # Max E and BTBT spatial coordinates per identical ROI, including full Silicon.
        for metric,field in [('EABS_max_V_per_cm','Abs(ElectricField-V)'),('G_BTBT_max_per_cm3_s','Band2BandGeneration'),('G_BTBT_POS_max_per_cm3_s','CMP_BTBT_POS')]:
            lines.append('record_max $rawout $plot %d %d %d %s %s {%s} %.6f %.6f'%(depth,mode,n,name,metric,field,xa,xb))
    if do_lines:
        # Four matched cutlines from every mode: x=10..60 nm; y=0/7.5nm; z=-48/-25nm.
        # These are diagnostic and do not define an interface/contact by themselves.
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

def select_tdr(project,archives, d,m,n,pp_cmd):
    text='\n'.join(l for l in pp_cmd.read_text(encoding='utf-8',errors='replace').splitlines() if not l.lstrip().startswith(('*','#','//')))
    grid=GRID_RE.search(text)
    gd=2*d+1
    if not grid or re.search(r'n(\d+)_msh\.tdr',grid.group(1)) is None or int(re.search(r'n(\d+)_msh\.tdr',grid.group(1)).group(1)) !=gd:
        return None,'GRID_MISMATCH','',text
    pl=PLOT_RE.search(text)
    if not pl:return None,'NO_PLOT_DECLARATION','',text
    expected=Path(pl.group(1)).name
    if not expected or not expected.lower().endswith('.tdr'):return None,'BAD_PLOT_DECLARATION',expected,text
    if not re.match(r'^n%d(?:_|\.)'%n,expected):return None,'OUTPUT_NOT_NODE_NAMED',expected,text
    # Direct original SWB node-owned native final TDR: exact filename, never guessed from snapshots.
    candidates=[x for x in project.rglob(expected) if x.is_file() and x.name==expected and x.is_symlink()==False]
    if len(candidates)==1:return ('source',candidates[0]),'MATCH_SOURCE',expected,text
    if len(candidates)>1:return None,'AMBIGUOUS_SAME_NAME',expected,text
    # Fallback to immutable original collector archives; exact node section + basename required.
    if archives:
        zp=archives/('CMP_3D_24_48_TDR_DBCAT_%02d.zip'%d)
        if zp.exists():
            with zipfile.ZipFile(zp) as zz:
                hits=[i for i in zz.infolist() if (not i.is_dir()) and i.filename.rsplit('/',1)[-1]==expected and re.match(r'^nodes/n%d/'%n,i.filename)]
            if len(hits)==1:return ('archive',zp,hits[0].filename),'MATCH_ARCHIVE',expected,text
            if len(hits)>1:return None,'AMBIGUOUS_ARCHIVE',expected,text
    return None,'MISSING_FINAL_TDR',expected,text

def consolidate(out, records, spatial_rows):
    cols=['depth_nm','mode','node','roi','metric','value','x_um','y_um','z_um','status']
    writecsv(out/'SPATIAL_RAW_ALL.csv',spatial_rows,cols)
    by={}
    for r in spatial_rows:
        key=(r['depth_nm'],r['mode'],r['node'],r['roi'])
        if r['status']=='OK':by.setdefault(key,{})[r['metric']]=r
    summary=[]
    for (d,m,n,roi),vals in sorted(by.items(),key=lambda k:(int(k[0][0]),int(k[0][1]),k[0][3])):
        row={'DBCAT_nm':d,'RunMode':m,'node':n,'roi':roi}
        for k,v in vals.items():
            row[k]=v['value']
            if k in ('EABS_max_V_per_cm','G_BTBT_max_per_cm3_s','G_BTBT_POS_max_per_cm3_s'):
                for axis in 'xyz':row[k+'_'+axis+'_um']=v[axis+'_um']
        for k, newk in [('G_BTBT_SIGNED_integral_per_s','qG_signed_A'),('G_BTBT_POS_integral_per_s','qG_positive_A'),('G_BTBT_NEG_integral_per_s','qG_negative_A')]:
            try:row[newk]=float(row[k])*Q
            except (KeyError,ValueError,TypeError):row[newk]=''
        if row.get('qG_signed_A')!='' and row.get('qG_positive_A')!='' and row.get('qG_negative_A')!='':
            row['qG_pos_neg_identity_residual_A']=float(row['qG_signed_A'])-float(row['qG_positive_A'])-float(row['qG_negative_A'])
        summary.append(row)
    cols=['DBCAT_nm','RunMode','node','roi','Si_volume_um3','G_BTBT_SIGNED_integral_per_s','G_BTBT_POS_integral_per_s','G_BTBT_NEG_integral_per_s','qG_signed_A','qG_positive_A','qG_negative_A','qG_pos_neg_identity_residual_A','EABS_max_V_per_cm']
    for k in ['EABS_max_V_per_cm','G_BTBT_max_per_cm3_s','G_BTBT_POS_max_per_cm3_s']:
        cols.extend([k+'_'+a+'_um' for a in 'xyz'])
        if k not in cols:cols.append(k)
    writecsv(out/'SPATIAL_ROI_SUMMARY.csv',summary,cols)
    # Controlled ON-OFF spatial delta, not a terminal collection efficiency.
    a={(str(r['DBCAT_nm']),str(r['RunMode']),r['roi']):r for r in summary}
    delta=[]
    for d in range(24,49):
        for roi in list(ROI)+['FULL_SILICON']:
            on=a.get((str(d),'5',roi),{});off=a.get((str(d),'6',roi),{})
            rr={'DBCAT_nm':d,'roi':roi,'on_node':on.get('node',''),'off_node':off.get('node','')}
            for metric in ['qG_signed_A','qG_positive_A','qG_negative_A','EABS_max_V_per_cm','G_BTBT_POS_max_per_cm3_s']:
                try:
                    rr[metric+'_ON']=float(on[metric]);rr[metric+'_OFF']=float(off[metric]);rr[metric+'_ON_minus_OFF']=rr[metric+'_ON']-rr[metric+'_OFF']
                except(KeyError,ValueError,TypeError):rr[metric+'_ON']=rr[metric+'_OFF']=rr[metric+'_ON_minus_OFF']=''
            delta.append(rr)
    writecsv(out/'HURKX_SPATIAL_ON_OFF_DELTA.csv',delta,list(delta[0]))
    return len(summary)

def numerical_qc(rows, d, m):
    """Check signed/positive/negative generation identities and ROI extrema locations.

    3D SVisual runtime correctness still requires actual T-2022.03 server execution.
    """
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

def merge_terminal_and_spatial(out,collection):
    """Comparison table for 25 depths, preserving missing entries as blank."""
    terminal={}
    p=collection/'metrics'/'DBCAT_25DEPTH_SUMMARY_PROVISIONAL.csv'
    if p.exists():
        with p.open(encoding='utf-8-sig',newline='') as f:
            terminal={int(r['DBCAT_nm']):r for r in csv.DictReader(f)}
    spatial={}
    f=out/'SPATIAL_ROI_SUMMARY.csv'
    if f.exists():
        with f.open(encoding='utf-8-sig',newline='') as reader:
            for r in csv.DictReader(reader):spatial[(int(r['DBCAT_nm']),int(r['RunMode']),r['roi'])]=r
    rows=[]
    for d in range(24,49):
        base=terminal.get(d,{})
        row={'DBCAT_nm':d,'Vth_high_proxy_V':base.get('Vth_high_proxy_V',''),
             'DIBL_proxy_V_per_V':base.get('DIBL_proxy_V_per_V',''),
             'Ion_Vg1p2_A':base.get('Id_Vg1p2_Vd1p2_A',''),
             'Hurkx_terminal_ON_minus_OFF_A':base.get('Hurkx_ON_minus_OFF_A','')}
        for mode in [3,5,6]:
            for roi in list(ROI)+['FULL_SILICON']:
                rr=spatial.get((d,mode,roi),{})
                stem='M%d_%s_'%(mode,roi)
                for val in ['qG_signed_A','qG_positive_A','qG_negative_A','EABS_max_V_per_cm','EABS_max_V_per_cm_x_um','EABS_max_V_per_cm_y_um','EABS_max_V_per_cm_z_um','Si_volume_um3']:
                    row[stem+val]=rr.get(val,'')
        try:
            gate=float(row['M5_GATE_DRAIN_qG_positive_A'])
            outer=float(row['M5_OUTER_DRAIN_qG_positive_A'])
            mid=float(row['M5_MID_DRAIN_qG_positive_A'])
            row['M5_gate_positive_qG_fraction_threeROI']=gate/(gate+outer+mid) if gate+outer+mid else ''
        except(KeyError,ValueError):row['M5_gate_positive_qG_fraction_threeROI']=''
        rows.append(row)
    writecsv(out/'ALL25_TERMINAL_SPATIAL_COMBINED.csv',rows,list(rows[0]))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--project',type=Path,default=Path('/user2/cmp/cmp212/CMP_3D_COMPETITION_DBCAT24_48'))
    ap.add_argument('--collection',type=Path,default=Path('/user2/cmp/cmp212/CMP_DBCAT24_48_EXTRACT_20261029_153027'))
    ap.add_argument('--modes',default='all',help='all=every RunMode 0..6; or comma-separated modes (e.g. 5,6)')
    ap.add_argument('--out',type=Path,help='New output directory (never within the original SWB project)')
    ap.add_argument('--run',action='store_true',help='Invoke svisual -batch on selected final native TDR files')
    ap.add_argument('--svisual-bin',default='svisual')
    ap.add_argument('--no-cutlines',action='store_true')
    ap.add_argument('--limit',type=int,default=0,help='Debug: stop discovery after N cases')
    args=ap.parse_args()
    project=args.project.resolve(); collection=args.collection.resolve()
    if not project.is_dir():ap.error('SWB project missing: '+str(project))
    modes=sorted(MODES) if args.modes=='all' else sorted(set(int(x.strip()) for x in args.modes.split(',')))
    if not modes or any(x not in MODES for x in modes):ap.error('Invalid --modes')
    parent=project.parent
    out=(args.out.resolve() if args.out else parent/('CMP_SPATIAL_24_48_'+datetime.now().strftime('%Y%m%d_%H%M%S')))
    if out.exists():ap.error('Output already exists; no overwrite: '+str(out))
    if out==project or project in out.parents:ap.error('Output must be outside source Workbench project')
    if args.run and not shutil.which(args.svisual_bin):ap.error('svisual executable not available. Check Sentaurus environment.')
    out.mkdir(parents=True)
    (out/'case_logs').mkdir(); (out/'tcl_scripts').mkdir();(out/'cutlines').mkdir()
    records=[]; raw=[];cases=0
    for d in range(24,49):
        for m in modes:
            n=node(d,m)
            pp=[x for x in project.rglob('pp%d_des.cmd'%n) if x.is_file() and not x.is_symlink()]
            rr={'DBCAT_nm':d,'RunMode':m,'SDevice_node':n,'SDE_node':2*d+1,
                'PP_count':len(pp),'PP_path':'','PP_SHA256':'','expected_final_TDR':'','TDR_location':'','TDR_SHA256':'',
                'TDR_bytes':'','Hurkx':'','status':'','svisual_returncode':'','raw_record_count':0,'notes':''}
            if len(pp)!=1:rr['status']='MISSING_OR_AMBIGUOUS_PP';records.append(rr);continue
            rr['PP_path']=str(pp[0].relative_to(project))
            rr['PP_SHA256']=sha256(pp[0])
            deck_folder=out/'pp_decks'; deck_folder.mkdir(exist_ok=True)
            shutil.copyfile(pp[0],deck_folder/('DBCAT_%02d_mode%d_pp%d_des.cmd'%(d,m,n)))
            pick,status,basename,txt=select_tdr(project,collection/'archives',d,m,n,pp[0])
            rr['expected_final_TDR']=basename;rr['Hurkx']='ON' if HURKX_RE.search(txt) else 'OFF_OR_UNDETECTED'
            if (m==5 and rr['Hurkx']!='ON') or (m==6 and rr['Hurkx']=='ON'):
                rr['status']='PHYSICS_MISMATCH';rr['notes']='Expected mode 5 ON, mode 6 OFF; verify PP model differences';records.append(rr);continue
            if not pick:rr['status']=status;records.append(rr);continue
            rr['TDR_location']=str(pick[1])+((' :: '+pick[2]) if pick[0]=='archive' else '')
            folder=out/'cutlines'/('DBCAT_%02d'%d)/('mode%d'%m)
            folder.mkdir(parents=True,exist_ok=True)
            tdr=pick[1]
            if pick[0]=='archive':
                # Unpack only one node-verified final TDR to a temporary private location.
                cache=out/'_extracted_tdr';cache.mkdir(exist_ok=True)
                tdr=cache/('%d_mode%d_%s'%(d,m,basename))
                with zipfile.ZipFile(pick[1]) as zz:
                    with zz.open(pick[2]) as src,tdr.open('wb') as dst:shutil.copyfileobj(src,dst,1024*1024)
            rr['TDR_SHA256']=sha256(tdr);rr['TDR_bytes']=tdr.stat().st_size
            tcl=out/'tcl_scripts'/('DBCAT_%02d_mode%d_n%d.tcl'%(d,m,n))
            tcl.write_text(tcl_script(tdr,folder,d,m,n,not args.no_cutlines),encoding='utf-8')
            if args.run:
                log=out/'case_logs'/('DBCAT_%02d_mode%d_n%d.log'%(d,m,n))
                with log.open('w',encoding='utf-8') as f:
                    proc=subprocess.run([args.svisual_bin,'-batch',str(tcl)],cwd=str(out),stdout=f,stderr=subprocess.STDOUT,check=False)
                rr['svisual_returncode']=proc.returncode
                result=folder/'raw_rows.csv'
                if result.exists():
                    with result.open(encoding='utf-8',newline='') as f:
                        for row in csv.DictReader(f):
                            raw.append(row);rr['raw_record_count']+=1
                errors=[r for r in raw if r['depth_nm']==str(d) and r['mode']==str(m) and r['status']!='OK']
                cuts=list(folder.glob('line_*.csv'))
                cut_ok=args.no_cutlines or len(cuts)==4
                num_notes=numerical_qc(raw,d,m)
                rr['status']='EXPORTED' if proc.returncode==0 and rr['raw_record_count']==28 and not errors and cut_ok and not num_notes else 'PARTIAL_OR_FAILED'
                rr['notes']=';'.join(num_notes + ([] if cut_ok else ['CUTLINES_MISSING_%d_OF_4'%len(cuts)]))
            else:rr['status']='DRY_RUN_FOUND' if status=='MATCH_SOURCE' else 'DRY_RUN_FOUND_ARCHIVE'
            records.append(rr);cases+=1
            print('CASE DBCAT=%02d Mode=%d n%d: %s [%d/28 records]'%(d,m,n,rr['status'],rr['raw_record_count']),flush=True)
            if args.limit and cases>=args.limit:break
        if args.limit and cases>=args.limit:break
    names=list(records[0]) if records else []
    writecsv(out/'SPATIAL_CASE_QC.csv',records,names)
    cnt=consolidate(out,records,raw)
    merge_terminal_and_spatial(out,collection)
    # Delete only this script's temporary extracted TDRs, not originals/archive.
    shutil.rmtree(out/'_extracted_tdr',ignore_errors=True)
    status={'project':str(project),'collection':str(collection),'output':str(out),'timestamp_utc':datetime.now(timezone.utc).isoformat(),
            'default_modes':'all (explicit) or 3,5,6 (default)','requested_modes':modes,'cases_expected':(len(records) if args.limit else 25*len(modes)),
            'cases_pp_found':sum(r['PP_count']==1 for r in records),
            'cases_tdr_identified':sum(bool(r['TDR_SHA256']) for r in records),
            'cases_svisual_completed':sum(r['status']=='EXPORTED' for r in records),
            'cases_partial_or_failed':sum(r['status']=='PARTIAL_OR_FAILED' for r in records),
            'roi_records_summarized':cnt,'run_requested':args.run,
            'scientific_status':'PROVISIONAL; not pure terminal GIDL, not contact-independent hotspot, not retention or temperature',
            'native_originals_modified':False}
    (out/'COLLECTION_STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # Companion metadata: no binary 3D TDR included, kept on Linux in source/archive.
    (out/'READ_ME_FIRST.txt').write_text('CMP 3D spatial extraction T-2022.03. 1 um=1e-4 cm.\n'
      'Generation fields: cm^-3 s^-1; native SVisual Band2BandGeneration integrate_field already in [s^-1].\n'
      'Only CMP_BTBT_POS/NEG derived integrals are multiplied by 1e-12 to [s^-1]; qG_A = 1.602176634e-19 C * integral.\n'
      'E max V/cm; hotspot coordinates um. Gate x15..30nm, Mid 30..45nm, Outer 45..60nm; all material Silicon.\n'
      'ON-OFF differences are model sensitivity, not pure terminal-collected GIDL or retention.\n'
      'Outer contact/boundary Face91 spatial membership NOT independently proven.\n'
      'Check SPATIAL_CASE_QC.csv (EXPORTED), raw records and case_logs; dry-run is not extraction.\n',encoding='utf-8')
    # Include existing DC curve evidence from previous verified collection (small files only), for one upload.
    zpath=out/'CMP_ALL25_DC_GIDL_SPATIAL_REVIEW.zip'
    with zipfile.ZipFile(zpath,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as zz:
        for p in out.rglob('*'):
            if p.is_file() and p!=zpath and '_extracted_tdr' not in p.parts and p.suffix.lower() not in ('.tdr','.tcl'):
                zz.write(p,'SPATIAL/'+p.relative_to(out).as_posix())
        for rel in ['metrics','curves','RUN_MAPPING_QC.csv','WARNINGS.txt','COLLECTION_STATUS.json']:
            p=collection/rel
            if p.is_file():zz.write(p,'DC/'+rel)
            elif p.is_dir():
                for x in p.rglob('*'):
                    if x.is_file() and x.suffix.lower()=='.csv':zz.write(x,'DC/'+x.relative_to(collection).as_posix())
    print('RESULT',out)
    print('CASES',status['cases_tdr_identified'],'identified,',status['cases_svisual_completed'],'spatial data extracted of',status['cases_expected'])
    print('UPLOAD_ZIP',zpath)
    print('NOTES: Source SWB unchanged. This script does not execute SDevice or Cgd/temperature/1T1C simulations.')
    return 0 if not args.run or status['cases_svisual_completed']==status['cases_expected'] else 3

if __name__=='__main__':sys.exit(main())
