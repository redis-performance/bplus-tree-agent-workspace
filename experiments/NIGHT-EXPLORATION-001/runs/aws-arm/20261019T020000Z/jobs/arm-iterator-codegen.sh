set -eu
cd @REPO@
P=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/005-iterator
mkdir -p "$P/codegen"
for V in base A B; do
 objdump -dS --disassemble=zbtreeIteratorNext "$P/build/$V" > "$P/codegen/$V-iterator-next.asm"
 nm -S --size-sort "$P/build/$V" > "$P/codegen/$V-symbols.txt"
 objcopy --dump-section .text="scratch/arm-iterator-$V.text" "$P/build/$V"
done
python3 - <<'PY'
from pathlib import Path
import json,hashlib
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/005-iterator')
s={v:{'text_bytes':Path('scratch/arm-iterator-'+v+'.text').stat().st_size,'text_sha256':hashlib.sha256(Path('scratch/arm-iterator-'+v+'.text').read_bytes()).hexdigest()} for v in ['base','A','B']}
(p/'codegen/sections.json').write_text(json.dumps(s,indent=2)+'\n')
PY
