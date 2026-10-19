set -eu
cd @REPO@
python3 experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/020-fold-predicate-aa/run-aa.py
python3 experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/020-fold-predicate-aa/audit.py
