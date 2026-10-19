# M6-LOOKUP-CALLER-001 results

**REJECT dual primary / source NONE.** Three actual independent proposals and three
isolated implementations are complete. Exposing the generic leaf-search call boundary
does not clear the declared100K and1M public successful-score-lookup speed gates.
The main tree source remains exact baseline; all three losing patches are retained.

| Variant | 100K median (six-block range) | 1M median (six-block range) | Decision |
|---|---:|---:|---|
| A | -2.712% (-3.127..-2.378) | -1.762% (-4.645..-0.213) | REJECT |
| B | -2.024% (-2.710..-0.972) | -0.596% (-2.216..+1.142) | REJECT |
| C | -1.827% (-2.957..-1.100) | -0.833% (-2.950..+1.806) | REJECT |

Effects are percentage changes in elapsed time; negative is faster. The ranges are
observed block extrema, not confidence intervals. A clears every100K block by2%;
its1M blocks do not. B and C also fail the two-primary every-block gate. A's100K
result is a scoped exploratory lead only. No post-hoc primary or guard removal.

## Qualification and schedule

The common new referee suite contains101 unique cases:40 standard operations,
30 independent hit/miss/mixed lookups including binary member-length boundaries,
six public batch cases and25 reversible update-pattern cases. Original source/referees
are unchanged. Short insert/delete windows prepare independent trees outside timing,
with4096-replica/64MiB replicated-owned-memory limits and full per-tree checks.

Baseline calibration:303 observations,101 fixed counts targeting100ms;100-member
delete reached4096 replicas. Full A/A:2424 rows, six ABBA blocks on seeds1/2/3 twice,
250.562s timed / 545.474s wall.39/101 cases qualify;62 exceed1% in
at least one block, zero have windows below10ms. The100K primary qualifies(max0.808%);
the1M primary fails(max1.252%). No rows dropped or completed schedule repeated.

All three primary screens rotate by block on the same fixed counts:144 serial
processes, 14.515s timed / 55.859s shared wall. Owned tree memory is identical
in every compared primary row. No contender is eligible for the full candidate101-case
guard screen, fresh confirmation, candidate profiling or adoption; those were not run.
The101-case qualification is baseline-only and must not be presented as candidate guard
coverage. Failed controls independently block acceptance.

## Correctness, mechanism and review

Each implementation passes all43 original tests native and ASan/UBSan, frozen public
lookup smoke checks, and4160 private physical-score oracle cells/515840 exact outputs
per build. C also tests its added read-only helper against the full oracle.
The common32 native/sanitizer binaries pass312 frontend checks, including replicated
mutations. Separate referee validation retains invalid-input and injected-fault evidence.

A forces inlining on the generic helper; B exposes a shared inline body behind a
noinline generic wrapper; C adds a read-only helper while preserving the original
generic helper. Original decoding, memchr/memcmp, hashing and layout stay unchanged.
All three normalized read-only lookup instruction streams coincide. Caller frame
grows176→240 bytes while the separate144-byte helper call disappears; instructions
grow345→601. A also expands rank/mutation functions. Matching frontend paths and
source-file prefix maps were used for every comparative binary. Timing differences
do not establish three distinct read-only instruction mechanisms.

C cross-reviews A/B; root independently reviews C. The independent arithmetic/raw audit passes all2871 CSV rows and66 frozen artifacts.
See [audit](INDEPENDENT-AUDIT.md). This is not independent timing confirmation.
Backend: inherited Codex/GPT-6 family; exact serving identifier, agent token usage and
monetary costs are unknown. Both populations used actual agents, unlike the four core
M6 comparisons' sequential fallback.

## Evidence and publication

- [Preregistration](PLAN.json), [population](population.json), [chair](selection.md).
- [Frozen harness/build identity](freeze.json), [calibration](calibration.json), [A/A](aa.json).
- [A](screen-A.json), [B](screen-B.json), [C](screen-C.json); all raw CSVs in `raw/`.
- [Cross-author review](REVIEW-CALLER.md), [root review of C](OPERATOR-REVIEW-C.md).
- Candidate patches and validation are in `variants/A`, `variants/B`, `variants/C`.
- Git froze harness9d94c41fc, counts6e221106f and completed controls016f45136
  before their dependent phases.

The coordinator refused build metadata containing a local path before public release.
The path was substituted in public metadata and future records before freeze; binaries
and measured data were unchanged. [Incident](PUBLICATION-HYGIENE.json). Reporting
worker rounds ended via the existing ownership barrier; root drove all comparisons,
with no agent/build/test/profile/publication overlap. No permission/supervisor/prompt/
STOP/deadline change.

Branch totals:12 completed populations(9 sequential+3 actual multi-agent),
0 accepted/7 rejected/5 parked,36 retained optimization patches/15 validated harnesses.
Concurrent M1 night counts remain separate.
