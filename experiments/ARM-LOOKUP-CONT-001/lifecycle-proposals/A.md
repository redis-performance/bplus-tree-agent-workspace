# A — bounded baseline lifecycle correctness diagnostic

Choose a **separate untimed lifecycle diagnostic**, not candidate implementation. The completed census establishes 124/500 useful primary exposures and two additional miss-filter positives. It exercises none of the maintenance that makes stale hints safe. Three candidate implementations plus their missing correctness, target-code and performance gates cannot responsibly close in the remaining window. A small diagnostic can close specific lifecycle risks without borrowing performance acceptance.

Freeze one deterministic 64-member fixture, hash seed 17, unique binary payloads with lengths 0, 1, 7, 8, 253, 254, 255 and 384 (exact byte-construction table frozen before execution; only one empty member). Scores are exact integers 1–64. Use the original source `16def20f…` and a separate generated copy of the reviewed shadow instrumentation; preserve the completed six-case census and all variants.

Freeze these operations in order:

1. Construct through ordinary insertion, finish existing migration within a declared 256-step bound, then call the original `zbtIndexRebuild` once. Require rebuild-origin seeds and a noncentral seeded position in a nonreversed leaf with at least two members. Select the lowest eligible bucket by a fixed rule, solely for correctness coverage.
2. Invoke the original `zbtScoreLeafReverseForPop` on that leaf. This reverses physical arrays while preserving logical contents. Require its copied seeded identity to become stale in range. Query the original seeded member and require full-search success despite the failed hint.
3. Duplicate the tree through `zbtreeDup`. Require a distinct allocation generation, unchanged copied hint codes/seed identities, and the same stale classification. Do not refresh hints during duplication.
4. On the duplicate, call the original `zbtIndexSetId` for that selected slot zero with its existing full ID. Require invalidation even though the ID is unchanged; logical contents must remain unchanged.
5. Rebuild the duplicate once. Require fresh rebuild-origin seeds at current physical positions, then free both trees. Construct one fresh identical tree and check that new generations never inherit retired hints; physical address reuse is recorded if observed, not assumed.

After each live-tree stage, compare all 64 members against an independent sorted-vector model, exact bytes/order, score bits, rank and negative output sentinels. Exercise membership, score and position output combinations through the original lookup interfaces. Record stage boundaries, table generations, seed origins, invalidations, stale classifications and original-search results. Complete original destruction before success; require zero live generations and empty contexts. No shadow result may skip the original leaf call.

Use a new `slot-lifecycle` harness with one fixed mode and a separate strict JSON checker. Preserve all current generation, schema, checksum, clock-denial and real-call static gates. Freeze bounds: 4096 query records, 65536 leaf/filter/mutation records, 16 live tables, 1024 buckets/table, 4096 lifecycle records, 384-byte seed snapshots. No searching alternative seeds or increasing bounds after failure.

Run four serial Intel-only processes: original control and shadow, each native and ASan/UBSan, with identical fixture/model. Require exact stage-result and owned-byte agreement within each build pair. Per-process external timeout: 60 seconds; no elapsed result or speed interpretation. Independent code/parser review must finish by 06:25, and execution must start by 06:35 and close before 06:45; otherwise NONE. Assertion, coverage, sanitizer, model or timeout failure stops the diagnostic without retry.

Remaining risks explicitly include out-of-range stale hints, full-ID boundaries, scan, real resizing transitions, defrag and allocator-address reuse when unobserved. This targeted harness is maintainable because it reuses original operations and fixed independent models; it does not qualify a candidate or replace the broader correctness matrix.
