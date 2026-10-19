set -eu
cd @REPO@
python3 @JOB@/run-profile.py --checkout "$PWD" --lease @LEASE@ --perf @PERF@
python3 @JOB@/audit-profile.py
