#!/bin/sh
set -eu
EXP=experiments/ARM-LOOKUP-CONT-001
V=$EXP/variants/H8-C
OUT=build/arm-cont-private
for kind in native sanitizer; do
 FLAGS='-O2'
 if [ "$kind" = sanitizer ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
 for name in record decoder mutation; do
  TESTFLAGS=
  if [ "$name" = mutation ]; then TESTFLAGS='-DREDIS_TEST'; fi
  cc -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS $TESTFLAGS -DREDIS_DEBUG -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" "$V/${name}_oracle.c" "$EXP/current/compat/standalone.c" "$EXP/current/vendor/siphash.c" -lm -o "$OUT/$name-$kind" > "$V/$name-$kind-build.stdout" 2> "$V/$name-$kind-build.stderr"
  "$OUT/$name-$kind" > "$V/$name-$kind.stdout" 2> "$V/$name-$kind.stderr"
 done
done
for name in output output_external; do
 cc -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -O1 -fsanitize=address,undefined -fno-sanitize-recover=all -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" "$EXP/${name}_oracle.c" "$EXP/current/compat/standalone.c" "$EXP/current/vendor/siphash.c" -lm -o "$OUT/$name-san" > "$V/$name-build.stdout" 2> "$V/$name-build.stderr"
 "$OUT/$name-san" > "$V/$name.stdout" 2> "$V/$name.stderr"
done
