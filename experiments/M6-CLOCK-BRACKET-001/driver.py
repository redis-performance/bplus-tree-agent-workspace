#!/usr/bin/env python3
"""Separate harness build, empirical controls, then fixed fresh A/A. No source candidates."""
import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import signal
import time
from datetime import datetime, timezone

ROOT = Path.cwd()
E = Path(__file__).resolve().parent.relative_to(ROOT)
BUILD = Path('build/m6-clock-bracket-001')
spec = importlib.util.spec_from_file_location('frozen_exp009_supervision', ROOT / 'experiments/EXP-009/driver.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
FIELDS = 'w0_ns,t0_ns,w1_ns,w2_ns,t1_ns,w3_ns,wall_resolution_ns,thread_resolution_ns'.split(',')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def save(path, value):
    old.save(path, value)


def verify(table):
    for path, expected in table.items():
        assert sha(path) == expected, str(path)


def bracket(row):
    v = {key: int(row[key]) for key in FIELDS}
    assert 0 <= v['w0_ns'] <= v['w1_ns'] <= v['w2_ns'] <= v['w3_ns']
    assert 0 <= v['t0_ns'] <= v['t1_ns']
    assert v['wall_resolution_ns'] >= 0 and v['thread_resolution_ns'] >= 0
    inner = v['w2_ns'] - v['w1_ns']
    thread = v['t1_ns'] - v['t0_ns']
    margins = v['w1_ns'] - v['w0_ns'] + v['w3_ns'] - v['w2_ns']
    lower, upper = max(0, thread - margins), min(thread, inner)
    return {'inner_wall_ns': inner, 'outer_thread_ns': thread, 'wall_margins_ns': margins,
            'recorded_residual_ns': inner - thread,
            'conditional_cpu_lower_ns': lower, 'conditional_cpu_upper_ns': upper,
            'conditional_zero_error_model_nonempty': lower <= upper,
            'physical_attribution': 'UNVALIDATED: unknown clock accuracy/accounting error'}


def parse(path, n, ops, seed, case='lookup-hit', member=16, fixture=None):
    reader = csv.DictReader(io.StringIO(Path(path).read_text()))
    rows = list(reader)
    assert reader.fieldnames == old.CSV_HEADER + FIELDS and len(rows) == 1
    r = rows[0]
    assert None not in r and all(value is not None for value in r.values())
    for key, value in {'size': n, 'operations': ops, 'requested_ops': ops, 'seed': seed,
                       'case': case, 'member_bytes': member, 'warmup_passes': 1, 'traversals': 0}.items():
        assert r[key] == str(value), key
    checksum, digest = (fixture['checksum'], fixture['query_order_sha256_le_u64']) if fixture else old.expected_checksum(case, n, ops, seed)
    assert int(r['checksum']) == int(checksum)
    b = bracket(r)
    assert b['inner_wall_ns'] == int(r['elapsed_ns']) > 0
    assert b['outer_thread_ns'] == int(r['thread_elapsed_ns']) >= 0
    assert int(r['tree_bytes']) > 0
    assert abs(float(r['ns_per_op']) - int(r['elapsed_ns']) / ops) <= .0006
    return {'csv': r, 'bracket': b, 'query_order_sha256_le_u64': digest}


class Owner:
    def __init__(self, phase, publication):
        self.phase = phase
        self.plan = load(E / 'PLAN.json')
        self.started = time.monotonic()
        self.limit = self.plan['phase_wall_caps_seconds'][phase]
        self.absolute = datetime.fromisoformat(self.plan['absolute_stop_utc']).timestamp()
        assert self.remaining() > 20
        self.inputs = load(E / 'inputs.json')['files_sha256']
        verify(self.inputs)
        self.prerequisites = {}
        if phase != 'build':
            build_manifest = E / 'results/build/build-manifest.json'
            build_status = E / 'results/build/status.json'
            previous = load(build_status)
            assert previous['status'] == 'COMPLETE' and previous['release_safe']
            assert load(build_manifest)['status'] == 'COMPLETE'
            self.prerequisites = dict(load(build_manifest)['files_sha256'])
            self.prerequisites.update({str(build_manifest): sha(build_manifest), str(build_status): sha(build_status)})
            verify(self.prerequisites)
        if phase == 'aa':
            control_manifest = E / 'results/controls/evidence-manifest.json'
            control_status = E / 'results/controls/status.json'
            previous = load(control_status)
            assert previous['status'] == 'COMPLETE' and previous['release_safe'] and previous['native_lock_released']
            self.prerequisites.update(load(control_manifest)['files_sha256'])
            self.prerequisites.update({str(control_manifest): sha(control_manifest), str(control_status): sha(control_status)})
            verify(self.prerequisites)
            controls = load(E / 'results/controls/summary.json')
            assert controls['sensitivity_pass'], 'Control failure: qualification not authorized by protocol'
        self.out = E / 'results' / phase
        assert not self.out.exists(), 'No phase overwrite/retry'
        self.out.mkdir(parents=True)
        self.raw = self.out / 'raw'
        self.raw.mkdir()
        self.records = []
        self.state = {'status': 'RUNNING', 'phase': phase, 'published_commit': publication,
                      'started_utc': old.utc(), 'release_safe': True, 'source_selection': 'NONE',
                      'physical_attribution': 'UNVALIDATED', 'input_manifest_sha256': sha(E / 'inputs.json')}
        self.lock = ROOT.parents[1] / 'scratch/m6-clock-bracket-native.lock'
        self.owns_lock = False

    def remaining(self):
        return min(self.limit - (time.monotonic() - self.started), self.absolute - time.time())

    def bound(self):
        assert self.remaining() > 0, 'Deadline reached'

    def persist(self):
        save(self.out / 'status.json', self.state)

    def acquire(self):
        if self.phase in ['controls', 'aa']:
            self.lock.parent.mkdir(exist_ok=True, parents=True)
            with self.lock.open('x') as f:
                json.dump({'pid': os.getpid(), 'phase': self.phase, 'started_utc': old.utc()}, f)
            self.owns_lock = True
        self.persist()
        signal.signal(signal.SIGALRM, old.cancel)
        signal.signal(signal.SIGTERM, old.cancel)
        signal.signal(signal.SIGHUP, old.cancel)
        signal.setitimer(signal.ITIMER_REAL, self.remaining())

    def finish(self, failure):
        final_error = None
        try:
            verify(self.inputs)
            verify(self.prerequisites)
            assert sha(E / 'inputs.json') == self.state['input_manifest_sha256']
            self.bound()
            self.state.update(status='FAILED_NO_RETRY' if failure else 'COMPLETE',
                              failure_type=type(failure).__name__ if failure else None,
                              finished_utc=old.utc(), wall_seconds=time.monotonic() - self.started,
                              journaled_commands=len(self.records),
                              release_safe=all(r['release_safe'] for r in self.records))
            if not failure:
                save(self.out / 'evidence-manifest.json', {'files_sha256': {
                    str(p): sha(p) for p in self.out.rglob('*')
                    if p.is_file() and p.name not in ['status.json', 'evidence-manifest.json']}})
        except BaseException as ex:
            self.state.update(status='FAILED_FINALIZATION_NO_RETRY', finalization_error_type=type(ex).__name__)
            final_error = ex
        finally:
            mask = signal.pthread_sigmask(signal.SIG_BLOCK, old.SIGS)
            try:
                self.state.update(finished_utc=old.utc(), wall_seconds=time.monotonic() - self.started,
                                  journaled_commands=len(self.records),
                                  release_safe=all(r['release_safe'] for r in self.records))
                if self.owns_lock and self.state['release_safe']:
                    assert load(self.lock)['pid'] == os.getpid()
                    self.lock.unlink()
                    self.state['native_lock_released'] = True
                if self.remaining() <= 0:
                    self.state['status'] = 'FAILED_DEADLINE_NO_RETRY'
                    final_error = TimeoutError('Finalization deadline')
                self.persist()
                if self.remaining() <= 0:
                    self.state['status'] = 'FAILED_DEADLINE_NO_RETRY'
                    self.persist()
                    final_error = TimeoutError('Final serialization deadline')
                signal.setitimer(signal.ITIMER_REAL, 0)
            finally:
                signal.pthread_sigmask(signal.SIG_SETMASK, mask)
        if final_error:
            raise final_error


def build(o):
    assert not BUILD.exists(), 'No build overwrite'
    BUILD.mkdir(parents=True)
    for mode, flags in [('native', old.NATIVE), ('san', old.SAN)]:
        (BUILD / mode).mkdir()
        for name, source, tree, defines in [
                ('lookup', E / 'harness/lookup.c', True, []),
                ('controls', E / 'harness/controls.c', False, []),
                ('old-lookup', Path('experiments/EXP-009/harness/lookup.c'), True, []),
                ('original43', Path('tests/upstream.c'), True, ['-DREDIS_TEST', '-DREDIS_DEBUG'])]:
            cmd = ['clang', *flags, *defines, '-I.', *old.INC, str(source),
                   *(old.COMMON if tree else old.COMMON[1:]), '-o', str(BUILD / mode / name)]
            old.run(o, cmd, 'compile-' + mode + '-' + name, max_seconds=120)
        paths = old.run(o, [BUILD / mode / 'original43'], mode + '-original43', max_seconds=120)
        assert not paths['stderr'].stat().st_size
        assert '0 failed, 43 total' in paths['stdout'].read_text() and '43 passed' in paths['stdout'].read_text()
        for member in [8, 16, 319, 320, 321, 1024]:
            for case in ['lookup-hit', 'lookup-miss', 'lookup-mixed']:
                name = mode + '-' + case + '-m' + str(member)
                paths = old.run(o, old.lookup_cmd(BUILD / mode / 'lookup', 1000, 2003, 1, case, member), name)
                assert not paths['stderr'].stat().st_size
                row = parse(paths['stdout'], 1000, 2003, 1, case, member)
                old_paths = old.run(o, old.lookup_cmd(BUILD / mode / 'old-lookup', 1000, 2003, 1, case, member), name + '-referee')
                baseline = old.parse_csv(old_paths, 1000, 2003, 1, case, member)
                for key in ['operations', 'checksum', 'tree_bytes', 'requested_ops', 'size', 'seed', 'member_bytes', 'warmup_passes']:
                    assert row['csv'][key] == baseline['csv'][key]
    metadata = old.run(o, ['clang', '--version'], 'compiler')
    save(o.out / 'compiler.json', {'compiler': metadata['stdout'].read_text(), 'native_flags': old.NATIVE,
                                 'san_flags': old.SAN, 'environment': old.ENV})
    for name in ['lookup', 'controls']:
        old.run(o, ['otool', '-tvV', BUILD / 'native' / name], name + '-assembly')
    fixtures = {}
    for n in o.plan['sizes']:
        for seed in [1, 2, 3]:
            checksum, digest = old.expected_checksum('lookup-hit', n, o.plan['operations'][str(n)], seed)
            fixtures[f'{n}-{seed}'] = {'checksum': checksum, 'query_order_sha256_le_u64': digest}
    save(E / 'fixtures.json', fixtures)
    files = dict(o.inputs)
    files[str(E / 'fixtures.json')] = sha(E / 'fixtures.json')
    for path in BUILD.rglob('*'):
        if path.is_file():
            files[str(path)] = sha(path)
    for path in o.out.rglob('*'):
        if path.is_file() and path.name not in ['status.json', 'build-manifest.json']:
            files[str(path)] = sha(path)
    save(o.out / 'build-manifest.json', {'files_sha256': files, 'status': 'COMPLETE',
                                       'validation': 'Original43 native/san;36 paired new/old exact lookup smokes; fixtures precomputed outside native lease'})


def controls(o):
    paths = old.run(o, [BUILD / 'native/controls'], 'controls')
    assert not paths['stderr'].stat().st_size
    reader = csv.DictReader(paths['stdout'].open())
    rows = list(reader)
    assert reader.fieldnames == ['control', 'repetition', 'iterations', 'requested_block_ns',
                                 'sleep_wall_ns', 'sleep_interruptions', 'checksum'] + FIELDS
    assert len(rows) == 72
    a, c, n, mul, add = 1664525, 1013904223, 2000000, 1, 0
    mask = (1 << 64) - 1
    while n:
        if n & 1:
            mul, add = (a * mul) & mask, (a * add + c) & mask
        a, c = (a * a) & mask, (a * c + c) & mask
        n >>= 1
    expected = (mul + add) & mask
    results = []
    for index, row in enumerate(rows):
        assert None not in row and all(value is not None for value in row.values())
        kind = ['empty', 'cpu', 'block'][index % 3]
        assert row['control'] == kind and int(row['repetition']) == index // 3
        assert int(row['iterations']) == (2000000 if kind == 'cpu' else 0)
        assert int(row['requested_block_ns']) == (20000000 if kind == 'block' else 0)
        assert int(row['checksum']) == (expected if kind == 'cpu' else 1)
        b = bracket(row)
        sensitivity = kind != 'block' or (int(row['sleep_wall_ns']) >= 20000000 and b['recorded_residual_ns'] >= 18000000)
        results.append({'raw': row, 'bracket': b, 'sensitivity_pass': sensitivity})
    save(o.out / 'summary.json', {'rows': results, 'sensitivity_pass': all(r['sensitivity_pass'] for r in results),
        'model_empty_intervals': sum(not r['bracket']['conditional_zero_error_model_nonempty'] for r in results),
        'physical_attribution': 'UNVALIDATED', 'expected_cpu_checksum': expected})


def aa(o):
    fixtures = load(E / 'fixtures.json')
    rows, blocks = [], []
    for block, seed in enumerate(o.plan['seeds']):
        for n in (o.plan['sizes'] if block % 2 == 0 else list(reversed(o.plan['sizes']))):
            group = []
            for position, side in enumerate('ABBA'):
                index = len(rows)
                ops = o.plan['operations'][str(n)]
                paths = old.run(o, old.lookup_cmd(BUILD / 'native/lookup', n, ops, seed), f'{index:03}')
                assert not paths['stderr'].stat().st_size
                r = parse(paths['stdout'], n, ops, seed, fixture=fixtures[f'{n}-{seed}'])
                r.update(index=index, block=block, seed=seed, size=n, position=position, side=side)
                rows.append(r)
                group.append(r)
            for key in ['checksum', 'operations', 'tree_bytes']:
                assert len({r['csv'][key] for r in group}) == 1
            aw, bw = (sum(int(group[i]['csv']['elapsed_ns']) for i in pair) for pair in [(0, 3), (1, 2)])
            at, bt = (sum(int(group[i]['csv']['thread_elapsed_ns']) for i in pair) for pair in [(0, 3), (1, 2)])
            minimum = min(int(r['csv']['elapsed_ns']) for r in group)
            item = {'block': block, 'seed': seed, 'size': n, 'wall_A_ns': aw, 'wall_B_ns': bw,
                    'thread_A_ns': at, 'thread_B_ns': bt, 'wall_effect_percent': 100 * (bw - aw) / aw,
                    'thread_effect_percent_diagnostic': 100 * (bt - at) / at,
                    'minimum_elapsed_ns': minimum,
                    'qualified': abs(bw - aw) * 100 <= aw and minimum >= o.plan['minimum_wall_ns']}
            blocks.append(item)
            save(o.out / 'summary.json', {'rows': rows, 'blocks': blocks, 'complete': False})
            print(json.dumps(item), flush=True)
    save(o.out / 'summary.json', {'rows': rows, 'blocks': blocks, 'complete': True,
        'decision': 'QUALIFIED_BASELINE_ONLY' if all(b['qualified'] for b in blocks) else 'PARK',
        'source_selection': 'NONE', 'physical_attribution': 'UNVALIDATED'})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phase', choices=['build', 'controls', 'aa'])
    parser.add_argument('--publication', required=True)
    args = parser.parse_args()
    owner = Owner(args.phase, args.publication)
    failure = None
    try:
        owner.acquire()
        {'build': build, 'controls': controls, 'aa': aa}[args.phase](owner)
    except BaseException as ex:
        failure = ex
        raise
    finally:
        owner.finish(failure)


if __name__ == '__main__':
    main()
