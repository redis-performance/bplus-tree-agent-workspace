#!/usr/bin/env python3
"""Independent raw histogram reconstruction; no worker profile audit imported."""
import argparse,collections,csv,datetime,hashlib,json,pathlib,re
p=argparse.ArgumentParser();p.add_argument('evidence',type=pathlib.Path);p.add_argument('--original-freeze',required=True,type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args();root=a.evidence;read=lambda n:json.loads((root/n).read_text());sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();clock=datetime.datetime.fromisoformat
inputs=read('inputs.json')
for n,h in inputs['files'].items():assert sha(root/n)==h
for n,k in [('run-profile.py','prepared_driver_sha256'),('PLAN.md','plan_sha256'),('capture-schedule.json','schedule_sha256')]:assert sha(root/n)==inputs[k]
assert inputs['captures']==120 and inputs['repetitions']==10 and inputs['phase_cap_seconds']==600 and not inputs['v1_executed']
schedule=[]
for repeat in range(10):
 for seed in [301,302,303]:
  for n in [100000,1000000]:
   for v in (['base','B'] if (seed+repeat)%2 else ['B','base']):schedule.append(dict(index=len(schedule),repeat=repeat,seed=seed,size=n,variant=v,requested_operations=5000000,member_bytes=16))
assert read('capture-schedule.json')==schedule
processes=read('processes.json');proc={r['tag']:r for r in processes};assert len(proc)==len(processes)
for i,r in enumerate(processes):
 assert r['returncode']==0 and clock(r['started_utc'])<=clock(r['finished_utc'])
 if i:assert clock(processes[i-1]['finished_utc'])<=clock(r['started_utc'])
job=read('matched-profile.sh.job.json');assert job['returncode']==0 and job['cpu']==2 and job['limit_seconds']==600;assert clock(job['started_utc'])<=clock(processes[0]['started_utc']);assert clock(processes[-1]['finished_utc'])<=clock(job['finished_utc'])
complete=read('complete.json');assert complete['status']=='complete' and complete['captures']==120 and complete['elapsed_seconds']<=600
freeze=read('build-freeze.json');original=json.loads(a.original_freeze.read_text())
for name,expected,source in [('post-phase-hashes.json',freeze,root/'build-freeze.json'),('original-post-phase-hashes.json',{v:original[v] for v in ['base','B']},a.original_freeze)]:
 post=read(name);assert post['status']=='pass' and not post['mismatches'];assert post['observed']==expected and post['expected_manifest_sha256']==sha(source);assert clock(post['started_utc'])>=clock(job['finished_utc'])
assert freeze['base']['src/zset_btree.c']==original['base']['src/zset_btree.c'];assert freeze['B']['src/zset_btree.c']==original['B']['src/zset_btree.c']
for f in freeze['base']:
 if not f.startswith('build/') and f!='src/zset_btree.c':assert freeze['base'][f]==freeze['B'][f]
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']
def rawrow(tag):
 rr=list(csv.DictReader((root/'profiles'/(tag+'.stdout')).read_text().splitlines()));assert len(rr)==1;assert rr[0]['cpu_start']==rr[0]['cpu_end']=='2';return rr[0]
def hist(tag):
 rows=list(csv.DictReader((root/'profiles'/(tag+'.hist.csv')).read_text().splitlines()));d={int(r['offset']):int(r['count']) for r in rows};assert len(d)==len(rows);return d
for v in ['base','B']:
 for n in [100,1000,10000]:
  first=rawrow(f'{v}-original-control-{n}');second=rawrow(f'{v}-disabled-control-{n}');assert all(first[k]==second[k] for k in fields);assert not sum(hist(f'{v}-disabled-control-{n}').values())
 first=rawrow(v+'-original-san-control');second=rawrow(v+'-disabled-san-control');assert all(first[k]==second[k] for k in fields);assert not sum(hist(v+'-disabled-san-control').values())
known=hist('known-enabled');assert not sum(hist('known-disabled').values());assert (root/'profiles/known-enabled.stdout').read_bytes()==(root/'profiles/known-disabled.stdout').read_bytes();symbols=[s.split() for s in (root/'profiles/known-enabled-symbols.stdout').read_text().splitlines()];base=int(next(s[0] for s in symbols if s[-1]=='__executable_start'),16);work=next(s for s in symbols if s[-1]=='known_work');low=int(work[0],16)-base;high=low+int(work[1],16);inside=sum(c for o,c in known.items() if low<=o<high);total=sum(known.values());assert total>=20 and inside/total>=.9
maps={}
for v in ['base','B']:
 meta=read(v+'-mapping.json');mapped=read('profiles/'+v+'-inline-map.stdout');maps[v]={int(x['Address'],16)-meta['linker_base']:any(s['FunctionName']=='zbtLeafTagMatches' for s in x['Symbol']) for x in mapped};assert len(maps[v])==meta['bucket_count']
captures=read('captures.json');assert len(captures)==120
assert [r['tag'] for r in processes if re.fullmatch(r'r[0-9]{2}-(?:base|B)-scan-[0-9]+-seed[0-9]+',r['tag'])]==[c['tag'] for c in captures]
for mode in ['original','disabled','profile','original-sanitize','disabled-sanitize']:
 assert proc['base-'+mode+'-build']['command']==proc['B-'+mode+'-build']['command']
 assert '-pg' not in proc['base-'+mode+'-build']['command']
groups=collections.defaultdict(lambda:dict(samples=0,helper_samples=0,actual_callbacks=0,captures=0));rows=[]
for i,(c,s) in enumerate(zip(captures,schedule)):
 for k in ['repeat','seed','size','variant']:assert c[k]==s[k]
 tag=f"r{s['repeat']:02d}-{s['variant']}-scan-{s['size']}-seed{s['seed']}";assert c['tag']==tag;r=rawrow(tag);assert r==c['row'];assert [r['case'],int(r['size']),int(r['seed']),int(r['requested_ops']),int(r['member_bytes'])]==['scan',s['size'],s['seed'],5000000,16]
 assert proc[tag]['command']==['build/profile','--case','scan','--size',str(s['size']),'--ops','5000000','--member-bytes','16','--seed',str(s['seed'])]
 if i%2:assert all(captures[i-1]['row'][k]==r[k] for k in fields)
 d=hist(tag);meta={k:int(v) for k,v in re.findall(r'(\w+)=(\d+)',(root/'profiles'/(tag+'.stderr')).read_text())};assert meta['scale']==65536 and meta['bin_bytes']==2 and meta['interval_ns']==10000000 and meta['disabled']==0;assert meta['cpu_elapsed_ns']//meta['interval_ns']+4<65535;assert sum(d.values())==meta['captured'];assert max(d.values(),default=0)==meta['max_bin']<65535
 assert all(o%2==0 and 0<=o<meta['text_offset_end'] and o in maps[c['variant']] for o in d);helper=sum(count for off,count in d.items() if maps[c['variant']][off]);key=(c['size'],c['variant']);g=groups[key];g['samples']+=sum(d.values());g['helper_samples']+=helper;g['actual_callbacks']+=int(r['operations']);g['captures']+=1;rows.append(dict(index=i,tag=tag,samples=sum(d.values()),helper_samples=helper,actual_callbacks=int(r['operations']),max_bin=meta['max_bin']))
summary=[]
for (size,v),g in sorted(groups.items()):
 assert g['captures']==30;summary.append(dict(size=size,variant=v,**g,helper_per_million_callbacks=g['helper_samples']/g['actual_callbacks']*1e6,helper_share_pct=g['helper_samples']/g['samples']*100))
for n in [100000,1000000]:assert groups[(n,'base')]['actual_callbacks']==groups[(n,'B')]['actual_callbacks']
a.out.write_text(json.dumps({'status':'pass','evidence_commit':'e49b21fe6','capture_count':120,'serial_commands':len(processes),'known_work':{'enabled':total,'inside':inside,'disabled':0},'diagnostic_post_hashes':sum(len(x) for x in freeze.values()),'original_post_hashes':sum(len(original[v]) for v in ['base','B']),'summary':summary,'captures':rows,'source_adoption':'NONE','limits':['Counts are only in-range executable text samples; uncaptured/library/lost events unknown','Same-profile-binary scope, not exact original timing layout or cycles','No new measurements, retries or worker audit-script imports']},indent=2)+'\n');print(json.dumps(summary,indent=2))
