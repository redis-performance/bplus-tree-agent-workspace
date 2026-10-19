#!/usr/bin/env python3
"""Read-only, fixed-duration ambient observations; never benchmark qualification."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import time


def cpu_list(text):
    result = set()
    for part in text.strip().split(','):
        ends = [int(x) for x in part.split('-')]
        result.update(range(ends[0], ends[-1] + 1))
    return result


def optional(path):
    try:
        return {'value': Path(path).read_text().strip()}
    except OSError as error:
        return {'unavailable': type(error).__name__, 'errno': error.errno}


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(exist_ok=False)
    online_path = Path('/sys/devices/system/cpu/online')
    online = cpu_list(online_path.read_text())
    siblings = cpu_list(Path('/sys/devices/system/cpu/cpu2/topology/thread_siblings_list').read_text())
    assert 2 in siblings and siblings <= online
    # Only this observer changes its own affinity; services, benchmarks and the
    # owning lease remain untouched. Keep observation work off the target core.
    observer = min(online - siblings)
    os.sched_setaffinity(0, {observer})
    assert os.sched_getaffinity(0) == {observer}
    metadata = dict(started_utc=now(), observer_cpu=observer, target_cpu=2,
                    target_siblings=sorted(siblings), online_cpus=sorted(online),
                    samples=61, interval_seconds=10, expected_intervals=60,
                    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    clock_ticks_per_second=os.sysconf('SC_CLK_TCK'),
                    clocksource=optional('/sys/devices/system/clocksource/clocksource0/current_clocksource'),
                    cpu_governors={str(cpu): optional(f'/sys/devices/system/cpu/cpu{cpu}/cpufreq/scaling_governor') for cpu in siblings},
                    status='running', changes='observer process affinity only; no host configuration or service changes')
    (args.output / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')
    start = time.monotonic()
    previous = None
    deltas = []
    with (args.output / 'samples.jsonl').open('x') as stream:
        for index in range(61):
            delay = start + index * 10 - time.monotonic()
            if delay > 0:
                time.sleep(delay)
            read_start = time.monotonic()
            counters = {}
            for line in Path('/proc/stat').read_text().splitlines():
                fields = line.split()
                if fields[0] == 'cpu' or fields[0] in {'cpu' + str(cpu) for cpu in siblings | {observer}}:
                    counters[fields[0]] = [int(x) for x in fields[1:]]
            sample = dict(index=index, utc=now(), monotonic_seconds=read_start,
                          scheduled_offset_seconds=index * 10,
                          actual_offset_seconds=read_start - start,
                          online_cpus=sorted(cpu_list(online_path.read_text())),
                          observer_affinity=sorted(os.sched_getaffinity(0)),
                          counters=counters, loadavg=optional('/proc/loadavg'),
                          cpu_pressure=optional('/proc/pressure/cpu'),
                          reported_frequency_khz={str(cpu): optional(f'/sys/devices/system/cpu/cpu{cpu}/cpufreq/scaling_cur_freq') for cpu in siblings})
            sample['read_seconds'] = time.monotonic() - read_start
            stream.write(json.dumps(sample) + '\n')
            stream.flush()
            if previous is not None:
                interval = dict(index=index - 1, duration_seconds=read_start - previous['monotonic_seconds'], valid=True, cpu={})
                if sample['online_cpus'] != metadata['online_cpus'] or previous['online_cpus'] != metadata['online_cpus']:
                    interval.update(valid=False, error='online CPU set changed')
                for label, values in counters.items():
                    before = previous['counters'].get(label)
                    if before is None or len(values) != len(before) or len(values) < 8 or any(b < a for a, b in zip(before, values)):
                        interval.update(valid=False, error='missing/reset/changed CPU counters')
                        continue
                    diff = [b - a for a, b in zip(before, values)]
                    # Linux user/nice already include guest/guest_nice: use only
                    # the first eight fields in the total, retaining all raw ones.
                    total = sum(diff[:8])
                    interval['cpu'][label] = dict(raw_delta=diff, total_ticks=total,
                        idle_ticks=diff[3], iowait_ticks=diff[4], steal_ticks=diff[7],
                        nonidle_excluding_iowait_steal_ticks=sum(diff[i] for i in [0, 1, 2, 5, 6]))
                    if total <= 0:
                        interval.update(valid=False, error='nonpositive CPU tick interval')
                deltas.append(interval)
            previous = sample
    metadata.update(status='complete', finished_utc=now(), elapsed_seconds=time.monotonic() - start)
    (args.output / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')
    (args.output / 'intervals.json').write_text(json.dumps(deltas, indent=2) + '\n')
    print(json.dumps(dict(status='complete', samples=61, intervals=len(deltas), valid_intervals=sum(x['valid'] for x in deltas))))


if __name__ == '__main__':
    main()
