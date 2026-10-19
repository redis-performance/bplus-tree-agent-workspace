set -eu
cd @REPO@
job=scratch/arm-mask-followup-20261019
python3 "$job/run-phase.py" --checkout "$PWD" --phase original-comparison
python3 "$job/audit-phase.py" --phase original-comparison
