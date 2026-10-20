# Advancing the parked work

**Start with Intel iterator-cache B qualification. Source selection remains NONE.**
This is a ranked review of retained evidence, not a new performance result or a runner launch.

| Priority | Work | Why revisit | Concrete next gate |
|---|---|---|---|
| 1 | Intel iterator-cache B | Public iterator; B keeps the observed 16-byte state. Historical full-output leads and matched code support warrant investigation. | Qualify the corrected-source baseline, including fractional and score-only guards, on a dedicated Intel runner. Then consider exact B, without completing the old partial schedule. |
| 2 | AMD scan A mechanism | Instructions fell ~12%, but cycles fell <1%, inconsistent with the unqualified 4–5% elapsed observation. | Validate profiling against the actual timing binary and qualify 1M controls before another comparison. The corrected B replication remains rejected. |
| 3 | M1 EXP-004 predicate | Earlier primary and some guards passed; score-plus-length and compact guards remain unresolved. | Qualify those exact adverse guards first. The focused decoder slowdown prevents a general decoder claim. |
| 4 | M1 EXP-006 inline search | Fresh primary lead; one long-key guard interval and single-lane behavior remain problematic. | Long-key and single-lane guard diagnosis first; no favorable subset substitution. |
| 5 | Bulk decoder family | Large private full-leaf observations, but real short-range losses and short windows. | A separately validated duration-correct referee and a demonstrated public consumer opportunity. Broad cutoffs and count-one policies have already been tried. |
| Hold | M6/M1 lookup precision | M6 still fails 1M controls with ~600ms windows; thread contrasts track wall variation. | A falsifiable measurement diagnostic, with actual placement/frequency observations where available. Longer runs or switching to thread time alone are not a solution. |
| Hold | Mask / rejected scan / NEON | Rejected replications and failed fresh gates are adverse evidence, not paperwork. | A distinct, profile-supported mechanism is needed. Do not revive an unchanged rejected patch. |

Ranking is our inference from the archived evidence. It does not estimate expected speedup.
All **17 parked records** are mapped to explicit next actions in [backlog.json](backlog.json).

## First actionable package: Intel iterator B

[Draft preflight](intel-iterator-preflight.json) defines eight baseline cells and 192 A/A
runs, with no candidate timing. The unchanged B patch applies cleanly to current source
(`git apply --check`); that is applicability, not a correctness result. Its reset sites
cover starts/seeks and leaf transitions; replay the original fault/oracle checks before
any timing. The original invalid-oracle attempt, noisy controls, two trailing rows and
ten missing screen rows stay intact.

The next campaign must provide a dedicated Intel runner and a documented new
measurement condition; simply granting more time to the old run is insufficient.
Rebuild against the corrected adapter, preserve the original frontend semantics,
freeze exact compiler/flags/source/binary/fixture identities, inspect current generated
code, and validate a fresh baseline profile. No old control crosses this identity boundary.
The draft is not launch-ready until ownership, environment, counts, hashes and review are sealed.

Only after **all eight baseline cells qualify** can a separate reviewed exact-B
comparison proceed. Acceptance still needs the complete guard matrix, iterator-state
and tree-memory checks, a matched candidate profile, held-out confirmation and
independent adversarial review. Guard coverage includes all output masks, reverse,
small trees, long/binary members, ties/signed zero, starts/seeks, leaf transitions,
range-delete callers and mutation followed by explicit iterator reinitialization.
A remains a separate 24-byte-state trade-off; C is rejected. B is a diagnostic priority,
not an implementation winner. Any new source hypothesis must use both population stages.

## Evidence and limits

- [Intel screen and missing gates](../NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator/README.md), [matched profile](../NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator/MATCHED-PROFILE.md): 75/369 in-range samples at a dependent prefix-load/comparison bucket do **not** assign 20% of total runtime to that instruction. PMU evidence was unavailable.
- [AMD profile discrepancy](../NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/008-scan-tags/mechanism/RESULT.md): instrumentation changes binary layout. Fewer instructions alone do not establish the elapsed gain.
- [Bulk losses](../EXP-007/RESULTS.md), [failed broad cutoffs](../EXP-008/RESULTS.md), [later M6 decoder work](../NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/MORNING-REPORT.md): no public scalar-iterator gain is established.
- [M6 clock brackets](../M6-CLOCK-BRACKET-001/RESULTS.md): nominal resolution and edge margins do not bound accounting accuracy. The existing failed schedules remain frozen.

The required CPU-perf `library_status`, `ask` and `read_source` calls are recorded in
[CONSULTATION.json](CONSULTATION.json). Retrieval supplied no supporting source passages;
we used archived primary experiment reports and checked external primary methodology.
[LLVM](https://llvm.org/docs/Benchmarking.html) distinguishes low noise from absence of
bias and discusses isolation/frequency/layout controls.
[Google Benchmark](https://google.github.io/benchmark/user_guide.html) documents duration,
repetitions and interleaving. These support protocol design, not a diagnosis of our machines;
no system settings were changed and no benchmark package was substituted.

[Three sequential review passes and decision](REVIEW.md) · [Offline validation](VALIDATION.json).
