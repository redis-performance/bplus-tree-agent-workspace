# Next steps — 20 October 2026

**Intel diagnostic sweep complete:**32/36 configurations fully qualify;
[assessment](INTEL-PARKED-PROFILES-001/ASSESSMENT.md) ranks update lookup-load attribution
as the strongest new lead and iteratorB as the best existing parked continuation.
Resolve four isolated TMA gaps and original timing-guard failures before acceptance
work. Profiler released, OSS restored; no workload queued.

| Order | Work | Required next evidence |
|---|---|---|
| 1a | Intel update lookup | 1M≈68% Memory Bound; attribute dependent loads with precise sampling and actual operation/phase counts before proposing code. |
| 1b | Intel iterator B | Leaf-transition load versus arithmetic diagnostic; CPU/wall/frequency diagnosis of failed guards; all eight controls before timing. |
| 1c | Corrected Intel scan B | Branch/layout attribution; resolve two unavailable guard TMA baselines with a changed isolation protocol. |
| 2 | AMD scan A | Resolve timing/profile-binary transfer and 1M control failure. Corrected B stays rejected. |
| 3 | M1 predicate / inline search | Qualify the original adverse guards before any further candidate comparison. |
| 4 | Bulk decoder | Validated longer-window referee plus a demonstrated public consumer; existing cutoff/count-one trials already happened. |
| Hold | M6 lookup / mask / NEON | New diagnostic evidence; no unchanged retry or rescue of a rejected patch. |

[Full review and all17 parked records](PARKED-NEXT-STEPS-20261020/README.md) ·
[Executed Intel preflight](INTEL-ITERATOR-TMA-001/protocol.json) ·
[All34 experiment attempts](EXPERIMENT-FLOWS-20261020/README.md)

Exact runner ownership, new measurement condition, compiler/binary/fixture identities,
calibrated counts and review remain prerequisites. No old control qualifies a new source
identity. Acceptance still needs correctness, full qualified guards, profiles, fresh
confirmation and independent review. New hypotheses require both population stages.

The [previous next-step notes](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/430364100228964db9bf3467c5c09911e3d33be9/experiments/NEXT-STEPS.md)
are historical: M6 replications and count-one trials have since completed; do not queue them as untested work.
