# DIAG-001 preregistration — fresh-process versus reused-fixture windows

2026-10-17, before measurement. AA-001 remains PARK for lookup. This is a new
measurement diagnostic, not a retry of its A/A gate and not a candidate comparison.

Hypothesis: using one process/tree for six consecutive read-only lookup windows reduces
within-block wall-time variation relative to six fresh processes with the same binary,
fixture and operation count. This tests a bundle of process/fixture reuse and workload
history effects; it does not isolate ASLR, allocation addresses, cache or frequency.
It cannot by itself qualify future fresh-process ABBA comparisons.

Instrument: isolated snapshot beneath scratch/overnight-diag-001/base, derived from
HARNESS-001. The saved diagnostic patch only adds --samples and sample_index, retains
each timed/checksummed loop, and restricts the instrument to lookup-hit. Main harness
and src unchanged. One tree and ten warm-up lookup passes before its windows; per-window
expected checksum generation remains untimed. Warm-up fields describe the one process
warm-up and are repeated in CSV. Output buffered normally to a file. No mutation windows.
Freeze source/file hashes and binary SHA256 before measurements.

Host/compiler/allocator/frequency limits identical to AA-001. Apple M1 ARM64, one thread,
macOS 26.3, Apple Clang 17.0.0, C11 -O3 -g -Wall -Wextra -fno-omit-frame-pointer, libc.
No QoS/pinning change, no frequency estimate. Boundary CPU IDs remain opaque and do not
prove residency; thread time is supplementary. No overlapping builds/tests/profiles.

Fixed schedule: six blocks; each arm contributes six windows per block. Fresh arm uses
six processes with --samples 1; reuse arm one process with --samples 6. Fresh then reuse
in odd blocks, reverse order in even blocks. All windows use lookup-hit, size100000,
member-bytes16, seed1, ops10000000, warmup-passes10. 42 processes, 72 windows total.
No excluded warm-up process; every measured window retained. Child timeout120s; total
budget240s. Preserve failure/timeout and stop on correctness failure. No optional stopping.

Primary diagnostic: within-block wall ns/op coefficient of variation (sample sd/mean).
Report each arm/block CV, min/max, all raw observations and same-block reuse/fresh mean
ratios. The hypothesis is supported only if reuse CV <= half fresh CV in at least four
of six complete blocks, with identical effective counts/checksums/memory throughout.
Otherwise classify inconclusive/not supported. This fixed diagnostic criterion is not
the optimisation acceptance gate. No outlier removal or changes after observing results.
Report boundary ID changes, raw thread/wall ratios and first-to-last reuse trends as
descriptive context only. Do not filter based on these observations or substitute CPU time.

Backend/model unknown. Single coordinator; no independent agent/confirmation claimed.
Further work must preserve AA-001's PARK outcome unless a separate qualification passes.
