set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup
mkdir -p "$P/build" "$P/raw"
clang --version > "$P/raw/compiler.txt"
clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -O3 "$P/lookup.c" src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o "$P/build/base"
clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -O1 -fsanitize=address,undefined -fno-sanitize-recover=all "$P/lookup.c" src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o "$P/build/sanitize"
sha256sum src/zset_btree.c src/zset_btree.h compat/* vendor/redis/* bench/* tests/* "$P/lookup.c" "$P/build/base" "$P/build/sanitize" > "$P/raw/build-sha256.txt"
objdump -d "$P/build/base" > "$P/raw/base-assembly.txt"
