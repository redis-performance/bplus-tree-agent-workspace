set -eu
cd @REPO@
P=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/005-iterator
for MODE in native sanitize; do
 FLAGS=-O3;NAME=base
 if [ "$MODE" = sanitize ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all';NAME=base-sanitize;fi
 clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -fno-lto $FLAGS "$P/cache-oracle-additive.c" src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o "$P/build/$NAME-additive"
 "$P/build/$NAME-additive" > "$P/raw/$NAME-additive.stdout" 2> "$P/raw/$NAME-additive.stderr"
done
