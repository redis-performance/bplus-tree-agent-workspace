# AA-002 — large fixture qualification: lookup PARK

All 96 planned serial rows completed in 654.3 seconds, with no
failures/timeouts/exclusions. All checksums, operation counts and tree-owned memory
stable; frozen binary and source hashes verified before/after. Six fixed ABBA blocks,
one million members, seed1, fixed warmup and counts: [plan](PLAN.md).

Rank16 qualifies under the unchanged descriptive precision gate. Hit16, miss16 and
hit320 fail. Thus lookup comparisons remain PARK; source selection NONE. Rank has no
matching sampled time profile, and its lookup guards remain unqualified; no population
or optimisation acceptance. This new fixture coverage does not establish a general
longer-batch remedy. Do not repeat unchanged until it passes.

[Raw rows](raw/), [manifest and commands](manifest.json), [runner](run.py),
[analysis](analyse.py), [table](SUMMARY.md), [full summary](summary.json).
Thread/wall time and opaque CPU IDs do not establish stable frequency or residency.
Requested QoS was user-interactive; effective QoS unknown. No timing claim promoted.
CPU MCP evidence checker consulted: drop_number because frequency is absent (its
heuristic also missed the explicitly specified single benchmark thread). Prior ask
retrieval's OpenVINO passages were irrelevant; benchmark05/14 method/code consulted
without transferring M4 measurements, clocks or CPU numbering.

Uncommitted HARNESS-001 snapshot over base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c;
git protection previously recorded, no retry. Backend/model and token costs unknown;
supervisor records CLI usage separately. Next: natural wide-ID/scan boundary coverage.
