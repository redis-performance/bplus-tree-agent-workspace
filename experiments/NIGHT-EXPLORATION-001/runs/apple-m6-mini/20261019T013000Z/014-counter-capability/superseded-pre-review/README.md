# CPU counter capability — prepared, no collection authorized

The local tools advertise promising instruments, but **hardware counter access,
permissions, exact metric units and usable process/thread scope remain UNKNOWN**.
No counter recording, probe execution, process attachment or privilege change has
been performed. The standalone probe may be compiled only after 013 has finished;
root confirmed its last capture ended at04:29:29.623856UTC with all children stopped.

This investigates whether richer causal evidence is available after 012's corrected
adapter controls failed fine precision. It cannot repair those controls, establish
that CPU endpoint changes represent within-window migration, or turn wall/thread
differences into hardware stall costs. No tree hypothesis or optimization acceptance
is selected here.

## What the primary local evidence establishes

`xctrace version` reports27.0(27A266a). Standard templates include CPU Counters,
CPU Profiler and Processor Trace. Local `help record` explicitly states that
`--show-recording-options` prints configuration JSON without starting a recording
and requires no target. Those are the only `record`-subcommand invocations used
during preparation. Original command/stdout/stderr hashes remain in commands.jsonl
and ignored scratch; generic public help/configuration results are in metadata/.

|Instrument|Observed configuration|Still unverified|
|---|---|---|
|CPU Counters|Guided CPU Bottlenecks, EL0, sample-by-time, no explicit events in allEventsAndFormulas|Permission, actual hardware events, formula denominators, export tables and target scope|
|CPU Profiler|Normal frequency setting; kernel call stacks disabled|Local cycle-sampling support, period/weight units and permissions|
|Processor Trace|Fill buffer, decoding enabled, throttling enabled|Hardware support, existing settings/permission, trace volume and exportability|
|powermetrics|Help exposes cpu_power and task IPC; no process-selection filter|Privilege requirements and all actual readings remain untested|

CPU Counters' standard template also includes Time Profiler and Points of Interest.
The frozen proposed recording options preserve the advertised configuration, with
`excludeOSLogs=true` for Points of Interest. That setting alone does not prove all
instruments exclude unrelated processes. Root must review target scoping before
authorizing the self-launch attempt. No all-process collection, remote device,
attachment, developer setting change, signing entitlement or elevated invocation
is part of this driver. If acceptable scope cannot be established, select NONE.

`powermetrics` is excluded from the qualification driver. Its defaults include
task/system samplers, and inspected help provides no target-process selector.
No attempt to run its samplers or discover privileged access is proposed.

Apple describes CPU Profiler as CPU-cycle based sampling and CPU Counters as guided
bottleneck/event analysis. This motivates qualification rather than assuming timer-PC
positions measure instruction costs. Apple also describes Processor Trace's special
hardware/settings and substantial data volume; it is excluded from the initial
driver. [Apple's Instruments methodology](https://developer.apple.com/videos/play/wwdc2025/308/),
[CPU bottlenecks](https://developer.apple.com/documentation/xcode/addressing-cpu-bottlenecks),
[Processor Trace](https://developer.apple.com/documentation/xcode/analyzing-cpu-usage-with-processor-trace).
These documents describe capabilities, not proof that this runner permits them.

## Safe two-stage qualification

Stage1, after a separate root/independent review and exclusive publication ACK,
may launch exactly one owned frozen executable under CPU Counters. The driver has
no attach/all-process branch. It uses `--no-prompt`; denial stops the attempt without
retries, sudo, permission changes or a fallback instrument.

The probe performs a fixed268,435,456-item unsigned xorshift recurrence, starting
from1. Its named non-inline function, disassembly/object/dSYM and binary hashes are
retained. Its result must equal **9087321014236724183**. Root independently derived
this expectation by GF(2) 64-column transition-matrix exponentiation, without
executing the probe or repeating its C loop. Setup includes a250ms sleep before the signposted
work interval. The probe prints its own checksum/identity only to private output;
it never enumerates processes or reads machine configuration. Compilation is allowed
now; execution is not.

The record limit is4seconds, tool wall limit60seconds clipped to the later ACK's
deadline, and the probe has an independent6second alarm. A256MiB trace-size watchdog
is a **soft stop, not a filesystem quota**: helper writers can overshoot between
polls, and root must accept that limitation before issuing the ACK. Only the owned
trace directory is inspected. Raw traces/TOC/output remain local, with hashes.
Tool timeout/interruption stops its process group; lack of a completed owned probe
result prevents treating the attempt as a qualified measurement.

After that single attempt, the driver exports only a private table of contents and
publishes bounded schema identifiers. It stops for root to inspect the actual units,
process/thread/CPU fields, signpost interval and loss/multiplexing semantics. No broad
counter-row export, wildcard XPath, whole-machine/process listing or automatic
additional recording is implemented. Traces can contain platform metadata; root
must establish that the selected instruments' measured data targets only the owned
launch before authorizing collection, and keep raw traces private.

Stage2 is a plan only, requiring another reviewed scope/schema decision. Its fixed
six captures would be two idle controls, two N-work controls and two2N-work controls.
N=268,435,456;2N=536,870,912; seed1. The stage1 capture is retained as the first N
capture, with no replacement or retry. Idle work sleeps1000ms inside the interval.
The exact expected checksums are1 for idle and16730757284781413201 for2N, from
the same independent matrix calculation.
All cases use the same frozen binary and250ms pre-interval sleep. Permission failure,
missing fields or an insufficient fixed probe stays unavailable/insufficient; counts
must not be retuned after inspecting results.

Qualification requires all of the following, rather than only a successful exit:

- Native event/formula values are finite, nonzero when expected, and have verified
  units, denominators and loss/multiplexing treatment.
- Aggregation includes only the owned PID/thread and intended signpost interval;
  setup/printing/sleeps outside that interval are excluded.
- Idle control activity and the ALU function/scope differ in the expected direction.
  Missing idle samples are reported as insufficient, rather than interpreted as zero.
- If retired instruction totals are available, scoped N:2N counts lie within1.8..2.2
  and repeated runs give consistent checksum/direction. Percentages alone do not
  qualify absolute instruction counts or IPC.
- Cycle/sample periods, per-core attribution and frequency information remain
  separate fields. Aggregate counts or PCs do not identify a frequency, core
  residency, cache miss or exact source-instruction cost.

Only after qualification could root design a separate matched iterator/lookup
profile using the corrected adapter. Such profiling remains separate from timing
qualification and optimization selection. No historical adapter effects are pooled.

## Commands and authorization barrier

Preparation supports only read-only metadata and build actions:

```
python3 <campaign>/014-counter-capability/driver.py metadata
python3 <campaign>/014-counter-capability/driver.py build
```

The second command compiles/links/symbolizes/disassembles without executing the
probe. It writes a freeze only after this README, source, plan and metadata exist.

The unexecuted future bootstrap requires an ACK with status=authorized, exact
freeze/driver/plan hashes, a full published commit, root and independent PASS
reviews, exclusive_runner=true, only_self_launch=true,
template_target_scope_reviewed=true, soft_trace_cap_understood=true,
stop_after_private_toc=true, and an absolute UTC deadline no more than10minutes
ahead. No ACK is supplied by preparation. Its future command would be:

```
python3 <campaign>/014-counter-capability/driver.py availability --ack <reviewed-ack.json>
```

Current status is preparation only. Runtime permission, marker visibility, schema
scope, counter values and driver collection behavior are untested. No probe was run
even as a timing smoke. Any future collection-driver refinements require root review
and a new exact freeze before collection. Participant /root/followup_proposal_b,
inherited Codex/GPT-6 family; exact serving model, token usage and cost unknown.
