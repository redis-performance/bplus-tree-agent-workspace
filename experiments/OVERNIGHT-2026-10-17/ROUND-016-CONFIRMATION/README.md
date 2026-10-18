# Fresh-seed, debug-disabled confirmation — validated

All64fixed cells pass:48external-ownership cells (two fresh seeds, three intervention
modes, control/EXP-004 A/B/C, native andASan/UBSan), plus16live-narrowing cells. Every
semantic/coverage assertion remains active. Per-case/seed/mode logical ID/score digests
agree across all sources/builds; runtime stderr is empty. Full key bytes are checked
separately, not included in the printed digest.

Sources/tests/support are exact copies of successful frozen snapshots. Only input seeds
and omission of REDIS_DEBUG differ; unconditional serverAssert and oracle CHECK remain.
No earlier debug/timing binary or assertion setting changes. All commands serial and
bounded120s, with source/binary/stdout/stderr hashes in [manifest](manifest.json).
[Plan](PLAN.md), [summary](summary.json), [driver](run.py).

This is sequential fresh-input/build confirmation, not independent-agent confirmation
or a speed claim. SourceNONE and existing performancePARK remain. No added suite,
diagnostic, baseline or optimization count; backend/model/token cost unknown.
