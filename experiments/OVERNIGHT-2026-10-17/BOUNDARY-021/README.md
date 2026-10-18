# BOUNDARY-021 — natural 16-bit member-resize generation wrap

Baseline native/debug and ASan/UBSan both PASS two fixed-seed fixtures. Each build
executes131080natural grow/shrink resizes and observes two65535→1transitions without
assigning private fields or shortening the counter. Each seed runs32770fixed cycles,
keeping eight anchor members while growing to29and shrinking back.274full model
checks/build and10960exact public results pass; completed leaves retain the expected
nonzero generation and anchor leaf identity. Complete outputs/digests agree.

The isolated sanitizer fault removes the zero-generation skip and is detected at
stage32769, the expected first natural wrap cycle. No production bug is observed.
Full lookup/order/rank/scan/ownership checks occur at the low-water state, every256
cycles and around wrap; high-water states receive length, generation, leaf-tag and
public deletion checks. This scope is explicit; high-water full-model checks and
retained optimization variants remain a useful extension, not claimed coverage.

Commands: `python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-021/run.py` and
`faults.py`. [Plan](PLAN.md), [manifest](manifest.json), [summary](summary.json),
[fault](faults/manifest.json), complete logs, source/binary hashes and additive oracle
patch retained. Both seeds use public insert/delete/lookup transitions. No timing
claim or source adoption. Exact backend/model/token costunknown; sequential review.
Decision: baseline wrap coverage validated; suite21, distinct boundary fault41.
EXP-004 A/PARK and EXP-005 PARK/NONE unchanged; variants were not run in this scope.
