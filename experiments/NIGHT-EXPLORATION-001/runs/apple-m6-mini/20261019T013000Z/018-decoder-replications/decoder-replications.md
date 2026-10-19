# M6 decoder replication chart

All displayed elapsed-time differences are **conditional private-kernel diagnostics**.
Discovery has 0/210 fully qualified cells: all 2,476,800 timer windows are below 10 ms.
Fresh EXP-007 A confirmation has 0/30 fully qualified cells: all 185,760 windows are
also below 10 ms. Relative A/A PASS means only that all six block effects fit ±1%;
it does not clear the minimum timer window or permit source acceptance.

The four panels show EXP-004 forward A at widths 8/60/64; EXP-007 width 60/forward/
count 96 A/B/C; EXP-008 width 60/forward/count 16 and count 96 A/B/C; and fresh EXP-007 A.
The fresh panel includes its primary and the two guard median losses with passing
relative A/A controls. There are six fresh guard median losses in total; the full
audit retains all cases. Fresh means new seeds on the same M6, **not an independent
machine**. No M1 values are pooled or plotted.

Each row displays all six candidate block effects and all six corresponding
same-binary A/A block effects. Squares/diamonds mark their respective medians;
thin horizontal lines show observed minima/maxima, not confidence intervals.
Gray shading is the ±1% relative A/A screen. The −2% gain and +1% loss lines are
references, not evidence that any case passes full qualification. Negative means
less elapsed time within that exact frozen workload. Native ns/decode is not
compared across contracts. Label notation: w=packed-score width, n=decoded count,
F=forward and R=reverse.

Data come from the independent discovery audits and their byte-identical summaries.
The fresh confirmation blocks are separately checked against CONFIRMATION-AUDIT.json;
its primary A/A fails, and the two shown guard losses exceed +1% in every block.
decoder-replications.json retains exact values, qualification flags and SHA256
provenance for all chart inputs, plus the complete fresh audit. Existing source,
referee, frozen inputs, discovery evidence and earlier profile reports are unchanged.

Reproduce from the repository root with:

```
uv run --offline --with matplotlib python experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/018-decoder-replications/plot.py
```

The PNG was visually inspected for legible labels, separate experiments, visible
control failures and complete block markers. PNG and SVG are standalone exports.
Public artifacts pass a scan for local user paths and credential patterns. No new
measurement, build or profile ran. Selected A's software profile is recorded as a
separate profile-analysis/PROFILE-A-ADDENDUM.md/json; raw path-bearing captures stay
private. Exact serving model/token/cost unknown.
