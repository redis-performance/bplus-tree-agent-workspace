#!/bin/sh
set -eu
EXP=experiments/ARM-LOOKUP-CONT-001
LOG=$EXP/variants/H8-B
OUT=build/arm-cont-private
mkdir -p "$LOG" "$OUT"
sh "$EXP/qualify.sh" > "$LOG/qualify.stdout" 2> "$LOG/qualify.stderr"
cp "$EXP/qualification-unstable/upstream-native.log" "$EXP/qualification-unstable/upstream-sanitizer.log" "$EXP/qualification-unstable/fixture-native.jsonl" "$EXP/qualification-unstable/fixture-sanitizer.jsonl" "$LOG/"
for name in output_oracle output_external_oracle; do
 cc -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O1 -fsanitize=address,undefined -fno-sanitize-recover=all -DREDIS_DEBUG -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" "$EXP/$name.c" "$EXP/current/compat/standalone.c" "$EXP/current/vendor/siphash.c" -lm -o "$OUT/$name" > "$LOG/$name.build.stdout" 2> "$LOG/$name.build.stderr"
 "$OUT/$name" > "$LOG/$name.stdout" 2> "$LOG/$name.stderr"
done
