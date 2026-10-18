# DIAG-004 preregistration — insertion history with identical lookup order

Written before build/measurement. Orthogonal fixture-history diagnostic after DIAG-003
failed: vary tree construction, keep the lookup stream fixed. No source optimisation,
A/A requalification or claim that this remedies noise. Root harness/source frozen.

Hypothesis: ascending score-order insertion lowers lookup-hit wall cost by at least5%
versus shuffled insertion for100000 16-byte members. Existing EXP-001 short-key profile
shows leaf memchr work; changing leaf packing may change that work, but neither timings
nor leaf counts alone prove a cache/search mechanism. Sorted insertion uses the same
ordinary InsertNew API as shuffled insertion, not the special append API.

Instrument is a frozen HARNESS-001 snapshot plus one diagnostic option and read-only
leaf occupancy observations via iterator boundaries. Each arm has identical key bytes,
scores, hash seed, shuffled lookup order, operation counts, compiler/asserts/allocator.
Insertion sequence is the intervention. Tree-owned bytes and leaf count/min/max/mean
are allowed to differ: this is fixture coverage, not a source memory trade-off or win.
Record them, never use them to exclude a row. General harness expected checksum and
length checks remain; iterator observation verifies exact member count outside timing.

Fixed48 fresh serial processes: six ABBA blocks, two member sizes16 and320 per block,
four processes/cell. A=ascending, B=shuffled. Odd blocks ABBA, even blocks BAAB. Seeds
1,1,17,17,101,101 by block. Within odd block run16 then320; reverse in even blocks.
Every process size100000, ops10000000, warmup-passes10, case lookup-hit. No excluded
normal-fixture warmup process. Small release/sanitizer tests (1000/10000, both orders,
both sizes) excluded prospectively. Each child<=120s, total schedule<=240s. Serial only;
no builds/tests/profiles/agents during timing. All rows/failures retained, no outlier
removal, optional stopping or adaptive counts. Stop on failure/budget and mark incomplete.

Primary: per-block mean wall ns/op A / mean B for16-byte keys. Support only if median
of six ratios<=0.95 and A<B in>=5/6 blocks, all48 rows valid with expected checksum/count,
all timed windows>=10ms, memory/leaf structure stable within identical seed/arm/size.
Otherwise not supported. Long-key320 ratios and paired-window CVs descriptive only;
no posthoc promotion to primary. All three seed results reported separately. This is
not precision qualification and cannot override existing lookup PARK or speed gates.

Apple M1 ARM64, installed4P+4E, one benchmark thread/no SMT,16GiB,macOS26.3. Apple
Clang17.0.0 C11 -O3 -g -Wall -Wextra -fno-omit-frame-pointer, libc. Frequency/turbo state,
effective QoS and residency unknown; no policy changes. Wall time primary; thread time,
opaque boundary CPU IDs and queried requested QoS supplementary, not filtering rules.
Uncommitted snapshot over a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c; exact hashes/patches.
Backend/model/token cost unknown. No independent reviewer ran; sequential review only.
Source selection NONE. Any later source proposal still needs both population stages,
qualified guard workloads, profile explanation, fresh confirmation and adversarial review.
