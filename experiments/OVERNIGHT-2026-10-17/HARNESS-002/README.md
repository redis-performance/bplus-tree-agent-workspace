# HARNESS-002 — independent query fixture, locally validated

Separate isolated referee revision; root source and HARNESS-001 remain unchanged.
Adds --query-order coupled|independent and --query-seed, construction/query labels and
fingerprints. Default coupled behavior preserves historical access order. Independent
mode shuffles identity using its own seed, independent of hash/construction RNG draws.
Both modes allocate the same arrays. Point reads, updates, deletes and warmup use the
query permutation; insertion uses construction order. Partial-pass update verification
uses query positions. Existing scan/iterator count and member checks remain intact.

[Patch](harness.patch), [snapshot freeze](freeze.json), [validation](validation.json),
[independent Python oracle](test_query.py), [MCP methods consulted](cpu-mcp.json).
Exact build/test commands, stdout/stderr and hashes are in validation.json. Both release
and ASan/UBSan pass43 upstream tests, all3 existing referee groups, and80 new all-case
fixture cells per build. New oracle reconstructs SplitMix64/Fisher-Yates/FNV separately,
checks partial sums, binary-key boundaries, independent-seed separation, malformed input
rejection and coupled behavior. Timing values from tests are not performance results.

Sequential code review checked query uses and update verification. Reviewer startup
failed before execution: thread-store context load error, no rollout. No independent
review claimed. Backend/model/token cost unknown; supervisor tracks actual CLI usage.

No new OS APIs adopted: inherited observability was inspected, public pthread query
reports requested QoS only. Effective QoS/frequency/residency unknown. CPU MCP ask first,
then methods/code05/14; irrelevant Roofline retrieval not evidence. No M4 numbering,
frequency or rates transferred. Fixture coverage is supported by DIAG-005, not a promise
of reduced noise. A new A/A must qualify this referee before source comparison.

Provenance is base commit plus uncommitted isolated patch/hashes; previous protected-git
denial not retried. Commit review pending. No source candidate or population acceptance.
Next: fixed AA-003 plan, serial measurement after all validation/agent activity is idle.
