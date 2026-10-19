# M6 LOOKUP-001 — dual-primary REJECT / source NONE

Hypothesis **M6-LOOKUP-PHYSICAL-001**: decode a found member score at its existing
physical slot and compute logical position only when requested. The memchr tag scan,
full hash/length/member checks, allocator and packed layout remain unchanged.
Both population steps used three **sequential passes by one worker**, not independent
agents. Visible backend Codex/GPT-6 family; exact serving model and token cost unknown.

| Variant | 100K median / block range | 1M median / block range | Decision |
|---|---:|---:|---|
| A | -1.328% / -2.646..+0.333% | -0.407% / -3.083..+3.568% | REJECT dual primary |
| B | -4.800% / -6.243..-3.482% | +0.428% / -3.926..+5.681% | REJECT dual primary |
| C | -1.095% / -1.662..-0.320% | -1.389% / -3.241..+2.396% | REJECT dual primary |

Negative effects mean less elapsed time. **B is a 100K exploratory lead only**: all
six blocks reduce time by3.48–6.24%, versus maximum0.745% same-cell A/A. Its1M blocks
range−3.93..+5.68%, with maximum4.184% A/A. No candidate passes both declared primary
cells. Keep all patches; do not relabel100K as the sole primary, rank noisy1M effects,
or call B a broadly safe optimization. An exact B/M6-to-M1 replication is NOT RUN.

No candidate enters the adoption shortlist. No fresh confirmation, candidate profile,
full candidate guard matrix or independent review was run. A separate preregistered
100K-scoped experiment could revisit B with qualified controls, both-host replication
and all retained guards. This observation does not authorize adopting the patch.

Batch-average ns/op (minimum / median / observed range), all12 side observations per
variant/cell. These describe complete timed batches, not individual-operation latency.

| Variant / size | Baseline A ns/op | Candidate B ns/op | Owned memory change |
|---|---:|---:|---:|
| A / 100000 | 43.702 / 44.468 / 43.702–45.204 | 42.583 / 43.750 / 42.583–45.170 | 0.000% |
| A / 1000000 | 123.310 / 127.587 / 123.310–133.041 | 124.459 / 126.977 / 124.459–135.448 | 0.000% |
| B / 100000 | 43.425 / 44.539 / 43.425–45.412 | 41.409 / 42.152 / 41.409–43.538 | 0.000% |
| B / 1000000 | 123.877 / 128.030 / 123.877–133.168 | 123.139 / 126.336 / 123.139–144.793 | 0.000% |
| C / 100000 | 43.696 / 44.200 / 43.696–45.217 | 43.228 / 43.627 / 43.228–44.500 | 0.000% |
| C / 1000000 | 125.035 / 129.076 / 125.035–136.130 | 124.454 / 128.923 / 124.454–132.647 | 0.000% |

Source/referee/profile freeze published **e18d69d0**, chair **e1f3b73c**, and validated
candidate freeze **94e4e897** before comparison. Exact hashes and fixed operations are
in [comparison-freeze.json](comparison-freeze.json), [implementation-manifest.json](implementation-manifest.json),
and [freeze.json](freeze.json). Separate copied0/A/B/C sources/builds were used after
the previously recorded Git worktree denial; no retry or permission changes.
Apple Clang21 C11 O3, no LTO, identical frame-pointer/assertion/hash/allocator options.
Release control instruction text exactly matches the calibrated binary despite build-ID
differences. Timing serial with no compilation, tests or profiles overlapping.

Baseline calibration30 rows; six-block ABBA controls48 rows; fixed six-block discovery
144 rows. Seeds1/2/3 repeated with deterministic cell/variant rotation. All rows retained.
A/A100000: qualified=True, max absolute=0.744507%, shortest=48.877ms.
A/A1000000: qualified=False, max absolute=4.183806%, shortest=50.120ms.

Discovery timed work 7.358168s; setup/warmup/correctness outside timer.
The controls fail at1M; exploratory comparison cannot support fine acceptance. No
noise diagnostic/repeated calibration schedule was run. All memory observations match.

Baseline profiling/census is in [PROFILE-DIAGNOSIS.md](PROFILE-DIAGNOSIS.md). Hit PC
regions identify existing memchr/leaf work; they are not unbiased time shares. Two
miss captures fail minimum25samples and remain insufficient. Round3 interruption
and original assertion/logs preserved; round4 resumed only four unrun profiles.
The concrete new mechanism comes from release assembly showing a physical→logical→
physical round trip. Candidate leaf functions have161(control)/153(A)/151(B)/153(C)
instructions and retain memchr/memcmp. Static changes support code identity only;
there is no candidate profile validation or causal attribution for B timing.

All4 sources pass43 upstream tests per native/sanitizer build,20 public size/length
hit/miss cells per build, and private4160-cell/515840-check exact-bit/output oracle
per build. Oracle covers widths0..64, shifts0/3, both orientations, signed zero,
colliding tags, missing members and all four optional-output combinations. Deliberate
reversed-base and logical-position faults are detected. No original checks weakened.
Required100K long-key/mixed/batch1/16 timing and all-operation mutation/memory guards
remain NOT RUN on candidates. Only arm64 little-endian execution; no portability claim.

[Audit](final-audit.json) PASS: 222 reconstructed rows, 48 effects, three reconstructed patches,
524 serial command windows and216 matched referee files. Baseline nine launcher file hashes
remain identical. Last experimental child02:33:28 UTC. Review in[review.md](review.md)
is sequential by this worker, not independent confirmation/adversarial review.

Reproduce from the frozen host commit in the repository root into fresh output paths.
The existing output has write-once guards and must not be overwritten. Driver phases:
run.py prepare/faults/census/profile (partial profile resume documented separately),
run.py calibrate/qualify; implement.py; compare.py validate; faults-codegen.py;
compare.py discover; audit.py. Exact completed commands and time boundaries are in
commands.jsonl and candidate-commands.jsonl. Original profile driver minimum assertion
is preserved; resume-profile.py salvages insufficient rows without rerunning captures.

Host identity is launcher-verified Apple M6 / arm64 / macOS27 /12 cores. Worker sysctl
denied previously, not retried. Frequency/DVFS/performance-core residency/migration/PMU
remain unknown. Public sampler only; no external attach retry or permission changes.
Cached M1 published4c48fa7e inspected at round4; it chose lookup scanner NONE with a
different referee hash. No timings pooled or remote results inferred. Prior DNS failure
retained; no fresh fetch. Coordinator alone commits/pushes. No baseline src adoption.
