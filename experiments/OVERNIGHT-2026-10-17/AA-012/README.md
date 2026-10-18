# AA-012 — batched lookup qualification is mixed

All240fixed rows plus prospective warmup complete serially; exact fixture, checksum,
API count, hit count and unchanged memory checks pass. Long-key hit320/batch16 and
mixed short-key/batch16 qualify on both seeds. Short-key hit/batch16 (the preregistered
primary), hit/batch1 and miss/batch16 do not qualify. Those claims remain PARK.

Wall time is primary and every window meets the declared duration floor. Per-cell
raw block effects and95%t intervals are in [summary.json](summary.json); thread-time
intervals are separate observations. No row excluded or threshold/count changed.
This is local same-binary A/A, not a source comparison, stable-frequency claim, or
replacement for any original unresolved guard. Source selection remains NONE.

[Plan](PLAN.md), [driver](run.py), [analysis](analyse.py), [manifest](manifest.json)
and raw/ retain all commands, UTC endpoints, hashes, stderr and rows. Both seeds,
sixABBA blocks/cell, one unpinned M1 thread; unknown frequency/effective QoS/migration.
The timed scope includes batch assembly, result masks and checksums. Additional
qualified subsets require their own baseline profiles before hypothesis selection.
