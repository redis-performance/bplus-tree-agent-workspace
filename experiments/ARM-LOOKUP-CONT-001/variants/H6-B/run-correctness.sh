#!/bin/sh
# Local correctness only: never execute lookup's timing mode.
set -eu
EXP=experiments/ARM-LOOKUP-CONT-001
LOG=$EXP/variants/H6-B
OUT=build/arm-cont-private
mkdir -p "$OUT"
sh "$EXP/qualify.sh" > "$LOG/qualify.stdout" 2> "$LOG/qualify.stderr"
for kind in native sanitizer; do
    cp "$EXP/qualification-unstable/upstream-$kind.log" "$LOG/"
    cp "$EXP/qualification-unstable/fixture-$kind.jsonl" "$LOG/"
done
for name in output_oracle output_external_oracle; do
    cc -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O1 \
       -fsanitize=address,undefined -fno-sanitize-recover=all -DREDIS_DEBUG \
       -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" \
       "$EXP/$name.c" "$EXP/current/compat/standalone.c" "$EXP/current/vendor/siphash.c" \
       -lm -o "$OUT/$name" > "$LOG/$name.build.stdout" 2> "$LOG/$name.build.stderr"
    "$OUT/$name" > "$LOG/$name.stdout" 2> "$LOG/$name.stderr"
done
for kind in native sanitizer; do
    FLAGS='-O2'
    if [ "$kind" = sanitizer ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
    cc -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer $FLAGS -DREDIS_DEBUG -DREDIS_TEST \
       -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" \
       "$LOG/descriptor_oracle.c" "$EXP/current/compat/standalone.c" "$EXP/current/vendor/siphash.c" \
       -lm -o "$OUT/descriptor-$kind" > "$LOG/descriptor-$kind.build.stdout" 2> "$LOG/descriptor-$kind.build.stderr"
    "$OUT/descriptor-$kind" > "$LOG/descriptor-$kind.stdout" 2> "$LOG/descriptor-$kind.stderr"
done
