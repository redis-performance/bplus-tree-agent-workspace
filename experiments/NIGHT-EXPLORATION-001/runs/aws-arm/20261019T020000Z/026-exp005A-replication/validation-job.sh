set -eu
cd @REPO@
job=scratch/arm-exp005A-replication-13e459ff8
python3 "$job/run-validation.py" --checkout "$PWD"
