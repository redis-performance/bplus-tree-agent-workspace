# CPU-perf MCP consultation — M6 controller,19 October2026

A real post-closure consultation is complete using **cpu-perf0.1.1 over local MCP stdio**. The newly fetched main rule is [docs/PERFORMANCE-MCP.md](../../../docs/PERFORMANCE-MCP.md). This is source/evidence retrieval, separate from hardware-counter collection. No previous MCP use or benchmark qualification is implied retrospectively.

[Call inputs/timestamps/response hashes](tool-calls.json) · [Actual discovered schema](tool-catalog.json) · [Findings and limitations](CONSULTATION.json).

Eight actual calls: library_status twice, ask twice with actual M6 source/build/assembly/control results, get_benchmark once, check_evidence twice, read_source once. Initial direct-tool/config/cache discovery was negative; the documented local launcher successfully fetched controller dependencies. Agent settings and benchmark inputs were unchanged.

The wheel serves bundled library commit deb5a0bac467(5October2026). Automatic indexing, updates and embeddings were disabled. The library initially had0/287linked sources; an explicit [LLVM Benchmarking](https://llvm.org/docs/Benchmarking.html) read indexed one source/five passages. It discusses OS-dependent noise reduction and cautions that low noise alone does not eliminate bias. Linux-specific commands were not applied on M6. The bundled [measurement-pitfalls method](https://github.com/usamahz/cpu-performance-engineering/tree/main/misc/benchmarks/05-measurement-pitfalls) was also read; its measured M4 Pro results are not our M6 data.

The initial ask could not parse the narrative/otool context as tool metrics and supplied unread-source leads. The heuristic evidence checker misread compact formatting and still missed known fields after clearer formatting. Its outputs cannot fill unknown frequency, core-residency or microarchitecture data. These limits are recorded, rather than presenting an MCP endorsement.

**Decision unchanged: EXP-009 PARK/sourceNONE.** No new benchmark, candidate, population, count adjustment, permission change or protocol relaxation occurred. Future investigations must include fresh availability checks and contextual MCP consultation; current frozen results remain intact. Raw responses and indexed source bodies stay in ignored controller storage; public Git holds requests, summaries, links and hashes.
