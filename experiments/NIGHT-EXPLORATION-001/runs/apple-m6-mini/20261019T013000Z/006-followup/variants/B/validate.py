#!/usr/bin/env python3
import hashlib,json,shutil,subprocess,time,re
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path.cwd(); OUT=Path(__file__).resolve().parent; WT=ROOT/'worktrees/m6-caller-B'; REF=ROOT/'experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/004-lookup'
LOG=OUT/'logs'; LOG.mkdir(); RAW=WT/'scratch/caller-validation'; RAW.mkdir(parents=True)
(WT/'build').mkdir(exist_ok=True); (WT/'referee').mkdir()
for name in ('lookup-bench.c','physical-oracle.c'):shutil.copy2(REF/name,WT/'referee'/name)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
records=[]
report=dict(status='running',participant='/root/followup_proposal_b',backend='Codex/GPT-6 family; inherited exact serving model unknown',token_usage=None,monetary_cost=None,source_commit='e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf',worktree='worktrees/m6-caller-B',started_utc=utc(),commands=records,referees={n:sha(WT/'referee'/n) for n in ('lookup-bench.c','physical-oracle.c')})
def save():(OUT/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
def run(cmd,name):
 start=utc();t=time.monotonic();r=subprocess.run(list(map(str,cmd)),cwd=WT,capture_output=True,text=True,timeout=120)
 for channel,data in [('stdout',r.stdout),('stderr',r.stderr)]:
  (RAW/(name+'.'+channel)).write_text(data)
  public=data.replace(str(WT),'<variant-worktree>').replace(str(ROOT),'<workspace>')
  (LOG/(name+'.'+channel)).write_text(public)
 records.append(dict(name=name,command=list(map(str,cmd)),cwd='worktrees/m6-caller-B',started_utc=start,finished_utc=utc(),wall_seconds=time.monotonic()-t,returncode=r.returncode,stdout_sha256=sha(LOG/(name+'.stdout')),stderr_sha256=sha(LOG/(name+'.stderr'))));save()
 assert r.returncode==0,(name,r.returncode)
 return r.stdout
try:
 for san in (False,True):
  suf='-san' if san else '';flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1' if san else '-O3']
  if san:flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
  for label,source,extra,included in [('upstream','tests/upstream.c',['-DREDIS_TEST','-DREDIS_DEBUG'],False),('lookup','referee/lookup-bench.c',[],False),('physical','referee/physical-oracle.c',[],True)]:
   name=label+suf;cmd=['clang',*flags,'-Isrc','-Icompat','-Ivendor/redis','-I.',*extra,source,*([] if included else ['src/zset_btree.c']),'compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+name]
   run(cmd,'build-'+name)
   if label in ('upstream','physical'):
    output=run(['build/'+name],name)
    if label=='physical':assert 'cells=4160' in output and 'checks=515840' in output
   else:
    for n in (100,1000,10000,100000,1000000):
     for case in ('lookup-hit','lookup-miss'):run(['build/'+name,'--case',case,'--size',str(n),'--ops','2003','--seed','1','--member-bytes','16'],name+'-n'+str(n)+'-'+case)
    for m in (8,319,320,321,1024):
     for case in ('lookup-hit','lookup-miss'):run(['build/'+name,'--case',case,'--size','1000','--ops','2003','--seed','1','--member-bytes',str(m)],name+'-m'+str(m)+'-'+case)
  print('B native/sanitizer validation completed:',suf or 'native',flush=True)
 asm=run(['otool','-tvV','build/lookup'],'lookup-assembly')
 lines=asm.splitlines(); sections={};cur=None
 for line in lines:
  if line.startswith('_') and line.endswith(':'):cur=line[:-1];sections[cur]=[]
  if cur is not None:sections[cur].append(line)
 for name in ('_zbtreeScoreRaw','_zbtreeScore','_zbtScoreLeafFindMember'):
  (OUT/(name.lstrip('_')+'.asm')).write_text('\n'.join(sections.get(name,[]))+'\n')
 report.update(status='PASS',finished_utc=utc(),source_sha256=sha(WT/'src/zset_btree.c'),patch_sha256=sha(OUT/'candidate.patch'),binaries={p.name:sha(p) for p in (WT/'build').iterdir() if p.is_file()},summary='43 original upstream tests per native/sanitizer build; 20 public size/length correctness smoke cells per build; 4160-cell/515840-check physical oracle per build. No comparative benchmark, profile, or performance inference.')
except Exception as e:
 report.update(status='FAIL',finished_utc=utc(),error=repr(e));raise
finally:save()
