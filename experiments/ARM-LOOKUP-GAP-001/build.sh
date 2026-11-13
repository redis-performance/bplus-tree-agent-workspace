#!/bin/sh
set -eu
# Run from repository root. Optional argument: output directory.
OUT=${1:-build/arm-lookup-gap}
EXP=experiments/ARM-LOOKUP-GAP-001
mkdir -p "$OUT"
cc -std=c11 -O3 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" "$EXP/lookup.c" "$EXP/current/src/zset_btree.c" "$EXP/current/compat/standalone.c" "$EXP/current/vendor/siphash.c" -lm -o "$OUT/lookup"
