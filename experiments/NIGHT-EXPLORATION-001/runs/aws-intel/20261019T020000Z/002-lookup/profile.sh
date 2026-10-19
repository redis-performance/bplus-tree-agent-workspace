set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup
PERF=/usr/lib/linux-tools/7.0.0-1014-aws/perf
mkdir -p "$P/profiles"
for N in 10000 100000 1000000; do
 for CASE in lookup-hit lookup-miss; do
  TAG="$CASE-$N"
  "$PERF" stat -x, -e task-clock,cycles,instructions,branches,branch-misses,cache-references,cache-misses -o "$P/profiles/$TAG-stat.csv" -- "$P/build/base" --size "$N" --ops 20000000 --member-bytes 16 --seed 1 --query-seed 101 --query-order independent --case "$CASE" > "$P/profiles/$TAG-stat-row.csv"
  "$PERF" record -q -F 499 -g -o "$P/profiles/$TAG.data" -- "$P/build/base" --size "$N" --ops 20000000 --member-bytes 16 --seed 1 --query-seed 101 --query-order independent --case "$CASE" > "$P/profiles/$TAG-record-row.csv"
  "$PERF" report --stdio --no-children --percent-limit 0.5 -i "$P/profiles/$TAG.data" > "$P/profiles/$TAG-report.txt"
 done
done
sha256sum "$P"/profiles/*.data > "$P/profiles/raw-profile-sha256.txt"
