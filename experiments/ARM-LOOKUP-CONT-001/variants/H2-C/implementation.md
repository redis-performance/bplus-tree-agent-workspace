# H2-C: metadata before packed scores

Status: implemented; local correctness PASS; performance selection NONE. Independent implementer: Codex worker `cont_tags`. Other H2 implementation trees were not read. Model, token accounting and monetary costs are unknown. No commit, push, fleet access or local performance measurement was performed.

Baseline: `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, extracted upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`. Only `current/src/zset_btree.c` changes production code. Candidate source SHA256: `789ca7e217baa67cba165d2ebed7be0c9c1a2a7067f94ae870431395e66ffe49`. [candidate.patch](candidate.patch) SHA256: `12c5bcf8e29b8415264192b58b789b9c394d57baf66bef6689f7c8428ea8ee2d`.

## Layout and scope

The layout is now `header | u16 offsets | byte tags | packed scores | free | records`. Offsets are fixed at `leaf->data`; tags start at `data + 2*count`; a score accessor returns `data + 3*count`. Metadata addressing no longer needs score width or score-reservation arithmetic.

Neither header changes. The node remains 24 bytes and the leaf header remains 56 bytes on the tested 64-bit target. A compile-time alignment assertion protects the offset array. Scores can have odd byte addresses; every score read/write still uses memcpy or byte/bit operations, with the existing endian conversion. No typed unaligned score access is introduced.

For the same count, score encoding and records, requested bytes remain `56 + 3*count + score_bytes + record_bytes`. The original score reservation, including eight spare bytes and even rounding, is retained byte-for-byte; at count96/width64 it remains776 bytes. Reordering the arrays changes neither the capacity check nor any allocation request formula. This algebra does not waive the registered tree-memory guard on fleet runs.

The [scope audit](scope-audit.json) checks that the leaf membership search body, both index-search bodies, raw APIs, score-byte formula, leaf request formula and low-level bit-reader/writer bodies are byte-for-byte unchanged. There is no H1 helper-boundary change, scanner replacement, equality specialization, cached field, position shortcut, or fixture-dependent behavior.

## Mutation ordering and bounds

Let `D` be the data base and `S(n,b)` the existing score reservation. The old score region is `[D+3n, D+3n+S(n,b))`.

- **Fast insertion:** save the old tags; memmove `S(n,b)` bytes to the new base `D+3(n+1)`; zero only the newly added score reserve; insert the bit field there using the old count explicitly. Then shift fixed-base offsets, restore tags at the new count's tag base, write the new record and publish count. The copied destination and zeroed extension are both within the new reserved score region. The existing index-end check establishes that this region ends before the new record. Moving scores first prevents new tags/offsets from destroying their source. The helper takes an explicit score pointer/count so no accessor sees a half-published count.
- **Deletion:** preserve tags and record metadata; retain the existing record compaction order. Delete the bit field at the old score base while count is still old, compact fixed-base offsets, then memmove `S(n-1,b)` bytes to `D+3(n-1)`. Rebuild saved tags and publish count afterward. The compacted offsets end at `D+2(n-1)`, before the relocated scores, and new tags end exactly at the new score base. The old tag copy survives the overlapping move. Count zero is excluded by the existing delete-in-place assertion/caller path.
- **Build and re-encoding insert:** set the new count/encoding, zero the new score reservation through the accessor, then rebuild scores/offsets/tags from existing temporary arrays. The same capacity check keeps all metadata below records.
- **Reverse-for-pop:** count does not change; reverse offsets/tags as before and rewrite the zeroed score reservation through the new accessor. Reversed prepends/pops avoid shifting individual score fields, but now relocate the score stream on count changes. That additional mutation work is an explicit risk.

All four remaining direct `leaf->data` uses are enumerated in the scope audit: fixed offsets, the count-based score accessor, and the explicit new-count score destinations in fast insert/delete. No old score-relative offset calculation remains.

## Read/write and lifecycle audit

| Path | Treatment |
|---|---|
| Score read, zero-field write, update-in-place | Use the new score accessor; preserve bit packing and endian conversions. |
| Bit insertion | Explicit relocated score pointer, old count and unchanged bit-shift algorithm. |
| Bit deletion | Resolve old score pointer before count changes. |
| Complete build, compact/repack, split, merge, bulk append | Existing builders still own these transitions; builder score zeroing uses the new base. |
| Re-encoding insert | Existing temporary scores/locations/tags are the source; score zeroing uses the published new count. |
| Fast insert/delete and reversed leaves | Ordered moves described above; fixed-base offsets remain aligned. |
| Duplication | Entire allocation copied; metadata remains relative to the copied leaf, external ownership repair uses existing accessors. |
| Defragmentation | No cached pointers were added; relocation and external-member fixups use existing record accessors. |
| Iteration/rank/index/record ownership | Existing accessors expose the new arrays; algorithms and record formats unchanged. |

## Correctness evidence

Controller compiler: GCC 13.3.0, Ubuntu `13.3.0-6ubuntu2~24.04.1`. [run-correctness.sh](run-correctness.sh) reproduces the correctness-only commands from the worktree root. The unchanged qualification script and both supplied oracles remain the controls.

| Check | Result |
|---|---|
| Upstream tests, native O2 | 57/57 PASS |
| Upstream tests, ASan/UBSan O1 | 57/57 PASS |
| Existing fixture verification | 18/18 native and18/18 sanitizer PASS: seeds17/29/43 × hit/score/miss/256-byte inline/384-byte external/update |
| Supplied optional-output oracle, ASan/UBSan | 90,000 PASS |
| Supplied external-record output oracle, ASan/UBSan | 45,000 PASS |
| New focused oracle, candidate native and ASan/UBSan | Each:10,752 mutation cases,366,336 leaf invariant checks,156 whole-tree/model checks PASS |
| Same focused oracle, unchanged baseline native and ASan/UBSan | Same case/check counts PASS |

The focused oracle uses an independent array of exact scores/member IDs for direct leaf transitions and a member/score model plus the upstream structural/index checker for full trees. It covers every score width0..64, shift0 and each nonduplicate endpoint shift through63, counts1/2/3/7/8/9/15/16/31/32/63/64/94/95 with insertions up to96, both physical orientations, beginning/middle/end insertion, repeated beginning/middle/end deletion down to1, record compaction on/off, reversal and score output correctness. Synthetic encodings are valid but deliberately need not be the most compact encoding, so full field widths are exercised rather than inferred from ordinary integer scores.

Each candidate focused run checks186,616 odd score bases. The mixed-record phase uses binary lengths0/1/2/3/7/8/9/253/254/255/256/319/320/321/384, embedded zero/high bytes, signed zero and infinities, score-changing mutations, multiple leaves, rehash, duplication, moving defragmentation, bulk append and edge deletion. It observes8 rehash states and7,833 external-record checks per run. Full-hash filtering and optional-output correctness additionally remain covered by the supplied/upstream controls. These counters describe correctness coverage, not timing or hardware measurements.

There were no failed correctness runs. Initial focused native compilation produced conservative `-Wmaybe-uninitialized` warnings about the expected-value arrays; those arrays are now zero-initialized and final focused builds are warning-free. Initial logs, including warnings and successful runs, are retained under `attempt-1/`. Native and sanitizer allocator accounting must not be compared across builds. No acceptance claim is made from local owned-byte fields.

## Static mechanism check and remaining risk

[Local leaf disassembly](local-leaf-assembly.txt), from the x86 GCC13/O2 correctness binary, retains the original out-of-line leaf symbol. At `0x3c2f` it forms the fixed offset base `leaf+56`; `0x3c36` adds twice count for tags, before memchr at `0x3c9c`. There is no score-width multiply/rounding dependency in that address chain. This only checks the implementation's shape locally; exact ARM fleet assembly must be inspected independently before interpreting performance. No instruction-count or timing measurement was collected.

The principal risk is greater mutation cost from moving score bytes on every count change, including reversed edge operations, plus the added count-dependent score address for score-producing callers. The original layout could move metadata instead; C trades those costs rather than eliminating all movement. Header and allocation formulas are unchanged, but the fixed ≥2% primary and ≤1% guard/memory gates still apply. Any failure remains rejection/park under the chair's frozen protocol. Native discovery is the qualified cohort; GCC15/LTO remains PARK and supplies no acceptance credit.

## Consultation and TMA provenance

Own fresh discovery found no callable `cpu-perf` or `library_status` tools. The coordinator's actual metadata-specific stdio `ask` response is shared evidence, not this worker's call. Its question explicitly covered cached displacement, header packing, metadata-first layout, mutation/footprint costs, and the exact Neoverse/GCC13 baseline. The library reports3/287 sources and158 passages with keyword-only coverage; no supporting source passage matched. Unread related sources carry no claim here. Direct source reasoning and the scoped correctness/static checks establish this implementation, not a library-backed speedup prediction.

| Pipeline-slot category | Baseline | H2-C |
|---|---|---|
| Frontend_Bound | Unavailable: no qualified workload-isolated/formula-qualified funnel | Unavailable: uncollected |
| Bad_Speculation | Unavailable: same blocker | Unavailable: uncollected |
| Backend_Bound | Unavailable: same blocker | Unavailable: uncollected |
| Retiring | Unavailable: same blocker | Unavailable: uncollected |

Qualified child categories are also unavailable. Static dependencies and whole-process sample shares are not converted into slot categories. Fleet comparison, guard validation, matched profiles, independent confirmation and review remain outstanding.
