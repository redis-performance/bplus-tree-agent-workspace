# Intel next experiments — evidence-led priorities

**No implementation selected.** This sweep closes diagnostic coverage of both parked
families and the unfinished update investigation. It does not qualify timing or
rescue rejected patches. Full TMA trees: [iterator](ITERATOR.md), [scan](SCAN.md),
[update](UPDATE.md). All figures below are scoped to these fresh diagnostic binaries.

| Priority | Evidence | Next falsifiable question and stop condition |
|---|---|---|
| 1 — strongest new lead | Update1M same/position: Memory Bound68.12%/68.15%; Backend80.71%/80.99%. `FindForAdd`+`LeafFindMember` account for69.33%/64.01% of user-cycle sampled period. | Are dependent member-index/leaf loads the dominant cost? Resolve the≈10% unresolved libc sample address, map exact lookup instructions and use qualified precise-load sampling, with actual operation/phase counts. Reject a lookup-memory hypothesis if samples locate the cost elsewhere. Do not spend a round on neighbor-check arithmetic without evidence of meaningful cost. |
| 2 — best existing parked candidate | Iterator B retains16-byte state versus A24. At1M full output, base/A/B Memory Bound15.94%/16.27%/16.26%; Bad Speculation2.80%/2.00%/2.00%; Frontend0.70%/1.85%/2.35%. | Distinguish leaf-transition metadata-load dependencies from removed offset arithmetic using transition census and precise load attribution. [Exact annotation](annotation/README.md) identifies the relevant sites. Test memory stalls per completed operation and precise-load attribution; unchanged slot fractions alone neither prove nor refute work reduction. No speed conclusion from slot percentages. Before timing, diagnose original reverse/fraction A/A failures on that host with CPU/wall brackets and frequency/residency evidence. |
| 3 — corrected scan B | Baseline Bad Speculation33.50%/23.96%, Frontend19.20%/16.70% at100K/1M; `IndexScanSlot`≈85% of user-cycle samples. B raises frontend share3.95/2.49pp. | Attribute unpredictable branches and code layout inside the slot function before another SIMD rewrite. Seven-member trim guard executes no full8/16-tag chunks: test fixed setup/tail/layout overhead separately. Reject a direct SIMD-chunk explanation there. Both guard baseline TMA comparisons are currently unavailable. |
| Hold — corrected baseline013 | Historical30/40 cells fail precision. This representative profile sweep is not its exact full referee. | Separate causal metrology investigation before using those cells for any acceptance. No unchanged retry. |

“Best parked” is a follow-up priority, not an implementation winner. New source
hypotheses still need three independent proposals/chair and three isolated
implementations, correctness, qualified A/A/ABBA guards, fresh confirmation and review.
Old-source scan B, lookup SSE2 and iterator C remain rejected. Update has no candidate.

## What is still missing

This is family-level triage, not the full acceptance matrix: iterator1M reverse/fraction,
update100/1K/10K and other historical guard fixtures were not swept. Their existing
controls/results remain unchanged.

Four whole configurations cannot support qualified TMA interpretation:

| Configuration | Failed window | Sibling occupancy (gate≤1%) |
|---|---|---:|
| Iterator100K score-only B | L2-3 | 2.852% |
| Iterator1M score-only A | L2-1 | 2.467% |
| Scan trim319 signed-zero baseline | L2-1 | 2.662% |
| Scan resize319 signed-zero baseline | L2-1 | 1.145% |

Every raw capture remains. **No retry or averaging away the failed window.** A future
completion protocol must diagnose/change the isolation condition first (including
sibling/interrupt activity), preregister matched base/candidate captures and retain
this attempt. The online sibling is a measured limitation; its activity source is
unidentified. Changing SMT or host scheduling would create a new measurement condition.

All36 counter windows and36 PID sample windows pass their own scope checks. Counter
ratios do not supply operation counts. All36 exploratory L3 captures have minimum8%
scheduling and mixed denominators: L1/L3/DRAM attribution is unavailable. A smaller
compatible event group/precise-load protocol must be independently qualified before
claiming a cache level. Request no new measurements from the released runner without
a fresh bounded lease/preflight.

Updates evolve during successive windows. Present phase/order; neither stationary
state nor timing transfer to the historical binaries is established. Perf period
shares, optimized line mapping and sampling skid do not identify instruction latency.
A source line with few samples can still have indirect costs. No acceptance claim,
new population or ledger-status change follows from these profiles.
