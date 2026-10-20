#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
exec 9>/tmp/bplus-intel-followup-001.lock
flock -n 9
python3 preflight.py
python3 - <<'PY'
import datetime,json
from pathlib import Path
p=Path('reservation.json');assert not p.exists()
p.write_text(json.dumps({'owner':'bplus-intel-followup-001','state':'ACTIVE','original_sibling_topology':Path('/sys/devices/system/cpu/cpu2/topology/thread_siblings_list').read_text().strip(),'original_sibling_online':Path('/sys/devices/system/cpu/cpu50/online').read_text().strip(),'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n')
PY
WORK_PID=
restore() {
 if [ -n "$WORK_PID" ]; then
  kill -TERM -- "-$WORK_PID" 2>/dev/null || true
  sleep 1
  kill -KILL -- "-$WORK_PID" 2>/dev/null || true
  wait "$WORK_PID" 2>/dev/null || true
 fi
 python3 restore.py
}
trap restore EXIT
systemd-run --unit=bplus-intel-followup-recovery --on-active=30m /usr/bin/python3 "$PWD/restore.py" --recovery
supervisorctl stop redis-benchmarks-spec-sc-coordinator > results/coordinator-stop.txt
supervisorctl status redis-benchmarks-spec-sc-coordinator > results/coordinator-stopped.txt || true
grep -q STOPPED results/coordinator-stopped.txt
test -z "$(docker ps -q)"
printf 0 > /sys/devices/system/cpu/cpu50/online
setsid timeout --kill-after=10s 1500 taskset -c 0 python3 validate.py &
WORK_PID=$!
python3 - "$WORK_PID" <<'PYWORK'
import json,sys
from pathlib import Path
p=Path('reservation.json');s=json.loads(p.read_text());s['worker_pgid']=int(sys.argv[1]);p.write_text(json.dumps(s,indent=2)+'\n')
PYWORK
wait "$WORK_PID"
