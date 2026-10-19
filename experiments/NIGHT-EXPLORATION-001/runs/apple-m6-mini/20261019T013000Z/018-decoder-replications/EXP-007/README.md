# EXP-007 M6 replica — preparation READY

Both canonical builds and all eight canonical decoder test invocations pass:
base/A/B/C, native and ASan/UBSan. Each binary passes four unittest methods,
including its 1820-fixture exact-reference self-test, geometry/sample accounting,
invalid arguments and optional counter availability. These are correctness checks;
their small referee timing fields are not performance observations. No discovery,
confirmation or sampling profile has started. All preparation children stopped.

The isolated checkout is `worktrees/m6-replica-exp007`, at harness commit
`e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf`. Canonical build.py creates only its
own nested `worktrees/exp007-{base,A,B,C}` at source commit
`4fd3a3fdbce5acca18ee292642a3d80a79f50362`. The original production C hash is
`d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`.
The adapter is the original legacy campaign adapter, matching the historical M1
experiment; this is not the current corrected-adapter tree baseline. The legacy
compat/server.h hash is
`79b3c9cfa8aec6e003dcf10e6d1c3af71799e357db7d0a0526dca0fd575af0be`.

Apple clang 21.0.0, target arm64-apple-darwin27.0.0, built the canonical native
flags: C11, O3, g, Wall/Wextra/Werror, frame pointers, no LTO, identical include
paths and the canonical file-prefix map. Sanitizers use O1, address+undefined,
and no sanitizer recovery. Full compiler text, exact commands/flags, shared object,
helper, combined source, kernel object and binary hashes are retained in the two
public build manifests and freeze.json. Hashing/allocator/assertion policies and
all original source/referee files are unchanged.

Canonical patch regeneration produces byte-identical A/B/C candidate.patch files.
Before/after hashes are recorded; original copies are retained privately. The
worktree has no tracked edits after preparation. Native assembly retains decode
control flow and output stores before checksum consumption. B calls its retained
bulk helper; base/A/C materialize in decoder_batch. Assembly hashes and exact
store/function regions are in assembly-inspection.json; no instruction cost or
speed is inferred from them.

## Exact future phases — NOT LAUNCHED

Run from the isolated checkout only, after root review/publication/exclusive ACK.
The output directory must be new. All other builds/tests/profiles must be stopped.

```
python3 experiments/EXP-007/run.py --out build/m6-replications/EXP007/discovery --budget-seconds 300
python3 experiments/EXP-007/analyse.py build/m6-replications/EXP007/discovery
python3 experiments/EXP-007/audit.py build/m6-replications/EXP007/discovery --kind discovery
```

**Discovery is 2880 processes**, not 4320: 30 cells × 6 blocks ×ABBA × 4 phases
(same-binary A/A, base/A, base/B, base/C). It retains 371520 measured batches.
The 4320 figure includes a separate 1440-process fresh confirmation if the original
diagnostic shortlist rule selects a candidate. Each process has 129 samples,
16 warmup batches, eight leaves, shift 0 and rounds=ceil(49152/(count×8)).
Discovery seeds alternate 81031/81041, cells rotate by block, phases stay fixed.
The primary is width 60/forward/count 96; the other original cells remain guards.
Nothing is retuned to hit the budget.

The canonical 300 second budget is campaign-loop wall time, including subprocesses
and validation. Each benchmark child timeout is min(30 seconds, remaining budget).
Timeout stdout/stderr and partial manifests/summaries are retained, without retry.
Metadata before the loop and final serialization occur outside that internal
budget. Root needs an external absolute cutoff/owned-child cleanup supervisor to
enforce 07:15 UTC across phases; this preparation does not change the canonical
runner or silently claim its internal limit bounds every setup/finalization step.
The runner validates fixture/checksum/operations/accounting equality across roles
and binary hashes before/after. It records OS/architecture, generic CPU description,
endpoint observations and unknown frequency/residency. No KPC/privilege workaround
is part of these phase commands.

analyse.py retains process minima/medians/p90/max, six paired block effects and
observed ranges, creates histograms and selection-input.json; it makes no source
acceptance decision. audit.py independently reconstructs raw CSV statistics,
geometry, checksums, serial windows, schedule/counts and hashes; its output is
evidence reconstruction, not independent experimental confirmation.

Keep the original diagnostic shortlist rule: semantically valid candidates with
primary median change≤−2%; prefer fewest guard median regressions>1%, then best
primary, with ties within one percentage point favoring the smaller patch.
The shortlist is not acceptance. If eligible, run exactly one confirmation for
that selected original variant, replacing X below by A/B/C without other changes:

```
python3 experiments/EXP-007/run.py --out build/m6-replications/EXP007/confirmation --confirmation X --budget-seconds 180
python3 experiments/EXP-007/analyse.py build/m6-replications/EXP007/confirmation
python3 experiments/EXP-007/audit.py build/m6-replications/EXP007/confirmation --kind confirmation
```

Confirmation uses the unchanged 30 cells, six blocks, 129 samples and fresh
alternating seeds 82037/82051, with fresh same-binary A/A preceding the selected
candidate. It has 1440 processes/185760 batches. If none meets the original
shortlist rule, skip confirmation and select NONE. Acceptance still requires
all six same-cell A/A median effects within±1%, ≥2% primary gain, no demonstrated
>1% guard/memory regression, explained profiling, independent confirmation and
review. Unqualified effects remain conditional/PARK. No row drops or M1/M6 pooling.

The canonical runbook's separate profiling commands are:

```
python3 experiments/EXP-007/profile.py base --out-dir build/m6-replications/EXP007/profiles
python3 experiments/EXP-007/profile.py B --out-dir build/m6-replications/EXP007/profiles
```

profile.py does not build. It runs the actual native binary, width 60/count 96,
eight leaves, rounds 65536, 64 samples, 16 warmups, seed 81031. It launches a 1 second
sample at 1 ms interval; sampler timeout 10 seconds, then child wait timeout 20 seconds.
On failure it kills/reaps its owned benchmark child. These are whole-process
profiles including warmup, and their timing CSVs are excluded from comparisons.
No profiler runs concurrently with timing. Profile output can contain platform,
process and local-path metadata: raw output stays private until root publishes a
generic summary/hashes. This preparation does not run these commands or infer
supported hardware counters from historical CPU sampling availability.

## Evidence and scope

preparation.json records 10 successful bounded commands and their public/private
log hashes. prepare.py enforces an 8 minute preparation budget, build child limits
180seconds and per-test invocation limits 90 seconds; canonical tests themselves
limit each referee child to 60 seconds. Raw logs remain in ignored
scratch/m6-exp007-replication-prep; public logs use generic paths. The wrapper was
run once. No failure, production source edit or canonical referee/script edit occurred.
Only the canonical build generated the authorized nested combined source files.

This replicates a private packed-score bulk decoder experiment. It cannot clear
the original mixed-output iterator guard, integrate a scalar API, qualify the
corrected adapter, or establish a tree optimization. Existing unique patch/harness
and optimization-population counts remain unchanged. Participant
/root/followup_proposal_b, inherited Codex/GPT-6 family; exact serving model,
token usage and cost unknown.
