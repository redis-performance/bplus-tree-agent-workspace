set -eu
cd @REPO@
out=scratch/amd-scan-mechanism
mkdir "$out"
selected=A
cp scratch/amd-scoped-profile/profile-scoped-fifo2.c "$out/referee-diagnostic.c"
for v in base "$selected"; do
 dir="scratch/amd-scan-build/$v"
 clang -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3 -I"$dir/src" -I"$dir/compat" -I"$dir/vendor/redis" "$out/referee-diagnostic.c" "$dir/src/zset_btree.c" "$dir/compat/standalone.c" "$dir/vendor/redis/siphash.c" -lm -o "$out/$v-profile" > "$out/$v-build.stdout" 2> "$out/$v-build.stderr"
 objdump -d --disassemble=zbtIndexScanSlot "$out/$v-profile" > "$out/$v.scan-slot.asm"
done
export BPLUS_PERF_CTL="$PWD/scratch/amd-scoped-profile/control2.fifo" BPLUS_PERF_ACK="$PWD/scratch/amd-scoped-profile/ack2.fifo"
for seed in 1 2 3; do
 for n in 100000 1000000; do
  for v in base "$selected"; do
   label="$v-n$n-ops1000000-s$seed"
   @PERF@ stat -D -1 --control="fifo:$BPLUS_PERF_CTL,$BPLUS_PERF_ACK" -x, -e cycles:u,instructions:u,branches:u,branch-misses:u -o "$out/$label.stat" -- "$out/$v-profile" --case scan --size "$n" --ops 1000000 --member-bytes 16 --seed "$seed" > "$out/$label-stat.csv" 2> "$out/$label-stat.stderr"
   @PERF@ record -q -D -1 --control="fifo:$BPLUS_PERF_CTL,$BPLUS_PERF_ACK" -e cycles:u -F997 -g --call-graph fp -o "$out/$label.data" -- "$out/$v-profile" --case scan --size "$n" --ops 1000000 --member-bytes 16 --seed "$seed" > "$out/$label-record.csv" 2> "$out/$label-record.stderr"
   @PERF@ report --stdio --no-children --sort symbol -i "$out/$label.data" > "$out/$label-report.txt" 2> "$out/$label-report.stderr"
   @PERF@ script -i "$out/$label.data" -F ip,sym,symoff,period > "$out/$label.samples" 2> "$out/$label-script.stderr"
  done
 done
done
sha256sum "$out/"*-profile "$out/"*.data "$out/referee-diagnostic.c" > "$out/hashes.txt"
