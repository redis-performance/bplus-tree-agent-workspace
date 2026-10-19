# Corrected ARM iterator baseline diagnosis and controls — awaiting root review

No runner work or measurements are authorized by this plan alone. No candidate is
selected, implemented or timed. Root requested a distinct baseline-only diagnosis.
Exact corrected source13e459ff8800be3f02b6b45c87dd7b0c39453fa9 and actual existing013
baseline timing binary330b39a991573985c421194cfe83f21b44797e1a83372f623120672eb910b3bc
remain unchanged. expected.json pins source/referee/compiler inputs and protected
existing binaries. Use the same Clang18.1.3, native-O3, assertions, hashing and allocator.
No original checkout HEAD change, rebuilt A/A binary or old/new performance pooling.

## Fixed workload contract

Public bench/microbench.c iterate, forward, score-only output: calls
zbtreeIteratorNext(&it,0,NULL,NULL,&score), consumes each score into checksum, checks
visited==n after every traversal. Fix **50,000,000 requested operations** now for both
100K and1M,16-byte members. This is exactly500 and50 complete traversals, respectively,
with50M actual visited members, one original lookup warmup pass and original fixture
construction. Seeds1/2/3 profile; held-out A/A seeds701/702/703 twice. No calibration,
operation count change, row dropping or retry after observing data.

At50M operations the known iterate checksum is traversals*n*(n−1)/2, independent of
seed, and original owned memory must match each diagnostic fixture. Exact finite
integer scores are used by this original referee. These observations do not imply
reverse, member/length output, fractions/ties/signedzero or mutation coverage.

Source inspection shows the current public iterator skips zbtScoreLeafElement when
ele/len areNULL, then decodes the packed score, updates position and crosses leaves.
Intel004's prior lazy member-offset cache targeted full-output materialization; it
is not automatically relevant to this score-only case. Old Intel/ARM conditional
iterator leads, failed precision/incomplete schedules and original8fab decisions
remain final. Fresh ARM/corrected identity is neither rescue nor replication evidence.

## Profile phase: one600-second owned serialCPU2 job

Use a new isolated archive/source/build/output at
scratch/arm-corrected-iterator-13e459ff8. The existing013 timing binary stays outside
that path and is only read/disassembled/hash-checked. Archive exact13e inputs, use
relative frontend paths, keep native/sanitizer flags identical to the corrected013 baseline.
Build original and diagnostic native/sanitizer frontends separately plus the standalone
known-work control. Preserve original43-test suite unchanged; run once natively.
All children have a120-second cap and remaining whole-job budget. Partial failures
are retained; no rerun or extension.

Reuse byte-identical validated profile-scoped-fifo2.c SHA86ef544dd7612f35bf9853ad3eb1d871ccd3c0868941e3952aaaa40d04b94dfe.
FIFO enable precedes the original start clock; disable follows the original end clock.
Construction, lookup warmup, postvalidation and destruction remain outside the intended
PMU window; FIFO acknowledgements and clock edges remain included. Clear inherited
PROFILE_DISABLE for enabled jobs; use fresh control/ack FIFOs and existing perf tool.
No PMU permissions/settings change.

Controls before scientific samples:

- Six native original/PROFILE_DISABLE pairs in fixed seed1/2/3,100K then1M order,
  all50M iterate operations. Require original case/size/ops/bytes/seed,50M actual
  operations, expected checksum, tree bytes, traversals, warmup and CPU2 parity.
- One original/disabled ASan+UBSan pair at1K/2001 requestedops/seed101, preserving
  the unchanged rounded3K-item traversal/checksum semantics and allocator per mode.
- One disabled perf-stat iterate control at100K/50M/seed1: cycles:u,instructions:u,
  branches:u,branch-misses:u all0 or not-counted, with exact native semantic parity.
- A separate deterministic known-work control validates transport/scoping: fixed100M
  dependent unsigned64-bit steps inside known_work, bracketed by distinct outside_work
  before enable and after disable. Run once disabled without perf, once disabled with
  four-counter perf-stat, once enabled with four-counter perf-stat, and one enabled
  cycles:u997Hz/frame-pointer sample. All modes must emit exact independently computed
  checksums. Disabled counters must be0/not-counted; enabled cycles/instructions/
  branches positive and branch-misses nonnegative. At least20 samples must occur in
  known_work and its sampled-period share must exceed80%; outside_work must have zero
  sampled events. Retain all other samples/period in this control's denominator. A
  failure halts this profile as inconclusive, without tuning/retry. This known kernel
  is a separate diagnostic, never part of tree timings or attribution denominators.

After controls, exactly six scoped cycles:u997Hz/frame-pointer captures in the frozen
profile-schedule.json order, each50M iterate operations. No enabled tree perf-stat
captures or additional sample repeats. Sampled CSV outputs must equal the corresponding
original/disabled controls. Retain raw perf.data locally with hashes and full sample
text/reports publicly; include loss counts, unknown/system/control events and period
sums. No instrumented elapsed speed claim.

Disassemble separately built original, diagnostic and the actual unchanged013 timing
binary with source lines. Map sampled physical IPs/function offsets to all three by
exact instruction bytes; explicitly report layout/body/relocation differences, never
assume identical code because source matches. Report exclusive innermost same-IP
source attribution; overlapping inline labels separately, not summed. Distinguish
zbtreeIteratorNext, packed score decode, iterator advance/leaf transition and harness
consumer only where exact code/source attribution permits. Ancestor frames receive
no cumulative charge. Unknown/unmapped samples stay in totals. No aggregate hot share
alone establishes a safe optimization or enough removable work to meet the speed gate.

Freeze actual build/source/referee/compiler/diagnostic hashes before samples and verify
after; protect existing013/015/017 binaries before/after. New builds are diagnostic
only and never replace the actual013 A/A executable. Estimated cost is bounded by600s,
not justified by adaptive trials. Any failure ends this phase and no A/A launches until
its independent completeness/control audit passes.

## A/A phase: separate300-second owned serialCPU2 job

Only after a completed/validated profile phase, run the actual unchanged013 baseline
binary for48 processes/12 blocks according to aa-schedule.json: six same-binaryABBA
blocks per size, seeds701/702/703 twice; size order reverses on odd blocks.50Mops,
16-byte members, original warmup, no candidate. Each child cap30s and remaining phase
budget. Source/referee/binary hashes before and after, exact commands/CPU endpoints,
start/end/exit codes and every raw row preserved.

All six blocks at BOTH sizes must have absolute paired effect<=1% and every measured
window>=10ms. Effect=100*((middle sum elapsed_ns/operations)/(outer sum)−1). Require
50M actual operations, exact checksum and tree-owned bytes, traversal and warmup parity.
Any failed control meansNONE/PARK for subsequent candidate work; no count increase,
retry, new seed substitution or reduced matrix. Complete the fixed matrix unless the
hard resource cap or semantic/process failure stops it. No candidate follows without
profile evidence, actual independent proposals/chair and a separately frozen campaign.

## Provenance and stopping

Plan, fixed schedules, expected source/binary hashes, reused scope and known-control
source must be sealed before runner execution; execution drivers must also be sealed
before data. This publication contains preparation only. Root review precedes launch.
No target source edits/adoption. Stop new experiments07:15UTC and release08:00UTC.
Actual author/root worker ARM; native inherited Codex, exact model/tokens/USD unknown.

## ARM-specific context and compatibility

This separate score-only diagnosis is useful because original corrected013 iterator
windows at1M requested operations were all below10ms.100K had minimum3.332161ms and
max A/A1.1723049%;1M minimum3.755492ms and max0.7652236%. All five sizes were short.
The exact prior table is retained in prior-baseline-context.json.50M operations is
fixed now by the requested cross-host diagnostic contract, without calibration,
priming, data-driven duration tuning or any claim that longer windows cure noise.
This is distinct from005's old8fab full-member iterator replication and from AMD029;
those decisions remain final, and no timing or qualification transfers here.

Actual013 A/A binary lives under scratch/adapter-worktree-13e459ff8 and remains
immutable. Fresh source/diagnostic paths are separate. The known-work C kernel is
portable unsigned64-bit arithmetic; identical source/oracle is reused. The scoped
frontend is byte-identical to the already validated native ARM014 frontend. Every
control still repeats on this exact native build before its six scientific captures.

GNU AArch64 objdump uses one8-hex encoded word per instruction, unlike x86 byte tokens.
arm_asm.py explicitly requires elf64-littleaarch64, aligned addresses and one word,
retains source lines, and fails on incompatible instruction encoding. Local checks
cover valid/invalid architecture text, retained old ARM codegen and inline/ancestor
attribution behavior. Mapping records exact sampled-word equality across diagnostic,
isolated original and actual013, plus the entire iterator body's offset differences.
No relocation normalization, inferred alignment or silent caller equivalence. Mapping
status alone is not authorization for a hypothesis: independent review must assess
any sampled tree mismatches, missing coverage and changed caller contexts first.

Root and independent AMD review must approve the immutable plan/execution freeze
before any launch. Ambient observation occupies ARM until approximately06:25UTC;
no deployment/workload overlaps it. Root must confirm idle handoff. Profile and A/A
are separate600s/300s owned-helper jobs; A/A requires completed profile audit and
root phase grant. Latest permissible launch must leave each full cap before07:15UTC:
profile no later07:00UTC when both phases are intended; no new phase after07:15UTC.
No source hypothesis, implementation, candidate timing or new population is authorized.
