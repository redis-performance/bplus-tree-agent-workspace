# Matched adapter diagnostic chart — all effects conditional

![Eight-cell matched adapter diagnostic](adapter-diagnostic.png)

**ALL CONDITIONAL: 0/8 cells qualify both adapter controls; 3/16 individual A/A controls qualify.**
This measures the standalone panic compiler contract under matched source/referee/compiler conditions. It is a harness diagnostic, with no tree candidate or optimization acceptance. Tree-owned memory differs by exactly0% in every compared block.

Circles show all six ABBA block effects, diamonds their median, and segments the observed min/max. Negative means less elapsed time for the corrected adapter. Ranges are observed extrema, not confidence intervals. No old/new A/A control pooling or historical timing subtraction is used.

|Members|Contract|Median elapsed change|Observed block range|Old A/A|New A/A|
|---|---|---:|---:|---|---|
|100000|integer-full-forward|-6.081%|-7.119..-4.618%|PASS|FAIL|
|100000|integer-full-reverse|-8.122%|-9.372..-7.037%|PASS|FAIL|
|100000|integer-score-forward|-1.966%|-7.808..+8.308%|FAIL|FAIL|
|100000|fraction-full-forward|-3.434%|-5.694..-0.077%|PASS|FAIL|
|1000000|integer-full-forward|-4.674%|-6.937..-2.682%|FAIL|FAIL|
|1000000|integer-full-reverse|-7.058%|-9.229..-5.837%|FAIL|FAIL|
|1000000|integer-score-forward|-9.864%|-18.417..-2.722%|FAIL|FAIL|
|1000000|fraction-full-forward|-5.164%|-6.668..-3.661%|FAIL|FAIL|

Every comparison window exceeds10ms; failed A/A precision causes the conditional labels. Only the old-adapter100K full-forward, full-reverse and fractional full-forward controls qualify. All eight corrected-adapter controls fail the ±1% every-block rule. Exact A/A effects and window minima are retained in chart-data.json.

The plot script independently reconstructs all576 raw CSV rows and144 block effects (96A/A +48matched), using exact rational ratios of integer elapsed totals. It verifies raw hashes, metadata, checksums, construction fingerprints, exact owned bytes and stored effects. chart-data.json retains exact effect fractions and per-run evidence plus source/header/adapter/referee/binary/input hashes. Exact fixture semantics and native compiler flags are unchanged; only the declared panic contract differs.

Reproduce from the repository root:

```
uv run --offline --with matplotlib python experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/012-contract-diagnostic/plot-results.py
```

PNG supports embedding and SVG preserves vector shapes/selectable text. The PNG was visually inspected for eight cells, all points, labels, conditional status and legends. The five owned chart artifacts were scanned for concrete private paths and credential patterns. Frozen PLAN.json, driver.py, README.md and freeze.json are verified byte-unchanged before and after plotting. No build, test, benchmark, profile, Git or shared-memory action was performed.

Participant /root/followup_proposal_b; inherited Codex/GPT-6 family; exact serving model, token usage and cost unknown.
