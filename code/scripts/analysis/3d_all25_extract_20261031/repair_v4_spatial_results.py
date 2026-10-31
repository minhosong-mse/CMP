#!/usr/bin/env python3
"""Recover 2026-10-31 V4 Sentaurus spatial CSV without any SVisual/SDevice run.

Native integrate_field(Band2BandGeneration) is already [s^-1]. V4 accidentally
multiplied it by 1e-12; user-derived POS/NEG fields were properly scaled.
This tool checks native SVisual log integrals and recomputes CSV/QC/summary.
"""
import argparse
import csv
import json
import math
import re
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from extract_cmp3d_spatial_all import consolidate, numerical_qc, merge_terminal_and_spatial

ROI = ('GATE_DRAIN', 'MID_DRAIN', 'OUTER_DRAIN', 'FULL_SILICON')
PAT = re.compile(r'DBCAT_(\d+)_mode(\d+)_n(\d+)\.log$')
LOG_UNIT = re.compile(r'Total Integral:\s*([-+0-9.eE]+)\s*\[s\^-1\]')


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fields):
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)


def verify_and_fix(source):
    assert (source/'SPATIAL_RAW_ALL.csv').is_file(), 'Missing raw file'
    assert (source/'SPATIAL_CASE_QC.csv').is_file(), 'Missing case QC'
    raw = read_csv(source/'SPATIAL_RAW_ALL.csv')
    qc = read_csv(source/'SPATIAL_CASE_QC.csv')
    expected = {(d,m) for d in range(24,49) for m in range(7)}
    assert len(qc) == 175 and {(int(r['DBCAT_nm']),int(r['RunMode'])) for r in qc}==expected, 'Case QC mapping wrong'
    assert len(raw)==4900, f'Expected 4900 raw rows; got {len(raw)}'
    counts=Counter((int(r['depth_nm']),int(r['mode'])) for r in raw)
    assert set(counts)==expected and set(counts.values())=={28}, 'Unexpected case/record-count mapping'
    assert all(r['status']=='OK' for r in raw), 'One or more SVisual raw records not OK'
    assert all(str(r['svisual_returncode'])=='0' for r in qc), 'SVisual process returned errors'
    assert all(r['raw_record_count']=='28' for r in qc), 'Incomplete record count'
    assert all(r['TDR_SHA256'] and r['PP_SHA256'] for r in qc), 'Source hash missing'
    before_counts=Counter(r['status'] for r in qc)
    assert before_counts==Counter({'EXPORTED':25,'PARTIAL_OR_FAILED':150}), f'Not the target V4 case set: {before_counts}'

    # Reconcile raw-v4 data to native integral values written by SVisual.
    # Each of 4 ROI windows has native signed integral once and again with
    # -returndomain: exactly eight [s^-1] values in the original SVisual log.
    signed={}
    for r in raw:
        if r['metric']=='G_BTBT_SIGNED_integral_per_s':
            key=(int(r['depth_nm']),int(r['mode']),r['roi'])
            assert key not in signed, 'duplicate signed integral '+str(key)
            old=float(r['value'])
            recovered=old*1e12
            assert math.isfinite(recovered), 'nonfinite signed '+str(key)
            r['value']=format(recovered,'.16g')
            signed[key]=recovered
    assert len(signed)==700, f'Signed integral records {len(signed)} !=700'
    native_checks=0
    cutline_log_count=0
    for r in qc:
        d,m,n=(int(r['DBCAT_nm']),int(r['RunMode']),int(r['SDevice_node']))
        f=source/'case_logs'/f'DBCAT_{d:02d}_mode{m}_n{n}.log'
        assert f.is_file(), 'Missing log '+str(f)
        s=f.read_text(encoding='utf-8',errors='replace')
        assert 'CMP_SPATIAL_TCL_DONE' in s and 'CMP_SELECTED_PLOT=' in s, 'SVisual log incomplete '+str(f)
        assert all(e not in s for e in ('CMP_CREATE_POS_ERROR','CMP_CREATE_NEG_ERROR','CMP_FIELD_ERROR','CMP_MAX_ERROR','CMP_CUTLINE_ERROR')), 'SVisual error '+str(f)
        count=s.count('CMP_CUTLINE_OK')
        assert count==4, f'Expected four successful cutline logs for {f}: {count}'
        cutline_log_count+=count
        vals=[float(z) for z in LOG_UNIT.findall(s)]
        assert len(vals)==8, f'Expected eight native [s^-1] log integrals for {f}: {len(vals)}'
        for i,roi in enumerate(ROI):
            a,b=vals[2*i:2*i+2]
            actual=signed[(d,m,roi)]
            assert math.isclose(a,b,rel_tol=1e-5,abs_tol=1e-40), f'Native double check mismatch {f} {roi}'
            assert math.isclose(actual,a,rel_tol=1e-5,abs_tol=1e-40), f'CSV/log [s^-1] mismatch {f} {roi}: {actual} vs {a}'
            native_checks+=1
    assert native_checks==700 and cutline_log_count==700
    for r in qc:
        notes=numerical_qc(raw,int(r['DBCAT_nm']),int(r['RunMode']))
        assert not notes, f'Uncorrected scientific QC d={r["DBCAT_nm"]} m={r["RunMode"]}: {notes}'
        r['status']='EXPORTED'
        r['notes']='V5_RECOVERED_FROM_V4_SIGNED_UNIT;NATIVE_LOG_VERIFIED'
    return raw, qc, before_counts, native_checks,cutline_log_count


def verify_saved_cutlines(source):
    """Check all 175 cases; distinguish 4 cutlines from the 5th raw_rows CSV.

    V4 writes one raw_rows.csv plus four line_*.csv files for each
    depth/mode case. Count and check these separately instead of counting
    every *.csv as a cutline. No existing result files are modified.
    """
    expected_cutline_names = {
        'line_y0p0_zm0p048.csv',
        'line_y0p0_zm0p025.csv',
        'line_y0p0075_zm0p048.csv',
        'line_y0p0075_zm0p025.csv',
    }
    base = source / 'cutlines'
    assert base.is_dir(), f'Missing cutlines folder: {base}'
    counts = {'cutline': 0, 'raw': 0, 'inventory': 0}
    for depth in range(24, 49):
        for mode in range(7):
            folder = base / f'DBCAT_{depth:02d}' / f'mode{mode}'
            assert folder.is_dir(), f'Missing per-case cutline folder: {folder}'
            line_files = sorted(folder.glob('line_*.csv'))
            actual_names = {f.name for f in line_files}
            assert actual_names == expected_cutline_names, (
                f'Expected 4 named cutlines in {folder}; got {sorted(actual_names)}'
            )
            raw = folder / 'raw_rows.csv'
            inventory = folder / 'field_inventory.txt'
            assert raw.is_file(), f'Missing per-case raw_rows.csv: {raw}'
            assert inventory.is_file(), f'Missing per-case field_inventory.txt: {inventory}'
            for f in (*line_files, raw, inventory):
                assert f.stat().st_size > 5, f'Empty cutline/raw/inventory: {f}'
            rows = read_csv(raw)
            assert len(rows) == 28, (
                f'Expected 28 SVisual spatial source records in {raw}, got {len(rows)}'
            )
            assert all(int(r['depth_nm']) == depth and int(r['mode']) == mode
                       and r['status'] == 'OK' for r in rows), (
                f'Unexpected case identity or source record status in {raw}'
            )
            counts['cutline'] += len(line_files)
            counts['raw'] += 1
            counts['inventory'] += 1
    assert counts == {'cutline': 700, 'raw': 175, 'inventory': 175}, counts
    print('CUTLINE_INVENTORY_PASS 700 line_*.csv + 175 raw_rows.csv + 175 field_inventory.txt')
    return counts['cutline'], counts['inventory']


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-spatial',type=Path,required=True,help='V4 spatial folder, e.g. ...ALL175/spatial')
    ap.add_argument('--terminal',type=Path,help='V4 terminal folder (default sibling of spatial)')
    ap.add_argument('--collection',type=Path,help='Existing original DC collection directory')
    ap.add_argument('--out',type=Path,help='NEW root folder, default source run folder name + _V5_RECOVERED')
    ap.add_argument('--diagnostic-only',action='store_true',help='Produce numerical QC only; cannot claim full cutline completeness or create review ZIP')
    args=ap.parse_args()
    source=args.source_spatial.resolve()
    assert source.is_dir(), 'Source spatial directory missing'
    raw,qc,original,checks,logs=verify_and_fix(source)
    if args.diagnostic_only:
        print('DIAGNOSTIC_OK numerical_QC=175/175 raw_records=4900 native_log_checks=700 cutline_log_success=700')
        print('DIAGNOSTIC_ONLY: no source mutation; cutline files and terminal source NOT checked, no review ZIP')
        return 0

    root=source.parent
    out=(args.out.resolve() if args.out else root.with_name(root.name+'_V5_RECOVERED'))
    assert not out.exists(), f'Output already exists; no overwrite: {out}'
    assert out!=root and root not in out.parents, 'Refuse destination within V4 original'
    terminal=(args.terminal.resolve() if args.terminal else root/'terminal')
    collection=(args.collection.resolve() if args.collection else Path(json.loads((source/'COLLECTION_STATUS.json').read_text())['collection']))
    assert terminal.is_dir(), 'Terminal folder missing: '+str(terminal)
    assert collection.is_dir(), 'Original collected results missing: '+str(collection)
    counts=verify_saved_cutlines(source)
    term_names=('TERMINAL_700_CONTACT_ENDPOINTS.csv','TERMINAL_ALL175_QC_AND_DERIVATIVES.csv',
                'TERMINAL_EXTRACTION_STATUS.json','TERMINAL_NATIVE_CSV_FIELD_INVENTORY.csv')
    for name in term_names:
        assert (terminal/name).is_file(), 'Missing terminal output '+name
    out.mkdir(parents=True)
    spa=out/'spatial';spa.mkdir()
    try:
        for dirname in ('cutlines','case_logs','pp_decks','tcl_scripts'):
            if (source/dirname).exists():shutil.copytree(source/dirname,spa/dirname)
        shutil.copytree(terminal,out/'terminal')
        n=consolidate(spa,qc,raw)
        assert n==700, f'Expected 700 ROI summary rows, got {n}'
        write_csv(spa/'SPATIAL_CASE_QC.csv',qc,list(qc[0]))
        merge_terminal_and_spatial(spa,collection)
        srcstatus=json.loads((source/'COLLECTION_STATUS.json').read_text(encoding='utf-8'))
        srcstatus.update({
            'output':str(spa),'timestamp_utc':datetime.now(timezone.utc).isoformat(),
            'cases_svisual_completed':175,'cases_partial_or_failed':0,
            'roi_records_summarized':700,
            'recovery_status':'V5 POSTPROCESS QC VERIFIED; no SVisual/SDevice rerun',
            'recovery_method':'Native Band2BandGeneration signed [s^-1] was erroneously multiplied by 1e-12 in V4. Multiplied ONLY signed CSV by 1e12; custom positive/negative unchanged.',
            'native_log_crosschecks':checks,'cutline_success_log_count':logs,
            'actual_cutline_csv_count':counts[0],'field_inventories':counts[1],
            'original_v4_spatial':str(source),
            'native_originals_modified':False,
            'scientific_status':'PROVISIONAL ROI/BTBT generation equivalents, not terminal-collected GIDL, contact-independent hot spot, mesh-converged, Cgd or retention'
        })
        (spa/'COLLECTION_STATUS.json').write_text(json.dumps(srcstatus,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        (spa/'READ_ME_FIRST.txt').write_text(
            'V5 RECOVERY from V4 executed logs; original source and original V4 remain unmodified.\n'
            'Original SVisual integrate_field Band2BandGeneration produced integral in s^-1.\n'
            'Only USER-DERIVED minmax CMP_BTBT_POS/NEG fields required factor 1e-12.\n'
            'V4 signed integral was multiplied by 1e-12 mistakenly; recover by multiplying signed CSV by 1e12.\n'
            'All 700 signed ROI results independently compared against native SVisual log [s^-1].\n'
            'All 175 scientific numerical QC passed; 700 original cutline CSV and 175 field inventories verified.\n'
            'Original saved V4 tcl_scripts are historical provenance and contain wrong signed unit conversion: DO NOT RERUN those scripts.\n'
            'This postprocessing does not execute Sentaurus. External drain contact/boundary issue unresolved.\n'
            'Generation qG in A is electron charge x volume generation rate, NOT pure collected GIDL.\n',encoding='utf-8')
        review=out/'CMP_3D_ALL175_GITHUB_REVIEW_V5_RECOVERED.zip'
        cmd=[sys.executable,str(Path(__file__).with_name('prepare_github_review.py')),
             '--collection',str(collection),'--spatial',str(spa),'--terminal',str(out/'terminal'),'--out',str(review)]
        rc=subprocess.call(cmd)
        if rc:raise RuntimeError('Review packaging failed; see logs in '+str(out))
        print('RECOVERY_PASS 175/175; 4900 raw records; 700 ROI; 700 native-integral comparisons; 700 Cutlines; 175 field inventories')
        print('ORIGINAL_UNCHANGED',root)
        print('RESULT',out)
        print('UPLOAD_FILE',review)
        print('GITHUB_STATUS not uploaded or committed; review ZIP only')
    except BaseException:
        print('INCOMPLETE_RECOVERY_FOLDER',out,'DO NOT UPLOAD OR COMMIT',file=sys.stderr)
        raise
    return 0

if __name__=='__main__':raise SystemExit(main())
