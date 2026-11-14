#!/bin/sh
# Compile and inspect only. This script never executes the diagnostic ELF.
set -eu
test "$#" -eq 2
PC_OUT=$1
PC_MODE=$2
PC_EXP=experiments/ARM-LOOKUP-CONT-001
PC_DIR=$PC_EXP/probe-census
case "$PC_MODE" in
 native) set -- -O3 ;;
 lto) set -- -O3 -flto=auto ;;
 *) exit 2 ;;
esac
test ! -e "$PC_OUT"
mkdir -p "$PC_OUT"
python3 "$PC_DIR/generate.py" --check > "$PC_OUT/generation-check.stdout"
PC_CC=${TASK_CC:-cc}
"$PC_CC" --version > "$PC_OUT/compiler.txt"
PC_WRAP=
for PC_SYMBOL in clock_gettime clock_getres clock time gettimeofday times getrusage timespec_get timespec_getres __clock_gettime __clock_gettime64 __gettimeofday syscall; do
 PC_WRAP="$PC_WRAP -Wl,--wrap=$PC_SYMBOL"
done
"$PC_CC" "$@" -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer \
 -I"$PC_EXP/current/src" -I"$PC_EXP/current/compat" -I"$PC_EXP/current/vendor" \
 "$PC_DIR/generated/census.c" "$PC_DIR/deny_clock.c" \
 "$PC_EXP/current/compat/standalone.c" "$PC_EXP/current/vendor/siphash.c" \
 $PC_WRAP -lm -o "$PC_OUT/census" > "$PC_OUT/build.stdout" 2> "$PC_OUT/build.stderr"
nm "$PC_OUT/census" > "$PC_OUT/symbols.txt"
nm -u "$PC_OUT/census" > "$PC_OUT/undefined.txt"
objdump -d "$PC_OUT/census" > "$PC_OUT/assembly.txt"
sha256sum "$PC_OUT/census" "$PC_DIR/generated/zset_btree.c" "$PC_DIR/generated/census.c" \
 "$PC_DIR/instrumentation.h" "$PC_DIR/deny_clock.c" "$PC_DIR/build.sh" \
 "$PC_DIR/GENERATION.json" > "$PC_OUT/SHA256SUMS"
