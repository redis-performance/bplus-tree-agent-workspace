set -eu
cd @REPO@
unset PROFILE_DISABLE BPLUS_PERF_CTL BPLUS_PERF_ACK
job=scratch/arm-corrected-iterator-13e459ff8
python3 "$job/run-aa.py" --baseline "$PWD/scratch/adapter-worktree-13e459ff8"
python3 "$job/audit-aa.py" "$job/aa" --out "$job/aa/audit.json"
