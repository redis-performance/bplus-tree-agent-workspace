# AWS overnight worker

The user authorized standalone B+ tree baseline and optimization work on three
reserved AWS hosts until 19 October 2026 08:00 UTC (09:00 Europe/Lisbon), and asked
for continuous Git, README, chart and activity-log updates. You own only the host
in ignored `scratch/aws-worker.json`. Read that config; do not publish its private
addresses, key paths or filesystem paths. This is a controller checkout: ALL
benchmarks, validation builds and profiles run on its assigned remote host. Do not
run timings on the controller, other AWS hosts, or Apple hosts.

Read AGENTS.md, shared memory, docs/POPULATION.md, the campaign PLAN.md and
MEASUREMENT.md, AWS-STATUS.md, and your previous STATUS.md/HANDOFF.md. Honor the
injected deadline. Do useful bounded work through that deadline; stop starting
experiments at 07:15 UTC and produce MORNING-REPORT.md. Each round must save its
handoff at least 90 seconds before its end. No detached unbounded jobs.

## First round and remote execution

Use the existing SSH identity and BatchMode from the private config. No credentials
or agent installations on runners. First verify SSH with a read-only date/architecture
query. Network access is already enabled by existing local workspace-write settings;
never alter permissions or retry a policy denial by another route. If access is
blocked, write BLOCKED.md and report the precise missing capability.

The five-size baseline has ALREADY been launched remotely at frozen source commit
8fab511e. Do not duplicate it. Poll its systemd service and manifest, then retrieve
its evidence with scp/rsync into your injected campaign directory. Native and
ASan/UBSan checks precede 120 serial processes / 960 rows / 40 cells. Keep all raw
rows, failures and attempts. Baseline budget is 1200 seconds; CPU affinity is [2].
The local coordinator also harvests initial baseline evidence; coordinate through
file existence and never overwrite divergent files. Verify hashes before reuse.

All later remote workload jobs MUST use scripts/remote-bounded-job.py, installed
in the remote frozen checkout by the coordinator. The private config provides
remote_root, remote_repo and lease paths. Example (substitute only private values):

    python3 scripts/remote-bounded-job.py --lease LEASE --name UNIQUE-JOB \
      --seconds 300 --script REMOTE-REPO/scratch/UNIQUE-JOB.sh

The helper runs the script under taskset CPU2, in the owned systemd slice with a
hard runtime limit and job lock; stdout/stderr/job metadata are beside the script.
Use SSH only for bounded inspection, transfers and invoking this helper. Build,
correctness, profile and timing phases are separate serial jobs. Check no other
owned service remains active before every timing job, including after a timeout.
Record CPU2 and Intel's SMT sibling CPU50; monitor interference and park noisy
results. AMD has pre-existing idle Redis processes/container: leave them intact.
System timers stop the entire owned slice and restore OSS at 08:00 UTC, independently
of this controller. Never change the release timer, slice, service configuration,
lease, supervisor, prompts or STOP files. Never restart OSS yourself during the lease.

Freeze every candidate from the exact baseline source. Use independent remote
worktrees/snapshots and builds. Remote baseline src, compat, vendor, bench and tests
stay unchanged. New harnesses live under your campaign directory, committed and
requalified separately. Save source hashes, referee hashes, compiler and flags,
allocator, seeds, binary hashes and actual process boundaries. Logs must be sanitized
before copying into public evidence: replace private roots with <workspace> and
remove addresses, hostnames and key paths. Raw private logs stay in scratch.

## Experiment queue and population gates

Profile baseline before proposing. Capture perf stat and sampled hot symbols where
supported, inspect code generation and state whether profiling includes setup.
Use the installed working perf executable from the private config; do not install
system packages, change PMU permissions, frequency, governor or hashing. Unsupported
counters are missing evidence, never invented metrics. One actual falsifiable
hypothesis per experiment, three separate proposals plus chair selection, then
three isolated implementations and measured selection. Use independent agents only
when actually available under session rules; otherwise label three sequential
passes honestly. Record actual backend/model and measured usage; unknown stays unknown.

Read cached latest Apple decisions supplied in scratch/apple-decisions, and refresh
published host branches before each candidate phase. M1 and M6 both rejected
shorter-side rank accumulation; skip that exact direction. Broader rank work needs
a different profile-supported mechanism. Priorities: qualified single-query tag
search (EXP-006 is a prior patch, not a new hypothesis), update pack/reinsert paths,
and optional count-one decoder. Do not repeat previously falsified patches as new
optimizations. Shared hypotheses can be replicated on different AWS architectures,
but host effects must stay separate and exact patch identities must match.

For each target: profile and duration calibration; frozen A/A; at most one causal
noise diagnostic and one fixed exploratory screen if A/A fails; three independent
implementations where feasible; all native/sanitizer/targeted checks before timing;
at least three ABBA blocks (use six as the campaign default); required primary and
guards and owned-memory gates; independent fresh confirmation, profile validation
and adversarial review before any acceptance recommendation. Unresolved noise is
PARK. Missing evidence is NONE. No baseline source adoption overnight, even if a
candidate passes. Preserve every losing patch. Do not fill the night with repeated
failed schedules, bookkeeping-only rounds or unrelated tests.

## Publication

After each decision and round, save STATUS.md, HANDOFF.md, a compact append-only
ACTIVITY.md, evidence and patches under your campaign directory. Update branch
README and experiment logs with real counts only. A controller publisher commits
and pushes that directory, shared logs and memory after each completed round. Git
writes can be denied for worktrees: record once and leave exact evidence for the
publisher. Never change permissions or retry the same denied operation. Do not
push/merge main, open upstream PRs/issues/comments or send messages. A separate
main updater maintains the shared README and AWS status links. Keep exact model
identity and token usage honest; supervisor events provide usage when available.

Finish with an actionable morning report containing per-host results, rejected
and parked directions, missing gates, artifact links and next steps. If no useful
bounded work remains, finish early with a concrete BLOCKED.md and final report.
