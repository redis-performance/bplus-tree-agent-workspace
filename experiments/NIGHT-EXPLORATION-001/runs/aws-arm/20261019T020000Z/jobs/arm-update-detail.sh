set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/004-update
for SIZE in 100000 1000000; do
 CELL=same-$SIZE
 timeout 120 @PERF@ record -F 999 -g -o "$OUT/profile/perf.data" -- "$OUT/build/update-native" --case same --size "$SIZE" --ops 20000000 --seed 1 > "$OUT/profile/$CELL.csv" 2> "$OUT/profile/$CELL-record.stderr"
 @PERF@ report -i "$OUT/profile/perf.data" --stdio --no-children --percent-limit 0.5 > "$OUT/profile/$CELL-report.txt"
 sha256sum "$OUT/profile/perf.data" > "$OUT/profile/$CELL-raw-sha256.txt"
 mv "$OUT/profile/perf.data" "scratch/arm-update-$CELL-perf.data"
done
for CELL in same-100000 same-1000000 preserve-100000 distant-100000; do
 for SYMBOL in zbtreeFindForAdd zbtScoreLeafFindMember zbtScoreUpdateInPlace zbtScoreInsertAt; do
  @PERF@ annotate -i "scratch/arm-update-$CELL-perf.data" --stdio --symbol "$SYMBOL" > "$OUT/profile/$CELL-$SYMBOL-annotate.txt"
 done
done
