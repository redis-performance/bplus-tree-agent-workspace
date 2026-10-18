# Small packed-score decoder benchmark

This isolates `zbtScoreLeafScore` and EXP-004 A's one-line predicate change. It is
a throughput microbenchmark of synthetic, cache-warmed packed leaves. It does not
measure tree traversal, member decoding, iterator output modes or dependent latency.
The score-plus-length iterator guard remains unresolved regardless of these results.

```sh
make decoder-check
make decoder-sanitize
build/decoder/base/decoder-bench --width 63 --samples 129 --rounds 64
build/decoder/A/decoder-bench --width 63 --samples 129 --rounds 64

# Serial same-binary A/A and baseline/A; output directory must be new.
python3 scripts/run-decoder.py --out scratch/decoder-example
python3 scripts/analyse-decoder.py scratch/decoder-example
```

The build script reconstructs A and verifies its SHA256 against the original EXP-004
freeze. Main `src/` is unchanged. Baseline and A have separate source/kernel objects;
driver and allocator object bytes are shared. No LTO. The actual production decoder
is included in the kernel translation unit so it can inline naturally. The benchmark
driver is compiled separately, preventing constant propagation of CLI fixture values.
Default flags are C11, O3, frame pointers, warnings-as-errors. `build.json` records
compiler, exact commands, source hashes, object hashes and executable hashes.

Fixture construction, bit-level verification, allocation and printing are outside the
timed region. An independent scalar bit writer and ordered-to-IEEE conversion provide
exact expected results. These synthetic leaves contain valid finite encodings but are
not necessarily sorted or minimally encoded as a complete production tree would be.
Boundary self-tests cover all widths 0..64, both physical directions, seven leaf sizes
and zero/maximal valid score shifts. Timed values include zero, large and seeded deltas.

Defaults: eight leaves, 96 scores each, 64 rounds per batch, 16 warm-up batches and
129 measured batches in one process. Four independent uint64 checksum chains retain
every result; count/checksum checks follow timing. A compiler memory barrier at the
round boundary prevents invariant decoding from being hoisted out of repeated rounds.
The loop includes address arithmetic, branches, checksum and wrapper costs. Inspect
`build/decoder/{base,A}/kernel.s`: there must still be packed loads/decoding inside the
round loop. Width zero legitimately has a simpler path. No empty-loop cost subtraction.

Every CSV row reports actual decode count, allocated leaf bytes (excluding reference
arrays/fixture overhead), reachable bit-offset mask, ninth-byte crossings, fixture
fingerprint, checksum, elapsed ns, ns/decode and boundary CPU IDs. A crossing requires
`width + ((physical_position * width) & 7) > 64`; arbitrary width/offset combinations
are not manufactured. For example width 64 is always byte-aligned, and width 60 never
needs the ninth byte at its reachable offsets. Allocations are reused within a process.

macOS uses `mach_absolute_time` with its reported timebase. Linux uses
`CLOCK_MONOTONIC_RAW` when available. Timer ticks are **not CPU cycles**. Timer-floor
and empty-call observations are printed on stderr; no overhead is subtracted. CPU IDs
cannot exclude migration within a batch. Cache residency is intended by the small
working set/warmup, not established with cache-miss counters. Frequency and effective
QoS are unknown on the local Mac. Nothing changes affinity or system power settings.

Optional Linux `--counters` requests per-thread user-space cycles/instructions through
`perf_event_open` in a **separate pass after timing**. Allocation, fixture validation,
printing and clock calls are outside the counter bracket; wrapper/checksum and
user-space enable/disable boundaries remain. Unsupported/denied counters are reported
unavailable, never zero. Multiplexed/invalid samples are rejected without scaling.
This Linux-only path needs validation on an actual permitted Linux host; the local
macOS validation covers the explicit unavailable path. No privilege changes are made.

The runner rotates cells in fixed ABBA blocks, alternates two fixture seeds, runs the
exact same binary for A/A, then compares baseline/A. It preserves every inner sample.
Analysis reports minimum, median, p90/max per process, paired minimum/median effects
and their block ranges, plus histogram bins. Inner samples are correlated and are not
treated as independent experimental replicates. Minima describe observed best-case
batch throughput; they do not substitute for iterator guard acceptance or hide spread.

This design follows the small isolated-operation, warmed-data, assembly-inspection and
short-repetition ideas in [Daniel Lemire's methodology](https://lemire.me/blog/2018/01/16/microbenchmarking-calls-for-idealized-conditions/).
It retains a distribution alongside the minimum. His idealized conditions are a target;
this uncontrolled Mac does not satisfy every condition. The CPU Performance Engineering
MCP was consulted; its broad retrieval was not direct evidence for this decoder.
