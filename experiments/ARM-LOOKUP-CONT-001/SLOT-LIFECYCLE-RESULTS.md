# Slot-hint lifecycle correctness results

**The single fixed native check passed; selected source remains NONE.** Independent source, emitted-code, semantic and operational reviews agree. This baseline diagnostic exercised mutation and stale-hint cases absent from the earlier census. It contains no optimized fast path and measures no performance.

The source/schema froze at06:12:48UTC, before06:15. Actual native-code review passed at06:17, before06:30. One fixed native process and its saved-output checker completed successfully, with final isolation at06:18:03, before06:45. There were no C retries, fixture changes, bound changes or deadline extensions.

| Checkpoint | Members | Enabled hints | Unchanged | Stale | Out of range | Original full-search successes |
|---|---:|---:|---:|---:|---:|---:|
| After insertion | 2,048 | 493 | 493 | 0 | 0 | 493 |
| After64 deletions | 1,984 | 436 | 380 | 56 | 28 | 436 |
| Original after duplication | 1,984 | 436 | 380 | 56 | 28 | 436 |
| Duplicate | 1,984 | 436 | 380 | 56 | 28 | 436 |
| Original after rank deletion/Rebuild | 959 | 250 | 250 | 0 | 0 | 250 |
| Duplicate after original Rebuild | 1,984 | 436 | 380 | 56 | 28 | 436 |
| Duplicate after original destruction | 1,984 | 436 | 380 | 56 | 28 | 436 |

The64 individual deletions produced57 slot-zero ID writes and57 hint invalidations. Of the56 retained stale hints,28 are out of range and28 remain in range with a different physical record. All436 enabled seed identities still succeed through the original full search. These observations support the need for the complete bounds/tag/hash/length/bytes predicate and fallback; they do not measure its cost.

Duplication copied all436 enabled hints, including56 stale hints, into a distinct generation without reseeding. Exact bounded snapshots in the C harness check that original-tree rank deletion and destruction leave the duplicate's generations and complete hint arrays unchanged. Original generation8 retires and new generation10 receives250 fresh origin-2 Rebuild seeds; duplicate generation9 survives independently. All27 recorded lifecycle transitions reconcile, ending with no live generations.

Seven independent vector models verify membership, score bits, forward/reverse rank, forward/reverse iteration and exact member bytes, including unchanged negative-output sentinels. The count is57,344 public model lookups plus3,795 direct seed audits, totaling61,139, within the frozen65,536 bound. Caller-owned bytes are regenerated at every checkpoint. Final success follows both tree frees, all caller-buffer frees and empty instrumentation contexts.

Tree-owned byte observations are416,240 after insertion,408,008 after the64 deletions and for the duplicate, and202,504 for the959-member rebuilt original. Shadow memory is excluded. These observations are not a candidate memory-overhead guard or an independently fixed allocator model. The aggregate JSON does not serialize every member or hint byte: exact content and copy checks remain runtime assertions bound to the reviewed executable.

This closes the fixed native stale-hint, out-of-range, duplication and Rebuild coverage questions only. Sanitizers, defrag, forced address reuse, high IDs, active resize, arbitrary-query terminal combinations, compiler comparison and cross-ABI coverage remain untested here. Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and all children are unavailable; no profiling formed part of this correctness check.

See the [decision](SLOT-LIFECYCLE-DECISION.md), [source review](reviews/SLOT-LIFECYCLE-SOURCE.md), [actual native-code review](reviews/SLOT-LIFECYCLE-TARGET.md), [independent semantic review](reviews/SLOT-LIFECYCLE-FINAL.md), [operational review](reviews/SLOT-LIFECYCLE-FINAL-OPERATIONS.md), and [26-text/352-private-entry evidence manifest](slot-lifecycle-results/manifest.json). Canonical raw output is [native-lifecycle.stdout](slot-lifecycle-results/test/native-lifecycle.stdout). Its SHA256 is `81cbf9004a8e863fead238b0c7c2dd6d6ca76f12435acb5eb6766c35c736ed42`.

H2 and Q4 remain PARK. This diagnostic adds no performance attempt or candidate approval:47 completed attempts,25PARK,22REJECT,0approved remain unchanged. Fleet restoration is tracked separately from successful diagnostic object destruction. Intel is now RELEASED with independent live verification; the initial unloaded-unit cleanup failure and reviewed repair are retained in the [restoration record](FLEET-RESTORATION.md).
