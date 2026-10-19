# CPU Counters bootstrap: launch succeeded, counters remain unqualified

The owned probe completed with its exact expected checksum and enabled signposts;
the recorder exited successfully and target exit was observed. **This establishes
the bounded launch path, not hardware counter acquisition.** The available structural
evidence does not distinguish missing acquisition from guided data that the command
line exporter does not expose. No additional recording or table-row export was used
for this investigation. Frozen preparation files are unchanged.

The installed Apple CPU Counters package explicitly declares two export schemas:
`counters-profile` and `cpu-pmc-value`. The first contains a counter-value array;
the second contains event name/value columns. Both include process/thread/core
attribution. Neither schema occurs among this trace's **49 table instances** or
its public schema inventory. Its archived engineering-type registry also contains
no PMC/counter/cycle-weight type keys. This supports the narrower conclusion that
the inspected export inventory provides no established native counter measurements.
It cannot establish that every raw data stream is free of PMU information.

The trace preserves the selected guided CPU Bottlenecks mode, EL0 counting and
`allEventsAndFormulas=[]` exactly as configured. That empty list is also present
in the tool's advertised guided default. It therefore does **not** prove that a
manual recording accidentally selected no events. Legacy PMC setup fields resolve
to `NSNull`, but the newer guided configuration is separately serialized; those
legacy fields alone do not diagnose the selected mode.

Apple documents guided CPU Bottlenecks as a mode that gathers hardware counters
and derives bottleneck percentages. Those are expected capabilities, not proof
that this runner delivered them. Neither the successful CLI return nor ordinary
Time Profiler tables establishes them. The inspected run-issue metadata has one
generic issue, `Data stream: Time Mapping`; it supplies no explicit counter
permission/unsupported diagnosis. Absence of such a diagnosis does not exclude
an unresolved configuration, unavailable event set, silent fallback or export
limitation. [Apple's bottleneck workflow](https://developer.apple.com/documentation/xcode/addressing-cpu-bottlenecks),
[Instruments methodology](https://developer.apple.com/videos/play/wwdc2025/308/).

One structural OS state-reporting signpost table has `target-pid=ALL`, restricted
to Apple's Heartbeat/Transition/Volatile subsystems. Other table declarations include
SINGLE-target data. No rows were exported, so this does not identify activity from
another process; it does show why the entire private trace cannot be described as
universally restricted to the owned process. Measured process/thread/interval scope
remains unqualified. Raw archives and platform/process metadata stay private.

The next useful **read-only** discriminator is a private Instruments inspection
of this exact trace's CPU Counters track, Summary: Metrics and diagnostics, without
recording. Visible bottleneck metrics would support an exporter visibility gap;
an empty track would support absent or unresolved counter acquisition. Neither
outcome would establish row scope or numerical units by itself. An unchanged
recording retry is not justified by this evidence.

If a new qualification is chosen, a distinct bounded hypothesis is: **CPU Profiler
materializes target-scoped `cpu-profile` records with cycle weights on this runner.**
Its installed Apple schema explicitly contains `weight: cycle-weight`, process,
thread and core columns, plus `target-pid=ALL|SINGLE`. Apple describes this profiler
as cycle-triggered sampling. This offers a separate route to better weighted
profiles without assuming this guided counter mode works.

That proposal changes only the template to CPU Profiler and retains the exact
frozen standalone binary, seed1, 268,435,456 items and checksum9087321014236724183.
Use one self-launch with the same 4second recording, 60second recorder bound,
256MiB soft cap, self-alarm and bounded target-exit gates. A new reviewed plan,
freeze and exclusive ACK must precede it. Stop after the private TOC: require
`cpu-profile` with SINGLE scope, otherwise preserve the failure/insufficiency and
stop. Later owned-interval row exports would require a separate scope/unit review.
This would not establish IPC, retired instructions, stalls, cache misses or frequency.

CAPABILITY-INTERPRETATION.json retains exact structural findings, provenance hashes,
and the unexecuted proposal. Participant /root/followup_proposal_b; inherited
Codex/GPT-6 family; exact serving model, token usage and cost unknown.
