set -eu
cd @REPO@
out=scratch/amd-delete-profile
objdump -d --disassemble=zbtScoreDeleteInPlace scratch/amd-scoped-profile/base-fifo2-profile > "$out/delete-in-place.asm"
@PERF@ annotate --stdio -i "$out/delete-n1000000-s1.data" --symbol zbtScoreDeleteInPlace > "$out/delete-in-place.annotate" 2> "$out/delete-in-place-annotate.stderr"
