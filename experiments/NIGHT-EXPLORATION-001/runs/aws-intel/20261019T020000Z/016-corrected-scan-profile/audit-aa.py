from pathlib import Path
import json,csv,datetime,statistics
p=Path(__file__).parent;m=json.loads((p/'aa.json').read_text());schedule=json.loads((p/'aa-schedule.json').read_text());assert m['status']=='complete' and len(m['rows'])==len(schedule)==48 and m['elapsed_seconds']<300;last=None
for i,(x,spec) in enumerate(zip(m['rows'],schedule)):
 assert x['index']==i and all(x[k]==v for k,v in spec.items()) and x['returncode']==0;assert list(csv.DictReader((p/'aa-raw'/f'{i:03d}.stdout').open()))==[x['row']];r=x['row'];assert r['cpu_start']==r['cpu_end']=='2' and r['requested_ops']=='5000000' and r['member_bytes']=='16' and r['case']=='scan' and int(r['size'])==spec['size'] and int(r['seed'])==spec['seed'];a=datetime.datetime.fromisoformat(x['started_utc']);b=datetime.datetime.fromisoformat(x['finished_utc']);assert a<=b and (last is None or last<=a);last=b
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes'];effects=[]
for i in range(0,48,4):
 g=m['rows'][i:i+4];assert len({tuple(x['row'][k] for k in fields) for x in g})==1;v=[int(x['row']['elapsed_ns'])/int(x['row']['operations']) for x in g];effects.append(dict(size=g[0]['size'],block=g[0]['block'],seed=g[0]['seed'],percent=100*((v[1]+v[2])/(v[0]+v[3])-1),minimum_window_ns=min(int(x['row']['elapsed_ns']) for x in g)))
summary=[]
for n in [100000,1000000]:
 g=[x for x in effects if x['size']==n];assert len(g)==6;summary.append(dict(size=n,effects=[x['percent'] for x in g],qualified=all(abs(x['percent'])<=1 and x['minimum_window_ns']>=10000000 for x in g),minimum_window_ns=min(x['minimum_window_ns'] for x in g)))
for tag in ['aa-before','aa-after']:assert json.loads((p/(tag+'.json')).read_text())['status']=='pass'
assert json.loads((p/'aa-before.json').read_text())==json.loads((p/'aa-after.json').read_text());result=dict(status='pass',rows=48,blocks=12,qualified_sizes=sum(x['qualified'] for x in summary),summary=summary,effects=effects,elapsed_seconds=m['elapsed_seconds'],source_adoption='NONE',new_population=False);(p/'aa-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
