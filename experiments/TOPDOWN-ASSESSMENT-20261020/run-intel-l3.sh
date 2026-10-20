#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
exec 9>/tmp/bplus-topdown-diagnostic.lock
flock -n 9
SERVICE=redis-benchmarks-spec-sc-coordinator
mkdir -p results
supervisorctl status "$SERVICE" > results/coordinator-before.txt
test -z "$(docker ps -q)"
grep -q RUNNING results/coordinator-before.txt
systemd-run --unit=bplus-topdown-recovery-20261020 --on-active=8m /usr/bin/supervisorctl start "$SERVICE"
restore() {
 supervisorctl start "$SERVICE" > results/coordinator-restore.txt 2>&1 || true
 supervisorctl status "$SERVICE" > results/coordinator-after.txt
 if grep -q RUNNING results/coordinator-after.txt; then systemctl stop bplus-topdown-recovery-20261020.timer; fi
}
trap restore EXIT
supervisorctl stop "$SERVICE" > results/coordinator-stop.txt
BPLUS_TMA_LEVEL=3 python3 capture.py
