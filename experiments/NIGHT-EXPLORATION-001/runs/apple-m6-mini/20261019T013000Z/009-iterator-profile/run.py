#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import hashlib,json,subprocess,csv,io,os,time,re
ROOT=Path.cwd();OUT=Path(__file__).resolve().parent;REL=OUT.relative_to(ROOT);SCR=Path('scratch/m6-iterator-profile');SCR.mkdir(parents=True,exist_ok=True);(OUT/'validation').mkdir(exist_ok=True);(OUT/'profiles').mkdir(exist_ok=True)
CONTRACTS=[dict(id='integer-full-forward',encoding='integer',mask=7,direction='forward'),dict(id='integer-full-reverse',encoding='integer',mask=7,direction='reverse'),dict(id='integer-score-forward',encoding='integer',mask=4,direction='forward'),dict(id='fraction-full-forward',encoding='fraction',mask=7,direction='forward')]
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
def run(cmd,name,folder='validation',env=None):
 if folder=='profiles':assert not (SCR/(name+'.stdout')).exists(),('no profile retry',name)
 else:
  original=name;attempt=1
  while (SCR/(name+'.stdout')).exists():attempt+=1;name=original+'-attempt'+str(attempt).zfill(3)
 start=utc();t=time.monotonic();r=subprocess.run(list(map(str,cmd)),capture_output=True,text=True,timeout=120,env=env)
 raw={}
 for channel,data in [('stdout',r.stdout),('stderr',r.stderr)]:
  path=SCR/(name+'.'+channel);path.write_text(data);raw[channel]=dict(path='ignored scratch/m6-iterator-profile/'+path.name,sha256=sha(path))
  if folder=='validation':(OUT/folder/(name+'.'+channel)).write_text(data.replace(str(ROOT),'<workspace>'))
 record=dict(name=name,command=[str(a).replace(str(ROOT)+'/', '') for a in cmd],started_utc=start,finished_utc=utc(),wall_seconds=time.monotonic()-t,returncode=r.returncode,raw=raw)
 with (OUT/'commands.jsonl').open('a') as f:f.write(json.dumps(record)+'\n')
 assert r.returncode==0,(name,r.returncode)
 return r,record

def args(binary,n,ops,seed,c,warmup):return [binary,'--size',n,'--ops',ops,'--seed',seed,'--member-bytes',16,'--warmup-passes',warmup,'--direction',c['direction'],'--mask',c['mask'],'--encoding',c['encoding']]

def prepare():
 assert not (OUT/'freeze.json').exists()
 save(OUT/'LOCAL-PLAN.json',dict(status='preregistered before captures',created_utc=utc(),type='baseline-only local public iterator PC profile; no optimization selected',contracts=CONTRACTS,validation='native+ASan/UBSan: four contracts,size1000,requested_ops2003,seed1,warmup1;8runs total',captures=[dict(size=n,seed=s,contract=c['id'],requested_items=100000000,warmup_passes=3) for n in (100000,1000000) for c in CONTRACTS for s in (1,2)],minimum_pcs=25,requested_sample_interval_us=1000,no_retry=True,source_sha256='d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2',participant='/root/followup_proposal_b',backend='Inherited Codex/GPT-6 family; exact serving model/token usage/cost unknown',scope='Existing sampler hooks include QoS/CPU/thread-clock observations around traversal; fixture setup,warmup and semantic verification excluded. Sampled PC counts are not unbiased time shares or hardware costs.'))
 for label,san,profile in [('iterator-native',False,False),('iterator-san',True,False),('iterator-profile',False,True)]:
  flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1' if san else '-O3']
  if san:flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
  if profile:flags+=['-DPROFILE_SAMPLE']
  if not profile and (SCR/label).exists():continue
  run(['clang',*flags,'-Isrc','-Icompat','-Ivendor/redis',REL/'iterator.c',*([REL/'apple-sampler-bridge.c'] if profile else []),'src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',SCR/label],'build-'+label)
 checks=[]
 for label in ('iterator-native','iterator-san'):
  for c in CONTRACTS:
   r,record=run(args(SCR/label,1000,2003,1,c,1),label+'-'+c['id']);rows=list(csv.DictReader(io.StringIO(r.stdout)));assert len(rows)==1;row=rows[0];assert row['checksum']==row['expected_checksum'] and int(row['operations'])==3000
   checks.append(dict(build=label,contract=c['id'],status='PASS',checksum=row['checksum'],operations=3000,raw=record['raw']))
 save(OUT/'validation.json',dict(status='PASS',checks=checks,original_referees_unmodified=True))
 # Existing controls are read and pinned; never rerun them unchanged.
 prior=[]
 for i in (0,1):
  f=OUT/'../002-rank/profile'/f'sampler-calibration-{i}.stderr';lines=[s for s in f.read_text().splitlines() if s.startswith('PC,')];assert lines and all('sampler_probe' in s for s in lines);prior.append(dict(file='../002-rank/profile/'+f.name,sha256=sha(f),captured_pcs=len(lines),all_pcs_at_known_sampler_probe=True))
 run(['dsymutil',SCR/'iterator-profile','-o',SCR/'iterator-profile.dSYM'],'dsymutil')
 assembly,rec=run(['otool','-tvV',SCR/'iterator-profile'],'release-assembly');lines=assembly.stdout.splitlines();wanted=False;subset=[]
 for line in lines:
  if line.startswith('_') and line.endswith(':'):wanted=line=='_zbtreeIteratorNext:'
  if wanted:subset.append(line)
 assert subset;(OUT/'zbtreeIteratorNext.asm').write_text('\n'.join(subset)+'\n')
 # Public assembly omits process addresses; otool link-time addresses are retained.
 compiler=run(['clang','--version'],'compiler')[0].stdout
 files=['src/zset_btree.c','src/zset_btree.h','compat/standalone.c','compat/server.h','vendor/redis/siphash.c',str(REL/'iterator.c'),str(REL/'microbench.c'),str(REL/'apple-sampler-bridge.c'),str(REL/'../002-rank/night-rank-sampler.h'),str(REL/'LOCAL-PLAN.json'),str(REL/'run.py')]
 save(OUT/'freeze.json',dict(frozen_utc=utc(),status='frozen after correctness and before capture',files_sha256={p:sha(p) for p in files},binaries_sha256={name:sha(SCR/name) for name in ('iterator-native','iterator-san','iterator-profile')},compiler='\n'.join(s for s in compiler.splitlines() if not s.startswith('InstalledDir:')),sampler_prior_known_work_controls=prior,host='Launcher-verified Apple M6/arm64/macOS27; frequency/DVFS/core residency/PMU unknown'))
 print('PREPARE PASS:8semantic runs; exact refs; prior sampler controls reused; freeze written',flush=True)

def captures():
 freeze=json.loads((OUT/'freeze.json').read_text());assert not (OUT/'summary.json').exists()
 for f,h in freeze['files_sha256'].items():assert sha(f)==h,f
 assert sha(SCR/'iterator-profile')==freeze['binaries_sha256']['iterator-profile']
 results=[];env=os.environ.copy();env['PROFILE_USEC']='1000'
 save(OUT/'capture-status.json',dict(status='running',started_utc=utc(),completed=0,planned=16))
 for n in (100000,1000000):
  for c in CONTRACTS:
   for seed in (1,2):
    name=f'n{n}-{c["id"]}-s{seed}';r,record=run(args(SCR/'iterator-profile',n,100000000,seed,c,3),name,'profiles',env);row=list(csv.DictReader(io.StringIO(r.stdout)));assert len(row)==1;row=row[0];assert row['checksum']==row['expected_checksum'] and int(row['operations'])==100000000
    pcs=[s.split(',') for s in r.stderr.splitlines() if s.startswith('PC,')];header=next(s.split(',') for s in r.stderr.splitlines() if s.startswith('PROFILE,'));assert int(header[3])==len(pcs) and header[4]=='0'
    bins=Counter();symbols=Counter()
    for pc in pcs:
     module,address,base,symbol,start=pc[1:];offset=int(address,16)-int(start,16);bins[(module,symbol,offset)]+=1;symbols[symbol]+=1
    item=dict(size=n,seed=seed,contract=c['id'],direction=c['direction'],mask=c['mask'],encoding=c['encoding'],requested_items=100000000,operations=int(row['operations']),checksum=row['checksum'],expected_checksum=row['expected_checksum'],tree_bytes=int(row['tree_bytes']),samples=len(pcs),minimum_samples=25,sufficient=len(pcs)>=25,requested_interval_us=int(header[2]),symbols=dict(symbols),pc_bins=[dict(module=k[0],symbol=k[1],offset_bytes=k[2],count=v) for k,v in sorted(bins.items())],raw=record['raw'],started_utc=record['started_utc'],finished_utc=record['finished_utc'],scope='existing PROFILE_SAMPLE begin/end hooks only; setup/warmup/verification excluded; emitted elapsed values unused')
    save(OUT/'profiles'/(name+'.json'),item);results.append(item);save(OUT/'capture-status.json',dict(status='running',completed=len(results),planned=16,last_completed=name));print('captured',len(results),'/16',name,'PCs',len(pcs),'sufficient',item['sufficient'],flush=True)
 save(OUT/'summary.json',dict(status='COMPLETE',finished_utc=utc(),captures=results,sufficient=sum(x['sufficient'] for x in results),total_captures=16,counts_not_time_shares=True,emitted_elapsed_values_unused=True,no_optimization_selected=True))
 save(OUT/'capture-status.json',dict(status='complete',completed=16,planned=16,finished_utc=utc()))
 print('CAPTURES COMPLETE: no retries; all processes finished',flush=True)
if __name__=='__main__':
 import sys
 globals()[sys.argv[1]]()
