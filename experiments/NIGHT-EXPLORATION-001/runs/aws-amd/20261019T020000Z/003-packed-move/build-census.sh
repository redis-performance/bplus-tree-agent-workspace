set -eu
cd @REPO@
clang -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3 -Isrc -Icompat -Ivendor/redis scratch/amd-census/census-bench.c scratch/amd-census/zset_btree.c compat/standalone.c vendor/redis/siphash.c -lm -o scratch/amd-census/census
