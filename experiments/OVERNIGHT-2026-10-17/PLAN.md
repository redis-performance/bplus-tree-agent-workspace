# Overnight local campaign — 17–18 October 2026

User instruction: continue experimenting and loop through the night. The assumed
endpoint is **18 October 08:00 Europe/Lisbon / 07:00 UTC**. Scope remains standalone
data structure microbenchmarks. No Redis integration or upstream publication.

Starting commit: `a1a364d835d5be4c0e4c46aeb24b5a0e08f70948`. Its EXP-001 evidence has
144 processes, 984 checked rows and four sampled profiles. Only 1/41 workload cells
qualifies. This campaign starts by repairing measurement limitations, not claiming gains.

## Queue

1. A separate referee revision for duration, thread CPU time, boundary CPU IDs and
   observable QoS; test it and freeze exact provenance before any comparison.
2. A preregistered, targeted A/A campaign with longer intervals. Choose fixed sample
   counts and guard cases beforehand. All measurements serial; no overlapping builds.
3. When the evidence supports comparison, both population stages in
   [the protocol](../../docs/POPULATION.md), followed by correctness, sanitizers,
   same-session ABBA, profile validation, fresh confirmation and adversarial review.
4. Preserve candidate patches and all rejected/parked decisions. Keep root source at
   baseline for morning review. Failed precision is a reason to investigate or PARK,
   not to loosen the >=2% primary / <=1% guard gates after observing a result.
5. Use final round for the morning report and reconciled memory/ledgers.

MCP methodology: consult `cpu_perf.ask` first, then benchmark methods 05 and 14.
[Benchmark 14](https://github.com/usamahz/cpu-performance-engineering/blob/main/misc/benchmarks/14-pcore-vs-ecore/README.md)
records boundary CPU IDs and thread CPU time; its method says "nothing pinned".
These are useful observability ideas. Its M4 Pro results and CPU numbering are not
evidence about this M1. The broad retrieval on this turn returned unrelated Propeller
and concurrent-queue passages, which are not used to justify this campaign.

## Runtime and recovery

[Supervisor](../../scripts/overnight.py) runs fresh, serial `codex exec` rounds of up
to 30 minutes with a workspace-write sandbox and inherited user configuration.
[Worker instructions](../../docs/OVERNIGHT-PROMPT.md) require continuous saved
progress and handoff before each timeout. No settings or hook overrides. This uses
the documented [non-interactive CLI](https://learn.chatgpt.com/docs/non-interactive-mode).
The capability checks verified shell execution, scratch writes and the CPU MCP tool
registry. Exact worker model ID was not exposed; it identifies itself as GPT-6 Codex.

Runtime directory: `scratch/overnight-20261017`. It contains `status.json`, the
supervisor PID, exact prompts, per-round reports, private JSONL transcripts, stderr,
actual reported token usage and timestamps. Public experiment evidence goes in
`experiments/`; transcripts remain ignored. No automatic publication of worker drafts.
Commits/worktrees may be denied by workspace-write protection of `.git`; workers must
record this and freeze baseline-commit-plus-patch/SHA256 snapshots. Such results remain
provisional until committed and reviewed. This does not relax acceptance requirements.

An exclusive repository lock prevents two supervisors. A bounded `caffeinate -i`
assertion prevents idle sleep while the supervisor lives; it does not prevent manual
sleep, lid closure, loss of power, network interruptions or exhausted model quota.
Each round has a timeout. Only the worker and its observed descendants are terminated.
Three consecutive failed CLI rounds stop the supervisor. A permanent blocker should be
recorded in `BLOCKED.md`. No external services, paid machines or credentials are created.

Inspect current state:

```sh
cat scratch/overnight-20261017/status.json
```

Stop early (checks every five seconds; allow brief cleanup):

```sh
touch scratch/overnight-20261017/STOP
```

Start command (run directory must be new):

```sh
python3 scripts/overnight.py --deadline 2026-10-18T07:00:00+00:00 \
  --run-dir scratch/overnight-20261017
```

The supervisor stops at the deadline and releases its sleep assertion. Existing
results are retained on timeout, failure or manual stop. An interrupted final report
is not represented as completed work. Optimisation counts start at zero.

Prelaunch validation: `python3 tests/test_overnight.py -v` passed all four tests
(real child-process cleanup including a separate session, an unrelated process left
alive, STOP interruption, round continuation/usage, and exclusive-lock refusal).
`python3 scripts/check-workspace.py --pristine-source` and `git diff --check` passed.
No B+ tree source or referee change is included in this orchestration preparation.
