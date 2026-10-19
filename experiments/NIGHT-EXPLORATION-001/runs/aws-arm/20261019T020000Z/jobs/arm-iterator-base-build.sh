set -eu
cd @REPO@
P=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/005-iterator
mkdir -p "$P/build" "$P/raw" "$P/profiles"
for MODE in native sanitize; do
 FLAGS=-O3
 if [ "$MODE" = sanitize ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
 NAME=base
 if [ "$MODE" = sanitize ]; then NAME=base-sanitize; fi
 for DRIVER in iterator cache-oracle; do
  SUFFIX=''
  if [ "$DRIVER" = cache-oracle ]; then SUFFIX=-oracle; fi
  clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -fno-lto $FLAGS "$P/$DRIVER.c" src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o "$P/build/$NAME$SUFFIX"
 done
 clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -fno-lto -DREDIS_TEST -DREDIS_DEBUG $FLAGS tests/upstream.c src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o "$P/build/$NAME-upstream"
 "$P/build/$NAME-upstream" > "$P/raw/$NAME-upstream.stdout" 2> "$P/raw/$NAME-upstream.stderr"
 "$P/build/$NAME-oracle" > "$P/raw/$NAME-oracle.stdout" 2> "$P/raw/$NAME-oracle.stderr"
done
python3 "$P/validate.py" base
sha256sum src/zset_btree.c src/zset_btree.h "$P"/*.c "$P"/build/* > "$P/base-build-sha256.txt"
