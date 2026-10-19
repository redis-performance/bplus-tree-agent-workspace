set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode
mkdir -p "$OUT/profile"
for V in base root; do
 @PERF@ stat -x, -e cycles,instructions,branches,branch-misses,cache-references,cache-misses -o "$OUT/profile/$V-stat.csv" "$OUT/build/$V/decoder-native" --width 60 --reversed 0 --count 1 --leaves 64 --rounds 65536 --samples 64 --warmup 1 --seed 1 > "$OUT/profile/$V-run.csv" 2> "$OUT/profile/$V-run.stderr"
 @PERF@ record -F 999 -g -o "$OUT/profile/perf.data" -- "$OUT/build/$V/decoder-native" --width 60 --reversed 0 --count 1 --leaves 64 --rounds 65536 --samples 64 --warmup 1 --seed 1 > "$OUT/profile/$V-sample.csv" 2> "$OUT/profile/$V-record.stderr"
 @PERF@ report -i "$OUT/profile/perf.data" --stdio --no-children --percent-limit 0.5 > "$OUT/profile/$V-report.txt"
 @PERF@ annotate -i "$OUT/profile/perf.data" --stdio --symbol decoder_batch > "$OUT/profile/$V-batch-annotate.txt"
 @PERF@ annotate -i "$OUT/profile/perf.data" --stdio --symbol zbtScoreLeafDecodePolicy > "$OUT/profile/$V-policy-annotate.txt" || true
 sha256sum "$OUT/profile/perf.data" > "$OUT/profile/$V-raw-sha256.txt"
 mv "$OUT/profile/perf.data" "scratch/arm-decode-$V-perf.data"
 objdump -dS --disassemble=decoder_batch "$OUT/build/$V/decoder-native" > "$OUT/profile/$V-decoder-batch.asm"
 objdump -dS --disassemble=zbtScoreLeafDecodePolicy "$OUT/build/$V/decoder-native" > "$OUT/profile/$V-decoder-policy.asm"
done
