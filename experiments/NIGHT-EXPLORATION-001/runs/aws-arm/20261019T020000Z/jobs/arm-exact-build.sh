set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/002-lookup
mkdir -p "$OUT/variant-build"
for V in base A B C; do
 ROOT=scratch/arm-exact/$V
 mkdir -p "$ROOT"
 cp -a src compat vendor tests Makefile "$ROOT/"
 if [ "$V" != base ]; then cp "scratch/arm-candidate-$V.c" "$ROOT/src/zset_btree.c"; fi
 for MODE in native sanitize; do
  FLAGS='-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -fno-lto'
  if [ "$MODE" = native ]; then FLAGS="$FLAGS -O3"; else FLAGS="$FLAGS -O1 -fsanitize=address,undefined -fno-sanitize-recover=all"; fi
  clang $FLAGS -I"$ROOT/src" -I"$ROOT/compat" -I"$ROOT/vendor/redis" "$OUT/lookup-bench.c" "$ROOT/src/zset_btree.c" "$ROOT/compat/standalone.c" "$ROOT/vendor/redis/siphash.c" -lm -o "$OUT/build/$V-$MODE"
  clang $FLAGS -DREDIS_TEST -DREDIS_DEBUG -I"$ROOT/src" -I"$ROOT/compat" -I"$ROOT/vendor/redis" "$ROOT/tests/upstream.c" "$ROOT/src/zset_btree.c" "$ROOT/compat/standalone.c" "$ROOT/vendor/redis/siphash.c" -lm -o "$ROOT/upstream-$MODE"
  for TEST in index_storage_oracle index_probe_oracle; do
   clang $FLAGS -I"$ROOT/src" -I"$ROOT/compat" -I"$ROOT/vendor/redis" "$ROOT/tests/$TEST.c" "$ROOT/compat/standalone.c" "$ROOT/vendor/redis/siphash.c" -lm -o "$ROOT/$TEST-$MODE"
  done
  if [ "$V" != base ]; then
   cp "$OUT/exact_tag_oracle.c" "$ROOT/tests/"
   clang $FLAGS -I"$ROOT/src" -I"$ROOT/compat" -I"$ROOT/vendor/redis" "$ROOT/tests/exact_tag_oracle.c" "$ROOT/compat/standalone.c" "$ROOT/vendor/redis/siphash.c" -lm -o "$ROOT/exact_tag_oracle-$MODE"
  fi
 done
 if [ "$V" != base ]; then cp "$OUT/build/$V-native" "$OUT/build/$V"; fi
 sha256sum "$ROOT/src/zset_btree.c" "$ROOT/src/zset_btree.h" "$ROOT/compat/standalone.c" "$ROOT/vendor/redis/siphash.c" "$ROOT/tests/upstream.c" "$ROOT/tests/index_storage_oracle.c" "$ROOT/tests/index_probe_oracle.c" "$OUT/build/$V-native" "$OUT/build/$V-sanitize" > "$OUT/variant-build/$V-hashes.txt"
 objdump -d --disassemble=zbtreeScoreRaw "$OUT/build/$V-native" > "$OUT/variant-build/$V-zbtreeScoreRaw.asm"
done
cmp "$OUT/build/base" "$OUT/build/base-native" || true
