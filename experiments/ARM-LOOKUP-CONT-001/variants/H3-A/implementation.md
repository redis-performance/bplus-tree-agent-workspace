# H3-A: bounded scalar equality for short inline records

Status: **correctness ready for fleet code-generation inspection and diagnostic comparison**. No performance result, source acceptance or local performance measurement. Independent implementer: implementer `cont_helper`; exact model, tokens and monetary cost unknown. Base commit `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`. Completed 2026-11-14 01:50 UTC. Other H3 implementation trees were not inspected. No commit or push.

## Change and bounds argument

Only the equality expression inside `zbtScoreLeafFindMember` changes. After the unchanged tag search and external full-hash rejection, `elelen <= 8 && record[0] == elelen` proves both a short inline record and equal payload lengths. The specialized comparison uses:

| Length | Payload reads per input |
|---|---|
| 0 | None; equal immediately |
| 1 | One byte |
| 2–3 | First and last two bytes using fixed-size `memcpy` into `uint16_t` |
| 4–7 | First and last four bytes using fixed-size `memcpy` into `uint32_t` |
| 8 | Exactly eight bytes using fixed-size `memcpy` into `uint64_t` |

For each head/tail case, both intervals `[0,w)` and `[n-w,n)` are within the proven range `[0,n)` and cover it completely. Overlap is intentional. Unsigned equality is independent of byte order. `memcpy` avoids alignment and aliasing assumptions; no terminator, padding or adjacent record is read. Zero-length tests use non-NULL pointers, including a one-past readable range; this does not broaden the public API's NULL-pointer contract.

Other representations and lengths retain the original `zbtPackedData`, length check and `memcmp` expression. The successful match's physical/logical mapping and optional score/position writes remain byte-for-byte unchanged. The leaf helper declaration/boundary, scanner, external filter, metadata access, allocator and all code outside this helper are unchanged. No H1/H2 or rejected position-arithmetic patch is bundled. The additional branches and code growth may still hurt generic, miss or mutation guards; source correctness does not predict a win.

Candidate source SHA-256: `9c9b248b0b0a162f8679f8d189ff224652f3bfa5017c2f17e679fee83acaa7c9`.
Baseline source SHA-256: `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.
See [implementation.patch](implementation.patch) and [source-verification.json](source-verification.json).

## Correctness evidence

Local compiler GCC 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1). The unchanged `qualify.sh` exited 0; all fixture executions use its correctness-only `verify` branch. No timer-based benchmark, profiling, instruction count or fleet access was performed by this worker.

| Check | Result | Evidence |
|---|---|---|
| Upstream native `-O2` | 57 passed, 0 failed | [upstream-native.log](upstream-native.log) |
| Upstream ASan/UBSan `-O1` | 57 passed, 0 failed | [upstream-sanitizer.log](upstream-sanitizer.log) |
| Six fixture cases × three seeds, native | 18 passed | [fixture-native.jsonl](fixture-native.jsonl) |
| Same fixtures, ASan/UBSan | 18 passed | [fixture-sanitizer.jsonl](fixture-sanitizer.jsonl) |
| Existing optional-output oracle, ASan/UBSan | 90,000 passed | [output_oracle.json](output_oracle.json) |
| Existing 384-byte external oracle, ASan/UBSan | 45,000 passed | [output_external_oracle.json](output_external_oracle.json) |
| Added short-range oracle, ASan/UBSan | 51,888 passed | [short-oracle.json](short-oracle.json) |
| Same short-range oracle, candidate native `-O3` | 51,888 passed | [short-oracle-candidate-o3.json](short-oracle-candidate-o3.json) |
| Same short-range oracle, unchanged baseline native `-O3` | 51,888 passed; identical result JSON | [short-oracle-baseline-o3.json](short-oracle-baseline-o3.json) |

The new [short_oracle.c](short_oracle.c) is a focused internal-helper fixture, separate from the frozen referees. It tests all lengths 0–8 and all mismatch positions, all-zero/all-255/mixed binary bytes, and all four optional-output masks. Its 1,080 guard-page checks place record payloads exactly against an inaccessible following page and query payloads at either end of a readable page between two inaccessible pages. The zero-length end query is never dereferenced.

Another 34,560 checks use exact-sized allocations ending at the declared payload end, independently varying source and query address residues through all eight alignments. ASan supplies allocation-end redzones. These are bounds tests, not padded-read permissions. The `-O3` correctness run additionally exercises the compiler's optimized accesses with the same guard pages; the unchanged baseline confirms that the narrow synthetic fixtures have matching baseline behavior.

The 864 collision checks use tags 0/255, a wrong-full-hash external candidate with a NULL payload pointer (which must be rejected before dereference), a nine-byte candidate, a different-length candidate and a same-length unequal candidate before the final short match. They cover both physical orientations and removal of the final matching tag. These are deliberately constructed helper-level collision cases; no naturally occurring 32-bit hash collision is claimed.

Generic fallback checks cover lengths 0, 1, 8, 9, 15, 16, 253, 254, 255, 256, 319, 320, 321 and 384, all mismatch positions and all outputs. Representation markers are checked at the inline encoding boundary. Synthetic external representations of short strings test that a small query length alone cannot select the inline path. Empty and 96-member synthetic leaves check unchanged scanner bounds. Existing full-tree suites cover their original mutation, iterator, split/merge, signed-zero and reversed-leaf semantics.

Supplied and added sanitizer oracles use C11, `-g -Wall -Wextra -O1 -DREDIS_DEBUG -fno-omit-frame-pointer -fsanitize=address,undefined -fno-sanitize-recover=all`; the added oracle also uses `-Werror`. Native added-oracle builds use `-O3 -Werror` without `REDIS_DEBUG`. Include paths and linked `standalone.c`/`siphash.c` are from this experiment's unchanged current referee. The baseline oracle includes the source copied directly from the base commit. Build and stderr logs are retained; all runs exited 0, stderr was empty, and no build/test failure or retry occurred. `git diff --check` passes.

## Remaining decision gates

Before timing, inspect each exact fleet ELF for bounded scalar loads and absence of a general short-path `memcmp`/`memcpy` call, while assessing spill/caller growth. Local correctness builds provide no performance evidence. Use only the chair's separately qualified host/compiler controls, ≥2% hit improvement in every block, ≤1% guard/memory regression and ≥250 ms windows. Long/external and no-candidate misses remain mandatory guards. Allocation layout is unchanged, so tree-owned bytes are expected to match but require fleet verification. Selection, fresh confirmation, matched profiles, Intel guards and review remain separate obligations; failed cohorts stay parked.

## TMA classification

| Category | Baseline | H3-A |
|---|---|---|
| Frontend_Bound | Unavailable: workload scope/formula qualification absent | Unavailable: uncollected |
| Bad_Speculation | Unavailable: same blocker | Unavailable: uncollected |
| Backend_Bound | Unavailable: same blocker | Unavailable: uncollected |
| Retiring | Unavailable: same blocker | Unavailable: uncollected |

Child categories unavailable. The chair owns actual topdown assessment; this worker supplies no pipeline-slot causal claim from helper or libc sample shares.

## Performance MCP provenance

Own exposed-tool discovery on this turn returned no `cpu-perf`/`library_status` tools. Consumed the parent's actual shared stdio short-record `library_status` and `ask`; these are not this worker's calls. The question addressed the exact record-marker/length proof, the scalar ladder, alternative implementations, the small named-memcmp share, unchanged SIMD tag scanning, and bounds/output coverage across separately controlled cohorts.

Library revision `deb5a0bac467` (2026-10-05), 3/287 sources, 158 passages, zero vectors, keyword-only. No supporting passage matched; the Arm guide was unavailable and other suggested sources were unread. No library assertion or bundled benchmark number establishes safety or speed here. The consultation did not change the chair's selected implementation scope. Safety rests on the interval argument and observed correctness runs; performance remains for fleet validation. Missing worktree memory files were read from the parent checkout.
