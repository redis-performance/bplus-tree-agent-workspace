set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator
for REP in 1 2 3; do
 for N in 100000 1000000; do
  for SPEC in integer:forward:7 integer:reverse:7 integer:forward:4 fraction:forward:7; do
   IFS=: read -r ENCODING DIRECTION MASK <<< "$SPEC"
   TAG="$ENCODING-$DIRECTION-$MASK-$N-$REP"
   SAMPLE_OUT="$P/profiles/$TAG.hist.csv" timeout 120 "$P/build/profile" --size "$N" --ops 100000000 --member-bytes 16 --mask "$MASK" --encoding "$ENCODING" --direction "$DIRECTION" --seed "$REP" > "$P/profiles/$TAG.stdout" 2> "$P/profiles/$TAG.stderr"
  done
 done
done
