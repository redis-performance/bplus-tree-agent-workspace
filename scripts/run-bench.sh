#!/usr/bin/env bash
set -euo pipefail
if [[ $# != 3 ]]; then
    echo "Usage: $0 /absolute/base-binary /absolute/candidate-binary NEW-OUTDIR" >&2
    exit 2
fi
base=$1
candidate=$2
out=$3
[[ -x "$base" && -x "$candidate" ]] || { echo "Both binaries must be executable" >&2; exit 2; }
blocks=${BLOCKS:-3}
[[ "$blocks" =~ ^[0-9]+$ && "$blocks" -ge 3 ]] || { echo "BLOCKS must be >=3" >&2; exit 2; }
args=(--size "${BENCH_SIZE:-100000}" --ops "${BENCH_OPS:-1000000}" --member-bytes "${MEMBER_BYTES:-16}" --seed "${SEED:-1}" --case "${CASE:-all}")
if [[ -n ${CPU:-} ]]; then
    command -v taskset >/dev/null
fi
mkdir "$out"
python3 - "$base" "$candidate" "$blocks" "${CPU:-unbound}" "${args[@]}" > "$out/manifest.json" <<'PY'
import hashlib,json,platform,sys
from datetime import datetime,timezone
from pathlib import Path
a,b,blocks,cpu,*args=sys.argv[1:]
print(json.dumps({"utc":datetime.now(timezone.utc).isoformat(),"system":platform.system(),"release":platform.release(),"arch":platform.machine(),"blocks":int(blocks),"cpu":cpu,"args":args,"binaries":{name:{"sha256":hashlib.sha256(Path(path).read_bytes()).hexdigest()} for name,path in [("A",a),("B",b)]}},indent=2))
PY
for ((block=1; block<=blocks; block++)); do
    step=0
    for label in A B B A; do
        step=$((step+1))
        binary=$base
        [[ "$label" == A ]] || binary=$candidate
        run=("$binary" "${args[@]}")
        if [[ -n ${CPU:-} ]]; then run=(taskset -c "$CPU" "${run[@]}"); fi
        "${run[@]}" > "$out/block-$block-step-$step-$label.csv" 2> "$out/block-$block-step-$step-$label.stderr"
    done
done
echo "Recorded $blocks ABBA blocks in $out; interpretation and confirmation remain required."
