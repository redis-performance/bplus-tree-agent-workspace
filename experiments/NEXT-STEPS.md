# Next steps — 20 October 2026

**First: Intel iterator-cache B baseline qualification and matched TMA.**
Fresh baseline [slot classifications](TOPDOWN-ASSESSMENT-20261020/README.md) show
Memory Bound8.55%→16.47% at100K→1M, Frontend Bound<1%. Test work/dependent-load
removal, not an assumed frontend bottleneck. No candidate captured or selected;
the bounded Intel profiling lease is released.

| Order | Work | Required next evidence |
|---|---|---|
| 1 | Intel iterator B | Corrected baseline, eight qualified controls, matched baseline/B TMA plus cycles/instructions per element, complete guards. |
| 2 | AMD scan A | Resolve timing/profile-binary transfer and 1M control failure. Corrected B stays rejected. |
| 3 | M1 predicate / inline search | Qualify the original adverse guards before any further candidate comparison. |
| 4 | Bulk decoder | Validated longer-window referee plus a demonstrated public consumer; existing cutoff/count-one trials already happened. |
| Hold | M6 lookup / mask / NEON | New diagnostic evidence; no unchanged retry or rescue of a rejected patch. |

[Full review and all17 parked records](PARKED-NEXT-STEPS-20261020/README.md) ·
[Intel draft preflight](PARKED-NEXT-STEPS-20261020/intel-iterator-preflight.json) ·
[All33 experiment attempts](EXPERIMENT-FLOWS-20261020/README.md)

Exact runner ownership, new measurement condition, compiler/binary/fixture identities,
calibrated counts and review remain prerequisites. No old control qualifies a new source
identity. Acceptance still needs correctness, full qualified guards, profiles, fresh
confirmation and independent review. New hypotheses require both population stages.

The [previous next-step notes](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/430364100228964db9bf3467c5c09911e3d33be9/experiments/NEXT-STEPS.md)
are historical: M6 replications and count-one trials have since completed; do not queue them as untested work.
