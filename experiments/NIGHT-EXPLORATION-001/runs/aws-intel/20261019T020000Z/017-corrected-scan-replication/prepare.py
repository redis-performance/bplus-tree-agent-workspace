from pathlib import Path
import json,subprocess,hashlib,datetime,time,io,tarfile,struct
from common import ROOT,P,SOURCES,ACTUAL,sha,check_execution,actual_identity,build_identity
start=time.monotonic();check_execution();actual_identity('actual-before-preparation');assert not SOURCES.exists();SOURCES.mkdir();(P/'preparation').mkdir(exist_ok=False);records=[];validation={};fresh={};freezes={};source=json.loads((P/'source-freeze.json').read_text());models=json.loads((P/'fresh-guard-models.json').read_text());flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer'];inc=['-Isrc','-Icompat','-Ivendor/redis'];v2=[]
def run(cmd,tag,cwd=ROOT):
 left=600-(time.monotonic()-start);assert left>0;t=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:r=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,timeout=left)
 except subprocess.TimeoutExpired as e:
  for ext,val in [('stdout',e.stdout),('stderr',e.stderr)]:(P/'preparation'/(tag+'.'+ext)).write_text(val.decode(errors='replace') if isinstance(val,bytes) else val or '')
  raise
 (P/'preparation'/(tag+'.stdout')).write_text(r.stdout);(P/'preparation'/(tag+'.stderr')).write_text(r.stderr);records.append(dict(tag=tag,command=cmd,cwd=str(cwd.relative_to(ROOT)),started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));(P/'preparation-processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode();return r.stdout
def text_section(path):
 b=path.read_bytes();assert b[:6]==b'\x7fELF\x02\x01';off=struct.unpack_from('<Q',b,40)[0];ents,count,index=struct.unpack_from('<HHH',b,58);assert ents==64 and index<count;sections=[struct.unpack_from('<IIQQQQIIQQ',b,off+i*ents) for i in range(count)];s=sections[index];names=b[s[4]:s[4]+s[5]]
 for x in sections:
  name=names[x[0]:].split(b'\0',1)[0]
  if name==b'.text':return b[x[4]:x[4]+x[5]]
 raise AssertionError('missing ELF text')
for v in ['base','B']:
 d=SOURCES/v;d.mkdir();archive=subprocess.check_output(['git','archive',source['commit'],'src','compat','vendor/redis','bench','tests','Makefile']);tarfile.open(fileobj=io.BytesIO(archive)).extractall(d)
 if v=='B':run(['patch','-p1','-i',str(P/'candidate.patch')],v+'-patch',d)
 assert {f:sha(d/f) for f in source[v]}==source[v];(d/'source-identity.json').write_text(json.dumps(dict(archive_commit=source['commit'],modified_files=[] if v=='base' else ['src/zset_btree.c'],files=source[v]),indent=2)+'\n');(d/'tests/all_match_guard_oracle_v2.c').write_bytes((P/'all_match_guard_oracle_v2.c').read_bytes());(d/'build/corrected-adapter-intel').mkdir(parents=True)
 run(['clang',*inc,*flags,'-O3','bench/microbench.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/corrected-adapter-intel/btree-bench'],v+'-primary-build',d)
 if v=='base':
  original=text_section(ACTUAL/'build/corrected-adapter-intel/btree-bench');reproduced=text_section(d/'build/corrected-adapter-intel/btree-bench');assert original==reproduced;(P/'baseline-text-parity.json').write_text(json.dumps(dict(status='pass',actual_binary_sha256=sha(ACTUAL/'build/corrected-adapter-intel/btree-bench'),reproduced_binary_sha256=sha(d/'build/corrected-adapter-intel/btree-bench'),text_sha256=hashlib.sha256(original).hexdigest(),text_bytes=len(original),debug_path_differences_not_timed=True),indent=2)+'\n')
 for mode in ['native','san']:
  out=d/'build'/('supplement' if mode=='native' else 'supplement-san');run(['python3',str(P/'referee/build.py'),'--source',str(d),'--out',str(out)]+(['--sanitize'] if mode=='san' else []),v+'-'+mode+'-supplement-build');(P/'preparation'/(v+'-'+mode+'-build-manifest.json')).write_bytes((out/'build-manifest.json').read_bytes())
  f=flags+(['-O3'] if mode=='native' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'])
  for portable in ([False] if v=='base' else [False,True]):
   macro=['-DZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE'] if portable else [];suffix=mode+('-portable' if portable else '');binary='build/'+suffix+'-oracle-v2';run(['clang',*inc,*f,*macro,'tests/all_match_guard_oracle_v2.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary],v+'-'+suffix+'-v2-build',d);out=run([binary],v+'-'+suffix+'-v2',d);assert out.strip()=='PASS checks=299664 positions=79864 zero_spans=3072 digest=39f4d4c13e2fdc15';v2.append(dict(variant=v,mode=mode,portable=portable,output=out.strip()))
   if portable:
    binary='build/'+suffix+'-original-tests';run(['clang',*inc,*f,*macro,'-DREDIS_TEST','-DREDIS_DEBUG','tests/upstream.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary],v+'-'+suffix+'-original-build',d);run([binary],v+'-'+suffix+'-original-tests',d)
 left=int(600-(time.monotonic()-start));assert left>0;run(['python3',str(P/'referee/validate.py'),'--native',str(d/'build/supplement'),'--sanitize',str(d/'build/supplement-san'),'--out',str(P/('validation-'+v)),'--seconds',str(left)],v+'-supplement-validation');validation[v]=json.loads((P/('validation-'+v)/'RESULT.json').read_text());assert validation[v]['status']=='pass';assert (P/('validation-'+v)/'fixture-model-manifest.json').read_bytes()==(P/'original-reviewed-models.json').read_bytes();fresh[v]=[]
 for model in models:
  for mode in ['native','san']:
   build=d/'build'/('supplement' if mode=='native' else 'supplement-san');args=['run','trim','319',str(model['seed']),'2','0','0'];public=json.loads(run([str(build/'scan-supplement'),*args],v+'-'+mode+'-fresh-'+str(model['seed'])+'-public'));both=[json.loads(x) for x in run([str(build/'scan-census'),*args],v+'-'+mode+'-fresh-'+str(model['seed'])+'-census').splitlines()];assert len(both)==2;cen,row=both;assert row==public
   for k in ['n','bytes','seed','encoding','callbacks_per_pass','checksum_per_pass']:assert public[k]==model[k]
   assert public['passes']==public['elapsed_ns']==public['thread_elapsed_ns']==0 and public['validation']=='pass' and public['warmup_passes']==public['prepost_oracles']==2 and public['warmup_callback_parity'];assert cen['members']==cen['reversed_members']==cen['long_records']==7 and cen['leaves']==cen['reversed_leaves']==1;assert cen['full16_chunks']==cen['full8_chunks']==cen['external']==cen['short_records']==0;fresh[v].append(dict(seed=model['seed'],mode=mode,census=cen,public=public));(P/'fresh-validation.json').write_text(json.dumps(fresh,indent=2)+'\n')
 names=list(source[v])+['source-identity.json','tests/all_match_guard_oracle_v2.c','build/corrected-adapter-intel/btree-bench']
 for mode in ['supplement','supplement-san']:names += ['build/'+mode+'/'+name for name in ['scan-supplement','scan-census','upstream-test','inputs/scan-supplement.c','inputs/tree-census.c','inputs/census.h']]
 names += [str(f.relative_to(d)) for f in (d/'build').glob('*-oracle-v2')]+[str(f.relative_to(d)) for f in (d/'build').glob('*-original-tests')];freezes[v]={f:sha(d/f) for f in names}
assert fresh['base']==fresh['B'];assert json.loads((P/'validation-base/cells.json').read_text())==json.loads((P/'validation-B/cells.json').read_text());assert (P/'validation-base/fixture-model-manifest.json').read_bytes()==(P/'validation-B/fixture-model-manifest.json').read_bytes();(P/'build-freeze.json').write_text(json.dumps(freezes,indent=2)+'\n');build_identity('build-after-preparation');actual_identity('actual-after-preparation');compiler=run(['clang','--version'],'compiler-version').strip();(P/'preparation-summary.json').write_text(json.dumps(dict(status='pass',elapsed_seconds=time.monotonic()-start,validation=validation,fresh_guard_cells_per_source=len(fresh['base']),v2=v2,baseline_text_parity=True,compiler=compiler),indent=2)+'\n');print('PASS corrected exact B correctness and fresh known-guard validation')
