set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/004-update
mkdir -p "$OUT/profile"
for CELL in preserve-100000 nearby-100000 distant-100000 plus-n-100000 preserve-1000000 distant-1000000; do
 CASE=${CELL%-*}
 SIZE=${CELL##*-}
 timeout 120 @PERF@ record -F 999 -g -o "$OUT/profile/perf.data" -- "$OUT/build/update-native" --case "$CASE" --size "$SIZE" --ops 2000000 --seed 1 > "$OUT/profile/$CELL.csv" 2> "$OUT/profile/$CELL-record.stderr"
 @PERF@ report -i "$OUT/profile/perf.data" --stdio --no-children --percent-limit 0.5 > "$OUT/profile/$CELL-report.txt"
 @PERF@ annotate -i "$OUT/profile/perf.data" --stdio --symbol zbtreeUpdateScore > "$OUT/profile/$CELL-update-annotate.txt"
 sha256sum "$OUT/profile/perf.data" > "$OUT/profile/$CELL-raw-sha256.txt"
 mv "$OUT/profile/perf.data" "scratch/arm-update-$CELL-perf.data"
done
objdump -dS --disassemble=zbtreeUpdateScore "$OUT/build/update-native" > "$OUT/profile/update.asm"
