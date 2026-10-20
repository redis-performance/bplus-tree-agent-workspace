#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
exec 9>/tmp/bplus-iterator-tma-001.lock
flock -n 9
mkdir -p results
SERVICE=redis-benchmarks-spec-sc-coordinator
supervisorctl status "$SERVICE" > results/coordinator-before.txt
grep -q RUNNING results/coordinator-before.txt
test -z "$(docker ps -q)"
systemd-run --unit=bplus-iterator-tma-recovery --on-active=30m /usr/bin/supervisorctl start "$SERVICE"
WORK_PID=
restore() {
 if [ -n "$WORK_PID" ]; then
  kill -TERM -- "-$WORK_PID" 2>/dev/null || true
  sleep 1
  kill -KILL -- "-$WORK_PID" 2>/dev/null || true
  wait "$WORK_PID" 2>/dev/null || true
 fi
 supervisorctl start "$SERVICE" > results/coordinator-restore.txt 2>&1 || true
 supervisorctl status "$SERVICE" > results/coordinator-after.txt
 if grep -q RUNNING results/coordinator-after.txt; then systemctl stop bplus-iterator-tma-recovery.timer; fi
}
trap restore EXIT
supervisorctl stop "$SERVICE" > results/coordinator-stop.txt
supervisorctl status "$SERVICE" > results/coordinator-stopped.txt || true
grep -q STOPPED results/coordinator-stopped.txt
test -z "$(docker ps -q)"
timeout --kill-after=10s 1500 bash work.sh &
WORK_PID=$!
wait "$WORK_PID"
