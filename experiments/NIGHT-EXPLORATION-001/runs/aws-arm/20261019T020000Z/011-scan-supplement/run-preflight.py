from pathlib import Path
import subprocess,json,time,datetime,hashlib
p=Path(__file__).resolve().parent;o=Path('scratch/scan-supplement-preflight/output');o.mkdir(exist_ok=False);rows=[];start=time.monotonic();budget=300
for mode in ['native','sanitize']:
 for history in ['ascending','trim','resize']:
  for width in [8,319,320,321,1024]:
   for encoding in [0,1,2]:
    n=4096 if history=='resize' else 7 if width==319 else 31;maximum=32768 if history=='resize' else n;label=f'{mode}-{history}-b{width}-e{encoding}';cmd=[f'scratch/scan-supplement-preflight/{mode}',history,str(n),str(width),'201',str(encoding),str(maximum)];remaining=budget-(time.monotonic()-start);assert remaining>0
    t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(30,remaining));end=datetime.datetime.now(datetime.timezone.utc).isoformat();(o/(label+'.stdout')).write_text(r.stdout);(o/(label+'.stderr')).write_text(r.stderr);row=dict(label=label,command=cmd,start_utc=t,end_utc=end,returncode=r.returncode);rows.append(row);(o/'commands.json').write_text(json.dumps(rows,indent=2)+'\n')
    if r.returncode!=0:raise RuntimeError((label,'fixture intent unsupported or correctness failed',r.returncode,r.stderr,r.stdout))
    row['result']=json.loads(r.stdout);(o/'commands.json').write_text(json.dumps(rows,indent=2)+'\n')
(o/'RESULT.json').write_text(json.dumps({'status':'pass','children':len(rows),'seconds':time.monotonic()-start,'baseline_timing_windows':0,'candidate_timings':0,'source_sha256':hashlib.sha256(Path('src/zset_btree.c').read_bytes()).hexdigest(),'diagnostic_sha256':hashlib.sha256((p/'preflight.c').read_bytes()).hexdigest()},indent=2)+'\n')
