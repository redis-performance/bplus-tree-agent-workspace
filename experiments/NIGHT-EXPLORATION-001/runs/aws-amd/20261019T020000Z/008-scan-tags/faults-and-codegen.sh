set -eu
cd @REPO@
python3 scratch/amd-scan-faults.py
mkdir scratch/amd-scan-codegen
for v in base A B C; do
 binary="scratch/amd-scan-build/$v/build/native/btree-bench"
 size "$binary" > "scratch/amd-scan-codegen/$v.size"
 nm -S --size-sort "$binary" > "scratch/amd-scan-codegen/$v.symbols"
 objcopy --dump-section ".text=scratch/amd-scan-codegen/$v.text" "$binary"
 objdump -d --disassemble=zbtreeScanSlot "$binary" > "scratch/amd-scan-codegen/$v.scan-slot.asm"
done
sha256sum scratch/amd-scan-codegen/*.text > scratch/amd-scan-codegen/text-sha256.txt

objcopy --dump-section .text=scratch/amd-scan-codegen/frozen-referee.text build/size-matrix/btree-bench
sha256sum scratch/amd-scan-codegen/*.text > scratch/amd-scan-codegen/text-sha256.txt
