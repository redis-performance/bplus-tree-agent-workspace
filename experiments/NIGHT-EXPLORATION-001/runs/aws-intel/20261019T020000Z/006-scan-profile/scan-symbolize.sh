set -eu
python3 - <<'PY'
from pathlib import Path
import json,subprocess
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/006-scan-profile');m=json.loads((p/'mapping-command.json').read_text());cmd=['llvm-symbolizer-18','--inlining','--output-style=JSON','--obj='+str(p/'build/profile')]+m['command'][7:]
# mapping command is addr2line -a -f -i -C -e BINARY ADDRESSES...
assert cmd[4].startswith('0x'),cmd
out=subprocess.check_output(cmd,text=True);(p/'llvm-inline-map.json').write_text(out);(p/'llvm-mapping-command.json').write_text(json.dumps({'command':cmd,'version':subprocess.check_output(['llvm-symbolizer-18','--version'],text=True)},indent=2)+'\n')
PY
