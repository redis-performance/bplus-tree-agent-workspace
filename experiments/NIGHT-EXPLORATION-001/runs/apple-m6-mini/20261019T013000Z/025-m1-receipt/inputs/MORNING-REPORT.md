# Early final report — Apple M1, 20261019T005019Z

Status: first-pass queue complete; no source candidate selected. Started
2026-10-19 00:50:42 UTC; early final report prepared about 01:44 UTC under
the PLAN.md stop-early rule. Injected campaign deadline remains 20:00 UTC.
Launch source commit `77d32df82cd5da02b95c6afb6193fcf83f67223f`;
host branch at reporting `4c48fa7ed2d8cf4f1144626276bfb2a602c63bf9`
(round-2 publication). Both have the same baseline tree source hash. No
upstream PR, issue, merge, release or server work was attempted.

## What changed our understanding

1. The five-size all-operation baseline is validated, but 39/40 cells fail
   strict A/A precision. [Baseline matrix](001-baseline/matrix/SUMMARY.md)
   measures descriptive batch averages only.
2. Rank's shorter-side accumulation reduces predicted visits, but three
   [isolated variants](002-rank/RESULT.md) do not show a consistent gain at
   both 100K and 1M. Position-preserving updates at 1M still reinsert on
   11,058/20,000 exact pack failures, even without a neighbor-order change;
   [update result](003-update/RESULT.md) separates this from other paths.
3. The private count-one decoder can show large scoped gains, yet its current
   policy bodies alter codegen and repeatedly lose guards. All 70 A/A cells
   have sub-10-ms windows. [DECODE-001](005-decode/RESULT.md) is PARK, not an
   iterator or tree-level optimization.

## Experiment scoreboard

| Target | Profile finding | Candidate | Primary effect / range | Guards and precision | Decision |
|---|---|---|---|---|---|
| Five-size baseline | Validated descriptive eight-operation matrix | none | not a code comparison | 39/40 A/A cells fail strict gate | COMPLETE baseline |
| Rank | Public sampled PCs and structural census support shorter-side test | A/B/C sequential | No variant consistently improves both 100K and 1M across six blocks | Strict 100K/1M A/A fails | REJECT bounded trial; source NONE |
| Update paths | Five named paths and scoped public profiles; exact pack failures at 1M | none | NOT RUN | Both primary A/A cells fail | Diagnostic COMPLETE; candidate NONE |
| Single lookup | Hit profile lands many PCs in platform memchr; about 1.14–1.16 full comparisons/hit | none | NOT RUN | EXP-006 already tested supported inline scanner family | Diagnostic COMPLETE; chair NONE |
| Private single-score decoder | Prior whole-process profile plus current release assembly locate policy/caller; fresh sampler denied | A/B/C sequential | Width-60 forward count-one medians −18.00% / −35.29% / −43.68%, exploratory | 0/70 A/A qualify; 21/22/31 guard cells have median loss >1% for A/B/C | PARK; source NONE |

The decoder numbers are Apple M1 batch averages under a private output-array
contract. They are not public iterator effects, individual-operation latency
percentiles, portable speedups or server predictions. No optimization has
passed correctness, qualified benchmark guards, profile validation, independent
confirmation and independent adversarial review together. Overall optimization
decisions: **0 accepted / 3 rejected / 6 parked across 9 populations**.
Three proposal and implementation passes in rank and decoder were sequential
by one worker, not independent agents.

## Reproduce and provenance

The actual host is an Apple M1 MacBook Air, eight cores (four performance/four
efficiency), macOS 26.3 ARM64, Apple Clang 17. Full generic
[host manifest](HOST-MANIFEST.json) records compiler and initial hashes.
Root `src/zset_btree.c` SHA256 remains
`d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`;
header `496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83`;
frozen `bench/microbench.c`
`b84d81d0e39b4c7405da0bc12e4f1a14b7fd1f83a38fec595fea87ad3d9effde`.
New update and lookup referee hashes are in their results; decoder source,
referee, binary and assembly hashes are in its
[build summary](005-decode/BUILD-SUMMARY.json). All three decoder patches and
three rank patches are retained. No root `src/` edit was made.

Runbook commands and fixed seeds are in the [queue](../../../PLAN.md) and
[measurement protocol](../../../MEASUREMENT.md). Baseline reproduction uses
`python3 scripts/run-size-matrix.py --out NEW-OUTPUT --budget-seconds 600`
followed by `python3 scripts/analyse-size-matrix.py NEW-OUTPUT`; use a new
directory. Decoder build/run/audit commands are in its [result](005-decode/RESULT.md).
Rank, update and lookup result pages link their manifests, raw rows, checksums,
profiles and validation. Round 2 [audit](ROUND-002-AUDIT.json) and decoder
[audit](005-decode/AUDIT.json) pass. Decoder's four raw archives contain all
6,720 process CSVs, 866,880 timed sample rows and stderr files; every archive
member hash and per-process median was independently reconstructed.
Measurements ran serially, with no compilation, test or profile overlap.
Frequency, DVFS and within-window core residency were not measured.

## Other-host comparison

| Identical patch/harness | M1 baseline/candidate | M6 baseline/candidate | Reproduced? |
|---|---|---|---|
| Rank shorter-side variants | Bounded trial REJECT | NOT RUN / UNKNOWN | No |
| Private count-one decoder A/B/C | Exploratory gains plus guard losses; PARK | NOT RUN / UNKNOWN | No |

Remote checks for `exploration/apple-m6-mini-*` and main repeatedly failed DNS
resolution for `github.com`, last at 01:43:12 UTC. M6 branch, commit, patch
identity and decision are UNKNOWN. No M6 binary, timing or baseline was used
as M1 data. Local branch publication through round 2 was observed at
`4c48fa7e`; this round's evidence is still uncommitted.

## Limits and handoff

RANK-001 has no winner; UPDATE-001 and LOOKUP-001 have no selected candidate;
DECODE-001 has no qualified control and many guard losses. Fresh candidate
confirmation, cross-host replication, public iterator integration and an
independent reviewer were NOT RUN. Fresh macOS system sampling on decoder
release binaries failed with return code 255; prior whole-process samples
cannot attribute timed-only cost. No schedule was rerun to seek favorable
noise. The earlier Git index-lock denial was recorded once and no worker
retry was made; commit and push provenance for round 3 is pending. No detached
children remain.

Exact backend variant and monetary cost are unknown; model family GPT-6 is
known. Supervisor status recorded round-1 input/output tokens
11,407,444/49,899 and round-2 16,894,158/66,737, with most inputs cached;
round-3 usage is unavailable until the supervisor closes it. These counts
are usage, not a computed price.

The first-pass queue is exhausted early. The concrete resume condition is a
reachable, published M6 patch/decision for exact local replication, or a
separately committed, qualified measurement revision for one specific
profile-supported target. Recheck M6 branch/main and patch/harness hashes
before any future implementation or timing. Do not repeat the failed rank,
update or decoder schedules unchanged. The [blocked note](BLOCKED.md) and
[handoff](HANDOFF.md) record this early stop.
