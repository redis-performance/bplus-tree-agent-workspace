set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup
mkdir -p scratch/intel-variants
for V in A B C; do
 D="scratch/intel-variants/$V"
 mkdir -p "$D"
 git archive 8fab511e src compat vendor/redis tests bench Makefile | tar -x -C "$D"
 patch -d "$D" -p1 < "$P/variants/$V/candidate.patch"
 clang -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -O3 "$P/lookup.c" "$D/src/zset_btree.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" -lm -o "$P/build/$V"
 clang -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -O1 -fsanitize=address,undefined -fno-sanitize-recover=all "$P/lookup.c" "$D/src/zset_btree.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" -lm -o "$P/build/$V-sanitize"
 make -C "$D" CC=clang all > "$P/raw/$V-make.stdout" 2> "$P/raw/$V-make.stderr"
 make -C "$D" CC=clang BUILD=build/sanitize OPT=-O1 CFLAGS='-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O1 -fsanitize=address,undefined -fno-sanitize-recover=all' LDFLAGS='-fsanitize=address,undefined' build/sanitize/btree-test > "$P/raw/$V-sanitize-build.stdout" 2> "$P/raw/$V-sanitize-build.stderr"
 for MODE in native sanitizer fallback; do
  FLAGS=-O3
  if [ "$MODE" = sanitizer ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
  if [ "$MODE" = fallback ]; then FLAGS='-O3 -U__SSE2__'; fi
  clang -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS "$P/tag-oracle.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" -lm -o "$P/build/$V-oracle-$MODE"
 done
 sha256sum "$D/src/zset_btree.c" "$D/src/zset_btree.h" "$P/build/$V" "$P/build/$V-sanitize" > "$P/variants/$V/build-sha256.txt"
 objdump -d "$P/build/$V" > "$P/raw/$V-assembly.txt"
done
