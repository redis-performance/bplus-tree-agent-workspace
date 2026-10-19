set -eu
cd @REPO@
out=scratch/amd-delete-profile
mkdir "$out"
export BPLUS_PERF_CTL="$PWD/scratch/amd-scoped-profile/control2.fifo" BPLUS_PERF_ACK="$PWD/scratch/amd-scoped-profile/ack2.fifo"
for seed in 1 2 3; do
 for n in 100000 1000000; do
  label="delete-n$n-s$seed"
  @PERF@ record -q -D -1 --control="fifo:$BPLUS_PERF_CTL,$BPLUS_PERF_ACK" -e cycles:u -F997 -g --call-graph fp -o "$out/$label.data" -- scratch/amd-scoped-profile/base-fifo2-profile --case delete --size "$n" --ops 1000000 --member-bytes 16 --seed "$seed" > "$out/$label.csv" 2> "$out/$label.stderr"
  @PERF@ report --stdio --no-children --sort symbol -i "$out/$label.data" > "$out/$label-report.txt" 2> "$out/$label-report.stderr"
  @PERF@ script -i "$out/$label.data" -F ip,sym,symoff,period > "$out/$label.samples" 2> "$out/$label-script.stderr"
 done
done
sha256sum src/zset_btree.c scratch/amd-scoped-profile/base-fifo2-profile "$out/"*.data > "$out/hashes.txt"
