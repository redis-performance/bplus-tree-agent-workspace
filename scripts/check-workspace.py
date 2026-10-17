#!/usr/bin/env python3
"""Check pinned support, optional pristine source, and local Markdown links."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--pristine-source", action="store_true")
a = p.parse_args()
root = Path(__file__).resolve().parent.parent
manifest = json.loads((root / "source-manifest.json").read_text())
errors = []
for entry in manifest["files"]:
    path = root / entry["path"]
    if entry["path"].startswith("src/") and not a.pristine_source:
        continue
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
        errors.append(f"Source hash mismatch: {entry['path']}")
for path in root.rglob("*.md"):
    relative = path.relative_to(root)
    if relative.parts[0] in {".git", "build", "worktrees", "scratch"}:
        continue
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
        if "://" in target or target.startswith("#"):
            continue
        target = unquote(target.split("#", 1)[0])
        if not (path.parent / target).exists():
            errors.append(f"Broken link in {relative}: {target}")
if errors:
    raise SystemExit("\n".join(errors))
print("Workspace links and pinned source/support hashes: PASS")
