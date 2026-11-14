#!/bin/sh
# Build only. Measurement execution requires a separate controller admission.
# SOURCE OUTPUT native|lto|sanitizer public|diagnostic
set -eu
test "$#" -eq 4
IG_SOURCE=$1 IG_OUTPUT=$2 IG_MODE=$3 IG_SCOPE=$4
IG_EXP=experiments/ARM-LOOKUP-CONT-001
case "$IG_MODE" in
  native) set -- -O3 ;;
  lto) set -- -O3 -flto=auto ;;
  sanitizer) set -- -O1 -fsanitize=address,undefined -fno-sanitize-recover=all ;;
  *) exit 2 ;;
esac
case "$IG_SCOPE" in
  public) set -- "$@" "$IG_SOURCE" ;;
  diagnostic) set -- "$@" -DINDEX_DIAGNOSTIC "-DZBT_SOURCE=\"$IG_SOURCE\"" ;;
  *) exit 2 ;;
esac
if test "${VERIFY_CLOCK_DENY:-0}" = 1; then
  set -- "$@" "$IG_EXP/index-guards/clock-deny.c" -Wl,--wrap=clock_gettime
fi
"${TASK_CC:-cc}" "$@" -std=c11 -g -Wall -Wextra -Werror \
  -fno-omit-frame-pointer -I. -I"$IG_EXP/current/src" \
  -I"$IG_EXP/current/compat" -I"$IG_EXP/current/vendor" \
  "$IG_EXP/index-guards/guards.c" "$IG_EXP/current/compat/standalone.c" \
  "$IG_EXP/current/vendor/siphash.c" -lm -o "$IG_OUTPUT"
