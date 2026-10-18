# Round 19 — batch-size diagnosis and heterogeneous batch coverage

**Source adoption NONE. EXP-006 remains C/PARK.** EXP-004 A/PARK and EXP-005 PARK/NONE
also remain. No optimization was accepted, rejected anew, or installed in the main
source. All fifteen candidate patches and prior failures remain intact.

This round ends at 06:06:41 UTC; the handoff cutoff is 06:05:11 UTC. Experimental
children finished at 05:50:14 UTC. This is not the campaign's final round. The final
worker still writes MORNING-REPORT.md before 07:00 UTC / 08:00 Europe/Lisbon.

## Completed work and decisions

[PROFILE-005](PROFILE-005/README.md) adds eight scoped single-lane hit captures and
four known-function calibrations. All sampler controls pass. Baseline memchr leads
sample attribution; C removes that attribution and leaf lookup leads. These establish
the transformed path, not unbiased time fractions or a timing explanation.

[DIAG-019](DIAG-019/README.md) tests batch size × bucket-prefetch presence, using
identical all-hit streams at batch sizes 1 and 16. Four isolated control/C × on/off
snapshots pass 332 validation/codegen commands, including the original 43 tests,
exhaustive batch oracle and small fixtures in native and ASan/UBSan builds. Assembly
contains two bucket-prefetch instructions in the on builds and none in the off builds.

All 576 fixed rows complete: 192 A/A, 192 discovery and 192 fresh mirrored confirmation.
Every operation, fixture, checksum, duration and owned-memory invariant passes. None
of the eight A/A cell/seed intervals qualifies. The preregistered attenuation criterion
fails on both discovery and both fresh seeds. **Prefetch-removal remedy unsupported;
causal claim PARK.** The descriptive single-lane concern persists with prefetch removed.
No row was excluded, threshold changed, count extended or original guard substituted.

The caller assembly audit finds control/C zbtreeScores instructions equal except for
five panic source-line immediates per prefetch mode. This is not equality of relocated
machine bytes or code placement. Removing prefetch also changes compilation, so the
intervention cannot establish a pure prefetch-latency cause.

[BOUNDARY-026](BOUNDARY-026/README.md) passes all 32 source/build/seed cells, including
16 fresh confirmations with debug-only assertions disabled. Each exercises 1,345
empty/binary-prefix keys, lengths through 4,096, six independent sorted live models,
342,975 batches and 2,743,800 lanes. Each checks 1,567,343 exact score results, including
signed zeros and finite extremes. All counts 0–16, aliased/copied duplicate lanes,
heterogeneous lengths, score changes, deletion, reinsertion, clone ownership, rank,
both iterator orders, input fingerprints and owned-memory guards pass. Both deliberate
lane0-hash and lane0-length reuse controls are detected. No production bug is claimed.

[COUNTERS-011](COUNTERS-011/README.md) uses the inspected public LLVM reset/dump API.
The scope control exports 0 calls before, 20 inside and 0 after. Sixteen captures pass
expected query/API counts and zero insertion/free counts. Leaf/index/hash logical
function and branch counts match across batch sizes and control/C/prefetch conditions
per seed; C helper branches also match. API calls change as expected. These are scoped
execution counts, not cycles, stalls, cache measurements, hotness or candidate timings.
A post-hoc helper census checks branch-flow conservation and records equal-length
comparisons; it is descriptive, with no new capture or decision rule.

## Evidence and verification

Principal commands, with full arguments and per-child stdout/stderr in the manifests:

```sh
python3 experiments/OVERNIGHT-2026-10-17/PROFILE-005/run.py control
python3 experiments/OVERNIGHT-2026-10-17/PROFILE-005/run.py C
python3 experiments/OVERNIGHT-2026-10-17/DIAG-019/attempt-002/run.py prepare
# Then run.py aa, discovery, confirm; analyse.py after each phase.
python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-026/attempt-002/run.py discovery
python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-026/attempt-002/run.py confirm
python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-026/attempt-002/run.py faults
python3 experiments/OVERNIGHT-2026-10-17/COUNTERS-011/run.py
python3 experiments/OVERNIGHT-2026-10-17/COUNTERS-011/analyse.py
python3 experiments/OVERNIGHT-2026-10-17/verify-round019.py
```

[Audit](ROUND-019-VERIFY.json) passes 7,455 hash checks, 1,051 serial child-command
windows, 60 raw-derived intervals, 1,080 raw branch mappings and 33 patch reconstructions.
All fifteen optimization patches reconstruct exactly. Workspace/pristine-source and
git diff --check pass. The main source/header, root
referee, allocator adapter and original test entry retain their starting hashes.

Two preparation failures remain with their original snapshots: ANSI colour codes
broke an original-test summary classifier despite all 43 tests passing; a new oracle
initially omitted math.h. Corrections change only that classifier/header respectively.
An initial read-only caller audit wrongly assumed a panic call immediately followed
its line-number load; its documented correction permits the intervening x2 message
loads. No measurement was rerun for any of these corrections. A finalizer regex self-match
is also [preserved and corrected](ROUND-019-FINALIZE-ERRATUM.md); it found its own
pattern literals, not a private path in experiment evidence.

CPU MCP ask, benchmark 05/14 methods/code and evidence checker were consulted. The ask
retrieval was not direct M1 evidence and is not attributed as support. No M4 numbering,
frequency or rates were transferred. The checker returned no_number for the qualitative
claim; this is not approval of the methodology. All sampling/counter limitations remain.

## Handoff

Totals: **7 harnesses / 13 baseline explorations / 34 diagnostics / 26 named boundary
suites; 5 sequential populations; 0 accepted / 2 rejected / 3 parked.** The 54 previously
catalogued distinct boundary fault types remain; this round's two lane-reuse controls
are separate pending taxonomy review. The stale SUMMARY top table was reconciled with
round18's recorded totals before adding this round's decisions.

[Sequential review](ROUND-019-REVIEW.md) is complete; reviewer-agent startup failed.
Exact backend/model/token cost are unknown; supervisor records CLI usage separately.
Independent confirmation/review and committed provenance remain pending. Frequency,
effective QoS, migration, portability and the guard mechanism remain unresolved.
No publishing, git metadata retry, credentials, permission changes or supervisor/runtime/
STOP edits occurred. Main baseline stays for separate morning review.

Next: preregister the [retained-candidate cross-boundary matrix](ROUND-019-NEXT-FIXTURE.md)
or obtain qualified performance evidence. The [candidate decision matrix](ROUND-019-CANDIDATE-MATRIX.md)
records superseded decisions so the final report does not revive rejected variants.
Do not rerun DIAG-019 unchanged or substitute correctness for performance gates.
