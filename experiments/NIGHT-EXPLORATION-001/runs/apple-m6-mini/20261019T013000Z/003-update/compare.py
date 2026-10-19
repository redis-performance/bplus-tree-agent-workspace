#!/usr/bin/env python3
import csv,hashlib,io,json,shutil,statistics,subprocess,sys,time
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path.cwd();OUT=Path(__file__).resolve().parent;REL=OUT.relative_to(ROOT);BASE=Path('scratch/m6-update/variants')
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
def run(cmd,name,variant,folder='candidate-validation',expect=0,timeout=120):
 p=OUT/folder;p.mkdir(exist_ok=True)
 log=OUT/'candidate-commands.jsonl'
 prior=[json.loads(l) for l in log.read_text().splitlines()] if log.exists() else []
 if any(x['name']==name and x['variant']==variant and x['folder']==folder and x['returncode']==0 for x in prior):
  return subprocess.CompletedProcess(list(map(str,cmd)),0,(p/(name+'.stdout')).read_text(),(p/(name+'.stderr')).read_text())
 start=utc();t=time.monotonic();cwd=BASE/variant
 r=subprocess.run(list(map(str,cmd)),cwd=cwd,capture_output=True,text=True,timeout=timeout)
 (p/(name+'.stdout')).write_text(r.stdout);(p/(name+'.stderr')).write_text(r.stderr)
 with (OUT/'candidate-commands.jsonl').open('a') as f:f.write(json.dumps(dict(name=name,variant=variant,command=list(map(str,cmd)),cwd=str(cwd),started_utc=start,finished_utc=utc(),wall_seconds=time.monotonic()-t,returncode=r.returncode,folder=folder))+'\n')
 if expect is not None:assert r.returncode==expect,(name,r.returncode,r.stderr[:500])
 return r
def build(variant,name,bench=None,san=False,extra=(),included=False):
 flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1' if san else '-O3']
 if san:flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
 return run(['clang',*flags,'-Isrc','-Icompat','-Ivendor/redis','-I.',*extra,bench or REL/'update-path-bench.c',*([] if included else ['src/zset_btree.c']),'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',Path('build')/name],'build-'+variant+'-'+name,variant)
def args(binary='update',n=100000,ops=2003,seed=1,case='preserve',member=16):return [Path('build')/binary,'--case',case,'--size',n,'--ops',ops,'--seed',seed,'--member-bytes',member]
def validate():
 for v in ('0','A','B','C'):
  (BASE/v/'build').mkdir(exist_ok=True);shutil.copy2(OUT/'repack-oracle.c',BASE/v/REL/'repack-oracle.c')
  for san in (False,True):
   suffix='-san' if san else '';binary='update'+suffix;build(v,binary,san=san)
   test='upstream'+suffix;build(v,test,bench='tests/upstream.c',san=san,extra=['-DREDIS_TEST','-DREDIS_DEBUG']);run([Path('build')/test],v+'-'+test,v)
   for n in (100,1000,10000,100000,1000000):
    for case in ('same','preserve','nearby','distant','plus-n'):run(args(binary,n=n,case=case),f'{v}-{binary}-n{n}-{case}',v)
   for m in (8,319,320,321,1024):
    for case in ('same','preserve','nearby','distant','plus-n'):run(args(binary,n=1000,member=m,case=case),f'{v}-{binary}-m{m}-{case}',v)
   semantic='semantic'+suffix;build(v,semantic,bench=REL/'semantic-check.c',san=san);run([Path('build')/semantic],v+'-'+semantic,v)
   oracle='repack-v2'+suffix;build(v,oracle,bench=REL/'repack-oracle.c',san=san,extra=['-DCANDIDATE'] if v!='0' else [],included=True);run([Path('build')/oracle],v+'-'+oracle,v)
  print('validated',v,flush=True)
 # Prove the isolated control's actual instruction text matches the calibrated binary.
 for label,binary in [('original',Path('scratch/m6-update/build/update')),('isolated',BASE/'0/build/update')]:
  r=subprocess.run(['otool','-tvV',str(binary)],capture_output=True,text=True,check=True);lines=r.stdout.splitlines()[2:];(OUT/'candidate-validation'/(label+'-text.sha256')).write_text(hashlib.sha256(('\n'.join(lines)).encode()).hexdigest()+'\n');(Path('scratch/m6-update')/(label+'-text.asm')).write_text('\n'.join(lines)+'\n')
 original=(OUT/'candidate-validation/original-text.sha256').read_text();isolated=(OUT/'candidate-validation/isolated-text.sha256').read_text();assert original==isolated,'baseline instruction text changed; new controls required'
 save(OUT/'candidate-validation.json',dict(status='complete',finished_utc=utc(),original_control_text_equals_isolated=True,variants={v:{'source':sha(BASE/v/'src/zset_btree.c'),'binary':sha(BASE/v/'build/update')} for v in ('0','A','B','C')},tests='43 upstream tests/build; 100 pattern-size-length checks +2 finite semantic +2 private repack oracles/source; native and ASan/UBSan'))
def discover():
 assert not (OUT/'discovery.json').exists();validation=json.loads((OUT/'candidate-validation.json').read_text());cal=json.loads((OUT/'calibration.json').read_text());d=dict(status='running',started_utc=utc(),scope='exploratory primary-only; failed A/A, cannot adopt',publication=json.loads(Path('scratch/night-apple-m6-mini-20261019T013000Z/publish-ack.json').read_text()),runs=[],results=[]);total=0
 try:
  for block,seed in enumerate((1,2,3,1,2,3)):
   order=('A','B','C');order=order[block%3:]+order[:block%3]
   for v in order:
    for n in ((100000,1000000) if block%2==0 else (1000000,100000)):
     for step,label in enumerate('ABBA'):
      current='0' if label=='A' else v;assert sha(BASE/current/'build/update')==validation['variants'][current]['binary'];ops=cal['fixed_ops'][f'{n}-preserve'];assert total<300
      name=f'b{block}-{v}-n{n}-{step}-{label}';r=run(args(n=n,ops=ops,seed=seed),name,current,'discovery');x=list(csv.DictReader(io.StringIO(r.stdout)));assert len(x)==1;x=x[0];assert int(x['ops'])==ops
      row=dict(block=block,seed=seed,variant=v,binary=current,size=n,step=step,label=label,ops=ops,elapsed_ns=int(x['elapsed_ns']),ns_op=int(x['elapsed_ns'])/ops,checksum=x['checksum'],tree_bytes=int(x['tree_bytes']),file='discovery/'+name+'.stdout',sha256=sha(OUT/'discovery'/(name+'.stdout')));d['runs'].append(row);total+=row['elapsed_ns']/1e9;save(OUT/'discovery.json',d)
   print('discovery block',block+1,flush=True)
  for v in ('A','B','C'):
   for n in (100000,1000000):
    effects=[];memory=[]
    for block in range(6):
     rs=[r for r in d['runs'] if r['variant']==v and r['size']==n and r['block']==block];assert len(rs)==4 and len({r['checksum'] for r in rs})==1
     a=statistics.mean(r['ns_op'] for r in rs if r['label']=='A');b=statistics.mean(r['ns_op'] for r in rs if r['label']=='B');effects.append(100*(b/a-1));a=statistics.mean(r['tree_bytes'] for r in rs if r['label']=='A');b=statistics.mean(r['tree_bytes'] for r in rs if r['label']=='B');memory.append(100*(b/a-1))
    d['results'].append(dict(variant=v,size=n,effects_pct=effects,median_pct=statistics.median(effects),memory_effects_pct=memory,passes_exploratory_primary=all(e<=-2 for e in effects)))
  d['status']='complete'
 finally:d['finished_utc']=utc();d['timing_seconds']=total;save(OUT/'discovery.json',d)
 print(json.dumps(d['results'],indent=2),flush=True)
if __name__=='__main__':globals()[sys.argv[1]]()
