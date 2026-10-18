# COUNTERS-004 — monotonic signed-zero layout coverage

All48 fixtures pass release/debug and ASan/UBSan (96children). Independent scalar bit
reader matches exact model bits; all direction/output modes pass. Structural results
agree across builds; allocator usable bytes intentionally compared within each build.

Predeclared coverage prediction passes: descending insertion includes reversed leaves;
alternating zeros use nonzero packed widths. Caution: only64members occupy reversed
physical leaves at both n4096 and n100000. Thus the large fixtures add construction
coverage but are poor stress tests for reversed-leaf throughput. This census does not
claim a CPU profile or a frequency/performance result. Full histograms in manifest.json.

Decision: eighteenth additional diagnostic completed, source NONE. Existing parked
optimization claims unchanged. Next AA-010 new fixture qualification. A future distinct
small-tree or deletion-induced fixture is required to concentrate reversed-leaf work.
