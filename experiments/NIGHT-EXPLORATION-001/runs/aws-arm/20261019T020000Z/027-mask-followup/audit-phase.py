#!/usr/bin/env python3
"""Reconstruct every complete phase; preserve qualification and diagnostic distinctions."""
import argparse,csv,datetime,decimal,hashlib,json,pathlib
D=decimal.Decimal;decimal.getcontext().prec=40
p=argparse.ArgumentParser();p.add_argument('--phase',required=True);a=p.parse_args();here=pathlib.Path(__file__).resolve().parent;out=here/a.phase;state=json.loads((out/'result.json').read_text());schedule=json.loads((here/'schedules'/(a.phase+'.json')).read_text());family=a.phase.split('-')[0];aa=a.phase.endswith('AA');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert state['status']=='complete' and len(state['runs'])==len(schedule)
assert state['schedule_sha256']==sha(here/'schedules'/(a.phase+'.json'))
for before,after in [('protected_before','protected_after'),('sources_before','sources_after'),('guard_binaries_before','guard_binaries_after')]:assert state[before]==state[after]
groups={};previous=None
for run,contract in zip(state['runs'],schedule):
 assert all(run[k]==v for k,v in contract.items()) and run['returncode']==0 and run['checked']
 start=datetime.datetime.fromisoformat(run['started_utc']);end=datetime.datetime.fromisoformat(run['finished_utc']);assert start<=end
 if previous is not None:assert previous<=start
 previous=end
 rows=list(csv.DictReader((out/(run['name']+'.csv')).read_text().splitlines()));assert rows==run['rows']
 assert len(rows)==(8 if family=='original' else 1)
 for row in rows:
  assert row['cpu_start']==row['cpu_end']=='2' and int(row['elapsed_ns'])>0
  key=(run['cell']['id'],row['case']);groups.setdefault(key,{}).setdefault(run['block'],[]).append((run,row))
original={(x['size'],x['case']):x for x in json.loads((here/'original-guards.json').read_text())};cells=[]
qualification={}
if not aa:
 q=json.loads((here/(family+'-AA')/'audit.json').read_text());assert q['complete'];qualification={x['id']:x['qualified'] for x in q['cells']}
for (cid,case),blocks in groups.items():
 assert set(blocks)==set(range(6));size=blocks[0][0][0]['cell']['size'];required=original[(size,case)]['required_for_acceptance'] if family=='original' else True;effects=[]
 for block,runs in sorted(blocks.items()):
  assert [r['position'] for r,z in runs]==[0,1,2,3] and [r['label'] for r,z in runs]==['A','B','B','A']
  for field in ['size','seed','member_bytes','requested_ops','operations','checksum','tree_bytes','traversals','warmup_passes']:assert len({z[field] for r,z in runs})==1,(cid,case,field)
  if family=='iterator':
   for field in ['direction','mask','encoding','construction_fingerprint','expected_checksum']:assert len({z[field] for r,z in runs})==1
  ns=[int(z['elapsed_ns']) for r,z in runs];effect=(D(ns[1]+ns[2])/D(ns[0]+ns[3])-1)*100
  effects.append(dict(block=block,seed=runs[0][0]['seed'],effect_pct=str(effect),minimum_window_ns=min(ns)))
 cellid=cid+'/'+case;windows=all(x['minimum_window_ns']>=10000000 for x in effects)
 if aa:qualified=windows and all(abs(D(x['effect_pct']))<=1 for x in effects);decision='QUALIFIED' if qualified else ('PARK' if required else 'UNQUALIFIED_DIAGNOSTIC')
 else:
  qualified=qualification[cellid] and windows
  values=[D(x['effect_pct']) for x in effects]
  if not qualified:decision='PARK' if required else 'UNQUALIFIED_DIAGNOSTIC'
  elif family=='primary':decision='PRIMARY_PASS' if all(v<=-2 for v in values) else 'REJECT'
  elif all(v<=1 for v in values):decision='GUARD_PASS'
  elif all(v>1 for v in values):decision='REJECT'
  else:decision='PARK'
 cells.append(dict(id=cellid,size=size,case=case,required_for_acceptance=required,qualified=qualified,decision=decision,blocks=effects))
allrequired=all(x['qualified'] for x in cells if x['required_for_acceptance']);reject=any(x['decision']=='REJECT' for x in cells);park=any(x['decision']=='PARK' for x in cells)
result=dict(complete=True,phase=a.phase,processes=len(schedule),rows=sum(len(r['rows']) for r in state['runs']),cells=cells,all_required_qualified=allrequired,qualified_cells=sum(x['qualified'] for x in cells),required_cells=sum(x['required_for_acceptance'] for x in cells),all_primary_pass=(not aa and family=='primary' and all(x['decision']=='PRIMARY_PASS' for x in cells)),all_required_guards_pass=(not aa and family!='primary' and all(x['decision']=='GUARD_PASS' for x in cells if x['required_for_acceptance']) and not reject and not park),decision='REJECT' if reject else ('PARK' if park else ('QUALIFIED' if aa else 'PHASE_PASS_NOT_ACCEPTANCE')),source_selection='NONE',raw_sha256={f.name:sha(f) for f in sorted(out.iterdir()) if f.is_file() and f.name!='audit.json'})
(out/'audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['cells','raw_sha256']}))
