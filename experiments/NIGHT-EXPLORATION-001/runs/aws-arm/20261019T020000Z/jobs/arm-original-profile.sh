set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/002-lookup/profile-original
mkdir -p "$OUT"
@PERF@ stat -x, -e cycles,instructions,branches,branch-misses,cache-references,cache-misses -o "$OUT/stat.csv" build/size-matrix/btree-bench --size 100000 --ops 20000000 --case lookup-hit --member-bytes 16 --seed 1 > "$OUT/run.csv" 2> "$OUT/run.stderr"
@PERF@ record -F 499 -g -o "$OUT/perf.data" -- build/size-matrix/btree-bench --size 100000 --ops 20000000 --case lookup-hit --member-bytes 16 --seed 1 > "$OUT/sample-run.csv" 2> "$OUT/record.stderr"
@PERF@ report -i "$OUT/perf.data" --stdio --no-children --percent-limit 0.5 > "$OUT/report.txt"
sha256sum "$OUT/perf.data" build/size-matrix/btree-bench src/zset_btree.c > "$OUT/hashes.txt"
