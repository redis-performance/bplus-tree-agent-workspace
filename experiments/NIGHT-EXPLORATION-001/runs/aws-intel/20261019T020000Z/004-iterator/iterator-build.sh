set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator
mkdir -p "$P/build" "$P/raw" "$P/profiles"
for MODE in release sanitize profile disabled; do
 FLAGS=-O3
 if [ "$MODE" = sanitize ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
 if [ "$MODE" = profile ]; then FLAGS='-O3 -DPROFILE_SAMPLE'; fi
 if [ "$MODE" = disabled ]; then FLAGS='-O3 -DPROFILE_SAMPLE -DSAMPLE_DISABLED'; fi
 clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS "$P/iterator.c" src/zset_btree.c compat/standalone.c vendor/redis/siphash.c "$P/sampler.c" -lm -o "$P/build/$MODE"
 nm -n -S "$P/build/$MODE" > "$P/raw/$MODE-nm.txt"
 objdump -d "$P/build/$MODE" > "$P/raw/$MODE-assembly.txt"
done
for MODE in enabled disabled; do
 FLAGS='-O3 -DSAMPLE_SELF_TEST'
 if [ "$MODE" = disabled ]; then FLAGS="$FLAGS -DSAMPLE_DISABLED"; fi
 clang -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS "$P/sampler.c" -o "$P/build/control-$MODE"
 nm -n -S "$P/build/control-$MODE" > "$P/raw/control-$MODE-nm.txt"
done
sha256sum src/zset_btree.c src/zset_btree.h "$P"/*.c "$P"/build/* > "$P/build-sha256.txt"
