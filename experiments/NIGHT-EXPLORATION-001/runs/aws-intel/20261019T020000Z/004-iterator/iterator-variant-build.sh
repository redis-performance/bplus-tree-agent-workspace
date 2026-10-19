set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator
mkdir -p scratch/intel-iterator-variants
for V in base A B C; do
 D="scratch/intel-iterator-variants/$V";mkdir -p "$D"
 git archive 8fab511e src compat vendor/redis tests bench Makefile | tar -x -C "$D"
 if [ "$V" != base ]; then patch -d "$D" -p1 < "$P/variants/$V/candidate.patch"; fi
 for MODE in native sanitize; do
  FLAGS=-O3
  if [ "$MODE" = sanitize ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
  OUT="$V";if [ "$MODE" = sanitize ]; then OUT="$V-sanitize"; fi
  clang -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS "$P/iterator.c" "$D/src/zset_btree.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" "$P/sampler.c" -lm -o "$P/build/$OUT"
  clang -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS "$P/cache-oracle.c" "$D/src/zset_btree.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" -lm -o "$P/build/$OUT-oracle"
  clang -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -DREDIS_TEST -DREDIS_DEBUG $FLAGS "$D/tests/upstream.c" "$D/src/zset_btree.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" -lm -o "$P/build/$OUT-upstream"
 done
 sha256sum "$D/src/zset_btree.c" "$D/src/zset_btree.h" "$P/build/$V" "$P/build/$V-sanitize" > "$P/raw/$V-variant-sha256.txt"
 objdump -d "$P/build/$V" > "$P/raw/$V-variant-assembly.txt"
done
