# H7 — exact scalar index candidate masks

Select the exact-mask mechanism nominated independently by two of the three population3 proposers; the third also identifies it as a separate viable lead. All three actual proposals are in `proposals-third/`; none read the others before finalizing. The chair separately retains range-first record classification as H8, not a component of H7. Fresh upstream fetch remains ee8e7f70152404649ac947157fd662d11b4a00d5. Every implementation starts original e13d9fc88 extraction/source16def20f…; H1–H6 patches are excluded.

The current approximate byte-zero mask can set false candidate bits through subtraction borrow. Every candidate is therefore rechecked with a variable stored-tag shift, byte comparison and branch before its leaf-ID load. Exact masks can remove that dependency at the cost of extra per-bucket arithmetic. The hypothesis is falsifiable and no speed is assumed; H4's miss failures make added miss-path work a leading risk.

Use the bounded unsigned64-bit identity `~(((x & L) + L) | x | L)`, where x is the original tag XOR broadcast and L=0x7f7f7f7f7f7f7f7f, or a plainly equivalent expression. Per-byte low7+127 cannot carry between bytes; the resulting high bit is set exactly for byte equality. Preserve numeric slot order and zero-input avoidance in first-bit extraction. No intrinsic, new load width, query cache, prefetch, batching, fixture change or branch hint.

Three independently implemented scopes of this one mechanism:

- A: add a named exact helper only for `zbtIndexTableFind`, removing only that consumer's redundant byte validation.
- B: exact helper for both table find and reference find; remove only their redundant validations, retain approximate boolean/scan users.
- C: strengthen the existing mask helper contract globally and remove now-redundant candidate checks in table/reference/full-word leaf scan. Preserve scan tails and folded-zero tag union. This has the broadest guard burden and may select NONE.

No leaf equality/decoder/boundary, negative-filter placement/formula, resize dispatch, ID representation or metadata layout changes. Keep original tombstone/free-ID/migration/bounds assertions and optional outputs. Memory must remain unchanged. A is the maintainability preference if multiple variants clear every gate; a preference is not a speed-superiority claim.

Require original57native+57sanitizer,36fixtures and135k supplied oracles. Add independent exact-mask/enumeration checks across all tags/bytes/lanes, adjacent pairs and borrow/high-bit adversaries; preserve tag0-to1 folding. Exercise multiple candidates, no candidates, tombstones, narrow/wide IDs, wrap/displacement, active/final resize and insertion hints. B additionally needs reference repair checks; C needs exact scan callbacks/cursor/tails/zero-tag/reversal coverage.

Before timing inspect exact native and target ARM ELFs, including actual no-score clones. The candidate-to-ID chain must lose the redundant stored-tag check; exact mask must have no call, no new out-of-bounds load, and a credible net dependency/work reduction. Reject static NONE if the recheck persists, raw frame grows, or four removed dependent steps are merely replaced by at least four new dependent steps on the home-hit path. Record complete mask and fallback costs. No post-hoc source rescue or compiler flag changes.

Original native-first six-case screening retains qualified same-session controls, three ABBA blocks, every row>=250ms, primary>=2% improvement every block, guards/memory<=1%. Intel is a separate portability cohort requiring no>1% regression. Only survivors advance to target, affected-operation guards, fresh seeds29/43, matched profiles and independent final review. Existing iterator/rank/churn guards remain; collision/displaced/resize traffic and C's scan traffic need separately frozen qualified guards before adoption.

Actual stdio CPU-perf discovery/library_status/ask covered the exact identity, removed ARM instructions, three scopes, miss risks, H3/H4/H6 failures and separate H8 classifier. Coverage3/287sources/158passages. An unrelated perf_event_open register/stack-sampling passage was retrieved; it does not establish this arithmetic's speed. Source observations and the byte proof support a trial, not a measured gain. ARM qualified Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children remain unavailable; Intel baseline scope is separate. No candidate TMA exists yet.
