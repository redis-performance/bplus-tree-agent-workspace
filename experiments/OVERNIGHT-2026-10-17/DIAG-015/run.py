from pathlib import Path
import datetime,hashlib,json,os,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[2]
F=json.loads((P.parent/'HARNESS-006/freeze.json').read_text());S=R/F['snapshot'];B=S/'build/release/iterator-modes'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
assert json.loads((P.parent/'BOUNDARY-015/summary.json').read_text())['status']=='pass'
assert all(r['detected'] for r in json.loads((P.parent/'BOUNDARY-015/faults/manifest.json').read_text()))
assert not (P/'manifest.json').exists();(P/'raw').mkdir()
for n,h in F['files'].items():assert sha(S/n)==h
assert sha(B)==json.loads((P.parent/'HARNESS-006/binaries.json').read_text())['release']
CELLS=[dict(name='int-trim-f0',encoding='integer',mask=0),dict(name='zero-trim-f6',encoding='alternating-zero',mask=6)]
M=dict(status='running',started_utc=utc(),base_commit=F['base_commit'],plan_sha256=sha(P/'PLAN.md'),runner_sha256=sha(Path(__file__)),freeze_sha256=sha(P.parent/'HARNESS-006/freeze.json'),binary=str(B.relative_to(R)),binary_sha256=sha(B),cells=CELLS,seeds=[45121,45131],blocks=6,protocols=['gap0','gap100','placebo100'],runs=[],warmup=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def command(c,seed,ops=20000000):
    return [str(B.relative_to(R)),'--size','95','--ops',str(ops),'--seed',str(seed),'--warmup-passes','3','--direction','forward','--encoding',c['encoding'],'--construction','trimmed','--member-bytes','16','--mask',str(c['mask'])]
def launch(cmd,out,err):
    t=time.monotonic_ns();started=utc()
    try:rc=subprocess.run(cmd,cwd=R,stdout=out,stderr=err,timeout=120).returncode
    except subprocess.TimeoutExpired:rc='timeout'
    end=time.monotonic_ns()
    return dict(command=cmd,started_utc=started,ended_utc=utc(),start_monotonic_ns=t,end_monotonic_ns=end,returncode=rc)
def complete(row,csv,err):
    row.update(csv=str(csv.relative_to(P)),stderr=str(err.relative_to(P)),csv_sha256=sha(csv),stderr_sha256=sha(err))
    return row
save();out=P/'raw/warmup.csv';err=P/'raw/warmup.stderr'
with out.open('w') as so,err.open('w') as se:r=launch(command(CELLS[1],45121,1000000),so,se)
M['warmup'].append(complete(r,out,err));save();ok=r['returncode']==0;start=time.monotonic()
target=CELLS[1]
for block in range(1,7):
    if not ok:break
    offset=(block-1)%3
    protocols=M['protocols'][offset:]+M['protocols'][:offset]
    seeds=M['seeds'] if block%2 else M['seeds'][::-1]
    for seed in seeds:
        if not ok:break
        for protocol in protocols:
            for step,label in enumerate('ABBA',1):
                if time.monotonic()-start>400:ok=False;M['status']='budget-exhausted';break
                predecessor=CELLS[0] if protocol!='placebo100' and label=='B' else target
                gap_ms=0 if protocol=='gap0' else 100
                stem=f'{protocol}-s{seed}-b{block}-p{step}-{label}'
                pcsv=P/'raw'/(stem+'-predecessor.csv');perr=P/'raw'/(stem+'-predecessor.stderr')
                tcsv=P/'raw'/(stem+'-target.csv');terr=P/'raw'/(stem+'-target.stderr')
                pcmd=command(predecessor,seed);tcmd=command(target,seed);load=os.getloadavg()
                with pcsv.open('w') as po,perr.open('w') as pe,tcsv.open('w') as to,terr.open('w') as te:
                    pr=launch(pcmd,po,pe)
                    if pr['returncode']==0 and gap_ms:time.sleep(gap_ms/1000)
                    tr=launch(tcmd,to,te) if pr['returncode']==0 else None
                meta=dict(target=target['name'],seed=seed,block=block,step=step,label=label,protocol=protocol,requested_gap_ms=gap_ms,load_before_pair=load,load_after_pair=os.getloadavg())
                pr.update(meta,role='predecessor',cell=predecessor['name']);M['runs'].append(complete(pr,pcsv,perr))
                if tr is not None:
                    tr.update(meta,role='target',cell=target['name'],coordinator_launch_gap_ns=tr['start_monotonic_ns']-pr['end_monotonic_ns']);M['runs'].append(complete(tr,tcsv,terr))
                ok=pr['returncode']==0 and tr is not None and tr['returncode']==0
                if not ok:M['status']='failed'
                save()
                if not ok:break
            if not ok:break
        print(block,seed,len(M['runs']),ok,flush=True)
M.update(ended_utc=utc(),seconds=time.monotonic()-start,binary_sha256_after=sha(B))
if ok:M['status']='complete'
assert M['binary_sha256']==M['binary_sha256_after']
for n,h in F['files'].items():assert sha(S/n)==h
save()
