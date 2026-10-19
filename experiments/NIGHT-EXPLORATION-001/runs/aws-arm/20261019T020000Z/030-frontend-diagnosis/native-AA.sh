set -eu
cd @REPO@
python3 @JOB@/run-native.py --checkout "$PWD" --lease @LEASE@ --phase native-AA
python3 @JOB@/audit-native.py --phase native-AA
