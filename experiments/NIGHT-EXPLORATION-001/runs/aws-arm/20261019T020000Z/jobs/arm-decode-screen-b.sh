set -eu
cd @REPO@
python3 - <<'VERIFY'
import hashlib,json
from pathlib import Path
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode')
for name,expected in json.load(open(p/'build-info/duration-hashes.json')).items():
 assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==expected,name
VERIFY
python3 experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/measure-long.py screen --variant B
