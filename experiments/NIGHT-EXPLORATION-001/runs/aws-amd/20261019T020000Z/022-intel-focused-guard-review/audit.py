#!/usr/bin/env python3
"""Independent reconstruction; does not import or read Intel audit-timing.py."""
import argparse,collections,datetime,hashlib,itertools,json,math,pathlib,statistics
p=argparse.ArgumentParser();p.add_argument('evidence',type=pathlib.Path);p.add_argument('--fixtures',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args();root=a.evidence;load=lambda n:json.loads((root/n).read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();cells=list(itertools.product([4096,100000],[16,321],range(3),range(3)));key=lambda r:tuple(r[k] for k in ['n','bytes','order','distribution']);freeze=load('timing-freeze.json');build=load('build-freeze.json')
for name,h in freeze['files'].items():assert sha(root/name)==h,name
assert freeze['floor_ns']==100000000 and freeze['phase_budgets_seconds']=={'aa':900,'b':900};assert build['base']['src/zset_btree.c']=='d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2';assert build['B']['src/zset_btree.c']=='204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23';assert build['base']['compat/standalone.c']==build['B']['compat/standalone.c']=='adf0f87cd7cd7bc043eeb1743b47f90e4484459c090024ffa837cfd34d9b3d63'
manifest=load('fixture-manifest.json');assert len(manifest)==36 and len({f['name'] for f in manifest})==36;verified_fixtures=0
if a.fixtures:
 for f in manifest:
  path=a.fixtures/(f['name']+'.bin');assert path.stat().st_size==f['bytes'] and sha(path)==f['sha256'];verified_fixtures+=1
counts={key(r):r for r in load('pass-counts.json')};assert set(counts)==set(cells)
cal_schedule=[]
for n,b,o,d in cells:
 for seed in [101,102,103]:
  for rep in range(3):cal_schedule.append(dict(index=len(cal_schedule),n=n,bytes=b,order=o,distribution=d,seed=seed,repeat=rep,binary='base',passes=1))
assert load('calibration-schedule.json')==cal_schedule
schedules={'calibration':cal_schedule}
for phase in ['aa','b']:
 schedule=[]
 for block in range(6):
  for n,b,o,d in (cells if block%2==0 else cells[::-1]):
   for pos in range(4):schedule.append(dict(n=n,bytes=b,order=o,distribution=d,passes=counts[(n,b,o,d)]['passes'],index=len(schedule),block=block,seed=101+block%3,position=pos,binary=('B' if phase=='b' and pos in [1,2] else 'base')))
 assert load(phase+'-schedule.json')==schedule;schedules[phase]=schedule
semantic=['kind','n','bytes','seed','distribution','order','passes','logical_members','callbacks_per_pass','checksum_per_pass','tree_bytes','validation'];phases={};post_hashes={}
for phase in ['calibration','aa','b']:
 if not (root/(phase+'.json')).exists():continue
 x=load(phase+'.json');cap=300 if phase=='calibration' else 900;assert x['status']=='complete' and x['phase']==phase and x['phase_cap_seconds']==cap and x['elapsed_seconds']<=cap;assert len(x['rows'])==len(schedules[phase]);assert freeze['frozen_utc']<x['started_utc'] if phase!='calibration' else x['finished_utc']<freeze['frozen_utc'];job=load('focused-'+phase+'.sh.job.json');assert job['cpu']==2 and job['limit_seconds']==cap and job['returncode']==0 and job['started_utc']<=x['started_utc']<=x['finished_utc']<=job['finished_utc'];group=collections.defaultdict(list)
 for i,(r,spec) in enumerate(zip(x['rows'],schedules[phase])):
  assert {k:r[k] for k in spec}==spec
  if i:assert x['rows'][i-1]['finished_utc']<=r['started_utc']
  assert r['started_utc']<=r['finished_utc'];tag=f'{phase}-{i:04d}';row=load('raw/'+tag+'.stdout');assert row==r['row'];assert not (root/'raw'/(tag+'.stderr')).read_text();assert row['start_cpu']==row['end_cpu']==2 and row['validation']=='pass' and row['kind']=='run';assert all(row[k]==spec[k] for k in ['n','bytes','order','distribution','seed','passes']);assert row['logical_members']==row['n']*row['passes'];cmd=r['command'];assert cmd[0]=='scratch/intel-focused-scan/'+spec['binary']+'/build/focused/scan-guard' and cmd[1]=='run' and cmd[2].endswith('/fixtures/'+f's{spec["seed"]}-n{spec["n"]}-b{spec["bytes"]}-d{spec["distribution"]}.bin') and cmd[3:]==[str(spec['order']),str(spec['passes']),'0'];group[key(spec)].append(r)
 post=load('post-'+phase+'-hashes.json');assert post['status']=='pass' and not post['mismatches'] and post['read_only'] and post['no_workload_executed'];assert post['observed']==build and post['expected_manifest_sha256']==sha(root/'build-freeze.json');assert x['finished_utc']<=post['started_utc']<=post['finished_utc'];post_hashes[phase]=sum(len(v) for v in post['observed'].values());phases[phase]={'raw':x,'groups':group}
assert 'calibration' in phases and 'aa' in phases
for cell,rr in phases['calibration']['groups'].items():
 assert len(rr)==9;minimum=min(r['row']['elapsed_ns'] for r in rr);count=counts[cell];assert count['minimum_elapsed_ns']==minimum;assert count['passes']==max(1,min(100000,math.ceil(200000000/minimum)));assert count['cap_sufficient']==(count['passes']*minimum>=200000000)
outputs={}
for phase in ['aa','b']:
 if phase not in phases:continue
 effects=[];percell={}
 for cell,rr in phases[phase]['groups'].items():
  assert len(rr)==24;blocks=[]
  for block in range(6):
   selected=[r for r in rr if r['block']==block];assert len(selected)==4 and [r['position'] for r in selected]==[0,1,2,3];rows=[r['row'] for r in selected];assert all(len({r[k] for r in rows})==1 for k in semantic)
   if phase=='b':
    for r in selected:
     aa=phases['aa']['raw']['rows'][r['index']]['row'];assert all(r['row'][k]==aa[k] for k in semantic)
   vals=[r['elapsed_ns'] for r in rows];effect=100*((vals[1]+vals[2])/(vals[0]+vals[3])-1);minimum=min(vals);entry=dict(cell=list(cell),block=block,seed=101+block%3,effect_pct=effect,min_window_ns=minimum);effects.append(entry);blocks.append(entry)
  k='/'.join(map(str,cell));minimum=min(e['min_window_ns'] for e in blocks);qualified=all(abs(e['effect_pct'])<=1 for e in blocks) and minimum>=100000000
  if phase=='aa':verdict='qualified' if qualified else ('short' if minimum<100000000 else 'noisy')
  else:
   aq=outputs['aa']['cells'][k]['verdict']=='qualified';regress=sum(e['effect_pct']>1 for e in blocks)
   verdict='unqualified-control' if not aq else ('short-candidate' if minimum<100000000 else ('pass' if regress==0 else ('demonstrated-regression' if regress==6 else 'mixed-PARK')))
  percell[k]=dict(verdict=verdict,min_window_ns=minimum,effects_pct=[e['effect_pct'] for e in blocks],median_pct=statistics.median(e['effect_pct'] for e in blocks),all_six_above_one=all(e['effect_pct']>1 for e in blocks))
 outputs[phase]={'processes':len(phases[phase]['raw']['rows']),'blocks':len(effects),'counts':dict(collections.Counter(r['verdict'] for r in percell.values())),'effects':effects,'cells':percell}
result={'status':'pass','calibration_processes':324,'fixture_bytes_independently_rehashed':verified_fixtures,'source_identity':'8fab original adapter; distinct from corrected13e','build_manifest_sha256':sha(root/'build-freeze.json'),'timing_freeze_sha256':sha(root/'timing-freeze.json'),'postphase_artifact_hash_counts':post_hashes,'phases':outputs,'source_selection':'NONE','limits':['Completed driver enforces returncode zero; per-process returncode is not separately retained in each row','Focused callback/referee differs from original scan; no cross-referee speed inference','Sparse reversed fixtures, no active resize/wide IDs and limited key lengths remain coverage gaps','No acceptance conclusion from noisy/unqualified cells']};a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({phase:x['counts'] for phase,x in outputs.items()},indent=2))
