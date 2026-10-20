# Next steps — 20 October 2026

**Intel iterator B qualification completed: PARK.** [Fresh evidence](INTEL-ITERATOR-TMA-001/README.md)
qualifies46/48 controls and six baseline TMA captures. Diagnose100K reverse/fraction
precision failures before another comparison; do not repeat the unchanged schedule.
Secondary Intel released, OSS restored; no candidate work queued.

| Order | Work | Required next evidence |
|---|---|---|
| 1 | Intel iterator B | Preregister frequency/residency and CPU/wall diagnostic for failed guards; require all eight controls before B timing. |
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
