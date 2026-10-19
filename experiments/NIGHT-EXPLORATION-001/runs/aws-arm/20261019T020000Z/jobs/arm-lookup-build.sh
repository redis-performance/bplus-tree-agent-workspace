set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/002-lookup
mkdir -p "$OUT/build"
clang -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3 -fno-lto -Isrc -Icompat -Ivendor/redis "$OUT/lookup-bench.c" src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o "$OUT/build/base"
clang -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O1 -fno-lto -fsanitize=address,undefined -fno-sanitize-recover=all -Isrc -Icompat -Ivendor/redis "$OUT/lookup-bench.c" src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o "$OUT/build/base-san"
sha256sum "$OUT/build/base" "$OUT/build/base-san" "$OUT/lookup-bench.c" > "$OUT/build/hashes.txt"
