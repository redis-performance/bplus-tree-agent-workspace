from pathlib import Path
import hashlib,json,re
P=Path(__file__).resolve().parent;R=P.parents[2];D=P/'attempt-002'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
M=json.loads((D/'manifest.json').read_text());assert M['status']=='complete' and len(M['runs'])==96
rows=[]
for r in M['runs']:
    assert r['returncode']==0
    for stream in ['stdout','stderr']:assert sha(D/(r['name']+'.'+stream))==r[stream+'_sha256']
    if r['stage']!='run':continue
    out=(D/(r['name']+'.stdout')).read_text()
    if r['target']=='upstream':
        assert '43 tests, 43 passed, 0 failed' in out or ('43 passed' in out and '0 failed' in out)
        continue
    lines=out.splitlines();assert sum(x.startswith('FIXTURE ') for x in lines)==96
    summary=next(x for x in lines if x.startswith('PASS '));physical=next(x for x in lines if x.startswith('PHYSICAL '))
    parsed=dict(re.findall(r'(\w+)=([0-9a-f]+)',summary));observed=dict(re.findall(r'(\w+)=([0-9a-f]+)',physical))
    assert parsed['fixtures']=='96' and all(int(observed[k])>0 for k in ['zero','partial','full','shifted','forward','reversed','growth','shrinkage'])
    rows.append(dict(policy=r['policy'],variant=r['variant'],kind=r['kind'],summary=parsed,physical=observed,stdout_sha256=r['stdout_sha256']))
assert len(rows)==24
assert len({r['summary']['logical'] for r in rows})==1
assert len({r['summary']['checks'] for r in rows})==1
equal={p:len({r['stdout_sha256'] for r in rows if r['policy']==p})==1 for p in ['ambient','exact','round16']}
assert equal['exact'] and equal['round16']
for desc in M['snapshots'].values():
    for n,h in desc['files'].items():assert sha(R/desc['path']/n)==h
for n,h in M['root_hashes'].items():assert sha(R/n)==h
result=dict(status='pass',cells=24,original_test_runs=24,fixtures_per_cell=96,logical_digest=rows[0]['summary']['logical'],controlled_output_equality={p:equal[p] for p in ['exact','round16']},ambient_output_equality_descriptive=equal['ambient'],rows=rows)
(P/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
