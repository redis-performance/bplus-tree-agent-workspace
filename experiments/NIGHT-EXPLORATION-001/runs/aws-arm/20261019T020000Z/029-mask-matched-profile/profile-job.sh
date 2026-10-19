#!/bin/bash
set -euo pipefail
cd '@REPO@'
job='scratch/arm-mask-matched-profile-20261019'
python3 "$job/run-profile.py" --checkout "$PWD" --perf '@PERF@'
python3 "$job/audit-profile.py" "$job/profile" --out "$job/profile/audit.json"
python3 "$job/map-code.py" "$job/profile" --variant control --out "$job/profile/control-code-map.json"
python3 "$job/map-code.py" "$job/profile" --variant A --out "$job/profile/A-code-map.json"
