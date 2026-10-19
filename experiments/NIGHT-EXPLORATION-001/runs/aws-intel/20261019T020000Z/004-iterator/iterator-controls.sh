set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator
for MODE in enabled disabled; do
 SAMPLE_OUT="$P/profiles/control-$MODE.hist.csv" timeout 120 "$P/build/control-$MODE" > "$P/profiles/control-$MODE.stdout" 2> "$P/profiles/control-$MODE.stderr"
done
SAMPLE_OUT="$P/profiles/iterator-disabled.hist.csv" timeout 120 "$P/build/disabled" --size 100000 --ops 100000000 --member-bytes 16 --mask 7 --encoding integer --direction forward --seed 1 > "$P/profiles/iterator-disabled.stdout" 2> "$P/profiles/iterator-disabled.stderr"
