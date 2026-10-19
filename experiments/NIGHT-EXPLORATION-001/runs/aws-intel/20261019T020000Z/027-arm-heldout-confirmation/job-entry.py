#!/usr/bin/env python3
"""Read a separately sealed private launch configuration, without shell evaluation."""
import json
from pathlib import Path
import subprocess
import sys
here=Path(__file__).resolve().parent
phase=sys.argv[1]
if phase not in ('aa','confirmation'):raise SystemExit('invalid phase')
config=json.loads((here/(phase+'-job-config.json')).read_text())
keys=('lease','baseline_root','candidate_root','evidence_root','receipt','receipt_sha256','output')
if set(config)!=set(keys):raise SystemExit('wrong launch configuration keys')
command=[sys.executable,str(here/'run-phase.py'),'--phase',phase]
for key in keys:command.extend(['--'+key.replace('_','-'),str(config[key])])
raise SystemExit(subprocess.run(command,check=False).returncode)
