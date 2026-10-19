# C benchmark review: Lemire blog examples and cbitset

Source inspection, not a claim that upstream code was run on M1/M6. Reviewed relevant
C examples and helpers, not every program in the repositories. No copied x86 code,
new dependency or changed tree harness is included in this review.

Revisions: blog `5ea4c8035aadccd30620ac85884aa460fc8c52a7`; cbitset
`b9f6ccaeedf54bff2a4cc2eaf4b659a532caa4ec`. [Fetched file manifest](review-sources.json)
records URLs and SHA256. Full fetched files remain in local temporary storage;
links identify the public originals.

## What we should do better

### 1. Make the output contract part of the benchmark name

cbitset's [iteration comparison](https://github.com/lemire/cbitset/blob/b9f6ccaeedf54bff2a4cc2eaf4b659a532caa4ec/benchmarks/lemirebenchmark.c)
compares one-at-a-time iteration, callbacks and buffered batches. It separately
counts outputs and sums their values. The blog's
[bitmap decoder](https://github.com/lemire/Code-used-on-Daniel-Lemire-s-blog/blob/5ea4c8035aadccd30620ac85884aa460fc8c52a7/2018/02/20/bitmapdecode.c)
also separates array-producing and callback paths and varies bitmap density.

Our standard `iterate` consumes scores only. It does not measure member decoding,
full member-byte consumption, callback delivery, or materialized batches. We already
have historical iterator-output fixtures: reuse their semantic oracles rather than
inventing another broad test suite. Add explicit modes for scores; member+length+score;
and materialized arrays, with identical downstream work on both candidate/control.
Count-only output is a separate diagnostic, not evidence that value decoding is cheap.

Concrete optional experiment ITERATE-001: compare repeated scalar calls with a private
bulk adapter that returns the same outputs in batches 1/8/32/96, at all five tree
sizes. Profile first. This may test whether EXP-007's bulk benefit transfers to real
traversal. It is distinct from EXP-008's rejected scalar cutoffs and from claiming a
public API optimization. No API change is adopted during the night.

### 2. Distinguish single-query latency, independent throughput and batching

The blog's [batchbinary.c](https://github.com/lemire/Code-used-on-Daniel-Lemire-s-blog/blob/5ea4c8035aadccd30620ac85884aa460fc8c52a7/extra/batchbinary.c)
interleaves multiple independent search states rather than merely calling the same
single-query loop repeatedly. This motivates a separate throughput question; it
does not prove a gain for our index.

Our own proposed extension: retain independent query streams and add a dependent
chain where each returned rank/score selects the next valid query. The same starting
set and a verified complete permutation must prevent accidental tiny hot cycles.
Report dependent-chain ns/query separately, including chaining overhead; do not
subtract it or compare it as if it performed the same work as the throughput loop.
Use independent batch sizes 1/2/4/8/16 as separately named workloads. Existing
EXP-006's batch/single-query disagreement makes this particularly relevant.

### 3. Control cache preparation explicitly

[understandingbinsearch.c](https://github.com/lemire/Code-used-on-Daniel-Lemire-s-blog/blob/5ea4c8035aadccd30620ac85884aa460fc8c52a7/extra/understandingbinsearch.c)
and the [shotgun search test](https://github.com/lemire/Code-used-on-Daniel-Lemire-s-blog/blob/5ea4c8035aadccd30620ac85884aa460fc8c52a7/extra/search/shotgun/shotguntest.c)
use explicit cache preparation and independently generated query fixtures, with
correctness checks alongside the timed comparisons.

For us: warm the actual operation; keep construction/query seeds independent; add
one fixed cache-disturbance experiment only when a profile supports a locality
hypothesis. Record bytes touched and the exact preparation method. On Apple hosts,
do not copy x86 clflush/rdtsc helpers or call an eviction-buffer pass a proven cold
cache. A 1M-member set alone does not establish cache misses. This is optional work
inside LOOKUP-001's budget, not another unbounded campaign.

### 4. Match the microkernel to the physical layout

[searchtinyarray.c](https://github.com/lemire/Code-used-on-Daniel-Lemire-s-blog/blob/5ea4c8035aadccd30620ac85884aa460fc8c52a7/extra/searchtinyarray.c)
compares scalar, unrolled and SIMD search on a deliberately small array. Its lesson
for us is to benchmark the actual leaf-tag lengths and inner-node prefix lengths,
including tails and first/middle/last/missing matches. Full-tree cardinality does
not specify those local shapes. Collect shape counts untimed, then use realistic
kernel fixtures. SIMD is a candidate, not an assumed winner or a copied AVX path.

### 5. Spend less time rebuilding fixtures during targeted exploration

The examples commonly prepare data once, then repeat a small kernel. Our decoder
already follows this. The whole-tree matrix builds a separate tree for each case
in every process: useful for isolation, but expensive at 1M and unsuitable as the
inner loop of every code edit.

Use `--case` for focused public-API screens, and a new frozen targeted harness with
multiple warmed batches per process. Keep ABBA at the process level, retain within-
process distributions, and do not treat those samples as independent replicates.
For mutations restore state or use bounded independent replicas; repeat calls do
not imply repeat workloads. Full five-size/all-operation coverage remains the final
guard, rather than the first test after every edit.

## What we should retain instead of copying

Our raw CSVs, hashes, monotonic wall timer, sanitizer checks, exact-value oracles,
A/A controls, paired comparisons and held-out confirmation are useful safeguards.
The old [benchmark helper](https://github.com/lemire/Code-used-on-Daniel-Lemire-s-blog/blob/5ea4c8035aadccd30620ac85884aa460fc8c52a7/2018/01/15/benchmark.h)
uses architecture-specific timing and estimated-overhead subtraction; some checks
are inside timing and others outside. Choose and freeze our own boundaries rather
than adopting these macros verbatim. Keep minima plus medians/ranges, not only minima.

Two concrete cbitset caveats at the inspected revision:
- [CMakeLists.txt](https://github.com/lemire/cbitset/blob/b9f6ccaeedf54bff2a4cc2eaf4b659a532caa4ec/benchmarks/CMakeLists.txt)
  builds both executable names from `benchmark.c`; the richer `lemirebenchmark.c`
  is not selected by the target named after it. Verify source-to-binary provenance.
- [benchmark.c](https://github.com/lemire/cbitset/blob/b9f6ccaeedf54bff2a4cc2eaf4b659a532caa4ec/benchmarks/benchmark.c)
  repeatedly intersects the same mutable bitset without restoring its initial state.
  Later repetitions operate on the intersection result. Also, its ns conversion is
  based on clock() CPU time, while the other file uses gettimeofday(). These are
  not drop-in replacements for our wall-clock methodology.

## Priority within the existing night

First: operation-specific warmup/batching and rank's real node shapes. Next: split
single-query versus independent/batched lookup; retain update-path decomposition.
The optional last experiment may be ITERATE-001 or DECODE-001, chosen from profiles
before implementing variants. Both must share the existing one-hour fallback slot;
skip the other explicitly. Cache disturbance is a bounded diagnostic, not mandatory.
