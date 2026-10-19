set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode
for V in A B C; do
 for MODE in native sanitize; do
  python3 tests/test_decoder.py "$OUT/build/$V/decoder-$MODE" > "$OUT/validation/$V-$MODE.stdout" 2> "$OUT/validation/$V-$MODE.stderr"
 done
done
