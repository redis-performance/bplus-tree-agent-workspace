# Baseline variance diagnostic final independent review

**INCOMPLETE at the single support capture; attempt consumed. Zero D0–D3 captures. Selected source remains NONE; H2 and Q4 remain PARK.** The frozen parser rejected the actual perf output. No parser rewrite, replacement capture, retry, new deployment or qualification is authorized by this review.

This reviewer previously approved the collector's exact code/record binding in [VARIANCE-CODE.md](VARIANCE-CODE.md) and authored earlier Intel offline parser hardening. The diagnostic collector has a separate implementer. This final review independently inspected saved artifacts and ran only the existing pure parser against saved text; it made no fleet query, perf/workload execution, build, source edit or publication. The earlier approval and all failed-attempt bytes remain preserved. Its source-format review was incomplete, as described below; the live support requirement correctly prevented full captures.

## Exact outcome and stop

The retained launch, child-start and completion logs each contain exactly one matching support entry. Its exact command is the registered perf stat configuration, strong four-event user hardware group plus five software events, `-vv --no-scale --no-big-num -x,`, followed by taskset CPU2 and the unchanged target baseline `verify hit 43 1`. The recorded locale is C. The process returned0 and stdout exactly reports verified=true, hit, seed43, 500 members and14,272 owned bytes. Perf pre-exec CPU0 verification and an available parent observation of affinity[0] agree; baseline affinity remains the pinned taskset contract, not an invented direct PID observation.

The frozen parser fails with exactly `Missing runtime/running field or unsupported CSV schema`. Independently feeding the unmodified saved counter/stderr text into that parser reproduces this error. The result records failed_stage=support, completed_captures=0, attempt_consumed=true, qualification=false and source_adoption=false. No D0–D3 launch, command, output, validated support file or four-capture analysis exists in the fetched attempt directory. This is a failed diagnostic compatibility gate, not a failed workload model or a qualified performance result.

## Two format assumptions missed before execution

The counter file contains nine process-map raw reads of the expected `EVENT: -1: COUNT ENABLED RUNNING` form, followed by **nine additional aggregate reads** of `EVENT: COUNT ENABLED RUNNING`, then nine CSV event rows. The parser recognized only the first raw form. The first aggregate line therefore reaches the CSV field-count check and causes the recorded failure.

The matching Linux v6.17.13 [perf_stat_process_counter implementation](https://github.com/gregkh/linux/blob/v6.17.13/tools/perf/util/stat.c) emits the aggregate form for global aggregation at verbosity greater than zero. This path was omitted from the earlier source review, which traced the per-map read and output routing. Independently retrieved util/stat.c SHA256 is `7f26e47ec068270e558cb11fac36b3c719ad4a5868e5de515b6cd49efd3b73eb`.

Separately, the exact admitted command's task-clock CSV row contains raw value952521 and an **empty unit**, matching the raw nanosecond count, rather than the parser's required milliseconds/msec schema. This second mismatch is directly observed; the review has not independently traced the source path selecting that scale/unit for this invocation. The prior fractional-scale rounding analysis does not establish that this invocation takes that display path. Removing aggregate lines would therefore not establish compatibility either, and no such altered input is substituted for the failed evidence.

Manual structural inspection finds nine unique events in each of the per-map, aggregate and CSV sections, corresponding count equality, enabled=running=CSV runtime952521ns, and displayed100.00 throughout. These observations describe the rejected support output only. They do not retroactively pass the frozen parser, prove full-capture scheduling, or supply four-capture statistics. The synthetic fixtures and the prior independent review missed both actual-output forms; 30 passing offline tests did not establish installed-tool compatibility.

## Identity, isolation and collection joins

Independent hashes join the deployed collector and review bytes, deployment launch pins, admission and metadata to collector `2a5b4b1fbea98ca40bd03ccb7d5f453d0acaac743cfd9e6fd9884d3276b9004e`, protocol `ac5c835a44c9885e23078bb5fc6cb7f197882aa6aebe64b49ec0b722f5170d19`, and diagnostic review `91e6fc60733642d6762bee2bc59b5eeb2e2b319f9ee367510905d0347809c8a6`. The imported isolation collector, saved isolation record and earlier independent isolation review retain their approved hashes. The saved target ELF independently hashes to `77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb`; frozen source/referee files match every metadata pin, including baseline source `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.

The two metadata commands returned0 with empty stderr and exact reviewed version-stdout hashes. Recorded tool/kernel pins match the review: perf6.17.13, taskset2.39.3, kernel6.14.0-1010-aws. Installed tool ELF hashes remain the controller's saved live capture and collector checks, not independently fetched executable bytes. The collector checks identities before and after metadata and support; successful progress through support-post establishes those code gates passed, but the output is not a separate continuous identity attestation.

All five retained isolation snapshots pass: deployment preflight, metadata pre/post and support pre/post. All30 associated operational commands returned0 with empty stderr. Independently checked raw outputs match exact timer targets/schedules and cleanup ExecStart hashes; lease/timer margins exceed the required300seconds. Snapshots retain the same paused coordinator identity, controllerCPU0, CPU2 online with expected sibling set, and no profiler matches. Service outputs are inactive/dead/MainPID0 with empty CPU policies; Docker outputs are empty. These are bounded snapshots, not proof that no unrelated activity occurred between them.

Support command timestamps span04:39:08.199370–04:39:08.217785UTC; support-post checks finish at04:39:08.278160UTC. The recorded wrapper wall and rusage include perf and descendants, while event counts include taskset startup and its known migration. The support verification has no measured-loop elapsed output. None of these scopes may be relabeled as Q4 baseline-child or lookup-only performance.

The fetch receipt is timestamped04:39:54.588864UTC and records the controller's assertion that MainPID was zero twice before retrieval. It is retained owner evidence, not a separately persisted live systemd precondition independently observed by this reviewer. The receipt follows the saved completion/postflight timestamps; no stronger archival non-overlap claim is made. Later service restoration is a separate operational review.

## Preserved evidence and limits

| Retained artifact | SHA256 |
|---|---|
| Support counter output | `49842751d32c57e9997c4edaf6482298a09979af24ca7af6c1075fadefb2b797` |
| Support stderr | `0a3d5a2317903128278e503bc1c3d72dbd319c466670181b2b7f9027ccf7a114` |
| Support model stdout | `2e71309acb0001d49fb7d8a4c918436e32ccdf12f0a477962931af66c57f7229` |
| Final result | `8963becba637763de36fe44e13688361b40e906a7de22d28d290c9e1a4083b90` |
| Command completion log | `cce7571e3c2df9fcfaceca3a2fdaa3e2a7e5a4701837319c466081972abd5c19` |
| Controller fetch receipt | `8e9835d5bcbb5e9f0b29ff908765cfdd8eed920dd97340d5a6fa585feb16b258` |

There are no four-capture distributions, ratios, variance conclusions, causal explanations or acceptance results. This support-only attempt cannot explain the earlier Q4 failure or alter either PARK disposition. Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children remain unavailable; these events are not qualified TMA. The diagnostic is not another population, replication or qualification attempt. Any future work requires a separately proposed and independently reviewed scope; this failed phase remains consumed.
