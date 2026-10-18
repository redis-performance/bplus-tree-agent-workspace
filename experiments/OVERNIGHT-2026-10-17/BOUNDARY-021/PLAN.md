# BOUNDARY-021 — natural member-resize generation wrap

Preregistered correctness-only baseline scope; retained optimization variants are
not part of this round's wrap test. Native -O3 debug and -O1 ASan/UBSan, two fixed
seeds60509/60527 per build. All source/allocator files frozen from control snapshot.
No private state mutation or shortened counter. Observe the actual16-bit field.

Keep eight low-score319-byte binary members and repeatedly insert absent members
8..28, then delete the maximum until eight remain. Exactly32770cycles per seed,
expect65540natural grow/shrink resizes. Public anchor lookups finish each observed
resize within64calls; require nonzero resize ID, sequential progression with65535
wrapping to1, anchor leaf ID stable and all live leaves tagged with the completed
ID. Require exactly one observed wrap per seed. Full sorted-vector/iteration/seek/
lookup/rank/scan/ownership check every256cycles, everycycle near wrap (32764 onward),
and before/after; constant-size state assertions everyphase. Preserve all failures.

One isolated sanitizer fault removes the zero-generation skip; it must compile
and fail at actual natural wrap, not by a shortened injected counter. Child120s,
whole baseline+fault budget360s. Record absence of variant/independent confirmation;
this cannot accept an optimization. Existing source and tests unchanged. If bounded
runtime fails, retain it as incomplete rather than reducing cycle/coverage counts.
