set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/003-update
for N in 100 1000 10000 100000 1000000; do
 for PATTERN in same position nearby distant original; do
  "$P/build/census" --size "$N" --ops "$((N*3))" --member-bytes 16 --seed 1 --query-seed 101 --query-order independent --pattern "$PATTERN" > "$P/raw/census-$PATTERN-$N.csv"
 done
done
