#!/usr/bin/env python3
"""Reconstruct every fresh corrected-adapter A/A block without exclusions."""
import argparse,csv,datetime,hashlib,json,pathlib,collections,statistics
p=argparse.ArgumentParser();p.add_argument('results',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args();expected=json.loads((pathlib.Path(__file__).parent/'expected.json').read_text());x=json.loads((a.results/'result.json').read_text());assert x['status']=='complete' and len(x['runs'])==48 and x['elapsed_seconds']<=300;assert x['source_hashes_before']==x['source_hashes_after']==expected['source_hashes'];assert x['binary_sha256_before']==x['binary_sha256_after']==expected['aa_binary_sha256'];assert x['execution_freeze_sha256']==hashlib.sha256((pathlib.Path(__file__).parent/'execution-freeze.json').read_bytes()).hexdigest()
for name,relative in [('profile_audit_sha256','profile/audit.json'),('profile_mapping_sha256','profile/code-map.json')]:assert x[name]==hashlib.sha256((pathlib.Path(__file__).parent/relative).read_bytes()).hexdigest()
groups=collections.defaultdict(list);schedule=[]
for b in range(6):
 for n in ([100000,1000000] if b%2==0 else [1000000,100000]):
  for pos,letter in enumerate('ABBA'):schedule.append((b,n,701+b%3,pos,letter))
for i,(r,s) in enumerate(zip(x['runs'],schedule)):
 assert tuple(r[k] for k in ['block','size','seed','position','label'])==s;assert r['returncode']==0
 if i:assert datetime.datetime.fromisoformat(x['runs'][i-1]['finished_utc'])<=datetime.datetime.fromisoformat(r['started_utc'])
 assert datetime.datetime.fromisoformat(r['started_utc'])<=datetime.datetime.fromisoformat(r['finished_utc']);assert not (a.results/(r['name']+'.stderr')).read_text();rows=list(csv.DictReader((a.results/(r['name']+'.csv')).read_text().splitlines()));assert rows==[r['row']];row=r['row'];assert int(row['elapsed_ns'])>0;assert row['cpu_start']==row['cpu_end']=='2';assert [row['case'],int(row['size']),int(row['seed']),int(row['requested_ops']),int(row['member_bytes'])]==['iterate',r['size'],r['seed'],50000000,16];assert int(row['operations'])==50000000 and int(row['traversals'])==50000000//r['size']
 assert int(row['checksum'])==(r['size']*(r['size']-1)//2)*(50000000//r['size']) and int(row['warmup_passes'])==1
 assert r['command']==['<corrected-baseline>/build/adapter-requalification/btree-bench','--case','iterate','--size',str(r['size']),'--ops','50000000','--member-bytes','16','--seed',str(r['seed'])]
 groups[(r['size'],r['block'])].append(row)
effects=[]
for (n,b),rr in sorted(groups.items()):
 assert len(rr)==4
 for k in ['operations','checksum','tree_bytes','traversals','warmup_passes']:assert len({r[k] for r in rr})==1
 vals=[int(r['elapsed_ns'])/int(r['operations']) for r in rr];effect=100*((vals[1]+vals[2])/(vals[0]+vals[3])-1);window=min(int(r['elapsed_ns']) for r in rr);effects.append(dict(size=n,block=b,seed=701+b%3,effect_pct=effect,min_window_ns=window,qualified=abs(effect)<=1 and window>=10000000))
summary={str(n):{'qualified':all(e['qualified'] for e in effects if e['size']==n),'max_abs_pct':max(abs(e['effect_pct']) for e in effects if e['size']==n),'minimum_window_ns':min(e['min_window_ns'] for e in effects if e['size']==n)} for n in [100000,1000000]};result={'status':'audited','processes':48,'blocks':12,'both_sizes_qualified':all(s['qualified'] for s in summary.values()),'summary':summary,'effects':effects,'binary_sha256':expected['aa_binary_sha256'],'source_commit':expected['commit'],'source_selection':'NONE','candidate_measurements':0,'raw_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(a.results.iterdir()) if p.is_file() and (p.suffix in ['.csv','.stderr'] or p.name=='result.json')}};a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'both_sizes_qualified':result['both_sizes_qualified'],'summary':summary},indent=2))
