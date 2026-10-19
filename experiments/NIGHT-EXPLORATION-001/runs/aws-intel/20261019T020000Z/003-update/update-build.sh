set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/003-update
mkdir -p "$P/build" "$P/raw" "$P/profiles"
for MODE in release sanitize profile disabled; do
 FLAGS=-O3
 if [ "$MODE" = sanitize ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
 if [ "$MODE" = profile ]; then FLAGS='-O3 -pg -DPROFILE_TIMED=1'; fi
 if [ "$MODE" = disabled ]; then FLAGS='-O3 -pg -DPROFILE_TIMED=2'; fi
 clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS "$P/update.c" src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o "$P/build/$MODE"
done
sha256sum "$P/update.c" "$P"/build/* > "$P/build-sha256.txt"
