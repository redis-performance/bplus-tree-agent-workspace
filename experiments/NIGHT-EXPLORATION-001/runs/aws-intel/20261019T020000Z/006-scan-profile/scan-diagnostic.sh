set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/006-scan-profile
mkdir -p "$P/build" "$P/profiles"
for MODE in original profile disabled sanitize; do
 FLAGS=-O3; DRIVER="$P/scan-profile.c"
 if [ "$MODE" = original ]; then DRIVER=bench/microbench.c; fi
 if [ "$MODE" = profile ]; then FLAGS='-O3 -DPROFILE_SAMPLE'; fi
 if [ "$MODE" = disabled ]; then FLAGS='-O3 -DPROFILE_SAMPLE -DSAMPLE_DISABLED'; fi
 if [ "$MODE" = sanitize ]; then FLAGS='-O1 -DPROFILE_SAMPLE -DSAMPLE_DISABLED -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
 clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS "$DRIVER" src/zset_btree.c compat/standalone.c vendor/redis/siphash.c "$P/sampler.c" -lm -o "$P/build/$MODE"
done
for MODE in enabled disabled; do
 FLAGS='-O3 -DSAMPLE_SELF_TEST'; if [ "$MODE" = disabled ]; then FLAGS="$FLAGS -DSAMPLE_DISABLED"; fi
 clang -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS "$P/sampler.c" -o "$P/build/control-$MODE"
 SAMPLE_OUT="$P/profiles/known-$MODE.hist.csv" timeout 30 "$P/build/control-$MODE" > "$P/profiles/known-$MODE.stdout" 2> "$P/profiles/known-$MODE.stderr"
 nm -n -S "$P/build/control-$MODE" > "$P/known-$MODE-symbols.txt"
done
sha256sum src/zset_btree.c src/zset_btree.h bench/microbench.c "$P"/*.c "$P"/build/* > "$P/build-sha256.txt"
python3 "$P/run-diagnostic.py"
objdump -d --disassemble=zbtIndexScanSlot "$P/build/profile" > "$P/scan-slot-assembly.txt"
