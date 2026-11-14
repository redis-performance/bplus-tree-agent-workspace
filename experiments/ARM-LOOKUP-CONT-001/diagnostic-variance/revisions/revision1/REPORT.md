# Variance diagnostic preparation

The separate baseline-only collector is prepared for independent review. No perf capture, workload, build, fleet action, service change or publication was performed by this implementer. H2 and Q4 remain PARK. The diagnostic has no candidate path, A/A gate or acceptance decision.

[Protocol](PROTOCOL.md), [collector](../fleet_variance_diagnostic.py), [offline tests](test_diagnostic.py) and [test log](tests.log) are frozen by [manifest](manifest.json). Root supplies the reviewed operational record and exact live perf/taskset/kernel/version pins. Independent code and operational admission remain separate prerequisites. The existing Q4 collector remains byte-identical at531bbabc; no referee or original collector changed.

## Validation

All26 offline tests pass. Synthetic cases cover all event omissions, duplicates, unexpected events, nonfinite/negative/fractional/oversized numbers, zero work, valid zero software counts, runtime fields, exact scheduling display, strong-group runtime equality, units, source-verified verbose raw reads and unrounded mismatch, wrong models, fixed sequence/commands/locale, single-use claims, imported dependency pinning and affinity race reporting. The descriptive function revalidates parsed scheduling and model fields without clocks or processes.

Fully mocked orchestration exercises support plus exactly four captures, support failure, mid-sequence failure, and an interruption after a reaped child. Every failed path preserves its post-child isolation check and consumes the attempt. A reaped child is not signaled. These tests replace process execution, service/identity checks, clocks, accounting and affinity with deterministic mocks; they establish control-flow correctness, not fleet support or isolation.

The first unreviewed draft incorrectly assumed verbose raw reads lacked a CPU field and went to stderr. It was corrected from primary perf source before any execution; the draft remains in `development/revision0-unreviewed.py`. Initial25-test and final26-test logs remain. Root later identified installed perf6.17.13 under a6.14 directory. The implementer verified the matching stable source; no parser logic change was needed. The earlier freeze and its v6.14 provenance remain in `revisions/revision0`; the current protocol records the matching v6.17.13 source hashes.

## Consultation and evidence limits

Own enabled-tool discovery found no callable cpu-perf/library_status endpoint. The controller performed the actual fresh discovery, library_status and variance-specific ask through its existing transport. This is shared consultation, not this implementer's call. Reported coverage was3 indexed sources out of287,158 passages; the response retrieved two Yasin bibliography/professional-talk passages unrelated to this variance or scope question. They support no causal or collection claim. Detailed transport/backend provenance stays private; costs are unknown. Primary perf source checks support parser grammar only. This preparation has no fresh event-support result and does not explain Q4's failed row.

## TMA classification

| Category | Baseline | Candidate |
|---|---|---|
| Frontend_Bound | Unavailable | Not collected; no candidate |
| Bad_Speculation | Unavailable | Not collected; no candidate |
| Backend_Bound | Unavailable | Not collected; no candidate |
| Retiring | Unavailable | Not collected; no candidate |
| Child categories | Unavailable | Not collected; no candidate |

This nine-event diagnostic does not collect qualified topdown pipeline-slot shares. Ratios, hotspot shares and other-machine profiles cannot substitute for them. No TMA run or interpretation is claimed.

Role: collector implementer. Independent review and execution admission belong to separate roles. Status: PREPARED, NOT ADMITTED.
