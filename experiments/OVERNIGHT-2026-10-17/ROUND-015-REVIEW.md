# Round15 sequential adversarial review

Independent reviewer startup failed before execution. This is a separate coordinator
review, not an independent participant. Backend/model/token cost unknown; supervisor
records actual CLI usage separately. No source acceptance can follow this review alone.

- Natural wrap is reached through public reserve/insert/delete operations, never by
  shortening or writing the16-bit counter. Both low/high states receive complete models;
  growth direction, new leaf IDs, destination references and actual tag1 are observed.
  Multi-member batches exercise both a still-active resize and completion during flush.
  Exact finite half-integer scores and negative zero, binary lengths, ownership and clone
  independence remain checked. Natural-wrap fixtures intentionally use inline319-byte
  members; external-member ownership is covered by the separate SCAN fixtures.
- The singleton batch fault SURVIVES and remains visible. Prematurely migrated singleton
  leaves can still insert their one member normally. A fresh two-member fixture catches
  that flaw. The failed12-member two-leaf prediction is retained;13members strengthen
  coverage against the compiled conservative size budget without lowering a gate.
- SCAN callbacks check exact CURRENT membership; duplicates are legal. The independent
  scalar reversal checks the documented per-call interval invariant, while whole scans
  verify continuous anchors. That interval is specific to the documented cursor algorithm,
  not a universal requirement of every possible opaque-cursor implementation. A future
  different cursor design needs separate referee review. Production uses a different
  carry/clz implementation, and no production scan helper computes expected intervals.
- Same-size cleanup is observed with only56/256members copied and five uncopied leaves.
  Initial revision assumption was invalid: ordinary insertions do not change the index
  epoch. Revised checks require equal-before/different-after actual resize. The old failure
  is retained; unconditional source checks and all other ownership/model checks remain.
  Cached insertion positions are used only for the same member/hash; updates use fresh
  successful FindForAdd positions. No stale score position or iterator is dereferenced.
- Whole-oracle branch counts prove bounded reachability, not hotness or CPU time. Raw
  coverage file IDs are resolved before extracting statements, including macro expansions.
  Captures include setup and model verification; no comparison timing or noise remedy is
  inferred. Earlier frequency/effective QoS/within-window migration unknowns remain.
- Fresh-seed debug-enabled/disabled validation is an additive build matrix. The disabled
  build still retains every oracle CHECK and unconditional serverAssert; prior debug runs
  remain. Omitting REDIS_DEBUG matches that aspect of benchmark compilation, not a claim
  that all generated code/flags match every historical timing binary. This cannot change
  timing assertion settings or qualify an optimization. Outcomes belong in the separate
  confirmation summary and final audit, not assumed from compilation success.
- All physical results are local to these snapshots and allocator history. Exact owned
  bytes are independently recomputed, but no memory saving/guard comparison is claimed.
  Sanitizer success is bounded evidence, not a general proof of leak freedom or portability.
  Root source/referee and prior immutable evidence must pass the final hash audit. All
  candidate/fault patches stay isolated; uncommitted provenance awaits morning review.
