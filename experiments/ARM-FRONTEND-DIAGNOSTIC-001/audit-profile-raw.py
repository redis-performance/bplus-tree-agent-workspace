#!/usr/bin/env python3
"""Independent counter/fixture/instrumentation reconstruction from immutable Git data.

Own-code and physical sample mapping require the separate independent Intel review.
This script imports no producer modules and makes no causal acceptance decision.
"""
import argparse,collections,csv,datetime,decimal,hashlib,io,json,re,subprocess,tarfile
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('revision');p.add_argument('--out',type=Path,required=True);a=p.parse_args()
prefix='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/030-frontend-diagnosis/'
with tarfile.open(fileobj=io.BytesIO(subprocess.check_output(['git','archive',a.revision,prefix]))) as t:files={m.name[len(prefix):]:t.extractfile(m).read() for m in t if m.isfile()}
j=lambda n:json.loads(files[n]);sha=lambda b:hashlib.sha256(b).hexdigest();dt=datetime.datetime.fromisoformat
D=decimal.Decimal;decimal.getcontext().prec=40
f=j('profile-execution-freeze.json');s=j('profile/result.json');audit=j('profile/audit.json');contracts=j('profile-commands.json');ids=j('identities.json');oracle=j('fixture-oracle.json')
assert len(contracts)==len(s['commands'])==642 and s['status']=='complete' and s['cpu']==2
for n,h in f['files'].items():assert sha(files[n])==h,n
assert s['execution_freeze_sha256']==sha(files['profile-execution-freeze.json'])
assert s['lease_scope']==dict(unit_prefix='bplus-frontjob-20261019-',slice='bplus-front-20261019.slice',cpu=2,deadline='2026-10-19T11:45:00+00:00')
assert 0<float(s['elapsed_seconds'])<=1200 and 0<(dt(s['finished_utc'])-dt(s['started_utc'])).total_seconds()<=1200
assert (dt(s['lease_scope']['deadline'])-dt(s['started_utc'])).total_seconds()>=1220 and dt(s['finished_utc'])<dt(s['lease_scope']['deadline'])
assert s['identities_before']==s['identities_after'] and s['sources_before']==s['sources_after'] and s['binaries_before']==s['binaries_after']
assert s['identities_before']['binaries']=={k:v['sha256'] for k,v in ids['binaries'].items()}
assert set(s['identities_before']['sources'])==set(ids['binaries'])
for name,got in s['identities_before']['sources'].items():
 want=dict(ids['source_hashes'])
 if name.endswith('-A'):want['src/zset_btree.c']=ids['candidate_source_sha256']
 if name.startswith('h4-'):want['bench/iterator_modes.c']=sha(files['inputs/iterator_modes.c'])
 assert got==want
assert audit['result_sha256']==sha(files['profile/result.json'])
for n,h in audit['raw_files_sha256'].items():assert sha(files['profile/'+n])==h,n
assert audit['raw_data_sha256']==s['raw_data_sha256'] and len(s['raw_data_sha256'])==38
semantics=['case','size','seed','requested_ops','member_bytes','operations','traversals','checksum','warmup_passes','tree_bytes','direction','mask','encoding','expected_checksum','construction_fingerprint']
refs={};rows={};stat={};census={};instrument=collections.defaultdict(list);last=dt(s['started_utc']);warnings=[]
events={'cycles:u','instructions:u','branches:u','branch-misses:u'}
for r,c in zip(s['commands'],contracts):
 assert all(r[k]==v for k,v in c.items()) and r['returncode']==0 and r['checked']
 assert last<=dt(r['started_utc'])<dt(r['finished_utc'])<=dt(s['finished_utc']) and (dt(r['finished_utc'])-dt(r['started_utc'])).total_seconds()<=120;last=dt(r['finished_utc'])
 text=files['profile/'+c['name']+'.stdout'].decode();err=files['profile/'+c['name']+'.stderr'].decode()
 if re.search(r'\b(lost|warning)\b',err,re.I):warnings.append(c['name'])
 if c['kind']=='original43':assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',text)
 if c['fixture']:
  fixture=c['fixture'];n=fixture['size'];seed=fixture['seed'];traversals=(fixture['requested_ops']+n-1)//n;ops=traversals*n;z=list(csv.DictReader(text.splitlines()));assert len(z)==1;z=z[0];assert z==r['row'];rows[c['name']]=z
  checksum=(oracle[f'{n}/{seed}'][fixture['frontend']+'_one_traversal_checksum']*traversals)&((1<<64)-1)
  expected=dict(size=n,seed=seed,requested_ops=fixture['requested_ops'],member_bytes=16,operations=ops,traversals=traversals,checksum=checksum,warmup_passes=fixture['warmup_passes'],cpu_start=2,cpu_end=2,case='iterate' if fixture['frontend']=='primary' else 'iterator-modes')
  if fixture['frontend']=='h4':expected.update(direction=fixture['direction'],mask=4,encoding='integer',expected_checksum=checksum,construction_fingerprint=oracle[f'{n}/{seed}']['h4_construction_fingerprint'])
  for k,v in expected.items():assert z[k]==str(v),(c['name'],k)
  for k in ['elapsed_ns','thread_elapsed_ns','tree_bytes']:assert int(z[k])>0
  mode='sanitizer' if any(x.startswith('build/') and x.endswith('-san') for x in c['command']) else 'native'
  key=(mode,fixture['frontend'],fixture['direction'],n,seed,fixture['requested_ops']);ref=refs.setdefault(key,z);assert all(z.get(k)==ref.get(k) for k in semantics)
  if c['kind'] in ['instrument','tree']:assert not err.strip()
  if c['kind']=='instrument':instrument[(c['variant'],fixture['id'],c['instrument_phase'],c['instrument_contract']['block'])].append((c,z))
  if c['kind']=='census':
   assert len(err.splitlines())==1 and err.startswith('CENSUS ');obs=json.loads(err[7:]);assert obs==r['census']==census.setdefault(key,obs)
   assert obs['members']==n and obs['tree_bytes']==int(z['tree_bytes'])
   assert sum(obs['width_entry_hist'])==sum(obs['shift_entry_hist'])==n and len(obs['width_entry_hist'])==len(obs['shift_entry_hist'])==65
   assert sum(obs['occupancy_leaf_hist'])==obs['leaves'] and sum(i*v for i,v in enumerate(obs['occupancy_leaf_hist']))==n
   assert all(isinstance(v,int) and v>=0 for k in ['width_entry_hist','shift_entry_hist','occupancy_leaf_hist'] for v in obs[k])
   assert obs['score_digest']==j('census-score-oracle.json')[f'{fixture["frontend"]}/{n}']
 if c['kind'] in ['tree-stat','disabled-stat','known-stat']:
  assert '--no-scale' in c['command'];enabled=c['kind']=='tree-stat' or c['name']=='known-enabled-stat';values={}
  for z in csv.reader(files['profile/'+c['stat_file']].decode().splitlines()):
   if not z or z[0].startswith('#'):continue
   assert len(z)>=3 and z[2] not in values;values[z[2]]=z[0].strip()
   if enabled:
    assert re.fullmatch(r'[0-9]+',values[z[2]]) and len(z)>=5
    assert D(z[3]).is_finite() and D(z[3])>0 and D(z[4]).is_finite() and D(z[4])==100
  assert set(values)==events
  if enabled:assert all(int(values[k])>0 for k in events-{'branch-misses:u'}) and int(values['branch-misses:u'])>=0
  else:assert set(values.values())<={'0','<not counted>'}
  assert values==r['counters']['values'];stat[c['name']]=values
pairs=[]
for cell in j('cells.json'):
 for seed in [1701,1702,1703]:
  per={}
  for variant in ['control','A']:
   name=f'{variant}-{cell["id"]}-s{seed}-stat';per[variant]={e:D(stat[name][e])/D(rows[name]['operations']) for e in events}
  changes={e:(per['A'][e]/per['control'][e]-1)*100 if per['control'][e] else None for e in events}
  old=next(x for x in audit['matched_counter_pairs'] if x['cell']==cell['id'] and x['seed']==seed)
  for e,v in changes.items():assert (v is None and old['change_pct'][e] is None) or (v is not None and v==D(old['change_pct'][e]))
  decreased=per['A']['instructions:u']<per['control']['instructions:u'];assert decreased==old['instructions_decreased']
  pairs.append(dict(cell=cell['id'],seed=seed,instructions_decreased=decreased,change_pct={e:str(v) if v is not None else None for e,v in changes.items()}))
blocks=[]
for (variant,cell,phase,block),zs in sorted(instrument.items()):
 assert len(zs)==4 and [c['instrument_contract']['position'] for c,z in zs]==list(range(4));v=[D(z['elapsed_ns'])/D(z['operations']) for c,z in zs];effect=((v[1]+v[2])/(v[0]+v[3])-1)*100;window=min(int(z['elapsed_ns']) for c,z in zs)
 claimed=next(x for x in audit['instrumentation_qualification'] if x['source']==variant and x['cell']==cell)['phases'][phase]['blocks'][block]
 assert D(claimed['effect_pct'])==effect and claimed['minimum_window_ns']==window
 blocks.append(dict(source=variant,cell=cell,phase=phase,block=block,effect_pct=str(effect),minimum_window_ns=window,qualified=abs(effect)<=1 and window>=10000000))
assert len(blocks)==72 and len(pairs)==18 and len(stat)==42
qualified={}
for variant,cell,_,_ in instrument:
 key=variant+'/'+cell;qualified[key]=all(x['qualified'] for x in blocks if x['source']==variant and x['cell']==cell)
 assert qualified[key]==next(x['elapsed_transfer_qualified'] for x in audit['instrumentation_qualification'] if x['source']==variant and x['cell']==cell)
report=dict(audit_status='PASS',revision=a.revision,reviewed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),commands=642,elapsed_seconds=s['elapsed_seconds'],counter_runs=42,matched_pairs=pairs,instrumentation_blocks=blocks,instrumentation_qualified_cells=qualified,census_groups=len(census),warnings=warnings,source_selection='NONE',prior_candidate_decision='REJECT',scope='Independent contracts, raw rows/counters, fixture/memory/source identities and instrumentation arithmetic. Physical PC/code/scope mapping requires separate independent review; no causal or acceptance claim.',raw_profile_data_files=38,raw_profile_data_note='Checksums joined; large original perf.data retained by operator, not reread from public Git')
a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ['audit_status','commands','counter_runs','instrumentation_qualified_cells']}))
