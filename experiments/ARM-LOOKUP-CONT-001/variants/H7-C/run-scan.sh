#!/bin/sh
set -eu
EXP=experiments/ARM-LOOKUP-CONT-001
V=$EXP/variants/H7-C
OUT=build/arm-cont-private
for kind in native sanitizer; do
 FLAGS='-O2'
 if [ "$kind" = sanitizer ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
 for variant in base candidate; do
  SOURCE=zset_btree.c
  if [ "$variant" = base ]; then SOURCE="$PWD/$OUT/baseline.c"; fi
  cc -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS -DREDIS_TEST -DREDIS_DEBUG -DZBT_SOURCE=\""$SOURCE"\" -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" "$V/scan_oracle.c" "$EXP/current/compat/standalone.c" "$EXP/current/vendor/siphash.c" -lm -o "$OUT/scan-$variant-$kind" > "$V/scan-$variant-$kind-build.stdout" 2> "$V/scan-$variant-$kind-build.stderr"
  "$OUT/scan-$variant-$kind" > "$V/scan-$variant-$kind.stdout" 2> "$V/scan-$variant-$kind.stderr"
 done
 cmp "$V/scan-base-$kind.stdout" "$V/scan-candidate-$kind.stdout"
done
