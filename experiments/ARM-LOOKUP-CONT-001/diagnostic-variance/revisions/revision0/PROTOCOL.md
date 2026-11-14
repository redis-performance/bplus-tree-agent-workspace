# Baseline variance diagnostic protocol

Status: PREPARED, NOT ADMITTED. This document authorizes no execution. The controller and an independent reviewer must approve the exact collector, this protocol, operational isolation record and diagnostic review record before any fleet action. H2 and Q4 remain PARK. This is a new diagnostic question, not a qualification retry or candidate screen. No candidate, source modification, build, alternate event set or acceptance path exists here.

The design follows [the independent proposal](../DIAGNOSTIC-VARIANCE-PROPOSAL.md). Original referee files and collectors remain unchanged. The new collector imports `fleet_profiler_off_qualification.py` only after checking SHA256 `531bbabc2b50e26737a0be44773e7d195fa2576ba149e75bdf63a1a5698da743`. Its immutable source/referee/ELF checks, operational record validation and live isolation checks are reused. No Q4-PASS prerequisite is used: the failed Q4 result stays failed.

## Fixed identity and sequence

| Item | Frozen identity |
|---|---|
| Baseline source | `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9` |
| GCC15/LTO ELF | `77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb` |
| Lookup referee | `1e6dc19c9b0f49abafb75c67e3434a87cc6d7d5222049c90a68368755c2a5827` |
| Phase | `diagnostic-variance-43` |
| Perf | `/usr/lib/linux-tools/6.14.0-1010-aws/perf` |
| Launcher | `/usr/bin/taskset` |
| Locale policy | `LC_ALL=C`, `LANG=C`, enforced in each child environment |

The source pin is checked through the imported Q4 collector and diagnostic review. Both original baseline ELFs and all original referee files remain pinned through Q4 identities, although only the target baseline executes.

Atomically create the phase directory before admission checks. Any existing phase directory rejects the attempt; any failed/partial attempt consumes it. No resume, overwrite, retry, seed selection or capture replacement.

1. One support/model capture: `verify hit 43 1`.
2. Only if that passes, D0, D1, D2, D3 in that exact order, each `measure hit 43 250000`.
3. Stop on the first failed support, identity, isolation, exit, model, parser or scheduling gate. Retain the completed prefix and failed attempt. No subsequent child runs.

Each full capture reports 125,000,000 operations and hits, score sum zero, positive inner elapsed time, and exactly 14,272 tree-owned bytes. The support probe must report verified=true, 500 members and the same fixed memory. These values come from the frozen workload/model and retained Q4 verify output, not the first new observation. There is no 250ms qualification or ±1% A/A calculation in this diagnostic; duration remains a model/interpretation field. Four uneventful captures finish with no variance episode characterized and no authority for more runs.

## Exact capture and output contract

The event argument is one strong group followed by five software events:

```
{cycles:u,instructions:u,branches:u,branch-misses:u},task-clock,context-switches,cpu-migrations,minor-faults,major-faults
```

Each capture uses the fixed command shape:

```
PERF stat -vv --no-scale --no-big-num -x, -e EVENTS -o STAGE.counters.csv -- /usr/bin/taskset -c 2 ROOT/bin/gcc15-lto/lookup MODE hit 43 COUNT
```

`PERF`, `EVENTS`, `MODE`, `COUNT` are precisely those above. No weak grouping, substitution, event splitting, interval mode, repetition, delayed attach, CPU-wide collection or scaled reconstruction. The single support probe is the only support attempt. Unsupported software runtime fields end the diagnostic INCOMPLETE.

Python's child pre-exec function sets and verifies CPU0 before perf exec. The parent records a real live affinity observation when available; an exited-process race is explicitly unavailable, never a fabricated observation. Perf stays on CPU0. Its taskset child starts on CPU0 and explicitly constrains itself to CPU2 before baseline exec. The process counters therefore include taskset startup and the intentional migration. The baseline affinity claim is the pinned taskset contract; the collector does not invent an observed benchmark PID. This differs from Q4's child-before-taskset CPU2 contract.

The benchmark JSON goes to `STAGE.stdout`. Perf stderr/debug/errors go to `STAGE.stderr`. Counter CSV and perf verbose raw reads go to `STAGE.counters.csv` via `-o`. All are retained byte-for-byte. Launch argv, exact locale overrides, return code, start/finish audit timestamps, wrapper affinity guarantee/observation, wall duration and wrapper rusage are recorded separately. No environment dump or process credentials are retained.

Pre/post each capture, validate collector/protocol/review, original sources/referees/ELFs, perf/taskset hashes, kernel release, lease hash, saved coordinator identity, both cleanup timers and target ExecStart pins, exact reviewed timer schedules, cleanup artifacts, controller CPU0/workload CPU2 policy, no Docker, and Parca service exactly inactive/dead/MainPID0 with no remaining matching processes. Q4 isolation redacts matched process arguments. Preserve every raw check. Tool-version metadata is also bracketed by identity/isolation checks and checked against reviewed stdout hashes under the same locale policy. Root supplies the live tool/kernel pins and operational record; preparation does not claim they are valid.

On a capture exception, signal its process group only while `proc.poll() is None`, then reap. A reaped child is never signaled. External cleanup retains control-group responsibility for orphans and must prove owned work reaped before coordinator restoration.

## Parser gates and precision

The pure `parse_counters` function accepts exactly nine unique required events. Each CSV row must have count, unit, exact event name, positive integral runtime, and literal `100.00` running display. Extra/duplicate/missing events, nonfinite/negative values, unsupported/not-counted markers, missing runtimes and changed units fail. Hardware counts and software integer events must be integral. Task-clock is milliseconds. Zero cycles, instructions or task-clock fails; zero branch misses/switches/migrations/faults is valid. Hardware group runtimes must match exactly. Optional metric columns and recognized elapsed/user/sys footers are retained or ignored as formatting, not used to reconstruct counters.

Linux v6.14 `read_counter_cpu` emits `EVENT: CPU: RAW_COUNT TIME_ENABLED TIME_RUNNING` at verbosity >1 through `stat_config.output`; `-o` selects that output file. The parser removes only this recognized grammar before parsing CSV. The CPU-map entry must be `-1` for this process collection, raw event reads must be unique, and enabled=running=CSV runtime must hold. Unscaled integral raw counts must match CSV counts; task-clock raw count uses nanoseconds while CSV is rounded milliseconds, so that count is retained in raw evidence but is not equated across units. Recognized reads on stderr are also validated and cannot duplicate reads in the counter file. Unrecognized explicit event-read/timing output fails; it cannot become silently missing precision.

If the installed binary does not expose raw enabled/running values, the parser reports them unavailable and accepts only the registered literal100.00 display gate. Display100.00 is rounded scheduling evidence, not proof of unrounded equality. The single live support probe must pass the frozen parser; there is no adaptive parser retry on a failed phase.

Primary source provenance, inspected without executing perf:

- [Linux v6.14 builtin-stat.c](https://github.com/torvalds/linux/blob/v6.14/tools/perf/builtin-stat.c), fetched file SHA256 `8b833c274bb6a6d57e3dc11c3a785d9786cc5e77131df6af78d8832db456300c`: raw verbose grammar/output routing and `-o` binding.
- [Linux v6.14 stat-display.c](https://github.com/torvalds/linux/blob/v6.14/tools/perf/util/stat-display.c), SHA256 `6fce94c09f0fdc3d57d5a9e6746b76f68a8402f470f325abb774c9d64031e722`: CSV runtime and two-decimal running percentage.
- [Linux v6.14 debug.c](https://github.com/torvalds/linux/blob/v6.14/tools/perf/util/debug.c), SHA256 `409226b199327e88d907a3c6534a314ec1e3cacb5f0c65e82c814b246846e38b`: diagnostic debug stream.

These are primary source references, not proof that the installed distribution binary is byte-identical to upstream. Root must pin that executable and its version; current event support remains unknown until an independently admitted probe.

## Scopes and analysis

`describe` requires exactly D0–D3, all model-valid. It reports all nine event counts, inner elapsed and wrapper wall min/max/median and fractional range over median, with unavailable fractional range for a zero median. Per-row derived fields are user cycles/instruction, branch misses/branches (unavailable for zero branches), minor+major faults, and task-clock milliseconds converted to nanoseconds divided by perf-wrapper wall duration.

User hardware counters cover the measured taskset/baseline process, including startup/setup/warmup/loop/exit, and exclude kernel execution. Software task-clock and scheduling/fault events keep their normal process scope. Perf-wrapper wall starts before Popen and ends after wait. Parent RUSAGE_CHILDREN deltas include perf plus descendants, so they are not Q4 baseline-child rusage. The task-clock/wrapper-wall ratio is a scoped audit ratio, not exact workload occupancy or core frequency. No instructions/op is labeled pure lookup cost.

No row exclusion, A/A pairing, effect threshold, causal label, inferred confidence interval, tail-distribution claim or acceptance follows from these four captures. Interpret only newly observed descriptive differences; these counters cannot reconstruct the earlier Q4 failure. H2/Q4 stay PARK irrespective of result. A later condition change or qualification would need separate evidence and review.

## Diagnostic review record

Strict admission consumes a separately reviewed JSON with these required fields. Every SHA256 is the full lowercase64-character digest; substitute actual reviewed values before approval, not placeholders. Pass its exact byte hash separately as `--review-sha256`.

```json
{
  "schema_version": 1,
  "decision": "APPROVED",
  "reviewer_role": "independent reviewer",
  "collector_sha256": "<new collector>",
  "protocol_sha256": "<this protocol>",
  "q4_collector_sha256": "531bbabc2b50e26737a0be44773e7d195fa2576ba149e75bdf63a1a5698da743",
  "isolation_sha256": "<reviewed operational record>",
  "q4_review_sha256": "<review binding Q4 collector to that operational record>",
  "perf_path": "/usr/lib/linux-tools/6.14.0-1010-aws/perf",
  "perf_sha256": "<installed perf>",
  "perf_version_stdout_sha256": "<exact LC_ALL=C perf --version stdout>",
  "taskset_path": "/usr/bin/taskset",
  "taskset_sha256": "<installed taskset>",
  "taskset_version_stdout_sha256": "<exact LC_ALL=C taskset --version stdout>",
  "kernel_release": "<exact release>",
  "locale_policy": {"LC_ALL":"C", "LANG":"C"},
  "events": "{cycles:u,instructions:u,branches:u,branch-misses:u},task-clock,context-switches,cpu-migrations,minor-faults,major-faults",
  "baseline_sha256": "77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb",
  "source_sha256": "16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9"
}
```

The inherited isolation schema and its independent Q4-collector binding are unchanged. That binding approves isolation-code/record compatibility, not Q4 results or execution of a candidate. The new diagnostic review is an additional required gate. Exact new collector/protocol/review pins are checked before and after every child; phase claims remain consumed on any failure.
