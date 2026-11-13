#!/bin/sh
set -eu
# Run from repository root. Optional argument: output directory.
OUT=${1:-build/arm-lookup-cont}
EXP=experiments/ARM-LOOKUP-CONT-001
mkdir -p "$OUT"
TASK_CC=${TASK_CC:-cc}
TASK_LTO_FLAGS=
if [ "${TASK_LTO:-0}" = 1 ]; then TASK_LTO_FLAGS=-flto=auto; fi
"$TASK_CC" $TASK_LTO_FLAGS -std=c11 -O3 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor" "$EXP/lookup.c" "$EXP/current/src/zset_btree.c" "$EXP/current/compat/standalone.c" "$EXP/current/vendor/siphash.c" -lm -o "$OUT/lookup"
