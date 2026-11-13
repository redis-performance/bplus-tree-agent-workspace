#!/bin/sh
set -eu
EXP=experiments/ARM-LOOKUP-CONT-001
OUT=build/arm-cont-private
LOG=$EXP/qualification-unstable
mkdir -p "$OUT" "$LOG"
for kind in native sanitizer; do
 FLAGS='-O2'
 if [ "$kind" = sanitizer ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
 cc -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer $FLAGS -DREDIS_TEST -DREDIS_DEBUG -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" tests/upstream.c "$EXP/current/src/zset_btree.c" "$EXP/current/compat/standalone.c" "$EXP/current/vendor/siphash.c" -lm -o "$OUT/test-$kind-unstable"
 "$OUT/test-$kind-unstable" > "$LOG/upstream-$kind.log"
 cc -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer $FLAGS -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" "$EXP/lookup.c" "$EXP/current/src/zset_btree.c" "$EXP/current/compat/standalone.c" "$EXP/current/vendor/siphash.c" -lm -o "$OUT/lookup-$kind-unstable"
 for seed in 17 29 43; do for case in hit score miss long external update; do "$OUT/lookup-$kind-unstable" verify "$case" "$seed" 1; done; done > "$LOG/fixture-$kind.jsonl"
done
