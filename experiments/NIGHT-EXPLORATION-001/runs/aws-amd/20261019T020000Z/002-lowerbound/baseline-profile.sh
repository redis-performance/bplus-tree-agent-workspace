set -eu
cd @REPO@
out=scratch/amd-profile-001
mkdir -p "$out"
for case in update lookup-hit lookup-miss; do
  @PERF@ stat -x, -e cycles,instructions,branches,branch-misses,cache-misses -o "$out/$case.stat" -- build/size-matrix/btree-bench --case "$case" --size 100000 --ops 3000000 --member-bytes 16 --seed 1 > "$out/$case-stat.csv" 2> "$out/$case-stat.stderr" || echo "$case stat unavailable" >> "$out/failures.txt"
  @PERF@ record -q -e cycles:u -F 997 -g --call-graph fp -o "$out/$case.data" -- build/size-matrix/btree-bench --case "$case" --size 100000 --ops 3000000 --member-bytes 16 --seed 1 > "$out/$case-record.csv" 2> "$out/$case-record.stderr" || echo "$case record unavailable" >> "$out/failures.txt"
  @PERF@ report --stdio --no-children --sort symbol -i "$out/$case.data" > "$out/$case-report.txt" 2> "$out/$case-report.stderr" || true
done
sha256sum build/size-matrix/btree-bench src/zset_btree.c bench/microbench.c > "$out/hashes.txt"
