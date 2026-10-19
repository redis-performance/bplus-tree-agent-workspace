set -eu
cd @REPO@
python3 - <<'PY'
import subprocess,hashlib,json
from pathlib import Path
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode');rows={}
for v in ['base','root','A','B','C']:
 rows[v]={}
 for section in ['.text','.rodata']:
  dest=Path('scratch')/('arm-linked-'+v+section)
  subprocess.run(['objcopy','--dump-section',section+'='+str(dest),str(p/'build-long'/v/'decoder-native')],check=True)
  rows[v][section]={'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'bytes':dest.stat().st_size}
(p/'codegen/linked-sections.json').write_text(json.dumps(rows,indent=2)+'\n')
PY
