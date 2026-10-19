set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/002-lookup
mkdir -p "$OUT/build/attempt001" "$OUT/build/shared"
cp "$OUT"/build/*-native "$OUT"/build/*-sanitize "$OUT/build/attempt001/"
cp -a "$OUT/variant-build" "$OUT/variant-build-attempt001"
FLAGS='-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3 -fno-lto -Isrc -Icompat -Ivendor/redis'
clang $FLAGS -c "$OUT/lookup-bench.c" -o "$OUT/build/shared/driver.o"
clang $FLAGS -c compat/standalone.c -o "$OUT/build/shared/standalone.o"
clang $FLAGS -c vendor/redis/siphash.c -o "$OUT/build/shared/siphash.o"
for V in base A B C; do
 ROOT=scratch/arm-exact/$V
 clang $FLAGS "-ffile-prefix-map=$ROOT/=" -c "$ROOT/src/zset_btree.c" -o "$OUT/build/shared/tree-$V.o"
 clang $FLAGS "$OUT/build/shared/driver.o" "$OUT/build/shared/tree-$V.o" "$OUT/build/shared/standalone.o" "$OUT/build/shared/siphash.o" -lm -o "$OUT/build/$V-mapped"
 if [ "$V" != base ]; then cp "$OUT/build/$V-mapped" "$OUT/build/$V"; fi
 objdump -d --disassemble=zbtreeScoreRaw "$OUT/build/$V-mapped" > "$OUT/variant-build/$V-zbtreeScoreRaw-mapped.asm"
 sha256sum "$OUT/build/$V-mapped" "$OUT/build/shared/tree-$V.o" > "$OUT/variant-build/$V-mapped-hashes.txt"
done
objcopy --dump-section .text="$OUT/build/shared/original-text.bin" "$OUT/build/base"
objcopy --dump-section .text="$OUT/build/shared/mapped-text.bin" "$OUT/build/base-mapped"
cmp "$OUT/build/shared/original-text.bin" "$OUT/build/shared/mapped-text.bin"
objcopy --dump-section .rodata="$OUT/build/shared/original-rodata.bin" "$OUT/build/base"
objcopy --dump-section .rodata="$OUT/build/shared/mapped-rodata.bin" "$OUT/build/base-mapped"
cmp "$OUT/build/shared/original-rodata.bin" "$OUT/build/shared/mapped-rodata.bin"
sha256sum "$OUT/build/shared/"*.bin > "$OUT/variant-build/baseline-section-hashes.txt"
echo 'Original qualified baseline and mapped baseline .text/.rodata identical; original baseline retained for timing.'
