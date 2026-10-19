set -eu
cd @REPO@
unset PROFILE_DISABLE BPLUS_PERF_CTL BPLUS_PERF_ACK
job=scratch/amd-corrected-iterator-13e459ff8
python3 "$job/run-profile.py" --checkout "$PWD" --perf @PERF@
python3 "$job/audit-profile.py" "$job/profile" --out "$job/profile/audit.json"
python3 "$job/map-code.py" "$job/profile" --out "$job/profile/code-map.json"
