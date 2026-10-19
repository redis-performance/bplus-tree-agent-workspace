from pathlib import Path
import json,csv,statistics,datetime
p=Path('scratch/scan-screen');rs=json.loads((p/'processes.json').read_text());rows=json.loads((p/'rows.json').read_text());s=json.loads((p/'summary.json').read_text())
assert len(rs)==len(rows)==144
assert all(x['returncode']==0 for x in rs)
for i,r in enumerate(rs):
 if i:assert datetime.datetime.fromisoformat(rs[i-1]['end'])<=datetime.datetime.fromisoformat(r['start'])
 raw=list(csv.DictReader((p/(r['label']+'.csv')).read_text().splitlines()));assert len(raw)==1
 x=raw[0];assert x['case']=='scan' and int(x['requested_ops'])==1000000 and int(x['member_bytes'])==16 and int(x['cpu_start'])==int(x['cpu_end'])==2
 assert int(x['seed'])==1+r['block']//2
 q=next(z for z in rows if z['label']==r['label']);assert all(q[k]==v for k,v in x.items())
for v in ['A','B','C']:
 for n in [100000,1000000]:
  effects=[]
  for b in range(6):
   rr=[x for x in rows if x['variant']==v and int(x['size'])==n and x['block']==b];assert len(rr)==4 and ''.join(x['side'] for x in rr)=='ABBA'
   for field in ['checksum','tree_bytes','operations','seed','traversals','warmup_passes']:assert len({x[field] for x in rr})==1,(v,n,b,field)
   a=statistics.mean(float(x['ns_per_op']) for x in rr if x['side']=='A');c=statistics.mean(float(x['ns_per_op']) for x in rr if x['side']=='B');effect=100*(c/a-1);effects.append(effect)
   assert abs(effect-s[v][str(n)]['blocks'][b]['effect_pct'])<1e-9
  assert abs(statistics.median(effects)-s[v][str(n)]['median_pct'])<1e-9
leads=[v for v in ['A','B','C'] if all(s[v][str(n)]['primary_gate_all_blocks'] for n in [100000,1000000])]
o=dict(status='PASS',processes=144,effects=36,conditional_leads=leads,diagnostic_priority=leads[0] if leads else None,decision='PARK/NONE' if leads else 'REJECT/NONE',first=rs[0]['start'],last=rs[-1]['end'],note='Failed1M A/A prevents qualified winner or adoption; fixed alphabetical priority only for mechanism diagnostic.')
(p/'audit.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2));print(json.dumps({v:{n:c['median_pct'] for n,c in z.items()} for v,z in s.items()},indent=2))
