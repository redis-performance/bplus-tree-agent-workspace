set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup
clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3 -pg "$P/lookup.c" src/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o "$P/build/profile"
sha256sum "$P/build/profile" > "$P/raw/profile-binary-sha256.txt"
