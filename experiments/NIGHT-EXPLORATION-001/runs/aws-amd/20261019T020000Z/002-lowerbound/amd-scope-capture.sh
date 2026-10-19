set -eu
cd @REPO@
out=scratch/amd-scoped-profile
export BPLUS_PERF_CTL="$PWD/$out/control2.fifo" BPLUS_PERF_ACK="$PWD/$out/ack2.fifo"
for v in base C; do
 for spec in 100000:101717 1000000:52593 100000:3000000; do
  n=${spec%:*}; ops=${spec#*:}; label="$v-n$n-ops$ops"
  @PERF@ stat -D -1 --control="fifo:$BPLUS_PERF_CTL,$BPLUS_PERF_ACK" -x, -e cycles,instructions,branches,branch-misses,cache-misses -o "$out/$label.stat" -- "$out/$v-fifo2-profile" --case update --size "$n" --ops "$ops" --member-bytes 16 --seed 1 > "$out/$label-stat.csv" 2> "$out/$label-stat.stderr"
  @PERF@ record -q -D -1 --control="fifo:$BPLUS_PERF_CTL,$BPLUS_PERF_ACK" -e cycles:u -F 997 -g --call-graph fp -o "$out/$label.data" -- "$out/$v-fifo2-profile" --case update --size "$n" --ops "$ops" --member-bytes 16 --seed 1 > "$out/$label-record.csv" 2> "$out/$label-record.stderr"
  @PERF@ report --stdio --no-children --sort symbol -i "$out/$label.data" > "$out/$label-report.txt" 2> "$out/$label-report.stderr"
 done
done
sha256sum "$out/"*-profile "$out/"*.data > "$out/hashes.txt"
