# Independent proposal: bounded short-inline equality

Status: proposal only; no candidate code or new performance measurement. Author role: independent leaf-tag/short-record worker. Other continuation proposals were not read. Backend/model accounting and token costs are unavailable. Source target remains upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`; the historical standalone baseline was source/referee `4876d21ce62fdf9306572b690c891d2d5ed0e04d`.

## Evidence and consultation provenance

The sealed baseline places 41.91% of short-hit whole-process sample period in `zbtScoreLeafFindMember.constprop.0`, 21.91% in raw lookup and 3.45% in named `memcmp`. Matching the captured libc build ID to the retrieved ELF now resolves the unknown `0xa13c0..0xa1480` cluster as the selected **memchr implementation**: 23.3016675% of total short-hit sample period and 6.5814618% of long-hit period. Its code already uses vector compares and mask extraction. See [the independent offline attribution](../symbolization/README.md), including actual ELF resolver instructions and reproducible weighted aggregation. This result does not revise the sealed experiment, measure a new workload, or establish a bottleneck category.

The matching libc also already implements short memcmp through head/tail loads. Consequently replacing it can save call/setup work and ordering-result machinery, but does not replace a naive byte loop. This limits confidence: the 3.45% memcmp self share is a small target and is not a rigorous speedup ceiling because caller overhead, setup and sampling attribution differ. A ≥2% primary gain is plausible only as a hypothesis. It must not be justified by assigning memchr's 23.30% to this change.

Own discovery found no `cpu-perf` or `library_status` tool in the callable catalog. Shared evidence, explicitly **not this worker's invocation**, is the coordinator's fresh controller-local stdio cpu-perf consultation: version 0.1.1, bundled commit `deb5a0bac467`, coverage 3/287 sources and 158 passages, no vectors. The shared `ask` result found no supporting source passages for these specific mechanisms. Related unread sources are not support. Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring remain unavailable; flat cycles and unqualified CPU-wide topdown are not converted to slot categories. No inference of DRAM, branch, or execution-port limitation is made.

## One hypothesis, distinct from the rejected work

**When a matching leaf tag leads to an inline record of 0–8 bytes, evaluate exact byte equality through an inline bounded scalar comparator instead of the general variable-length memcmp call.** The bound comes from the width of a portable 64-bit scalar word, not a literal member prefix, numeric range, key order, or member rank. Leave tag scanning (`memchr`), leaf layout, hash function, packed decoder, physical/logical mapping and output behavior intact.

Target the equality condition in `zbtScoreLeafFindMember`, after candidate-tag location and external-hash rejection. Enter the specialized path only when `elelen <= 8` **and the actual record marker equals elelen**. This simultaneously proves short inline representation and equal length. Handle zero length before reading either payload. For everything else, retain the existing `zbtPackedData`, length check, and memcmp path, including externally represented short members if they occur. Query length alone is never proof of representation. Hash/tag equality is never proof of member equality.

The implementation must preserve the existing successful-match/output block verbatim. It must not add the rejected unused-position optimization, force the whole leaf helper inline, change raw index metadata, prefetch, batch lookups, or replace the tag scanner. There is no persistent cache or allocation and no change to tree-owned bytes.

## Three implementation options for this hypothesis

| Option | Implementation shape | Intended tradeoff | Static rejection criterion |
|---|---|---|---|
| E1: scalar width ladder, preferred first spelling | 0: equal; 1: byte; 2–3: first and last 2-byte words; 4–7: first and last 4-byte words; 8: one 8-byte word. Read multi-byte words using fixed-size memcpy into unsigned locals; compare equality only. Overlap is intentional and covers every byte. | Small length-class ladder, bounded unaligned-safe loads, no need to compute lexicographic sign. Query words may be reused across same-length collisions only if this does not tax no-candidate misses. | Any payload access outside its known length, emitted general memcpy/memcmp call on the short path, or unexplained spills/code growth across the generic fallback. |
| E2: compiler-owned constant-size equality | Switch on actual short length 0–8 and use constant-size `memcmp(..., N) == 0` in each arm. Keep generic comparator outside those arms. | Lets GCC select its own equality loads; larger dispatch and duplicated bodies may outweigh call removal. No compiler intrinsic or platform ISA dependency is needed. | Compiler retains calls or generates an indirect dispatch/code footprint that cannot be justified against E1; guard-page failures always reject. |
| E3: bounded equality accumulator | Inline a maximum-eight-byte loop that ORs XOR differences, with only the length controlling bounds; compare the accumulator with zero. Keep tag traversal unchanged. | Distinct source shape for compiler unrolling, little explicit width handling, no mismatch-dependent early exit. Could add too many branches/loads or fail to unroll. | Generated short path retains a loop/call or adds a branch chain with no credible advantage over the exact baseline. No manual vector scanner substitution to rescue it. |

These are three implementations of one new equality hypothesis, not three independent population proposals. Inspect emitted code on each exact compiler cohort before measurement. E1 is the clearest reviewable shape; static plausibility does not select a performance winner. Retain rejected spellings and their reasons. Do not add query preprocessing before a tag candidate exists merely to improve an ascending-hit fixture: no-tag miss guards would bear that cost.

For E1, the load intervals are a simple proof: for width `w <= n <= 2w`, `[0,w)` and `[n-w,n)` are both inside `[0,n)` and their union covers all bytes. Length 8 uses exactly `[0,8)`. Equality of unsigned words is endian-independent; it does not compute sort order. Fixed-size memcpy avoids unaligned typed dereferences and strict-aliasing violations. Zero length performs no data dereference. Padding bytes, terminators, neighboring records and the next allocation must never be read.

## Why this does not repeat historical failures

EXP-006 replaced memchr with byte, 8-byte SWAR, or 16-byte/unrolled tag scans. The byte approach was rejected; the others remained parked after mixed/batched improvements, unresolved long guards and roughly 3–7% single-lane hit regressions in screening. Those M1/Clang observations are warning evidence, not ARM Neoverse GCC predictions. Resolving the present libc shows a mature vector implementation, further weakening an unchanged scanner retry. This proposal retains that implementation and changes only verified-record equality.

ARM-LOOKUP-GAP-001's three deferred-logical-position spellings reached only 1.394–1.841% median improvement; none met the registered gate. Their successful-match mapping change is explicitly excluded here. The ARM decoder-mask follow-up failed iterator guards; this proposal leaves that shared decoder and its iteration callers unchanged. Prior SIMD/scanner populations supply no acceptance credit for the new path.

## Correctness and adverse-case qualification

Before any fleet timing, compare all three variants to the unchanged upstream/reference implementation with native and ASan/UBSan correctness runs. Keep the full upstream suite and mutation/iteration oracle, even though the proposed scope is equality only. The helper is reached by operations beyond the membership fixture.

Required focused checks:

- Binary strings at every length 0–9, plus 15/16, 253/254/255, 256, 319/320/321 and 384. Include embedded zero, high-bit bytes, all-zero bytes, equal keys, differing length with equal prefix, and a single differing byte at every position. No C-string assumptions.
- Guard pages immediately before and after query data and, with a narrow helper fixture, record payloads; exercise all possible payload alignments. Check exact-size allocations under ASan. This catches both head/tail underflow and overread; compiler-generated constant comparisons are subject to the same requirement.
- For every short length, a long same-tag candidate before the eventual match, a different-length short candidate, same-length unequal candidates, multiple same-tag candidates, and misses after each. Include distinct members with full 32-bit hash collisions, not merely matching 8-bit tags. The complete bytes still decide equality.
- Tag values 0 and 255, singleton/empty/full leaves, reversed physical/logical order, split/merge transitions, insert/delete/update, rank and range/iterator checks. No assumption that tag position equals logical rank.
- All combinations of requested score and position outputs; scores, positions, success and failure must match the referee exactly. Retain the original output mapping code.
- Explicit representation assertions at the 254-byte encoding transition and 320-byte external threshold. The existing 256-byte performance guard is **long inline**, not external. The 384-byte external correctness guard must prove external markers and the full-hash rejection behavior. If externally represented short records are constructible, exercise them too; otherwise document the construction invariant without deleting the fallback.

## Pre-registered falsification and guard plan

Do not execute measurement from this proposal. If the chair selects the hypothesis, use a fresh continuation experiment with a pinned referee and qualified fleet A/A; old A/A does not qualify a new run. Preserve at least the existing primary, score-returning, miss and 256-byte inline guard cells, then add true external-member, randomized order, variable-length binary, collision-heavy and mutation/iterator guard coverage. The additional adverse workloads must be fixed before candidate timing; none replaces the primary or changes its acceptance threshold.

Require each registered primary ABBA block to improve ≥2%, with no demonstrated >1% guard or memory regression, under the chair's frozen run budget. Fresh seeds and matched profiles follow only a discovery pass. Long/external cases should stay on the generic path; a slowdown exposes branch/code-placement or register-pressure costs and rejects rather than waives the guard. Tree-owned bytes should be exactly unchanged. Report memory and text-size changes separately.

Treat GCC 13.3/O3/no-LTO standalone and GCC 15.2/LTO server as different cohorts: pin exact flags, binary/build IDs, allocator and libc; inspect both emitted short/fallback paths; run separate A/A and matched baseline/candidate comparisons. Intel needs its own matched correctness/performance validation before portability claims. The command-level gap and standalone sample shares are not interchangeable outcomes.

Predicted supporting evidence is elimination of short-path general memcmp calls with bounded loads and unchanged tag-search code; matched profiles should reduce short equality/call work without expanding generic-path costs. A reduced memcmp sample share alone is insufficient if total lookup time fails the gate. Reject if the existing compiler already eliminates the call, code size/register pressure negates the saving, collision/miss/long/external guards regress, or any proposed wording needs out-of-bounds/padded-read assumptions. A clean sub-2% result remains a rejection, not permission to combine it with the sealed rejected patch.

Recommendation: eligible for population comparison as a distinct, narrow general mechanism, with lower confidence than the large memchr share might suggest. No candidate, adoption, or performance conclusion is selected here.
