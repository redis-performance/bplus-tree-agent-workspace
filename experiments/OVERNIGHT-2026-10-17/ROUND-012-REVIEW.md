# Round 12 sequential adversarial review

Independent reviewer startup failed before execution. This document is a separate
coordinator review pass, not an independent agent's opinion. Backend/model/token cost
are unknown; supervisor CLI usage is recorded separately.

## Semantics and test strength

BOUNDARY-015 uses independent numeric-score/binary-member sorting and scalar bit reads.
It preserves signed-zero bits despite numeric equality, includes adjacent finite values,
extreme finite values, empty/binary/external members, and checks rank/subtree counts and
leaf ownership. Clone modifications are checked against the unchanged original. Settled
SCAN may duplicate callbacks: the initial exactly-once assertion was invalid, documented,
and retained in a failed frozen attempt. The correction matches the source comment and
existing test contract; every callback still requires a live member and exact score,
and every live member must appear. Existing active-resize tests remain unchanged.

The mixed-score suite does not prove every packing width occurs naturally. Its observed
zero/partial/full-width, orientation and leaf-count coverage is explicit. Private synthetic
decoder tests separately cover widths; BOUNDARY-016 independently covers packed movement.
Its out-of-place scalar reference cannot share the source's in-place chunk-overlap mistake.
Whole-buffer equality checks untouched bits and tail clearing. Arbitrary private integer
fields are not presented as supported NaN score inputs. Four new deliberate faults are
detected by semantic assertions; timeout is never treated as detection.

## Allocation, UB and portability

All source variants pass O3/debug native and O1/debug ASan+UBSan. Controlled-capacity
adapters retain their diagnostic metadata/accounting limits and are never timing hosts
or production memory guards. All controlled fixture allocations return to zero. Complete
output equality within a controlled policy is stronger than the common logical digest;
ambient output equality is deliberately not required after the prior allocator evidence.
Scalar shifts avoid width64 UB, binary buffers have unique encoded IDs, and score models
never introduce NaN/infinity. Results remain local arm64 evidence, not cross-platform proof.

## Measurement validity

DIAG-014 discovery's contrast is selected before its fresh mirrored confirmation. The
confirmation reverses treatment labels and includes a same-predecessor placebo. Both
fresh contrast intervals pass, but one placebo interval fails: the joint criterion is
PARK. Reporting only the repeated contrast as an accepted precision remedy would be wrong.
DIAG-015 is a distinct gap intervention; its strong attenuation/placebo criteria fail.
Every row and failure remains; no outliers removed, thresholds moved, or optional extension
of either fixed schedule. No new source benchmark qualification or candidate acceptance.

Predecessor instruction mix and duration are intentionally confounded: this tests the
combined intervention. Parent-side timestamps do not measure the exact child execution
gap. Per-pair bookkeeping occurs after target exit, but can still affect later pairs.
The periodic ABBA schedule is fixed rather than randomized. Student-t intervals assume
approximately independent normal block effects; six blocks do not establish that assumption.
Frequency, effective QoS and within-window migration remain unknown; thread time and
CPU endpoints cannot resolve them. No causal cache/clock claim is warranted.

## Provenance and conclusion

Read-only audit independently recomputes all 32 wall/thread intervals and verifies 675
serial measurement windows, disjoint from 122 build/test/fault windows. Frozen files,
raw hashes, fixed counts, label order and predecessor assignments match. Root source,
header, adapter, benchmark and original test entry point retain their starting hashes.
All retained source patches survive. Git metadata protection is not retried and acceptance
remains pending committed provenance and independent morning review.

Review verdict: new local correctness evidence passes its declared checks. Performance
robustness and source adoption remain PARK/NONE. Maintainability cost is confined to
additive test/evidence drafts; production source has no change. Next work should examine
a distinct source of coordinator/process-boundary variation or use a separately qualified
runner, not repeat the failed warmup/gap schedules unchanged.
