#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 ]]; then
    echo "Usage: $0 /absolute/btree-bench NEW-OUTDIR [benchmark options]" >&2
    exit 2
fi
binary=$1
out=$2
shift 2
command -v perf >/dev/null
[[ -x "$binary" ]] || { echo "Binary must be executable" >&2; exit 2; }
mkdir "$out"
run=("$binary" "$@")
if [[ -n ${CPU:-} ]]; then run=(taskset -c "$CPU" "${run[@]}"); fi
printf '%q ' "$binary" "$@" > "$out/command.txt"
printf '\nWhole-process capture includes fixture setup and cleanup.\n' >> "$out/command.txt"
perf stat -o "$out/stat.txt" -e cycles,instructions,branches,branch-misses,cache-references,cache-misses -- "${run[@]}" > "$out/stat-bench.csv"
perf record -g -o "$out/perf.data" -- "${run[@]}" > "$out/record-bench.csv"
perf report --stdio -i "$out/perf.data" > "$out/report.txt"
