# Intel parked-work profiles

**36 configurations collected;32 qualify for complete L2 interpretation.**
104/108 L2 windows pass; four fail the unchanged sibling-activity gate. No retries.
Both parked families and the unfinished update investigation are covered. Source **NONE**;
34 attempts remain18parked /16rejected /0approved, with22 implementation populations.

| Work | Concrete finding | Next action |
|---|---|---|
| [Update NONE](UPDATE.md) | 1M same/position: **68% Memory Bound**; lookup functions receive **64–69%** of user-cycle samples. | Strongest new lead: precise lookup-load attribution and phase/work counts. |
| [Iterator A/B](ITERATOR.md) | 1M full output: memory share stays≈16%; speculation falls, frontend share rises. | Best parked continuation: distinguish leaf-transition loads from offset arithmetic; resolve failed timing guards. |
| [Corrected scan B](SCAN.md) | Baseline speculation24–34%; slot function≈85% of samples. B frontend share rises2.49–3.95pp. | Branch/layout attribution; complete two unavailable guard-baseline comparisons under a corrected isolation protocol. |

[Ranked hypotheses and exact blockers](ASSESSMENT.md) · [Instruction annotation](annotation/README.md)

## TMA classification

Every cell/build has its own four-root tree plus Memory/Core children:
**[Iterator18 configurations](ITERATOR.md) · [Scan8](SCAN.md) · [Update10](UPDATE.md)**.
Qualified L1 roots sum100% within the frozen tolerance. Failed configurations display
unavailable, with every numeric observation retained. L3 cannot identify cache/DRAM
shares: minimum scheduling8%, mixed units. No IPC, sample share or TMA share is a speedup.

## Validation and provenance

177 preparation commands pass: original tests, sanitizer checks, iterator oracles,
36 completed original/profile/sanitizer semantic cases and same-mode owned-byte parity.
All36 counter windows and36 PID sample windows pass their own scope gates;
all raw samples decode independently with zero recorded losses.
[Independent audit](INDEPENDENT-AUDIT.json) · [Review](FINAL-REVIEW.md) · [Raw results](results/)

Source37efd287f; Clang18/O3; exact retained patches in isolated builds; Intel Sapphire
Rapids CPU2/NUMA0, sibling50 online. [Protocol](protocol-v2.json), [build hashes](results/build-sha256.json),
[analysis](analysis.json), [44 actual topdown MCP queries](topdown-mcp-calls.json).
Topdown71dea5e / pmu-tools2026.4.7.0. CPU-perf actual start/final consultations and source
lookup logged;1/287 sources indexed,27 passages. Retrieved material does not establish
our mechanisms; priorities are measured-evidence reasoning, not MCP endorsement.

Attempt1's36 launcher failures occurred before any capture; retained [failure audit](attempt1/INDEPENDENT-AUDIT.json).
V2 corrected absolute CPU placement only. A later busy-host preflight safely declined
the lease before an idle window was acquired. No unrelated workload was killed.

**Runner released14:43UTC:** coordinator RUNNING, service/timer inactive, no owned work.
[Fresh live proof](RELEASE-FINAL.json) · [Activity](ACTIVITY.md). Raw perf/ELFs remain local
with committed hashes. Root plus independent intel_b_review; model/token costs unknown.
