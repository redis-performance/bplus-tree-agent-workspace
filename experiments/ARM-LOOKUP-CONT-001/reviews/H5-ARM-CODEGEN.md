# H5 ARM static gate review

Reviewed 2026-11-14. **A and C pass the state-separation gate in both saved ARM native and GCC15/LTO builds. B is mechanism-ineligible (NONE) in both.** This selects candidates eligible for subsequent gates, not a performance winner. No executable, collector, benchmark or correctness test was run for this review; no source was changed.

Independence limitation: this reviewer previously implemented B. This is a fresh review of B's target assembly, but cannot count as an independent-author review of B. A/C implementations and all six target assembly captures were newly inspected here. An additional reviewer is needed if the campaign requires independent authorship for B's disposition.

## Evidence identity and method

Read the three isolated patches/reports under `build/arm-cont-private/worktrees/H5-{A,B,C}/experiments/ARM-LOOKUP-CONT-001/variants/H5-*`, plus complete saved `assembly-{A,B,C}.stdout`, `metadata.json`, `commands.jsonl` and `size-*.stdout` in [H5-native](../../../build/arm-cont-private/fleet/H5-native/) and [H5-lto](../../../build/arm-cont-private/fleet/H5-lto/). The saved full disassemblies, rather than only the extracted raw-function snippets, matter: LTO A/C use membership clones, while LTO B inlines dispatch into `lookup_loop`.

The saved native build uses `cc -std=c11 -O3 -g -Wall -Wextra -Werror -fno-omit-frame-pointer`; LTO uses the recorded immutable compiler image with `-flto=auto` and those same flags. Exact compiler identity remains scoped to the parent cohort metadata; no workstation compiler substitutes for either capture. Baseline ELF hashes are native `2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf` and LTO `77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb`.

| Variant | Source SHA-256, independently matched to saved metadata | Native ELF SHA-256 | LTO ELF SHA-256 |
|---|---|---|---|
| A | `ef2098f8cedf2aae88e845162d15ef1fd09a9abcaae0e3939d3043594b5a77e0` | `d77de23d4497572501e7e33abcaea6f6aa4631b0151e1482734d62586249f101` | `036fbc6a4842d53d61ee6669e16e43eee005610f8f3c2805241a2e691920cc29` |
| B | `a2f627b71b398a75a5f793132d2e15de547d3808622f949870c952506eb496fd` | `5007400df989bf4ab07c7453be9123339fe4fc61b482290f70408e9096dbf57f` | `c6cf046181210cac21f50d71ad518102ce2e367d11ea216e9988c12ff0aaef92` |
| C | `00297055998a105dd8fe4998e1d7b7a388e1a052ac2db661e494bf1f9fb6b850` | `e6543b401f4d05a08e2fc7bdb33157077a323a0bd4036a4b5087076736647266` | `f2db867187cf21cd5fd22b6d8a39c3941acef8798763bb439d2dd1679d143ea2` |

ELF identities above are recorded build metadata, not newly recomputed ELF hashes; the review had saved text captures. Actual source hashes were recomputed. All source comparisons use e13d9fc88 / upstream ee8e7f701. `member_rehash` is at set offset 64, the leaf migration stamp at leaf offset 22, and resize generation at context offset 44.

## Stable-path control flow

One entry state test is necessary dispatch and is allowed by the gate. The requirement is removal of live resize state and migration filtering from the subsequent stable table probe, including narrow/wide IDs and repeated candidate misses.

| Variant/build | Dispatch and stable path | Gate |
|---|---|---|
| A native | Raw at `c990` hashes once at `c9bc`; `c9c0` loads state and `c9c8` branches active to `cc40`. Stable falls through `c9cc`; narrow/wide leaf calls are `cab8`/`cd50`. No later state reload or stamp load/compare exists in this raw function. Active restores the frame and tail-branches at `cc60` to `zbtIndexReadResizing` (`76c0`). Prehashed entry at `cdb0` likewise has one state load and no hashing. | PASS |
| A LTO | Scored raw at `406760` hashes at `406788`, tests state at `406790`/`406794`, and enters stable at `406798`; leaf calls `406888`/`406a94`. Active tail-branches at `4069dc` after frame restoration. The actual membership clone at `406b80` hashes at `406ba4`, dispatches at `406ba8`/`406bb0`, and enters stable at `406bb4`; leaf calls `406ca4`/`406eb4`. Both complete stable bodies omit state/stamp accesses. `lookup_loop` calls scored raw at `40c378` and the membership clone at `40c3c0`. | PASS |
| B native | Raw at `cdc0` hashes at `cde8`; state load `cdec` and branch `cdfc` choose tail branches to resizing (`ce14`) or stable (`ce2c`). In stable kernel `50a4`, every valid narrow candidate reaches state reload `5180` and null branch `5184`. Nonnull code loads generation/stamp at `5188`/`518c`, compares and filters through `51a4`; leaf call is `51b4`. Wide path repeats at `5300` through `5338`. Invalid-reference paths reload state at `5204`/`538c`. | **NONE** |
| B LTO | Dispatch is inlined into `lookup_loop`. Membership hashes at `40c3b0`, loads state at `40c3b4`, and branches at `40c3c0` to stable call `40c3f4` or resizing call `40c3d0`. Subsequent stable-loop calls at `40c448` retain the same non-inlined stable kernel. Scored paths similarly call it at `40c488`/`40c4ec`. Kernel `405688` still reloads state at `405754`, branches at `405758`, and retains stamp comparisons at `40575c`–`405778` before leaf call `405790`. Wide equivalents are `405940`–`40597c`; stale-reference reloads are `4057e4`/`4059cc`. | **NONE** |
| C native | Raw at `da90` hashes at `dac0`; state load/test `dac4`/`dac8` branch directly to stable `db0c` when null. Active calls generic resizing at `daf0`, then returns. Stable narrow/wide leaf calls `dbfc`/`ddb0` have no later state/stamp loads or migration filtering. Prehashed entry `dee0` has the same split, with state load `deec` and resizing call `df04`. | PASS |
| C LTO | Scored raw at `4080e0` hashes at `40810c`, loads/tests at `408110`/`408114`, and enters stable `408154`; leaf calls `408248`/`4083c4`. Membership clone `408530`, called at `40ce00`, hashes at `408558`, tests at `40855c`/`408560`, and enters stable `4085a0`; leaf calls `408694`/`40881c`. Both stable bodies omit state/stamp accesses. The scored raw call site is `40cdb8`. | PASS |

For B, a truly stable input takes the null branch and therefore **does not execute the conditional migration-ID loads**. The failure is the retained per-candidate state reload/null branch and unspecialized filtering machinery, not a claim that a null context is dereferenced. LTO's caller optimization does not remove those checks inside the non-inlined kernel. This confirms the earlier local B failure on both exact ARM builds.

A/C stable invalid/free-ID paths reduce the original resize-dependent assertion to failure, as expected with null resize state. Their normal valid-ID checks remain. Narrow/wide loops, candidate-mismatch backedges and displaced probing stay entirely within the stable body; none can enter resizing without the entry active branch.

## Static stack and text tradeoffs

Frames below are procedure-local allocations, not total process stack usage or measurements. Disassembly spans run from function entry through the last emitted non-padding instruction; they are not claimed as independently queried ELF symbol sizes.

| Variant/build | Stable search frame | Resize frame and call relationship | Stable raw/kernel span | Whole ELF `size` text bytes |
|---|---:|---|---:|---:|
| A native | 160 B | 176 B; raw restores its frame before tail branch | raw 1,028 B; prehashed 996 B | 96,559 |
| B native | 176 B | 176 B; 48 B raw wrapper restores before either tail branch | stable kernel 1,064 B; raw wrapper 112 B | 94,631 |
| C native | 176 B | 320 B; caller frame remains, so raw+resize is 496 B before nested callees | raw 1,076 B; prehashed 1,048 B | 92,487 |
| A LTO | 144 B | 176 B; raw/cloned raw tail-branch after restoration | scored raw 1,056 B; membership clone 1,056 B | 56,563 |
| B LTO | 176 B kernel | 176 B resize kernel; dispatch is inside the 416 B harness loop frame | stable kernel 1,080 B; no separate raw symbol | 56,695 |
| C LTO | 160 B | 304 B; caller remains, so raw+resize is 464 B before nested callees | scored raw 1,104 B; membership clone 1,112 B | 59,267 |

C's generic resize fallback spans 6,736 B native and 8,632 B LTO; A/B's raw-only fallbacks span 1,992 B native and 2,104 B LTO. C's broader optional-output interface retains a stack argument and prevents the tail-call shape seen in A. Native `lookup_loop` has a 176 B frame in all variants; LTO A/C loop frames are 400 B versus B's 416 B. B's small native raw wrapper must not be reported as a 48 B stable search frame, nor added to its tail-called kernel frame.

These differences expose possible resize-call, code-layout and register-pressure tradeoffs. They do not identify a bottleneck or predict elapsed time. In particular C has smaller native whole text despite its much larger shared resize procedure, and larger LTO text; total-text changes reflect compiler sharing across callers, not just the primary path.

## Semantic review and remaining risk

Independently compared source bodies: the table finder, leaf finder, tag-bit math and rehash-step implementation are identical to baseline for A/B/C. C's extracted resizing finder equals the original complete generic finder body after renaming. A/B call the unchanged generic finder with original raw-reader output arguments. No additional hash, copied probe, comparator change or layout change appears in these patches.

The active fallbacks retain one-step progress and reload state after the step, which can free the context. Native A/B call the step at `76f4` and reload at `76f8`; C calls at `75a0` and reloads at `75a4`. LTO A calls/reloads at `405f58`/`405f5c`, B at `4066d8`/`4066dc`, and C at `405f70`/`405f74`. The surviving active path searches the destination first and retains migration ownership checks; completion switches safely to current-table search. No entry-context pointer is reused across the step without reload.

C has wider semantic exposure because generic lookup callers change too. Its stable locals preserve original NULL/zero defaults and publish found outputs on hits versus insertion hints on misses. Position-without-bucket continues to return the hit position and zero on miss. Existing paired-state C evidence covers all 32 output combinations; this review inspected the implementation/evidence but did not rerun it. The three reports record their original 57+57, 36-cell and 135,000-output checks plus focused active/final-resize cases. This static review does not replace those tests or independent correctness review.

No static semantic defect was identified. Before adopting A or C, separately qualified resize/displaced traffic and affected mutation/output guards remain mandatory, followed by the preregistered block gates, held-out confirmation and matched profiles. B must not enter timing merely because its wrapper is smaller or its correctness passed. Static selection: **A/C eligible; B NONE; no adopted winner**.

## Consultation and TMA

Own fresh CPU-perf/library-status tool-name discovery again returned no exposed matches. The actual shared raw-state stdio consultation remains the relevant evidence: bundled deb5a0bac467, 3/287 indexed sources, 158 passages, no supporting primary passage. It is not a call by this reviewer. No source-derived speedup claim is made.

| TMA category | Qualified ARM baseline | H5 candidates |
|---|---|---|
| Frontend_Bound | unavailable | uncollected |
| Bad_Speculation | unavailable | uncollected |
| Backend_Bound | unavailable | uncollected |
| Retiring | unavailable | uncollected |

Qualified slot scope/formula and child categories remain unavailable. Static frame sizes and branches do not substitute for TMA. Separate Intel evidence is not an ARM cause. No collector or source modification was made during this review.
