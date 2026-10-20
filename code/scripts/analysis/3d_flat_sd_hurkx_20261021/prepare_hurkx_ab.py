#!/usr/bin/env python3
"""Prepare isolated Hurkx ON/OFF native SDevice controls from executed PP CMD.
Python 3.8+; no simulation launched, and never edits the SWB project.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path('/user2/cmp/cmp212')
MODEL_ONLY = re.compile(
    r'\bRecombination\s*\(\s*Band2Band\s*\(\s*'
    r'(?:Hurkx|Model\s*=\s*Hurkx)\s*\)\s*\)', re.I | re.S)
GRID_RX = re.compile(r'\bGrid\s*=\s*"([^"\r\n]+)"', re.I)
FILE_FIELDS = ('Current', 'Plot', 'Output')
VOLTAGE_RX = lambda contact, value: re.compile(
    r'Goal\s*\{\s*Name\s*=\s*["\']?' + re.escape(contact) +
    r'["\']?\s+Voltage\s*=\s*' + re.escape(str(value)) +
    r'(?:\s|\})', re.I | re.S)

def sha256(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def cmd_candidates(project, node=47):
    ps = [p for p in project.rglob('*.cmd') if p.is_file()]
    def score(p):
        nm = p.name.lower()
        if nm == 'pp%d_des.cmd' % node: return 0
        if nm == 'n%d_des.cmd' % node: return 1
        if re.match(r'(?:pp|n)%d[_-].*des.*\.cmd$' % node, nm): return 2
        return 10
    return sorted([p for p in ps if score(p) < 10], key=lambda p: (score(p), str(p)))

def check_parent(text, expected_grid='n41_msh.tdr'):
    problems = []
    grid_m = GRID_RX.search(text)
    if not grid_m:
        problems.append('No parseable Grid="..." declaration')
    else:
        actual = Path(grid_m.group(1)).name
        if actual != expected_grid:
            problems.append('Grid mismatch: %s (expected %s)' % (actual, expected_grid))
    if len(MODEL_ONLY.findall(text)) != 1:
        problems.append('Must have EXACTLY ONE Recombination(Band2Band(Hurkx)) ONLY-model statement; mixed sections require manual audit')
    bb_occurrences = len(re.findall(r'\bBand2Band\s*\(', text, re.I))
    if bb_occurrences != 1:
        problems.append('Found %d Band2Band(...) model invocations; expected 1' % bb_occurrences)
    for token in ('source', 'drain', 'gate', 'substrate'):
        if not re.search(r'\bName\s*=\s*["\']?' + token + r'["\']?', text, re.I):
            problems.append('Electrode %s not found' % token)
    if not re.search(r'\bTemperature\s*=\s*300(?:\D|$)', text, re.I):
        problems.append('Expected Temperature=300 not found')
    if not re.search(r'\bWorkfunction\s*=\s*4\.8(?:\D|$)', text, re.I):
        problems.append('Expected Workfunction=4.8 not found')
    for contact, v in [('drain', '1.2'), ('gate', '-1.0')]:
        if not VOLTAGE_RX(contact, v).search(text):
            problems.append('Expected %s ramp Goal=%s not found' % (contact, v))
    if 'Band2BandGeneration' not in text:
        problems.append('Plot Band2BandGeneration not found')
    if re.search(r'@\w+@', text):
        problems.append('Unresolved SWB @placeholder@ detected')
    if re.search(r'^\s*#include\b', text, re.I | re.M):
        problems.append('SDevice #include present: external dependency path audit required')
    for field in FILE_FIELDS:
        matches = re.findall(r'\b'+field+r'\s*=\s*"([^"\n]+)"', text, re.I)
        if not matches:
            problems.append('File %s="..." missing' % field)
        for path in matches:
            if Path(path).is_absolute():
                problems.append('Absolute %s path may overwrite original: %s' % (field, path))
    for x in re.findall(r'\bFilePrefix\s*=\s*"([^"\n]+)"', text, re.I):
        if Path(x).is_absolute():
            problems.append('Absolute FilePrefix may overwrite original: %s' % x)
    return grid_m, problems

def contact_audit(project, base, out):
    """Identify executed source and print evidence; not face adjacency proof."""
    candidates=[]
    for p in project.rglob('*.cmd'):
        name=p.name.lower()
        if re.match(r'(?:pp|n)41_(?:dvs|sde|.*sde).*\.cmd$',name):
            candidates.append(p)
    candidates.sort(key=lambda p: (not p.name.lower().startswith('pp41_'),str(p)))
    result={'pp_sde_candidates':[str(p) for p in candidates], 'pp_sde_selected':None,
            'drain_contact_probe_um':'(Xhalf,0,-0.025) um',
            'expected_x_half_um':0.060,
            'sde_contact_qa':'NOT_VERIFIED: face extent/adjacency requires native executed boundary/contact inspection'}
    if candidates:
        p=candidates[0]
        t=p.read_text(encoding='utf-8',errors='replace')
        result['pp_sde_selected']=str(p)
        result['pp_sde_sha256']=sha256(p)
        result['found_probe']=bool(re.search(r'\(define\s+P\.Drain\s*\(position\s+Xhalf\s+0(?:\.0+)?\s+-0\.025\s*\)\s*\)',t,re.S))
        result['found_assignment']=bool(re.search(r'\(sdegeo:set-contact\s+\(find-face-id\s+P\.Drain\)\s+"drain"\s*\)',t,re.S))
        result['found_Xhalf_60nm']=bool(re.search(r'\(define\s+Xhalf\s+0\.0?60\s*\)',t))
        if all(result.get(z,False) for z in ('found_probe','found_assignment','found_Xhalf_60nm')):
            result['sde_contact_qa']='CODE_GEOMETRY_CONFIRMED_ONLY: x=60 nm face probe at z=-25 nm; actual face extent unverified'
        else:
            result['sde_contact_qa']='PP_SDE_MISMATCH_OR_UNEXPANDED: inspect PP-CMD and face ID before geometry claim'
    (out/'contact_audit.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return result

def prepare(base, project, out):
    project = Path(project).expanduser().resolve()
    base = Path(base).expanduser().resolve()
    out = Path(out).expanduser().resolve()
    if not project.is_dir(): raise ValueError('Project not found: %s' % project)
    if out.exists(): raise ValueError('Refusing to overwrite existing output: %s' % out)
    if out == project or project in out.parents:
        raise ValueError('Output must be OUTSIDE original SWB project')
    cand=cmd_candidates(project)
    if not cand: raise ValueError('Cannot find pp47_des.cmd/n47_des.cmd.')
    source=cand[0]
    src=source.read_text(encoding='utf-8',errors='replace')
    grid_m, problems=check_parent(src)
    grid_path=None
    if grid_m:
        specified=Path(grid_m.group(1))
        if specified.is_absolute():
            gp=specified
        else:
            gp=project/specified
            if not gp.is_file():
                matches=list(project.rglob(specified.name))
                if len(matches)==1: gp=matches[0]
                elif len(matches)>1: problems.append('Multiple possible meshes: '+ ', '.join(str(x) for x in matches))
        if gp.is_file(): grid_path=gp.resolve()
        else: problems.append('Grid TDR missing: %s' % gp)
    if problems:
        raise ValueError('PRE-FLIGHT BLOCKED:\n - '+'\n - '.join(problems))
    common=src[:grid_m.start(1)] + str(grid_path) + src[grid_m.end(1):]
    off,n=MODEL_ONLY.subn('',common)
    if n!=1 or MODEL_ONLY.sub('',common)!=off:
        raise ValueError('Model removal failed or OFF diff exceeds single model statement')
    out.mkdir(parents=True)
    ct=contact_audit(project,base,out)
    for case, content in [('ON',common),('OFF',off)]:
        target=out/case
        target.mkdir()
        (target/'cmp_highneg.cmd').write_text(content,encoding='utf-8')
    original_snapshot=project/'n47_QC_D2_NEG_VG_0002_des.tdr'
    doc={
        'created_utc':datetime.now(timezone.utc).isoformat(),
        'lineage':'3D-Sun-SADDLE-V1 Flat upper S/D, provisional',
        'project':str(project),'sdevice_source':str(source),
        'source_sha256':sha256(source),'candidates':[str(p) for p in cand],
        'mesh_A':str(grid_path),'mesh_sha256':sha256(grid_path),
        'original_ON_TDR':str(original_snapshot) if original_snapshot.is_file() else None,
        'ON_output_cmd_sha256':sha256(out/'ON'/'cmp_highneg.cmd'),
        'OFF_output_cmd_sha256':sha256(out/'OFF'/'cmp_highneg.cmd'),
        'only_physics_edit':'remove one standalone Recombination(Band2Band(Hurkx)) clause in OFF',
        'nonphysics_edit':'File Grid path relocated to exact verified absolute original n41_msh.tdr',
        'bias_target':'Vd=1.2V, Vg=-1.0V','temperature_K':300,
        'status':'PREPARED_ONLY_NOT_EXECUTED','contact_code_status':ct['sde_contact_qa']}
    (out/'manifest.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PREPARED: %s' % out)
    print('SOURCE: %s' % source)
    print('MESH A: %s' % grid_path)
    print('MODEL: ON original Hurkx / OFF exactly one Recombination(Band2Band(Hurkx)) removed')
    print('SDE CONTACT: %s' % ct['sde_contact_qa'])
    print('NO SOLVER RUN; NO ORIGINAL SWB FILE CHANGED')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--base',default=str(ROOT))
    ap.add_argument('--project',default=str(ROOT/'B0_3D_highneg'))
    ap.add_argument('--out',default=str(ROOT/'CMP_3D_HURKX_AB_20261021_RUN'))
    args=ap.parse_args()
    try: prepare(args.base,args.project,args.out)
    except (OSError,ValueError) as exc: ap.exit(2,'BLOCKED: %s\n' % exc)

if __name__=='__main__': main()
