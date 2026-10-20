#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
python3 - <<'PY'
import json,platform,subprocess
from pathlib import Path
paths=['/sys/devices/system/cpu/cpu2/topology/thread_siblings_list','/sys/devices/system/cpu/cpu2/cpufreq/scaling_governor','/sys/devices/system/cpu/cpu2/cpufreq/scaling_driver','/sys/devices/system/cpu/intel_pstate/no_turbo','/proc/sys/kernel/perf_event_paranoid']
x={'arch':platform.machine(),'kernel':platform.release(),'source_commit':json.loads(Path('protocol.json').read_text())['source_commit'],
'compiler':subprocess.check_output(['clang-18','--version'],text=True),'state':{p:Path(p).read_text().strip() for p in paths},
'numa':subprocess.check_output(['numactl','--hardware'],text=True)}
Path('results/environment.json').write_text(json.dumps(x,indent=2)+'\n')
PY
for V in base B; do
 D="variants/$V"; mkdir -p "build/$V"
 COMMON="-I$D/src -I$D/compat -I$D/vendor/redis -Idriver -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer"
 SOURCES="$D/src/zset_btree.c $D/compat/standalone.c $D/vendor/redis/siphash.c"
 clang-18 $COMMON -O3 -DPROFILE_SAMPLE driver/iterator-long.c $SOURCES ready.c -lm -o "build/$V/iterator"
 for MODE in native sanitize; do
  FLAGS=-O3; if [ "$MODE" = sanitize ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
  clang-18 $COMMON $FLAGS -DREDIS_TEST -DREDIS_DEBUG "$D/tests/upstream.c" $SOURCES -lm -o "build/$V/test-$MODE"
  "build/$V/test-$MODE" > "results/$V-tests-$MODE.txt" 2>&1
  for ORACLE in cache-oracle cache-oracle-additive; do
   clang-18 $COMMON $FLAGS "driver/$ORACLE.c" $SOURCES -lm -o "build/$V/$ORACLE-$MODE"
   "build/$V/$ORACLE-$MODE" > "results/$V-$ORACLE-$MODE.txt" 2>&1
  done
 done
done
D=variants/base
clang-18 -I$D/src -I$D/compat -I$D/vendor/redis -Idriver -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -O3 driver/iterator.c "$D/src/zset_btree.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" -lm -o build/base/original
sha256sum build/base/* build/B/* driver/* variants/base/src/* variants/B/src/* > results/build-sha256.txt
PYTHONPATH=glue:pmu python3 campaign.py
