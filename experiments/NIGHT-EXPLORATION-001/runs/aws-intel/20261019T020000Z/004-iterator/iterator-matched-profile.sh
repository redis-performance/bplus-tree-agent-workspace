set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator
mkdir -p "$P/matched-profiles"
for V in base A B C; do
 D="scratch/intel-iterator-variants/$V"
 FLAGS='-O3 -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -DPROFILE_SAMPLE'
 for MODE in enabled disabled; do
  EXTRA=''; if [ "$MODE" = disabled ]; then EXTRA=-DSAMPLE_DISABLED; fi
  clang -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" $FLAGS $EXTRA "$P/iterator.c" "$D/src/zset_btree.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" "$P/sampler.c" -lm -o "$P/build/$V-profile-$MODE"
 done
 nm -n -S --defined-only "$P/build/$V-profile-enabled" > "$P/matched-profiles/$V.symbols.txt"
 objdump -d --disassemble=zbtreeIteratorNext "$P/build/$V-profile-enabled" > "$P/matched-profiles/$V.next.txt"
 sha256sum "$P/build/$V-profile-enabled" "$P/build/$V-profile-disabled" "$D/src/zset_btree.c" "$D/src/zset_btree.h" > "$P/matched-profiles/$V.sha256.txt"
 SAMPLE_OUT="$P/matched-profiles/$V-disabled.hist.csv" timeout 30 "$P/build/$V-profile-disabled" --size 100000 --ops 1000000 --member-bytes 16 --mask 7 --encoding integer --direction forward --seed 1 > "$P/matched-profiles/$V-disabled.stdout" 2> "$P/matched-profiles/$V-disabled.stderr"
done
for SEED in 1 2 3; do
 ORDER='base A B C'; if [ "$SEED" = 2 ]; then ORDER='A B C base'; fi; if [ "$SEED" = 3 ]; then ORDER='B C base A'; fi
 for SPEC in 100000:7 1000000:7 1000000:4; do
  IFS=: read -r N MASK <<< "$SPEC"
  for V in $ORDER; do
   TAG="$V-$N-$MASK-$SEED"
   SAMPLE_OUT="$P/matched-profiles/$TAG.hist.csv" timeout 30 "$P/build/$V-profile-enabled" --size "$N" --ops 100000000 --member-bytes 16 --mask "$MASK" --encoding integer --direction forward --seed "$SEED" > "$P/matched-profiles/$TAG.stdout" 2> "$P/matched-profiles/$TAG.stderr"
  done
 done
done
