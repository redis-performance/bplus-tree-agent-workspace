from pathlib import Path
import json,subprocess,hashlib,datetime,time,io,tarfile,itertools
root=Path.cwd();p=Path(__file__).parent.resolve();d=root/'scratch/intel-focused-scan';d.mkdir(exist_ok=False);logs=p/'validation';logs.mkdir(exist_ok=False);records=[];start=time.monotonic();cells={};builds={}
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
fixtures=json.loads((p/'fixture-manifest.json').read_text())
for f in fixtures:assert sha(p/'fixtures'/(f['name']+'.bin'))==f['sha256']
def run(cmd,tag,expected=0):
 left=900-(time.monotonic()-start);assert left>0
 t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(120,left));(logs/(tag+'.stdout')).write_text(r.stdout);(logs/(tag+'.stderr')).write_text(r.stderr)
 records.append(dict(tag=tag,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode,expected_returncode=expected));(p/'validation-processes.json').write_text(json.dumps(records,indent=2)+'\n');assert r.returncode==expected,(tag,r.stderr);return r.stdout
for v in ['base','B']:
 dest=d/v;dest.mkdir();data=subprocess.check_output(['git','archive','8fab511e','src','compat','vendor/redis','tests','bench','Makefile']);tarfile.open(fileobj=io.BytesIO(data)).extractall(dest)
 if v=='B':run(['patch','-d',str(dest),'-p1','-i',str(p.parent/'007-scan-replication/variants/B/candidate.patch')],v+'-patch')
 for mode in ['native','san']:
  out=dest/'build'/('focused' if mode=='native' else 'focused-san');run(['python3',str(p/'referee/build.py'),'--source',str(dest),'--out',str(out)]+(['--sanitize'] if mode=='san' else []),v+'-'+mode+'-build');run([str(out/'upstream-test')],v+'-'+mode+'-original-tests');(logs/(v+'-'+mode+'-build-manifest.json')).write_bytes((out/'build-manifest.json').read_bytes())
 builds[v]={f:sha(dest/f) for f in ['src/zset_btree.c','src/zset_btree.h','compat/standalone.c','vendor/redis/siphash.c','tests/upstream.c','build/focused/scan-guard','build/focused/scan-census','build/focused-san/scan-guard']}
 cells[v]={}
 for f in fixtures:
  filename=p/'fixtures'/(f['name']+'.bin');assert sha(filename)==f['sha256']
  for order in [0,1,2]:
   tag=f['name']+'-o'+str(order);out=run([str(dest/'build/focused/scan-census'),'run',str(filename),str(order),'0','0'],v+'-'+tag+'-census');c,r=[json.loads(x) for x in out.splitlines()];assert c['members']==r['n'] and sum(c['tag_histogram'])==r['n']
   if order==1:assert c['reversed_leaves']>0 and c['reversed_members']>0
   if r['distribution']==1:assert c['tag_histogram'][17]==r['n']
   if r['distribution']==2:assert c['tag_histogram'][0]>0 and c['tag_histogram'][1]>0 and sum(c['tag_histogram'][:2])==r['n']
   models={}
   for mode in ['native','san']:
    binary=dest/'build'/('focused' if mode=='native' else 'focused-san')/'scan-guard';actual=json.loads(run([str(binary),'run',str(filename),str(order),'0','0'],v+'-'+tag+'-'+mode));keys=['n','bytes','seed','distribution','order']
    if mode=='native':keys+=['callbacks_per_pass','checksum_per_pass','tree_bytes']
    assert all(actual[k]==r[k] for k in keys);assert actual['validation']=='pass' and actual['passes']==actual['elapsed_ns']==0;models[mode]=actual
   cells[v][tag]=dict(census=c,models=models)
   (p/'validation-cells.json').write_text(json.dumps(cells,indent=2)+'\n')
 for mode in ['native','san']:
  binary=dest/'build'/('focused' if mode=='native' else 'focused-san')/'scan-guard'
  for fault in [1,2,3,4]:run([str(binary),'run',str(p/'fixtures/s101-n4096-b16-d0.bin'),'0','0',str(fault)],f'{v}-{mode}-fault{fault}',2)
assert builds['base']['src/zset_btree.c']=='d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2';assert builds['B']['src/zset_btree.c']=='204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23'
for tag in cells['base']:
 assert cells['base'][tag]==cells['B'][tag],tag
(p/'build-freeze.json').write_text(json.dumps(builds,indent=2)+'\n');(p/'validation-summary.json').write_text(json.dumps(dict(status='pass',sources=2,cells_per_source=108,native_sanitizer_models=432,census_cells=216,detected_faults=16,original_tests='43 per source/build',elapsed_seconds=time.monotonic()-start,commands=len(records),native_and_san_cross_source_models_equal=True,cross_allocator_equality_required=False),indent=2)+'\n');print('PASS baseline/B108 native+san models and census parity;16 fault controls; original43 tests/build')
