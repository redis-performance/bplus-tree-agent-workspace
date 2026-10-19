#!/usr/bin/env python3
"""Synthetic local parser/arithmetic checks only; no benchmark process executes."""
import ast,json,pathlib,tempfile
from profile_helpers import known_gate
here=pathlib.Path(__file__).resolve().parent;checks=[]
for p in here.glob('*.py'):ast.parse(p.read_text())
checks.append('all Python drivers parse')
commands=json.loads((here/'commands.json').read_text());assert len(commands)==104
assert sum(c['kind']=='tree-stat' for c in commands)==12
assert sum('build/profile' in c['command'] and 'record' in c['command'] for c in commands)==12
assert sum(c['kind']=='tree-disabled-stat' for c in commands)==2
assert sum(c['kind']=='original43' for c in commands)==2
assert all(c['fixture']['requested_ops']==50000000 for c in commands if c['kind']=='tree-stat')
assert {c['fixture']['seed'] for c in commands if c['kind']=='tree-stat'}=={1401,1402,1403}
assert {c['variant'] for c in commands if c['kind']=='tree-stat'}=={'control','A'}
assert all(c['fixture']['requested_ops'] in [50000000,2001] for c in commands if c['fixture'])
checks.append('104-command exact two-source profile/counter/disabled/sanitizer schedule consistent')
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
from arm_asm import parse
from profile_helpers import samples
with tempfile.TemporaryDirectory() as temp:
    q=pathlib.Path(temp)/'native.asm'
    q.write_text('x: file format elf64-littleaarch64\n0000000000001000 <fn>:\nx.c:7\n 1000:\td65f03c0 \tret\n')
    parsed=parse(q);assert parsed['fn']['instructions'][0]['bytes']==['d65f03c0'] and parsed['fn']['instructions'][0]['source_line']=='x.c:7'
    for label,text in [('x86 encoding','x: file format elf64-x86-64\n0000000000001000 <fn>:\n 1000:\tc3 \tret\n'),('partial word','x: file format elf64-littleaarch64\n0000000000001000 <fn>:\n 1000:\td65f03 \tret\n')]:
        q.write_text(text)
        try:parse(q)
        except AssertionError:checks.append(label+' rejected')
        else:raise AssertionError(label)
    q.write_text('100\n 100 packed_score+0x4 (inlined)\n 100 zbtreeIteratorNext+0x4\n 200 main+0x10\n\n100\n 300 [unknown]\n 200 known_work+0x8\n')
    rows=samples(q);assert rows[0]['exclusive']=='packed_score' and rows[0]['physical']=='zbtreeIteratorNext';assert rows[1]['exclusive']==rows[1]['physical']=='[unknown]'
    checks.append('ARM same-IP inline physical attribution and ancestor exclusion pass')
old=here.parent/'005-iterator/codegen/base-iterator-next.asm'
oldmap=parse(old);assert len(oldmap['zbtreeIteratorNext']['instructions'])>50
checks.append('retained original ARM iterator objdump parses; compatibility only, no timing transferred')
old2=here.parent/'017-corrected-neon/validation/base-native-codegen.stdout';assert len(parse(old2)['zbtIndexScanSlot']['instructions'])>100
checks.append('retained corrected ARM slot objdump parses; compatibility only')
(here/'LOCAL-CHECKS.json').write_text(json.dumps(dict(scope='Local static/synthetic only; no runner or timing',checks=checks),indent=2)+'\n');print(json.dumps(checks))
