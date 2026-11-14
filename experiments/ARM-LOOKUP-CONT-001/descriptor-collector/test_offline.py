#!/usr/bin/env python3
"""Pure/offline collector tests. Never build or invoke a benchmark/fleet command."""
import copy
from contextlib import ExitStack
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import types
import unittest
from unittest.mock import patch

EXP = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('collector', EXP / 'fleet_descriptor_guards.py')
c = importlib.util.module_from_spec(spec)
# Import itself must not execute commands or inspect a live reservation.
with patch.object(subprocess, 'run', side_effect=AssertionError('Import spawned child')), \
     patch.object(subprocess, 'Popen', side_effect=AssertionError('Import spawned child')):
    spec.loader.exec_module(c)


def row(case='member-forward', variant='base', block=0, slot=0):
    return dict(verified=True, revision=0, mode='measure', case=case, seed=17,
                sweeps=c.CASES[case], members=529, **c.expected(case, c.CASES[case]),
                elapsed_ns=1000000000, owned_bytes_before=100000, owned_bytes_after=100000,
                owned_bytes_after_validation=100000, variant=variant, block=block,
                slot=slot, label='ABBA'[slot], binary_sha256='0' * 64 if slot in (0, 3) or
                variant == 'base' else variant.lower() * 64)


def grid(variants=('base',)):
    return [row(case, v, block, slot) for v in variants for case in c.CASES
            for block in range(3) for slot in range(4)]


class Offline(unittest.TestCase):
    def test_frozen_inputs(self):
        for path, digest in c.REFEREE_PINS.items():
            self.assertEqual(c.sha(EXP / path), digest, path)
        self.assertEqual(c.sha(EXP / 'current/src/zset_btree.c'), c.SOURCE_PINS['base'])

    def test_saved_384_correctness_rows(self):
        count = 0
        for path in (EXP / 'descriptor-guards/correctness').glob('*.jsonl'):
            for line in path.read_text().splitlines():
                r = json.loads(line)
                c.check_row(r, r['case'], r['seed'], r['sweeps'], 'verify')
                count += 1
        self.assertEqual(count, 384)

    def test_independent_closed_forms(self):
        f, r = c.expected('member-forward', 1), c.expected('member-reverse', 1)
        self.assertEqual(f['ops'], 529)
        self.assertEqual(f['scores'], 529 * 530 // 2)
        self.assertEqual(f['weighted'], 529 * 530 * 1059 // 6)
        self.assertEqual(r['weighted'], 530 * f['scores'] - f['weighted'])
        for case, lo, hi in [('lookup-inline', 1, 465), ('lookup-external', 466, 529)]:
            x = c.expected(case, 1)
            n = hi - lo + 1
            self.assertEqual(x['ops'], 2 * n)
            self.assertEqual(x['hits'], n)
            self.assertEqual(x['scores'], (lo + hi) * n // 2 - 123 * n)
            self.assertEqual(x['weighted'], (lo + hi) * n // 2)
        for case in c.CASES:
            values = c.expected(case, 2000000)
            self.assertTrue(all(0 <= n < 2**64 for n in values.values()))
            self.assertLess(values['scores'], 2**63)

    def test_bad_count_and_case(self):
        for value in [0, -1, 2000001, True, 2.0, '2']:
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                c.expected('lookup-inline', value)
        with self.assertRaises(RuntimeError):
            c.expected('other', 1)

    def test_bad_row(self):
        for key, value in [('verified', 1), ('revision', False), ('members', 528), ('seed', 29),
                           ('sweeps', 5), ('mode', 'verify'), ('case', 'member-reverse'),
                           ('elapsed_ns', 249999999), ('elapsed_ns', float('nan')),
                           ('owned_bytes_before', 0), ('owned_bytes_after', -1),
                           ('owned_bytes_after_validation', True)]:
            r = row()
            r[key] = value
            with self.subTest(key=key, value=value), self.assertRaises(RuntimeError):
                c.check_row(r, 'member-forward', 17, 1000000, 'measure')
        for key in c.expected('member-forward', 1):
            for value in [row()[key] + 1, True, str(row()[key])]:
                r = row()
                r[key] = value
                with self.subTest(key=key, value=value), self.assertRaises(RuntimeError):
                    c.check_row(r, 'member-forward', 17, 1000000, 'measure')
        r = row()
        del r['elapsed_ns']
        r['mode'] = 'verify'
        c.check_row(r, 'member-forward', 17, 1000000, 'verify')
        r['elapsed_ns'] = 0
        with self.assertRaises(RuntimeError):
            c.check_row(r, 'member-forward', 17, 1000000, 'verify')

    def test_exact_grid(self):
        q = c.analyze(grid(), ['base'], 17, True)
        self.assertEqual(q['rows'], 48)
        self.assertEqual(len(q['blocks']), 12)
        self.assertTrue(q['passed'])
        r = c.analyze(grid('ABC'), list('ABC'), 17, False)
        self.assertEqual(r['rows'], 144)
        self.assertEqual(len(r['blocks']), 36)
        self.assertTrue(r['passed'])

    def test_missing_duplicate_reordered_rows(self):
        full = grid()
        bad = [full[:-1], full + [full[-1]], [full[1], full[0], *full[2:]],
               [full[0], *full[:-1]]]
        for rows in bad:
            with self.subTest(rows=len(rows)), self.assertRaises(RuntimeError):
                c.analyze(rows, ['base'], 17, True)
        for variants in [[], ['base', 'base'], ['A']]:
            with self.assertRaises(RuntimeError):
                c.analyze(full, variants, 17, True)

    def test_one_percent_duration_boundary(self):
        for delta, aa, comparison in [(10000000, True, True), (10000001, False, False),
                                      (-10000000, True, True), (-10000001, False, True)]:
            rr = grid()[:4]
            for r in rr[1:3]:
                r['elapsed_ns'] += delta
            self.assertEqual(c.block_result(rr, True)['passed'], aa)
            self.assertEqual(c.block_result(rr, False)['passed'], comparison)
        rr = grid()[:4]
        rr[0]['elapsed_ns'] = 249999999
        self.assertFalse(c.block_result(rr, False)['passed'])

    def test_both_immediate_memory_endpoints(self):
        for key in c.MEMORY:
            for delta, comparison in [(1000, True), (1001, False), (-1000, True)]:
                rr = grid()[:4]
                for r in rr[1:3]:
                    r[key] += delta
                self.assertFalse(c.block_result(rr, True)['passed'])
                self.assertEqual(c.block_result(rr, False)['passed'], comparison)
        rr = grid()[:4]
        rr[1]['owned_bytes_after_validation'] = 1
        self.assertTrue(c.block_result(rr, True)['passed'])
        rr[1]['owned_bytes_after'] += 2001
        self.assertFalse(c.block_result(rr, False)['passed'])

    def test_unstable_memory_and_no_case_cancellation(self):
        rows = grid()
        rows[-1]['owned_bytes_after'] += 1
        with self.assertRaises(RuntimeError):
            c.analyze(rows, ['base'], 17, True)
        rows = grid(('A',))
        for r in rows:
            if r['label'] == 'B':
                r['elapsed_ns'] = 1010000001 if r['case'] == 'lookup-external' else 900000000
        report = c.analyze(rows, ['A'], 17, False)
        self.assertFalse(report['passed'])
        self.assertEqual(sum(not b['passed'] for b in report['blocks']), 3)

    def test_exclusions_required_and_source_bound(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            with self.assertRaises(FileNotFoundError):
                c.exclusions(root)
            p = root / 'H6-exclusions.json'
            p.write_text('{}')
            self.assertEqual(c.exclusions(root), {})
            good = {'B': {'source_sha256': c.SOURCE_PINS['B'], 'reason': 'guard rejection'}}
            p.write_text(json.dumps(good))
            self.assertEqual(c.exclusions(root), good)
            for bad in [{'B': {'source_sha256': '0' * 64, 'reason': 'stale'}},
                        {'B': {'source_sha256': c.SOURCE_PINS['B'], 'reason': ''}},
                        {'base': good['B']}, {'D': good['B']}, [], {'B': 'rejected'}]:
                p.write_text(json.dumps(bad))
                with self.subTest(bad=bad), self.assertRaises(RuntimeError):
                    c.exclusions(root)

    def test_discovery_scope_and_eligibility(self):
        meta = dict(cohort='native', seed='17', source_freeze=c.UPSTREAM,
                    baseline_sha256='0' * 64, variants={'B': {
                        'source_sha256': c.SOURCE_PINS['B'], 'binary_sha256': 'b' * 64}})
        report = {'variants': {'B': {'eligible': True}}}
        c.discovery_gate(meta, report, 'B', 'native', '0' * 64)
        for key, value in [('cohort', 'gcc15-lto'), ('seed', '29'), ('source_freeze', 'other'),
                           ('baseline_sha256', '1' * 64)]:
            bad = copy.deepcopy(meta)
            bad[key] = value
            with self.subTest(key=key), self.assertRaises(RuntimeError):
                c.discovery_gate(bad, report, 'B', 'native', '0' * 64)
        for key in ['source_sha256', 'binary_sha256']:
            bad = copy.deepcopy(meta)
            bad['variants']['B'][key] = 'bad'
            with self.assertRaises(RuntimeError):
                c.discovery_gate(bad, report, 'B', 'native', '0' * 64)
        for eligible in [False, 1, 'true']:
            with self.assertRaises(RuntimeError):
                c.discovery_gate(meta, {'variants': {'B': {'eligible': eligible}}}, 'B', 'native', '0' * 64)

    def test_artifact_escape_and_one_shot(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            (root / 'escape').symlink_to('/tmp')
            for value in ['/tmp/file', '../escape-file', 'escape/file']:
                with self.assertRaises(RuntimeError):
                    c.contained(root, value)
            path = c.contained(root, 'once.json')
            c.write_new(path, {'first': True})
            with self.assertRaises(FileExistsError):
                c.write_new(path, {'overwritten': True})
            self.assertEqual(c.read(path), {'first': True})
        self.assertEqual(c.phase_name('arm', 'native', 17), 'H6-descriptor-arm-native-r0-seed17')
        for triple in [('amd', 'native', 17), ('arm', 'other', 17), ('arm', 'native', 18)]:
            with self.assertRaises(RuntimeError):
                c.phase_name(*triple)

    def test_lease_and_isolation_with_mocked_state_only(self):
        for failure in [None, 'owner', 'state', 'deadline', 'saved', 'timer', 'coordinator',
                        'ticks', 'affinity', 'architecture', 'offline', 'sibling', 'container',
                        'compiler', 'collector', 'benchmark', 'intel_smt', 'intel_profiler']:
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as name, ExitStack() as stack:
                root = Path(name)
                lease = dict(owner='bplus ARM-LOOKUP-CONT-001', state='RESERVED', deadline=1000,
                             coordinator_pid=900001, coordinator_ticks='123', sibling50_online='1')
                if failure in ('owner', 'state'):
                    lease[failure] = 'other'
                if failure == 'deadline':
                    lease['deadline'] = 500
                (root / 'reservation.json').write_text(json.dumps(lease))
                coord = root / 'proc/900001'
                coord.mkdir(parents=True)
                fields = ['R' if failure == 'coordinator' else 'T', *(['0'] * 18),
                          '999' if failure == 'ticks' else '123']
                (coord / 'stat').write_text('900001 (coordinator) ' + ' '.join(fields))
                cpu = root / 'sys/devices/system/cpu/cpu2'
                (cpu / 'topology').mkdir(parents=True)
                (cpu / 'online').write_text('0' if failure == 'offline' else '1')
                (cpu / 'topology/thread_siblings_list').write_text('2,50')
                sibling = root / 'sys/devices/system/cpu/cpu50'
                sibling.mkdir()
                (sibling / 'online').write_text('1' if failure in ('sibling', 'intel_smt') else '0')
                if failure in ('compiler', 'collector', 'benchmark'):
                    proc = root / 'proc/900002'
                    proc.mkdir()
                    (proc / 'stat').write_text('900002 (other) R ' + ' '.join(['0'] * 19))
                    (proc / 'comm').write_text('cc1' if failure == 'compiler' else 'python3')
                    arg = ('fleet_compare.py' if failure == 'collector' else
                           str(root / 'bin/lookup') if failure == 'benchmark' else 'cc1')
                    (proc / 'cmdline').write_bytes(arg.encode() + b'\0')

                def fake_path(value):
                    value = str(value)
                    return root / value.lstrip('/') if value.startswith(('/proc', '/sys')) else Path(value)

                def fake_run(command, **kwargs):
                    if command[:2] == ['systemctl', 'is-active']:
                        return types.SimpleNamespace(returncode=1 if failure == 'timer' else 0)
                    if command[:2] == ['systemctl', 'show']:
                        return types.SimpleNamespace(returncode=0, stdout='active' if failure == 'intel_profiler' else 'inactive')
                    raise AssertionError('Unexpected command ' + str(command))

                host = 'intel' if failure in ('intel_smt', 'intel_profiler') else 'arm'
                stack.enter_context(patch.object(c, 'Path', side_effect=fake_path))
                stack.enter_context(patch.object(c.time, 'time', return_value=100))
                stack.enter_context(patch.object(c.os, 'sched_getaffinity', return_value={1} if failure == 'affinity' else {0}))
                stack.enter_context(patch.object(c.platform, 'machine', return_value='wrong' if failure == 'architecture' else
                                                 'x86_64' if host == 'intel' else 'aarch64'))
                stack.enter_context(patch.object(c.subprocess, 'run', side_effect=fake_run))
                stack.enter_context(patch.object(c.subprocess, 'check_output', return_value='container' if failure == 'container' else ''))
                saved = [900001, '123', 999] if failure == 'saved' else None
                if failure:
                    with self.assertRaises(RuntimeError):
                        c.leasecheck(root, host, saved, 540)
                else:
                    self.assertEqual(c.leasecheck(root, host, saved, 540), [900001, '123', 1000])


if __name__ == '__main__':
    unittest.main(verbosity=2)
