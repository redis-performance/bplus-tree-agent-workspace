# Slot-hint census: prepared, not executed

The isolated baseline diagnostic is ready for independent source, parser and
saved-artifact review. Twenty Python synthetic/static tests and native/LTO
compile-only validation pass. No C diagnostic, clock probe, correctness binary,
workload or counter census has executed locally. No fleet operation occurred.
There are no observed hints, path counts, speed results or selected candidate.

The admitted [design revision 1](PROTOCOL.md) remains frozen at SHA256
`9e47780f163e9399f66b5059eedada278c49504154ed1cf25f9051109130f117`.
Its earlier revision is preserved in `design-history/revision0/`. Original source
and lookup remain SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`
and `1e6dc19c9b0f49abafb75c67e3434a87cc6d7d5222049c90a68368755c2a5827`.
The seven frozen source/header/compat/vendor inputs are in `DEPENDENCIES.json`.
No original file, prior census, variant, fixture, seed or compiler flag changed.

## Generated source and maintained shadow state

`generate.py` reads exact pinned source and lookup bytes, verifies every dependency,
and writes a separate source, harness, reconstructible patch and generation
manifest. Normal generation refuses existing outputs; `--check` is read-only.
`hooks.py` confines edits to index/lifetime/filter hook sites and one disclosed
diagnostic retention attribute. `shadow.h` contains fixed arrays and assertions;
`emit.h` serializes scalar records after cleanup.

Shadow allocation generations are globally unique across registry-slot reuse.
Allocation, duplication, release, promotion and relocation preserve exact bucket
ownership, width and size; duplicate live integer keys fail. Duplication copies
stale hints as they stand. Rebinding captures the old address as an integer before
the original allocator callback may free it. All hinted member identity is copied
hash/length/bytes, not retained leaf or external pointers.

Only the existing CopyLeaf and Rebuild loops open a nonnested seeding context.
Their one existing raw insertion consumes it exactly once, with owner/table/leaf/
hash/physical agreement. Every slot-zero ID write invalidates; a subsequent known
position may seed. Other slots do not invalidate or hold hints. Query/table entry
checks enforce an absent seed context even outside the counted phase. Setup and
warmup maintain hints; counted entry resets only counters and records a bounded
snapshot of live hint codes/IDs/origins. Full narrow and wide ID domains remain.

The full original leaf search executes once per eligible leaf event. Private
shadow comparisons classify disabled, out-of-range, wrong raw tag, complete
predicate failure or success; seed identity separately classifies stale versus
unchanged. Staleness uses the seed hash; query equality uses the query hash.
External hash rejection precedes pointer decoding in both. Prospective outputs
remain private, and a shadow success must agree with the original actual result,
logical position and requested score bytes.

## Review-driven corrections before the freeze

LTO v2 inlined the original leaf helper into the shadow wrapper, failing the
design's real-call gate. The generated helper declaration now has diagnostic-only
`noinline,noipa`; its complete original body is byte-identical. This is an explicit
instrumentation retention measure, not an optimization, new benchmark flag or cost
claim. Native and LTO final control-flow validation inspects each normal wrapper
exit and requires exactly one call or tail call to the retained original helper.
It also checks the helper still contains its memchr/memcmp path. Assertion exits
are distinguished from normal returns; compiler-generated fatal assertion clones
are admitted only after checking their straight-line call to the panic function.

Independent review identified reference-maintenance calls to the home filter
outside an active lookup table call. Filter events now have an explicit consumer:
0=lookup, 1=reference maintenance, 2=direct scan. Lookup and reference hooks call
the original HomeMayContain once, then observe its unchanged word/mask. Direct
scan observes its original test. The returned decision is always original; a
folded positive never drives extra probing. Query-linked reference/scan events
have no lookup call ID, and each consumer has separate totals.

Counted mutation events include every known-position insertion attempt, including
nonzero index slots. Slot-zero ID write → attempt → seed is an adjacent event
chain. Every slot-zero attempt must produce one seed, and nonzero attempts cannot
seed. The checker reconstructs all four counted mutation totals exactly. Setup,
warmup, validation and cleanup mutation totals are C-asserted aggregates; they are
not per-write traces. Initial hint snapshots are C-verified and bounded by prior
seeds and possible duplication amplification; their full warmup history and exact
seed bytes are not independently reconstructed from JSON. Zero earlier seeds
cannot admit a nonempty initial snapshot.

Every original free runs before the final success record: source, target, then
member/miss buffers. The completion fence requires an empty allocation registry
and absent query/table/seed contexts. Cleanup lifecycle events are in the final
record. Immediate owned bytes were captured before validation and remain exact
independent baseline values; later validation bytes never replace that endpoint.

## Static evidence and honest limits

`STATIC-VALIDATION.json` joins each final saved build receipt to current generated
source, helpers, build script, manifest, original dependencies and actual ELF.
Receipts also hash saved assembly, symbols, undefined symbols and compiler output.
Native/LTO GCC 13.3 compile-only builds retain all 13 clock-denial wrappers, each
calling write and exit, with no unresolved denied clock symbol. `CLOCK-LINK-CHECK.json`
records a separate never-executed explicit-clock link probe whose disassembly calls
the denial wrapper. This covers owned linked clock calls, not hypothetical injected
libraries with private timer implementations.

The final native ELF is `2e689ccbc0380e46d234dc51543c1edcd7bead7ff6d85065dba475a82fa1c315`;
the final LTO ELF is `f871fe375fbe2a085542a49ed3f09650a037c36ed73d2fda00cda3f7f9dc2c3f`.
These are controller compile-only artifacts, not target compiler or runtime proof.
The original-call CFG checker currently decodes saved x86 objdump text; a future
target artifact needs its own exact emitted-code review, not a carried-over PASS.

`static-tests-final.stderr` records 20 passing Python tests: fixed six-case models,
memory/cleanup failures, prior admission counterexamples, terminal/stale bijection,
equal-count out-of-range hints, nonzero index slots, successful-original implication,
folded false-negative rejection, generation/duplication/reuse/relocation states,
counted invalidation/attempt/reseed, copied stale hints, reference filters, complete
counted attempts, exact schema/duplicate-key rejection, ordered event scopes and
resize completion. Source/scope/fence validation and deliberately skipped/doubled
original-call CFG negatives are included. Integer checks exhaust all byte tags,
single-bit filter bases, tag pairs and hint-byte replacements; the general OR
property is algebraic, not enumeration of all 2^64 filter words.

Failed or superseded preparation is retained: initial signedness compile failure,
the static printf matcher confusing snprintf with output, outlined panic CFG
classification, actual LTO original-call failure, the reference-consumer review
gap and the weaker parser before schema/seed hardening. Pre-checker sources and
earlier build/manifests/logs remain. None followed a C execution or observed count.

Runtime coverage remains absent. The original six warm fixtures are bounded;
large IDs, active resize, duplication, defrag, all mutation histories, arbitrary
binary records and scan are not newly exercised by this preparation. Synthetic
records are validator inputs, not measured or observed fixture behavior. Failure
of later correctness or any fixed bound invalidates the census; no inputs, hints
or bounds may be expanded after observing opportunity under this freeze.

## Interface for a later separately admitted action

From the checkout root, `sh experiments/ARM-LOOKUP-CONT-001/slot-hint-census/build.sh
OUTPUT_DIRECTORY native|lto` compiles and inspects only. OUTPUT_DIRECTORY must not
exist; `TASK_CC` chooses the compiler. No build action executes its output.
The future binary interface is `census CASE`, one of the six fixed cases, without
seed/count/timing parameters. Each case is a separate one-shot process. Save full
stdout/stderr and exit status. Validate all six saved stdout files with
`python3 experiments/ARM-LOOKUP-CONT-001/slot-hint-census/check_output.py FILE...`.
The checker rejects duplicate JSON keys, nonfinite constants and undeclared fields,
then reconstructs event order, lifetimes, bounds, counted hints and aggregate totals.

`GENERATION.json` contains `generated_sha256`, `generator_inputs_sha256` and
`original_dependencies_sha256` maps, alongside upstream/source/lookup/fixture/setup
pins. Paths in the first two maps are relative to this directory; original dependency
paths are relative to its parent experiment directory. The complete directory is
frozen by `SHA256SUMS`. Build receipts use checkout-relative paths.

Intel-only fleet build, static review and later untimed execution are distinct
controller actions requiring authorization and owned-runner checks. This artifact
does not authorize them. ARM remains released. Zero useful primary exposure closes
the lead; nonzero exposure and weaker-filter positives imply no speed prediction,
candidate admission, qualification, replication or selected source.

Public role: diagnostic preparation author. The shared actual fifth consultation
and own unavailable cpu-perf endpoint discovery are recorded in the design. There
is no supporting retrieved passage. Backend provenance is private; exact costs
remain unknown.

| TMA category | Baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

No roots or children were collected; no diagnostic executed and no candidate exists.
