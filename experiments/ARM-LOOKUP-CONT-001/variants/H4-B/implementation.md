# H4-B: outline only the lookup query mask

Implementer: H4-B query-mask role. Status: local correctness PASS and local static mechanism PASS; target-cohort code-generation qualification and performance selection remain pending. Other H4 implementation trees were not read. No fleet access, performance measurement, commit or push was performed. Detailed participant provenance is retained privately.

Baseline: `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`. Candidate source SHA256: `a1aef5b623a24fda5ed4a9a47c68fe7b29f75150f4cd996db640059221252fac`. [candidate.patch](candidate.patch) SHA256: `4eb7560048b7b04c74181c701806af72deeee234d7cf992d14684bd23b287504`. [manifest.json](manifest.json) preserves compiler and source/referee/binary identities.

## Exact change

Add one `static __attribute__((noinline)) uint64_t zbtIndexQueryTagBits(uint8_t tag)` wrapper that returns the existing `zbtIndexTagBits(tag)`. Change only the mask-construction call inside `zbtIndexHomeMayContain` to use that wrapper. Its home-bucket addressing, table load and mask predicate remain in the caller.

The original `zbtIndexTagBits` mathematics and inline declaration remain unchanged. `zbtIndexRecordHomeTag` still calls it directly, so insertion-side filter maintenance gains no new source call boundary. The zero-to-one tag fold is unchanged and occurs before the query wrapper. Existing reference lookups also use `zbtIndexHomeMayContain`, so their query-mask construction shares this boundary; this can affect mutation callers even though insertion filter maintenance is unchanged.

[scope-audit.json](scope-audit.json) verifies that removing the added wrapper and restoring the single call expression reproduces the baseline file byte-for-byte. Thus probe order, candidate matching, leaf helper, record equality, metadata layout, ID/migration checks, first-tombstone hints, rehash advancement, allocations and optional outputs are unchanged. No volatile data, artificial effect, barrier, inline assembly, cached state, H1/H2/H3 change or referee edit is included.

## Static prerequisite: local result and target limit

Inspected controller binaries use GCC13.3.0 (`13.3.0-6ubuntu2~24.04.1`), x86-64, C11, debug information and frame pointers, without LTO. O2 is the native correctness build. A separate O3 binary was compiled for static inspection and was not executed. These are not the ARM or target GCC15/LTO ELFs.

The local O2 and O3 raw-lookup control flow passes the intended boundary check. The necessary repeated-byte tag mask remains in raw lookup. The three-bit filter multiply constant `0x9e3779b97f4a7c15` is absent from that function; its construction is inside the outlined query helper. All query-helper calls in the inspected raw function are after candidate exhaustion, gated by the first-probe condition. A verified home candidate returns without reaching them.

In [O3 raw assembly](local-O3-raw-assembly.txt), the four narrow/wide and table-path expansions have these branches:

| Leaf call | Success branch | Query-mask call reached after failed candidates |
|---|---|---|
| `0xd6da` | `0xd6e9 → 0xde4b` | `0xd76c` |
| `0xd937` | `0xd942 → 0xde4b` | `0xd9bd` |
| `0xdb39` | `0xdb44 → 0xde4b` | `0xdbb8` |
| `0xdd38` | `0xdd47 → 0xde4b` | `0xddbe` |

`0xde4b` is the return epilogue. After the first query call, for example, the home-filter load and comparison remain in the caller at `0xd778..0xd77f`. [O2 raw assembly](local-O2-raw-assembly.txt) similarly returns on leaf success before query calls at `0x96f7` and `0x993c`. No claim relies solely on textual address ordering; the success branches and candidate-exhaustion/probe guards were traced.

This proof applies per table search. During resize, a failed destination-table search can legitimately consume its mask before a source-table hit; that is used filter work, not the unused mask construction targeted here.

[O3 insertion assembly](local-O3-insert-assembly.txt) still contains the original mixed-mask constant/arithmetic at `0x32ad`, and has no call to the query wrapper. Necessary filter maintenance during rehash copying remains intact. [O3 query-helper assembly](local-O3-query-mask-assembly.txt) shows the original mask computation inside the retained boundary.

Local symbol metadata records a56-byte query helper and2343-byte raw function. Raw lookup reserves120 stack bytes with `sub rsp,0x78`, in addition to its register saves. These are static descriptors, not speed or instruction-count measurements, and are not compared across architectures. No local code-generation gate failed. One inspection command initially used the controller root instead of the isolated worktree, found no binary and wrote no artifact; it was rerun at the correct root.

**Before timing each target cohort, inspect its exact ELF again.** The wrapper is pure and noinline alone does not universally prevent motion. If target compilation hoists the call or reconstructs filter work on a successful home path, preserve that failure and reject the implementation for that cohort without timing. Do not add effects or barriers to rescue it. No ARM/GCC15/LTO static pass is claimed by these local artifacts.

## Correctness

[run-correctness.sh](run-correctness.sh) reproduces the completed correctness command sequence. Native uses O2; sanitizer uses O1 with ASan/UBSan and no recovery. All completed builds/runs exited0 with empty stderr; there were no correctness failures or compiler warnings.

| Check | Result |
|---|---|
| Upstream suites | 57/57 native +57/57 sanitizer PASS |
| Existing fixture verification | 18 native +18 sanitizer PASS; six cases × seeds17/29/43 |
| Supplied optional-output oracle | 90,000 ASan/UBSan checks PASS |
| Supplied external-record oracle | 45,000 ASan/UBSan checks PASS |
| Focused index oracle | Candidate and unchanged baseline each PASS in native and sanitizer builds |

Each focused run records131,584 filter checks,222 member hits,24 misses,222 reference-lookup checks,126 wrapped hits,111 hits using actual IDs above65535,12 earliest-tombstone assertions,16 migration-table assertions and4 final-step completions.

The focused oracle exhausts all256 recorded high-byte values against all256 queried values in both bucket formats, checking the unchanged mask through a separately expressed arithmetic model. This includes zero folding into one, filter absence and allowed false positives. A saturated filter is also checked against an empty table to confirm that a positive filter does not manufacture a member hit.

Synthetic consistent index states then force19 distinct members into the final home bucket and following wrapped buckets. They mix raw high bytes0/1, and separately use7/255, forcing same-tag collisions; a distinct member also shares a full hash with another. Narrow IDs and wide IDs beginning at70000 are checked through membership and reference lookups. Two tombstones in successive probe buckets verify the earliest insertion hint, reuse without increasing filled count, remaining displaced hits and continued miss behavior. Synthetic hashes are only correctness inputs; no source or timing fixture depends on them.

Whole-tree resize tests use real binary-member hashes and the upstream structural/index checker, separately with narrow and wide tables. A raw lookup copies exactly one leaf. Direct queries of both tables then prove that migrated leaves are visible only in the destination and remaining leaves only in the source. After all leaves are migrated but the old table is still allocated, a raw hit or miss performs the final resize step, frees/replaces the old table, updates the revision and returns the expected result. Allfour narrow/wide × hit/miss final-completion cases pass.

These are correctness checks, not qualified collision/displaced/resize performance guards. Such traffic must still receive a separately frozen and qualified guard suite before any adoption. Native/sanitizer owned-byte output is not compared across allocator builds or used as local performance evidence.

## Risk and decision boundary

Home hits can avoid query-mask construction if the target compiler retains the verified boundary. Misses and displaced hits still need the same mask and now pay a call; reference searches can also incur that call. Live-state preservation, code placement and caller spills may offset any saved work. No speedup or hardware-resource cause is asserted.

The existing ≥2% primary-per-block and ≤1% guard/memory rules remain unchanged. Native ARM, target LTO ARM and Intel must keep separate controls and results. A static pass only permits consideration for the target's controlled comparison; performance selection, held-out confirmation, matched profiles and independent review remain outstanding.

## Consultation and TMA

Own tool-catalog discovery found no callable `cpu-perf` or `library_status` tool. The actual controller `filter-consult` stdio response is explicitly shared evidence, not this implementer's invocation. It asks about the three filter-boundary spellings, exact captured eager mask work, pure-call hoisting, miss/displaced/resize costs and required edge cases. The bundled list is `deb5a0bac467`, with3/287 linked sources and158 passages, keyword-only coverage. No supporting retrieved passage established this mechanism or predicted a gain; unread sources carry no claim here. The consultation's manually entered02:15 recheck time was corrected by the chair to around02:04; the exact source hash is unchanged.

| Pipeline-slot category | Qualified ARM baseline | H4-B candidate |
|---|---|---|
| Frontend_Bound | Unavailable | Unavailable: uncollected |
| Bad_Speculation | Unavailable | Unavailable: uncollected |
| Backend_Bound | Unavailable | Unavailable: uncollected |
| Retiring | Unavailable | Unavailable: uncollected |

ARM workload isolation/formula qualification remains unavailable in the supplied funnel; qualified child categories are unavailable. Intel baseline captures are audited separately and are not transferred to ARM. No H4-B candidate funnel was collected here. Static assembly and whole-process samples are not substituted for slot shares.
