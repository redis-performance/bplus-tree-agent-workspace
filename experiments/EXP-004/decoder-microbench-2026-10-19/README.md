# Focused packed-score decoder microbenchmark

The new small benchmark is ready and has run locally. EXP-004 A does **not** improve
this decoder loop across layouts: it is substantially slower in the byte-aligned
8-bit and 64-bit cases. The earlier iterator gains therefore cannot be generalised
to a universally cheaper decoder. EXP-004 remains A/PARK; main source is unchanged.

| Forward layout | Baseline median ns/decode | A median ns/decode | Paired median time change | Observed six-block range |
|---|---:|---:|---:|---:|
| 8 bits | 1.136 | 1.314 | +15.65% | +14.39% to +18.13% |
| 60 bits | 1.199 | 1.256 | +4.72% | +3.47% to +4.99% |
| 64 bits | 1.134 | 1.253 | +10.39% | +9.80% to +10.75% |

Positive percentages mean slower. Process medians are descriptive; paired effects
compare the means of two process statistics per side within each ABBA block, then
report the median of six effects. Minimum-based effects agree for these layouts.
Same-cell A/A median-effect ranges are respectively -1.39% to +0.26%, -0.46% to
+0.18%, and -0.22% to +3.16%. The candidate ranges are separated from these controls.
Other cells have retained noisy blocks; small differences are inconclusive. No
confidence intervals or independent confirmation are claimed.

The complete matrix took **12.58 seconds**: 960 serial processes, 123,840 measured
batches, 49,152 decodes/batch. It used Apple M1, Darwin 25.3.0, Apple Clang 17, O3,
no LTO, eight warmed synthetic leaves and one unpinned thread. Frequency, effective
QoS and within-window migration remain unknown. The run occurred at 23:13 UTC on
18 October / 00:13 Lisbon on 19 October. No overnight supervisor was restarted.

Use [the benchmark guide](../../../docs/DECODER-MICROBENCHMARK.md) to build and run:

```sh
make decoder-check
make decoder-sanitize
python3 scripts/run-decoder.py --out scratch/decoder-new-run
python3 scripts/analyse-decoder.py scratch/decoder-new-run
```

The experiment compares the exact original control and A source hashes in
`EXP-004/freeze.json`. The separate harness commit is
`c5b817d056dd7d033640777a067e3fd73cad0dfa`, made before the timing matrix. The build
manifest's `base_commit` is its parent because compilation preceded that commit;
recorded file hashes identify the committed harness, and the run manifest records
its commit and binary hashes before/after. Neither production source nor original
iterator guards were changed.

[Assembly excerpts](codegen/) retain packed loads and decoding inside the loop.
A has fewer static conditional branches (24 versus 29), yet takes longer here.
These counts are not executed instructions. The baseline can short-circuit its
predicate at aligned offsets; code shape and dependency differences are plausible
explanations, not demonstrated hardware causes. This loop's unrolling, checksums
and inlining differ from the original iterator. It does not identify the cause of
the score-plus-length iterator regression.

The timer reports a 41.67 ns tick and minimum nonzero interval. Empty-call minima
can quantize to zero; they do not establish zero overhead, and nothing is subtracted.
There are no measured CPU cycles/instructions on this Mac. Optional Linux counters
still require validation on a permitted Linux host. Cache warming is intended by
the fixture and warm-up, not verified with cache-miss counters.

Evidence:

- [Preregistered plan](PLAN.md) and [validation record](VALIDATION.md).
- [All cell results](local-m1/SUMMARY.md), [process statistics](local-m1/process-summary.json),
  [histogram bins](local-m1/histogram.csv), and [raw samples](local-m1/raw/).
- [Run manifest](local-m1/manifest.json), [release build](local-m1/build.json),
  [sanitizer build](sanitize-build.json), and [static code inventory](codegen/summary.json).
- [Raw-data audit](local-m1/AUDIT.json): 1,920 raw file hashes, all 123,840 rows,
  960 process summaries and 480 paired effects checked. Reproduce with
  `python3 experiments/EXP-004/decoder-microbench-2026-10-19/audit.py`.

The next useful diagnostic is to compare this loop's generated predicate paths with
those in the actual score-plus-length iterator, preserving aligned layouts as
explicit controls. A new optimization proposal should explain both the iterator
benefit and these decoder regressions before another bounded population experiment.
This is one new harness/diagnostic after the overnight campaign, not a sixth
optimization population. Optimization totals remain 0 accepted / 2 rejected / 3 parked.
