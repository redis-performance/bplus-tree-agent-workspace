# EXP-008 proposal C — scalar fallback below eight scores

Date: 2026-10-19
Proposer: C (separate proposal pass; no access to other EXP-008 proposals)
Actual backend/model: unknown to this author
Token and currency cost: unknown

## Evidence and hypothesis

EXP-007's fresh confirmation shows B's outlined bulk helper is about 33% faster
for a 96-score, 60-bit range and about 43% faster for 96-score aligned 8- and
64-bit ranges. In contrast, B is 20.8% slower for one 60-bit score, 10.6% slower
for one 63-bit score, and 6.5% slower for seven 63-bit scores. These measurements
use the same materialization and checksum work on both sides. They support a
range-length interaction, but do not establish its cause or predict public
iterator latency.

The saved M1 assembly shows that B's `zbtScoreLeafDecodeRange` is an outlined
call from `decoder_batch`, while the control range helper is inlined. The B
helper contains width dispatch and loop setup before decoding. Its process-wide
sample includes the helper and active decode loop, but includes warm-up and is
not a timed-only cycle profile. Thus call/prologue overhead is a plausible
explanation for short-range losses, not a demonstrated causal mechanism.

**Hypothesis:** at a known range call site, dispatch counts below eight through
the existing scalar score decoder, and counts of eight or more through frozen
EXP-007 B. This will recover the short-range regressions while retaining most
of B's large-range advantage. The threshold is fixed at eight before
measurement; do not search thresholds or move it after seeing results.

## Proposed comparison

Keep the EXP-007 B helper byte-for-byte frozen as the bulk branch. At the same
range call site used by the referee, use the original scalar `zbtScoreLeafScore`
path for counts 1, 2, and 4; call B for counts 8, 16, 32, and 96. Use the
control's scalar loop for the short branch so that it does not call B and does
not allocate a temporary output buffer beyond the common referee contract.
Count zero remains the existing no-op. Do not add a stored threshold, leaf
metadata, public API, or persistent iterator state.

Inspect natural compiler output before timing: establish whether the short
branch is inlined into the caller, whether B remains outlined, and whether the
count test is paid once per range or repeated per score. Do not force `inline`
or `noinline` in only one variant. If the compiler produces an unexpectedly
different structure, retain it and explain the generated code; do not tune flags
or source after observing timing. A small threshold branch in the timed caller
is part of this proposal and must remain included in every candidate measurement.

## Predictions and guards

- At counts 1, 2, and 4, elapsed time should return to within the control's
  qualified noise; width 60 and 63 are the adversarial short-range cases.
- At count 7, run an additional held-out guard even though the fixed count grid
  starts at 8; it should take the scalar branch and avoid B's observed loss.
- At counts 8 and 16, measure the threshold transition directly. A discontinuity
  or regression here can falsify the proposed threshold even if count 96 wins.
- At counts 32 and 96, especially width 60/count 96, retain a material part of
  B's bulk gain. Include aligned widths 8 and 64, crossing widths 59, 61, 62,
  and 63, both physical orientations, and widths 0 and 60 as controls.
- Require exact score bits, output order, and checksums across scalar and bulk
  branches; exercise empty and partial ranges, maximal valid shifts, reversed
  leaves, and guard-page/canary boundaries. No tree-owned bytes should change.

Use identical compiler, flags, allocator, fixtures, source and referee across
control and candidate. Qualify same-binary A/A, then run at least three serial
ABBA blocks and retain every raw process row. Use the planned count grid
2/4/8/16/32/96 and separately preregister count 1/7 guards before running.
Hold out fresh seeds for confirmation. Primary remains width 60, count 96;
the default gate is at least 2% faster there, with no demonstrated regression
above 1% on qualified guards. Do not pool within-process samples as independent
replicates. Report observed paired ranges as ranges, not confidence intervals.

## Falsification and limits

Reject this hypothesis if the short cases still regress beyond the guard after
the scalar branch is selected, if the compiler emits an extra per-score test or
an avoidable call on that branch, or if count 8/16 exposes a material cliff.
Park it if A/A precision is insufficient, the primary gain does not survive
held-out seeds, or any guard is unresolved. A successful result supports only a
private bulk-range helper on the measured host. It does not prove a gain for
the public scalar iterator: that API receives one score at a time and has no
range count to dispatch on. A later iterator integration needs its own design,
referee, profile, and guards.

The current evidence is one unpinned Apple M1 run with unknown frequency/QoS
and no timed-only hardware counters. The focused experiment should first test
the controlled local hypothesis; broader architecture portability and the
original EXP-004 mixed-output iterator guard remain unresolved.
