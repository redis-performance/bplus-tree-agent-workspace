from pathlib import Path
import json,csv,hashlib,statistics,datetime
p=Path('scratch/review-intel-c3e5882ca/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/007-scan-replication');result={};freeze=json.loads((p/'screen-freeze.json').read_text())
for name,h in freeze['files'].items():assert hashlib.sha256((p/name).read_bytes()).hexdigest()==h
man=json.loads((p/'candidate-freeze.json').read_text())
for name in ['src/zset_btree.h','bench/microbench.c','compat/standalone.c','vendor/redis/siphash.c','tests/upstream.c','Makefile','tests/all_match_guard_oracle_v2.c']:assert len({v[name] for v in man.values()})==1,name
assert man['base']['build/btree-bench']==json.loads((p/'comparison-freeze.json').read_text())['binary_sha256']
assert man['B']['src/zset_btree.c']=='204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23'
schedule=json.loads((p/'screen-schedule.json').read_text())
for phase,expected in [('aa',48),('screen',96)]:
 data=json.loads((p/(phase+'.json')).read_text());assert data['status']=='complete';rows=data['rows'];assert len(rows)==expected
 for i,x in enumerate(rows):
  raw=list(csv.DictReader((p/'raw'/f'{phase}-{i:03d}.stdout').read_text().splitlines()));assert len(raw)==1 and raw[0]==x['row'];assert not (p/'raw'/f'{phase}-{i:03d}.stderr').read_text()
  r=x['row'];assert r['case']=='scan' and int(r['requested_ops'])==5000000 and int(r['member_bytes'])==16 and int(r['cpu_start'])==int(r['cpu_end'])==2
  assert int(r['seed']) in [101,102,103] and int(r['seed'])==101+x['block']%3
  assert int(r['elapsed_ns'])>=10000000
  if i:assert datetime.datetime.fromisoformat(rows[i-1]['finished_utc'])<=datetime.datetime.fromisoformat(x['started_utc'])
  if phase=='screen':assert all(x[k]==v for k,v in schedule[i].items())
 groups={}
 for x in rows:groups.setdefault((x.get('variant','base'),x['size'],x['block']),[]).append(x)
 effects=[]
 for (v,n,b),rr in groups.items():
  assert len(rr)==4 and [x['position'] for x in rr]==[0,1,2,3]
  for field in ['size','seed','checksum','operations','tree_bytes','traversals','warmup_passes']:assert len({x['row'][field] for x in rr})==1,(phase,v,n,b,field)
  values=[int(x['row']['elapsed_ns'])/int(x['row']['operations']) for x in rr]
  effect=100*((values[1]+values[2])/(values[0]+values[3])-1)
  passed=abs(effect)<=1 if phase=='aa' else effect<=-2
  effects.append(dict(variant=v,size=n,block=b,effect_pct=effect,passes=passed))
  if phase=='screen':assert [x['binary'] for x in rr]==['base',v,v,'base']
 assert all(e['passes'] for e in effects)
 result[phase]=dict(rows=len(rows),blocks=len(effects),raw_identity=True,serial=True,semantic_memory_cpu_identity=True,effects=effects)
result['reviewer']='/root/aws_amd';result['reviewed_commit']='c3e5882ca';result['status']='PASS for declared discovery only';result['source_adoption']='NONE';result['limits']=['Original/long-key/focused guards not part of this immutable checkpoint','Fresh confirmation seeds201–203 not run','Matched Intel profile mechanism still required; AMD profile discrepancy remains unresolved']
out=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/010-intel-scan-review');(out/'independent-raw-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:dict(rows=v['rows'],blocks=v['blocks']) for k,v in result.items() if isinstance(v,dict)},indent=2))
