#!/usr/bin/env python3
"""Independently recompute every saved row's checksums from the fixture spec."""
import json
from pathlib import Path

here = Path(__file__).resolve().parent
lengths = [0, *range(1, 18), 24, 32, 64, 127, 128, 129, 252, 253, 254,
           255, 318, 319, 320, 321, 512, 1024]
members = []
for length in lengths:
    for replica in range(16 if length else 1):
        member = bytearray(0 if offset % 7 == 0 else (offset * 37 + replica * 11) % 256
                           for offset in range(length))
        if length:
            member[0] = replica
        members.append(bytes(member))
assert len(members) == len(set(members)) == 529
count = 0
for path in sorted((here / 'correctness').glob('*.jsonl')):
    for line in path.read_text().splitlines():
        row = json.loads(line)
        assert row['verified'] and row['mode'] == 'verify' and 'elapsed_ns' not in row
        case = row['case']
        want = dict(ops=0, hits=0, bytes=0, samples=0, scores=0, weighted=0)
        if case.startswith('member-'):
            order = list(range(len(members)))
            if case == 'member-reverse':
                order.reverse()
            for ordinal, index in enumerate(order, 1):
                member = members[index]
                sample = (member[0] + 257 * member[len(member) // 2] + 65537 * member[-1]
                          if member else 0)
                want['ops'] += 1
                want['hits'] += 1
                want['bytes'] += len(member)
                want['samples'] += sample * ordinal
                want['scores'] += index + 1
                want['weighted'] += (index + 1) * ordinal
        else:
            for index, member in enumerate(members):
                if (len(member) < 320) != (case == 'lookup-inline'):
                    continue
                want['ops'] += 2
                want['hits'] += 1
                want['scores'] += index + 1 - 123
                want['weighted'] += index + 1
        for key, value in want.items():
            assert row[key] == value * row['sweeps'], (path.name, case, key, row[key], value)
        count += 1
assert count == 384, count
print(json.dumps(dict(verified=True, independent_checksum_rows=count,
                     distinct_fixture_members=len(members), local_measurement_calls=0)))
