from pathlib import Path
import subprocess,json,hashlib,datetime,time,io,tarfile,os,csv
root=Path.cwd();p=Path(__file__).parent.resolve();d=root/'scratch/intel-scan-profile-matched';d.mkdir(exist_ok=False);(p/'profiles').mkdir(exist_ok=True);records=[];start=time.monotonic();hashes={}
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def run(cmd,tag,cwd,env=None):
 left=300-(time.monotonic()-start);assert left>0
 t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,env=env,timeout=min(left,120))
 (p/'profiles'/(tag+'.stdout')).write_text(r.stdout);(p/'profiles'/(tag+'.stderr')).write_text(r.stderr)
 records.append(dict(tag=tag,command=cmd,cwd=str(cwd.relative_to(root)),started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));(p/'processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode();return r.stdout
flags=['-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']
for v in ['base','B']:
 dest=d/v;dest.mkdir();data=subprocess.check_output(['git','archive','8fab511e','src','compat','vendor/redis','tests','bench','Makefile']);tarfile.open(fileobj=io.BytesIO(data)).extractall(dest);(dest/'build').mkdir()
 if v=='B':run(['patch','-p1','-i',str(p.parent/'007-scan-replication/variants/B/candidate.patch')],v+'-patch',dest)
 (dest/'bench/scan-profile.c').write_bytes((p/'scan-profile.c').read_bytes());(dest/'bench/sampler.c').write_bytes((p/'sampler.c').read_bytes())
 for mode in ['original','disabled','profile','original-sanitize','disabled-sanitize']:
  san=mode.endswith('sanitize');f=flags+(['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'] if san else ['-O3']);original=mode.startswith('original');driver='bench/microbench.c' if original else 'bench/scan-profile.c'
  extra=[] if original else ['-DPROFILE_SAMPLE','bench/sampler.c']+(['-DSAMPLE_DISABLED'] if mode.startswith('disabled') else [])
  run(['clang',*f,*extra,driver,'src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+mode],v+'-'+mode+'-build',dest)
 hashes[v]={f:sha(dest/f) for f in ['src/zset_btree.c','src/zset_btree.h','bench/microbench.c','bench/scan-profile.c','bench/sampler.c','compat/standalone.c','vendor/redis/siphash.c']+['build/'+mode for mode in ['original','disabled','profile','original-sanitize','disabled-sanitize']]}
assert hashes['base']['src/zset_btree.c']=='d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2';assert hashes['B']['src/zset_btree.c']=='204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23'
for f in hashes['base']:
 if not f.startswith('build/') and f!='src/zset_btree.c':assert hashes['base'][f]==hashes['B'][f]
(p/'build-freeze.json').write_text(json.dumps(hashes,indent=2)+'\n')
for mode in ['enabled','disabled']:
 dest=d/'base';extra=['-DSAMPLE_SELF_TEST']+(['-DSAMPLE_DISABLED'] if mode=='disabled' else [])
 run(['clang',*flags,'-O3',*extra,'bench/sampler.c','-o','build/known-'+mode],'known-'+mode+'-build',dest)
 env=os.environ.copy();env['SAMPLE_OUT']=str(p/'profiles'/('known-'+mode+'.hist.csv'));run(['build/known-'+mode],'known-'+mode,dest,env)
 syms=run(['nm','-n','-S','build/known-'+mode],'known-'+mode+'-symbols',dest)
known={mode:{int(r['offset']):int(r['count']) for r in csv.DictReader((p/'profiles'/('known-'+mode+'.hist.csv')).open())} for mode in ['enabled','disabled']}
assert not sum(known['disabled'].values());assert (p/'profiles/known-enabled.stdout').read_text()==(p/'profiles/known-disabled.stdout').read_text()
syms=[x.split() for x in (p/'profiles/known-enabled-symbols.stdout').read_text().splitlines()];base=[int(x[0],16) for x in syms if x[-1]=='__executable_start'][0];work=[x for x in syms if x[-1]=='known_work'][0];address,size=int(work[0],16),int(work[1],16);total=sum(known['enabled'].values());inside=sum(c for o,c in known['enabled'].items() if address<=base+o<address+size);assert total>=20 and inside/total>=.9
(p/'known-control.json').write_text(json.dumps(dict(enabled_samples=total,known_work_samples=inside,disabled_samples=0,checksum_equal=True),indent=2)+'\n')
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes'];semantic=[]
def scan(v,mode,n,ops,seed,tag):
 env=os.environ.copy();env['SAMPLE_OUT']=str(p/'profiles'/(tag+'.hist.csv'))
 out=run(['build/'+mode,'--case','scan','--size',str(n),'--ops',str(ops),'--member-bytes','16','--seed',str(seed)],tag,d/v,env);rows=list(csv.DictReader(out.splitlines()));assert len(rows)==1 and rows[0]['cpu_start']==rows[0]['cpu_end']=='2';return rows[0]
for v in ['base','B']:
 for n in [100,1000,10000]:
  a=scan(v,'original',n,n,301,f'{v}-original-control-{n}');b=scan(v,'disabled',n,n,301,f'{v}-disabled-control-{n}');assert all(a[k]==b[k] for k in fields);assert sum(int(r['count']) for r in csv.DictReader((p/'profiles'/f'{v}-disabled-control-{n}.hist.csv').open()))==0;semantic.append(dict(variant=v,mode='native',size=n,fields_equal=True))
 a=scan(v,'original-sanitize',1000,1000,301,v+'-original-san-control');b=scan(v,'disabled-sanitize',1000,1000,301,v+'-disabled-san-control');assert all(a[k]==b[k] for k in fields);assert sum(int(r['count']) for r in csv.DictReader((p/'profiles'/(v+'-disabled-san-control.hist.csv')).open()))==0;semantic.append(dict(variant=v,mode='sanitizer',size=1000,fields_equal=True))
(p/'semantic-controls.json').write_text(json.dumps(semantic,indent=2)+'\n')
captures=[]
for seed in [301,302,303]:
 for n in [100000,1000000]:
  pair=[]
  for v in (['base','B'] if seed%2 else ['B','base']):
   tag=f'{v}-scan-{n}-seed{seed}';row=scan(v,'profile',n,5000000,seed,tag);pair.append(row);captures.append(dict(variant=v,size=n,seed=seed,tag=tag,row=row));(p/'captures.json').write_text(json.dumps(captures,indent=2)+'\n')
  assert all(pair[0][k]==pair[1][k] for k in fields)
for v in ['base','B']:
 syms=run(['nm','-n','-S','build/profile'],v+'-symbols',d/v);base=[int(x.split()[0],16) for x in syms.splitlines() if x.split()[-1]=='__executable_start'][0];offsets=set()
 for c in captures:
  if c['variant']==v:offsets.update(int(r['offset']) for r in csv.DictReader((p/'profiles'/(c['tag']+'.hist.csv')).open()))
 cmd=['llvm-symbolizer-18','--inlining','--output-style=JSON','--obj=build/profile']+[hex(base+x) for x in sorted(offsets)];mapping=run(cmd,v+'-inline-map',d/v);json.loads(mapping)
 (p/(v+'-mapping.json')).write_text(json.dumps(dict(linker_base=base,bucket_count=len(offsets),command=cmd),indent=2)+'\n')
 run(['objdump','-d','--disassemble=zbtIndexScanSlot','build/profile'],v+'-scan-slot',d/v)
(p/'complete.json').write_text(json.dumps(dict(status='complete',elapsed_seconds=time.monotonic()-start,captures=len(captures)),indent=2)+'\n');print('PASS12 matched captures, known-work and matched-mode controls')
