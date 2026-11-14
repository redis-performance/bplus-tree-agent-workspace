# Slot-hint census independent source review

**PASS for staging the exact frozen diagnostic sources.** No source-level blocker remains in this freeze. This approves neither fleet execution nor a candidate, performance result, qualification or source adoption. Exact target compiler/ELF review, operational admission and validation of all six eventual raw outputs remain separate gates. H2 and Q4 remain PARK; ARM remains released.

| Reviewed artifact | SHA256 |
|---|---|
| Complete 93-entry source freeze, `SHA256SUMS` | `f2f8f882de6d48a6207ffff86f9af5fae53461ff0593e9e06bcc39c4fa82849b` |
| Approved protocol | `9e47780f163e9399f66b5059eedada278c49504154ed1cf25f9051109130f117` |
| `GENERATION.json` | `ba617cffda9c52c932dcb5777a700de440d39a0ab12fd83d40eedfb5250f6348` |
| `shadow.h` | `6792cb830b9f3a34beb8f29bec7de330e9ccce814df9a0152323796e2fa078a5` |
| Strict output checker | `9c415e2a56faa6edd7babdd1e7c9c74cc03d38227f16637faf2a13af4c742c04` |
| Native v6 compile-only ELF | `2e689ccbc0380e46d234dc51543c1edcd7bead7ff6d85065dba475a82fa1c315` |
| LTO v6 compile-only ELF | `f871fe375fbe2a085542a49ed3f09650a037c36ed73d2fda00cda3f7f9dc2c3f` |

This reviewer authored proposal B and the earlier [design review](SLOT-HINT-CENSUS-DESIGN.md), and supplied adversarial findings during preparation. The diagnostic implementation and checker have a separate author. This is independent implementation review, not an assertion of independence from the design discussion. Exact model, tokens and costs are unknown. This review performed no fleet operation, C/workload execution, timing or profiling.

I independently verified all 93 freeze entries, reran all **20 Python synthetic/static tests**, and reran `validate_static.py` against both final v6 builds: all passed. I also reran `objdump -d`, `nm` and `nm -u` on each saved ELF and obtained byte-identical assembly, symbol and undefined-symbol artifacts. Build receipts bind the current generated source, shadow/emitter/hooks, build script, generation manifest, seven frozen dependencies, compiler output and actual ELF/artifacts. These local GCC 13.3 artifacts establish compile/static properties only. The exact frozen baseline C and lookup remain `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9` and `1e6dc19c9b0f49abafb75c67e3434a87cc6d7d5222049c90a68368755c2a5827`.

The generated patch is restricted to the admitted hooks and disclosed diagnostic retention declaration. The original leaf-search body and fixture/setup regions remain byte-identical. Actual final native and LTO code retain the original helper's `memchr`/`memcmp` paths. The wrapper CFG has exactly one original-helper call or tail call on every normal exit; assertions terminate separately. Native original calls are at `0xb672` and `0xb79e`; LTO at `0x751c` and `0x764b`. This covers hinted successes as well as misses and disabled hints. The source keeps original arguments, output writes and return value; hinted position and requested score bytes are checked against the original result, never substituted for it.

The earlier LTO v2 artifact failed this real-call gate because it inlined away the helper. Its failure is preserved. The final diagnostic uses `noinline,noipa` on the helper declaration while preserving its complete body. This is an accepted diagnostic retention measure, not a candidate optimization or evidence about the cost of an uninstrumented lookup. The current CFG decoder is specific to the saved x86 assembly; its PASS cannot transfer to a different target build.

Allocation tracking uses bounded registry slots with globally unique checked generations, distinct from pointer values and owner descriptors. Allocation/release, duplicate-table copies, promotion and defrag rebinding are explicitly hooked. Reused addresses obtain new generations; duplicate live keys fail. Old allocation keys are captured as integers before relocation. Duplication copies existing hint state into a distinct generation without refreshing stale identity. Empty descriptors carry no generation. Unknown nonempty identities, inconsistent width/size, invalid bucket domains and exhausted fixed bounds fail closed.

Only existing CopyLeaf/Rebuild insertion contexts can seed. Every slot-zero ID write invalidates, including same-ID writes; all legal original leaf IDs retain their original representation. Counted slot-zero write → attempt → seed records must form an adjacent chain. Nonzero-slot attempts are recorded but cannot seed. Context checks apply before the noncounted-phase early returns as well as during counting. A seed copies its hash, length and member bytes; it retains no pointer to a mutable record or external allocation. Current seed identity and current query equality are separate predicates: seed hash determines staleness, query hash determines a potential match. Out-of-range means position >= current count. External cached-hash rejection precedes member pointer decoding. Stale does not automatically mean query failure, and query mismatch does not automatically mean stale.

Review found a real additional filter consumer: reference maintenance during updates can call HomeMayContain without a lookup table-call context. The final hooks and schema distinguish lookup, reference maintenance and direct scan, with separate totals and valid query/context links. Each wrapped HomeMayContain executes once and returns its original decision. Folding observes unchanged words only. The OR mapping cannot introduce false negatives; checked bit/tag cases supplement the algebraic argument. Additional folded positives describe only evaluations reached by the original path, not extra probes, a complete alternate execution or a speed estimate.

The output checker rejects undeclared fields, duplicate JSON keys, nonfinite constants, invalid integer domains, bucket sizes, phase/event order, generation transitions, mutation chains and inconsistent totals. Its CLI calls the strict `loads()` for every raw file before `check_all()`. Final audit callers must use that loader too; parsing with an ordinary JSON loader first would discard duplicate-key evidence. Counted mutation totals, terminal/stale partitions, useful query IDs and consumer totals are reconstructed from ordered raw events. Initial snapshots are bounded by prior seeds and possible duplication amplification; zero earlier seeds cannot produce hints. Full setup/warmup seed history and exact copied member bytes remain C-asserted evidence, not independently reconstructed from the JSON. The tests exercise parser counterexamples and synthetic lifecycle records; they do not establish runtime coverage of those C paths.

The counted phase preserves the fixed seed17 fixture, 1000 warmup sweeps, one counted read sweep or two update sweeps and original operation/hit/score models. Immediate tree-owned memory endpoints remain the independent fixed values and precede validation. Original destruction completes before final output; the completion fence requires zero live generations and absent query/table/seed contexts. Cleanup lifecycle events are retained. Bounds are checked before append/increment; exceeding a bound invalidates the census rather than truncating it or authorizing an expanded rerun.

All 13 clock-denial wrappers remain linked, with no unresolved denied clock symbol. I independently rederived the separate clock-probe disassembly and hashes: its explicit clock call targets `__wrap_clock_gettime`. The probe was not executed. This establishes owned linked-call interception, not protection against hypothetical injected libraries implementing private clocks.

Later execution still must establish successful final records for all six unchanged fixtures and pass the strict checker. Large legal IDs, active resize, duplication, defrag, scan, arbitrary binary members and all mutation histories have no new C runtime coverage from this preparation. No observed hint count exists. Zero useful primary exposure closes the lead; nonzero exposure does not meet the unchanged speed/memory/guard gates or admit an implementation candidate. No performance-attempt count changes follow from this source-stage review.

The shared fresh CPU Performance Engineering consultation supplied no supporting passage. This reviewer's tool discovery found no callable cpu-perf/library-status endpoint; no consultation is attributed to this reviewer. TMA was not collected, and no candidate exists.

| TMA category | Baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

All child categories are likewise unavailable. No hotspot, count, alternate machine or illustrative value substitutes for those shares.
