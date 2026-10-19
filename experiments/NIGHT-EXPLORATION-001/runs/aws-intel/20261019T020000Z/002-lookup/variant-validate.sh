set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup
for V in A B C; do
 D="scratch/intel-variants/$V"
 "$D/build/btree-test" > "$P/raw/$V-upstream.stdout" 2> "$P/raw/$V-upstream.stderr"
 "$D/build/sanitize/btree-test" > "$P/raw/$V-upstream-sanitize.stdout" 2> "$P/raw/$V-upstream-sanitize.stderr"
 for MODE in native sanitizer fallback; do
  "$P/build/$V-oracle-$MODE" > "$P/raw/$V-oracle-$MODE.stdout" 2> "$P/raw/$V-oracle-$MODE.stderr"
 done
 python3 "$P/validate.py" "$V"
done
