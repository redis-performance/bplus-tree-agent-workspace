#!/bin/sh
# Build only. Execute measurement mode only on an authorized benchmark fleet host.
# Usage from repository root: sh .../guards/build.sh SOURCE OUTPUT [native|lto]
set -eu
test "$#" -ge 2 && test "$#" -le 3
GUARD_SOURCE=$1
GUARD_OUTPUT=$2
GUARD_MODE=${3:-native}
GUARD_EXP=experiments/ARM-LOOKUP-CONT-001
GUARD_CC=${TASK_CC:-cc}
case "$GUARD_MODE" in
    native) set -- ;;
    lto) set -- -flto=auto ;;
    *) exit 2 ;;
esac
"$GUARD_CC" "$@" -std=c11 -O3 -g -Wall -Wextra -Werror \
    -fno-omit-frame-pointer -I"$GUARD_EXP/current/src" \
    -I"$GUARD_EXP/current/compat" -I"$GUARD_EXP/current/vendor" \
    "$GUARD_EXP/guards/guards.c" "$GUARD_SOURCE" \
    "$GUARD_EXP/current/compat/standalone.c" \
    "$GUARD_EXP/current/vendor/siphash.c" -lm -o "$GUARD_OUTPUT"
