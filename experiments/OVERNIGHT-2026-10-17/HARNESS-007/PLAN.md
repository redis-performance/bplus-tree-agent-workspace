# HARNESS-007 — steady-state public batched score lookup

Separate referee addition, not a source candidate. Preserve all old harness snapshots
and root referee. Extend HARNESS-003 frozen baseline with a new standalone
bench/batch_lookup.c, using public APIs, independent query shuffle and unchanged allocator.
The prior partial-batch transition oracle supplies correctness context, not timings.

Measure complete batch assembly, public zbtreeScores, exact mask checking and score
checksum consumption; report wall ns/requested member as primary, API call count,
hit count, exact effective lanes, thread time, boundary CPU IDs and reported QoS.
Those observations cannot establish stable frequency, effective QoS or placement.
Use fixed warmup passes matching layout and batching. Setup validation drains active
migration before warmup; this fixture does not measure resize transitions.

Fixture n, keybytes, constructionseed, independent queryseed, batchsize1..16,
layout hit/miss/mixed, and ops explicitly recorded. Final partial batch consumes only
remaining lanes, no rounding; mixed alternates global operation positions, even=hit.
Binary keys use fixed-endian IDs and embedded zeros; score=id. Full lookup/model checks
before/after and exact memory equality guard remain. Invalid args exit2.

Before freezing for A/A: nativeO3 and O1ASan/UBSan with unchanged debug options;
540cases/build from n1/17/257, bytes8/16/319/320/4097, batches1/2/3/7/15/16,
hit/miss/mixed, ops1 or n+3. Seeds80603/query80611. Python independently reconstructs
PRNG shuffles/fingerprints, hit counts/checksums/API-call counts. Invalid inputs and
deliberate wrong-count/wrong-query/wrong-checksum controls must be detected.
Children serial<=120s; no correctness/builds overlap later A/A. A/A plan is separate
and frozen only after validation; no automatic performance acceptance.
