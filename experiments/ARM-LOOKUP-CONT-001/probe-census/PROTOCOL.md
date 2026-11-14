# Baseline lookup path census — preparation only, admission revision 1

This is a diagnostic instrumented copy of the original baseline, **not an
optimization candidate**. It is prepared for independent review; it has never
executed. Local work was limited to source generation, compile/disassembly and
synthetic Python validation. No path counts, elapsed measurements or performance
claims exist. No source/fixture outside this directory changed.

Source pin: `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.
Frozen lookup pin: `1e6dc19c9b0f49abafb75c67e3434a87cc6d7d5222049c90a68368755c2a5827`.
Upstream remains `ee8e7f70152404649ac947157fd662d11b4a00d5`, extraction
`e13d9fc8875a636ca07203b1f3fdd1aa28488bda`. H1–H8 changes are absent.
`generate.py` fails on a pin mismatch, emits `generated/zset_btree.c`,
`generated/census.c`, `instrumentation.patch` and `GENERATION.json`, and supports
read-only `--check`. Existing generated outputs cannot be overwritten by its
normal generation command. The manifest hashes the generator, templates,
instrumentation and clock-denial source, plus the generated outputs and original
fixture/setup substrings. `SHA256SUMS` freezes the full prepared directory.

## Fixed work and counting boundary

Only the original six cases—hit, score, miss, long, external, update—are accepted.
Seed 17 is fixed in the executable; it has no seed/count/measurement-mode argument.
Each fresh process uses the exact original 500 members, construction/reserve hints,
insertion order, byte patterns, query order and independent source/target buffers.
The fixture function and query setup are extracted byte-for-byte from frozen
`lookup.c`; the static validator checks this. Scored outputs and all exact bytes
are validated as in the original setup. The update loop's scratch score starts
at 0 solely to give diagnostic output snapshots a defined representation; the
successful API writes its original score. No query or stored score is changed by
that initialization.

Setup runs with counters disabled. Execute the original 1000-sweep warmup with
counters disabled; updates alternate fractional/integer scores exactly as before.
Only then reset shadow state, capture owned bytes and resize state, and enable
counters. Count one query sweep for the five read cases; update uses **two** sweeps
to restore integer scores. Each update operation remains the original
FindForAdd/UpdateScore pair, so 1000 operations contain 2000 public API calls.

| Case | Counted sweeps | Operations | Hits | Score sum |
|---|---:|---:|---:|---:|
| hit | 1 | 500 | 500 | 0 |
| score | 1 | 500 | 500 | 125250 |
| miss | 1 | 500 | 0 | 0 |
| long, external | 1 each | 500 each | 500 each | 0 |
| update | 2 | 1000 pairs | 1000 | 0 |

Immediately after counted work, disable counters and capture tree-owned memory
and active-resize status **before** validation lookups, printing or cleanup.
The original equal pre/post-owned-bytes assertion remains. Admission additionally
requires both immediate endpoints to equal the independently frozen original
baseline bytes: hit/score/miss 14272, long 146656, external 217600, update 14432.
`MEMORY-PROVENANCE.json` records all 324 baseline-label-A seed17 rows from the
saved ARM/Intel native/LTO H2 cohorts, their comparison/metadata hashes, and the
four independently hashed original baseline ELFs. Label A means the baseline
within each pair, not H2 candidate A. These are memory facts only; H2 remains
PARK and supplies no performance acceptance. Exact iteration,
successful scores, negative lookup outputs and final integer scores are then
validated; post-validation memory is reported separately. No validation operation
enters the census. It remains possible for validation to advance a pending rehash;
that is why its later endpoint cannot replace the immediate one.

## Counter meaning and instrumentation scope

Only `zbtIndexTableFind` is instrumented in the generated tree source; all text
outside that function and its added instrumentation include is byte-identical to
baseline. In particular, the leaf helper, index reference finder, rehash code,
filter formula, tags, decoder, comparator, layout and assertions are unchanged.
Every original leaf call executes with the original arguments. Counters describe
logical paths of the instrumented baseline, not retired instructions of its
unmodified compiler output.

Each table call records its ordered query ID, current/destination table identity,
wide-ID flag, table size, active-resize status, result and these counters:

* Bucket visits and visits after the home bucket.
* Approximate mask candidates, true stored-tag candidates, tombstone skips,
  invalid/free-ID skips and migration-owner skips. Original tests and assertions
  remain in their original order.
* Actual leaf calls and their successful/failed returns. `leaf_entries_present`
  sums those leaves' counts; it is **not** a count of tags/bytes actually scanned.
* Distinct validated leaves whose full search failed; eligible repeats of any
  previously failed identity, consecutive repeats among actual leaf calls, and
  repeats whose first failed occurrence was in a different bucket. The cross-
  bucket and consecutive subsets may overlap and must not be added together.
* Home hits, filter evaluation, filter true/false results, and the home post-filter
  fallback entered when the original home filter permits further search. This
  fallback may end in an unused home slot; it is not synonymous with a displaced
  bucket visit. False approximate matches do not count as true tags or leaf calls.

Shadow history resets at **each table call**. It stores only IDs from completed
failed leaf calls after original bounds/free/migration validation. No cross-query,
cross-table or persistent cache exists. A repeated eligible leaf still calls the
original helper; its return must stay negative and the actual requested score/
position output bytes must remain unchanged. Snapshot copying uses object bytes,
not floating-point conversion. Inactive warmup/validation forwards directly to
the original helper without recording. No new leaf call is added for validation
of the shadow prediction itself.

Per-call assertions partition true candidates into skip categories and actual
leaf calls; leaf calls into successes/failures; failed calls into distinct/repeat;
and home outcomes into hit/filter paths. A completed table call has exactly its
reported success count. A separate per-query before/after resize pair surrounds
the complete original operation, exposing a final rehash step that might finish
before the table finder sees an active context.

Capacity limits are 1000 counted queries, 4096 table calls and4096 distinct failed
leaf identities per call. Fixed arrays are diagnostic state outside tree-owned
memory. Exceeding a limit asserts rather than truncating/merging counts. There is
one synchronous query at a time; this is not a concurrent instrumentation API.
The limits exceed this bounded 500-member fixture's requirements, not every
possible production tree size.

## Clock denial and build-only validation

The generated harness has no clock reader, timing mode or elapsed output. Link
wrappers terminate with status 125 before reading time if an explicit clock entry
is reached: clock_gettime/getres, clock, time, gettimeofday, times, getrusage,
timespec_get/getres, their listed internal compatibility names and generic syscall.
All 13 wrapper symbols are explicitly retained, including under LTO. The source
contains no direct cycle-counter instruction or alternate timer implementation.
The contract covers owned linked calls; it is not a claim that an arbitrary
injected library cannot use a private clock implementation.

`build.sh OUTPUT_DIRECTORY native|lto` compiles and inspects only. It never invokes
the resulting ELF. It uses `-O3` or `-O3 -flto=auto`, identical frozen dependencies,
assertions and frame-pointer policy, plus the clock-denial linker arguments.
Output directories are exclusive; failed builds are preserved. The build
environment needs Python3, the selected compiler, nm and objdump. Target compiler
availability has not been tested here.

Local GCC 13.3 native/LTO compile-only builds pass. They are not target GCC 15
qualification or runtime validation. `STATIC-VALIDATION.json` pins their ELFs and
confirms generated-patch reconstruction, exact fixture/setup, counting boundary,
mandatory leaf call and 13 retained clock wrappers with no unresolved clock API.
A separate never-executed static link probe contains an explicit clock_gettime
call; disassembly confirms it targets the denial wrapper and has no unresolved
clock_gettime. `CLOCK-LINK-CHECK.json` records this compile/disassembly check.

Twelve Python-only static/synthetic tests pass; the original eight-test evidence
is retained separately from `revision1-static-tests.stderr`. Negative cases cover omitted cases,
wrong seeds/counts/checksums, elapsed output, changed immediate memory, inconsistent
candidate/leaf/filter/repeat partitions, duplicate/reordered calls, query-state
discontinuity and incorrect totals. Synthetic integers are validator inputs,
not observed path counts. No C diagnostic or clock probe ran locally.

Two preparation failures are retained under `failed-attempts/`: the initial compile
found an ignored checked-write return plus warnings after the diagnostic return
hook obscured literal return values. The hook now records and returns the original
literal through a macro; no original output local was altered. Later LTO symbol
inspection found the unused compatibility wrapper `__clock_gettime64` discarded;
explicit linker retention fixed the denial-symbol check. No diagnostic execution,
source hypothesis selection or measured result preceded either correction.

## Future fleet admission and interpretation

This preparation authorizes no deployment/execution by itself. After independent
review and controller freeze, build separate native/target artifacts on the owned
ARM/Intel fleet only, with live lease, coordinator/timer/isolation checks and exact
compiler/source/referee/ELF identities. Keep each build separate from its later
six-case census action so exact instrumented assembly can be reviewed. The fleet
controller must log successful commands, stderr, output and all hashes; each case
is a one-shot fresh process on the admitted CPU, with counters after warmup only.
There is no clocked pilot, calibration, A/A duration test, perf invocation or
timing comparison in this diagnostic. Never run the ELF on the controller.

Invocation shape on an admitted fleet host is `census hit` (likewise the other
five fixed cases), with stdout/stderr retained separately. Validate the complete
six-file set using `check_output.py`; it rederives checksums, per-query results,
counter partitions, totals, fixed baseline memory endpoints and ordered call
records. It checks consistency of emitted aggregates, not independent
reconstruction of leaf-identity traces: those identities are not emitted.
Admission revision 1 also rejects repeat counts without an earlier distinct
failed leaf, successful filter rejection, an active table without an active
query-entry resize, and a home hit without a bucket visit. It bounds approximate
candidates by eight slots per visited bucket, requires a positive filter before
displaced probing, and validates cross-bucket repeats and migration/free-reference
skips against their necessary path states. Empty tables must report zero work.
A query entering active resize and ending inactive remains valid, including when
rehash finishes before its first table call.

The checker reports whether primary repeat count is nonzero, not whether caching
is worthwhile. Missing cases, malformed output or a failed assertion invalidate
the diagnostic; do not change inputs/counts after seeing results and retry under
the same frozen identity.

**Zero eligible previously-failed repeats in the original primary rules out the
negative-cache lead for that primary fixture.** A nonzero result only proves
possible removable calls; first-candidate-hit overhead, state/spills and other
guards can still make any candidate fail. Do not multiply call counts by sampled
function percentages or static instruction estimates to predict elapsed gain.

The table/filter lead requires actual target fallback traffic **and** supporting
original-target code/evidence. Native counters or speculative hoisted-mask work
cannot establish the target's dynamic arithmetic cost. Source-level filter counts
must be interpreted with the exact uninstrumented target assembly, because adding
side-effect counters can prevent compiler hoisting. No path count alone selects
either mechanism, and no H2 acceptance is borrowed from its PARK evidence.

Coverage is intentionally bounded: original seed 17, 500 members, deterministic
original order, six warm states and query buffers. It adds no favorable seeds,
manufactured collisions, displaced chains, forced resize, large tree, ownership
history or mixed-length workload. Resize flags may all be zero; that would report
the fixture's coverage, not establish a universal absence of resize cost.
Original timing/guard/confirmation thresholds remain unchanged for any separately
selected future candidate.

Public role: census-preparation author. Own tool discovery found no callable
cpu-perf/library-status tool. The controller completed a fresh actual fourth-
population discovery/library_status/ask on these two diagnostic leads, with
3/287 sources and 158 passages and no matched supporting passage. This is shared
consultation, not a call or proof claimed by this author. Backend provenance stays
private; exact token costs are unknown. Baseline and prospective candidate
Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children remain
unavailable here; no TMA collection or pipeline attribution occurred.

## Admission revision history

Independent review of revision 0 found four impossible aggregates accepted by
the parser despite internally consistent totals. The instrumentation itself had
no reported defect. Original parser, tests, protocol, manifests and test results
are preserved under `failed-attempts/revision0-parser-admission/`. The four exact
reviewer mutations are reproduced in `revision1-admission-reproductions.json`: all
pass the archived parser and fail the revised parser. Wrong-but-equal memory is
also reproduced as a fifth former admission gap.

Only parser/tests, memory-provenance evidence, documentation and the directory
freeze changed. Generated source, harness, instrumentation, patch, generator
manifest and previously compiled ELF bytes remain unchanged. The C output schema
therefore remains revision 0; admission/parser revision 1 is a separate identity.
No diagnostic execution occurred before or during this hardening. This revision
is ready for independent re-review, not deployment authorization.
