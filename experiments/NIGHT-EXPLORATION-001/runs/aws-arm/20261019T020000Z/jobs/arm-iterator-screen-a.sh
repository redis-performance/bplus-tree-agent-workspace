set -eu
cd @REPO@
P=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/005-iterator
python3 - <<'VERIFY'
import hashlib,json
from pathlib import Path
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/005-iterator')
for name,want in json.load(open(p/'comparison-hashes.json')).items():
 assert hashlib.sha256((p/name).read_bytes()).hexdigest()==want,name
VERIFY
python3 "$P/measure.py" screen-A
