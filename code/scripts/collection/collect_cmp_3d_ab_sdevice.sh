#!/usr/bin/env bash
# CMP 3D-Sun-SADDLE-V1 FLAT SD - collect 3 bias families x 2 CurveGrid results.
# Read-only: never changes SWB results. Python3 standard library only.
# Usage: bash collect_cmp_3d_ab_sdevice.sh [/user2/cmp/cmp212]
set -euo pipefail
BASE="${1:-/user2/cmp/cmp212}"
if [[ ! -d "$BASE" ]]; then
  echo "ERROR: SWB parent directory not found: $BASE" >&2
  exit 2
fi
python3 - "$BASE" <<'PY'
import csv, hashlib, io, re, sys, zipfile
from pathlib import Path
from datetime import datetime

base = Path(sys.argv[1]).expanduser().resolve()
projects = [('low', 'B0_3D_low'), ('highpos', 'B0_3D_highpos'), ('highneg', 'B0_3D_highneg')]
node_map = [(1, 41, 47), (2, 46, 48)]  # CurveGrid, SDE node, SDevice node
core_suffixes = {'.plt', '.log', '.cmd', '.out', '.err', '.csv', '.txt', '.prf', '.sta'}
spatial_suffixes = {'.tdr'}
excluded_dirs = {'.git', '__pycache__', '.svn'}
all_warnings = []
manifest_rows = []
run_rows = []
records = {}

for label, project in projects:
    root = base / project
    if not root.is_dir():
        print('ERROR: SWB project folder not found:', root, file=sys.stderr)
        sys.exit(3)
    found = []
    # SWB outputs may be in the project root or in per-node work directories.
    # Preserve relative paths so similarly named node files never collide.
    for p in root.rglob('*'):
        if not p.is_file() or p.is_symlink() or any(seg in excluded_dirs for seg in p.relative_to(root).parts):
            continue
        if p.suffix.lower() in core_suffixes | spatial_suffixes:
            found.append(p)
    found.sort(key=lambda p: str(p.relative_to(root)))
    records[label] = (root, found)
    core = [p for p in found if p.suffix.lower() in core_suffixes]
    tdr = [p for p in found if p.suffix.lower() in spatial_suffixes]
    print('%-8s core-files=%-5d TDR-files=%-5d %s' % (label, len(core), len(tdr), root))
    if not any(p.suffix.lower() == '.plt' for p in core):
        all_warnings.append('%s: No .plt found; check SDevice current output location' % label)
    if not tdr:
        all_warnings.append('%s: No .tdr found; cannot do spatial E/BTBT audit' % label)

    for cg, mesh, device in node_map:
        def owner_match(p, n):
            name = p.name.lower()
            return bool(re.match(r'(?:pp)?n?%d(?:_|\.|$)' % n, name)) or any(re.fullmatch(r'(?:n|node)?%d' % n, x.lower()) for x in p.relative_to(root).parts[:-1])
        owned = [p for p in core if owner_match(p, device)]
        cmds = [p for p in core if p.suffix.lower() == '.cmd' and owner_match(p, device) and 'des' in p.name.lower()]
        # Prefer executed SWB PP deck, not a user-authored template.
        cmds.sort(key=lambda p: (0 if p.name.lower().startswith('pp%d_des' % device) else 1,
                                 0 if p.name.lower().startswith('n%d_des' % device) else 1,
                                 len(p.parts)))
        cmd_file = cmds[0] if cmds else None
        grid = ''
        status = 'UNVERIFIED'
        if cmd_file:
            text = cmd_file.read_text(encoding='utf-8', errors='replace')
            # Strip whole-line comments before looking for File Grid declaration.
            text = '\n'.join(line for line in text.splitlines()
                             if not line.lstrip().startswith(('#', '*', '//')))
            m = re.search(r'(?im)\bGrid\s*=\s*["\']?([^"\'\s}]+)', text)
            if m:
                grid = m.group(1)
                status = 'MATCH' if re.search(r'(?<!\d)n%d_msh\.tdr\b' % mesh, grid, flags=re.I) else 'CHECK_GRID'
            if not grid:
                all_warnings.append('%s: n%d device CMD has no parseable File Grid declaration' % (label, device))
        else:
            all_warnings.append('%s: cannot find n%d executed SDevice CMD' % (label, device))
        if status == 'CHECK_GRID':
            all_warnings.append('%s: n%d Grid=%s (expected n%d_msh.tdr). Verify before A/B comparison.' % (label,device,grid,mesh))
        if not any(p.suffix.lower() == '.plt' for p in owned):
            all_warnings.append('%s: no clearly n%d-owned .plt; possible custom Current= prefix. All project PLTs are still included.' % (label,device))
        if not any(p.suffix.lower() == '.log' for p in owned):
            all_warnings.append('%s: no clearly n%d-owned .log; check job log output.' % (label,device))
        run_rows.append([project, cg, 'n%d' % mesh, 'n%d' % device,
                         str(cmd_file.relative_to(root)) if cmd_file else '', grid, status,
                         sum(p.suffix.lower() == '.plt' for p in owned),
                         sum(p.suffix.lower() == '.log' for p in owned)])

output_core = base / 'CMP_3D_AB_DC_CORE.zip'
output_tdr = {lab: base / ('CMP_3D_AB_SPATIAL_%s.zip' % lab.upper()) for lab, _ in projects}

def write_zip(path, wanted_suffixes, only_label=None, add_metadata=False):
    with zipfile.ZipFile(str(path), 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=4, allowZip64=True) as z:
        for label, project in projects:
            if only_label is not None and label != only_label:
                continue
            root, items = records[label]
            for p in items:
                if p.suffix.lower() not in wanted_suffixes:
                    continue
                rel = p.relative_to(root)
                name = '%s/%s' % (project, rel.as_posix())
                z.write(str(p), arcname=name)
                h = hashlib.sha256()
                with p.open('rb') as f:
                    for block in iter(lambda: f.read(1024 * 1024), b''):
                        h.update(block)
                manifest_rows.append([path.name, project, str(rel), p.stat().st_size, h.hexdigest()])
        if add_metadata:
            s = io.StringIO(); w = csv.writer(s)
            w.writerow(['project', 'CurveGrid', 'SDE_node', 'SDevice_node', 'preprocessed_or_executed_CMD', 'Grid_reference', 'grid_status', 'node_PLT_count', 'node_LOG_count'])
            w.writerows(run_rows)
            z.writestr('RUN_MAPPING.csv', s.getvalue().encode('utf-8-sig'))
            z.writestr('COLLECTOR_WARNINGS.txt', '\n'.join(all_warnings or ['No basic issues detected; numerical convergence still requires inspection.'])+'\n')
            z.writestr('README.txt',
                'CMP 3D FLAT-SD A/B SDevice output collector\n'
                'Projects: B0_3D_low / B0_3D_highpos / B0_3D_highneg\n'
                'For each project: CurveGrid 1: SDE n41 -> SDevice n47; CurveGrid 2: SDE n46 -> SDevice n48\n'
                'CORE ZIP: all .plt/.log/.cmd and lightweight text/status files per project.\n'
                'SPATIAL ZIPs: all .tdr files per project, including voltage snapshots and mesh when present.\n'
                'Check RUN_MAPPING.csv Grid_reference against expected SDE node; MATCH only validates the written Grid reference,\n'
                'not that the simulation numerically converged or E/BTBT data are physically correct.\n'
                'Project folder structure is preserved; unrelated preexisting project files may be included.\n')
    print('CREATED:', path, '(%.1f MiB)' % (path.stat().st_size / 1024**2))

write_zip(output_core, core_suffixes, add_metadata=True)
for label, _ in projects:
    write_zip(output_tdr[label], spatial_suffixes, only_label=label)

manifest_path = base / 'CMP_3D_AB_FILE_MANIFEST.csv'
with manifest_path.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['archive', 'project', 'relative_filename', 'bytes', 'sha256'])
    w.writerows(manifest_rows)
print('MANIFEST:', manifest_path)
print('\nGRID CHECK (from available CMD files):')
for row in run_rows:
    print('  %-17s CurveGrid=%s SDE=%s Device=%s Grid=%-24s %s' % (row[0],row[1],row[2],row[3],row[5] or '(unavailable)',row[6]))
if all_warnings:
    print('\nWARNINGS (also in CORE ZIP):')
    for warning in all_warnings:
        print('  -', warning)
    print('WARNING: no claims of valid A/B physics before reading logs and plots.')
print('\nUPLOAD: CORE ZIP first, then HIGHNEG SPATIAL ZIP, then HIGHPOS/LOW SPATIAL ZIPs.')
PY
