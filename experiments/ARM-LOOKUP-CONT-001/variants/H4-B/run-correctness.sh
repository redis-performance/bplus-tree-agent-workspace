#!/bin/sh
# Reproduce the completed correctness commands from the isolated worktree root.
# No benchmark, timer, instruction-count or PMU measurement is executed.
set -eu
EXP=experiments/ARM-LOOKUP-CONT-001
LOG=$EXP/variants/H4-B
OUT=build/arm-cont-private
mkdir -p "$LOG" "$OUT/baseline"
sh "$EXP/qualify.sh" > "$LOG/qualify.stdout" 2> "$LOG/qualify.stderr"
cp "$EXP/qualification-unstable/upstream-native.log" \
   "$EXP/qualification-unstable/upstream-sanitizer.log" \
   "$EXP/qualification-unstable/fixture-native.jsonl" \
   "$EXP/qualification-unstable/fixture-sanitizer.jsonl" "$LOG/"
for name in output_oracle output_external_oracle; do
    cc -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O1 \
       -fsanitize=address,undefined -fno-sanitize-recover=all -DREDIS_DEBUG \
       -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" \
       "$EXP/$name.c" "$EXP/current/compat/standalone.c" \
       "$EXP/current/vendor/siphash.c" -lm -o "$OUT/$name" \
       > "$LOG/$name.build.stdout" 2> "$LOG/$name.build.stderr"
    "$OUT/$name" > "$LOG/$name.stdout" 2> "$LOG/$name.stderr"
done
git show e13d9fc8875a636ca07203b1f3fdd1aa28488bda:"$EXP/current/src/zset_btree.c" \
    > "$OUT/baseline/zset_btree.c"
for variant in candidate baseline; do
    FIRST_INCLUDE="$EXP/current/src"
    PREFIX=
    if [ "$variant" = baseline ]; then
        FIRST_INCLUDE="$OUT/baseline"
        PREFIX=baseline-
    fi
    for kind in native sanitizer; do
        FLAGS=-O2
        if [ "$kind" = sanitizer ]; then
            FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'
        fi
        name="${PREFIX}index-$kind"
        cc -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer $FLAGS \
           -DREDIS_DEBUG -DREDIS_TEST -I"$FIRST_INCLUDE" -I"$EXP/current/src" \
           -I"$EXP/current/compat" -I"$EXP/current/vendor" \
           "$LOG/index_oracle.c" "$EXP/current/compat/standalone.c" \
           "$EXP/current/vendor/siphash.c" -lm -o "$OUT/$name" \
           > "$LOG/$name.build.stdout" 2> "$LOG/$name.build.stderr"
        "$OUT/$name" > "$LOG/$name.stdout" 2> "$LOG/$name.stderr"
    done
done
