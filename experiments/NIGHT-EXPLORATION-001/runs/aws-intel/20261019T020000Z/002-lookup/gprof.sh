set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup
for N in 10000 100000 1000000; do
 for CASE in lookup-hit lookup-miss; do
  TAG="$CASE-$N"
  GMON_OUT_PREFIX="$P/profiles/$TAG.gmon" "$P/build/profile" --size "$N" --ops 20000000 --member-bytes 16 --seed 1 --query-seed 101 --query-order independent --case "$CASE" > "$P/profiles/$TAG-gprof-row.csv"
  gprof -b "$P/build/profile" "$P"/profiles/"$TAG".gmon.* > "$P/profiles/$TAG-gprof.txt"
 done
done
sha256sum "$P"/profiles/*.gmon.* > "$P/profiles/gmon-sha256.txt"
