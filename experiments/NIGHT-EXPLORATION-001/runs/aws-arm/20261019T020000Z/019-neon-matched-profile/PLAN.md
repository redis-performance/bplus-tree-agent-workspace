# Matched profile of rejected ARM B: frozen diagnostic plan

Purpose: test whether the generated fold-predicate reconstruction identified in 018
receives material samples. Population 017 remains REJECT/NONE regardless of results.
No new source, build, candidate, timing comparison or acceptance is part of this job.
Root review and explicit launch authorization are required after this freeze.

Use exact existing baseline 869425ed06643058e561df05177d1b85c42c9f662c5a80654c25caca02349055
and B 1e58419358c1187f3fdfe99ddce3d9fa6e857f3f52ae43f61efc1b515233af0d,
bound to 017/comparison-freeze.json. Source, referee and binary identities checked
before and after. Existing compiler Clang18.1.3, flags, allocator, assertions unchanged.
Serial CPU2 through one owned 600-second job, including controls and analysis export.
Hard cap, no retries, no additional captures or frequency/count changes.

Fixed matrix: both binaries, sizes100K/1M, member_bytes16, requested_ops5M, seeds1/2/3.
For each seed and size, capture baseline then B on odd seeds, B then baseline on seed2.
Each of the12 cells gets one ordinary execution and one full-process cycles:u capture,
997Hz, frame-pointer callchains. Four initially disabled perf-stat controls (both
sources and sizes, seed1) must report zero/not-counted cycles. All28 executions must
preserve case/size/requested_ops/member_bytes/seed/actual operations/checksum/owned
bytes/traversals/warmup counts, and start/end CPU2. Instrumented elapsed values are
retained solely as provenance, never a speed comparison. Plain, disabled and sampled
rows must agree semantically within a cell; baseline/B must also agree for each fixture.

## Analysis scope, distinct from PMU scope

PMU sampling covers the full process. The analysis uses a fail-closed callchain filter
for the timed main→zbtreeScan call site. This is **post-filtered analysis**, not physical
timed-only PMU enablement. Setup, lookup warmup, verification, ambiguous and incomplete
stacks remain retained and counted separately. No omitted samples disappear from the
denominator accounting. Unfiltered perf.data stays runner-local with its SHA256;
full unfiltered text callchains and per-sample classification are published.

Read-only disassembly of both exact binaries verifies main starts0xf18, the timed
scan_count call is0x1d18, return0x1d1c=main+0xe04, while the postclock scan_verify call
is0x1ea4, return0x1ea8=main+0xf90. Source-linked main assembly is included. Only a stack
with exactly one physical main frame at0xe04 and no verify marker qualifies as timed.
Only0xf90 qualifies as verification. Other/missing/contradictory main frames are excluded
and classified, not guessed. Physical main ignores inlined duplicate labels. Existing
014 samples confirm this perf tool reports the actual main return PC, not call-PC.
No adjustment of these markers is allowed after observing this capture.

At least90% of sampled events whose sampled physical symbol is zbtIndexScanSlot must
be assignable unambiguously to timed or verify call sites in each capture; otherwise
that capture is insufficient for a materiality claim. All ambiguous frames are retained.
At least100 timed B predicate events pooled over the three fixed seeds at each size
are required for a stable-support label. Report each seed separately and pooled only
within the same source and size, never across hosts, sources or sizes.

Primary diagnostic region: exact35 instruction addresses per B forward/reverse
predicate reconstruction in018/analysis.json, relative to zbtIndexScanSlot0x10298.
Only the sampled instruction counts; ancestors are not charged. Also report whole
zbtIndexScanSlot sampled period/events, explicitly including lookup-ID/resize/decode/
callback setup rather than mislabeling it as only the helper. Do not attribute baseline
samples to candidate offsets. Source-linked maps/hashes remain exact.

Preregistered support criterion for this diagnostic: B's predicate has at least5% of
post-filtered timed sampled period at each size, at least1% in every seed, at least100
pooled events/size, and the stack completeness gate above. This is evidence that the
region is material in the sampled workload, not proof that it explains all regression
or that removing it yields a win. Failure or inadequate samples means unsupported or
inconclusive, with no retry. Sampling skid and unequal instruction costs limit precision.

Parser negative controls must exclude verify, missing-main, conflicting-main, and
inlined-only-main stacks. A valid timed stack must qualify and an unrelated sampled
IP must not be charged to the predicate. These use synthetic text only and do not
alter any fixture, candidate or referee. No fresh hypothesis or implementation follows
until root independently reviews the profile and attribution.
