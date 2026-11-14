# H5-A: stable raw reads with an outlined resize fallback

Status: **correctness ready; exact fleet code-generation gate and performance validation pending**. Implementer: `cont_helper` (H5-A). Base commit `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`; upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`. Completed 2026-11-14 02:20 UTC. Other H5 implementations were not inspected. No fleet access, local benchmark, instruction-count measurement, profiling, commit or push.

## Implementation and preserved behavior

Add `zbtIndexReadRaw`, an inline raw-reader dispatcher. When `member_rehash` is NULL, it invokes the original inline `zbtIndexTableFind` on the current table, passing the requested score pointer and NULL for all position/insertion outputs. Otherwise it calls the new noinline `zbtIndexReadResizing`, which wraps the unchanged generic `zbtIndexFind` with the original raw-reader arguments.

Only `zbtreeScoreRaw` and `zbtreeScoreRawWithHash` switch to this dispatcher. Raw hashing remains exactly once before dispatch; the prehashed API uses its supplied hash. The original generic finder preserves one-step resize progress, reload after possible completion/free, destination-first search and old-table migration checks. No resize pointer is retained in the wrapper across that call. Stable reads have no resize to advance. Ordinary mutation and batched callers retain their original source paths.

The table matcher, generic index finder, leaf helper/boundary, scanner, equality, home-filter predicate, filter mathematics, allocator and representations are byte-for-byte unchanged. No H1–H4 changes are stacked. No probe implementation is copied. The extra fallback call and changed layout can still regress resize traffic or ordinary guards; reducing live state is a hypothesis, not a performance result.

Candidate source SHA-256: `ef2098f8cedf2aae88e845162d15ef1fd09a9abcaae0e3939d3043594b5a77e0`.
Baseline source SHA-256: `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.
Reversing only the two raw-entry substitutions and removing the new wrapper block restores the baseline exactly. See [implementation.patch](implementation.patch) and [source-verification.json](source-verification.json).

## Correctness evidence

Local GCC 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1). The unchanged `qualify.sh` exited 0. Its fixture calls use the correctness-only `verify` branch; no measurement timer is read.

| Check | Result | Evidence |
|---|---|---|
| Upstream native `-O2` | 57 passed, 0 failed | [upstream-native.log](upstream-native.log) |
| Upstream ASan/UBSan `-O1` | 57 passed, 0 failed | [upstream-sanitizer.log](upstream-sanitizer.log) |
| Six fixtures × seeds 17/29/43, native | 18 passed | [fixture-native.jsonl](fixture-native.jsonl) |
| Same fixtures, ASan/UBSan | 18 passed | [fixture-sanitizer.jsonl](fixture-sanitizer.jsonl) |
| Existing optional-output oracle, ASan/UBSan | 90,000 passed | [output_oracle.json](output_oracle.json) |
| Existing external-record oracle, ASan/UBSan | 45,000 passed | [output_external_oracle.json](output_external_oracle.json) |
| Added raw-state oracle, ASan/UBSan | 21,612 lookups, 62 active steps, four completed resizes | [raw-state-oracle.json](raw-state-oracle.json) |

The added [raw_state_oracle.c](raw_state_oracle.c) builds 600 binary members of lengths 4, 256 and 384. It compares raw, prehashed and unchanged generic lookup on three independent matching copies, checking return values, exact score bytes, untouched miss outputs and table/resize progress after every operation. It covers scored/non-scored lookups in stable state, forced active resizes, the lookup that completes each resize, and subsequent stable reads.

The four cases combine narrow versus wide resize destinations with intact versus deletion-heavy trees. The latter retain freed leaf IDs in two cases and exercise misses for deleted members. During active phases, non-advancing checks identify 32 requested keys in the old table and 30 in the new table, proving both ownership paths were exercised. Both destination widths and all four final completion transitions are asserted. The existing structural checker validates the copies at completion. The wide setup uses the upstream bounded ID-gap helper to request wide tables; the unchanged 57-test suite separately covers actual IDs exceeding the narrow limit, late widening, and mutation bookkeeping. This oracle adds no performance qualification for those states.

The existing and added sanitizer oracles use C11, `-g -Wall -Wextra -O1 -DREDIS_DEBUG -fno-omit-frame-pointer -fsanitize=address,undefined -fno-sanitize-recover=all`; the added oracle also uses `-Werror` and the existing test-only helpers. They link unchanged experiment `standalone.c` and `siphash.c` with `-lm`. All executed checks exited 0 with empty stderr; no failed builds, runtime failures or retries occurred. Candidate logs were copied into this variant directory and tracked baseline qualification evidence restored. `git diff --check` passes.

## Static code-generation evidence and limit

Built a separate **unexecuted x86-64 ELF** with GCC 13.3, C11, `-O3 -g -Wall -Wextra -Werror -fno-omit-frame-pointer`, no LTO, and the unchanged lookup fixture/compatibility sources. SHA-256: `2b4e9093af7b8a6a7b1430fc8560428cf29658986c640e7e2b219ba141f43f61`. This is code inspection only; it supplies no local performance evidence and does not satisfy another compiler cohort's static gate.

In [raw assembly](zbtreeScoreRaw-codegen.txt), the original hash call occurs at `0xdec7`, followed by one entry resize-state check at `0xdecc`. The active branch reaches a tail jump to `zbtIndexReadResizing` at `0xe2da`. The stable body retains the leaf calls at `0xe009` and `0xe32c`, but has no per-candidate resize-state or migration-ID checks. In [prehashed assembly](zbtreeScoreRawWithHash-codegen.txt), one resize check at `0xe3ab` separates the same stable-table work from its fallback, with no hashing call.

The [outlined fallback](zbtIndexReadResizing-codegen.txt) calls the original rehash step at `0x83b0` and reloads `member_rehash` at `0x83b5`; migration checks remain there (for example, `0x8504`/`0x8508`). Thus the local compiler realizes the state separation while preserving the leaf boundary. The raw prologue reserves `0x68` stack bytes beyond saved registers and the prehashed prologue `0x78`; these are static observations, not timing or bottleneck evidence. Exact ARM native, GCC15/LTO and fleet Intel ELFs must independently confirm absence of migration state on stable reads before timing. A failed cohort mechanism must remain ineligible rather than being rescued by unrelated changes.

## Remaining gates

Apply the chair's separately qualified host/compiler controls, ≥2% primary gain in every block, ≤1% guard/memory regression and ≥250 ms windows. Verify stable fixture state through an untimed fleet structural check. No allocation/layout change is expected, but tree-owned memory remains a measured gate. Separately freeze and qualify resize/displaced traffic guards before adoption, since ordinary stable fixtures do not price the outlined fallback. Selection, held-out confirmation, matched profiles, Intel portability and independent review remain outstanding.

## TMA classification

| Category | ARM baseline | H5-A |
|---|---|---|
| Frontend_Bound | Unavailable: scope/formula qualification absent | Unavailable: uncollected |
| Bad_Speculation | Unavailable: same blocker | Unavailable: uncollected |
| Backend_Bound | Unavailable: same blocker | Unavailable: uncollected |
| Retiring | Unavailable: same blocker | Unavailable: uncollected |

Child categories unavailable. No pipeline cause is inferred from frame size, static assembly or other-architecture baseline data. The controller owns the required actual topdown assessment.

## Consultation provenance

Own exposed-tool discovery found no `cpu-perf`/`library_status` tools. Consumed the controller's actual shared stdio raw-state `library_status` and `ask`, not calls made by this implementer. The question covered the exact source, original combined state/frame, rejected leaf-inlining trade-off, stable/resize dispatch choices, final-step lifetime and affected-path guards.

Bundled library revision `deb5a0bac467` (2026-10-05), 3/287 sources, 158 passages, zero vectors, keyword-only. No retrieved primary passage supported the proposed mechanism. Unread entries and unrelated bundled examples are not validation. The consultation did not change the selected scope; exact fleet code generation and resize costs remain open gates. Detailed participant accounting remains in the private record.
