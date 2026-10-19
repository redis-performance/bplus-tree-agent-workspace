#!/usr/bin/env python3
"""Synthetic local parser/arithmetic checks only; no benchmark process executes."""
import ast,json,pathlib,tempfile
from profile_helpers import known_gate
here=pathlib.Path(__file__).resolve().parent;checks=[]
for p in here.glob('*.py'):ast.parse(p.read_text())
checks.append('all Python drivers parse')
commands=json.loads((here/'commands.json').read_text());assert len(commands)==51
assert sum('build/profile' in c['command'] and 'record' in c['command'] for c in commands)==6
assert len(json.loads((here/'aa-schedule.json').read_text()))==48
assert all(r['requested_ops']==50000000 for r in json.loads((here/'profile-schedule.json').read_text())+json.loads((here/'aa-schedule.json').read_text()))
checks.append('51-command profile and fixed 50M schedules consistent')
with tempfile.TemporaryDirectory() as temp:
    p=pathlib.Path(temp)
    def emit(known_count,known_period,other_count,other_period,other_symbol='[unknown]'):
        text=''.join(f'{known_period}\n 100 known_work+0x8\n 200 main+0x10\n\n' for _ in range(known_count))+''.join(f'{other_period}\n 300 {other_symbol}\n 200 main+0x10\n\n' for _ in range(other_count))
        (p/'known-samples.stdout').write_text(text)
        (p/'known-report.stdout').write_text(f'# Total Lost Samples: 0\n# Samples: {known_count+other_count} of event cycles:u\n# Event count (approx.): {known_count*known_period+other_count*other_period}\n')
    emit(20,100,1,1);assert known_gate(p,here)['status']=='pass';checks.append('valid known region passes')
    for label,vals in [('insufficient events',(19,100,1,1)),('80-percent boundary',(20,4,1,20)),('outside region leakage',(20,100,1,1,'outside_work+0x8'))]:
        emit(*vals)
        try:known_gate(p,here)
        except AssertionError:checks.append(label+' rejected')
        else:raise AssertionError(label)
# Independently compare affine composition oracle with explicit small recurrences.
ns={};exec((here/'known-oracle.py').read_text().split('print(json.dumps')[0],ns)
for mul,inc in [(2862933555777941757,3037000493),(6364136223846793005,1442695040888963407)]:
    for n in [0,1,2,3,7,31,127]:
        value=3
        for _ in range(n):value=(value*mul+inc)&((1<<64)-1)
        assert ns['recurrence'](mul,inc,3,n)==value
checks.append('14 small affine-oracle crosschecks pass')
(here/'LOCAL-CHECKS.json').write_text(json.dumps(dict(scope='Local static/synthetic only; no runner or timing',checks=checks),indent=2)+'\n');print(json.dumps(checks))
