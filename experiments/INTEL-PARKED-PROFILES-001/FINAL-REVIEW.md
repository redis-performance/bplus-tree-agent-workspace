# Independent final review

**PASS for diagnostic publication; NONE for source adoption or timing acceptance.**
Reviewer: `/root/intel_b_review`, Codex; actual model/token costs unknown. No runner
commands or measurements were performed by this reviewer.

[Raw reconstruction](INDEPENDENT-AUDIT.json) independently verifies36 configurations,
104/108 qualified L2 windows and32/36 complete configurations. [Report check](INDEPENDENT-REPORT-CHECK.json)
matches all36 qualification decisions and432 slot-metric means against the raw
reconstruction. The renderer shows unavailable for any incomplete TMA configuration;
counter and sample stages use their own qualification.

## Evidence integrity

- 358 preparation files match archived attempt1;221 source/driver hashes checked.
  All177 validation commands succeeded. All36 completed original/profile/sanitizer
  cases preserve semantics and same-mode owned bytes. Eight original test suites
  pass43/43; original and additive iterator cache oracles pass for base/A/B.
- 44 downloaded ELF files independently match recorded SHA256, including every
  profiled binary. Recorded windows are serial. Exact frozen baseline/patch,
  launcher correction and readiness-loop provenance remain explicit.
- All36 grouped counter stages have the exact five events, finite nonnegative
  values,100% scheduling, successful return codes and valid scope.
- All36 PID sample stages pass their own scope and command/report checks.
  Raw sizes/hashes match; runner-compatible perf7 decodes every file with no
  recorded loss records. Reports show zero lost samples and exported sample
  counts agree. This does not establish absence of sampling bias/skid.
- Attempt1's36 pre-capture launch failures remain archived. V2 changes absolute CPU
  selection only and reuses exact prepared binaries. No failed capture was retried.
  Parent's [fresh release proof](RELEASE-FINAL.json) reports the runner released;
  this reviewer did not independently contact it.

## TMA classification and exclusions

Full baseline/candidate four-root partitions and Memory/Core children are in
[iterator](ITERATOR.md), [scan](SCAN.md) and [update](UPDATE.md). They use total
pipeline slots, not sampled periods. All qualified roots meet the frozen sum,
unit, interval,100% scheduling and scope gates. All36 exploratory L3 captures
have minimum scheduling8%; cache-level/DRAM attribution remains unavailable.

| Entire configuration unavailable | Failed L2 window | Sibling occupancy |
|---|---:|---:|
| Iterator100K score-only B | 3 | 2.851711% |
| Iterator1M score-only A | 1 | 2.466793% |
| Scan trim319 signed-zero baseline | 1 | 2.661597% |
| Scan resize319 signed-zero baseline | 1 | 1.145038% |

These failures exceed the unchanged1% gate. Their other windows cannot qualify the
whole configuration. Both scan guard baseline/B TMA comparisons are unavailable.
Independently valid counter/sample stages may still be described with their own
scope; they cannot replace missing TMA or historical timing guards.

## Assessment challenged

1. **Strongest new investigation: update member lookup/data supply.** At1M,
   same/position have Memory Bound68.12%/68.15%, Backend80.71%/80.99% and
   Retiring10.04%/9.72%; `FindForAdd` plus `LeafFindMember` account for69.33%/64.01%
   of user-cycle sampled period. This supports investigating those lookup paths
   before neighbor-check arithmetic. Resolve the roughly10% unresolved libc PC,
   then attribute exact loads and collect phase/completed-work counts. Do not
   guess its function or claim DRAM, stationary state, or per-operation cost.
2. **Best retained parked follow-up: iterator B, conditional on metrology.**
   It retains16-byte state versus A24 and has qualified full-output profiles.
   At1M, Memory Bound remains15.94%/16.27%/16.26% for base/A/B while speculation
   falls and frontend share rises. Fractions alone neither prove nor refute
   reduced memory stalls per operation. The exact annotation supports testing
   leaf-transition metadata dependencies against removed offset arithmetic.
   Resolve the historical reverse/fraction A/A failures before candidate timing.
3. **Scan: inspect branch/fetch/layout inside the slot function.** Baseline
   Bad Speculation33.50%/23.96% at100K/1M and approximately85% user-cycle samples
   in `IndexScanSlot` make this a concrete target. B's frontend increases are
   observations, not a regression measurement. Seven-member guards execute no
   full8/16-tag chunk, so a direct vector-chunk explanation there is unsupported.
   Guard TMA pairs still need a separately preregistered isolation correction.

[Annotation](annotation/README.md) correctly distinguishes optimized source-line
aggregates from instruction cost: baseline packed-length line589 combines0.56%
load and20.04% compare samples. B's12.08% width-test attribution follows a metadata
load; the0.19% cache-presence-test attribution does not establish either
instruction's total cost. Raw/ELF identities and all three full-output sample
scopes agree. Sampling skid and optimized DWARF prevent causal latency claims.

This ranking is for investigation, not candidate selection. New hypotheses still
require the prescribed population process. Historical scan/lookup/iterator
rejections, parked decisions, failed timing guards and full baseline precision
debt remain unchanged. No unchanged rerun or approval is justified by this sweep.

## MCP use and limits

Own fresh `library_status` and `ask` calls supplied these final counters and
annotation observations: [inputs, hashes and findings](reviewer-final-consultation.json).
Local stdio MCP revision `a5a05e6bf7c9` was available;1/287 sources and27 passages
were indexed. No supporting passage matched the final question. These judgments
come from independently checked measurements, not an MCP endorsement; unread
retrieval leads carry no claims. Raw responses remain local. Parent's44 actual
topdown MCP queries are shared evidence, not this reviewer's calls.
