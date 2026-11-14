# H7-A — lookup-only exact index mask

Status: **correctness ready; independent exact ARM codegen gate pending**. Implementer role: lookup-only mask implementer. Baseline commit `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`; frozen upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`. No H7-B/C implementation was inspected. No timing, instruction-count measurement, profiling, fleet access, commit or push was performed.

## Frozen change

Candidate source SHA-256: `002c3568202dff5cb5f39f28753f4b48d1c9ec1c533775371f2fea41eccb6ce8`.
Baseline source SHA-256: `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.

[implementation.patch](implementation.patch) adds `zbtIndexExactTagMask`, using unsigned 64-bit `~(((x & low) + low) | x | low)` with `low=0x7f7f7f7f7f7f7f7f` and the original tag XOR broadcast. Only `zbtIndexTableFind` calls it. Only that consumer's redundant stored-byte comparison/skip block is removed. The original approximate helper, reference lookup, existence tests, leaf-tag scan, all ID/tombstone/free/migration checks, negative filter, record matching, leaf boundary, data layout and allocation are unchanged.

Per lane, low-seven-bit input plus 127 is at most 254, so addition cannot carry into its neighbor. The sum's high bit rejects nonzero low-seven-bit input; OR with the original byte rejects a set original high bit. OR with `low` forces all low result bits off after complement. Thus each surviving bit is exactly a matching byte. Repeatedly clearing the least significant set bit preserves ascending candidate order without revalidation; first-bit extraction remains guarded by a nonzero mask.

[source-verification.json](source-verification.json) records an exact reconstruction check: removing the named helper, restoring its one call site to the approximate helper and restoring the removed validation reproduces the baseline source byte-for-byte. It records frozen referee hashes and the unexecuted codegen ELF identity. No H1–H6 changes are present. `git diff --check` passes.

## Correctness results

Compiler: GCC 13.3.0, Ubuntu 13.3.0-6ubuntu2~24.04.1. All executed tests returned zero with empty stderr. The unchanged `qualify.sh` ran its native and sanitizer tests and only `verify` fixture mode.

| Check | Result | Evidence |
| --- | --- | --- |
| Original upstream native | 57 passed, 0 failed | [upstream-native.log](upstream-native.log) |
| Original upstream ASan/UBSan | 57 passed, 0 failed | [upstream-sanitizer.log](upstream-sanitizer.log) |
| Six original fixture cases × seeds 17/29/43, native | 18 passed | [fixture-native.jsonl](fixture-native.jsonl) |
| Same fixtures, ASan/UBSan | 18 passed | [fixture-sanitizer.jsonl](fixture-sanitizer.jsonl) |
| Supplied optional-output oracle, ASan/UBSan | 90,000 checks passed | [output_oracle-sanitizer.json](output_oracle-sanitizer.json) |
| Supplied external-record oracle, ASan/UBSan | 45,000 checks passed | [output_external_oracle-sanitizer.json](output_external_oracle-sanitizer.json) |
| Exact-mask oracle, native and ASan/UBSan separately | Each: 2,559,808 masks, 4,711,764 enumerated positions passed | [mask_oracle-native.json](mask_oracle-native.json), [mask_oracle-sanitizer.json](mask_oracle-sanitizer.json) |
| Focused index oracle, native and ASan/UBSan separately | Each: 54 reference checks, 21,654 table checks, 3,072 output combinations, 16 migration steps, 2 completed resizes | [index_oracle-native.json](index_oracle-native.json), [index_oracle-sanitizer.json](index_oracle-sanitizer.json) |

[mask_oracle.c](mask_oracle.c) derives expected masks and complete position order using independent byte comparisons. It covers all 256 tags × 256 byte values × eight positions; every adjacent pair of XOR bytes at all seven boundaries under zero, one, high-bit and all-one surrounding backgrounds; 200,000 deterministic full-word queries; and every tag's all-match/no-match words. Adjacent-pair testing uses XOR-domain translation rather than the unnecessary full tag×pair Cartesian product. Folded index tag zero/one equivalence is asserted separately. These counts describe correctness cases, not instruction or timing measurements.

[index_oracle.c](index_oracle.c) extends the previously retained H4-A correctness oracle. Its new synthetic index-only fixtures allocate 24 single-member leaves with explicitly chosen hashes whose folded tag is one and home bucket is the last of four. Queries encounter multiple unsuccessful leaf candidates, displacement and wrap before a hit. Both narrow and actual wide IDs are used. All 64 combinations of optional score/leaf/position/found-slot/insertion-hint output groups are checked for every member. Misses verify unused-slot and first-tombstone hints; deleting an early slot must not hide later or wrapped hits. These fixtures are isolated internal correctness constructions, not generated workload distributions or altered public referee fixtures.

The retained tests additionally check an all-tombstone run, reference reachability and tombstone reuse. Full trees of 600 actual hashed binary keys are checked before and after each narrow/wide-destination resize step, asserting exactly one visible owner across old/new tables, exact score and structural invariants. Both final completion transitions occur, followed by public lookups. Original tests provide their broader free-ID/migration, relocation and scan coverage. The new test does not claim separately measured collision/resize traffic coverage.

Exact compile commands, return codes and binary hashes for all six additional builds/runs are in [oracle-runs.json](oracle-runs.json). Native added oracles use `-O2`; supplied and added sanitizer oracles use `-O1 -fsanitize=address,undefined -fno-sanitize-recover=all`, with C11, debug information, `-DREDIS_DEBUG`, frame pointers and warning checks. Sources link the unchanged standalone compatibility and SipHash files. Original qualification flags and referee identities remain unchanged.

One initial driver invocation failed before executing `qualify.sh` because the fresh sparse worktree lacked the redirected log's parent directory. [initial-driver-error.log](initial-driver-error.log) preserves the failure. After creating that output directory, unchanged qualification ran successfully. No source correction, runtime failure or measurement retry was needed.

## Static artifact and remaining gates

Built, but did not execute, a separate local x86-64 lookup ELF with GCC 13.3, C11, `-O3 -g -Wall -Wextra -Werror -fno-omit-frame-pointer`, no LTO, linking unchanged lookup/compatibility/SipHash sources. ELF SHA-256: `4e46e102bd35a705298d06342e1b4bd901c08a25dc10fe89db1251d2627c4f93`.

[raw-codegen.txt](raw-codegen.txt) shows the inlined scalar sequence at `0xd689`–`0xd69b`. Candidate selection at `0xd716` uses `tzcnt`, shifts its result by three at `0xd71b`, then directly loads the narrow ID at `0xd71e`; the removed stored-tag extraction/comparison is absent from that chain. The existing leaf calls remain, for example `0xd6f3`. This is static local inspection only, not an exact ARM gate, Intel fleet validation, instruction-count measurement or evidence of a gain. It makes no whole-function frame comparison claim.

The controller's independent native and target ARM review must inspect actual scored/no-score paths, complete mask cost, frame size and ID-dispatch chains under `H7-selection.md`. Reject if the original recheck persists, the frame grows or new dependencies erase the intended removal. Only an eligible ELF may enter separately qualified fleet timing with all original ≥2%/≤1%/250 ms gates. Intel miss behavior is a leading risk because extra exact-mask arithmetic applies even without candidates. Collision/displaced/resize traffic needs separately frozen qualification before adoption. No performance or memory acceptance is claimed here.

## Consultation and TMA

Own enabled-tool discovery found no callable cpu-perf/library_status endpoint. This implementer consumed the controller's actual shared `mask-classifier-consult` library-status and ask results. They cover the exact unsigned mask proof, three implementation scopes, removed ARM instructions, miss risks and codegen falsifiers. Library revision `deb5a0bac467` (2026-10-05) reports 3/287 indexed sources, 158 passages and zero vectors. The retrieved perf_event_open register/stack-sampling passage is unrelated to this arithmetic's speed and is not supporting evidence. These were shared controller calls, not this implementer's calls; the selected source/algebra/test contract remains the basis for the trial. Detailed backend provenance is private; exact token/cost totals are unknown.

| TMA category | Qualified ARM baseline | H7-A |
| --- | --- | --- |
| Frontend_Bound | Unavailable: scope/formula/exclusion qualification absent | Unavailable: uncollected |
| Bad_Speculation | Unavailable: same blocker | Unavailable: uncollected |
| Backend_Bound | Unavailable: same blocker | Unavailable: uncollected |
| Retiring | Unavailable: same blocker | Unavailable: uncollected |

Child categories are unavailable. No pipeline cause is inferred from assembly, hotspot shares or another architecture. Existing Intel baseline classification does not classify this candidate.
