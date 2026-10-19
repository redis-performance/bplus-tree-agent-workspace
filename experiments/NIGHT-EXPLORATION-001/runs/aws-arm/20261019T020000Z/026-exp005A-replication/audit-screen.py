#!/usr/bin/env python3
import pathlib,json,hashlib,csv,datetime,collections
here=pathlib.Path(__file__).resolve().parent;out=here/'screen';x=json.loads((out/'result.json').read_text());schedule=json.loads((here/'screen-schedule.json').read_text());assert x['status']=='complete' and len(x['runs'])==len(schedule)==48 and x['elapsed_seconds']<=300
assert x['binary_before']==x['binary_after'] and x['sources_before']==x['sources_after'];groups=collections.defaultdict(list)
for i,(r,e) in enumerate(zip(x['runs'],schedule)):
 assert all(r[k]==v for k,v in e.items());assert r['returncode']==0 and not (out/(r['name']+'.stderr')).read_text();assert list(csv.DictReader((out/(r['name']+'.csv')).read_text().splitlines()))==[r['row']]
 assert datetime.datetime.fromisoformat(r['started_utc'])<=datetime.datetime.fromisoformat(r['finished_utc'])
 if i:assert datetime.datetime.fromisoformat(x['runs'][i-1]['finished_utc'])<=datetime.datetime.fromisoformat(r['started_utc'])
 z=r['row'];n=e['size'];values=dict(case='iterate',size=n,seed=e['seed'],requested_ops=50000000,member_bytes=16,operations=50000000,traversals=50000000//n,checksum=50000000*(n-1)//2,warmup_passes=1,cpu_start=2,cpu_end=2);assert all(z[k]==str(v) for k,v in values.items());groups[(n,e['block'])].append(z)
effects=[]
for (n,b),rows in sorted(groups.items()):
 assert len(rows)==4
 for field in ['tree_bytes','checksum','operations','traversals','warmup_passes']:assert len({z[field] for z in rows})==1
 ns=[int(z['elapsed_ns']) for z in rows];pct=100*((ns[1]+ns[2])/(ns[0]+ns[3])-1);effects.append(dict(size=n,block=b,effect_pct=pct,minimum_window_ns=min(ns),primary_pass=pct<=-2 and min(ns)>=10000000))
survives=all(e['primary_pass'] for e in effects);result=dict(status='audited',rows=48,blocks=12,effects=effects,all_primary_blocks_pass=survives,decision='PARK' if survives else 'REJECT',source_selection='NONE',scope='Explicit historical EXP005 A architecture replication; no new implementation population; no broad guards/confirmation/profile acceptance.',evidence_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.is_file()});(out/'audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'decision':result['decision'],'effects':effects},indent=2))
