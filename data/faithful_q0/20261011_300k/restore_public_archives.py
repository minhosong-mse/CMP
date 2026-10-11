#!/usr/bin/env python3
"""Reconstruct archived public CMP Faithful-Q0 source-evidence ZIPs without external dependencies.

Run: python3 data/faithful_q0/20261011_300k/restore_public_archives.py [OUTPUT_DIRECTORY]
Assembles numbered binary parts in Git and verifies SHA256 and resulting archive integrity.
The archived original user ZIPs have different hashes because public copies omit scheduler
intermediates and anonymize workspace metadata; see PUBLIC_ARCHIVES_MANIFEST.json.
"""
from pathlib import Path
import hashlib
import json
import sys
import zipfile

HERE = Path(__file__).resolve().parent

def restore(key: str, item: dict, output_dir: Path) -> Path:
    parts_dir = HERE / item["chunk_dir"]
    chunks = [parts_dir / f"part_{i:03d}.bin" for i in range(len(item["chunks"]))]
    missing = [str(p) for p in chunks if not p.is_file()]
    if missing:
        raise FileNotFoundError("Missing ZIP parts: " + ", ".join(missing))
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / item["public_filename"]
    digest = hashlib.sha256()
    with out.open("wb") as dest:
        for p in chunks:
            data = p.read_bytes()
            digest.update(data)
            dest.write(data)
    actual = digest.hexdigest()
    if actual != item["public_sha256"] or out.stat().st_size != item["public_size_bytes"]:
        out.unlink(missing_ok=True)
        raise ValueError(f"{key}: archive SHA/size failed. Got sha256={actual}")
    with zipfile.ZipFile(out) as z:
        if z.testzip() is not None:
            raise ValueError(f"{key}: ZIP CRC validation failed")
        if key != "plots_qc":
            assert "PUBLIC_MANIFEST.json" in z.namelist()
    print(f"VALIDATED {key}: {out} SHA256={actual}")
    return out

def main():
    with (HERE / "PUBLIC_ARCHIVES_MANIFEST.json").open(encoding="utf-8") as f:
        cfg = json.load(f)
    out_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE / "_restored_public_zips"
    for key in ("original_q0", "surface_l1", "plots_qc"):
        restore(key, cfg[key], out_dir)

if __name__ == "__main__":
    main()
