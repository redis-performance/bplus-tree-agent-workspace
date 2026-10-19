#!/usr/bin/env python3
"""Fixed held-out ARM schedule, executed only after root's idle-runner grant."""
import argparse,csv,datetime,hashlib,io,json,os,pathlib,subprocess,time
from audit import inputs,expected,audit,sha,HERE
p=argparse.ArgumentParser();p.add_argument('--phase',choices=['aa','confirm'],required=True);p.add_argument('--repo',type=pathlib.Path,required=True);p.add_argument('--grant',type=pathlib.Path,required=True);p.add_argument('--out',type=pathlib.Path,required=True);p.add_argument('--aa',type=pathlib.Path);a=p.parse_args()
f,schedule=inputs();grant_text=a.grant.read_text();grant=json.loads(grant_text);v=grant['selected']
assert v in ['A','B','C'] and grant['root_authorized'] is True
for k in ['selection_revision','root_grant','idle_handoff_utc']:assert isinstance(grant[k],str) and grant[k]
assert sorted(os.sched_getaffinity(0))==[2],'requires lease job pinned to CPU2'
if a.phase=='confirm':
    assert a.aa is not None
    control=audit(a.aa);assert control['qualified'] and control['selected']==v
    assert json.loads((a.aa/'result.json').read_text())['grant']==grant
roots={k:a.repo/f['sources'][k]['root'] for k in ['base',v]};pins=expected(v)
a.out.mkdir(parents=True,exist_ok=False);raw=a.out/'raw';raw.mkdir();started=time.monotonic();end_limit=started+300
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
state=dict(phase=a.phase,selected=v,status='running',started_utc=now(),grant=grant,grant_text=grant_text,grant_sha256=hashlib.sha256(grant_text.encode()).hexdigest(),driver_affinity=sorted(os.sched_getaffinity(0)),processes=[],source_adoption='NONE',input_hashes={n:sha(HERE/n) for n in ['freeze.json','driver.py','audit.py','schedule.json','discovery-freeze.json']})
if a.phase=='confirm':state['aa_result_sha256']=sha(a.aa/'result.json')
def save():
    tmp=a.out/'result.tmp';tmp.write_text(json.dumps(state,indent=2)+'\n');tmp.replace(a.out/'result.json')
def verify():
    got={k:{name:sha(roots[k]/name) for name in pins[k]} for k in roots};assert got==pins,'source/referee/binary mismatch';return got
save()
try:
    state['initial_hashes']=verify();save()
    for s in schedule:
        target=v if a.phase=='confirm' and s['position'] in [1,2] else 'base'
        remaining=end_limit-time.monotonic();assert remaining>0,'total phase cap'
        args=['--case','scan','--size',str(s['size']),'--ops','5000000','--member-bytes','16','--seed',str(s['seed'])]
        r={**s,'binary':target,'started_utc':now(),'argv':['<'+target+'>/build/btree-bench',*args]};state['processes'].append(r);save()
        try:
            proc=subprocess.run([str(roots[target]/'build/btree-bench'),*args],capture_output=True,timeout=min(30,remaining))
            stdout,stderr=proc.stdout,proc.stderr;r['returncode']=proc.returncode
        except subprocess.TimeoutExpired as e:
            stdout,stderr=e.stdout or b'',e.stderr or b'';r['returncode']=124
        r['finished_utc']=now();op=raw/f"{s['index']:03d}.stdout";ep=op.with_suffix('.stderr');op.write_bytes(stdout);ep.write_bytes(stderr)
        r['stdout_sha256']=sha(op);r['stderr_sha256']=sha(ep);save()
        assert r['returncode']==0 and not stderr,'process failure or stderr'
        data=list(csv.DictReader(io.StringIO(stdout.decode())));assert len(data)==1;r['row']=data[0];save()
    state['final_hashes']=verify();assert time.monotonic()<=end_limit;state['status']='complete'
except BaseException as e:
    state['status']='failed';state['failure_type']=type(e).__name__;state['failure']=str(e);raise
finally:
    state['finished_utc']=now();state['wall_seconds']=time.monotonic()-started;save()
result=audit(a.out,a.aa);(a.out/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'phase':a.phase,'qualified':result['qualified'],'selected':v}))
