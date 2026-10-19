# Static findings before a fresh dual-frontend diagnosis

The retained primary and H4 guard binaries are the intended exact sources/builds. Their opposite measured effects remain valid distinct workload observations; no artifact inspected here waives the nine qualified H4 losses. Candidate REJECT/sourceNONE remains final. New optimization selection is not authorized before profile evidence.

Read-only retrieval (explicit root authorization) fetched all four exact protected ELFs, source-linked disassembly and ELF metadata, with20 read-only commands and matching before/after hashes. No benchmark, build, PMU, service, timer, lease or container change ran on ARM. Full raw ELF copies are retained locally; public assembly and retrieval manifest are in `artifact-retrieval/`. Binary hashes bind to027 final identity evidence.

| Actual artifact | SHA256 |
|---|---|
| Primary control |330b39a991573985c421194cfe83f21b44797e1a83372f623120672eb910b3bc|
| Primary A |b1cb9e4b2a1df204a75b4b4a3264364c3f0b5b46dbf475bae72c3c9a3ee5811d|
| H4 control |0af4cb0a636074bd4b7b4be4ac98c2188b4b085709130f7a6709883c9496b830|
| H4 A |6c68cd2e5ff78914f9662266af5d31fc4fe59956b2df1fbd22c95fd7e6cf9361|

## Actual generated code

Both frontends' actual `zbtreeIteratorNext` have114 instructions in control and113 in A. Same-source crossfrontend comparison has only four unequal encoded instruction words: assertion-address setup at control offsets0x1b0–0x1bc and A0x1ac–0x1b8. All other relative instruction words match exactly. This is retained in `exact-cross-frontend-iterator-map.json`; no normalization hides the four differences. Linked addresses/alignment remain different, and equal instruction bytes do not establish equal dynamic paths or costs.

Primary control IteratorNext starts0xa4b4; primary A0xa490. H4 control starts0xbe3c; H4 A0xbe18. H4 `traverse` starts0x3858 and contains282 instructions in both sources. Its runtime mask4 selection is outside the inner score-only loop: mask bits0/1 select other loops, bit2 selects `traverse+0xd4`. The repeated mask4 loop at+0xd4..+0xfc loads the returned score bits from the stack, prepares call arguments, adds raw bits and one visit to the checksum, calls IteratorNext, and branches on success. There is no per-visit mask selector in this loop. Thirteen static IteratorNext callsites exist across all output-mask loops; they are not thirteen calls per visit.

Primary's timed loop is in main and uses numeric `fcvtzu` conversion before checksum accumulation. H4 uses a raw integer load of IEEE score bits. These are real distinct consumers, but neither consumer is a measured causal explanation. Exact source-linked caller mapping remains a prerequisite for attributing new sampled periods.

## Fixture and build differences

| Dimension | Primary | H4 integer mask4 |
|---|---|---|
| Scores |i, nonnegative |i−n/2, centered |
| Timed checksum |numeric double→uint64 sum |raw score-bit sum plus visitcount |
| Allocations |2n keys; temporary buffer freed before tree |n keys; temporary buffer retained |
| Output before tree |CSV header printed before tree creation |CSV header after timed work |
| Warmup |one shuffled lookup pass |full exact verifier then three iterator traversals |
| Requested visits |50M |20M |
| Direction |forward literal |runtime forward/reverse |
| Translation unit |microbench.c |H4 includes renamed legacy microbench main |
| Past fixture seeds |1101–1103 |1301–1303 |

Both use the same hash-seed draws and insertion shuffle; identical seed/size gives equal logical permutation but not equal packed scores or placement. Ordered IEEE representation and per-leaf width/shift depend on exact scores. No retained census proves which paths dominated earlier runs; the new diagnostic separately observes exact fresh fixtures. Stdio allocation history is another reason not to claim exact heap/address correspondence from observation copies.

Both use Clang18.1.3, C11,-O3, debug info, frame pointers, identical hashing/allocator/assertions, separate target TU and no LTO/fastmath/NDEBUG. Identical source/compiler does not establish equal cache/branch placement. The new instrumented copies preserve original loop/fixture source and require their own semantic, scope, same-fixture A/A, perturbation and exact-own-code checks. Unqualified timing or ambiguous attribution stays explicit.

## Concrete preparation and limits

See `PLAN.md`, the six `cells.json` and fixed `schedules.json`:144 native A/A +144 native comparison; profile phase includes144 same-fixture instrumentation A/A +144 perturbation runs,36 cycle captures and36 scoped counter runs. Caps600/600/1200s, no retry. All are preparation only; none ran.

The separate census reads actual leaf count/width/shift/reversal and entry-weighted decode predicates, verifies each member and exact model score, and preserves frontend construction/warmup/printing order in additive copies. It reports logical packing and structural predicates, never actual historical heap addresses or dynamic PMU costs. Its source is prepared, not yet compiled or executed. Old referees and sources are unchanged. Complete executable command freeze and independent review remain required.

Authored by/root/aws_arm using native Codex tools. Exact model/tokens/USD unknown. Intel e345fa9b6 and AMD d5fc035e0 requirements were read after initial findings; this is disclosed collaboration, not a blinded independent proposal round.
