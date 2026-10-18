# Round4 sequential adversarial review

This is a separate coordinator pass over the completed artifacts, not an independent
agent review, population proposal, confirmation or source-acceptance decision.
Reviewer startup failed before execution; backend/model/token cost unknown.

## Referee semantics and test strength

HARNESS-002's independent permutation starts from identity with its own RNG, so changing
construction seed does not change the query array. Coupled mode copies the original
permutation and ignores the query seed operationally, although the requested seed is
reported. Insert remains construction-ordered; read/update/delete/warmup use queries.
Update verification uses query positions, including the partial final pass. Python oracle
reimplements RNG/permutation/fingerprint and partial sums; original three referee groups
and43 embedded tests pass both builds. All cases allocate the extra query array, so this
is a separate referee revision that invalidates prior qualification, not a source change.
The extra fixture bytes are not included in tree-owned memory; no net memory win claimed.

Checksums are aggregates, not proof of every timed lookup's output. Existing original
tests and added direct-API boundary oracles provide separate exact checks. Future source
variants must still pass that entire referee; performance checksum success alone cannot
establish semantic equivalence. No existing assertions/checks were weakened.

Lexical expected results use sorted binary bytes and a linear bound oracle, not tree
search helpers. Only equal numerical scores are supplied; signed-zero bits retained.
Sentinel pointers are distinguished from actual empty/+/− members. Successful seek is
checked before advancing through nearby results; failed seek is checked for exhaustion.
Mutation paths reacquire iterators, so tests never rely on invalidated pointers.

Batch test inputs sort strictly by binary member under equal numerical scores. Exact
precomputed hashes use the same frozen seed. Caller buffers are overwritten after Add
and before Finish, detecting borrowed inline/external lifetime errors. Read-only private
observations prove count/byte flush and natural active-resize coverage. Incomplete batches
are not otherwise queried/mutated. Both semantic mutation controls fail specific oracle
assertions; an arbitrary process crash was not treated as sufficient evidence.

## Measurement validity

AA-003 is same-executable A/A with its own fresh frozen referee/seed. All96 rows and the
prospectively separated warmup remain. The six-block descriptive t interval is unchanged,
including the nearly qualifying cell; all four cells PARK. This is not a blanket claim
that independent queries are ineffective, only that this trial did not meet its gate.
Normality/independence are assumptions, and wall/thread/CPU-boundary data do not prove
stable clock or whole-window placement. No post-hoc outlier removal or optional stopping.

PROFILE-002 is a baseline instrument, not an eligible timing binary. User-space PCs
arrive via process CPU timer signals. Signal coalescing/rounding, periodic aliasing,
interrupted-PC attribution bias and code layout affect observed distributions. All
calibration PCs resolved to the known loop; this tests the capture/symbolication path,
not unbiased weighting. Twelve fixed captures meet the sample threshold without extension.
Library names from dladdr are coarser than executable dSYM locations. No PMU/frequency,
continuous migration or kernel-time attribution is available. Matching dSYM UUID/hash
checks and the absence of out-of-line atomic imports support correct reconstruction.

PROFILE-002's output contaminates its thread interval; that field is explicitly unusable
for CPU/wall analysis. DIAG-006 moves dumping after the endpoint. Its fixed off/on bound
is a diagnostic selected before outcomes, not a relaxation of source2%/1% gates. Coarse
bounded perturbation cannot establish sub-percent overhead or unbiased sample fractions.
Off/on environment values and ASLR may still change process placement; no address-layout
identity is claimed despite executable identity. No timing from sampler captures enters
AA-003. Warmup and fixture work are outside sampled loops except tiny boundary helpers.

## Portability, ownership and maintainability

Sampler is explicitly macOS arm64 diagnostic code using inspected SDK fields; do not
merge it as a cross-platform referee. Lock-free atomics are checked before handlers
start; handler contains no allocation,symbolication or I/O. Timer/handler lifecycle is
owned by a standalone single-thread process, not a reusable embedded application.
No external process attachment or denied permission path is retried. Actual frequency,
effective QoS and within-window residency remain unknown. No M4 constants transferred.

DIAG-006's copied calibrate.c still calls the old stop helper and is not built by that
diagnostic. This is a known prototype maintenance issue, not hidden validation success.
Before reusing its helper, update the calibration call or consolidate a shared interface
in a new snapshot and validate it. Preserve existing measurement snapshots unchanged.

Uncommitted source+patch/hash provenance is explicit. All candidates remain baseline;
intentional fault patches are test controls. No independent reviewer or confirmation
was available, so source acceptance remains impossible even if timing later improves.
Required two population stages were not silently bypassed: none was started or accepted.

## Review outcome

Local harness/boundary validation and diagnostic findings are supported within their
stated scope. Source selection NONE and lookup qualification PARK remain appropriate.
No source optimisation, portable speedup or independent acceptance is established.
Next work needs a distinct preregistered diagnostic or a qualified controlled runner;
repeating these failed schedules unchanged would add little evidence.
