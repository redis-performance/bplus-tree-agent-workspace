# H5-C: partition the generic index dispatcher

Independent implementer: state-dispatch. Completed2026-11-14 02:25UTC. Base `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`; source SHA256 `00297055998a105dd8fe4998e1d7b7a388e1a052ac2db661e494bf1f9fb6b850`. [Patch](change.patch), [manifest](manifest.json). Other H5 implementations were not read.

The generic inline `zbtIndexFind` now returns early through the existing current-table finder when no resize is active at entry. This branch retains the original local output/hint defaults and optional-output conventions. Active resize dispatches to `zbtIndexFindResizing`, an explicitly non-inlined function containing the exact original generic-dispatcher body. That body still performs one rehash step, reloads resize state afterward, searches the destination first if it remains active, then checks the old/current table with the original migration and insertion-hint rules.

The table finder and leaf helper are text-identical to baseline, verified by a source comparison. The original dispatcher body is also text-identical after extraction into the resizing helper. The public raw/prehashed APIs and hashing are unchanged. There is no copied probe, H1–H4 patch, scanner/equality/layout change, new assumption, compiler barrier or forced leaf inlining. The source change adds31 net lines.

## Optional outputs and resize safety

The stable branch initializes found and insertion buckets to NULL, and their positions to zero, exactly as the original dispatcher. On a hit it publishes the found bucket/position; on a miss it publishes the insertion hint/position. Position-only callers remain valid: requesting `found_bucket_position` without `found_bucket` still returns the actual position on a hit and zero on a miss. A requested bucket without a position retains insertion-hint maintenance. Score and score-leaf outputs remain controlled by the unchanged table finder and are untouched on failure.

The active branch neither caches a resize pointer across the rehash step nor skips progress for membership-only calls. The extracted original body checks `zs->member_rehash` again after the step, so final completion can free the context safely. Its insertion hint comes from the destination while resizing and from the current table after completion. Existing tag folding, tombstones, free/deleted IDs, migration filtering and probe order remain in the single unchanged table finder.

## Correctness results

All execution was correctness-only. No local timing, instruction measurement, profiles or fleet activity occurred. No failed candidate builds/tests occurred.

| Check | Result | Evidence |
|---|---|---|
| Existing native suite | 57 passed,0 failed | [Log](qualification/upstream-native.log) |
| Existing ASan/UBSan suite | 57 passed,0 failed | [Log](qualification/upstream-sanitizer.log) |
| Native fixture cells | All18 passed | [Rows](qualification/fixture-native.jsonl) |
| ASan/UBSan fixture cells | All18 passed | [Rows](qualification/fixture-sanitizer.jsonl) |
| Optional-output oracle, ASan/UBSan | 90,000 checks passed | [Result](output_oracle.json) |
| External-record oracle, ASan/UBSan | 45,000 checks passed | [Result](output_external_oracle.json) |
| Paired-state native O3 oracle | 1,408 output comparisons;88 raw/prehashed pairs | [Result](state-native.json) |
| Paired-state ASan/UBSan oracle | Same checks passed | [Result](state-sanitizer.json) |
| Fixture outputs/owned bytes | All36 rows exactly match baseline records | [Result](footprint-check.json) |
| O3-Werror build and whitespace | Passed | [Binary hashes](local-binary-sha256.txt); `git diff --check` |

The [focused oracle](state_oracle.c) embeds the exact original generic dispatcher as a correctness reference, using the unchanged table finder. Each requested-output mask starts from two fresh copies of the same source tree. This matters because both implementations advance resize: running them consecutively on one tree would compare different states. It compares all32 combinations of five independently requested outputs, including bucket position without bucket, score bits, normalized leaf IDs, normalized table/bucket addresses, insertion positions and untouched failure values.

Fourteen phases cover narrow and actual70000+ wide leaf IDs, stable lookup, retained tombstones, active resize entry, simultaneous migrated/unmigrated leaves, final resize completion, completed state and released/free leaf-ID slots. Each state compares first/last member hits and a miss; deleted-member lookup is checked separately. All copied pairs pass the existing full tree/index validator. Across each focused build,204 paired calls finish and free an active resize context identically. This counts dispatcher and raw/prehashed checks, not distinct resize campaigns.

The oracle also discovers real same-folded-tag/home-bucket pairs under the current hash seed and inserts them at opposite score extremes, putting them in different leaves. Two such cases cover the narrow/wide layouts. The phase queries include those keys, so membership must reject the earlier same-tag candidate before finding the right leaf. Raw and prehashed API pairs independently verify identical result, score, resize activity and progress with optional scores both enabled and disabled.

`qualify.sh` ran with only its `LOG=` destination redirected into the variant directory; its referee inputs and commands are unchanged. [Stdout](qualify.stdout), [stderr](qualify.stderr). Supplied sanitizer oracles used C11/GCC13.3, `-O1 -g -Wall -Wextra -fno-omit-frame-pointer -fsanitize=address,undefined -fno-sanitize-recover=all`. Focused native uses `-O3`; focused sanitizer uses the same sanitizer flags, with `-DREDIS_TEST -DREDIS_DEBUG -Werror`. All use continuation src/compat/vendor headers, standalone compatibility source, SipHash and `-lm`.

## Static mechanism screen

The [local GCC13.3/x86-64 raw routine](local-raw-disassembly.txt) checks the resize pointer once at entry (`f02c`) and calls the outlined remainder only on the active branch (`f04e`). Its stable path starts at `f070`; the candidate loop has no retained resize pointer, leaf migration-ID load or migration comparison. The leaf calls remain out of line at `f191` and `f3a1`. The unchanged negative-filter arithmetic remains present; this is not H4.

The [prehashed routine](local-prehashed-disassembly.txt) likewise has its entry resize check at `f53b` and resizing call at `f54f`, with no migration filtering in its stable candidate loop. The [resizing remainder](local-resize-disassembly.txt) retains the original rehash step and both-table logic. Raw's local prologue reserves0x68 stack bytes after saved registers; that is a static detail, not a performance conclusion or an ARM frame measurement.

Disposition: **passes the local state-separation screen; exact ARM/LTO screening remains pending**. This implementation must be marked mechanism-ineligible if a target compiler retains migration state in its stable path or merges the split back. Do not repair such a failure with another hypothesis. No performance result is claimed from symbol, frame or branch changes.

The new call can penalize resize traffic, while broad generic dispatch changes can affect updates and optional-output callers. The frozen2% primary and1% guard/memory gates remain, including separately qualified resize/displaced-traffic guards before adoption. Fresh confirmation, matched profiles and independent review remain pending.

## Consultation and TMA

Session discovery found no exposed cpu-perf/library_status tools. The actual shared controller raw-state consultation, including library status and the exact state-boundary ask, was read; it is not attributed as another implementer invocation. Library coverage:3/287 sources,158 passages,0 vectors, bundled list `deb5a0bac467`. No matching passage supports a speedup or a causal resource explanation. Detailed participant provenance is retained privately.

| Category | Qualified ARM baseline | H5-C |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Qualified ARM child categories remain unavailable. No collector ran in this implementation session. Separate Intel evidence cannot establish an ARM resource cause, and static code separation is not pipeline-slot evidence.
