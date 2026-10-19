set -eu
cd @REPO@
P=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile
D="$P/build"
mkdir -p "$D" "$P/profiles"
git archive 13e459ff8800be3f02b6b45c87dd7b0c39453fa9 src compat vendor/redis bench | tar -x -C "$D"
cp "$P/profile-scoped-fifo2.c" "$D/bench/profile-scoped-fifo2.c"
cd "$D"
clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3 bench/microbench.c src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o original
clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3 bench/profile-scoped-fifo2.c src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o diagnostic
cd @REPO@
clang --version > "$P/profiles/compiler.txt"
sha256sum "$D/src/zset_btree.c" "$D/src/zset_btree.h" "$D/compat/standalone.c" "$D/compat/server.h" "$D/bench/microbench.c" "$D/bench/profile-scoped-fifo2.c" "$D/original" "$D/diagnostic" > "$P/profiles/build-hashes.txt"
export BPLUS_PERF_CTL="$PWD/$D/control.fifo" BPLUS_PERF_ACK="$PWD/$D/ack.fifo"
mkfifo "$BPLUS_PERF_CTL" "$BPLUS_PERF_ACK"
PROFILE_DISABLE=1 @PERF@ stat -D -1 --control="fifo:$BPLUS_PERF_CTL,$BPLUS_PERF_ACK" -x, -e cycles:u -o "$P/profiles/disabled.stat" -- "$D/diagnostic" --case scan --size 100000 --ops 5000000 --member-bytes 16 --seed 1 > "$P/profiles/disabled.csv" 2> "$P/profiles/disabled.stderr"
for SEED in 1 2 3; do
 for N in 100000 1000000; do
  LABEL="scan-n$N-s$SEED"
  "$D/original" --case scan --size "$N" --ops 5000000 --member-bytes 16 --seed "$SEED" > "$P/profiles/$LABEL-original.csv"
  PROFILE_DISABLE=1 "$D/diagnostic" --case scan --size "$N" --ops 5000000 --member-bytes 16 --seed "$SEED" > "$P/profiles/$LABEL-disabled.csv"
  @PERF@ record -q -D -1 --control="fifo:$BPLUS_PERF_CTL,$BPLUS_PERF_ACK" -e cycles:u -F997 -g --call-graph fp -o "scratch/arm-corrected-$LABEL.data" -- "$D/diagnostic" --case scan --size "$N" --ops 5000000 --member-bytes 16 --seed "$SEED" > "$P/profiles/$LABEL-profile.csv" 2> "$P/profiles/$LABEL-record.stderr"
  @PERF@ report --stdio --no-children --sort symbol -i "scratch/arm-corrected-$LABEL.data" > "$P/profiles/$LABEL-report.txt" 2> "$P/profiles/$LABEL-report.stderr"
  @PERF@ script -i "scratch/arm-corrected-$LABEL.data" -F ip,sym,symoff,period > "$P/profiles/$LABEL.samples" 2> "$P/profiles/$LABEL-script.stderr"
  @PERF@ annotate --stdio -i "scratch/arm-corrected-$LABEL.data" --symbol zbtIndexScanSlot > "$P/profiles/$LABEL-slot-annotate.txt" 2> "$P/profiles/$LABEL-annotate.stderr"
  sha256sum "scratch/arm-corrected-$LABEL.data" > "$P/profiles/$LABEL-raw-sha256.txt"
 done
done
nm -S --size-sort "$D/diagnostic" > "$P/profiles/symbols.txt"
objdump -dSl "$D/diagnostic" > "$P/profiles/diagnostic.asm"
objdump -dSl "$D/original" > "$P/profiles/original.asm"

A=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/015-corrected-scan-aa
BASE=scratch/arm-corrected-scan/base
mkdir -p "$BASE" "$A/raw"
git archive 13e459ff8800be3f02b6b45c87dd7b0c39453fa9 src compat vendor/redis bench Makefile | tar -x -C "$BASE"
make -C "$BASE" CC=clang BUILD=build OPT=-O3 build/btree-bench > "$A/build.stdout" 2> "$A/build.stderr"
clang --version > "$A/compiler.txt"
python3 - <<'FREEZE'
from pathlib import Path
import hashlib,json
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/015-corrected-scan-aa');d=Path('scratch/arm-corrected-scan/base')
f={'source_commit':'13e459ff8800be3f02b6b45c87dd7b0c39453fa9','build_command':'make CC=clang BUILD=build OPT=-O3 build/btree-bench','compiler':(p/'compiler.txt').read_text(),'sha256':{str(x.relative_to(d)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [d/'src/zset_btree.c',d/'src/zset_btree.h',d/'bench/microbench.c',d/'compat/standalone.c',d/'compat/server.h',d/'vendor/redis/siphash.c',d/'build/btree-bench']},'aa_driver_sha256':hashlib.sha256((p/'run-aa.py').read_bytes()).hexdigest(),'requested_ops':5000000,'sizes':[100000,1000000],'member_bytes':16,'seeds':[401,402,403,401,402,403],'blocks_per_size':6,'processes':48,'budget_seconds':300,'minimum_window_ns':10000000,'absolute_effect_limit_percent':1,'candidate_timing_started':False}
(p/'comparison-freeze.json').write_text(json.dumps(f,indent=2)+'\n')
FREEZE
