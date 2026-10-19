# Independent AMD proposal for native ARM all-match scan

Author: actual `/root/aws_amd` native agent; exact inherited model, measured tokens and monetary cost unknown. Prepared from immutable ARM baseline packet `c9664ab44` and its source-linked assembly, control parity and profile analysis. No Intel or ARM proposal was read. This is a proposal only; no candidate code, build or timing. Intel B review and held-out confirmation are separate tasks.

## Selection: investigate exact bounded 16-byte native vector matching

One hypothesis: on the Neoverse V2 runner, replacing each pair of scalar SWAR tag-mask passes with one exact 16-byte native vector comparison and ordered exact-mask enumeration reduces original scan elapsed per actual callback by at least 2% in both preregistered 100K and 1M primaries, without a demonstrated >1% guard or tree-memory regression.

Keep this architecture-specific: the x86 SSE2 results are not supporting timing evidence. Preserve the original scalar word/byte implementation as the fallback and as the residual path for fewer than 16 remaining tags. Do not combine this hypothesis with callback, hashing, member decoding, index traversal or ownership changes.

## Evidence and prediction

The ARM baseline has no vector instructions in the 202-instruction all-match range; diagnostic/original encodings match there. The hot forward loop handles eight tags with scalar equality-mask arithmetic, computes ordinary/folded paths and selects a result, then re-reads potential matches to reject SWAR false positives. Its native source-linked instructions include `csel` at relative 0x3f0 and byte recheck beginning at 0x418. This makes exact vector comparisons a concrete alternative rather than an architecture assumption.

At 100K/1M, the complete all-match range accounts for 34.459%/26.769% period weight (84/85 events), forward word processing 26.344%/23.792%, and mask/fold selection 14.995%/16.866%. These overlapping ranges must not be added. Rechecks alone are only 4.689%/2.357%; simply removing byte rechecks has little demonstrated headroom. The proposed mechanism instead changes the complete full-chunk mask computation and halves the number of chunk iterations.

Prediction: full chunks produce exact ordered masks without candidate byte loads or SWAR arithmetic; empty chunks advance with one exact mask test. The unchanged member hash/decode/callback region should remain semantically identical. Native mask reduction, vector-to-scalar transfers, extra setup and code growth may outweigh the saving, especially for short or dense leaves. AArch64 provides no reason to assume the x86 mask-extraction cost. No quantitative gain beyond the falsifiable gate is promised.

The baseline captures use one million requested operations, while pending precision controls use five million. They establish an original mechanism location, not identical traversal history or a validated five-million-operation speed ceiling. A subsequent selected-candidate mechanism capture must match the timed operation count, fixtures and seed scope.

## Concrete implementation constraints for the chair

For each complete 16-byte span, form exact byte equality; tag one matches physical zero OR one exactly once. Compress lane results into an unsigned 16-bit position mask with bit i corresponding to byte i. One straightforward implementation uses explicit lane weights 1,2,4,...,128 in each eight-lane half and separate half reductions, avoiding a carry between halves. Authors may choose another provably exact mask representation; they must document lane order and mask extraction cost.

Enumerate nonzero masks from the lowest physical position and apply the original `count - 1 - position` mapping when reversed. Retain original residual word and byte logic. No load crosses the last complete 16-byte span; no overlapping vector tail or load into member records is permitted. Do not assume alignment. Count zero performs no input load/output store and never calls count-trailing-zeros on zero.

Restrict an initial specialization to supported little-endian AArch64 vector builds unless lane mapping is proven for additional targets. Preserve portable fallback on other architectures and endianness, with a source-local force-fallback test selector. Architecture gating must not globally alter compiler target flags or change assertions/allocator/hash.

## Qualification, guards and falsification

Pending fresh original A/A must be frozen and assessed without retries or operation adjustment. Keep exact source 8fab511e, original referee, isolated builds and common relative frontend paths/flags. Use the declared same-session serial ABBA schedule; retain every row and actual callback denominator. Failed controls prevent adoption even when exploratory effects pass. An eligible contender still needs independent held-out confirmation and adversarial review.

Before timing, require unchanged original43 tests, native and sanitizer V2 guard-page/canary/order oracle across counts0..96 and all tags, deliberately unaligned full spans, vector boundaries, both orientations and forced fallback. Preserve existing scan/wide-ID/live-widen/resize correctness checks. Fault controls should catch fold omission, reversed order, lane/tail omission and illegal aligned/wide loads.

Performance guards must include original operations/sizes, length boundaries8/319/320/321/1024, real-hash dense ordinary/folded tags, ties/signed-zero, broad physical reversal and active resize/migration. Frozen focused referee2ab283daa covers useful dense/external cases but only one reversed64-member leaf per descending fixture, no active rehash and no wide IDs; it cannot close those gaps. Correctness coverage does not replace performance qualification.

Reject if every-block dual-primary speed gate fails or a qualified guard demonstrates >1% regression. PARK if controls, guards, confirmation or matched-profile attribution remain unresolved. A reduction of instructions alone does not validate elapsed gain. If the chair judges native mask extraction/code-size risks too high relative to the sampled headroom, NONE is an appropriate outcome; no forced population is required.
