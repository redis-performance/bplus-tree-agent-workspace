#!/usr/bin/env python3
"""Three scoped execution-count profiles; no timing comparison."""
import csv,hashlib,json,os,subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
SCRATCH=ROOT/'scratch/overnight-counters-001'
BINARY=SCRATCH/'base/build/btree-bench'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m={'binary_sha256':sha(BINARY),'runs':[]}
for name,case,size in [('scan16','scan',16),('scan320','scan',320),('hit16','lookup-hit',16)]:
    out=HERE/name;out.mkdir()
    raw=SCRATCH/(name+'.profraw');data=SCRATCH/(name+'.profdata');export=SCRATCH/(name+'.json')
    args=['--case',case,'--size','100000','--ops','1000000','--member-bytes',str(size),'--seed','1','--warmup-passes','10']
    env=dict(os.environ,LLVM_PROFILE_FILE=str(raw))
    with (out/'bench.csv').open('w') as stdout,(out/'bench.stderr').open('w') as stderr:
        p=subprocess.run([str(BINARY),*args],stdout=stdout,stderr=stderr,env=env,timeout=120)
    row={'name':name,'args':args,'returncode':p.returncode,'raw':str(raw.relative_to(ROOT))}
    if p.returncode==0 and raw.exists():
        commands=[['xcrun','llvm-profdata','merge','-sparse',str(raw),'-o',str(data)],['xcrun','llvm-cov','export',str(BINARY),'-instr-profile='+str(data)]]
        for i,command in enumerate(commands):
            with (out/f'tool{i}.stderr').open('w') as stderr,(export if i==1 else out/'merge.stdout').open('w') as stdout:
                result=subprocess.run(command,stdout=stdout,stderr=stderr,timeout=120)
            assert result.returncode==0,command
        report=json.loads(export.read_text())
        functions=[{'name':f['name'],'count':f['count'],'filenames':[x.replace(str(ROOT),'<workspace>') for x in f['filenames']]} for d in report['data'] for f in d['functions']]
        functions.sort(key=lambda f:(-f['count'],f['name']))
        (out/'function-counts.json').write_text(json.dumps(functions,indent=2)+'\n')
        bench=next(csv.DictReader((out/'bench.csv').open()))
        def count(name):
            return sum(f['count'] for f in functions if f['name']==name or f['name'].endswith(':'+name))
        assertions={'no_insert_calls':count('zbtreeInsertNew')==0,'no_delete_calls':count('zbtreeDelete')==0,
                    'loop_entry_count':count('scan_count' if case=='scan' else 'zbtreeScore')==int(bench['operations'])}
        row.update(assertions=assertions,operations=int(bench['operations']),raw_sha256=sha(raw),data_sha256=sha(data),export_sha256=sha(export),
                   commands=[[a.replace(str(ROOT),'<workspace>') for a in cmd] for cmd in commands])
        assert all(assertions.values()),assertions
    m['runs'].append(row)
    (HERE/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
    print(name,row,flush=True)
