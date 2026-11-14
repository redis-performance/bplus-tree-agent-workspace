#!/usr/bin/env python3
"""Fleet-only supplemental guard build, independent qualification, and comparison."""
import argparse, hashlib, json, os, pathlib, statistics, subprocess, time
p=argparse.ArgumentParser()
p.add_argument('--root',required=True);p.add_argument('--phase',required=True)
p.add_argument('--cohort',choices=['native','gcc15-lto'],required=True)
p.add_argument('--seed',type=int,default=17);p.add_argument('--variants',default='BC')
p.add_argument('--action',choices=['build','qualify','compare'],required=True)
a=p.parse_args();root=pathlib.Path(a.root);os.chdir(root)
exp=pathlib.Path('experiments/ARM-LOOKUP-CONT-001');out=root/a.phase
cases={'iterator-forward':1000000,'iterator-reverse':1000000,'rank-forward':200000,'rank-reverse':200000,'churn':20000}
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def leasecheck():
 d=json.loads((root/'reservation.json').read_text())
 assert d['owner']=='bplus ARM-LOOKUP-CONT-001' and d['state']=='RESERVED' and time.time()<d['deadline']-300
 assert subprocess.run(['systemctl','is-active','--quiet',root.name+'-release.timer']).returncode==0
 s=(pathlib.Path('/proc')/str(d['coordinator_pid'])/'stat').read_text().split(') ')[1].split()
 assert s[0]=='T' and s[19]==d['coordinator_ticks']
 assert os.sched_getaffinity(0)=={0}
 if 'sibling50_online' in d:
  assert pathlib.Path('/sys/devices/system/cpu/cpu50/online').read_text().strip()=='0'
  assert subprocess.run(['systemctl','is-active','--quiet','snap.parca-agent.parca-agent-svc.service']).returncode!=0
leasecheck()
def run(cmd,stem):
 started=time.time();q=subprocess.run(cmd,capture_output=True,text=True,timeout=240)
 (out/(stem+'.stdout')).write_text(q.stdout);(out/(stem+'.stderr')).write_text(q.stderr)
 with (out/'commands.jsonl').open('a') as f:f.write(json.dumps(dict(argv=cmd,stem=stem,returncode=q.returncode,started=started,finished=time.time()))+'\n')
 assert q.returncode==0,(stem,q.stderr[-1000:]);return q.stdout
if a.action=='build':
 out.mkdir();prior=json.loads((root/'baseline/metadata.json').read_text())
 meta=dict(cohort=a.cohort,seed=a.seed,cases=cases,harness_sha256=sha(exp/'guards/guards.c'),build_script_sha256=sha(exp/'guards/build.sh'),compiler_image=prior['gcc15_image'] if a.cohort=='gcc15-lto' else None,binaries={},started=time.time())
 for v in ['base',*a.variants]:
  source=exp/'current/src/zset_btree.c' if v=='base' else pathlib.Path('variants/H2-native')/v/'zset_btree.c'
  binary=pathlib.Path('bin')/(a.phase+'-'+v)
  cmd=['sh',str(exp/'guards/build.sh'),str(source),str(binary),'lto' if a.cohort=='gcc15-lto' else 'native']
  if a.cohort=='gcc15-lto':cmd=['docker','run','--rm','--cpuset-cpus','0-3','--network','none','-v',str(root)+':/work','-w','/work',prior['gcc15_image']]+cmd
  run(cmd,'build-'+v)
  meta['binaries'][v]=dict(path=str(binary),source_sha256=sha(source),binary_sha256=sha(binary))
  run(['objdump','-d',str(binary)],'assembly-'+v);run(['size',str(binary)],'size-'+v)
  for case in cases:run(['taskset','-c','2',str(root/binary),'verify',case,str(a.seed),'2'],'verify-'+v+'-'+case)
 (out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
 raise SystemExit(0)
meta=json.loads((out/'metadata.json').read_text())
assert meta['cohort']==a.cohort and meta['seed']==a.seed and meta['cases']==cases
assert sha(exp/'guards/guards.c')==meta['harness_sha256']
for v,b in meta['binaries'].items():assert sha(root/b['path'])==b['binary_sha256']
assert not subprocess.check_output(['docker','ps','-q'],text=True).strip()
run(['taskset','-c','2','python3','-c','import os;assert os.sched_getaffinity(0)=={2}'],'affinity-'+a.action)
if a.action=='compare':
 gate=json.loads((out/'qualification.json').read_text());assert gate['pass'] and len(gate['blocks'])==15
requested_variants=list(a.variants)
exclusions={}
exclusion_file=root/'H2-exclusions.json'
if a.action=='compare' and exclusion_file.exists():
 exclusions=json.loads(exclusion_file.read_text())
 for v,item in exclusions.items():
  if v in meta['binaries']:assert item['source_sha256']==meta['binaries'][v]['source_sha256']
variants=['base'] if a.action=='qualify' else [v for v in requested_variants if v not in exclusions]
assert variants
if a.action=='compare':
 meta.update(requested_variants=requested_variants,measured_variants=variants,excluded_variants=exclusions,comparison_collector_sha256=sha(__file__),comparison_started=time.time())
 (out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
rowfile=out/('aa.jsonl' if a.action=='qualify' else 'comparison.jsonl');assert not rowfile.exists()
blocks=[];allrows=[]
for v in variants:
 assert v in meta['binaries']
 for case,sweeps in cases.items():
  rows=[]
  for block in range(3):
   rr=[]
   for slot,label in enumerate('ABBA'):
    leasecheck();which='base' if label=='A' else v;b=meta['binaries'][which]
    stem=f'{a.action}-{v}-{case}-{block}-{slot}'
    q=run(['taskset','-c','2',str(root/b['path']),'measure',case,str(a.seed),str(sweeps)],stem)
    row=json.loads(q);assert row['verified'] and row['case']==case and row['seed']==a.seed and row['sweeps']==sweeps
    row.update(cohort=a.cohort,variant=v,block=block,slot=slot,label=label,binary_sha256=b['binary_sha256'])
    with rowfile.open('a') as f:f.write(json.dumps(row)+'\n')
    rr.append(row);rows.append(row);allrows.append(row);print(stem,flush=True)
   for k in ['ops','mutation_api_calls','items','rank_sum','score_sum','weighted_sum']:assert len({x[k] for x in rr})==1
   aa=[x for x in rr if x['label']=='A'];bb=[x for x in rr if x['label']=='B']
   delta=(statistics.mean(x['elapsed_ns'] for x in bb)/statistics.mean(x['elapsed_ns'] for x in aa)-1)*100
   memory={k:(statistics.mean(x[k] for x in bb)/statistics.mean(x[k] for x in aa)-1)*100 for k in ['owned_bytes_before','owned_bytes_after']}
   ok=(abs(delta)<=1 if a.action=='qualify' else delta<=1) and all(m<=1 for m in memory.values()) and min(x['elapsed_ns'] for x in rr)>=250000000
   blocks.append(dict(variant=v,case=case,block=block,delta_pct=delta,memory_delta_pct=memory,min_window_ns=min(x['elapsed_ns'] for x in rr),passed=ok))
  for binary in {r['binary_sha256'] for r in rows}:
   subset=[r for r in rows if r['binary_sha256']==binary]
   for k in ['owned_bytes_before','owned_bytes_after']:assert len({r[k] for r in subset})==1,(case,binary,k)
result=dict(rows=len(allrows),blocks=blocks,finished=time.time())
result['pass']=all(b['passed'] for b in blocks)
(out/('qualification.json' if a.action=='qualify' else 'comparison-analysis.json')).write_text(json.dumps(result,indent=2)+'\n')
print('COMPLETE',a.action,result['pass'],flush=True)
