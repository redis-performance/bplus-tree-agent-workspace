set -eu
cd @REPO@
job=scratch/arm-mask-followup-20261019
python3 "$job/run-phase.py" --checkout "$PWD" --phase iterator-comparison
python3 "$job/audit-phase.py" --phase iterator-comparison
