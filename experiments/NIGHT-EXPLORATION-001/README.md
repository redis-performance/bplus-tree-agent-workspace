# Overnight exploration — shared M1 / M6 plan

**Status: prepared for launch.** The first eight hours follow the core queue; an
explicit later user deadline activates the bounded extension in PLAN.md.
Target: the standalone B+ tree and member index. No Redis server. Both hosts follow
this queue and measurement protocol; their evidence and decisions stay separate.

The baseline matrix is **100 / 1K / 10K / 100K / 1M members × eight operations**:
insert, hit lookup, miss lookup, rank, forward iteration, scan, score update, delete.
The [five-size M1 baseline](../SIZE-MATRIX-001/apple-m1-five-sizes/SUMMARY.md) is complete
and separate from the preserved four-size data. The overnight campaign is still unstarted.

## Read first

- [Experiment queue and time limits](PLAN.md)
- [Measurement and selection rules](MEASUREMENT.md)
- [Worker instructions](WORKER.md)
- [Morning report template](REPORT-TEMPLATE.md)
- [M1 publication and M6 decision checks](COORDINATION.md)
- [Lessons from Lemire's benchmark template](LEMIRE-NOTES.md)
- [C blog benchmarks and cbitset: changes worth making](BENCHMARK-REVIEW.md)

## Start on each host

Use a separate clean checkout on each machine. Fetch the same published plan revision
on both before starting. Keep the baseline tree source identical; do not copy binaries
between machines. Requires Python 3.9+, Clang, Make, and a working local `codex` CLI.
The supervisor uses existing authentication and permission settings.

```sh
# On M1 use apple-m1; on the planned M6 mini use apple-m6-mini.
HOST_LABEL=apple-m1
RUN_ID=$(date -u +%Y%m%dT%H%M%SZ)
CAMPAIGN_DIR="experiments/NIGHT-EXPLORATION-001/runs/$HOST_LABEL/$RUN_ID"
RUNTIME_DIR="scratch/night-$HOST_LABEL-$RUN_ID"
NIGHT_DEADLINE=$(python3 -c 'from datetime import datetime,timedelta,timezone; print((datetime.now(timezone.utc)+timedelta(hours=8)).isoformat())')

git switch -c "exploration/$HOST_LABEL-$RUN_ID"
python3 scripts/overnight.py --deadline "$NIGHT_DEADLINE" \
  --run-dir "$RUNTIME_DIR" --round-seconds 1800 \
  --prompt-file experiments/NIGHT-EXPLORATION-001/WORKER.md \
  --campaign-dir "$CAMPAIGN_DIR" --host-label "$HOST_LABEL"
```

This launch starts autonomous local work. Preparation alone does not start it.
The host label is a label: the worker must record the actual detected CPU and stop
if it disagrees with the intended host. Do not assume M6 specifications or reuse M1
frequency/core information. Machines can run at different dates/times.

The supervisor runs foreground. In a second terminal use the literal runtime path
printed in your launch variables (those variables are not shared between terminals):

```sh
cat scratch/night-HOST-RUNID/status.json
touch scratch/night-HOST-RUNID/STOP
```

Replace `HOST-RUNID` with the actual label and timestamp. STOP terminates the worker
and its observed children; partial evidence remains. The supervisor prevents idle
sleep on macOS, enforces round/deadline limits, and stops after three failed rounds
or a host-specific BLOCKED.md. It does not protect against power loss/lid closure.
No worker changes the supervisor, deadline, STOP file or permission settings.

## Follow progress and publish

Each host writes `STATUS.md`, `HANDOFF.md`, and numbered experiment folders under
its campaign directory. Runtime transcripts stay in ignored `scratch/`. The final
45 minutes before the supplied deadline produce `MORNING-REPORT.md`, curated evidence, and a commit on that host's
branch. Commit and push each validated host decision so the other host can read it. The
M1 worker checks the latest published M6 branch before each candidate trial and
skips hypotheses explicitly discarded there. An unpushed M6 decision cannot be
observed remotely; keep the state UNKNOWN until it appears. Publish the host branch:

```sh
git push -u origin HEAD
```

Keep M1/M6 commits on separate branches; avoid concurrent pushes to main. Bring a
candidate patch and frozen harness to the other host for exact replication. If two
hosts independently produce different patches, treat those as different candidates.
Compare each candidate against its local baseline before comparing directions
across machines. A win on one host is not a cross-host win.

No candidate is merged into the baseline tree during the night. A useful morning
outcome may be a supported candidate, a falsified hypothesis, or a concrete
measurement limitation. It must include reproducible artifacts, not just activity counts.
