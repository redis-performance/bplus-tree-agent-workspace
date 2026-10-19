set -eu
cd @REPO@
P=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/005-iterator
for N in 100000 1000000; do
 for SPEC in integer-forward-7 integer-reverse-7 integer-forward-4 fraction-forward-7; do
  E=${SPEC%%-*};REST=${SPEC#*-};D=${REST%-*};M=${SPEC##*-};CELL=$N-$SPEC
  timeout 120 @PERF@ record -F 999 -g -o "$P/profiles/perf.data" -- "$P/build/base" --size "$N" --ops 50000000 --member-bytes 16 --seed 1 --encoding "$E" --direction "$D" --mask "$M" > "$P/profiles/$CELL.csv" 2> "$P/profiles/$CELL-record.stderr"
  @PERF@ report -i "$P/profiles/perf.data" --stdio --no-children --percent-limit 0.5 > "$P/profiles/$CELL-report.txt"
  @PERF@ annotate -i "$P/profiles/perf.data" --stdio --symbol zbtreeIteratorNext > "$P/profiles/$CELL-iterator-annotate.txt"
  sha256sum "$P/profiles/perf.data" > "$P/profiles/$CELL-raw-sha256.txt"
  mv "$P/profiles/perf.data" "scratch/arm-iterator-$CELL-perf.data"
 done
done
objdump -dS --disassemble=zbtreeIteratorNext "$P/build/base" > "$P/profiles/iterator.asm"
