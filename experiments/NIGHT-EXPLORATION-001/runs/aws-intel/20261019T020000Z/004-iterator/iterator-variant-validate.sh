set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator
for V in base A B C; do
 for MODE in "$V" "$V-sanitize"; do
  "$P/build/$MODE-upstream" > "$P/raw/$MODE-upstream.stdout" 2> "$P/raw/$MODE-upstream.stderr"
  "$P/build/$MODE-oracle" > "$P/raw/$MODE-oracle.stdout" 2> "$P/raw/$MODE-oracle.stderr"
 done
 python3 "$P/validate.py" "$V"
done
