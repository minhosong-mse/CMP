#!/usr/bin/env python3
"""Prepare verified-source *review bundle* for eventual GitHub upload. No GitHub/network writes.
The original native TDR files and archives remain on the server; hashes/provenance are indexed.
"""
import argparse,csv,hashlib,json,zipfile
from pathlib import Path

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def read_rows(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--collection',required=True,type=Path)
    ap.add_argument('--spatial',required=True,type=Path)
    ap.add_argument('--terminal',required=True,type=Path)
    ap.add_argument('--out',type=Path,help='Path for ZIP output, default inside the spatial output')
    args=ap.parse_args()
    c=args.collection.resolve();s=args.spatial.resolve();t=args.terminal.resolve()
    qc=c/'RUN_MAPPING_QC.csv';ep=c/'metrics/RUNMODE_ENDPOINTS.csv';sqc=s/'SPATIAL_CASE_QC.csv';tqc=t/'TERMINAL_ALL175_QC_AND_DERIVATIVES.csv'
    for p in (qc,ep,sqc,tqc):
        if not p.is_file():ap.error('Required source missing: '+str(p))
    maps=read_rows(qc);ends=read_rows(ep);spatial=read_rows(sqc);terminal=read_rows(tqc)
    target={(d,m) for d in range(24,49) for m in range(7)}
    mapset={(int(r['dbcat_nm']),int(r['mode'])) for r in maps}
    epset={(int(r['DBCAT_nm']),int(r['RunMode'])) for r in ends if r.get('endpoint_reached')=='1'}
    spatset={(int(r['DBCAT_nm']),int(r['RunMode'])) for r in spatial if r.get('status')=='EXPORTED'}
    termset={(int(r['DBCAT_nm']),int(r['RunMode'])) for r in terminal if r.get('status')=='EXTRACTED'}
    good=(target==mapset==epset==spatset==termset)
    status={'schema_version':'CMP-FULL-EXTRACTION-V5-RECOVERED','expected_cases':175,
      'mapped':len(mapset&target),'terminal_csv_endpoints':len(epset&target),
      'terminal_detailed':len(termset&target),'spatial_qc_pass':len(spatset&target),
      'complete':good,'unverified_spatial_cases':sorted([f'{d}:{m}' for d,m in target-spatset]),
      'scientific_status':'Executed simulation evidence + spatial QC. Not paper-calibrated, mesh-converged, pure-terminal GIDL, Cgd, temperature or retention.'}
    out=(args.out.resolve() if args.out else s/'CMP_3D_ALL175_GITHUB_REVIEW.zip')
    if out.exists():ap.error('Output already exists: '+str(out))
    out.parent.mkdir(parents=True,exist_ok=True)
    manifest=[]
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        z.writestr('REVIEW_FIRST/status.json',json.dumps(status,indent=2)+'\n')
        z.writestr('REVIEW_FIRST/README.md',
          '# CMP 3D DBCAT 24–48 nm — extracted source evidence\n\n'
          'Independent 3D-Sun-SADDLE-V1/Flat-upper-SD lineage; 300 K; Lg20nm; Wfin17nm; Tox5nm; recess120nm; junction48nm; WF4.8eV, CurveGrid1.\n'
          'All numeric files are extracted from previously executed SWB nodes (RunMode 0–6); no SDevice simulation is performed.\n\n'
          '**Statuses:** 175/175 endpoints are required; spatial must also pass independently.\n'
          'ROI: Gate x15–30nm, Mid x30–45nm, Outer Drain x45–60nm and Full Silicon.\n'
          'Signed/positive/negative Band2BandGeneration q-integrals are generation equivalents, NOT pure collected GIDL.\n'
          'SVisual native Band2BandGeneration integral already in s^-1; only custom minmax positive/negative fields require x1e-12 before q.\n'
          'Boundary x≈60nm contact artifact requires independent audit. Original binary TDR/PLT retained outside GitHub, with SHA256.\n'
          'SDevice `Charge` is not a verified AC Cgd; gm/gds are finite-difference proxies. 3D temperature and 1T1C Retention not executed.\n'
          'DO NOT claim scientific freeze before source, bias and spatial QC reviewed.\n')
        def add(p,arc):
            if p.is_file():
                z.write(p,arc)
                manifest.append({'path':arc,'bytes':p.stat().st_size,'sha256':sha(p)})
        for rel in ['RUN_MAPPING_QC.csv','WARNINGS.txt','COLLECTION_STATUS.json','FILE_SHA256_MANIFEST.csv']:
            add(c/rel,'DC/'+rel)
        for base in ['metrics','curves']:
            for p in sorted((c/base).rglob('*.csv')):
                add(p,'DC/'+str(p.relative_to(c)))
        for p in sorted(t.glob('*')):
            if p.is_file():add(p,'TERMINAL_DERIVED/'+p.name)
        keep=['SPATIAL_CASE_QC.csv','SPATIAL_ROI_SUMMARY.csv','SPATIAL_RAW_ALL.csv',
              'HURKX_SPATIAL_ON_OFF_DELTA.csv','ALL25_TERMINAL_SPATIAL_COMBINED.csv',
              'COLLECTION_STATUS.json','READ_ME_FIRST.txt']
        for name in keep:add(s/name,'SPATIAL/'+name)
        # All cutlines and field inventories, one archive member per case/bias.
        for p in sorted((s/'cutlines').rglob('*.csv')):add(p,'SPATIAL/'+str(p.relative_to(s)))
        for p in sorted((s/'cutlines').rglob('field_inventory.txt')):add(p,'SPATIAL/'+str(p.relative_to(s)))
        for p in sorted((s/'pp_decks').glob('*.cmd')):add(p,'SOURCE_PP/'+p.name)
        for p in sorted((s/'case_logs').glob('*.log')):add(p,'LOGS/'+p.name)
        z.writestr('REVIEW_FIRST/FILE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
    print('GITHUB_REVIEW_ZIP',out)
    print('STATUS',json.dumps(status))
    print('REVIEW_ONLY: This step does NOT push to GitHub. Verify QC and obtain commit approval first.')
    return 0 if good else 3
if __name__=='__main__':raise SystemExit(main())
