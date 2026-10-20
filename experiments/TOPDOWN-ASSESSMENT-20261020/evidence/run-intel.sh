#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
exec 9>/tmp/bplus-topdown-diagnostic.lock
flock -n 9
mkdir -p results build
# This script is started as root after live idle/ownership inspection.
SERVICE=redis-benchmarks-spec-sc-coordinator
sudo supervisorctl status "$SERVICE" > results/coordinator-before.txt
sudo docker ps --format '{{.Names}}' > results/containers-before.txt
test ! -s results/containers-before.txt
grep -q RUNNING results/coordinator-before.txt
# Independent recovery survives an SSH/controller failure; normal exit restores sooner.
systemd-run --unit=bplus-topdown-recovery-20261020 --on-active=12m /usr/bin/supervisorctl start "$SERVICE"
restore() {
    supervisorctl start "$SERVICE" > results/coordinator-restore.txt 2>&1 || true
    supervisorctl status "$SERVICE" > results/coordinator-after.txt
    if grep -q RUNNING results/coordinator-after.txt; then
        systemctl stop bplus-topdown-recovery-20261020.timer
    fi
}
trap restore EXIT
supervisorctl stop "$SERVICE" > results/coordinator-stop.txt
python3 - <<'PY'
import json,platform,subprocess,importlib.metadata
from pathlib import Path
from topdown.collector.toplev import ToplevRunner,ToplevOptions
p=Path('results')
meta={'arch':platform.machine(),'kernel':platform.release(),'topdown':importlib.metadata.version('topdown-profiler'),
      'pmu_tools':importlib.metadata.version('pmu_tools'),
      'pid_scope_reproducer':ToplevRunner('toplev.py',ToplevOptions(pids=[12345])).build_command(),
      'compiler':subprocess.check_output(['clang-18','--version'],text=True),
      'cpu_model':next(l.split(':',1)[1].strip() for l in Path('/proc/cpuinfo').read_text().splitlines() if l.startswith('model name'))}
p.joinpath('environment.json').write_text(json.dumps(meta,indent=2)+'\n')
PY
# Separate diagnostic copy; original referee is preserved and never timed here.
python3 - <<'PYMARK'
from pathlib import Path
p=Path('driver/iterator.c')
s=p.read_text()
needle='    size_t traversals=1+(ops-1)/n,count=traversals*n,owned=zbtreeAllocSize(tree);'
assert s.count(needle)==1
s=s.replace(needle, '    if (getenv("BPLUS_PROFILE_STOP")) ops *= 200; /* diagnostic windows only */\n'+needle)
Path('driver/iterator-diagnostic.c').write_text(s)
PYMARK
FLAGS='-Isrc -Icompat -Ivendor/redis -Idriver -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -O3'
clang-18 $FLAGS -DPROFILE_SAMPLE driver/iterator-diagnostic.c src/zset_btree.c compat/standalone.c vendor/redis/siphash.c ready.c -lm -o build/iterator-profile
clang-18 $FLAGS -DREDIS_TEST -DREDIS_DEBUG tests/upstream.c src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o build/btree-test
build/btree-test > results/correctness.txt 2>&1
./build/iterator-profile --size 100000 --ops 1000000 --mask 7 --encoding integer --direction forward --member-bytes 16 --seed 7103 > results/smoke.csv
sha256sum src/* compat/* vendor/redis/* driver/* ready.c build/* > results/inputs-sha256.txt
python3 capture.py
