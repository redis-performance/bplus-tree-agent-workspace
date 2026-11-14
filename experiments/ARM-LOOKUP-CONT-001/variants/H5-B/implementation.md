# H5-B: correctness passes; inspected mechanism NONE

The H5-B implementer added two `noinline` raw-reader kernels and dispatches both raw APIs on `member_rehash`. The stable kernel calls the original table finder with `member_index`; the resizing kernel calls the original generic index finder. The raw API still hashes once; the prehashed API never hashes. The source starts at e13d9fc88, with no H1–H4 changes.

The controller GCC 13.3.0 non-LTO O3 ELF **fails the mechanism gate**: the stable kernel retains migration filtering and resize-state loads. This implementation is therefore not ready for timing on the evidence inspected here. Exact ARM and LTO code generation has not been inspected by this implementer; any such gate remains separate. No local or fleet performance measurement was made.

`local-O3-stable-assembly.txt` preserves the failed code generation. In its narrow-ID path, 0x583c loads `member_rehash`, 0x5840/0x5843 tests it, and 0x5845/0x5849 loads and compares migration IDs before the leaf call at 0x586d. The wide-ID path likewise checks migration state at 0x5a46–0x5a5d. Invalid-reference handling also retains resize-state tests. The call boundary prevents the caller's state predicate from proving those checks unnecessary in this build. No assumptions, assertions intended to influence optimization, barriers, duplicated probe loops, or further source attempts were added to force the mechanism.

Static symbol sizes in this ELF are 1,247 bytes for the stable kernel, 2,377 for the resizing kernel, 93 for raw dispatch and 21 for prehashed dispatch. These are static observations, not executed instruction counts or performance evidence. The static executable was built from `lookup.c` and the unchanged compatibility/vendor sources with `-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3`; it was not executed.

Correctness passed:

- Original upstream suite: 57 native and 57 ASan/UBSan tests.
- Unchanged fixture verifier: 18 native and 18 sanitizer seed/case cells.
- Supplied output oracles under ASan/UBSan: 90,000 ordinary/long and 45,000 external-member checks.
- Focused raw-state oracle: 104 API checks in each native/sanitizer run, repeated successfully against baseline source in both modes. Each run includes 32 stable, 48 active-resize and 24 final-completion checks; 52 use actual wide IDs. Two stale-reference fixtures and two tombstone-hint fixtures pass.

The focused oracle constructs binary keys and checks raw/prehashed × scored/unscored calls from independent identical starting states. It verifies one-leaf progress during resize, lookup in source and destination tables, final resize-context release and destination adoption, hit/miss score outputs including signed zero and unchanged sentinels, deleted slots, same-tag stale/free leaf references, tombstone hints, and structural invariants after every call. Sparse high IDs exercise 32-bit IDs without allocating thousands of irrelevant leaves. Existing upstream collision tests also pass. Active/final states are explicitly asserted before calls. All compiler and runtime stderr logs are empty; no correctness failure occurred. This validation does not replace the separately required affected-path performance guards.

`scope-audit.json` verifies that removing the two helpers and restoring the two dispatch bodies yields the entire original source byte-for-byte. Thus generic table/index finders, migration progress/free handling, leaf lookup, probe math/order, insertion outputs, scanner and layout remain unchanged. `run-correctness.sh` reproduces the correctness commands. `manifest.json` records source, patch, referee and executable hashes; `candidate.patch` preserves the complete production change.

Source SHA-256: `a2f627b71b398a75a5f793132d2e15de547d3808622f949870c952506eb496fd`.

Own discovery found no tool names matching CPU-perf/library-status. The shared controller actually performed the raw-state stdio consultation; its `raw-state-consult/ask.json` is shared evidence, not an invocation by this implementer. That consultation had 3/287 indexed sources and 158 passages, with no supporting retrieved passage. No source-derived speedup claim follows. Qualified ARM Frontend Bound, Bad Speculation, Backend Bound, Retiring and their children remain unavailable; no candidate metrics were collected. Existing Intel baseline categories are separate evidence. Backend and unknown accounting fields remain in the ignored private participant record.

No commits, pushes, fleet operations or other H5 implementation reads were performed. Outcome: preserve H5-B as a clean mechanism-NONE result for the inspected compiler/build.
