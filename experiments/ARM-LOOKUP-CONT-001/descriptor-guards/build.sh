#!/bin/sh
# Build only; measurement mode is exclusively for a reserved benchmark fleet.
# Run from repository root: sh descriptor-guards/build.sh SOURCE OUTPUT MODE
set -eu
test "$#" -eq 3
DG_SOURCE=$1
DG_OUTPUT=$2
DG_MODE=$3
DG_EXP=experiments/ARM-LOOKUP-CONT-001
case "$DG_MODE" in
    native) set -- -O3 ;;
    lto) set -- -O3 -flto=auto ;;
    sanitizer) set -- -O1 -fsanitize=address,undefined -fno-sanitize-recover=all ;;
    *) exit 2 ;;
esac
"${TASK_CC:-cc}" "$@" -std=c11 -g -Wall -Wextra -Werror \
    -fno-omit-frame-pointer -I"$DG_EXP/current/src" \
    -I"$DG_EXP/current/compat" -I"$DG_EXP/current/vendor" \
    "$DG_EXP/descriptor-guards/guards.c" "$DG_SOURCE" \
    "$DG_EXP/current/compat/standalone.c" \
    "$DG_EXP/current/vendor/siphash.c" -lm -o "$DG_OUTPUT"
