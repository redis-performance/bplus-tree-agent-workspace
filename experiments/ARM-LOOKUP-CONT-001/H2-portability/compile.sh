#!/bin/sh
set -eu
export LC_ALL=C LANG=C
case "$1" in i686) CC=i686-linux-gnu-gcc;; s390x) CC=s390x-linux-gnu-gcc;; *) exit 2;; esac
EXP=/work/experiments/ARM-LOOKUP-CONT-001
HARNESS=$EXP/H2-portability
case "$2" in base) SRC=$EXP/current/src; VARIANT=;; B) SRC=/work/H2-B-source; VARIANT=-DH2_B;; *) exit 2;; esac
OUT=/out/$1-$2
mkdir "$OUT"
# Existing referee/header paths stay immutable, selected C is first in include order.
set -- -std=c11 -O2 -g -Wall -Wextra -fno-omit-frame-pointer $VARIANT -I"$SRC" -I"$EXP/current/src" -I"$EXP/current/compat" -I"$EXP/current/vendor"
COMMON="$EXP/current/compat/standalone.c $EXP/current/vendor/siphash.c"
$CC "$@" -DREDIS_TEST -DREDIS_DEBUG /work/tests/upstream.c "$SRC/zset_btree.c" $COMMON "$HARNESS/clock_guard.c" -Wl,--wrap=clock_gettime -lm -o "$OUT/unit"
$CC "$@" "$EXP/lookup.c" "$SRC/zset_btree.c" $COMMON "$HARNESS/clock_guard.c" -Wl,--wrap=clock_gettime -lm -o "$OUT/lookup"
for oracle in output_oracle output_external_oracle; do
 $CC "$@" "$EXP/$oracle.c" $COMMON "$HARNESS/clock_guard.c" -Wl,--wrap=clock_gettime -lm -o "$OUT/$oracle"
done
$CC "$@" "$HARNESS/abi.c" $COMMON "$HARNESS/clock_guard.c" -Wl,--wrap=clock_gettime -lm -o "$OUT/abi"
$CC "$@" -DREDIS_TEST -DREDIS_DEBUG "$HARNESS/paired_metadata.c" $COMMON "$HARNESS/clock_guard.c" -Wl,--wrap=clock_gettime -lm -o "$OUT/paired"
if [ -n "$VARIANT" ]; then
 $CC "$@" -DREDIS_TEST -DREDIS_DEBUG "$EXP/variants/H2-B/metadata_oracle.c" $COMMON "$HARNESS/clock_guard.c" -Wl,--wrap=clock_gettime -lm -o "$OUT/original_metadata"
fi
