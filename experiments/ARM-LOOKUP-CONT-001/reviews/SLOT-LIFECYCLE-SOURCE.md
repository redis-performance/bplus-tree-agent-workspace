# Independent lifecycle diagnostic source review

**APPROVED for source staging and native build only.** No C execution or lifecycle outcome is approved by this report. The actual fleet executable still requires independent emitted-code and identity review before the single correctness run. The source/schema freeze occurred at **2026-11-14 06:12:48 UTC**, epoch `1794636768`, before the 06:15 cutoff. Source and schema are immutable after that freeze; target review must finish by 06:30 and execution by 06:45, otherwise INCOMPLETE.

| Frozen artifact | SHA256 |
|---|---|
| [29-file manifest](../slot-lifecycle-check/SHA256SUMS) | `cd9b4bf0ea2dc4b0ce0c5109d1d87e76ae08c0e686c8183d32aa6c7abdd5deee` |
| [Harness](../slot-lifecycle-check/lifecycle.c) | `87767ea2c51024323cfe25e0df9303bb3b617863bcbfb39630ec91a3148886bc` |
| [Output checker](../slot-lifecycle-check/check_output.py) | `a9bc63863e97e5216b1b0f85152483e2fe83fffe2c7bb67cd9ca493a2154bee9` |
| [Protocol](../slot-lifecycle-check/PROTOCOL.md) | `cf56164d8b292837b1cc93b607f9330aa0ab1efd48016b1865c2f6de55d50551` |
| [Build script](../slot-lifecycle-check/build.sh) | `cb3555afd1b20d86cd52c1929a5a54f8aee73696eb6c42bb67119c0f1f2ab50c` |

The reviewer did not implement this harness or its shadow instrumentation. Review comprised source inspection, independent model arithmetic, hash joins and Python-only synthetic/static checks. No fleet action, new build, C execution, timing or source edit was performed by the reviewer.

## Model and lifecycle findings

The fixed 2048-member fixture is independent of tree output: unique integer IDs are encoded into deterministic binary bytes, caller-owned buffers are regenerated at every checkpoint, and scores are ID+1. An independent alive-ID array determines membership, expected scores, forward/reverse ranks, iteration order and all 1025 rank-deletion victims before the API call. Negative lookup outputs retain sentinels. Seven checkpoints each require exactly 8192 public lookups, plus separately counted direct hint audits, with the complete total bounded by 65536.

Independent arithmetic agrees with the checker:

| State | Members | ID sum | Score sum |
|---|---:|---:|---:|
| Inserted | 2048 | 2096128 | 2098176 |
| After 64 individual deletions / duplicate | 1984 | 2092096 | 2094080 |
| Original after rank deletion | 959 | 976896 | 977855 |

The hint audit covers both current and receiving tables. It checks live allocation ownership, ID/tombstone/free-leaf and migration eligibility before dereferencing a leaf. Staleness compares copied seed identity with the current physical record, including external-hash rejection before pointer decoding; it is not inferred from mismatch with an unrelated query. Audit calls the unchanged full leaf search without progressing rehash and checks its position/score agreement for a matching hint. Public verification follows the audit because public reads can advance resizing.

Duplication is checked immediately before public reads: distinct allocation generations and exact full hint-array copying, including at least one stale hint, with no reseeding. Exact bounded generation/hint snapshots also prove that original-tree rank deletion and destruction leave the duplicate's shadow state unchanged. The duplicate's full member model is checked after both operations, including after the original and its external members have been freed.

The original source explicitly takes Rebuild for 1025 deletions from 1984 members. The harness requires original generation retirement inside that call's recorded interval, a new generation, positive origin-2 seeds, and exact equality between the new seed count and every freshly eligible/unchanged/successful hint. No stale, out-of-range or ineligible fresh hint is accepted. Final success follows both tree frees, caller-buffer frees, an empty generation registry and absent query/table/seed contexts. The old fixed-query census stream remains empty throughout.

## Adversarial checks and provenance

A draft checker incorrectly accepted stale hints immediately after Rebuild. This review reproduced that acceptance before freeze. The author added source and checker freshness assertions and a negative test; the original draft remains in preparation history. The author also replaced a 64-bit duplicate fingerprint with exact snapshots, bounded audit counts by physical table capacity, and added deterministic buffer regeneration.

All 29 final pins and all 93 prior frozen census pins rehash successfully. The copied generated source, shadow header and clock-denial source are byte-identical to the completed census; original production dependencies remain pinned. The separate harness changes neither instrumentation policy nor production code.

The reviewer reran all eight Python test methods successfully and separately challenged fresh-hint staleness, impossible hint capacity, wrong duplicate-table count and wrong survivor-score sum; all malformed transcripts were rejected. The checker enforces exact schemas and integer types, ordered checkpoints, exact lookup accounting, bounded generation lifetimes, copied-parent joins, Rebuild retirement and final cleanup. Duplicate JSON keys, nonfinite values and added timing fields fail.

Replaying static validation against the retained final local compile-only artifact verifies all 13 clock tripwires and every normal shadow-leaf return path's exactly-one original-search call. The original leaf body retains memchr/memcmp. This is preparation evidence only: it does not establish the identity or behavior of a future fleet executable. The [final compile-only receipt](../slot-lifecycle-check/STATIC-VALIDATION-v2.json) pins that artifact separately.

## Limits

The proposed result is bounded native correctness evidence, with no candidate, performance gate, memory-regression threshold or pipeline attribution. Owned-byte fields are observations at checkpoints, not an independently fixed allocator model. Direct hint audits use the seed as their query; they do not cover every arbitrary-query terminal combination. Missing required stale/unchanged coverage means INCOMPLETE, not permission to change the fixture. No sanitizer, defrag, forced address reuse, high-ID, compiler-comparison or active-resize coverage is claimed. Exact hint-copy and member assertions are runtime checks bound to reviewed source; the JSON does not serialize every member or hint byte for independent reconstruction. Operational admission and final target review remain separate requirements.
