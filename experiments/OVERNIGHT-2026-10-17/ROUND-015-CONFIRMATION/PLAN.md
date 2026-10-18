# Fresh seeds and debug-assertion build coverage

New bounded correctness matrix, preregistered before execution. The benchmark builds
omit REDIS_DEBUG while the added boundary oracles used it. Existing successful debug
runs remain unchanged; add coverage for its omission, retaining every oracle CHECK and
all unconditional serverAssert checks. No timing campaign or assertion-policy adoption.

Three finalized oracles: multi-member natural wrap, colliding SCAN intervals, same-size
cleanup intervals. Exact control/EXP-004 A/B/C source snapshots and unchanged allocator.
Fresh fixed seeds: wrap64513/64553, scan64567/64577, cleanup64579/64601. No other test
changes. For each oracle and source: native-O3 and-O1ASan/UBSan, each with/without
REDIS_DEBUG.48build/run cells in fixed oracle/source/build/debug order, serial120s
children and600s total budget. No count reduction if bound fails. The full natural
wrap/cycle/model counts and every prior coverage gate remain mandatory.

Compare logical digests across all16cells within each oracle. Require each cell's
explicit PASS, exact expected model/fixture/resizes/scan counts and empty sanitizer
stderr. Physical identifiers and callback totals can differ by allocator; retain and
report without forcing physical equality. This is sequential fresh-seed confirmation,
not independent agents, independent hardware or optimization confirmation. No new
suite/diagnostic/population count and no promotion of existing PARK decisions.
