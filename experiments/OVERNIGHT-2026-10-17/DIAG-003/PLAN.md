# DIAG-003 preregistration — repeated versus reshuffled lookup order

2026-10-17, before build and measurement. New fixture-history diagnostic, not source
candidate selection or a repeat of a failed A/A schedule. Root referee/source frozen.

Hypothesis: repeating a fixed full-fixture permutation lowers wall lookup cost by at
least 2% relative to an independently reshuffled permutation each pass. This tests
access-order sensitivity only; it does not identify cache, branch, layout or DVFS costs.
A positive result motivates fixture coverage, not a performance acceptance or noise cure.

One immutable HARNESS-001-derived snapshot, replacing only diagnostic main. Both arms
use the same compiled lookup loop, tree, keys, exact hit multiplicity and checksum.
Precompute two equally sized size_t access arrays before building the tree: R repeats
one shuffled permutation, I shuffles each full-fixture pass. I's first pass equals R's.
Both arrays are fully touched/verified before any measurement; logical-to-physical array
assignment alternates by block. Stream seed 17+block, fixed fixture/hash seed1. Tree
insertion order is independent of the access-order RNG. Each array is reused across
its two windows, so I is independent across passes, NOT freshly randomized per window.
Before every window execute ten common insertion-order warmup passes. These fixed
warmups are not evidence of settled clock or stable placement.

Fixed schedule: six serial fresh processes, one block per process, 100000 members,
16-byte binary keys, 5000000 hit operations/window (50 full passes), four windows per
process. Odd blocks RIIR, even blocks IRRI. 24 measured windows total. No normal-sized
excluded warmup process. Separate size1000/ops10000 smoke tests per build excluded
prospectively. All children <=120s; campaign <=240s, no builds/tests/agents overlapping.
Preserve all raw rows/failures; no outlier removal, optional stopping or adaptive counts.
Stop on correctness failure, timeout or budget exhaustion and classify incomplete.

Primary diagnostic: within each process compute mean wall ns/op R / mean wall ns/op I.
Criterion: median of six ratios <=0.98 AND R<I in at least five of six blocks, all24
valid windows >=10ms, exact equal checksums/counts/tree memory. Otherwise hypothesis
not supported. Print all paired ratios and each arm's two-window CV per block, pooled
CV and process means as descriptive context only. No p-value/CI from treating24
clustered windows as independent. Thread time/opaque boundary CPU IDs/requested QoS
are observations; not filters, clock estimates, stable-frequency or residency proofs.

Apple M1 ARM64, installed4P+4E, one thread, no SMT,16GiB,macOS26.3; frequency, turbo
state, effective QoS and within-window residency unknown. Apple Clang17, C11 -O3 -g
-Wall -Wextra -fno-omit-frame-pointer, libc allocator, unchanged assertions/hash.
Base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus explicit uncommitted harness patch.
Backend/model/token costs unknown; supervisor records usage. Independent review agent
startup failed before running; reviews are sequential coordinator passes, not agents.
Prior git/sample denials respected, no retry. Source selection NONE and A/A PARK remain.
