# B: a separate, bounded lifecycle correctness diagnostic

**Choose lifecycle correctness, not candidate implementation.** The actual census found 124/500 useful primary queries and two extra shadow miss-filter positives, but exercised no stale hints, counted ID mutation, Rebuild, duplicate or defrag path. Building a candidate now would convert a representation/lifetime uncertainty into production edits before validating it. No speed projection follows from exposure.

Propose one new, explicitly separate untimed harness over the frozen instrumented source and existing shadow policy. Do not alter or rerun the completed census, its checker, bounds or fixtures. The harness can inspect existing shadow state at fixed checkpoints without enabling the census's fixed-500-query event stream. Every membership/score answer still comes from the original production lookup. A new small strict checker admits only the fixed checkpoint transcript and final completion fence; no timing fields.

Fixed sequence (no search for a favorable fixture):

1. Seed17; create 2,048 unique binary members, alternating lengths16/128/384, with a fixed embedded-zero pattern and an encoded unique integer. Insert ascending scores1..2048 through FindForAdd/InsertNew, preserving its returned position. Keep an independent array model and immutable member buffers.
2. Delete exactly IDs0,2,...,126 individually. Validate all2,048 membership/score answers, sorted iteration and rank against the model. Audit every enabled shadow hint's copied seed identity against its current record; require at least one unchanged and one stale hint, plus nonzero ID writes/invalidation since insertion. Missing coverage means INCOMPLETE, not permission to change deletions.
3. Duplicate the mutated tree with zbtreeDup. Require distinct allocation generations and exact copied hint code/hash/ID/length/bytes, including at least one stale hint. Verify both sets against the model. No reseeding during duplication is allowed.
4. On the original only, delete inclusive ranks512..1536: exactly1,025 deletions from1,984 members. Source zbtreeDeleteRangeByRank explicitly takes Rebuild when deleted>1024 and deleted>=length/10. Require this path, Rebuild-origin seeds and original table retirement. Validate the959 survivors and the unchanged1,984-member duplicate independently.
5. Free the original; verify the duplicate again, then free it and all caller-owned buffers. Require zero live generations and empty contexts before final JSON.

At each checkpoint, enumerate hints using copied seed bytes, never a retained record pointer. Full current predicate and original lookup results must agree whenever a hint succeeds; stale hints may fail and fall back. Query mismatch alone must not establish staleness. The external-member cases make freeing the original before rechecking its duplicate meaningful ownership coverage.

Hard bounds:2,048 members,384 bytes/member, at most2 live sets,16 table generations simultaneously,1,024 buckets/table,4,096 lifecycle records,65,536 total verification lookups; no unbounded completion/search loops. Keep counters checked before increments. No defrag, forced address reuse, active-resize coverage or IDs>32767 claim: those need separate tests, not rushed allocator callbacks.

At05:59UTC approximately45 minutes remained. Freeze code/schema by06:15, independent source/static review by06:30, and one owned-Intel untimed execution completed by06:45. If any deadline, coverage assertion, build/static identity or correctness gate fails, stop as INCOMPLETE/NONE; no adaptive retry, ARM reacquisition or failed-control retry. Native alone suffices for this narrow correctness question if declared before implementation; no compiler comparison or adoption follows. Existing operational cleanup/deadline review remains mandatory.

This proposal is independent of other new proposals. It builds on my earlier diagnostic reviews; I am not the implementation author. The prior source consultation supplied no supporting passage. All TMA roots and children remain unavailable. No source changed or C/fleet execution occurred for this proposal.
