# External-buffer and dense-renumbering reachability — validated

Both fixed whole-oracle captures pass. The external fixture calls the public defrag
external-member path 3,088 times: 2,059 moves and 1,029 declines. The narrowing fixture
executes one dense leaf renumbering and one index rebuild, while its original nonzero
SCAN cursor continues across an observed wide-to-narrow transition.

[Plan](PLAN.md), [manifest](manifest.json), [summary](summary.json), [mapped analysis](analyse.py).
Raw exports/profiles remain ignored under scratch, with exact hashes. Counts include
setup and validation; they do not establish hotness, cycles, frequency or speed. These
are two additional captures within COUNTERS-009, not a new diagnostic count.
