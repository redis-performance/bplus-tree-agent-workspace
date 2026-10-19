set -eu
cd @REPO@
for v in base C; do
 dir=scratch/amd-lowerbound-build/$v
 clang -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3 -I"$dir/src" -I"$dir/compat" -I"$dir/vendor/redis" scratch/amd-scoped-profile/profile-scoped-fifo.c "$dir/src/zset_btree.c" "$dir/compat/standalone.c" "$dir/vendor/redis/siphash.c" -lm -o "scratch/amd-scoped-profile/$v-fifo-profile"
done
