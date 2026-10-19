set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/003-update
GMON_OUT_PREFIX="$P/profiles/disabled.gmon" "$P/build/disabled" --size 100000 --ops 5000000 --member-bytes 16 --seed 1 --query-seed 101 --query-order independent --pattern position > "$P/profiles/disabled-row.csv"
gprof -b "$P/build/disabled" "$P"/profiles/disabled.gmon.* > "$P/profiles/disabled-report.txt"
for N in 10000 100000 1000000; do
 for PATTERN in same position nearby distant original; do
  TAG="$PATTERN-$N"
  GMON_OUT_PREFIX="$P/profiles/$TAG.gmon" "$P/build/profile" --size "$N" --ops 5000000 --member-bytes 16 --seed 1 --query-seed 101 --query-order independent --pattern "$PATTERN" > "$P/profiles/$TAG-row.csv"
  gprof -b "$P/build/profile" "$P"/profiles/"$TAG".gmon.* > "$P/profiles/$TAG-report.txt"
 done
done
sha256sum "$P"/profiles/*.gmon.* > "$P/profiles/gmon-sha256.txt"
