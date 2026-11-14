# H4-C: outline the post-home probe continuation

Independent implementer: index-continuation. Completed2026-11-14 02:13UTC. Base `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`; source SHA256 `52cd1ce514806d3b7097dd0ca46ac8ff9a932e6a8c06c14ab04862d400193621`. [Patch](change.patch), [manifest](manifest.json). Other H4 implementations were not read.

The original bucket-candidate body is factored into one shared inline `zbtIndexBucketFind`. The inline table lookup checks only the home bucket through that matcher; a hit returns immediately. On failure it calls the explicitly non-inlined `zbtIndexTableFindContinue` with the original lookup arguments. That continuation performs the unchanged home filter, then starts at the home bucket for insertion bookkeeping. It skips candidate matching only for that already-exhausted bucket; subsequent buckets use the same shared matcher.

There is no new state object, persistent field or duplicated candidate scanner. The source adds37 net lines, mostly function boundaries and forwarding calls. The continuation retains the original12-argument lookup contract, so its call can still carry a substantial cost on misses/displaced hits. This is a bounded experiment in separating the filter from successful home hits, not a claim that the extra call is cheap.

## Semantic audit

- The table-size-zero return remains before bucket access and leaves optional outputs untouched.
- Tag folding, match-mask generation and false-positive tag checks are unchanged. The necessary repeated-byte match mask remains on the home path.
- The shared matcher preserves deleted-ID handling, bounds/free-ID checks, resize source/destination migration checks, candidate order, leaf equality and success outputs. The entire leaf helper is text-identical to the baseline.
- The home filter is evaluated only after all home candidates fail, before home empty/tombstone bookkeeping, exactly as in the original routine. Filter-negative lookup still returns without producing an insertion hint.
- Home bookkeeping starts with no saved tombstone; the earliest tombstone remains preferred over later tombstones or an empty slot. The subsequent probe index wraps with the original mask and retains the original table-size bound.
- A completely occupied table still returns the earliest tombstone after the complete probe run. With no tombstone, it leaves insertion outputs untouched.
- Resize advancement remains in the original outer lookup; neither the matcher nor continuation advances rehash independently. No H1/H2/H3 patch, filter-formula change, scanner replacement, layout change or equality change is included.

## Correctness results

All local execution was correctness-only. No timing, instruction measurement, profiling or fleet access occurred. No failed candidate builds/tests occurred.

| Check | Result | Evidence |
|---|---|---|
| Existing native suite | 57 passed,0 failed | [Log](qualification/upstream-native.log) |
| Existing ASan/UBSan suite | 57 passed,0 failed | [Log](qualification/upstream-sanitizer.log) |
| Native fixture cells | All18 passed | [Rows](qualification/fixture-native.jsonl) |
| ASan/UBSan fixture cells | All18 passed | [Rows](qualification/fixture-sanitizer.jsonl) |
| Optional-output oracle, ASan/UBSan | 90,000 checks passed | [Result](output_oracle.json) |
| External oracle, ASan/UBSan | 45,000 checks passed | [Result](output_external_oracle.json) |
| Focused index differential oracle, native O3 | 138,496 comparisons passed | [Result](index-native.json) |
| Focused index differential oracle, ASan/UBSan | 138,496 comparisons passed | [Result](index-sanitizer.json) |
| Fixture outputs/owned bytes | All36 rows exactly match frozen baseline records | [Result](footprint-check.json) |
| O3-Werror build and whitespace | Passed | [Binary hashes](local-binary-sha256.txt); `git diff --check` |

The [focused oracle](index_oracle.c) embeds the exact original table-find routine from the baseline solely as a differential correctness reference. It compares return values and every output field over32 combinations of requested outputs, including untouched failure values and insertion hints. This reference copy is test-only; the candidate implementation has one shared matcher.

Synthetic four-bucket layouts force identical tags and wraparound starting at bucket3. Occupancies0,1,7,8,9,17,24,32 cover empty, home, displaced and full-table cases. The cases include high-byte zero folding, tag255, same-tag distinct members, home and displaced tombstones, first-tombstone priority, saturated false-positive filters, and intentionally cleared filters demonstrating that home hits bypass filtering while the original displaced-hit rejection is retained. Narrow IDs and genuine70000+ wide IDs both run. These are explicit structural fixtures, not a claim of finding naturally occurring hash collisions.

A real200-member tree uses normal hashing and a forced resize. Differential queries inspect both tables at each step and prove each member is accepted in exactly one according to migration state. Three single-leaf steps expose simultaneous old/new membership. Once all leaves are copied, public raw lookup performs the final resize step, frees the old table, returns the correct score and leaves no active rehash. The final table passes the existing full tree/index validator and all member lookups. Existing57-test suites add their unchanged wider mutation/resize coverage.

`qualify.sh` ran with only its `LOG=` destination redirected to this variant's directory. [Stdout](qualify.stdout), [stderr](qualify.stderr). Supplied sanitizer oracles used C11/GCC13.3, `-O1 -g -Wall -Wextra -fno-omit-frame-pointer -fsanitize=address,undefined -fno-sanitize-recover=all`. Focused native used `-O3`; focused sanitizer used the same sanitizer flags. The focused oracle additionally used `-DREDIS_TEST -DREDIS_DEBUG -Werror`, the continuation src/compat/vendor headers, standalone compatibility source, SipHash and `-lm`. Referee inputs remain unchanged.

## Static code-generation screen and limits

The [local GCC13.3/x86-64 raw lookup](local-raw-disassembly.txt) contains no filter mixing constant `0x9e3779b97f4a7c15`. Both failed-home paths call the separate continuation at `dfee` and `e16c`; successful candidate branches return without those calls. The [continuation](local-continuation-disassembly.txt) contains the filter constant at `44b1`, its multiply at `44bb`, and the subsequent unchanged shift/bit combination. Necessary bucket-stride and tag-broadcast arithmetic remains in raw lookup and must not be mistaken for the removed negative-filter mask.

Thus this local binary passes the intended boundary screen. The raw prologue reserves0x48 stack bytes after saving registers, while the continuation reserves0x78 and receives stack arguments; these are emitted local frame details, not comparative performance evidence. Exact ARM and GCC15/LTO control-flow inspection is still mandatory before measurement, including checking that successful home hits avoid filter work in each exact ELF. No local result establishes portability or speed.

The major risks are continuation call/argument cost on misses and displaced hits, loss of output specialization inside its generic body, and code-layout/register-allocation effects. The frozen2% primary and1% guard/memory gates remain. Additional collision/displaced/resize traffic must receive separately frozen, qualified performance guards before adoption; this oracle establishes correctness only. Confirmation, matched profiles and review remain pending.

## Consultation and TMA

Session availability discovery found no exposed cpu-perf/library_status tools. The actual shared controller filter consultation was read, including library status and the exact boundary question; it is not attributed as a separate implementer invocation. Coverage is3/287 linked sources,158 passages,0 vectors, bundled list `deb5a0bac467`; no matching source passage establishes this mechanism or a gain. The question's02:15 source-recheck time was a transcription error: the actual recheck was around02:04 and the upstream hash remained unchanged. Detailed participant provenance is retained privately.

| Category | Qualified ARM baseline | H4-C |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Qualified ARM child categories are unavailable. No collector ran in this implementation session. Separate Intel captures cannot establish an ARM resource cause, and static code inspection is not a pipeline-slot classification.
