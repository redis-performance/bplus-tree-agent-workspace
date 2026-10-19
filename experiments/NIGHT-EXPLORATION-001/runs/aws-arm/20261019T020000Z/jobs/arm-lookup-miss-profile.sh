set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/002-lookup
mkdir -p "$OUT/miss-profile"
for N in 100000 1000000; do
 @PERF@ stat -x, -e cycles,instructions,branches,branch-misses,cache-references,cache-misses -o "$OUT/miss-profile/n${N}-stat.csv" "$OUT/build/base" --size "$N" --ops 20000000 --case lookup-miss --member-bytes 16 --seed 1 > "$OUT/miss-profile/n${N}-run.csv" 2> "$OUT/miss-profile/n${N}-run.stderr"
 @PERF@ record -F 999 -g -o "$OUT/miss-profile/perf.data" -- "$OUT/build/base" --size "$N" --ops 20000000 --case lookup-miss --member-bytes 16 --seed 1 > "$OUT/miss-profile/n${N}-sample.csv" 2> "$OUT/miss-profile/n${N}-record.stderr"
 @PERF@ report -i "$OUT/miss-profile/perf.data" --stdio --no-children --percent-limit 0.5 > "$OUT/miss-profile/n${N}-report.txt"
 @PERF@ annotate -i "$OUT/miss-profile/perf.data" --stdio --symbol zbtreeScoreRaw > "$OUT/miss-profile/n${N}-annotate.txt"
 sha256sum "$OUT/miss-profile/perf.data" > "$OUT/miss-profile/n${N}-raw-sha256.txt"
 mv "$OUT/miss-profile/perf.data" "scratch/arm-miss-n${N}-perf.data"
done
objdump -dS --disassemble=zbtreeScoreRaw "$OUT/build/base" > "$OUT/miss-profile/zbtreeScoreRaw-source.asm"
