from pathlib import Path
import subprocess,json,hashlib,datetime,time,tarfile,io
root=Path.cwd();p=Path(__file__).parent.resolve();dest=root/'scratch/intel-scan-supplement';assert not dest.exists();dest.mkdir();(p/'preparation').mkdir();start=time.monotonic();records=[];freezes={};validation={}
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
for f,h in json.loads((p/'import-freeze.json').read_text())['files'].items():assert sha(p/f)==h

def run(cmd,tag):
 left=600-(time.monotonic()-start);assert left>0;t=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:r=subprocess.run(cmd,capture_output=True,text=True,timeout=left)
 except subprocess.TimeoutExpired as e:
  for ext,value in [('stdout',e.stdout),('stderr',e.stderr)]: (p/'preparation'/(tag+'.'+ext)).write_text(value.decode(errors='replace') if isinstance(value,bytes) else value or '')
  raise
 (p/'preparation'/(tag+'.stdout')).write_text(r.stdout);(p/'preparation'/(tag+'.stderr')).write_text(r.stderr);records.append(dict(tag=tag,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));(p/'preparation-processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode()
for v in ['base','B']:
 d=dest/v;d.mkdir();tarfile.open(fileobj=io.BytesIO(subprocess.check_output(['git','archive','8fab511e','src','compat','vendor/redis','bench','tests','Makefile']))).extractall(d)
 if v=='B':run(['patch','-d',str(d),'-p1','-i',str(p.parent/'007-scan-replication/variants/B/candidate.patch')],v+'-patch')
 for mode in ['native','san']:
  out=d/'build'/('supplement' if mode=='native' else 'supplement-san');run(['python3',str(p/'referee/build.py'),'--source',str(d),'--out',str(out)]+(['--sanitize'] if mode=='san' else []),v+'-'+mode+'-build');(p/'preparation'/(v+'-'+mode+'-build-manifest.json')).write_bytes((out/'build-manifest.json').read_bytes())
 left=int(600-(time.monotonic()-start));assert left>0
 run(['python3',str(p/'referee/validate.py'),'--native',str(d/'build/supplement'),'--sanitize',str(d/'build/supplement-san'),'--out',str(p/('validation-'+v)),'--seconds',str(left)],v+'-validate')
 validation[v]=json.loads((p/('validation-'+v)/'RESULT.json').read_text());assert validation[v]['status']=='pass';assert (p/('validation-'+v)/'fixture-model-manifest.json').read_bytes()==(p/'referee/baseline-validation/fixture-model-manifest.json').read_bytes()
 names=['src/zset_btree.c','src/zset_btree.h','compat/standalone.c','compat/server.h','vendor/redis/siphash.c','tests/upstream.c','bench/microbench.c']
 for mode in ['supplement','supplement-san']:
  names += ['build/'+mode+'/'+f for f in ['scan-supplement','scan-census','upstream-test','inputs/scan-supplement.c','inputs/tree-census.c','inputs/census.h']]
 freezes[v]={f:sha(d/f) for f in names}
assert json.loads((p/'validation-base/cells.json').read_text())==json.loads((p/'validation-B/cells.json').read_text());assert freezes['base']['src/zset_btree.c']=='d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2';assert freezes['B']['src/zset_btree.c']=='204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23'
(p/'build-freeze.json').write_text(json.dumps(freezes,indent=2)+'\n');(p/'preparation-summary.json').write_text(json.dumps(dict(status='pass',elapsed_seconds=time.monotonic()-start,validation=validation,models_equal=True,independent_model_hashes_match=True),indent=2)+'\n');print('PASS two-source original native/sanitizer supplemental validation')
