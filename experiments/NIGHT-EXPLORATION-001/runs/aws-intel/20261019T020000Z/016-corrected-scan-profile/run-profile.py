from pathlib import Path
import subprocess,json,hashlib,datetime,time,io,tarfile,os,csv,re
root=Path.cwd();p=Path(__file__).parent.resolve();d=root/'scratch/intel-corrected-scan-profile/base';actual=root/'scratch/intel-corrected-adapter';start=time.monotonic();records=[]
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
freeze=json.loads((p/'execution-freeze.json').read_text())
for f,h in freeze['files'].items():assert sha(p/f)==h
assert sha(p.parent/'013-corrected-adapter-baseline/source-after.json')==freeze['actual_artifact_manifest_sha256']
expected=json.loads((p.parent/'013-corrected-adapter-baseline/source-after.json').read_text())['files']
def identities(tag):
 observed={f:sha(actual/f) for f in expected};assert observed==expected
 (p/(tag+'.json')).write_text(json.dumps(dict(status='pass',files=observed),indent=2)+'\n')
identities('actual-before');assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=actual,text=True).strip()=='13e459ff8800be3f02b6b45c87dd7b0c39453fa9'
d.mkdir(parents=True,exist_ok=False);(p/'profiles').mkdir(exist_ok=False)
tarfile.open(fileobj=io.BytesIO(subprocess.check_output(['git','archive','13e459ff8','src','compat','vendor/redis','tests','bench','Makefile']))).extractall(d);(d/'build').mkdir()
for f in ['scan-profile.c','sampler.c']:(d/'bench'/f).write_bytes((p/f).read_bytes())
def run(cmd,tag,cwd=d,env=None):
 left=600-(time.monotonic()-start);assert left>0;t=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:r=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,env=env,timeout=left)
 except subprocess.TimeoutExpired as e:
  for ext,val in [('stdout',e.stdout),('stderr',e.stderr)]:(p/'profiles'/(tag+'.'+ext)).write_text(val.decode(errors='replace') if isinstance(val,bytes) else val or '')
  raise
 (p/'profiles'/(tag+'.stdout')).write_text(r.stdout);(p/'profiles'/(tag+'.stderr')).write_text(r.stderr);records.append(dict(tag=tag,command=cmd,cwd=str(cwd.relative_to(root)),started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));(p/'processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode();return r.stdout
assert os.sched_getaffinity(0)=={2}
flags=['-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']
for mode in ['disabled','profile','disabled-sanitize']:
 san=mode.endswith('sanitize');f=flags+(['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'] if san else ['-O3']);extra=['-DPROFILE_SAMPLE','bench/sampler.c']+(['-DSAMPLE_DISABLED'] if mode.startswith('disabled') else [])
 run(['clang',*f,*extra,'bench/scan-profile.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+mode],mode+'-build')
names=['src/zset_btree.c','src/zset_btree.h','compat/standalone.c','compat/server.h','bench/microbench.c','bench/scan-profile.c','bench/sampler.c','vendor/redis/siphash.c']+['build/'+x for x in ['disabled','profile','disabled-sanitize']];build={f:sha(d/f) for f in names};(p/'build-freeze.json').write_text(json.dumps({'base':build},indent=2)+'\n')
for f in names:
 if f in expected:assert build[f]==expected[f]
for mode in ['enabled','disabled']:
 run(['clang',*flags,'-O3','-DSAMPLE_SELF_TEST',*(['-DSAMPLE_DISABLED'] if mode=='disabled' else []),'bench/sampler.c','-o','build/known-'+mode],'known-'+mode+'-build')
 env=os.environ.copy();env['SAMPLE_OUT']=str(p/'profiles'/('known-'+mode+'.hist.csv'));run(['build/known-'+mode],'known-'+mode,env=env);run(['nm','-n','-S','build/known-'+mode],'known-'+mode+'-symbols')
hists={m:{int(r['offset']):int(r['count']) for r in csv.DictReader((p/'profiles'/('known-'+m+'.hist.csv')).open())} for m in ['enabled','disabled']};assert not sum(hists['disabled'].values());assert (p/'profiles/known-enabled.stdout').read_bytes()==(p/'profiles/known-disabled.stdout').read_bytes()
syms=[x.split() for x in (p/'profiles/known-enabled-symbols.stdout').read_text().splitlines()];base=int(next(x[0] for x in syms if x[-1]=='__executable_start'),16);work=next(x for x in syms if x[-1]=='known_work');lo,size=int(work[0],16),int(work[1],16);total=sum(hists['enabled'].values());inside=sum(c for o,c in hists['enabled'].items() if lo<=base+o<lo+size);assert total>=20 and inside/total>=.9
(p/'known-control.json').write_text(json.dumps(dict(enabled_samples=total,known_work_samples=inside,disabled_samples=0,checksum_equal=True),indent=2)+'\n')
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']
def scan(mode,n,ops,seed,tag):
 env=os.environ.copy();env['SAMPLE_OUT']=str(p/'profiles'/(tag+'.hist.csv'))
 binary=str(actual/('build/corrected-adapter-intel'+('/sanitize' if mode=='original-sanitize' else '')+'/btree-bench')) if mode.startswith('original') else 'build/'+mode
 out=run([binary,'--case','scan','--size',str(n),'--ops',str(ops),'--member-bytes','16','--seed',str(seed)],tag,env=env);rows=list(csv.DictReader(out.splitlines()));assert len(rows)==1 and rows[0]['cpu_start']==rows[0]['cpu_end']=='2';return rows[0]
controls=[];fixtures={}
for seed in [1,2,3]:
 for n in [100000,1000000]:
  a=scan('original',n,5000000,seed,f'original-control-{n}-{seed}');b=scan('disabled',n,5000000,seed,f'disabled-control-{n}-{seed}');assert all(a[k]==b[k] for k in fields);fixtures[(n,seed)]=a;controls.append(dict(size=n,seed=seed,mode='native',original=a,disabled=b))
a=scan('original-sanitize',1000,1000,1,'original-san-control');b=scan('disabled-sanitize',1000,1000,1,'disabled-san-control');assert all(a[k]==b[k] for k in fields);controls.append(dict(size=1000,seed=1,mode='sanitizer',original=a,disabled=b));(p/'semantic-controls.json').write_text(json.dumps(controls,indent=2)+'\n')
captures=[]
for spec in json.loads((p/'capture-schedule.json').read_text()):
 n,seed,repeat=spec['size'],spec['seed'],spec['repeat'];tag=f'r{repeat:02d}-scan-{n}-seed{seed}';row=scan('profile',n,5000000,seed,tag);assert all(row[k]==fixtures[(n,seed)][k] for k in fields);captures.append(dict(**spec,tag=tag,row=row));(p/'captures.json').write_text(json.dumps(captures,indent=2)+'\n')
# Preserve complete function disassembly and actual timing-binary instruction/source maps.
binaries={'diagnostic':'build/profile','actual':str(actual/'build/corrected-adapter-intel/btree-bench')};maps={}
for tag,binary in binaries.items():
 symbols=run(['nm','-n','-S',binary],tag+'-symbols');syms=[x.split() for x in symbols.splitlines()];linkbase=int(next(x[0] for x in syms if x[-1]=='__executable_start'),16);sym=next(x for x in syms if x[-1]=='zbtIndexScanSlot');address,size=int(sym[0],16),int(sym[1],16)
 asm=run(['objdump','-d','--insn-width=16','--disassemble=zbtIndexScanSlot',binary],tag+'-scan-slot');run(['objdump','-dSl','--disassemble=zbtIndexScanSlot',binary],tag+'-scan-slot-source');instructions=[]
 for line in asm.splitlines():
  match=re.match(r'^\s*([0-9a-f]+):\s+((?:[0-9a-f]{2}\s+)+)\s*(.*)$',line)
  if match:
   pc=int(match[1],16);raw=match[2].split();instructions.append(dict(address=pc,offset=pc-address,bytes=raw,assembly=match[3]))
 assert instructions
 mapping=json.loads(run(['llvm-symbolizer-18','--inlining','--output-style=JSON','--obj='+binary]+[hex(x['address']) for x in instructions],tag+'-instruction-map'))
 for ins,symbol in zip(instructions,mapping):assert int(symbol['Address'],16)==ins['address'];ins['frames']=symbol['Symbol']
 maps[tag]=dict(binary=binary,linker_base=linkbase,address=address,size=size,instructions=instructions)
(p/'instruction-maps.json').write_text(json.dumps(maps,indent=2)+'\n')
by_offset={x['offset']:x for x in maps['actual']['instructions']};matched=[]
for ins in maps['diagnostic']['instructions']:
 other=by_offset.get(ins['offset']);matched.append(dict(offset=ins['offset'],diagnostic=ins,actual=other,exact_bytes=bool(other and ins['bytes']==other['bytes'])))
(p/'actual-attribution-map.json').write_text(json.dumps(dict(method='Same ScanSlot function-relative instruction offset and exact opcode bytes; all mismatches retained. Two-byte sample buckets approximate instruction boundaries.',same_function_size=maps['actual']['size']==maps['diagnostic']['size'],instructions=matched),indent=2)+'\n')
offsets=set()
for c in captures:offsets.update(int(r['offset']) for r in csv.DictReader((p/'profiles'/(c['tag']+'.hist.csv')).open()))
base=maps['diagnostic']['linker_base'];run(['llvm-symbolizer-18','--inlining','--output-style=JSON','--obj=build/profile']+[hex(base+x) for x in sorted(offsets)],'diagnostic-inline-map');(p/'mapping.json').write_text(json.dumps(dict(linker_base=base,bucket_count=len(offsets)),indent=2)+'\n')
identities('actual-after');assert {f:sha(d/f) for f in build}==build;(p/'diagnostic-after.json').write_text(json.dumps(dict(status='pass',files=build),indent=2)+'\n')
(p/'complete.json').write_text(json.dumps(dict(status='complete',captures=len(captures),elapsed_seconds=time.monotonic()-start),indent=2)+'\n');print('PASS 60 corrected baseline captures and matched controls')
