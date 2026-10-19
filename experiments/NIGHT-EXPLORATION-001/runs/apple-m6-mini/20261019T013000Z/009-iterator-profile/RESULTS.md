# M6 baseline iterator profile — 16/16 captures sufficient

No optimization is selected. These are standalone baseline PC observations, not a candidate comparison. The exact Intel iterator referee and microbench source were copied from `c3e5882ca5ff3b04f65769d4ba49e4347d1f6351`; original PLAN.md/MATCHED-PROFILE.md remain clearly Intel evidence. The new M6 schedule is LOCAL-PLAN.json. No Intel/M6 timings or samples are pooled.

Baseline source/header match the frozen Intel source exactly (d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2 /496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83). Neither target nor referee semantics changed. Only a new Apple profiler bridge implements the existing PROFILE_SAMPLE hooks using the unchanged 002 public self-process sampler.

Four contracts pass native and ASan/UBSan at size 1000 / requested 2003 / seed 1 (8 runs; each rounds to 3000 items). Member bytes 16; full-output mask 7 consumes pointer/length/score, score-only mask 4 requests score only. Exact member bytes/order, finite-score bits, iterator-copy next state, nullable outputs, exhausted state, checksum/count and owned memory checks are retained.

Exactly 16 serial release captures ran: 100K/1M × four contracts × seeds 1/2, 100 million items each, three actual-contract warmup traversals. All 16 capture counts meet the fixed 25-PC minimum (43–83); no capture was retried. Sampler requested 1000 us ITIMER_PROF; delivered counts do not establish timer precision, hardware events or unbiased time shares.

|Members|Contract|Seed 1 PCs|Seed 2 PCs|IteratorNext PCs / all scoped PCs (two seeds)|
|---|---|---:|---:|---:|
|100000|integer-full-forward|73|83|155 / 156|
|100000|integer-full-reverse|68|72|137 / 140|
|100000|integer-score-forward|46|43|85 / 89|
|100000|fraction-full-forward|68|64|130 / 132|
|1000000|integer-full-forward|65|71|132 / 136|
|1000000|integer-full-reverse|75|76|149 / 151|
|1000000|integer-score-forward|53|56|107 / 109|
|1000000|fraction-full-forward|71|70|136 / 141|

Across all 16 captures, 1054 PCs were recorded: 1031 in zbtreeIteratorNext, 11 in the traversal consumer and 12 in __thread_selfusage. These totals describe this fixed matrix only. Per-capture bins and per-contract two-seed views are retained; unlike-contract populations must not be interpreted as one universal workload.

The iterator body has 155 instruction lines. Its full-output path still computes the packed-offset-array base using count×score width, maps orientation, loads a 16-bit record offset and reads the packed-record prefix. Score-only calls bypass the member-offset/prefix path. The score decoder and iterator advance remain separate observed instruction regions. Exact instruction offsets and manual source-region classifications are in pc-map.json. Reverse names traversal direction; these profiles do not establish the physical reversed-leaf population.

The entry saves six register pairs in a 96-byte frame (+0x0..+0x18); the epilogue restores them (+0x250..+0x268). These exact stack regions contain 151 and 152 PCs respectively across the fixed matrix, with no cycle-cost interpretation. The frozen compat/server.h declares standalone_panic without a non-returning contract, while compat/standalone.c unconditionally aborts. The iterator body calls only that panic on its cold paths. This is a possible baseline adapter/compiler-contract artifact contributing to frame generation; it is not a cache diagnosis. Root has independent review of this possibility pending. These profiles remain valid for the exact frozen baseline; no adapter/target/referee change, rebuild or recapture was made.

Selected per-contract instruction observations (two seeds combined, counts only):

- 100000 / integer-full-forward: +0x1c: 19 PCs, `ldr	x19, [x0]`; +0x1f0: 18 PCs, `str	x8, [x4]`; +0x250: 15 PCs, `ldp	x29, x30, [sp, #0x50]`.
- 100000 / integer-full-reverse: +0x1b0: 24 PCs, `mov	x11, #-0x1`; +0x1c: 23 PCs, `ldr	x19, [x0]`; +0x4: 11 PCs, `stp	x26, x25, [sp, #0x10]`.
- 100000 / integer-score-forward: +0x1c: 17 PCs, `ldr	x19, [x0]`; +0x1f0: 15 PCs, `str	x8, [x4]`; +0x250: 10 PCs, `ldp	x29, x30, [sp, #0x50]`.
- 100000 / fraction-full-forward: +0x1f0: 21 PCs, `str	x8, [x4]`; +0x1c: 16 PCs, `ldr	x19, [x0]`; +0x4: 12 PCs, `stp	x26, x25, [sp, #0x10]`.
- 1000000 / integer-full-forward: +0x1b0: 23 PCs, `mov	x11, #-0x1`; +0x1c: 17 PCs, `ldr	x19, [x0]`; +0x1f0: 12 PCs, `str	x8, [x4]`.
- 1000000 / integer-full-reverse: +0x1b0: 29 PCs, `mov	x11, #-0x1`; +0x1c: 17 PCs, `ldr	x19, [x0]`; +0x1f0: 15 PCs, `str	x8, [x4]`.
- 1000000 / integer-score-forward: +0x1b0: 18 PCs, `mov	x11, #-0x1`; +0x1f0: 18 PCs, `str	x8, [x4]`; +0x1c: 15 PCs, `ldr	x19, [x0]`.
- 1000000 / fraction-full-forward: +0x1c: 21 PCs, `ldr	x19, [x0]`; +0x1b0: 21 PCs, `mov	x11, #-0x1`; +0x4: 11 PCs, `stp	x26, x25, [sp, #0x10]`.

The M6 PCs are distributed among entry/frame, score-mask/output, member materialization and advance regions. The dominant Intel packed-prefix comparison observation should not be assigned to M6 from geometry or symbol overlap. Seeing the repeated offset-base arithmetic in M6 assembly establishes that the proposed Intel cache would change real work here; it does not show that this work dominates or that the exact patch will improve M6. A replication decision, three-implementation selection, correctness guards, qualification, serial comparison, fresh confirmation and review remain separate future steps.

Sampling starts/ends at the original referee hooks. They bracket QoS/CPU/thread-clock observations surrounding the traversal as well as the traversal itself; fixture construction, full verification and warmup are excluded. The 12 thread-selfusage PCs make this boundary visible. Raw command UTC bounds cover the process, not individual PCs. No frequency/DVFS/core-residency/cache/branch/cycle or isolated instruction-cost inference is made. Emitted elapsed fields are unused.

Existing 002 known-work controls were inspected and pinned without rerunning them. Freeze.json was written after correctness and before all captures; it pins exact sources, sampler/bridge, flags/compiler and binaries. Raw profiles remain ignored scratch with SHA256/command/time bounds in public per-capture JSON and commands.jsonl.

Limitations and retained failures: initial new bridge compilation omitted string.h; fixed only that bridge, preserving its failed log and reusing successful native/sanitizer binaries. No capture had started. Post-link dsymutil exited 0 but warned compiler temporary objects were gone; no DWARF lines were recovered. Public warnings use generic temporary paths; raw warnings/hash remain scratch. Exact PC offsets map to release assembly, with manually inspected source references, not exact DWARF source attribution. No rebuild or recapture was made to repair symbolization.

All experimental processes finished. Participant /root/followup_proposal_b, inherited Codex/GPT-6 family; exact serving model/token usage/cost unknown. No source optimization, Git write, shared-memory edit or new agent was performed.
