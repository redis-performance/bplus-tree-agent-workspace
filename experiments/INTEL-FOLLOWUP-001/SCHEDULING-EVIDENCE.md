# Why the deep probes remain unavailable

Both probes lack enabled/running measurements:2692 load samples and18,689 LBR
samples, zero READ/lost/throttle records, empty thread-value tables. Exact raw
hashes and scope reconstruction are in [independent gates](INDEPENDENT-PROBE-GATES.json).
Both methods remain disabled; there is no retry or protocol change this session.

## Observed configuration versus emitted measurements

Actual perf7.0.14 help describes `--running-time` as applying to read (`:S`)
events. This binary does not expose a `--sample-read` command-line option.
Its matching upstream implementation makes the distinction explicit:

- `-s` selects inherited-task statistics. In `evsel__config`, that sets timing
  fields in `read_format` and `inherit_stat`; `--running-time` also selects timing
  fields. Neither independently adds `PERF_SAMPLE_READ`.
- An event with `sample_read` does add `PERF_SAMPLE_READ`. The event modifier
  `S` sets this property.

These are separate options in [perf7.0.14 evsel configuration](https://github.com/gregkh/linux/blob/v7.0.14/tools/perf/util/evsel.c)
and [modifier parsing](https://github.com/gregkh/linux/blob/v7.0.14/tools/perf/util/parse-events.l).
The [record manual](https://github.com/gregkh/linux/blob/v7.0.14/tools/perf/Documentation/perf-record.txt)
also connects running-time output to read events.

The syscall contract distinguishes the sample payload from the read layout:
`PERF_SAMPLE_READ` includes a read-format structure inside a sample; the
enabled/running flags determine fields in that structure. Flags describing the
structure do not establish that its values were collected.
[perf_event_open(2)](https://man7.org/linux/man-pages/man2/perf_event_open.2.html)

For inherited events, upstream kernel `sync_child_event` can emit a READ record
through the child-exit path. That is not a periodic read of an already attached
standalone workload. Our workload stayed alive until after the collector stopped.
The absence of READ records is consistent with that path and the missing sample
bit; terminating an arbitrary workload is not the proposed remedy.
[Kernel event lifetime code](https://github.com/gregkh/linux/blob/v7.0.14/kernel/events/core.c)
This source matches the perf version, not necessarily every AWS kernel patch.

## Future method to validate, not an executed fix

For LBR, an event-specific read modifier is the documented starting point:

```text
perf record -e cycles:uS --running-time -c 1000000 -j any,u \
  --pid PID -o NEW_RAW -- sleep 5
```

It must be a new preregistered capability test. Verify actual `sample_type` contains
READ, actual decoded samples contain finite positive enabled/running values tied
to the intended event, and the declared scheduling threshold passes. Check the
sampling boundary and final uncovered tail; sample timestamps alone do not prove
whole-window scheduling. A future collector may need explicit start/end FD reads
for a strict full-window claim. Preserve all existing precision, loss, scope and
sample-population gates.

PEBS has a two-event group here: `mem-loads-aux` leads and `mem-loads` samples.
Generic group `:S` is leader sampling, but **this perf version explicitly handles
the auxiliary-load leader and chooses the second event as sampler**. My initial
generic warning was incomplete; it is not evidence that group `:S` would break
this configuration. The actual special case is in
[perf7.0.14 record configuration](https://github.com/gregkh/linux/blob/v7.0.14/tools/perf/util/record.c);
the general behavior is documented in the
[event modifier manual](https://github.com/gregkh/linux/blob/v7.0.14/tools/perf/Documentation/perf-list.txt).

A future PEBS protocol must verify that its selected syntax preserves the group,
intended sampling member, precise level, weight/data-source fields, requested
latency threshold and actual encoding. Do not count auxiliary samples as loads or
assume that the documented route is validated on this machine. Current probes
record requested ldlat30 and actual config1 `0x1f`; preserve both without silently
equating the encoding to a new threshold.

## Consultation and TMA

Own CPU-perf `library_status`, `ask` and explicit `read_source` calls are recorded
in [consultation and source hashes](SCHEDULING-CONSULTATION.json). Unlike the generic
ask output, the fetched syscall reference supplies relevant read-layout/sample-bit
passages. Retrieval ran on the controller only; source excerpts remain local.

This note describes collector qualification, not a fresh TMA experiment.
Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring for these deep probes
are unavailable; PEBS/LBR samples cannot substitute for the separately collected
L2 partitions. No source adoption, speed claim or new measurement was performed.
