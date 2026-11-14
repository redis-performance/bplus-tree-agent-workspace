#!/bin/sh
set -eu
EXP=experiments/ARM-LOOKUP-CONT-001
LOG=$EXP/variants/H8-B
OUT=build/arm-cont-private
mkdir -p "$OUT/baseline"
git show e13d9fc88:"$EXP/current/src/zset_btree.c" > "$OUT/baseline/zset_btree.c"
for variant in candidate baseline; do
 INCLUDE="$EXP/current/src"
 if [ "$variant" = baseline ]; then INCLUDE="$OUT/baseline"; fi
 for oracle in record; do
  DEFINE=
  if [ "$oracle" = mutation ]; then DEFINE=-DREDIS_TEST; fi
  for kind in native sanitizer; do
   FLAGS=-O2
   if [ "$kind" = sanitizer ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
   name="$variant-$oracle-v2-$kind"
   cc -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS -DREDIS_DEBUG $DEFINE -I"$INCLUDE" -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" "$LOG/${oracle}_oracle.c" "$EXP/current/compat/standalone.c" "$EXP/current/vendor/siphash.c" -lm -o "$OUT/$name" > "$LOG/$name.build.stdout" 2> "$LOG/$name.build.stderr"
   "$OUT/$name" > "$LOG/$name.stdout" 2> "$LOG/$name.stderr"
  done
 done
done
