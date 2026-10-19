#!/usr/bin/env python3
"""Reconstruct raw effects, patches and exact frozen identities; no timing runs."""
import csv,hashlib,importlib.util,io,json,statistics,subprocess,sys
from pathlib import Path
from datetime import datetime
sys.dont_write_bytecode=True
E=Path(__file__).resolve().parent;R=Path.cwd();S=Path('scratch/m6-decode')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
spec=importlib.util.spec_from_file_location('decode_worker',E/'run.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
freeze=json.loads((E/'comparison-freeze.json').read_text());ref=json.loads((E/'referee-freeze.json').read_text());checks=0; document_changes=[]
for group in (freeze['files'],freeze['baseline_hashes'],ref['files'],ref['original_referee']):
 for p,h in group.items():
  current=sha(p)
  if current!=h:
   assert p.endswith('/SELECTION.md') and group is ref['files'],(p,'frozen file changed')
   old=subprocess.check_output(['git','show','80177d1e:'+p]);chair=subprocess.check_output(['git','show','e62f839d:'+p])
   assert hashlib.sha256(old).hexdigest()==h and hashlib.sha256(chair).hexdigest()==current
   document_changes.append(dict(path=p,initial_referee_note_sha256=h,chair_note_sha256=current,initial_publication='80177d1e',superseded_before_timing_publication='e62f839d',cause='Case-insensitive SELECTION.md/selection.md path collision; executable referee/source unaffected. Original manifest preserved.'))
  checks+=1
for p in E.glob('build-*.json'):
 d=json.loads(p.read_text());assert sha(d['binary'])==d['binary_sha256'];assert sha(S/'variants'/d['variant']/'src/zset_btree.c')==d['source_sha256']
cal=json.loads((E/'calibration.json').read_text());observations=0;effects=0;windows=[]
def raw(r):
 global observations
 data=(E/r['file']).read_bytes();assert hashlib.sha256(data).hexdigest()==r['sha256']
 rr=list(csv.DictReader(io.StringIO(data.decode())));assert len(rr)==1;x=rr[0]
 assert tuple(map(int,(x['width'],x['reversed'],x['count'])))==tuple(r['cell'])
 assert int(x['operations'])==r['operations']==r['rounds']*8*r['cell'][2]
 assert int(x['rounds'])==r['rounds'] and int(x['seed'])==r['seed']
 assert float(x['elapsed_ns'])==r['elapsed_ns'] and float(x['ns_per_decode'])==r['ns_op']
 assert abs(r['ns_op']-r['elapsed_ns']/r['operations'])<1e-8
 assert x['checksum']==r['checksum'] and x['fixture_hash']==r['fixture_hash'] and int(x['leaf_bytes'])==r['leaf_bytes']
 observations+=1
for r in cal['observations']:raw(r)
assert len(cal['observations'])==528
for cell in m.CELLS:
 key='-'.join(map(str,cell));rs=[r for r in cal['observations'] if r['cell']==list(cell)];assert len(rs)==3
 import math
 expected=min(100000000//(8*cell[2]),math.ceil(50000000/min(r['elapsed_ns']/10000 for r in rs)))
 assert cal['fixed_rounds'][key]==expected
all_phases={}
for phase in ('aa','A','B','C'):
 d=json.loads((E/f'comparison-{phase}.json').read_text());assert d['status']=='complete' and len(d['runs'])==4224 and d['wall_seconds']<=300
 all_phases[phase]=d
 for r in d['runs']:
  raw(r);assert r['rounds']==cal['fixed_rounds']['-'.join(map(str,r['cell']))]
  assert r['operations']<=100000000 and r['seed']==(1,2,3,1,2,3)[r['block']]
  assert r['variant']==('base' if phase=='aa' or r['label']=='A' else phase)
 for result in d['results']:
  rs=[r for r in d['runs'] if r['cell']==result['cell']];assert len(rs)==24;es=[]
  if result['cell'][2]==1:assert len({r['fixture_hash'] for r in rs})==1,'count1 input diversity claim invalid'
  for block in range(6):
   rr=sorted((r for r in rs if r['block']==block),key=lambda r:r['step']);assert ''.join(r['label'] for r in rr)=='ABBA'
   assert len({r['checksum'] for r in rr})==len({r['fixture_hash'] for r in rr})==len({r['leaf_bytes'] for r in rr})==1
   es.append(100*(statistics.mean(r['ns_op'] for r in rr if r['label']=='B')/statistics.mean(r['ns_op'] for r in rr if r['label']=='A')-1))
  assert all(abs(a-b)<1e-10 for a,b in zip(es,result['effects_pct']));assert statistics.median(es)==result['median_pct'];effects+=6
  assert result['qualified']==(max(map(abs,es))<=1 and min(r['elapsed_ns'] for r in rs)>=10000000)
  # Same cell/seed memory identity applies across every phase too.
  for other in all_phases.values():
   assert {r['leaf_bytes'] for r in rs}=={r['leaf_bytes'] for r in other['runs'] if r['cell']==result['cell']}
patches=[]
for v in ('A','B','C'):
 dest=S/'audit'/v/'src';dest.mkdir(parents=True,exist_ok=True);target=dest/'zset_btree.c';target.write_text(m.source('base'))
 q=subprocess.run(['patch','-p1','-d',str(dest.parent)],input=(E/f'variants/{v}/candidate.patch').read_text(),text=True,capture_output=True,timeout=10)
 assert q.returncode==0,q.stderr
 assert sha(target)==sha(S/'variants'/v/'src/zset_btree.c')
 patches.append(dict(variant=v,patch_sha256=sha(E/f'variants/{v}/candidate.patch'),reconstructed_source_sha256=sha(target)))
commands=[json.loads(l) for l in (E/'commands.jsonl').read_text().splitlines()]
for i,r in enumerate(commands):
 a=datetime.fromisoformat(r['started_utc']);b=datetime.fromisoformat(r['finished_utc']);assert a<=b
 if i:assert a>=datetime.fromisoformat(commands[i-1]['finished_utc']),'overlapping command windows'
 assert r['returncode']==(2 if r['name'] in ('fault-wrong-one','fault-skip-bulk') else 0)
windows=len(commands)
normalize=lambda s:s.replace('_zbtDecodeBulkBridge','_zbtScoreLeafDecodeRange')
bc_caller=normalize((E/'codegen/B-decoder_batch.asm').read_text())==(E/'codegen/C-decoder_batch.asm').read_text()
bc_bulk=normalize((E/'codegen/B-zbtDecodeBulkBridge.asm').read_text())==(E/'codegen/C-zbtScoreLeafDecodeRange.asm').read_text()
guards=[];aa={tuple(x['cell']):x for x in all_phases['aa']['results']};caps={tuple(x['cell']) for x in json.loads((E/'cap-limited-cells.json').read_text())}
for v in ('A','B','C'):
 candidates=[x for x in all_phases[v]['results'] if x['cell']!=[60,0,1] and aa[tuple(x['cell'])]['qualified'] and tuple(x['cell']) not in caps]
 repeated=[x for x in candidates if x['min_pct']>1]
 best=max(candidates,key=lambda x:x['min_pct'])
 guards.append(dict(variant=v,uncapped_qualified_all_six_blocks_regress_over_1pct=len(repeated),example=best))
result=dict(status='pass_with_recorded_precomparison_document_change',document_changes=document_changes,frozen_file_checks=checks,raw_measurement_rows=observations,reconstructed_block_effects=effects,serial_command_windows=windows,patches=patches,bc_caller_equal_after_symbol_rename=bc_caller,bc_bulk_equal_after_symbol_rename=bc_bulk,guard_examples=guards,last_experimental_child=commands[-1]['finished_utc'],profile_validation='Baseline primary sufficient; three guard captures insufficient. No candidate profile validation or independent review.',source_selection='NONE')
save(E/'audit.json',result);print(json.dumps(result,indent=2))
