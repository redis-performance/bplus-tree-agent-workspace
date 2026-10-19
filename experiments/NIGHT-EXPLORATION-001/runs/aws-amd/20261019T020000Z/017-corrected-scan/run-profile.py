#!/usr/bin/env python3
"""Corrected-adapter baseline-only scope controls and six fixed PMU captures."""
import argparse,csv,datetime,hashlib,io,json,os,pathlib,subprocess,tarfile,time
p=argparse.ArgumentParser();p.add_argument('--checkout',required=True,type=pathlib.Path);p.add_argument('--perf',required=True);a=p.parse_args();here=pathlib.Path(__file__).resolve().parent;source=here/'source';out=here/'profile';source.mkdir();out.mkdir();records=[];start=time.monotonic();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();expected=json.loads((here/'expected.json').read_text());assert sorted(os.sched_getaffinity(0))==[2]
def save(): (out/'processes.json').write_text(json.dumps(records,indent=2)+'\n')
def run(cmd,name,env=None,cwd=source):
 left=600-(time.monotonic()-start);assert left>0,'fixed profile cap reached';record={'name':name,'command':[str(x).replace(str(a.checkout),'<checkout>').replace(a.perf,'<perf>') for x in cmd],'started_utc':now()};records.append(record);save();r=subprocess.run(cmd,cwd=cwd,env=env,capture_output=True,text=True,timeout=min(120,left));record.update(finished_utc=now(),returncode=r.returncode);(out/(name+'.stdout')).write_text(r.stdout);(out/(name+'.stderr')).write_text(r.stderr);save();r.check_returncode();return r.stdout
blob=subprocess.check_output(['git','archive',expected['commit'],'src','compat','vendor/redis','tests','bench','Makefile'],cwd=a.checkout)
with tarfile.open(fileobj=io.BytesIO(blob)) as t:t.extractall(source)
(source/'bench/profile-scoped-fifo2.c').write_bytes((here/'profile-scoped-fifo2.c').read_bytes());(source/'build').mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
sourcehash={f:sha(source/f) for f in expected['source_hashes']};assert sourcehash==expected['source_hashes'];assert sha(here/'profile-scoped-fifo2.c')==expected['scope_sha256']
flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-Isrc','-Icompat','-Ivendor/redis'];compiler=subprocess.check_output(['clang','--version'],text=True)
for name,driver,san in [('original','bench/microbench.c',False),('profile','bench/profile-scoped-fifo2.c',False),('original-san','bench/microbench.c',True),('profile-san','bench/profile-scoped-fifo2.c',True)]:
 opt=['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'] if san else ['-O3'];run(['clang',*flags,*opt,driver,'src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+name],name+'-build')
binaryhash={n:sha(source/'build'/n) for n in ['original','profile','original-san','profile-san']};(out/'build-freeze.json').write_text(json.dumps({'commit':expected['commit'],'source_hashes':sourcehash,'scope_sha256':expected['scope_sha256'],'binary_sha256':binaryhash,'compiler':compiler,'cpu_affinity':[2]},indent=2)+'\n')
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes'];controls={}
def args(n,ops,seed):return ['--case','scan','--size',str(n),'--ops',str(ops),'--member-bytes','16','--seed',str(seed)]
def row(text):
 rr=list(csv.DictReader(text.splitlines()));assert len(rr)==1 and rr[0]['cpu_start']==rr[0]['cpu_end']=='2';return rr[0]
def equal(rows):
 for k in fields:assert len({r[k] for r in rows})==1,(k,rows)
disabled=os.environ.copy();disabled['PROFILE_DISABLE']='1'
for seed in [1,2,3]:
 for n in [100000,1000000]:
  label=f'n{n}-s{seed}';r=row(run(['build/original',*args(n,5000000,seed)],label+'-original'));s=row(run(['build/profile',*args(n,5000000,seed)],label+'-disabled',env=disabled));equal([r,s]);controls[label]=r
r=row(run(['build/original-san',*args(1000,2001,101)],'san-original'));s=row(run(['build/profile-san',*args(1000,2001,101)],'san-disabled',env=disabled));equal([r,s])
ctl=here/'control.fifo';ack=here/'ack.fifo';os.mkfifo(ctl);os.mkfifo(ack);env=os.environ.copy();env['BPLUS_PERF_CTL']=str(ctl);env['BPLUS_PERF_ACK']=str(ack);disabledperf=dict(env,PROFILE_DISABLE='1');control=['-D','-1','--control=fifo:'+str(ctl)+','+str(ack)]
r=row(run([a.perf,'stat',*control,'-x,','-e','cycles:u,instructions:u,branches:u,branch-misses:u','-o',str(out/'disabled.stat'),'--','build/profile',*args(100000,5000000,1)],'disabled-zero',env=disabledperf));equal([r,controls['n100000-s1']]);counts=[]
for line in (out/'disabled.stat').read_text().splitlines():
 if line and not line.startswith('#'):
  rec=next(csv.reader([line]));counts.append(rec[0]);assert rec[0].strip() in ['<not counted>','0'],rec
assert len(counts)==4
run(['objdump','-d','--disassemble=zbtIndexScanSlot','build/profile'],'scan-slot-asm')
for seed in [1,2,3]:
 for n in [100000,1000000]:
  label=f'n{n}-s{seed}';r=row(run([a.perf,'stat',*control,'-x,','-e','cycles:u,instructions:u,branches:u,branch-misses:u','-o',str(out/(label+'.stat')),'--','build/profile',*args(n,5000000,seed)],label+'-stat',env=env));s=row(run([a.perf,'record','-q',*control,'-e','cycles:u','-F997','-g','--call-graph','fp','-o',str(out/(label+'.data')),'--','build/profile',*args(n,5000000,seed)],label+'-record',env=env));equal([r,s,controls[label]])
  run([a.perf,'report','--stdio','--no-children','--sort','symbol','-i',str(out/(label+'.data'))],label+'-report');run([a.perf,'script','-i',str(out/(label+'.data')),'-F','ip,sym,symoff,period'],label+'-samples')
assert {f:sha(source/f) for f in sourcehash}==sourcehash;assert {n:sha(source/'build'/n) for n in binaryhash}==binaryhash
(out/'complete.json').write_text(json.dumps({'status':'complete','finished_utc':now(),'elapsed_seconds':time.monotonic()-start,'sampled_captures':6,'counter_captures':6,'controls':controls,'source_hashes_after':sourcehash,'binary_hashes_after':binaryhash,'raw_data_sha256':{p.name:sha(p) for p in out.glob('*.data')},'source_selection':'NONE'},indent=2)+'\n')
