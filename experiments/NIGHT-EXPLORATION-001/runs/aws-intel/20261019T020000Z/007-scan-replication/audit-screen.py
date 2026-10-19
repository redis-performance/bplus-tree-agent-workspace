from pathlib import Path
import csv,datetime,hashlib,json,statistics
p=Path(__file__).parent;m=json.loads((p/'screen.json').read_text());rows=m['rows'];schedule=json.loads((p/'screen-schedule.json').read_text());last=None
freeze=json.loads((p/'screen-freeze.json').read_text())
for f,h in freeze['files'].items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h
assert len(rows)<=len(schedule)==96
for i,r in enumerate(rows):
 assert all(r[k]==v for k,v in schedule[i].items());assert list(csv.DictReader((p/'raw'/f'screen-{i:03d}.stdout').open()))==[r['row']]
 x=r['row'];assert x['cpu_start']==x['cpu_end']=='2';assert x['case']=='scan' and x['requested_ops']=='5000000' and x['member_bytes']=='16' and int(x['size'])==r['size'] and int(x['seed'])==r['seed']
 start=datetime.datetime.fromisoformat(r['started_utc']);end=datetime.datetime.fromisoformat(r['finished_utc']);assert start<=end
 if last is not None:assert last<=start
 last=end
effects=[]
for i in range(0,len(rows)-3,4):
 r=rows[i:i+4];assert len({(x['row']['checksum'],x['row']['operations'],x['row']['tree_bytes']) for x in r})==1
 v=[int(x['row']['elapsed_ns'])/int(x['row']['operations']) for x in r];effect=100*((v[1]+v[2])/(v[0]+v[3])-1);minimum=min(int(x['row']['elapsed_ns']) for x in r)
 effects.append(dict(variant=r[0]['variant'],size=r[0]['size'],seed=r[0]['seed'],block=r[0]['block'],percent=effect,min_window_ns=minimum,passes=effect<=-2 and minimum>=10000000))
summary=[]
for variant in ['A','B']:
 for size in [100000,1000000]:
  group=[x for x in effects if x['size']==size and x['variant']==variant];values=[x['percent'] for x in group]
  if group:summary.append(dict(variant=variant,size=size,blocks=len(group),minimum=min(values),maximum=max(values),median=statistics.median(values),min_window_ns=min(x['min_window_ns'] for x in group),passes=len(group)==6 and all(x['passes'] for x in group),effects=values))
aa=json.loads((p/'aa-audit.json').read_text());controls=all(x['qualified'] for x in aa['summary']);complete=len(rows)==96 and m['status']=='complete';eligible=[v for v in ['A','B'] if complete and controls and all(x['passes'] for x in summary if x['variant']==v)]
selected='B' if 'B' in eligible else ('A' if 'A' in eligible else 'NONE')
result=dict(status='pass',phase_status=m['status'],raw_rows=len(rows),complete_blocks=len(effects),partial_rows=len(rows)%4,serial_windows=True,fixture_identity=True,owned_bytes_equal=True,schedule_prefix_exact=True,controls_qualified=controls,eligible=eligible,followup_source=selected,source_adoption='NONE',summary=summary,effects=effects)
(p/'screen-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='effects'},indent=2))
