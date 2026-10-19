set -eu
cd @REPO@
out=scratch/amd-lowerbound-codegen
mkdir -p "$out"
for v in base A B C; do
 objdump -d -M intel --disassemble=zbtScoreLeafLowerBound "scratch/amd-lowerbound-build/$v/build/native/btree-bench" > "$out/$v-lowerbound.asm"
 size "scratch/amd-lowerbound-build/$v/build/native/btree-bench" > "$out/$v-size.txt"
done
objdump -d -M intel --disassemble=zbtScoreLeafLowerBound build/size-matrix/btree-bench > "$out/original-lowerbound.asm"
