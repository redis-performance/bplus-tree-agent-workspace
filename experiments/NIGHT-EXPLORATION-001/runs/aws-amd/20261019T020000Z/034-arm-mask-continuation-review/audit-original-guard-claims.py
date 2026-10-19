import json,pathlib,csv,decimal,hashlib,collections,statistics,sys
p=pathlib.Path(sys.argv[1]);D=decimal.Decimal;decimal.getcontext().prec=40;j=lambda n:json.loads((p/n).read_text());sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest();inventory={(x['size'],x['case']):x for x in j('original-guards.json')};evidence={};rows=0
for phase in ['original-AA','original-comparison']:
 r=j(phase+'/result.json');pub=j(phase+'/PUBLICATION.json');assert r['status']=='complete' and len(r['runs'])==120
 for n,h in pub.items():assert sha(p/phase/n)==h['public_sha256']
 groups={}
 for x in r['runs']:
  z=list(csv.DictReader((p/phase/(x['name']+'.csv')).read_text().splitlines()));assert len(z)==8 and z==x['rows'] and x['returncode']==0
  for v in z:groups.setdefault((int(v['size']),v['case'],x['block']),[]).append((x,v));rows+=1
 assert len(groups)==240;cells={}
 for (size,case,block),runs in groups.items():
  assert [x['position'] for x,z in runs]==[0,1,2,3] and [x['label'] for x,z in runs]==['A','B','B','A']
  for k in ['size','seed','member_bytes','requested_ops','operations','checksum','tree_bytes','traversals','warmup_passes']:assert len({z[k] for x,z in runs})==1
  if phase=='original-comparison':
   for (_,old),(_,new) in zip(evidence['original-AA']['groups'][(size,case,block)],runs):
    for k in ['size','seed','member_bytes','requested_ops','operations','checksum','tree_bytes','traversals','warmup_passes']:assert old[k]==new[k]
  ns=[int(z['elapsed_ns']) for x,z in runs];effect=(D(ns[1]+ns[2])/D(ns[0]+ns[3])-1)*100;cells.setdefault((size,case),[]).append(dict(block=block,seed=int(runs[0][1]['seed']),effect_pct=str(effect),min_ns=min(ns)))
 evidence[phase]={'groups':groups,'cells':cells,'seconds':r['elapsed_seconds']}
summary=[]
for key,blocks in evidence['original-AA']['cells'].items():
 required=inventory[key]['required_for_acceptance'];short=any(x['min_ns']<10000000 for x in blocks);noisy=any(abs(D(x['effect_pct']))>1 for x in blocks);qualified=not(short or noisy);cb=evidence['original-comparison']['cells'][key];values=[D(x['effect_pct']) for x in cb];cshort=any(x['min_ns']<10000000 for x in cb)
 verdict=('PARK' if required else 'UNQUALIFIED_DIAGNOSTIC') if not qualified or cshort else ('GUARD_PASS' if all(x<=1 for x in values) else ('REJECT' if all(x>1 for x in values) else 'PARK'))
 summary.append(dict(size=key[0],case=key[1],required=required,qualified=qualified,short=short,noisy=noisy,decision=verdict,comparison_blocks=cb,median=str(statistics.median(values))))
counts=collections.Counter((x['required'],x['qualified'],x['decision']) for x in summary)
assert sum(x['required'] for x in summary)==29 and sum(x['qualified'] for x in summary)==18
assert sum(x['required'] and not x['qualified'] for x in summary)==11
assert all(not x['short'] for x in summary if x['required']) and all(x['short'] for x in summary if not x['required'])
assert sum(x['noisy'] for x in summary if not x['required'])==8
assert sum(x['decision']=='GUARD_PASS' for x in summary)==17 and not any(x['decision']=='REJECT' for x in summary)
scan=next(x for x in summary if x['size']==100 and x['case']=='scan');assert scan['qualified'] and scan['decision']=='PARK';assert sum(D(x['effect_pct'])>1 for x in scan['comparison_blocks'])==1
print(json.dumps(dict(status='CLAIM_RECONSTRUCTION_PASS',phases=2,processes=240,raw_rows=rows,blocks=480,cells=40,required=29,qualified=18,qualified_passes=17,qualified_mixed=1,required_noisy=11,diagnostics_short=11,diagnostics_also_noisy=8,qualified_all_six_regressions=0,scan=scan,elapsed_seconds={k:v['seconds'] for k,v in evidence.items()},source_selection='NONE',interpretation='PARK remains binding; median does not rescue mixed block and unqualified comparisons are not qualified passes'),indent=2))
