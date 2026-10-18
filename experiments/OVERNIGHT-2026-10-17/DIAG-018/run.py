from pathlib import Path
import datetime,hashlib,json,os,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[2]
F=json.loads((P.parent/'HARNESS-006/freeze.json').read_text());S=R/F['snapshot'];B=S/'build/release/iterator-modes';O=json.loads((P/'freeze.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
assert json.loads((P/'validation.json').read_text())['status']=='pass'
assert sha(R/O['binary'])==O['binary_sha256'] and sha(R/O['source'])==O['source_sha256']
assert not(P/'manifest.json').exists();(P/'raw').mkdir()
for n,h in F['files'].items():assert sha(S/n)==h
assert sha(B)==json.loads((P.parent/'HARNESS-006/binaries.json').read_text())['release']
M=dict(status='running',started_utc=utc(),base_commit=F['base_commit'],plan_sha256=sha(P/'PLAN.md'),runner_sha256=sha(Path(__file__)),binary=str(B.relative_to(R)),binary_sha256=sha(B),observer=O,seeds=[53101,53113],blocks=6,runs=[],warmup=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def spec(seed,block,step,label,ops=20000000):
    stem=f's{seed}-b{block}-p{step}-{label}';meta='raw/'+stem+'.json'
    command=[O['binary'],str((P/meta).relative_to(R)),'110',str(B.relative_to(R)),'--size','95','--ops',str(ops),'--seed',str(seed),'--warmup-passes','3','--direction','forward','--encoding','alternating-zero','--construction','trimmed','--member-bytes','16','--mask','6']
    return dict(seed=seed,block=block,step=step,label=label,policy='file' if label=='A' else 'pipe',command=command,csv='raw/'+stem+'.csv',stderr='raw/'+stem+'.stderr',completion=meta)
schedule=[spec(seed,block,step,label) for block in range(1,7) for seed in (M['seeds'] if block%2 else M['seeds'][::-1]) for step,label in enumerate('ABBA',1)]
(P/'schedule.json').write_text(json.dumps(schedule,indent=2)+'\n');M['schedule_sha256']=sha(P/'schedule.json');save()
def execute(row):
    row['load_before']=os.getloadavg();row['started_utc']=utc()
    with (P/row['csv']).open('wb') as out,(P/row['stderr']).open('wb') as err:
        row['start_monotonic_ns']=time.monotonic_ns();row['parent_clock_start_ns']=time.clock_gettime_ns(time.CLOCK_MONOTONIC)
        try:
            pipe=row['policy']=='pipe'
            result=subprocess.run(row['command'],cwd=R,stdout=subprocess.PIPE if pipe else out,stderr=subprocess.PIPE if pipe else err,timeout=120)
            row['parent_clock_return_ns']=time.clock_gettime_ns(time.CLOCK_MONOTONIC);rc=result.returncode
            if pipe:out.write(result.stdout);err.write(result.stderr)
        except subprocess.TimeoutExpired:row['parent_clock_return_ns']=time.clock_gettime_ns(time.CLOCK_MONOTONIC);rc='timeout'
        row['end_monotonic_ns']=time.monotonic_ns()
    row.update(returncode=rc,ended_utc=utc(),load_after=os.getloadavg())
    for k in ['csv','stderr','completion']:
        if (P/row[k]).exists():row[k+'_sha256']=sha(P/row[k])
    return row
M['warmup'].append(execute(spec(53101,0,0,'A',1000000)));save();assert M['warmup'][0]['returncode']==0
start=time.monotonic()
for row in schedule:
    if time.monotonic()-start>180:M['status']='budget-exhausted';save();raise SystemExit(3)
    M['runs'].append(execute(row));save()
    if row['returncode']!=0:M['status']='failed';save();raise SystemExit(4)
    if row['step']==4:print(row['block'],row['seed'],len(M['runs']),flush=True)
M.update(status='complete',ended_utc=utc(),seconds=time.monotonic()-start,binary_sha256_after=sha(B));save()
assert M['binary_sha256']==M['binary_sha256_after']
for n,h in F['files'].items():assert sha(S/n)==h
assert sha(R/O['binary'])==O['binary_sha256'] and sha(R/O['source'])==O['source_sha256']
