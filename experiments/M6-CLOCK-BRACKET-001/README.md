# M6-CLOCK-BRACKET-001 — harness revision and fresh qualification

Protocol revision2, frozen before native build. [Current status](STATUS.md).
User authorized “y go” after the clock-bracketing recommendation.
Interactive M6 controller owns this separate harness campaign; source selection NONE.
No tree implementation/proposal population is started. This is a new referee revision;
EXP-009 and M6-METROLOGY-001 remain frozen with their original decisions.

Implement w0,t0,w1 / unchanged lookup body / w2,t1,w3, recording all six timestamps,
nominal clock resolutions and CPU/QoS snapshots outside the whole bracket. No profile
or counter hooks allowed in this frontend. Preserve lookup loop, query generation,
assertions, allocations, warmup and checksum checks from EXP-009 byte-for-byte.
Keep old CSV columns and append new fields. Tree/header/adapter/referees remain pinned.

One falsifiable control question: does the recorded estimator detect a fixed blocking
perturbation while preserving exact CPU-work output and nonempty conditional bounds?
The fixed72-row control schedule is24 repeats of empty/CPU/20msblocking in that order.
All raw timestamps/overshoots/interruptions remain. No empirical control or nominal
resolution establishes worst-case clock accuracy. Physical attribution stays UNVALIDATED.
CPU loop checksum is independently computed by affine-map exponentiation modulo2^64.

Build strict native and ASan/UBSan binaries; run both original43-test suites and
hit/miss/mixed lookup smokes across8/16/319/320/321/1024-byte members. Validate the
added CSV algebra and retained fixture/checksum against the old frozen frontend.
Inspect actual native codegen for read ordering and identical tree function bodies.
Obtain independent harness/protocol review before native timing. Freeze/publish the
harness separately before controls and fresh baseline qualification.

Then exclusively and serially run the fixed control schedule and48 same-binary lookup
processes: six ABBA blocks per100K/1M, seeds1/2/3 twice, alternating size order, original
fixed counts13,834,448/4,978,427 and one warmup pass. Wall acceptance remains±1% in
EVERY block, windows>=10ms. Fixed counts are a new protocol choice, not a retry of the
old unchanged frontend: six bracket timestamps and empirical controls are new.
No baseline calibration, duration inflation, failed-row exclusions or source timing.
If controls fail, record their failure and skip qualification. If A/A fails, PARK
this fresh baseline without rerun. Preserve successful prerequisites and failures.

The exact budget/gates are in PLAN.json. Native phases have separate journals/hashes,
process-group cleanup and no overwrite/retry. All retrieval/review work pauses before
reserved local M6 timing; no remote runner or private SSH access is used. Publish
ownership before timing and release it afterward. Corrected baseline source, compiler,
flags and allocator match EXP-009. Clock bounds are conditional diagnostics; wall
qualification alone never constitutes accepted optimization. Counts remain unchanged.

## Pre-native review refinement (protocol revision2)

Before any native execution, independent C review identified that a zero-error empty
conditional interval can reflect clock quantization/accounting uncertainty, especially
on empty bodies. Preserve these flags as attribution-INCONCLUSIVE; they are not fatal
structural/sensitivity failures. Valid clocks, counts, checksums, sleep sensitivity and
wall A/A gates remain mandatory. No guessed tolerance or accuracy claim is introduced.
Original PLANv1 is retained in plan-history; PLAN.json records its hash/reason.
The inner sleep bracket uses the same monotonic clock; it is not an independent clock.
