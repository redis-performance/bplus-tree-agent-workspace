# Q4 baseline-only collector — prepared for independent review

The separate [collector](../fleet_profiler_off_qualification.py) implements the [Q4 protocol](../ARM-PROFILER-OFF-QUALIFICATION.md). It has not run on any fleet host or executed any workload locally. No source/binary was built, no old collector changed, and no service/reservation was changed. It selects no candidate or source. Original H2 remains PARK/NONE regardless of a future Q4 outcome.

One invocation runs exactly `Q4-lto-43`, `Q4-lto-29`, `Q4-lto-17`, `Q4-native-17`. There is no seed, phase, binary or count override. The immutable original ARM baselines are native `2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf` and target `77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb`. Source remains16def20f… from upstream ee8e7f701…. Every frozen referee/dependency is pinned in the self-contained collector. No candidate executable, including candidate verification, has a code path.

Each cohort executes six original baseline verification processes followed by72 original measurement processes (three ABBA blocks for each case). Native sweeps remain50,000/50,000/100,000/20,000/20,000/20,000; LTO multiplies by5. The original binary alone supplies its1,000-sweep warmup and unchanged inner clock loop. The collector neither rebuilds nor alters it.

## One-shot and analysis rules

`Q4-profiler-off/` is atomically created before operational admission; an existing directory rejects every restart, even if its prior attempt failed or is partial. Each fixed cohort directory is also created exactly once. The only in-memory progression requires complete passing predecessor reports; no resume, phase skipping or manual substitution is supported. A noisy/short/memory-failing complete cohort retains all72 rows and stops before the next cohort. A process, model, source or isolation failure preserves the partial evidence and stops immediately. No row invalidation, exclusion, dropped row or count adaptation exists.

`analyse_rows(phase, rows)` is pure: no files, clock, subprocess, CPU state or environment. It requires the exact ordered72-row grid and exact schema, pins, labels, source/model/counts. Noninteger values, booleans masquerading as counts, NaN/Infinity, missing/extra/duplicate/reordered rows and unexpected fields reject. `read` also rejects duplicate JSON keys/nonfinite JSON constants. Every case must have identical owned bytes across all12 processes. The unchanged referee checks the measured tree-owned endpoint against its pre-loop value internally; collector verification memory may differ before warmup and is not substituted for that measured endpoint.

For each block, let A and B be their two elapsed-nanosecond sums. The exact gate is `100*abs(B-A) <= A`, avoiding floating tolerance at1%. Every duration must be at least250,000,000ns. Floating percentages are reporting only. All raw rows remain part of the decision. Baseline-only B labels represent the same immutable ELF as A, never a candidate.

The root controller will fetch no archives until the entire Q4 unit is inactive. This avoids overlapping transfer with automatically launched later cohorts. Builds, profiling, retrieval and other work remain prohibited on the measurement resource while Q4 runs.

## Reviewed isolation record schema

The controller supplies a UTF-8 JSON `isolation.json` plus its SHA256. Operational paths and real process identities belong in that private record. All values below are schematic; hashes must be actual64-character lowercase SHA256 values. Both cleanup timers can invoke the same cleanup script, so a single cleanup_artifacts entry is valid.

```json
{
  "schema_version": 1,
  "owner": "bplus ARM-LOOKUP-CONT-001",
  "run_root": "<absolute reserved fleet run root>",
  "lease_sha256": "<sha256 of exact reservation.json>",
  "deadline": 0,
  "coordinator": {"pid": 1, "start_ticks": "1"},
  "service": {
    "name": "snap.parca-agent.parca-agent-svc.service",
    "saved_active_state": "active",
    "saved_cpu_affinity": "",
    "saved_allowed_cpus": ""
  },
  "cleanup_timers": ["<primary>.timer", "<backup>.timer"],
  "cleanup_services": [
    {"unit": "<primary-target>.service", "exec_start_sha256": "<hash>"},
    {"unit": "<backup-target>.service", "exec_start_sha256": "<hash>"}
  ],
  "cleanup_artifacts": [{"path": "cleanup.py", "sha256": "<hash>"}],
  "restore_service": true,
  "resume_saved_coordinator": true,
  "reap_owned_children_before_resume": true
}
```

`run_root` must resolve exactly to `--root`. Coordinator PID/start ticks and deadline must equal the saved immutable owned lease. The lease must remain RESERVED with owner as above and at least300 seconds before its deadline at each check. Root will record saved Parca state in the lease before pinning it; any subsequent lease edit, including extension, stops this attempt. Cleanup artifact paths may be absolute or relative to the run root. These paths/hashes bind the reviewed operational recovery, not just declarations in the record.

Each timer must be distinct, active, have a nonempty/nonzero next realtime expiry, and target one of the reviewed cleanup services through its live `Unit` property. Every listed service must be a timer target. Its `exec_start_sha256` is the SHA256 of **exact stdout bytes, including the newline**, from `systemctl show UNIT --property=ExecStart --value`. This representation is intentionally explicit; do not hash a hand-normalized command. Its hash is checked live before/after every workload process. The collector only validates restoration declarations and live identity; it does not implement cleanup. Independent operational review must establish that both recovery paths terminate/reap the owned workload cgroup before resuming the exact coordinator and restoring Parca. A true boolean is not that proof by itself.

To avoid circular hashes, a **separate** immutable `review.json` is supplied with its own SHA256:

```json
{
  "schema_version": 1,
  "decision": "APPROVED",
  "reviewer_role": "independent operational reviewer",
  "isolation_sha256": "<exact isolation.json hash>",
  "collector_sha256": "<exact reviewed collector hash>"
}
```

The review must come from the actual independent review; the collector does not synthesize it. Invocation accepts only root and the three explicit content pins:

```text
python3 fleet_profiler_off_qualification.py --root RUN_ROOT \
  --collector-sha256 COLLECTOR_SHA \
  --isolation-record ISOLATION_JSON --isolation-sha256 ISOLATION_SHA \
  --isolation-review REVIEW_JSON --review-sha256 REVIEW_SHA
```

The reserved unit must constrain the controller to CPU0; the collector rejects any other affinity. The controller launches each baseline child with CPU2 set in pre-exec, additionally uses the fixed `taskset -c 2` command and records the actual child affinity immediately after creation. The immutable workload has no affinity-changing code. Child endpoint affinity cannot be read after it is reaped; the pre-exec/startup guarantee and fixed ELF are recorded honestly rather than inventing a post-exit observation. CPU2 must be online with sibling list exactly2. Architecture must be aarch64.

Before **and after** every verify/measure child, all source/referee/ELF/collector/record/cleanup pins and lease/coordinator checks rerun. `/proc/PID/stat` must show the saved coordinator in T state with unchanged start ticks. Parca must have `ActiveState=inactive`, `SubState=dead`, `MainPID=0`, and the original empty affinity/AllowedCPUs policy. The process audit rejects any `/proc` comm containing parca or command line containing parca-agent. Disappearing processes are tolerated only as FileNotFound races; permission/read errors stop the attempt. No Docker container may be running. These boundary checks do not claim continuous scheduling exclusion of every unrelated system daemon or diagnose Parca as the old failure's cause.

## Evidence and bounded failure handling

Per phase: `metadata.json`, `launches.jsonl`, `child-starts.jsonl`, `commands.jsonl`, exact child `.stdout/.stderr`, `aa.jsonl`, `analysis.json` and `result.json`. The overall directory retains admission and final/partial result. Exact isolation commands, stdout/stderr and snapshots are retained separately around every child. Launch argv is persisted before Popen, retaining the intended command even if external cleanup kills the controller mid-child. Partial directories consume the attempt.

Child timeout is240 seconds. A timed-out/failed child is killed and reaped before postflight; failure stops the sequence. External release/backup recovery remains responsible for the whole owned cgroup if the controller itself is killed. Resource diagnostics are the `RUSAGE_CHILDREN` delta directly around that sole child: user/system CPU, minor/major faults, voluntary/involuntary context switches. No operational audit child runs inside that bracket. The taskset exec, fixture construction, verification/warmup, measured loop, postvalidation and teardown all contribute; these are **whole-child diagnostics**, not instructions/op or timed-loop CPU metrics. Max-RSS is deliberately not differenced. Diagnostics never modify timing validity or replace wall-time A/A gates.

## Offline validation and limitations

`python3 -m unittest discover -s experiments/ARM-LOOKUP-CONT-001/Q4 -p 'test_*.py' -v` runs correctness-only synthetic analysis and temporary-directory claim tests. Twelve tests cover all four fixed phase models; no clocks/process/host calls from pure analysis; wrong/missing/duplicate/reordered/nonfinite rows; model/count/source/referee/ELF mutations; strict±1% and250ms boundaries; exact memory both within/across blocks; extra exclusion fields; phase/overall overwrite; skipping failed/partial predecessors; JSON duplicate keys; reviewed-record/policy/recovery binding. These tests execute no source binary, collector main, service command or fleet operation. Live timer, process, cleanup and Parca facts remain the root operational review's responsibility; this preparation cannot claim they were validated locally.

Own enabled-tool discovery found no callable cpu-perf/library_status tool. The controller's actual Q4 consultation and limited3/287-source,158-passage coverage are recorded in the protocol; no passage establishes a cause or predicts a passing control. No new consultation is claimed by this worker. Public role: collector implementer, not independent reviewer. Exact model/token costs remain unknown; detailed backend provenance stays private.

For both Q4 baseline compiler cohorts, Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children are unavailable: no profile/TMA collection is part of Q4. There is no candidate profile or optimization result. Offline synthetic rows are test data only and cannot qualify a real cohort.
