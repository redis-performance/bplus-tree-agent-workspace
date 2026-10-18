from pathlib import Path
import datetime,hashlib,json,os,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[2]
F=json.loads((P.parent/'HARNESS-006/freeze.json').read_text());S=R/F['snapshot'];B=S/'build/release/iterator-modes'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
assert not (P/'manifest.json').exists();(P/'raw').mkdir()
for n,h in F['files'].items():assert sha(S/n)==h
assert sha(B)==json.loads((P.parent/'HARNESS-006/binaries.json').read_text())['release']
CELLS=[dict(name='int-trim-f0',encoding='integer',mask=0),dict(name='zero-trim-f6',encoding='alternating-zero',mask=6)]
M=dict(status='running',started_utc=utc(),base_commit=F['base_commit'],plan_sha256=sha(P/'PLAN.md'),runner_sha256=sha(Path(__file__)),freeze_sha256=sha(P.parent/'HARNESS-006/freeze.json'),binary=str(B.relative_to(R)),binary_sha256=sha(B),cells=CELLS,seeds=[49109,49121],blocks=6,policies=['file','pipe'],protocols=['contrast','placebo'],runs=[],warmup=[],bookkeeping=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def command(c,seed,ops=20000000):
    return [str(B.relative_to(R)),'--size','95','--ops',str(ops),'--seed',str(seed),'--warmup-passes','3','--direction','forward','--encoding',c['encoding'],'--construction','trimmed','--member-bytes','16','--mask',str(c['mask'])]
def launch(cmd,out,err,policy="file"):
    payload=None
    started=utc();cpu0=time.process_time_ns();t=time.monotonic_ns()
    try:
        if policy=='pipe':
            result=subprocess.run(cmd,cwd=R,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120);rc=result.returncode;payload=(result.stdout,result.stderr)
        else:rc=subprocess.run(cmd,cwd=R,stdout=out,stderr=err,timeout=120).returncode
    except subprocess.TimeoutExpired as exc:
        rc='timeout';payload=(exc.stdout or b'',exc.stderr or b'') if policy=='pipe' else None
    end=time.monotonic_ns();cpu1=time.process_time_ns()
    row=dict(command=cmd,started_utc=started,ended_utc=utc(),start_monotonic_ns=t,end_monotonic_ns=end,parent_cpu_start_ns=cpu0,parent_cpu_end_ns=cpu1,returncode=rc)
    return row,payload
def complete(row):
    for key in ['csv','stderr']:row[key+'_sha256']=sha(P/row[key])
def flush(rows,meta):
    t=time.monotonic_ns();c=time.process_time_ns()
    for row in rows:complete(row)
    save()
    M['bookkeeping'].append(dict(**meta,wall_ns=time.monotonic_ns()-t,cpu_ns=time.process_time_ns()-c,manifest_bytes=(P/'manifest.json').stat().st_size))
order=[('file','contrast'),('pipe','contrast'),('file','placebo'),('pipe','placebo')];schedule=[]
for block in range(1,7):
    cells=order[(block-1)%4:]+order[:(block-1)%4]
    seeds=M['seeds'] if block%2 else M['seeds'][::-1]
    for seed in seeds:
        for policy,protocol in cells:
            group=[]
            for step,label in enumerate('ABBA',1):
                pred=CELLS[0] if protocol=='contrast' and label=='B' else CELLS[1]
                stem=f'{policy}-{protocol}-s{seed}-b{block}-p{step}-{label}'
                meta=dict(policy=policy,protocol=protocol,seed=seed,block=block,step=step,label=label)
                rows=[]
                for role,cell in [('predecessor',pred),('target',CELLS[1])]:
                    rows.append(dict(**meta,role=role,cell=cell['name'],command=command(cell,seed),csv='raw/'+stem+'-'+role+'.csv',stderr='raw/'+stem+'-'+role+'.stderr'))
                group.append(rows)
            schedule.append(group)
(P/'schedule.json').write_text(json.dumps(schedule,indent=2)+'\n');M['schedule_sha256']=sha(P/'schedule.json');save()
with (P/'raw/warmup.csv').open('w') as so,(P/'raw/warmup.stderr').open('w') as se:r,_=launch(command(CELLS[1],49109,1000000),so,se)
r.update(csv='raw/warmup.csv',stderr='raw/warmup.stderr');complete(r);M['warmup'].append(r);save();assert r['returncode']==0
start=time.monotonic();last=None
with (P/'journal.jsonl').open('w',buffering=1) as journal:
    for group in schedule:
        pending=[]
        for rows in group:
            if time.monotonic()-start>400:M['status']='budget-exhausted';save();raise SystemExit(3)
            pr,tr=rows;load=os.getloadavg()
            with (P/pr['csv']).open('w') as po,(P/pr['stderr']).open('w') as pe,(P/tr['csv']).open('w') as to,(P/tr['stderr']).open('w') as te:
                prow,pdata=launch(pr['command'],po,pe,pr['policy']);pr.update(prow);tdata=None
                if pr['returncode']==0:
                    trow,tdata=launch(tr['command'],to,te,tr['policy']);tr.update(trow)
                else:tr['returncode']='skipped'
                for payload,out,err in [(pdata,po,pe),(tdata,to,te)]:
                    if payload is not None:out.buffer.write(payload[0]);err.buffer.write(payload[1])
            if last is not None:
                pr['previous_target_gap_ns']=pr['start_monotonic_ns']-last['end_monotonic_ns']
                pr['previous_target_parent_cpu_ns']=pr['parent_cpu_start_ns']-last['parent_cpu_end_ns']
            if tr['returncode']!='skipped':
                tr['coordinator_launch_gap_ns']=tr['start_monotonic_ns']-pr['end_monotonic_ns']
                tr['coordinator_launch_cpu_ns']=tr['parent_cpu_start_ns']-pr['parent_cpu_end_ns']
            for row in rows:row.update(load_before_pair=load,load_after_pair=os.getloadavg())
            M['runs'].extend(rows);pending.extend(rows);journal.write(json.dumps(rows)+'\n');last=tr
            if pr['returncode']!=0 or tr['returncode']!=0:
                M['status']='failed';flush(pending,dict(failure=True));save();raise SystemExit(4)
        if pending:flush(pending,{k:pr[k] for k in ['policy','protocol','seed','block','step']})
        print(pr['block'],pr['seed'],pr['policy'],pr['protocol'],len(M['runs']),flush=True)
M.update(status='complete',ended_utc=utc(),seconds=time.monotonic()-start,binary_sha256_after=sha(B))
assert M['binary_sha256']==M['binary_sha256_after']
for n,h in F['files'].items():assert sha(S/n)==h
save()
