# Guarded physical-slot lookup: read-only preparation A

Preparation only; no hypothesis selected, source patch, build, executable test, profile or timing. Await the root's newly frozen common packet, fresh corrected-baseline profile and A/A before an independent proposal. Root owns publication of scope/checkpoints/evidence on main. This scratch note is not a candidate or acceptance record.

Participant `/root/followup_proposal_a`; inherited Codex/GPT-6 family, exact serving model/token/currency costs unknown. I previously authored parts of006 harness preparation and later raw audits; this operational role does not make historical timings fresh or supply independent candidate confirmation.

## Exact source and natural semantic boundary

Current C/H hashes remain d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2 /496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83. Adapter H/C are corrected468a5811ad80fa4dc47196b90835586cbbbd8b7d235af225092637e930708fa7 /c9237cd2e2fb08fff5c67431a9de5d6d1596d6211082a068116040c477689fb3.

Source `zbtScoreLeafFindMember` at1275 identifies a physical tag slot, verifies record/hash/length/member bytes, converts it to a logical position, then calls the logical decoder when a score was requested. `zbtScoreLeafScore` at499 maps that logical position back to physical. Reversal maps are involutions, but reversed-score base subtraction is still essential: cancelling index conversions must not cancel `score_base - delta`.

A natural semantic dispatch input is the optional **position output**, independently of tree size, CPU model, observed timing or member length. Current call graph:

- `zbtreeScoreRaw` at3183 passes all position/leaf/bucket outputs NULL; `zbtreeScore` wraps it.
- `zbtreeScores` at3197 passes each score output but no position outputs.
- `zbtreeRank` at3262 requests a leaf and logical position, whether or not its optional score output is NULL.
- `zbtreeFindForAdd` at3225 requests score-leaf/position and insertion bookkeeping.
- Delete at3514 requests positions with a NULL score output.

Thus `score != NULL && position == NULL` is a *potentially useful seam* for a score-producing, position-free path while retaining the exact original generic path for position consumers. It is not yet a selected hypothesis or a claim of useful codegen. Membership-only calls with both outputs NULL must remain valid and do no unnecessary score decoding. Misses must preserve output sentinels. There is no basis here for a benchmark-size dispatch such as100K-only, or a hardware-specific threshold.

`position == NULL` does not mean the entire public operation is mutation-free: `zbtIndexFind` at2258 advances an active member-index rehash before searching both tables. Every proposed seam must preserve that behavior, migration/leaf-ID checks, deletion filters, collision checks and insertion hint semantics. The leaf helper receives only the optional logical-position pointer; insertion-bucket bookkeeping is higher in the call chain. A future public-lookup specialization must not bypass that shared machinery.

## Historical evidence and novelty obstacle

004 B patch SHA b1ca29ae4594f00e0e5d5761462e9c1058d5249fde5708ad761c7329a91ec513 adds `zbtScoreLeafPhysicalScore` using existing `zbtReadBits`, and uses it for **every** score-producing helper call, even when a logical position is also requested. It computes the position only when requested. Therefore “only calculate a position if requested” is already old work; a new experiment must distinguish an actual semantic guard/original generic fallback or other independently supported mechanism, not relabel004 B.

004 results: B's100K median−4.800%, all six blocks−6.243..−3.482%, old same-cell AA maximum0.744507%; 1M median+0.428%, range−3.926..+5.681%, AA maximum4.183806%. This is a **legacy-adapter,100K exploratory lead only**; dual-primary REJECT/source NONE. There was no candidate profile, full candidate guard screen, fresh confirmation or independent final semantic/performance review. It cannot qualify current corrected source or a newly guarded patch.

004 diagnosis has56/139/266 hit PCs at10K/100K/1M; platform memchr21/57/148. Two miss captures remain insufficient. Release code shows the conversion round trip and B's helper shrinks161→151 static instructions. Those are region/codegen observations, not cycle costs or a causal explanation of B's timing.

006 tests a different mechanism: generic helper caller exposure, explicitly retaining the original decoder/scanner. Its B dispatches on non-NULL `score_pos` to an original generic wrapper and otherwise exposes an unchanged inline body; this already demonstrates the optional-output seam as semantics, **not** a validated guarded physical decoder. A/B/C ScoreRaw instruction streams normalize identically at601 instructions/240-byte frames versus old345/176-byte caller plus144-byte helper frame. Those are historical legacy-adapter binaries. The two-primary screen rejects all variants.006 contains no successful candidate-profile validation; its baseline profile context comes from earlier evidence. A future experiment must avoid silently combining failed inlining and physical decode families.

The later corrected020 profile remains useful location evidence, but its original-style frontend and fixed10M/three-warmup captures are not qualification of a newly chosen independent-query referee, counts or binary. Fresh matched baseline profiling is required before proposals here. No memchr replacement, early decode, prefetch, cache/frequency claim or tree speedup is supported by this preparation.

## Reusable referee contract, not a runnable old campaign

006 PLAN defines101 unique cases:40 standard,30 independent hit/miss/mixed lookups,6 public batch and25 reversible update-pattern cases. Independent lookup uses a query permutation distinct from insertion order and binary member lengths8/16/319/320/321/1024. Batch1/16 and five sizes100/1K/10K/100K/1M remain relevant. Source driver hash bd7cd797af4a6c58d3b294d3e81d34908c129df95c1b04f2010935ee1c28e38f; lookup referee a325dbc6429f770c7c09188c9091ff9dcdcdfbb544996dc237923c647d0d2ea6.

The historical protocol calibrates baseline-only with three observations/cell; fastest positive rate fixes counts targeting100ms, capped100M operations. Six process-level ABBA blocks share counts, rotate cells/variants and preserve every row. Original full AA had39/101 qualified,62 noisy, zero short windows;100K primary qualified,1M failed1.252%. Long windows did not establish precision. All101 were baseline coverage, **not candidate guard passes**.

Replicated insert/delete prepare independent trees outside timing, limit4096replicas/64MiB estimated and final tree-owned working set, preserve per-tree owned bytes and validate each final tree. This guard is not transient allocator peak. Single-tree original behavior remains separate. Other operations reject replicas>1. Reuse their validated semantics/accounting, not old calibration counts or allocator-address comparisons across build modes.

The old driver must not be run unchanged: it pins legacy worktrees, an expired03:10–04:40 experiment, old candidate identities and old output paths. It uses `subprocess.run` timeout handling, not the newer audited owned-process-group cleanup/watchdog. A new authorized harness must preserve referee checks, freeze current corrected support files/compiler/options/paths, use safe owned cleanup and clipped total/child/global bounds, retain spawn/timeout/partial-output journals, check hashes before/after and publish a reviewed immutable freeze on main. No old failed schedule is restarted and no count retuning follows failed controls. Matched relative frontend paths/literals, assertion/hash/allocator flags and no-LTO policy must be common across all new sources.

## Workload and correctness inventory for the shared packet

Useful **candidate cases to declare**, without selecting primaries here: independent successful score lookup at100K and1M with16-byte members; membership-only (score NULL); misses and mixed traffic; public batch1/16; and raw-byte versus sds API parity. A semantics-only guard applies at all sizes, so1M cannot be presumed isolated by a position-output condition. The future chair must explicitly preregister whether the question is dual-primary or a fresh100K-scoped question with1M guarded; historical failure cannot be retroactively changed.

Retain all101 original performance obligations plus applicable original long-key and focused score cases. Rank with and without score, reverse rank, FindForAdd/update patterns, insert/delete, iteration, scan, active rehash/resize/ID maintenance and tree-owned memory are necessary guards even when their source fast path is excluded: compiler context and code layout can still change.

Correctness prerequisites: original43 native and ASan/UBSan; unchanged004 physical oracle (source-included; link no second tree C), all four optional-output combinations, widths0..64, reversed/non-reversed, exact finite and signed-zero bits, ties, dense colliding tags, misses, first/last slots, bit spills/word boundaries and min/max shifts; supplement uncovered shift/count/encoding/long external-record cases without weakening original checks. Existing oracle uses counts1..8 then19/30/41/52/63/74/85/96, shifts0/3 (wide widths only0), inline8-byte records, and miss check only with both outputs NULL. Therefore add public/external full-hash collision, lengths319/320/321, miss sentinel/all-output combinations, reverse-wide finite-score and exact original generic-position assertions where missing. Negative controls should detect reversed-base and physical/logical-position mistakes, plus an incorrectly broadened guard.

Only fresh qualified AA (every block within±1%, every window>=10ms), at least six ABBA blocks, every primary block>=2% improvement, no demonstrated>1% guard/owned-memory loss, unchanged correctness/referees, held-out confirmation, matched profile/codegen and independent adversarial review could support adoption. Missing/noisy controls remain PARK. Current state is preparation/source NONE; root must freeze the new scope and budget before execution, and publish every checkpoint/evidence to main as requested.
