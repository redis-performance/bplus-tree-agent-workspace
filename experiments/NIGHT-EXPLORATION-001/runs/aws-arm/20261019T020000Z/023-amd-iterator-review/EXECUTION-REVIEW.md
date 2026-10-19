# Independent execution review of AMD iterator baseline diagnosis

**No blocker found for the fixed baseline profile diagnosis.** Reviewed immutable
234f70f44/execution-freeze.json SHA8ed212a37674c07c944fdb1ff88f3c394517a8fe9751ff2324498f67ff1628fc.
Root must grant execution; this review neither launches a job nor selects an optimization.
A/A remains a separate phase after independent completeness/control review. Prior
plan-only review c4fc85d7f remains unchanged.

Verified all21 frozen file hashes, Python syntax, the complete48-row same-binary ABBA
schedule and six-cell profile schedule against independently constructed expectations.
Inspected all driver/audit/helper/mapping/wrapper sources and the51-command manifest.
Six enabled tree capture argv/env contracts match the fixed50M/16byte/size/seed matrix.
Exact commands are checked before each subprocess and reconstructed by the final audit.

## Controls and failure behavior

Both wrappers clear inherited PROFILE_DISABLE/BPLUS_PERF_CTL/BPLUS_PERF_ACK. Enabled
capture environments explicitly remove PROFILE_DISABLE, disabled modes explicitly set1.
Every PMU workload starts disabled with-D-1 and uses acknowledged control/ack FIFOs.
The known-work positive/negative tests precede scientific captures. Disabled counters
must be0/not-counted; enabled cycles/instructions/branches must parse as positive values,
branch-misses nonnegative. Missing/not-counted positive values fail rather than becoming
zero. Known checksums are compared exactly in all modes.

known_gate classifies the sampled physical same-IP symbol, not ancestor frames. It
requires>=20 known_work events and strictly>80% of all sampled period, with zero sampled
outside_work events. Unknown/control events stay in that denominator. Independent
synthetic checks passed a valid20-event case and rejected19 events, the exact80% boundary,
and one outside_work sample. A separate unknown sampled-IP/known_work ancestor test
confirmed the ancestor receives no exclusive charge. These supplement AMD's frozen
local tests and do not execute the known100M kernel.

CPU affinity must be exactly[2]; children inherit it. The profile has600s remaining-time
budget/120s child cap, with the outer owned helper as the hard boundary. A/A separately
uses300s/30s. Records retain argv/cwd/profile environment, start/end/exit and stdout/stderr;
timeouts retain available partial streams and fail. No retry or limit change path exists.
New source/profile/aa directories must not already exist, preventing silent reuse.

## Semantics and identity

Original and disabled frontend controls preserve the benchmark's own visited/checksum
assertions; runtime checks require equal native rows and CPU2 before captures. The final
profile audit additionally reconstructs the literal50M expected operation/traversal/
checksum/warmup contract, all input fields and owned-memory equality across original,
disabled and sampled outputs. The sanitizer1K/2001 case retains3000-visit rounding.
Original43 tests run unchanged. The plan's50M checksums and independent known-work
oracle were verified in the preceding plan review.

The isolated source archive is exact13e; every target/referee hash is checked before
and after. Build hashes are written before controls, checked afterward, and separate
from the actual015 executable. Existing015/017/019 binaries are protected before/after.
Actual A/A uses1ecbe6a4 from015, checks its source and binary before/after, and records
profile audit/mapping/freeze hashes. It refuses absent/failed audit or absent mapping.
Root's explicit phase grant remains necessary beyond those file-status checks.

## Attribution and practical limits

Full source-linked original/diagnostic/actual015 assembly is retained. map-code uses
physical function+offset only to locate candidates, then compares exact encoded bytes
and records source lines, addresses, matching/different/missing events and period.
Relocation/body differences are not normalized away. Unknown/library/control events
remain in full denominators; known-work data is excluded from tree summaries.
Per-capture perf report periods are reconciled with raw sample periods, loss counts are
retained, and raw.data hashes are checked when files are available. Public results must
state when raw binary data remains remote. Same-IP inline-inclusive labels may overlap;
only the exclusive innermost sampled label is used for summed attribution.

Two limits deserve explicit retention, without blocking this baseline diagnosis:

- Per-instruction encoded-byte equality at a function offset is not proof of complete
  function/control-flow/register-context equivalence. Any future proposed hotspot must
  inspect the actual source-linked region/body, including differences and mapping gaps.
- Runtime pre-capture tree controls check original/disabled parity plus the unchanged
  referee's assertions. The explicit50M arithmetic/input contract is enforced by the
  final profile audit, rather than a duplicate literal contract in each pre-capture row
  check. No downstream hypothesis or A/A may proceed before that audit passes.

Zero reported losses and a passed known-work control do not prove perfect sampling or
that a hot operation is removable. No speed claim follows from instrumented elapsed
values, aggregate iterator shares, or a baseline-only A/A. All required independent
reviews and the population process remain gates before any candidate work.

Actual independent reviewer/root/aws_arm; no AMD source/control authorship, no runner
access or compilation/benchmark execution. Native Codex; exact model/tokens/cost unknown.
