#!/usr/bin/env python3
"""Check the decoder referee; no assertion about elapsed speed."""
import csv
import io
from pathlib import Path
import subprocess
import sys
import unittest

BINARY = str(Path(sys.argv.pop(1)).resolve()) if len(sys.argv) > 1 else 'build/decoder/base/decoder-bench'


def invoke(*args):
    return subprocess.run([BINARY, *map(str, args)], capture_output=True, text=True, timeout=60)


class DecoderTests(unittest.TestCase):
    def test_bit_reference_and_batch_checksum(self):
        p = invoke('--self-test')
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn('PASS fixtures=1820', p.stdout)

    def test_geometry_and_sample_accounting(self):
        for width in (0, 1, 8, 31, 57, 60, 63, 64):
            for reverse in (0, 1):
                rows_by_rounds = []
                for rounds in (1, 3):
                    p = invoke('--width', width, '--reversed', reverse, '--count', 7,
                               '--leaves', 2, '--rounds', rounds, '--samples', 3, '--warmup', 1, '--seed', 987)
                    self.assertEqual(p.returncode, 0, p.stderr)
                    rows = list(csv.DictReader(io.StringIO(p.stdout)))
                    self.assertEqual(len(rows), 3)
                    offsets = {(i*width) % 8 for i in range(7)}
                    crossings = sum(width + (i*width) % 8 > 64 for i in range(7))*2
                    for i, row in enumerate(rows):
                        self.assertNotIn(None, row)
                        self.assertEqual(int(row['sample']), i)
                        self.assertEqual(int(row['operations']), 14*rounds)
                        self.assertEqual(int(row['offset_mask']), sum(1 << o for o in offsets))
                        self.assertEqual(int(row['crossings_per_round']), crossings)
                        self.assertGreaterEqual(float(row['elapsed_ns']), 0)
                        self.assertEqual(row['cycles'], '')
                        self.assertEqual(row['instructions'], '')
                    self.assertEqual(len({r['checksum'] for r in rows}), 1)
                    rows_by_rounds.append(rows[0])
                first, third = rows_by_rounds
                self.assertEqual(first['fixture_hash'], third['fixture_hash'])
                self.assertEqual(int(third['checksum']), int(first['checksum'])*3 % 2**64)

    def test_bad_arguments(self):
        for args in [('--width', 65), ('--width', -1), ('--samples', 0), ('--count', 97),
                     ('--width', 64, '--score-shift', 1), ('--reversed', 2), ('--rounds', 'x'), ('--width',)]:
            self.assertEqual(invoke(*args).returncode, 2)

    def test_optional_counters_report_availability(self):
        p = invoke('--samples', 1, '--rounds', 1, '--warmup', 1, '--counters')
        self.assertEqual(p.returncode, 0, p.stderr)
        rows = list(csv.DictReader(io.StringIO(p.stdout)))
        self.assertEqual(rows[0]['kind'], 'time')
        for row in rows:
            self.assertNotIn(None, row)
        if len(rows) == 1:
            self.assertIn('counter_status=', p.stderr)
        else:
            self.assertEqual(rows[1]['kind'], 'counter')
            self.assertGreater(int(rows[1]['instructions']), 0)


if __name__ == '__main__':
    unittest.main()
