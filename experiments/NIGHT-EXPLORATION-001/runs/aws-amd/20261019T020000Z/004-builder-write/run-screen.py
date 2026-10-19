import subprocess,pathlib,time,datetime,json,csv,hashlib,statistics,os
out=pathlib.Path('scratch/amd-builder-screen');out.mkdir(parents=True,exist_ok=False)
counts={int(k):v for k,v in json.loads(pathlib.Path('scratch/amd-builder-aa/counts.json').read_text()).items()}
binaries={v:'scratch/amd-builder-build/'+v+'/build/native/btree-bench' for v in ['A','B','C']};binaries['base']='build/size-matrix/btree-bench'
freeze={v:hashlib.sha256(pathlib.Path(b).read_bytes()).hexdigest() for v,b in binaries.items()}
(out/'binary-hashes.json').write_text(json.dumps(freeze,indent=2)+'\n');records=[];rows=[];startphase=time.monotonic()
for block in range(6):
 variants=['A','B','C'];variants=variants[block%3:]+variants[:block%3]
 for variant in variants:
  for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
   for step,side in enumerate('ABBA'):
    if time.monotonic()-startphase>300:raise RuntimeError('screen phase budget')
    v='base' if side=='A' else variant;label=f'{variant}-b{block}-n{n}-s{step}-{side}'
    cmd=[binaries[v],'--case','update','--size',str(n),'--ops',str(counts[n]),'--member-bytes','16','--seed',str(1+block//2)]
    start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
    (out/(label+'.csv')).write_text(r.stdout);(out/(label+'.stderr')).write_text(r.stderr)
    records.append(dict(label=label,variant=variant,block=block,step=step,side=side,n=n,command=cmd,start=start,end=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode,loadavg=os.getloadavg()))
    (out/'processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode()
    row=list(csv.DictReader(r.stdout.splitlines()))[0];rows.append(dict(label=label,variant=variant,block=block,side=side,**row))
summary={}
for variant in ['A','B','C']:
 summary[variant]={}
 for n in counts:
  effects=[];blocks=[]
  for block in range(6):
   rr=[r for r in rows if r['variant']==variant and int(r['size'])==n and r['block']==block];assert len(rr)==4
   assert len(set(r['checksum'] for r in rr))==1
   a=statistics.mean(float(r['ns_per_op']) for r in rr if r['side']=='A');b=statistics.mean(float(r['ns_per_op']) for r in rr if r['side']=='B');effect=100*(b/a-1);effects.append(effect)
   mem=[int(r['tree_bytes']) for r in rr];assert len(set(mem))==1,(variant,n,block,'memory')
   blocks.append(dict(block=block,effect_pct=effect,tree_bytes=mem[0],minimum_ns=min(int(r['elapsed_ns']) for r in rr)))
  summary[variant][n]=dict(blocks=blocks,median_pct=statistics.median(effects),range_pct=[min(effects),max(effects)],primary_gate_all_blocks=all(x<=-2 for x in effects))
for v,b in binaries.items():assert hashlib.sha256(pathlib.Path(b).read_bytes()).hexdigest()==freeze[v]
(out/'rows.json').write_text(json.dumps(rows,indent=2)+'\n');(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
