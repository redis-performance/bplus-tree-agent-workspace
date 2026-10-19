# Corrected ARM NEON population: fixed validation and discovery

Root chair selects one exact16-byte NEON all-match hypothesis under corrected source
13e459ff8800be3f02b6b45c87dd7b0c39453fa9. Actual independently authored A/B/C patches
are pinned in inputs-freeze.json. Original8fab failures remain final. Only src.c changes;
all original source/referee files come from this exact source. Root static review passes
all three and independently checks all65536 comparison patterns for both mask reductions.
Maintenance preference is B,C,A (A28 changed non-comment lines,B26,C26; B wins B/C tie).
No candidate timing is authorized until full validation and exact schedule review.

## One fixed600s native correctness job

SerialCPU2 via owned helper; no benchmark timings. Isolated base/A/B/C source snapshots.
Identical relative frontend paths, native-O3 and ASan/UBSan-O1 options, allocator,
assertions, hash and compatibility adapter; no added ISA flags. Original43 tests in
both modes for all4 sources. Same unchanged V2 all-match oracle (299664checks),
scan_interval_oracle,wide_scan_oracle seeds7/19,live_widen_scan_oracle seeds7/19,
resize_generation_oracle in both modes. All outputs must match baseline per build,
oracle and seed. Every designated forced-portable candidate macro additionally runs
V2 in both modes. Native codegen is retained for every source; complete-word native
vector behavior and full portable fallback remain separate correctness obligations.

Retain prior x86 fault-control generator verbatim for provenance, but do not execute
its SSE2-specific aligned-load mutation on ARM. Four isolated A-derived mutations:
omit folded-zero equality, reverse physical lane order, omit residual tags after a
vector, and load16bytes when only one complete8-byte word remains. Each must fail V2
in native and sanitizer modes (eight negatives). The last fault deliberately crosses
the protected input edge and replaces the architecture-specific aligned-load fault;
it is not falsely reported as identical to the old x86 mutation. Fault-only ASAN_OPTIONS
symbolize=0 avoids diagnostic symbolizer stalls; memory checking remains enabled.
Original positive validation retains normal sanitizer runtime and complete cleanup.

Every command/returncode/stdout/stderr/timestamp/timeout retained, including failures.
A failed candidate is ineligible; no repairs after timing. Hard600s includes all builds,
originaltests/oracles/negatives/codegen. No extension or silent skippedcoverage. Existing
AA timing binary869425ed06643058e561df05177d1b85c42c9f662c5a80654c25caca02349055
is checked unchanged. Rebuilt validation baseline .text must match it exactly; all
source/referee and candidate binary hashes checked before/after. Only original AA
binary is used for discovery control. Full build flags/compiler in frozen artifacts.

## Fixed discovery, pending root timing review

One300s owned timing phase,144 serial processes. Sixblocks; eachblock rotates variants
A/B/C byblockindex, and alternates sizeorder100K/1M versus1M/100K. For each variant/size,
baseline/candidate/candidate/baseline. Original16-byte fixture,5M requestedops,
seeds401/402/403 twice. Exact raw schedule and driver are published before timing.
No retries, count changes, exclusion of firstblocks or failedrows, shortenedguard claim
or post hoc source fallback. Bothprimaries require <=−2% in everysix qualified blocks,
exact fixture/checksum/operations/tree-owned memory/CPU2 parity. Incomplete/noisy means
PARK. Among survivors maintenance preference B,C,A, not a statistical speed ranking;
identical codegen cannot support intrinsic performance ranking. No survivor means NONE.

Only selected survivor may proceed to separately frozen fresh501–503 confirmation,
48A/A and48ABBA,300s each, and all corrected-adapter original/focused/supplemental guards.
The corrected full baseline currently qualifies21/40cells; missing controls are not
waived. Matched profile and independent adversarial review remain required. No overnight
source adoption authorized. No newexperiment after07:15UTC; work ends08:00UTC.
