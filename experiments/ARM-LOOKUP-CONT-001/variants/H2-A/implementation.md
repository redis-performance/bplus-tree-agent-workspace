# H2-A: explicit cached packed-score extent

Status: **correctness ready for native diagnostic fleet evaluation**; no performance result or source acceptance. The declared leaf-header growth is 56 to 64 bytes on the tested 64-bit layout. The unchanged ≤1% tree-owned-memory gate still applies; local correctness fixture allocation output is not an acceptance measurement.

Independent implementer: Codex worker `cont_helper`; exact model, tokens and monetary cost unknown. Base commit `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, upstream source `ee8e7f70152404649ac947157fd662d11b4a00d5`. Completed 2026-11-14 01:35 UTC. Other H2 implementations were not inspected. No commit, push, fleet access, benchmark, instruction-count measurement or profiling was performed.

## Implementation

Add `uint16_t score_bytes` between the leaf's `next` pointer and `score_base`. This deliberately incurs alignment padding and moves `data` from offset 56 to 64; it does not claim unused free header space. `zbtScoreLeafOffsets` now loads that field instead of computing the extent from count and width. The array order, packed encoding, record format and relative record offsets remain the original design. Layout-dependent allocation/capacity changes are possible and are part of this variant's declared risk.

The maximum extent for 96 scores of width 64 is 776 bytes, including the spare load bytes and alignment, fitting `uint16_t`. Zero width caches zero. The ordinary formula remains the sizing authority for proposed mutations and new allocations. The cache is assigned at all four leaf count/width mutation sites. No pointer is cached, so relocation needs no added pointer repair.

Added `debugServerAssert(cache == formula)` in the offset accessor and a cache check in `zbtTestCheckNode`. The debug accessor check compiles away without `REDIS_DEBUG`; the structural checker is in the existing test-only section. It must not be enabled for only one timed binary. No H1 inlining, scanner, equality, batching or position-arithmetic change is included. An exact comparison verifies that the original `zbtScoreLeafFindMember` declaration and body are unchanged.

Candidate source SHA-256: `a9fb4302c8e17c7b8a498b2424251577e76c20ca46c9f9dc8f8fa57efeeb7783`.
Baseline source SHA-256: `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.
See [implementation.patch](implementation.patch) and [source-verification.json](source-verification.json).

## Complete mutation and copy audit

| Path | Cache handling and transition |
|---|---|
| `zbtScoreLeafBuild` | Sets count and width, computes cache, then calls array accessors. Covers initial/bulk build, rebuild, split, merge and compaction through their existing builder calls. |
| `zbtScoreInsertInPlace` | Uses computed prospective extent to establish capacity. Sets count, encoding and cache before accessing rewritten arrays. Failed capacity checks leave the old state untouched. |
| `zbtScoreInsertFast` | Reads old offsets/tags and shifts bits using the old count/cache. Moves arrays using the separately computed new extent. Sets count and cache together before publishing the successful insertion. |
| `zbtScoreDeleteInPlace` | Reads and moves old records/arrays with the old cache. Computes the new extent for the target arrays. Sets count and cache together before updating the parent path. |
| Whole-leaf deletion | Frees the leaf; no surviving cache state. Inner-node count mutations are not leaf mutations. |
| Score update, edge insertion and reversal | Count/width-changing work delegates to the four sites above. In-place score replacement and reversal change neither count nor width, so the extent remains valid. |
| Duplication | Existing full-allocation `memcpy` copies the scalar cache. External records are duplicated independently as before. |
| Defragmentation | Existing allocation copy preserves the scalar field; old pointer repair remains sufficient. |

Audited every assignment/increment/decrement to `n.count` and every assignment to `score_bits` in the target source. The four leaf count assignments above are the only leaf count writes; construction and re-encoding insertion are the only width writes. Remaining `n.count` assignments are inner-node fanout updates. The cache is not updated early while old array accessors are still needed.

## Correctness results

Local GCC 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1). The unchanged `qualify.sh` exited 0. Its fixture calls use `verify`, whose branch does not call the measurement timer.

| Check | Result | Evidence |
|---|---|---|
| Upstream native `-O2`, debug/test enabled | 57 passed, 0 failed | [upstream-native.log](upstream-native.log) |
| Upstream ASan/UBSan `-O1`, debug/test enabled | 57 passed, 0 failed | [upstream-sanitizer.log](upstream-sanitizer.log) |
| Six fixture cases × seeds 17/29/43, native | 18 passed | [fixture-native.jsonl](fixture-native.jsonl) |
| Same fixtures, ASan/UBSan | 18 passed | [fixture-sanitizer.jsonl](fixture-sanitizer.jsonl) |
| Existing output oracle, ASan/UBSan + debug | 90,000 checks passed | [output_oracle.json](output_oracle.json) |
| Existing 384-byte external oracle, ASan/UBSan + debug | 45,000 checks passed | [output_external_oracle.json](output_external_oracle.json) |
| Added cache/mutation oracle, ASan/UBSan + debug | 81,568 cache checks, 26,500 mutations, 497 relocations passed | [cache-oracle.json](cache-oracle.json) |

The new [cache_oracle.c](cache_oracle.c) explicitly constructs every score width 0–64 and deletes/reinserts through counts 1–96 in both physical orientations. It compares restored member bytes and score bits with its original arrays. This portion is an isolated internal-leaf fixture, not a constructed member-index reference test.

Its separate public-API portion exercises descending insertion, score movement/re-encoding (including signed zeros and finite extremes), deletion/merging, alternating edge pops, batch append, duplication and active defragmentation. Members include binary keys and lengths 4, 255, 256, 319, 320 and 384, crossing the actual external-storage boundary. It checks all live leaf cache values and lookup agreement with stored leaf scores after mutations. Static assertions establish node size 24 and leaf data offset 64. The original upstream suites and output oracles remain unchanged and provide their existing semantic checks.

Both supplied oracles and the new cache oracle were compiled with C11, `-g -Wall -Wextra -O1 -DREDIS_DEBUG -fno-omit-frame-pointer -fsanitize=address,undefined -fno-sanitize-recover=all`; the added oracle also uses `-Werror`. Include paths target this experiment's `current/src`, `current/compat`, `current/vendor`; link the included-source oracle with unchanged `standalone.c`, `siphash.c`, and `-lm`. All executable exits were 0; stderr was empty. Build logs and compiler identity are retained beside this report.

No source build or correctness test failed or was retried. One artifact-collection assertion initially counted the prefix of `==` expressions as assignments; its failure is retained in [artifact-audit-first-attempt.log](artifact-audit-first-attempt.log). Correcting that audit to match assignment but exclude equality verified exactly four writes, without changing source or tests. `git diff --check` passes.

## Remaining decision gates

Use the chair's separately qualified native cohort, unchanged ≥2% primary improvement in every hit block, ≤1% guard/memory regression, and ≥250 ms windows. First establish fleet fixture footprints, since the declared header growth can alter allocator classes and split capacity. A memory failure makes H2-A ineligible without relaxing the gate. Inspect the exact ARM binary to confirm cache-load addressing replaces the width/multiply/rounding dependency. Native performance, confirmation, matched profiles, Intel guards and review remain outstanding. The old GCC 15/LTO cohort stays PARK and is not repaired by native evidence.

## TMA classification

| Category | Baseline | H2-A |
|---|---|---|
| Frontend_Bound | Unavailable: CPU-wide scope/formula qualification absent | Unavailable: uncollected |
| Bad_Speculation | Unavailable: same blocker | Unavailable: uncollected |
| Backend_Bound | Unavailable: same blocker | Unavailable: uncollected |
| Retiring | Unavailable: same blocker | Unavailable: uncollected |

Child categories are unavailable. This correctness worker makes no pipeline-slot or resource-bottleneck claim. The chair owns the actual topdown assessment during fleet work.

## Performance MCP provenance

Own tool discovery on this implementation turn returned no exposed `cpu-perf`/`library_status` tools. Consumed the parent's fresh shared stdio metadata `library_status` and `ask`, not calls made by this worker. The question explicitly challenged cached extent with header growth, packed-header cache and metadata-first layout on the actual Neoverse V2/GCC13 source/profile, with fixed lookup, mutation and memory gates.

Shared library revision `deb5a0bac467` (2026-10-05), coverage 3/287 sources, 158 passages, zero vectors, keyword-only. No supporting passage matched; the Arm guide was unavailable and other listed sources were unread. No external source claim or bundled benchmark number is used as validation. The limited consultation did not change the chair's exact cached-field scope; mutation ordering and footprint remain explicit risks. Missing worktree memory files were read from the parent checkout.
