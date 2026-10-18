from pathlib import Path
import datetime,hashlib,json,subprocess,sys,time,shutil
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-diag018';assert not S.exists();S.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
shutil.copy2(P/'wait_observer.c',S/'wait_observer.c');rows=[]
def run(name,cmd,pipe=False):
    row=dict(name=name,command=cmd,started_utc=utc());out=P/(name+'.stdout');err=P/(name+'.stderr')
    with out.open('wb') as so,err.open('wb') as se:
        r=subprocess.run(cmd,cwd=R,stdout=subprocess.PIPE if pipe else so,stderr=subprocess.PIPE if pipe else se,timeout=120)
        if pipe:so.write(r.stdout);se.write(r.stderr)
    row.update(ended_utc=utc(),returncode=r.returncode,stdout_sha256=sha(out),stderr_sha256=sha(err));rows.append(row)
    (P/'validation.json').write_text(json.dumps(dict(status='running',runs=rows),indent=2)+'\n');return r
b=str((S/'observer').relative_to(R));cmd=['cc','-std=c11','-O2','-Wall','-Wextra','-Werror',str((S/'wait_observer.c').relative_to(R)),'-o',b];assert run('build',cmd).returncode==0
for policy in ['file','pipe']:
 for mode in ['success','nonzero','timeout']:
    tag=policy+'-'+mode;meta=P/(tag+'.json');code="import os,time;os.write(1,b'out\\x00ok\\n');os.write(2,b'err\\n');"+('time.sleep(3)' if mode=='timeout' else 'raise SystemExit(7)' if mode=='nonzero' else '')
    cmd=[b,str(meta.relative_to(R)),'1',sys.executable,'-c',code];result=run(tag,cmd,policy=='pipe');m=json.loads(meta.read_text())
    assert result.returncode==m['child_status']==(137 if mode=='timeout' else 7 if mode=='nonzero' else 0)
    assert bool(m['timed_out'])==(mode=='timeout')
    assert (P/(tag+'.stdout')).read_bytes()==b'out\x00ok\n' and (P/(tag+'.stderr')).read_bytes()==b'err\n'
(P/'validation.json').write_text(json.dumps(dict(status='pass',runs=rows),indent=2)+'\n')
(P/'freeze.json').write_text(json.dumps(dict(binary=b,binary_sha256=sha(R/b),source=str((S/'wait_observer.c').relative_to(R)),source_sha256=sha(S/'wait_observer.c'),plan_sha256=sha(P/'PLAN.md'),frozen_utc=utc(),clock='clock_gettime(CLOCK_MONOTONIC) both observer and Python parent'),indent=2)+'\n');print('PASS six transport/status/timeout controls')
