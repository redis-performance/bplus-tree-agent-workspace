# Independent ARM proposal for AMD all-match scan

Participant: `/root/aws_arm`. Submitted 2026-10-19T03:07:53.412658+00:00. Native Codex worker; exact serving model and measured token/USD costs unknown. This proposal is independently authored by this participant. I read the common packet atb1b670c0a, its profiles/rows.json and original source8fab511e, plus prior decisions already known in this campaign. I did not read AMD/Intel proposals or the chair. Common-packet SHA256: `ea5a6d16ab70be80a2aa68c9d12863320499224865c444afe1ea4ff9a783a0e5`.

## Proposal: bounded16-byte exact comparisons in zbtLeafTagMatches

Hypothesis: on AMD x86-64, replacing the full-word scan in `zbtLeafTagMatches` with an SSE2 exact byte-equality mask for each complete16-byte chunk reduces full-array scan work enough to improve original100K and1M scan by at least2% in every qualified primary block. Enumerate set bits in ascending physical order, map each to the same logical position, and retain a bounded existing-style tail. For index tag1, OR comparisons against byte1 and byte0 before enumeration. Never stop after the first match. Keep non-SSE2 targets on the unchanged scalar/SWAR implementation; change no compiler flags or global index lookup mask.

This is one mechanism: amortize all-match byte comparisons over16bytes with an exact mask. Do not combine prefetch, changed callback ordering, leaf metadata caches, special collision shortcuts or speculative loads. No candidate code is supplied here.

## Evidence and limits

The authoritative same-IP inclusive helper shares are21.31/38.99/36.53% at100K and27.93/23.34/26.25% at1M across seeds1/2/3. These already include nested TagMask work; adding formatted subhelper percentages would double-count. Only67–91 samples/capture make exact fractions imprecise. They support the helper's relevance, not a promised SIMD speedup or instruction latency.

Census reports roughly69bytes per call, about1M calls and76.6–76.7% single-match. This means approximately four complete16-byte chunks plus a small tail per typical call, compared with eight complete8-byte words. The all-match contract must still examine the entire array even when exactly one match exists. A16-byte exact comparison/movemask can reduce chunk-loop and mask construction work and avoids false-positive verification for vector chunks. Folded tag1 is only0.78% of calls, so its second compare should not dominate the ordinary path; correctness still requires it.

The earlier Intel bounded-SSE2 FIRST-match failures are an explicit negative prior. This proposal is distinct because first-match search often terminates early and competes with tuned memchr, whereas this helper must enumerate the complete array with correct multiplicity. That difference makes one bounded all-match experiment defensible, not automatically successful. Added vector setup, movemask latency, code size or tails may erase gains. Reversed calls were absent in the census and require separate testing.

## Required correctness and portability gates

Before candidate timing, an independent scalar oracle must compare the exact returned count and complete ordered positions for every tag0..255, lengths0..96, both orientations, every relevant alignment and adversarial patterns: zero/one folds, adjacent false-positive patterns, all-equal tags, no matches, first/last-only, dense matches and chunk/tail boundaries. Guard pages must prove that neither full-vector chunks nor tails read past the logical tag span, including every ending alignment. Preserve writes beyond the returned positions and capacity bounds. Deliberately faulty fold/order/tail implementations should be detected.

Run unchanged scan_interval, wide_scan, live_widen_scan and resize_generation oracles, original tests and sanitizer builds. Preserve narrow/wide IDs, tombstones, partial tables, migration ownership and external records. In ScanSlot, count>1 still drives hash/reachability disambiguation; losing a match or changing multiplicity is a semantic defect even if total callbacks happen to match. Keep ascending physical enumeration for reversed leaves too, yielding the original decreasing logical positions. SSE2 is compile-time guarded; portable fallback and build coverage remain mandatory. No wide-vector ISA requirement, runtime permission change, allocator change or baseline flag change.

## Performance and rejection

Use the packet's unchanged original scan primaries100K/1M,1M requested operations,16-byte members, six same-session ABBA blocks and frozen seeds. Preserve per-run rows. Predict a larger benefit for leaves spanning several chunks and smaller/negative benefit for tiny spans or dense tags; this is a falsifiable qualitative expectation, not a measured result. Broader performance guards must be frozen before timing: small100/1K/10K scans,8/321/1024-byte members, and supported collision/reversed/migration scan fixtures where available. Correctness coverage alone does not qualify those performance guards. Tree-owned memory and callback contract must remain exact.

Reject as a winner if either qualified primary fails the>=2% gate, any semantic/bounds fault appears, or a qualified required guard shows>1% regression. Failed A/A, incomplete phases or unresolved guards meanPARK, never acceptance. If generated code does not realize bounded16-byte comparisons, or matched profiles fail to support reduced all-match helper work, do not claim this mechanism validated. Fresh independent confirmation, candidate profile validation and root adversarial review remain mandatory. Existing first-match patches must not be relabeled as this experiment, and no source adoption is requested.

Signed by participant `/root/aws_arm`; this denotes authorship, not a cryptographic signature.
