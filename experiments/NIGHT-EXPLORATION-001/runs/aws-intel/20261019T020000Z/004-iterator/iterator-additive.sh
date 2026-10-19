set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator
for V in base A B C; do
 D="scratch/intel-iterator-variants/$V"
 for MODE in native sanitize; do
  FLAGS=-O3; OUT="$V"
  if [ "$MODE" = sanitize ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; OUT="$V-sanitize"; fi
  clang -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS "$P/cache-oracle-additive.c" "$D/src/zset_btree.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" -lm -o "$P/build/$OUT-additive"
  "$P/build/$OUT-additive" > "$P/raw/$OUT-additive.stdout" 2> "$P/raw/$OUT-additive.stderr"
 done
done
