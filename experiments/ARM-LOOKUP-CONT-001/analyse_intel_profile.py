"""Fail-closed qualification of saved Intel profiles; never collects measurements."""
import argparse
import collections
import csv
import hashlib
import json
import math
import pathlib
import re
import statistics

CHILDREN = {
    'Frontend_Bound': ('Fetch_Latency', 'Fetch_Bandwidth'),
    'Bad_Speculation': ('Branch_Mispredicts', 'Machine_Clears'),
    'Backend_Bound': ('Memory_Bound', 'Core_Bound'),
    'Retiring': ('Light_Operations', 'Heavy_Operations'),
}
AREAS = set(CHILDREN) | {p + '.' + c for p, cs in CHILDREN.items() for c in cs}
EVENTS = {'cycles:u', 'instructions:u', 'branches:u', 'branch-misses:u'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def number(value):
    require(not isinstance(value, bool), 'boolean used as number')
    result = float(value)
    require(math.isfinite(result), 'nonfinite number')
    return result


def read_json(path):
    return json.loads(path.read_text())


def checked(function, *args):
    try:
        return {'qualified': True, **function(*args)}
    except (OSError, ValueError, TypeError, KeyError, IndexError, AttributeError, OverflowError, csv.Error) as exc:
        return {'qualified': False, 'error': str(exc)}


def command(path, stem):
    data = read_json(path / (stem + '.command.json'))
    require(type(data['returncode']) is int, stem + ' malformed returncode')
    require(isinstance(data['argv'], list) and all(isinstance(x, str) for x in data['argv']),
            stem + ' malformed argv')
    return {'qualified': data['returncode'] == 0,
            'returncode': data['returncode'], 'argv': data['argv']}


def process_stat(text):
    pid, rest = text.split(' (', 1)
    fields = rest.rsplit(') ', 1)[1].split()
    require(fields[0] not in ('Z', 'X', 'x'), 'workload not live')
    require(int(fields[17]) == 1, 'workload is not single threaded')
    ticks = int(fields[11]) + int(fields[12])
    require(ticks >= 0, 'negative process ticks')
    return (int(pid), int(fields[19])), ticks


def scope(path, stem):
    saved = read_json(path / (stem + '.scope.json'))
    before, after = saved['before'], saved['after']
    for endpoint in (before, after):
        require(endpoint['affinity'] == [2], 'workload affinity is not CPU2')
        require(endpoint['sibling_offline'] is True and endpoint['parca_inactive'] is True,
                'isolation endpoint check failed')
        cpu = endpoint['cpu2']
        require(isinstance(cpu, list) and len(cpu) == 8 and
                all(type(x) is int and x >= 0 for x in cpu), 'malformed CPU ticks')
    elapsed = number(after['time']) - number(before['time'])
    require(elapsed > 0, 'scope time did not advance')
    identity, start = process_stat(before['proc'])
    final_identity, end = process_stat(after['proc'])
    require(identity == final_identity, 'process identity changed')
    delta = [y - x for x, y in zip(before['cpu2'], after['cpu2'])]
    require(all(x >= 0 for x in delta), 'CPU counter decreased')
    busy = sum(delta) - delta[3] - delta[4]
    work = end - start
    require(busy > 0 and work > 0, 'no active workload scope')
    error = 100 * abs(busy - work) / busy
    require(number(saved['cpu_busy_ticks']) == busy and number(saved['workload_ticks']) == work,
            'saved scope tick totals disagree')
    require(abs(number(saved['accounting_error_percent']) - error) <= 1e-9,
            'saved scope error disagrees')
    require(error <= 1 and saved['pass'] is True, 'scope exceeds registered 1% bound')
    return {'cpu_busy_ticks': busy, 'workload_ticks': work,
            'accounting_error_percent': error, 'bracket_seconds': elapsed,
            'process_identity': identity, 'attribution': 'CPU2 aggregate tick bound; not PID-exclusive TMA'}


def tma_rows(path, stem):
    candidates, advisories = [], []
    for suffix in ('stderr', 'stdout'):
        lines = (path / (stem + '.' + suffix)).read_text().splitlines()
        heads = [i for i, line in enumerate(lines) if line.startswith('Timestamp,')]
        require(len(heads) <= 1, 'multiple CSV headers in stream')
        if heads:
            candidates.append(lines[heads[0]:])
            advisories.extend(lines[:heads[0]])
        else:
            advisories.extend(lines)
    # Do not hide extra numeric rows or unknown diagnostics outside the CSV stream.
    prefixes = ('Consider disabling nmi watchdog ', '(echo 0 |',
                ' echo kernel.nmi_watchdog=', 'Add --run-sample ', 'Add --nodes ',
                'Run toplev ', '# ')
    require(all(not line.strip() or line.startswith(prefixes) for line in advisories),
            'unrecognized text outside TMA CSV')
    require(len(candidates) == 1, 'expected one TMA CSV stream')
    reader = csv.DictReader(candidates[0])
    require({'Timestamp', 'Area', 'Value', 'Unit', 'Multiplex'} <= set(reader.fieldnames or []),
            'incomplete TMA header')
    require(len(reader.fieldnames) == len(set(reader.fieldnames)), 'duplicate TMA CSV column')
    groups = collections.OrderedDict()
    previous = None
    for row in reader:
        stamp = row.get('Timestamp', '')
        # Only known toplev footer records may occur after the CSV header.
        if isinstance(stamp, str) and stamp.startswith(('Run toplev ', '# ')):
            require(not row.get('Area') or row['Area'] not in AREAS | {'MUX'},
                    'metric disguised as advisory')
            advisories.append(row)
            continue
        timestamp = number(stamp)
        require(timestamp > 0, 'nonpositive TMA timestamp')
        require(None not in row and all(value is not None for value in row.values()),
                'malformed TMA CSV row')
        if timestamp != previous:
            require(previous is None or timestamp > previous, 'repeated or unordered interval')
            previous = timestamp
        groups.setdefault(timestamp, []).append(row)
    require(len(groups) == 5, 'expected five TMA intervals')
    values = collections.defaultdict(list)
    residuals = []
    for rows in groups.values():
        require(len(rows) == 13 and {r['Area'] for r in rows} == AREAS | {'MUX'},
                'expected unique four roots, eight children and MUX')
        by_area = {r['Area']: r for r in rows}
        for area, row in by_area.items():
            require(number(row['Multiplex']) == 100, 'TMA event not fully scheduled')
            value = number(row['Value'])
            require(0 <= value <= 100, 'TMA value out of range')
            if area == 'MUX':
                require(row['Unit'] == '%' and value == 100, 'invalid MUX metric')
            else:
                require(row['Unit'] in ('% Slots', '% Slots <'), 'invalid slot unit')
                values[area].append(value)
        require(abs(sum(number(by_area[k]['Value']) for k in CHILDREN) - 100) <= .3 + 1e-9,
                'root partition outside rounding bound')
        for parent, children in CHILDREN.items():
            residual = sum(number(by_area[parent + '.' + c]['Value']) for c in children) - number(by_area[parent]['Value'])
            require(abs(residual) <= .15 + 1e-9, 'child partition outside one-decimal rounding bound')
            residuals.append(residual)
    return {'metric_rows': 65, 'intervals': 5, 'timestamps': list(groups),
            'root_partition': True, 'child_partition': True, 'mux_all_100': True,
            'child_residual_range_pp': [min(residuals), max(residuals)],
            'advisories': advisories, 'values': dict(values)}


def counter_rows(path):
    streams = [(path / ('counters.' + suffix)).read_text() for suffix in ('stderr', 'stdout')]
    rows = [r for r in csv.reader('\n'.join(streams).splitlines()) if r]
    require(len(rows) == 4 and all(len(r) == 7 for r in rows), 'malformed counter CSV')
    require({r[2] for r in rows} == EVENTS, 'missing or duplicate process counters')
    durations = []
    for row in rows:
        require(row[1] == '' and row[5:] == ['', ''], 'unexpected process counter units or fields')
        require(number(row[0]) >= 0 and number(row[3]) > 0, 'unsupported or invalid counter')
        require(row[2] == 'branch-misses:u' or number(row[0]) > 0, 'empty workload counter')
        require(number(row[4]) == 100, 'process counter not fully scheduled')
        durations.append(number(row[3]))
    require(len(set(durations)) == 1, 'group counter running durations differ')
    return {'full_scheduling': True, 'events': sorted(EVENTS), 'running_duration_ns': durations[0]}


def sample_quality(path):
    require((path / 'hit.data').stat().st_size > 0, 'sample data missing or empty')
    report = (path / 'report.stdout').read_text()
    losses = re.findall(r'^# Total Lost Samples:\s*(\d+)\s*$', report, re.MULTILINE)
    require(losses == ['0'], 'sample loss absent, duplicated or nonzero')
    require("of event 'cycles:u'" in report, 'sample event is not user cycles')
    samples = re.findall(r'\((\d+) samples\)', (path / 'samples.stderr').read_text())
    require(len(samples) == 1 and int(samples[0]) > 0, 'missing sample collection count')
    require(not (path / 'report.stderr').read_text().strip(), 'sample report emitted diagnostics')
    return {'lost_samples': 0, 'recorded_samples': int(samples[0])}


def provenance(path, captures):
    meta = read_json(path / 'metadata.json')
    require(meta['controller_affinity'] == [0] and meta['workload_affinity'] == [2],
            'metadata affinity mismatch')
    require(re.fullmatch(r'[0-9a-f]{64}', meta['binary_sha256']) is not None, 'invalid binary hash')
    require(meta['topdown_version'] == '0.2.2' and
            meta['pmu_revision'] == '2568760ffc9394ddaa7a71f0c39930e780cf2dca',
            'collector/model differs from registered cohort')
    argv = read_json(path / 'workload-command.json')
    require(argv[:3] == ['taskset', '-c', '2'] and argv[4:] == ['measure', 'hit', '17', '10000000'],
            'unexpected workload launcher')
    require(not (path / 'workload.stderr').read_text().strip(), 'workload emitted errors')
    ending = read_json(path / 'workload-end.json')
    require(ending['intentionally_terminated'] is True and ending['returncode'] == -15,
            'workload ended unexpectedly')
    verified = read_json(path / 'verify.stdout')
    require(verified['verified'] is True and verified['case'] == 'hit' and verified['seed'] == 17
            and verified['members'] == 500, 'fixture verification failed')
    for stem in ('affinity', 'verify'):
        require(command(path, stem)['qualified'], stem + ' command failed')
    require(command(path, 'verify')['argv'] == argv[:4] + ['verify', 'hit', '17', '1'],
            'verification command differs from workload binary/fixture')
    require((path / 'affinity.stdout').read_text().strip() == 'CPU2', 'launcher probe failed')
    resumed = (path / 'resume.json').exists()
    if resumed:
        resume = read_json(path / 'resume.json')
        require(pathlib.Path(resume['from']).name == resume['from'], 'invalid resume directory')
        prior = path.parent / resume['from']
        require(prior.resolve() != path.resolve() and resume['kept_capture'] == 'tma-0', 'invalid resume source')
        old = read_json(prior / 'metadata.json')
        require({k: v for k, v in meta.items() if k != 'started'} ==
                {k: v for k, v in old.items() if k != 'started'}, 'resume metadata mismatch')
        for suffix in ('command.json', 'scope.json', 'stdout', 'stderr'):
            name = 'tma-0.' + suffix
            require((path / name).read_bytes() == (prior / name).read_bytes(), 'resume capture bytes differ')
        require(hashlib.sha256((path / 'tma-0.stderr').read_bytes()).hexdigest() == resume['raw_sha256'],
                'resume checksum mismatch')
    selected = captures[1 if resumed else 0:]
    require(all(c['scope_check']['qualified'] for c in selected), 'capture scope evidence incomplete or invalid')
    identities = [c['scope_check']['process_identity'] for c in selected]
    require(identities and all(x == identities[0] for x in identities), 'workload identity differs across captures')
    return {'resumed_tma0': resumed, 'binary_sha256': meta['binary_sha256']}


def capture(path, stem):
    cmd = checked(command, path, stem)
    sc = checked(scope, path, stem)
    data = checked(tma_rows, path, stem) if stem.startswith('tma-') else checked(
        counter_rows if stem == 'counters' else sample_quality, path)
    argv = cmd.get('argv', [])
    if stem.startswith('tma-'):
        shape = argv[1:] == ['-l2', '-I1000', '-x,', '--no-desc', '-v', '-C', '2', '--', 'sleep', '5']
    else:
        pid = str(sc.get('process_identity', [''])[0])
        if stem == 'counters':
            shape = argv[1:] == ['stat', '-p', pid, '-x,', '-e',
                                 '{cycles:u,instructions:u,branches:u,branch-misses:u}', '--', 'sleep', '3']
        else:
            shape = len(argv) == 13 and argv[1:9] == ['record', '-p', pid, '-F', '999', '-e', 'cycles:u', '-o'] and argv[10:] == ['--', 'sleep', '3']
    result = {'capture': stem, 'command': cmd, 'command_scope_valid': shape,
              'scope_check': sc, 'data_check': data}
    result['qualified'] = shape and all(x['qualified'] for x in (cmd, sc, data))
    return result


def analyse(path):
    path = pathlib.Path(path)
    captures = [capture(path, 'tma-' + str(i)) for i in range(3)]
    counters, samples = capture(path, 'counters'), capture(path, 'samples')
    report = checked(command, path, 'report')
    argv = report.get('argv', [])
    report['scope_valid'] = len(argv) == 10 and argv[1:7] == ['report', '--stdio', '--no-children', '--percent-limit', '0', '-i'] and argv[8:] == ['-s', 'dso,symbol']
    sample_argv = samples['command'].get('argv', [])
    report['input_matches_capture'] = len(argv) > 7 and len(sample_argv) > 9 and argv[7] == sample_argv[9]
    provenance_check = checked(provenance, path, captures + [counters, samples])
    flags = {'tma_qualified': all(c['qualified'] for c in captures),
             'counter_qualified': counters['qualified'], 'sample_qualified': samples['qualified'],
             'report_qualified': report['qualified'] and report['scope_valid'] and report['input_matches_capture'],
             'provenance_qualified': provenance_check['qualified']}
    all_qualified = all(flags.values())
    metrics = collections.defaultdict(list)
    for c in captures:
        for area, values in c['data_check'].pop('values', {}).items():
            metrics[area].extend(values)
    return {'all_qualified': all_qualified, **flags, 'captures': captures,
            'counters': counters, 'samples': samples, 'report': report, 'provenance': provenance_check,
            'counters_scope': counters['scope_check']['qualified'],
            'samples_scope': samples['scope_check']['qualified'],
            'aggregation': 'unweighted mean of displayed interval percentages; not pooled slot counts',
            'formula_audit': 'rendered slot units/partitions only; underlying event counts and runtime model selector unavailable',
            'metrics': {area: {'mean': statistics.mean(v), 'min': min(v), 'max': max(v),
                               'n': len(v), 'unit': '% total pipeline slots', 'qualified': all_qualified}
                        for area, v in metrics.items()}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=pathlib.Path)
    parser.add_argument('--no-write', action='store_true', help='print only; preserve saved analysis and raw evidence')
    args = parser.parse_args()
    result = analyse(args.directory)
    text = json.dumps(result, indent=2, allow_nan=False) + '\n'
    if not args.no_write:
        (args.directory / 'analysis.json').write_text(text)
    print(text, end='')
    return 0 if result['all_qualified'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
