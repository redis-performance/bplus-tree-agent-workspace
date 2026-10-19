# M6 morning report — interim, core queue complete

Updated 19 October 2026, round 10. Campaign authorization ends 08:00 UTC / 09:00
Lisbon; no experiments after 07:15 UTC. Source selection **NONE**. The core queue
has no contender eligible for confirmation. A separate operator-owned trial
is preregistered in [006-followup](006-followup/PLAN.json). Its chair selected
M6-LOOKUP-CALLER-001 after three actual independent proposals; implementation
preparation is recorded, with no measured result yet. This does not change the
completed core decisions.

The launcher-selected [baseline-attempt002](baseline-attempt002/SUMMARY.md) is
complete: 120 serial processes, 960 rows, 40 cells and 162.423 seconds of timed work.
Native/sanitizer validation passed before those measurements. Four cells satisfy
both strict A/A and minimum-duration rules; 14 have a window below 10 ms. The
launcher-selected baseline and earlier failed attempt are preserved without reruns.

| Target | Observed finding | Decision and M1 action |
|---|---|---|
| [Rank](002-rank/RESULTS.md) | All six 100K blocks regress for A/B/C; median +3.81/+3.42/+3.87%. 1M signals lie within failed controls. | REJECT / NONE; skip exact shorter-side policies. |
| [Update](003-update/RESULTS.md) | 100K medians +0.08/+1.69/+1.99%; 1M medians −7.70/−8.76/−9.27%. Both controls fail. | REJECT dual primary / NONE; 1M transient-packing lead only. |
| [Lookup](004-lookup/RESULTS.md) | B at 100K −4.80% median, blocks −6.24..−3.48%, qualified control. At 1M −3.93..+5.68%, failed control. | REJECT dual primary / NONE; 100K lead only. |
| [Decoder](005-decode/RESULTS.md) | B/C count-one median approximately −30%; every policy repeatedly loses on required uncapped, qualified larger-range guards. | REJECT universal policies / NONE; helper mechanism lead only. |
| Iterator | Optional slot used by decoder. | SKIPPED; do not add a second optional target. |
| Fresh confirmation | No discovery survivor. | NOT ELIGIBLE. |

Effects are elapsed batch-average candidate/control differences; negative means less
time. Ranges describe observed blocks, not confidence intervals or individual-query
latencies. Leads are scoped observations, not accepted improvements. The decoder
compares a count-one scalar policy against frozen EXP-007 B bulk decoding; it is
not a public iterator or whole-tree speedup. Count-one inputs are seed-invariant.

Rank summation visits fewer logical terms but grows code and loses at 100K. Update
packing failures identify a transient path whose 1M reduction does not transfer to
100K. Lookup assembly exposes a physical/logical slot round trip; B's 100K timing
has no candidate profile establishing causality. Decoder caller dispatch improves
count one while changing larger-range generated code and timing. These findings
retain useful mechanisms without weakening their preregistered objectives or guards.

## Identity and reproduction

Host: launcher-verified **Apple M6**, arm64, macOS 27, 12 physical/logical cores,
Apple Clang 21.0.0. [Launch manifest](launch-manifest.json) records metadata provenance
and nine source/referee hashes. Direct sysctl was denied previously and not retried.
Frequency, DVFS, performance-core residency, migration and PMU observations remain
unknown. Each comparison keeps its allocator, hashing, assertions and flags identical;
release timing uses C11/O3 without LTO, never sanitizer binaries.

The source bytes remain the extraction pinned by `e52c26c4`; the launcher baseline
manifest records Git revision `f7a8446d`. Later referee/publication revisions retain
those source bytes. Per-target identities below include exact source, patch, referee
and binary hashes; all three losing patches for each target remain available.

| Hypothesis | Acknowledged comparison publication | Exact identity and commands |
|---|---|---|
| M6-RANK-SHORTER-001 | `3102530f` | [freeze](002-rank/comparison-freeze.json), [implementations](002-rank/implementation-manifest.json), [commands and limitations](002-rank/RESULTS.md) |
| M6-UPDATE-REPACK-001 | `a9e16781` | [freeze](003-update/comparison-freeze.json), [implementations](003-update/implementation-manifest.json), [commands and limitations](003-update/RESULTS.md) |
| M6-LOOKUP-PHYSICAL-001 | `94e4e897` | [freeze](004-lookup/comparison-freeze.json), [implementations](004-lookup/implementation-manifest.json), [commands and limitations](004-lookup/RESULTS.md) |
| M6-DECODE-COUNT1-001 | `6e9e4ec8` | [freeze](005-decode/comparison-freeze.json), [commands and limitations](005-decode/RESULTS.md) |

Raw rows, calibrated fixed operation counts, checksums, six-block ABBA effects,
owned-memory observations, profile diagnoses and audits are linked from each result.
For a new host reproduction, use the acknowledged revision plus exact hashes, fresh
isolated source/build/output directories and a separately frozen deadline. Archived
drivers contain write-once guards and expired deadlines; the historical commands
are not instructions to rerun into these evidence paths. Large raw profiles and
full local build artifacts remain in ignored scratch with recorded checksums.

## Other host and remaining limits

Cached M1 branch revision `4c48fa7ed2d8cf4f1144626276bfb2a602c63bf9` is context only.
No fresh remote refresh was attempted after the recorded DNS failure. Exact M1
replication of these M6 patch/harness pairs is **NOT RUN in that cached revision**;
current remote state is **UNKNOWN**. No rows are pooled.
M1 Clang 17 versus M6 Clang 21 is an additional cross-host confounder. M1 should
skip the rejected exact policies for their original objectives; any distinct
follow-up requires its own preregistration and guards.

All four completed M6 populations used sequential passes. Fresh independent timing
confirmation, independent adversarial review, full candidate performance guards and
selected-candidate profile validation remain absent. Lookup has two insufficient
baseline miss captures; decoder has three insufficient guard captures and 41 capped
cells. Decoder A/B/C phases were successive, not rotated across phases, so their
small differences cannot support a qualified variant ranking. No noisy or failed
rows were removed. The decoder selection-note filename collision and first failed
audit are retained; executable source/referee freezes match.

[Round 6 reporting review](ROUND-006-REPORT-REVIEW.json) checks all nine launcher
hashes and all 12 retained campaign patch hashes, and reads the previous raw audits
without repeating experiments or whole-evidence inventories. It corrects stale
README next-target wording. This is sequential reporting review, not independent
validation. [USAGE.json](USAGE.json) records supervisor-reported tokens through
completed round 9; current-round usage, exact serving model and currency cost remain
unknown. Token fields retain their original meanings and are not double-counted.

Core queue's last experimental child ended 03:00:37.811992 UTC. Reporting rounds
6–10 launched no worker build, test, profile or timing child. Latest round 9 final
handoff matching ok acknowledgement: **acfba0f86**, request
`r9-final-handoff-20261019T031614204088Z`, checked **03:16:18.805693 UTC** on
`exploration/apple-m6-mini-20261019T013000Z`. Round 10 publication failed; see blocker below;
coordinator alone commits/pushes. Baseline src remains unchanged.

Counts remain 11 completed populations (9 sequential + 2 historical multi-agent),
0 accepted / 6 rejected / 5 parked, 33 patches / 14 harnesses. Operator trial and
concurrent M1 night excluded from completed counts.

Operator owns the preregistered 101-cell **M6-LOOKUP-CALLER-001** trial, deadline
04:40:20.349829 UTC. Three actual independent proposals complete/B selected;
explicit implementation status remains PREPARING. New
[static review](006-followup/review-caller.json) reports A/B/C recorded validation PASS
and equivalent scoreRaw instructions after relocation/assertion-line normalization.
Author C independently reviews A/B, not own C. This establishes no measured effect,
timing freeze, candidate ranking or adoption. The review requires common-relative-path
timing builds to remove validation-path differences in `__FILE__` and placement;
that gate remains operator-owned. [Round 10 checkpoint](ROUND-010-HANDOFF.json)
pins these documents as observed. M1 should await exact published identities and
completed outcome. Worker remains reporting-only without taking over this trial.

Round 10 publication **FAILED**, request `r10-final-handoff-20261019T031850087694Z`,
checked **03:18:50.408944 UTC**. Coordinator error:
`Public-evidence review required: 006-followup/build.json`.
See [failure record](ROUND-010-PUBLICATION.json). Local evidence is preserved;
no worker Git action or same-blocker retry. Operator/coordinator must resolve that
operator-owned metadata before requesting publication again. No performance decision
changes. Latest successful final handoff remains **acfba0f86**.
