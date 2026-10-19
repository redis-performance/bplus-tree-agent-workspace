set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode
mkdir -p "$OUT/codegen"
for V in base root A B C; do
 objdump -d --disassemble=decoder_batch "$OUT/build-long/$V/decoder-native" > "$OUT/codegen/$V-decoder-batch.asm"
 objdump -d --disassemble=zbtScoreLeafDecodePolicy "$OUT/build-long/$V/decoder-native" > "$OUT/codegen/$V-decoder-policy.asm"
 nm -S --size-sort "$OUT/build-long/$V/decoder-native" > "$OUT/codegen/$V-symbols.txt"
 objcopy --dump-section .text="scratch/arm-$V-kernel.text" "$OUT/build/$V/kernel-native.o"
done
python3 - <<'PY'
import hashlib,json
from pathlib import Path
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode')
rows={v:{'text_sha256':hashlib.sha256(Path('scratch/arm-'+v+'-kernel.text').read_bytes()).hexdigest(),'text_bytes':Path('scratch/arm-'+v+'-kernel.text').stat().st_size} for v in ['base','root','A','B','C']}
(p/'codegen/kernel-text.json').write_text(json.dumps(rows,indent=2)+'\n')
PY
