set -eu
cd @REPO@
job=scratch/arm-mask-followup-20261019
python3 "$job/run-phase.py" --checkout "$PWD" --phase primary-AA
python3 "$job/audit-phase.py" --phase primary-AA
