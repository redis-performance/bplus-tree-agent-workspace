# Round 13 — completion observability and compact-index boundaries

**Source adoption NONE. EXP-004 remains A/PARK; EXP-005 remains PARK/NONE.**
Two new boundary suites pass. Two timing-policy interventions fail their fixed
criteria. A separate observer diagnostic supports a narrowly scoped completion-delay
effect and repeats it on fresh seeds; it does not establish a precision remedy.
Main source, header, root referee, adapter and upstream test entry point are unchanged.

Round began 03:03:25 UTC; deadline 03:33:25 UTC, handoff cutoff 03:31:55 UTC.
All experimental execution has finished; remaining work is read-only audit and curation.
This is not the final campaign round. A later worker still owes MORNING-REPORT.md
before 07:00 UTC / 08:00 Europe/Lisbon.

## Completed work

BOUNDARY-017 passes all eight baseline/EXP-004A/B/C × native/sanitizer cells. Each
checks 1,048,624 ID stores, 4,096 tag stores and 524,288 tag-mask patterns. Complete buffers
match an independent byte reference, including adjacent IDs, tags, filters and canaries.
All legal narrow storage values and selected wide edges are covered. Both new faults
are detected: narrow tombstone misdecoding and a tag store clearing its neighbor.

BOUNDARY-018 passes all eight cells with 38 fixtures each, 1,458,668 registrations and
releases, 81,310 pointer replacements and 602 full registry audits. It checks ID growth,
free-list links across 16-bit boundaries, deferred reuse during rehash, later reuse and
exact usable-size ownership. Both premature-reuse and truncated-link faults are caught.
The initial compile failed on an unavailable allocator API name; the corrected oracle
uses the adapter's existing zmalloc_usable_size. The failed snapshot and logs remain;
no assertions or existing checks were weakened. These are private registry invariants,
not claims that the synthetic registries are valid public trees.

DIAG-016 completes 192 target and 192 predecessor rows plus one warmup. Buffering hash/
JSON work until the end of each ABBA block reduces coordinator CPU as intended, but
both buffered contrasts remain outside equivalence and one buffered placebo fails
precision. The preregistered attenuation criterion is unsupported. No policy adopted.

DIAG-017 completes another 384 rows plus warmup. Local Python source inspection shows
the file-output timeout wait polls with backed-off sleeps; the pipe path uses a
selector. Four transport controls preserve binary output and verify bounded timeout
handling. The pipe contrast narrows descriptively, but one contrast and both placebo
intervals fail precision. The fixed criterion is unsupported. Transport, buffering and
parent wakeup change together; this does not isolate a cause or repair a source guard.

DIAG-018 measures a different quantity: time from a blocked wrapper's waitpid observation
of benchmark completion to Python's return, using CLOCK_MONOTONIC in both. Discovery
and fresh reversed-order confirmation each complete 48 rows plus warmup and satisfy
the preregistered delay criterion on both seeds. Six status/output/timeout controls
pass. The observation includes wrapper teardown and parent scheduling, not exact kernel
exit latency; the extra wrapper changes launch conditions. Benchmark A/A precision
remains mixed. The narrow delay claim is locally supported and repeated, with no
policy adoption or source-guard replacement.

## Commands and evidence

Exact commands, flags, timestamps, source/binary hashes, stdout, stderr and every raw
row are retained in the linked manifests. Benchmark execution is serial. No agent,
build, test or profile computation overlaps measured windows.

- [BOUNDARY-017](BOUNDARY-017/README.md): `run.py` and `faults.py` pass eight cells and
  both sensitivity controls; logical digests match.
- [BOUNDARY-018](BOUNDARY-018/README.md): initial `run.py` compile failure retained;
  `run-attempt002.py` and `faults-attempt002.py` pass all cells and controls.
- [DIAG-016](DIAG-016/README.md): `run.py` / `analyse.py`; criterion unsupported.
- [DIAG-017](DIAG-017/README.md): transport validation, `run.py` / `analyse.py`;
  criterion unsupported.
- [DIAG-018](DIAG-018/README.md): `prepare.py`, `run.py`, `analyse.py`, `confirm.py`
  and `analyse-confirm.py`; narrow observed-delay criterion supported in both stages.
- [Read-only audit](ROUND-013-VERIFY.json): `verify-round013.py` passes 868 serial
  measurement windows, 52 disjoint validation windows and 52 independently recomputed
  intervals. The 98 observer-wrapped windows contain one nested benchmark each;
  wrapper and benchmark are not counted as two independent samples.
- `python3 scripts/check-workspace.py --pristine-source` and `git diff --check`: PASS.
  [Sequential review](ROUND-013-REVIEW.md) records limitations and the next task.

## Decision and handoff

Totals: **six harness revisions, twelve baseline explorations, twenty-six additional
diagnostics, eighteen boundary suites / 36 distinct boundary fault types; four
sequential population rounds; zero accepted, two rejected, two parked optimizations.**
This round adds 864 measured rows plus four warmups, two boundary suites and four fault
types. It adds no harness, baseline or population count. Every fixed schedule completed.

Source base remains a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus explicitly uncommitted
isolated snapshots. Protected git operations were not retried. Losing patches and all
old evidence remain. No publishing, permission changes, private credential inspection,
runtime/STOP edits, detached processes or source adoption occurred.

Independent reviewer startup failed before execution. Fresh confirmation and review
are sequential coordinator passes, not independent agents or machines. Exact backend,
model and token cost are unknown; the supervisor records actual CLI usage separately.
CPU MCP ask and methods and code for benchmarks 05 and 14 were consulted; irrelevant ask passages do not support
local causality. Its checker returned drop_number on the first claim and no_number on
the final qualitative statement. No M4 CPU numbering, frequency or result is transferred.
Frequency, effective QoS, continuous placement and committed provenance remain unresolved.

Next concrete local action: preregister a public-API counterpart to the leaf-ID registry
oracle, forcing leaf retirement and new allocation during an active member resize,
then checking deferred-ID reuse after completion against an independent sorted-vector
model. Require actual coverage evidence rather than assuming the sequence is reachable.
For performance, qualify a separate runner or a distinct method; do not repeat failed
local bookkeeping/transport/placebo protocols unchanged or replace the original guards.
Keep main source at baseline for separate morning review.

[Next-fixture source notes](ROUND-013-NEXT-FIXTURE.md) identify a setup hazard: ordinary
lookup/rank verification advances rehash and can consume the intended coverage window.
The proposed public-API construction remains untested and adds no experiment count.
