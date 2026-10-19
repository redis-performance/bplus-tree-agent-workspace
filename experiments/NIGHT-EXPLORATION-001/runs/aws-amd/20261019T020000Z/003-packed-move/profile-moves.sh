set -eu
cd @REPO@
out=scratch/amd-move-profile
mkdir -p "$out"
export BPLUS_PERF_CTL="$PWD/scratch/amd-scoped-profile/control2.fifo" BPLUS_PERF_ACK="$PWD/scratch/amd-scoped-profile/ack2.fifo"
for case in insert delete; do
 for n in 100000 1000000; do
  label="$case-n$n"
  @PERF@ stat -D -1 --control="fifo:$BPLUS_PERF_CTL,$BPLUS_PERF_ACK" -x, -e cycles,instructions,branches,branch-misses,cache-misses -o "$out/$label.stat" -- scratch/amd-scoped-profile/base-fifo2-profile --case "$case" --size "$n" --ops "$n" --member-bytes 16 --seed 1 > "$out/$label-stat.csv" 2> "$out/$label-stat.stderr"
  @PERF@ record -q -D -1 --control="fifo:$BPLUS_PERF_CTL,$BPLUS_PERF_ACK" -e cycles:u -F 997 -g --call-graph fp -o "$out/$label.data" -- scratch/amd-scoped-profile/base-fifo2-profile --case "$case" --size "$n" --ops "$n" --member-bytes 16 --seed 1 > "$out/$label-record.csv" 2> "$out/$label-record.stderr"
  @PERF@ report --stdio --no-children --sort symbol -i "$out/$label.data" > "$out/$label-report.txt" 2> "$out/$label-report.stderr"
 done
done
objdump -d -M intel --disassemble=zbtScoreDeleteInPlace build/size-matrix/btree-bench > "$out/delete.asm"
objdump -d -M intel --disassemble=zbtScoreInsertAt build/size-matrix/btree-bench > "$out/insert.asm"
objdump -d -M intel --disassemble=zbtScoreLeafBuild build/size-matrix/btree-bench > "$out/build.asm"
