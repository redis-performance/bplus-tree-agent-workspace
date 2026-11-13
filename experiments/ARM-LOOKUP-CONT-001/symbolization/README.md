# Matching-ELF resolution of the sealed baseline

This is offline analysis of ARM-LOOKUP-GAP-001's existing `hit.data` and `long.data`, not a new profile or a performance measurement. The old experiment remains unchanged. No fleet access was performed by this worker.

The captured profiles name libc build ID `54ae5337044aaabab70d65e0c3444f7e4735e059`. The retrieved AArch64 ELF has that exact GNU build ID. Its SHA256 and the two input-profile SHA256 values are preserved in [libc-attribution.json](libc-attribution.json); the binary and raw profiles remain private. Controller-only dependencies were capstone 5.0.9 and pyelftools 0.33.

The ELF dynamic symbol `memchr` is an IFUNC resolver at `0x9a7b0`, size 64 bytes. Actual instructions construct `0xa13c0` as the normal target, conditionally selecting `0xa14c0`. Thus the previously unresolved sampled PCs in `0xa13c0..0xa1480` belong to a resolver-selected **memchr implementation**. No private debug symbol, guessed glibc source name, or address from another libc build is required. The implementation uses 16-byte vector comparisons and a narrowed match mask; its early return uses `rbit`/`clz`. The dynamic `memcmp` symbol spans `0x9a800..0x9a9c7` and already has specialized 1–15-byte paths.

| Profile | All samples | memchr implementation: samples | memchr: fraction of all sample period | memcmp: fraction of all sample period |
|---|---:|---:|---:|---:|
| hit | 5,984 | 1,392 | 23.3016675% | 3.4500779% |
| long | 20,627 | 1,357 | 6.5814618% | 9.7642723% |

These are period-weighted percentages, not percentages of sample counts or a selected-symbol subtotal. They include process setup, construction, warmup, and the lookup loop. Sampling skid, call-site attribution, and non-loop work prevent treating them as exact per-lookup costs. The memchr number is an opportunity-localization result, not a recoverable speedup estimate. All four qualified TMA categories remain unavailable.

Reproduction uses `resolve-libc.py ELF HIT_DATA LONG_DATA` with pyelftools available and the controller's `perf` executable. It runs only `perf buildid-list` and `perf script`, verifies the expected libc build ID in each capture, tracks recorded libc MMAP2 load addresses, and aggregates recorded sample periods at the implementation offsets. This ELF's executable PT_LOAD has matching zero file offset and virtual address, checked by the script. The script emits no host or raw operational paths. `disassemble-libc.py ELF` with capstone and pyelftools reproduces [the relevant disassembly](libc-relevant-disassembly.txt). Neither script executes target instructions or collects counters.
