#!/usr/bin/env python3
"""Create an experiment skeleton without changing the experiment ledger."""
import argparse
from datetime import date
from pathlib import Path
import re

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("id")
p.add_argument("title")
a = p.parse_args()
if not re.fullmatch(r"EXP-[0-9]{3,}", a.id):
    p.error("id must be EXP-NNN")
root = Path(__file__).resolve().parent.parent
dest = root / "experiments" / a.id
dest.mkdir(exist_ok=False)
for name in ("proposals", "variants", "bench-results", "profile-results", "review"):
    (dest / name).mkdir()
    (dest / name / ".gitkeep").touch()
body = (root / "experiments/TEMPLATE.md").read_text()
body = body.replace("{ID}", a.id).replace("{TITLE}", a.title).replace("{DATE}", date.today().isoformat())
(dest / "README.md").write_text(body)
print(f"Created {a.id}; append a PLANNED entry to experiments/EXPERIMENTS.md.")
