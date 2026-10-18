from pathlib import Path
import ast,csv,datetime,difflib,hashlib,itertools,json,math,os,re,shutil,statistics,subprocess,sys,time
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-diag-019';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
F6=json.loads((R/'experiments/EXP-006/freeze.json').read_text());variants=['control-on','C-on','control-off','C-off'];mode=sys.argv[1]
flags=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG'];support=['compat/standalone.c','vendor/redis/siphash.c','-lm']
def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def save():dump(manifest,M)
def run(tag,args,cwd,extra=None):
 assert datetime.datetime.now(datetime.timezone.utc)<datetime.datetime(2026,10,18,6,2,tzinfo=datetime.timezone.utc)
 out=D/(tag+'.stdout');err=D/(tag+'.stderr');r=dict(name=tag,command=args,cwd=str(cwd.relative_to(R)),started_utc=utc(),**(extra or {}))
 with out.open('w') as o,err.open('w') as e:
  try:rc=subprocess.run(args,cwd=cwd,stdout=o,stderr=e,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 r.update(returncode=rc,ended_utc=utc(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=sha(out),stderr_sha256=sha(err));M['runs'].append(r);save()
 if rc!=0:M['status']='failed';save();raise SystemExit((tag,rc))
 return out.read_text(),r
if mode=='prepare':
 S.mkdir();D=P/'validation';D.mkdir();manifest=P/'validation.json';M=dict(status='running',runs=[],binaries={},codegen=[]);save();files={}
 for v in variants:
  source,placement=v.split('-');B=S/v;B.mkdir()
  for n,h in F6['files'][source].items():
   p=R/F6['snapshot_root']/source/n;assert sha(p)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)
  shutil.copy2(R/'tests/batch_score_oracle.c',B/'tests/batch_score_oracle.c')
  p=B/'src/zset_btree.c';old=p.read_text()
  if placement=='off':
   a=old.index('        if (zs->member_index.size)',old.index('unsigned int zbtreeScores('));b=old.index('\n    }',a);p.write_text(old[:a]+old[b:])
  (P/(v+'.patch')).write_text(''.join(difflib.unified_diff(old.splitlines(True),p.read_text().splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
  files[v]={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()};(B/'build').mkdir()
 dump(P/'freeze.json',dict(base_commit=F6['base_commit'],snapshot=str(S.relative_to(R)),parent_freeze_sha256=sha(R/'experiments/EXP-006/freeze.json'),provenance='uncommitted diagnostic snapshots',frozen_utc=utc(),files=files,plan_sha256=sha(P/'PLAN.md'),runner_sha256=sha(Path(__file__))))
 for v in variants:
  B=S/v
  for build in ['release','sanitize']:
   opts=['-O3'] if build=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
   for name,src,extra,included in [('original','tests/upstream.c',['-DREDIS_TEST'],False),('oracle','tests/batch_score_oracle.c',[],True),('batch','bench/batch_lookup.c',[],False)]:
    binary='build/'+build+'-'+name;run(v+'-'+build+'-'+name+'-build',flags+opts+extra+[src]+([] if included else ['src/zset_btree.c'])+support+['-o',binary],B);M['binaries'][v+'-'+build+'-'+name]=sha(B/binary);save()
    if name!='batch':
     out,_=run(v+'-'+build+'-'+name,[binary],B);assert ('43 passed, 0 failed' in out) if name=='original' else 'PASS seeds=2' in out
   for i,(n,bytes_,batch,layout) in enumerate(itertools.product([17,257],[16,320],[1,3,16],['hit','miss','mixed'])):
    out,_=run(f'{v}-{build}-fixture{i}',['build/'+build+'-batch','--size',str(n),'--ops',str(n+3),'--member-bytes',str(bytes_),'--batch-size',str(batch),'--layout',layout,'--seed','81903','--query-seed','81919','--warmup-passes','2'],B);row=next(csv.DictReader(out.splitlines()));assert int(row['operations'])==n+3 and int(row['api_calls'])==(n+3+batch-1)//batch
   print(v,build,'43tests/batch-oracle/36fixtures PASS',flush=True)
  run(v+'-assembly',flags+['-O3','-S','src/zset_btree.c','-o','build/source.s'],B)
  s=(B/'build/source.s').read_text();a=s.index('_zbtreeScores:');b=s.index('.cfi_endproc',a);body=s[a:b];(P/(v+'-scores.s.txt')).write_text(body+'\n');prfm=len(re.findall(r'\bprfm\b',body));assert (prfm>0)==v.endswith('-on');M['codegen'].append(dict(variant=v,prefetch_instructions=prfm,assembly_sha256=sha(B/'build/source.s')));save()
 for v in variants:
  for n,h in files[v].items():assert sha(S/v/n)==h
 M['status']='complete';save()
elif mode in ['aa','discovery','confirm']:
 F=json.loads((P/'freeze.json').read_text());V=json.loads((P/'validation.json').read_text());assert V['status']=='complete';assert sha(P/'PLAN.md')==F['plan_sha256'];assert sha(Path(__file__))==F['runner_sha256']
 for v in variants:
  for n,h in F['files'][v].items():assert sha(S/v/n)==h
  assert sha(S/v/'build/release-batch')==V['binaries'][v+'-release-batch']
 phase=P/mode;phase.mkdir();D=phase/'raw';D.mkdir();manifest=phase/'manifest.json';seeds={'aa':[(81903,81919),(81911,81923)],'discovery':[(82003,82019),(82011,82023)],'confirm':[(82103,82119),(82111,82123)]}[mode];cells=[(p,b) for p in ['on','off'] for b in [1,16]]
 if mode=='confirm':cells=cells[::-1]
 M=dict(status='running',phase=mode,runs=[],seeds=seeds,cells=cells,blocks=6,plan_sha256=sha(P/'PLAN.md'),freeze_sha256=sha(P/'freeze.json'),runner_sha256=sha(Path(__file__)),binaries={v:V['binaries'][v+'-release-batch'] for v in variants});save();start=time.monotonic()
 for block in range(1,7):
  offset=(block-1)%4
  for seed,qseed in (seeds if block%2 else seeds[::-1]):
   for placement,batch in cells[offset:]+cells[:offset]:
    for step,label in enumerate('ABBA',1):
     if time.monotonic()-start>600:M['status']='budget-exhausted';save();raise SystemExit(3)
     source=('control' if mode=='aa' or label=='A' else 'C')+'-'+placement;cmd=[str((S/source/'build/release-batch').relative_to(R)),'--size','8192','--ops','2000000','--member-bytes','16','--batch-size',str(batch),'--layout','hit','--seed',str(seed),'--query-seed',str(qseed),'--warmup-passes','3']
     run(f'{placement}-b{batch}-s{seed}-k{block}-{step}{label}',cmd,R,dict(source=source,placement=placement,batch=batch,seed=seed,query_seed=qseed,block=block,step=step,label=label))
  print(mode,block,len(M['runs']),flush=True)
 for v in variants:
  for n,h in F['files'][v].items():assert sha(S/v/n)==h
 M['status']='complete';save()
else:raise SystemExit('prepare|aa|discovery|confirm')
