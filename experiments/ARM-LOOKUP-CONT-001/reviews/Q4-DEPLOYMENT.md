# Independent Q4 deployment review

**APPROVED for the exact v2 deployment and baseline-only Q4 sequence.** This approval binds the immutable isolation record, collector, cleanup, lease generation and saved restoration policy below. It permits the controller to proceed with the preregistered profiler-off qualification after its live preflight succeeds. It does not select a source, admit a candidate, or change H2's PARK/NONE disposition.

The reviewer did not implement the Q4 collector, cleanup or staging scripts. The reviewer identified defects and requested the retained fixes, independently inspected the final code and staged evidence, reran the18 offline collector tests, and exercised six additional actual cleanup restoration-method branches through entirely mocked operations. Prior authorship of the Intel profile parser and H2 readiness/final audits is disclosed; none is an independent second implementation of Q4. No live fleet query, service operation, process signal, workload, performance collection, source change or publication was performed by this reviewer. Detailed backend accounting remains private; exact model, token and monetary costs are unknown.

## Exact approved identities

| Artifact | SHA256 / identity |
|---|---|
| v2 isolation record (private retained evidence) | `1b22ec08fa256b91e341c2628f4baef9c6d7ac055376abeda4a995057e827674` |
| [Deployed collector](../fleet_profiler_off_qualification.py) | `531bbabc2b50e26737a0be44773e7d195fa2576ba149e75bdf63a1a5698da743` |
| Deployed cleanup (private retained evidence) | `7bd7d2437743bb2cbb6bc290c6ae4a556f09e41b38d2deeaa984516a7edf3c35` |
| Owned reservation (private retained evidence) | `57f396c449d78ed7280de777e2ccc5b2d6a4be0b2d5d558e331b86e956256a92` |
| Lease generation | `101e50d5b44349ff83740e0e9e446d35` |
| Upstream source commit | `ee8e7f70152404649ac947157fd662d11b4a00d5` |
| Frozen C source | `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9` |
| Original ARM GCC15/LTO lookup ELF | `77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb` |
| Original ARM native lookup ELF | `2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf` |

All file hashes above were independently recomputed. The collector's complete source/referee pins and both saved original ELF byte hashes also match. The new lease adds generation and restoration fields to the saved original lease without changing its coordinator identity, owner or deadline. The v2 saved lease equals the staged reservation byte content after parsing. The collector's actual `validate_record` accepts the concrete v2 record and this review's binding fields.

## Recovery schedule and rejected staging

The original staged schedule was **rejected before Parca stopped or any Q4 workload ran**. Its primary fired07:19:00 and its backup approximately14.934seconds later, each with a180-second runtime limit and15-second stop allowance. Because both cleanup invocations serialize on a lock, a stuck primary could exhaust the backup's runtime while it waited. Those original artifacts remain under Q4-staging (private retained evidence); no approval record was issued for their isolation hash `ee2169ce6e757a4ba885a94afdfee2787138b965f9cd523871cc469501aed018`.

The v2 deployment (private retained evidence) corrects this without changing reviewed source bytes. Both replacement timers were created and checked active before their predecessors were retired. Successful creation records, the staging/restaging controller source and completion capture agree with that order. Original resume-only timers and the first Q4 timer pair are recorded inactive after their respective replacements were armed; the original cleanup helper was not overwritten.

| v2 recovery path | Fire time, UTC2026-11-14 | Runtime / start timeout | Stop allowance | Fire + runtime + stop |
|---|---|---|---|---|
| Calendar primary | 07:12:00.000 | 180s /180s | 15s | 07:15:15.000 |
| Monotonic backup | 07:15:29.780362 | 180s /180s | 15s | 07:18:44.780362 |

The owned lease ends07:20:00. The209.780362-second separation exceeds the primary's180+15seconds by14.780362seconds. The backup then has its own complete recovery window, with75.219638seconds remaining before lease expiry. Both timers have1microsecond accuracy, zero randomized delay and `KillMode=control-group`. Their target services were inactive with MainPID0 at capture.

I independently parsed the retained numeric busctl values and reproduced the calendar epoch and monotonic-to-wall conversion from the retained realtime/monotonic anchor and boot identity. The resulting fire epochs equal both deployment and isolation records. The tiny sequential clock-read offset is not confused with a sampled workload time. Both exact realtime/monotonic display strings are bound in the isolation record; the collector checks those strings and a300-second live fire margin before and after every child. The earliest primary therefore also imposes the earlier operational cutoff.

Each timer targets the recorded cleanup service. Each retained ExecStart contains exactly one command: taskset CPU0, Python3, the canonical plain `cleanup-q4.py`, and the exact `--lease-generation=<approved generation>` argument. I independently parsed both argument lists and recomputed their ExecStart hashes. These match the isolation record. No old-helper target, alternate generation, extra command or unreviewed executable appears in those entries.

## Restoration and failure behavior

The saved service is active/running with empty CPUAffinity and AllowedCPUs policy. The final staging capture remains active/running with the same main process and policy. Its41 observed threads all allow CPUs0–95; the earlier39-thread observation was not a fixed count or a CPU0 affinity guarantee. No service configuration was changed by staging. The full saved policy and unrestricted CPU list are mandatory lease fields for the reviewed cleanup generation.

Cleanup acquires a file lock, rejects the wrong owner/generation or missing restoration record before actions, stops the owned work unit, and checks its cgroups and surviving root-associated processes. Container removal is limited to the exact owned bind root. Only same-generation reviewed cleanup invocations are excluded from survivor checks; ambiguous surviving processes prevent coordinator resume. The coordinator signal uses a pidfd bound to the process opened before its expected start ticks are checked. Numeric PID reuse therefore cannot redirect SIGCONT to a replacement process. Bounded polling checks the resumed identity/state.

Restoration starts the saved Parca service and checks active status, canonical service cgroup, unchanged unit policy and every observed thread's saved unrestricted affinity. A failed work stop prevents coordinator resume. Partial failure remains `RELEASE_INCOMPLETE`, with recorded errors and retryable restoration; RELEASED is written atomically only after both recovery obligations succeed. The serialized backup has its own time budget under v2. All subsequent reservation writers must preserve the generation/locking discipline; this approval does not cover replacing the lease or repointing timer units.

The existing eight orchestration tests and eight LiveOps tests cover generation/owner rejection, missing restoration metadata, retry/idempotence/race behavior, pidfd identity changes, relative-cwd/cgroup survivors and exact-container ownership. The reviewer's six additional fully mocked restoration tests exercise delayed readiness, policy mismatch, missing threads, wrong affinity, missing cgroup and start failure. They are correctness evidence, not demonstrations that a live cleanup has already run. Actual restoration still requires its post-run proof.

## Baseline-only collection and remaining runtime gates

The frozen collector has a single-use overall claim and fixed sequence: target seed43, target seed29, target seed17, native seed17. There is no phase/seed/count/binary selector and no candidate execution path, including verification. Each cohort verifies its six baseline cases and attempts the complete72-row ABBA grid; at most288 measurement rows exist. A failed/partial cohort consumes the attempt and prevents later cohorts. No retry, row exclusion or threshold relaxation is admitted.

The pure analyzer checks exact model, row schema, grid order, immutable identities, exact case memory, duration≥250ms and integer arithmetic for the±1% A/A boundary. I independently reran all18 offline tests, including wrong/missing/duplicate/nonfinite/model/hash rows, threshold edges, single-use claims, actual isolation branches with fake proc/sys trees, timer/lease/coordinator/service failures and argument-redaction checks. No real command or workload was used by those isolation tests.

Before and after every actual child, runtime admission must still validate the exact collector/record/review/cleanup/source/ELF hashes, unchanged owned lease, identical paused coordinator, both active reviewed recovery schedules/targets, CPU0 controller, CPU2 workload, no Docker work and exact inactive/dead Parca state with no remaining detected processes. The preexec path sets and verifies CPU2; an unavailable parent observation after a fast exit is labeled honestly and cannot excuse a failed child. Profiler command lines are inspected only for detection and never retained in evidence. Resource diagnostics cover the whole sole child outside the frozen inner loop and do not replace its elapsed-time metric.

The controller must retain the admission review and its hash, perform the service stop itself, and preserve the collector's failed/partial captures. No builds, profiling, archive transfer or consultation may overlap Q4 on the runner; archives are fetched only after the entire work unit is inactive. This approval is based on saved staged evidence, not a live query by the reviewer, and does not replace these immediate checks. A stale or changed concrete record requires re-review.

Q4 measures baseline qualification under the changed isolation condition. It does not prove that Parca caused the old H2 control failure. H2 remains PARK/NONE, and any H2R1 needs a new admission and all required comparisons, confirmations, affected-operation guards, profiles and final review. ARM Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and all child pipeline categories remain unavailable; no TMA or candidate profile is part of this admission review.

The reviewer's own tool discovery found no callable cpu-perf endpoint. The controller's actual Q4 consultation is shared evidence, with limited coverage and no retrieved causal proof; no new consultation is claimed here.
