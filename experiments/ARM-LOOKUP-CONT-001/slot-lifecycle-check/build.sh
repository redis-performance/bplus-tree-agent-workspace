#!/bin/sh
# Native compile/inspection only; never run lifecycle.
set -eu
test "$#" -eq 2
test "$2" = native
LC_OUT=$1
LC_EXP=experiments/ARM-LOOKUP-CONT-001
LC_DIR=$LC_EXP/slot-lifecycle-check
test ! -e "$LC_OUT"
mkdir -p "$LC_OUT"
python3 "$LC_DIR/validate_static.py" > "$LC_OUT/source-check.json"
LC_CC=${TASK_CC:-cc}
"$LC_CC" --version > "$LC_OUT/compiler.txt"
LC_WRAP=
for LC_SYMBOL in clock_gettime clock_getres clock time gettimeofday times getrusage timespec_get timespec_getres __clock_gettime __clock_gettime64 __gettimeofday syscall; do
 LC_WRAP="$LC_WRAP -Wl,--wrap=$LC_SYMBOL -Wl,--undefined=__wrap_$LC_SYMBOL"
done
"$LC_CC" -O3 -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer \
 -I"$LC_EXP/current/src" -I"$LC_EXP/current/compat" -I"$LC_EXP/current/vendor" \
 "$LC_DIR/lifecycle.c" "$LC_DIR/deny_clock.c" "$LC_EXP/current/compat/standalone.c" \
 "$LC_EXP/current/vendor/siphash.c" $LC_WRAP -lm -o "$LC_OUT/lifecycle" > "$LC_OUT/build.stdout" 2> "$LC_OUT/build.stderr"
nm "$LC_OUT/lifecycle" > "$LC_OUT/symbols.txt"
nm -u "$LC_OUT/lifecycle" > "$LC_OUT/undefined.txt"
objdump -d "$LC_OUT/lifecycle" > "$LC_OUT/assembly.txt"
sha256sum "$LC_OUT/lifecycle" "$LC_OUT/symbols.txt" "$LC_OUT/undefined.txt" "$LC_OUT/assembly.txt" \
 "$LC_OUT/compiler.txt" "$LC_DIR/lifecycle.c" "$LC_DIR/generated/zset_btree.c" "$LC_DIR/shadow.h" \
 "$LC_DIR/deny_clock.c" "$LC_DIR/build.sh" "$LC_DIR/DEPENDENCIES.json" \
 "$LC_EXP/current/compat/standalone.c" "$LC_EXP/current/compat/server.h" \
 "$LC_EXP/current/src/zset_btree.h" "$LC_EXP/current/vendor/sds.h" "$LC_EXP/current/vendor/siphash.c" \
 > "$LC_OUT/SHA256SUMS"
