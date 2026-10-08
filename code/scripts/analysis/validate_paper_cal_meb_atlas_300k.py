#!/usr/bin/env python3
"""Independent validation and derived evidence for 2026-10-08 CMP MEB Atlas.
All input files are unchanged; never infer physics from input names alone.
"""
import csv, io, json, math, hashlib, zipfile, statistics, argparse
from pathlib import Path
from collections import defaultdict

parser = argparse.ArgumentParser(description='Audit CMP 300 K MEB Atlas CSV archive')
parser.add_argument('--archive', default='CMP_MEB_ATLAS_300K_EVIDENCE_PUBLIC.zip', help='300 K MEB evidence ZIP')
parser.add_argument('--out', default='CMP_300K_ATLAS_ANALYSIS', help='output directory')
args = parser.parse_args()
ZIP = Path(args.archive)
OUT = Path(args.out)
OUT.mkdir(parents=True, exist_ok=True)
MEBS = [31,33,36,39,41,42,43,44,45,46,47,48,49,50,51]
BRANCHES = {
 'DC005':('raw/MEB_DC_0.05','_meb_atlas_DC005_summary.csv'),
 'DC12':('raw/MEB_DC_1.2','_meb_atlas_DC12_summary.csv'),
 'CGD':('raw/MEB_Cgd','_meb_atlas_cgd_summary.csv'),
 'P2':('raw/MEB_GIDL','_p2_spatial_summary.csv'),
 'ON':('raw/MEB_GIDL','_btbt_on_terminal_summary.csv'),
 'OFF':('raw/MEB_BTBT_OFF','_btbt_off_terminal_summary.csv'),
}
Q = 1.602176634e-19
issues=[]; tests=[]

def check(cond, tag, warning=False):
    if cond:tests.append('PASS '+tag)
    else:
        issues.append(('WARNING ' if warning else 'FAIL ')+tag)

def close(a,b,abs_tol=1e-9,rel_tol=1e-7):
    return math.isclose(float(a),float(b),rel_tol=rel_tol,abs_tol=abs_tol)

with zipfile.ZipFile(ZIP) as z:
    members = z.namelist()
    check(len(members)==201,'ZIP entry count 201')
    check(not any(p.startswith('/') or '..' in Path(p).parts for p in members),'ZIP paths safe')
    meta=json.loads(z.read('metadata/run_metadata.json'))
    check(meta['MEB_nm']==MEBS,'metadata MEB matches selected 15')
    source_manifest=list(csv.DictReader(io.StringIO(z.read('metadata/source_manifest.csv').decode())))
    print('MANIFEST COLUMNS:',list(source_manifest[0]))
    for r in source_manifest:
        # sources should be unchanged: checksum validated against source paths inside zip
        path=r.get('archive_path') or r.get('zip_path') or r.get('stored_path')
        digest=r.get('sha256') or r.get('SHA256')
        if path and digest and path in members:
            check(hashlib.sha256(z.read(path)).hexdigest()==digest,'sha256 '+path)
    rows={}
    for group,(folder,suffix) in BRANCHES.items():
        hits=[n for n in members if n.startswith(folder+'/') and n.endswith(suffix)]
        check(len(hits)==15,group+' has 15 summary files')
        d={}
        for name in hits:
            data=list(csv.DictReader(io.StringIO(z.read(name).decode())))
            check(len(data)==1,'single summary row '+name)
            if not data: continue
            r=data[0]; m=int(round(float(r['MEB_nm'])))
            check(m not in d,group+' no repeated MEB '+str(m))
            d[m]=r
        check(sorted(d)==MEBS,group+' complete 15-point coverage')
        rows[group]=d

    all_rows=[]
    for m in MEBS:
        lo=rows['DC005'][m]; hi=rows['DC12'][m]; ac=rows['CGD'][m]; p=rows['P2'][m]; on=rows['ON'][m]; off=rows['OFF'][m]
        for group,r in [('ac',ac),('p',p),('on',on),('off',off)]:
            check(int(r['MeshLevel'])==2,group+str(m)+' Level2')
        check(close(lo['Vd_V'],0.05,abs_tol=1e-9),f'low DC Vd {m}')
        check(close(hi['Vd_V'],1.20,abs_tol=1e-9),f'high DC Vd {m}')
        for group,r in [('lo',lo),('hi',hi)]:
            check(int(r['BiasReached'])==1,group+str(m)+' BiasReached')
            check(int(r['VthReached'])==1,group+str(m)+' VthReached')
            check(int(r['Npts'])>=100,group+str(m)+' Npts')
        for group,r in [('on',on),('off',off),('p',p)]:
            check(int(r['EndpointReached'])==1,group+str(m)+' EndpointReached')
        check(int(ac['ACPointReached'])==1,f'AC point reached {m}')
        check(close(ac['Frequency_Hz'],1e6,abs_tol=0.01),f'AC frequency {m}')
        check(close(ac['Vd_V'],1.2,abs_tol=1e-5),f'AC drain {m}')
        check(close(ac['Vg_V'],-0.7,abs_tol=1e-5),f'AC gate {m}')
        for group,r in [('on',on),('off',off)]:
            check(r['Model']==group.upper(),f'{group} declared model {m}')
            check(close(r['VG_Final_V'],-0.7,abs_tol=1e-6),f'{group} gate {m}')
            check(close(r['VD_Final_V'],1.2,abs_tol=1e-6),f'{group} drain {m}')
            check(int(r['CurrentsAvailable'])==1,f'{group} currents {m}')
            check(float(r['KCL_Rel'])<1e-9,f'{group} KCL {m}')
            check(close(sum(float(r[k]) for k in ['Id_End_Signed_Aperum','Is_End_Signed_Aperum','Ig_End_Signed_Aperum','Ib_End_Signed_Aperum']),0.,abs_tol=1e-20),f'{group} KCL explicit {m}')
        check(float(ac['Reciprocity_pct']) < 0.01,f'Cgd reciprocity <0.01% {m}')
        check(close(p['GIDL_Aperum'],on['Id_End_Abs_Aperum'],rel_tol=1e-9,abs_tol=1e-20),f'GIDL spatial vs ON terminal {m}')
        check(close(p['Ycut_um'],0.252174,abs_tol=1e-7),f'fixed Y-cut {m}')
        check(0<=float(p['BTBT20_IntFrac'])<=1, f'BTBT active integral fraction range {m}')
        check(float(p['BTBT20_Area2D_raw'])>0, f'BTBT active area positive {m}')
        I_on=float(on['Id_End_Signed_Aperum']);I_off=float(off['Id_End_Signed_Aperum']);delta=I_on-I_off
        qg=Q*float(p['BTBT_Int2D_raw'])
        check(delta>0 and I_on>0 and I_off>0,f'signed currents ordered {m}')
        delta_err=100*(delta-qg)/qg
        check(abs(delta_err)<1.,f'ON-OFF vs q integral within 1% {m}')
        r={
           'MEB_nm':m,
           'Vth_005_V':float(lo['Vth_CC_V']),
           'Vth_12_V':float(hi['Vth_CC_V']),
           'DIBL_mV_per_V':(float(lo['Vth_CC_V'])-float(hi['Vth_CC_V']))/1.15*1000,
           'SSquick_005_mV_dec':float(lo['SSquick_mVdec']),
           'SSquick_12_mV_dec':float(hi['SSquick_mVdec']),
           'SS1dec_005_mV_dec':float(lo['SS1dec_mVdec']),
           'SS1dec_12_mV_dec':float(hi['SS1dec_mVdec']),
           'SS2dec_005_mV_dec':float(lo['SS2dec_mVdec']),
           'SS2dec_12_mV_dec':float(hi['SS2dec_mVdec']),
           'Id_12_Vg0_A_per_um':float(hi['Id_Vg0_Aperum']),
           'Ion_12_Vg1p2_A_per_um':float(hi['Id_Vg1p2_Aperum']),
           'Ion_12_Vg2_A_per_um':float(hi['Id_Vg2_Aperum']),
           'IonIoff_12_Vg1p2':float(hi['IonIoff_1p2']),
           'IonIoff_12_Vg2':float(hi['IonIoff_2p0']),
           'Cgd_abs':float(ac['Cgd_raw_abs']),
           'Cdg_abs':float(ac['Cdg_raw_abs']),
           'Cgd_reciprocity_pct':float(ac['Reciprocity_pct']),
           'Id_ON_signed_A_per_um':I_on,
           'Id_OFF_signed_A_per_um':I_off,
           'Hurkx_delta_A_per_um':delta,
           'Hurkx_sensitive_pct':100*delta/I_on,
           'qG_BTBT_A_per_um':qg,
           'Delta_vs_qG_err_pct':delta_err,
           'BTBT_int2D_s_inv_um_inv':float(p['BTBT_Int2D_raw']),
           'BTBTmax_cm3s':float(p['BTBTmax_Si']),
           'Xhot_um':float(p['Xhot_um']),
           'Yhot_um':float(p['Yhot_um']),
           'Ehot_at_BTBT_V_cm':float(p['Ehot_at_BTBT']),
           'BTBT20_area_um2':float(p['BTBT20_Area2D_raw']),
           'BTBT20_int_fraction':float(p['BTBT20_IntFrac']),
           'fixedY_um':float(p['Ycut_um']),
           'BTBT_fixedcut_capture_ratio':float(p['BTBTcut_to_global_ratio']),
           'BTBT_fixedcut_width20_nm':float(p['width_20_nm']),
           'intAbsE_fixedcut_20_V':float(p['intAbsE_20_V']),
           'intG_fixedcut_20_cm2s':float(p['intG_20_cm2s']),
           'intAbsE_fixedcut_full_V':float(p['intAbsE_full_V']),
           'intG_fixedcut_full_cm2s':float(p['intG_full_cm2s']),
           'KCL_ON_rel':float(on['KCL_Rel']),
           'KCL_OFF_rel':float(off['KCL_Rel']),
        }
        all_rows.append(r)

    provisional=list(csv.DictReader(io.StringIO(z.read('processed/MEB_300K_ATLAS_MASTER_PROVISIONAL.csv').decode())))
    check(len(provisional)==15,'collector provisional master 15 rows')
    max_ref_delta=0
    for old,new in zip(provisional,all_rows):
        for ok,nk in [('Id_ON_signed_A_per_um','Id_ON_signed_A_per_um'),('Id_OFF_signed_A_per_um','Id_OFF_signed_A_per_um'),('Cgd_raw_abs','Cgd_abs'),('BTBT_integral_s_inv_um_inv','BTBT_int2D_s_inv_um_inv'),('DIBL_mV_per_V','DIBL_mV_per_V')]:
            a=float(old[ok]);b=float(new[nk]); d=abs(a-b)/max(abs(a),abs(b),1e-30);max_ref_delta=max(max_ref_delta,d)
            check(d<1e-9,f'vs collector master {new["MEB_nm"]} {ok}')

assert not issues, '\n'.join(issues[:50])

# Output table, subset for plotting, audit logs.
master=OUT/'CMP_300K_MEB_ATLAS_MASTER_VALIDATED.csv'
with master.open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=list(all_rows[0]));writer.writeheader();writer.writerows(all_rows)
qcreport=OUT/'CMP_300K_ATLAS_QC_REPORT.txt'
qcreport.write_text('ZIP sha256: '+hashlib.sha256(ZIP.read_bytes()).hexdigest()+'\n'
    +'Input member count: '+str(len(members))+'\n'
    +'Input original CSV: 90 branch summaries + 105 curves (all preserved in uploaded ZIP)\n'
    +'Independent test count: '+str(len(tests))+'\n'
    +'All independent tests: PASS\n'
    +'Maximum independent master/collector relative deviation: '+str(max_ref_delta)+'\n'
    +'Largest absolute ΔI/qG error: '+str(max(abs(x['Delta_vs_qG_err_pct']) for x in all_rows))+'%\n'
    +'Largest Cgd reciprocity error: '+str(max(x['Cgd_reciprocity_pct'] for x in all_rows))+'%\n'
    +'Largest KCL relative error: '+str(max(max(x['KCL_ON_rel'],x['KCL_OFF_rel']) for x in all_rows))+'\n'
    +'Claim caveats: EXACT FZ-C deck bridge outstanding, 2D/3D equivalence not shown, 1T1C PAPER-CAL not executed.\n',encoding='utf-8')

report={
 'zip_sha256':hashlib.sha256(ZIP.read_bytes()).hexdigest(),
 'source_files':len(source_manifest),'zip_items':len(members),'summary_files':90,'curve_files':105,
 'independent_check_count':len(tests),'failures':len(issues),
 'master_max_rel_diff':max_ref_delta,
 'max_signed_delta_qG_err_pct':max(abs(x['Delta_vs_qG_err_pct']) for x in all_rows),
 'max_cgd_reciprocity_pct':max(x['Cgd_reciprocity_pct'] for x in all_rows),
 'max_KCL_rel':max(max(x['KCL_ON_rel'],x['KCL_OFF_rel']) for x in all_rows),
 'nominal': next(r for r in all_rows if r['MEB_nm']==36),
 'endpoints':{'31':all_rows[0],'39':all_rows[3],'41':all_rows[4],'48':all_rows[11],'51':all_rows[-1]},
}
(OUT/'CMP_300K_ANALYSIS_QC_SUMMARY.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')

# Metrics and scientific comparisons.
a=all_rows[0];b=all_rows[-1];nom=all_rows[2]
print('QC_PASS',len(tests),'checks; archive=',len(members),'rows=',len(all_rows),'max err ON-OFF qG=',report['max_signed_delta_qG_err_pct'])
print('31 -> 51 total-leak reduction x',a['Id_ON_signed_A_per_um']/b['Id_ON_signed_A_per_um'])
print('36 -> 51 total-leak reduction x',nom['Id_ON_signed_A_per_um']/b['Id_ON_signed_A_per_um'])
print('31 -> 51 Cgd reduction pct',100*(1-b['Cgd_abs']/a['Cgd_abs']))
print('36 -> 51 Cgd reduction pct',100*(1-b['Cgd_abs']/nom['Cgd_abs']))
for col in ['Ion_12_Vg1p2_A_per_um','Ion_12_Vg2_A_per_um','DIBL_mV_per_V','SSquick_12_mV_dec','Vth_12_V']:
 print(col,'31',a[col],'51',b[col],'pctchange',100*(b[col]/a[col]-1),'absolute',b[col]-a[col])
print('BTBT max at',max(all_rows,key=lambda r:r['BTBTmax_cm3s'])['MEB_nm'],'Ehot max at',max(all_rows,key=lambda r:r['Ehot_at_BTBT_V_cm'])['MEB_nm'])
print('Hurkx-sensitive fraction 31 36 39 41 48 51',[(x['MEB_nm'],round(x['Hurkx_sensitive_pct'],3)) for x in all_rows if x['MEB_nm'] in (31,36,39,41,48,51)])
print('31->39 OFF reduction x',all_rows[0]['Id_OFF_signed_A_per_um']/all_rows[3]['Id_OFF_signed_A_per_um'])
print('31->51 qG current %change',100*(b['Hurkx_delta_A_per_um']/a['Hurkx_delta_A_per_um']-1))
print('47->48,48->49,49->50,50->51 % GIDL benefit',[(all_rows[i]['MEB_nm'],all_rows[i+1]['MEB_nm'],100*(1-all_rows[i+1]['Id_ON_signed_A_per_um']/all_rows[i]['Id_ON_signed_A_per_um'])) for i in range(10,14)])
