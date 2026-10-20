#!/usr/bin/env bash
# Exact isolated ON/OFF launcher from the user-executed 2026-10-21 control.
set -euo pipefail
if [[ $# -ne 2 ]]; then echo 'Usage: bash run_one_case.sh /path/to/CMP_3D_HURKX_AB_20261021_RUN ON|OFF' >&2; exit 2; fi
OUT="$(cd "$1" && pwd)"; CASE="$2"
[[ "$CASE" == ON || "$CASE" == OFF ]] || { echo 'CASE must be ON or OFF' >&2; exit 2; }
WORK="$OUT/$CASE"
[[ -s "$OUT/manifest.json" && -s "$WORK/cmp_highneg.cmd" ]] || { echo 'Prepare step not complete' >&2; exit 2; }
[[ ! -e "$WORK/run_stdout.log" ]] || { echo "REFUSING re-run: $WORK/run_stdout.log already exists" >&2; exit 2; }
command -v sdevice >/dev/null || { echo 'sdevice command not in PATH' >&2; exit 127; }
echo "Starting a real SDevice $CASE control in isolated directory: $WORK"
echo 'This runs FULL inherited HIGHNEG ramp to Vg=-1.0; check license/solver and endpoint.'
cd "$WORK"
set +e
sdevice cmp_highneg.cmd 2>&1 | tee run_stdout.log
status=${PIPESTATUS[0]}
set -e
printf 'sdevice_exit_status=%s\n' "$status" > run_exit_status.txt
exit "$status"
