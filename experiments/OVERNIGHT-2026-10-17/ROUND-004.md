# Overnight round 4 — evidence and handoff

Bounded round:2026-10-17 23:06:20–23:36:20 UTC. This is not the final campaign round.
All active work completed and handoff saved before the final90s. No benchmark/profile
child remains. Main src/zset_btree.c/.h and root HARNESS-001 referee remain byte-identical
to their pins. No source candidate, population, network publication or permission change.
Exact backend/model/token cost unknown; supervisor records actual CLI usage separately.

## Completed work and decisions

| Evidence | Completed result | Decision |
|---|---|---|
| [HARNESS-002](HARNESS-002/README.md) | Independent query RNG/order labels/fingerprints; original tests and80 new fixture cells/build pass release and sanitizers | Locally validated isolated referee revision; uncommitted |
| [AA-003](AA-003/README.md) |96 fixed independent-query A/A rows; all semantics/memory controls pass;0/4 cells qualify | Lookup qualification PARK, source NONE |
| [PROFILE-002](PROFILE-002/README.md) | Two known-function calibrations and12 scoped self-process captures; symbols resolved and all sample/count controls pass | Coarse diagnostic profiles useful; not unbiased time fractions or precision remedy |
| [BOUNDARY-007](BOUNDARY-007/README.md) |36 lexical fixtures,180 model verifications and4075200 seeks/build; both builds pass, two faults detected | Lexical/iterator boundary coverage validated |
| [BOUNDARY-008](BOUNDARY-008/README.md) |18 append-batch fixtures,162 model checks/build; both builds pass, two faults detected | Buffer ownership/flush/resize coverage validated |
| [DIAG-006](DIAG-006/README.md) |48 fixed sampler off/on rows satisfy preregistered coarse perturbation bound; all controls pass | Diagnostic support only; source qualification remains PARK |

Round totals:156 measured tree processes (96 A/A,12 profile captures,48 perturbation),
two separate profile calibrations and one prospectively excluded binary warmup. No
measured rows removed, normal-run failures or timeouts. Two additional boundary suites
and four detected intentional faults. Harness/test smoke times are not performance data.

Campaign totals: **two** locally validated harness revisions, **four** baseline
explorations, **nine** additional measurement/path-count/profile diagnostics and **eight**
boundary suites. **Sixteen** intentional faults detected. Optimisations **0 accepted /
0 rejected /0 parked**; population rounds **0**. Qualification PARK is separate from
optimisation counts. Root source remains baseline until a separate morning review.

## Findings and practical limits

HARNESS-002 decouples queries from construction using a separate seed and a shuffle
starting from identity. Its independent Python oracle reconstructs permutations and
fingerprints, checks partial-pass checksums and query-seed separation, and retains the
original iterator/scan tests. Coupled default remains available. Independent queries
improve fixture coverage but AA-003 does not establish a precision cure; even the nearly
qualifying long-key hit cell remains PARK under the unchanged gate.

PROFILE-002 uses the benchmark's own public ITIMER_PROF/SIGPROF timer and interrupted-PC
context. It never attaches to another process or retries denied sample access. Handler
work is limited to checked lock-free atomics and context reads; symbolication occurs
after timer disable/signal block. Installed SDK manuals/headers inspected first, dSYM
and binary UUIDs match, artifact hashes retained, no out-of-line atomic imports found.
Short-key samples concentrate in memchr, long-key samples in SipHash; rank samples
include both matching and traversal. These are observed sample distributions, not exact
CPU-time fractions, PMU counters or portable rates. Requested timer intervals can round
and coalesce; clock, actual cadence, aliasing and within-window residency are unresolved.

PROFILE-002's thread timer includes post-loop profile output and must not be interpreted
as CPU/wall share. DIAG-006 splits stop/dump to place output after the endpoint, then
uses the same binary off/on to test a coarse preregistered perturbation bound. Passing
that bound does not establish overhead small enough for tight source guards, unbiased
sampling or a source win. Its copied calibrate.c is archival with the old helper call;
consolidate/update that interface before reusing the calibration with DIAG-006's header.
Do not change the frozen snapshots used for these results.

Lexical tests respect the equal-score precondition and iterator invalidation. They cover
empty/binary-prefix/sentinel/forward/reverse/exclusive bounds, optional rank and all8
Next output masks, mutations and cloning. Batch tests overwrite caller buffers before
Finish and exercise count/byte flushes and natural active resize using public mutations;
private fields are read only to establish coverage. Exact signed-zero bits are checked.
No baseline source bug was found; mutation controls establish test sensitivity only.

## Commands, provenance and audits

- Each new harness/diagnostic has prepare.py,freeze.json and a patch. validate.py records
  exact compiler flags and all stdout/stderr/source/binary hashes. HARNESS-002 passes43
  original upstream tests and all3 original referee groups in both builds, plus80 new
  query-fixture cells/build. Release and ASan/UBSan profile/perturbation smoke pass.
- AA-003/run.py and analyse.py preserve96 rows, one explicit warmup, fixed rotating
  six-block ABBA schedule, integer wall clocks and all descriptive intervals. DIAG-006
  likewise preserves48 off/on rows, all sample buffers and fixed-bound computation.
- PROFILE-002/validate.py,run.py,analyse.py and inspect.py preserve calibration,12 capture
  commands, raw hashes, offline atos output, full distributions, SDK/artifact hashes and
  UUID checks. Raw profiles/dSYM remain ignored scratch; public summaries are reproducible.
- BOUNDARY-007/008 run.py and faults.py pass both baseline builds and detect all four
  specific faults. Every patch and expected assertion failure is retained.
- `python3 experiments/OVERNIGHT-2026-10-17/verify-round004.py` passes: root/snapshot/raw
  hashes, all fixed schedules, independently recomputed intervals and decisions,
  sample/symbol conservation, boundary outcomes and faults. This is a separate sequential
  coordinator audit, not independent performance confirmation.
- `python3 scripts/check-workspace.py --pristine-source` and `git diff --check` pass.
  New public evidence scanned for private paths/host patterns; no matches. Final hash
  inventory pins new evidence, oracles and final shared ledgers.
- One curation-script path calculation failed before touching evidence; original script
  and failure are retained in ROUND-004-CURATION-ATTEMPT1.json and ignored scratch.
  The root derivation was corrected, with no permission change or escalation. Full MCP
  retrieval/source excerpts stay in ignored scratch; curated method/audit metadata and
  original hashes are public in ROUND-004-CURATION.json. No measurement rows altered.

Workspace base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c; target pin remains
Redis PR#15635 a7ecd959374d66847c095250bf2d373edf7316c5. New results are explicit
uncommitted isolated snapshots/patches; commit-based acceptance awaits morning review.
Protected-git, external sample and metadata sysctl denials from prior rounds not retried.
No credentials/private hosts/settings, upstream actions or network publishing involved.

One reviewer-agent startup failed before any agent ran: thread-store context load error.
No independent participant, model identity or token cost invented. All reviews were
sequential coordinator passes. CPU MCP ask,methods05/14 and evidence checker consulted;
unrelated retrieved passages were not used as support. No M4 numbers/topology transferred.

A separate [sequential adversarial review](ROUND-004-REVIEW.md) records referee,
measurement,ownership and portability findings. It is not independent confirmation.

## Next concrete action

Do not repeat AA-003 or earlier failed schedules unchanged. The new profiles are usable
for coarse diagnostic planning, while qualification remains the limiting gate. A useful
next preregistered diagnostic can instrument finer fixed contiguous lookup windows with
wall/thread time and opaque CPU boundaries to test a placement/phase association. It
must preserve total operations/checksums and account for extra observation overhead;
boundary observations cannot exclude intervening migration or establish clock speed.
Alternatively investigate a distinct fixture-size/key-length boundary, rather than
increasing repetitions after a failed outcome. Predeclare budget, counts and criterion.

Use HARNESS-002 as the isolated independent-query referee for new work; keep root
HARNESS-001 untouched pending morning review. PROFILE-002 is the calibrated baseline
sampler, with its thread-timer caveat; DIAG-006 demonstrates the corrected dump ordering
and bounded perturbation, with the archival calibration interface caveat above.

Only when meaningful qualified comparisons and matching profiles exist should both
population stages begin: three proposals/chair, then three isolated implementations
and serial measured selection. All correctness/sanitizer/memory guards, fresh independent
confirmation and adversarial review remain mandatory. A capable dedicated runner may
still be needed; no access has been inferred or sought from private configuration.
Final campaign worker must write MORNING-REPORT.md by2026-10-18 07:00UTC/08:00Lisbon.
Supervisor runtime/status/STOP files remain untouched; this intermediate round does not
create the final morning report.
