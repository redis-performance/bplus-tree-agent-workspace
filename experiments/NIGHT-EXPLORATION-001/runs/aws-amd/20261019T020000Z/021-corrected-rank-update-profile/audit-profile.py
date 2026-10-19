#!/usr/bin/env python3
import argparse,collections,csv,hashlib,json,pathlib,re
p=argparse.ArgumentParser();p.add_argument('results',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args();r=a.results;read=lambda n:json.loads((r/n).read_text());e=json.loads((pathlib.Path(__file__).parent/'expected.json').read_text());c=read('complete.json');b=read('build-freeze.json');processes=read('processes.json');assert c['status']=='complete' and c['elapsed_seconds']<=600 and c['sampled_captures']==12 and c['enabled_counter_captures']==0;assert c['source_hashes_after']==b['source_hashes']==e['source_hashes'];assert c['protected_binaries_before']==c['protected_binaries_after']==e['protected_binaries'];assert b['commit']==e['commit'] and b['scope_sha256']==e['scope_sha256'] and b['cpu_affinity']==[2];assert b['binary_sha256']==c['binary_hashes_after'];assert len(processes)==74
for i,x in enumerate(processes):
 assert x['returncode']==0 and x['started_utc']<=x['finished_utc']
 if i:assert processes[i-1]['finished_utc']<=x['started_utc']
fixtures=[(case,n,seed) for seed in [1,2,3] for n in [100000,1000000] for case in ['rank','update']];schedule=[n+'-build' for n in ['original','profile','original-san','profile-san']]+['original43']
for case,n,seed in fixtures:schedule += [f'{case}-n{n}-s{seed}-'+mode for mode in ['original','disabled']]
for case in ['rank','update']:schedule += [case+'-san-original',case+'-san-disabled']
schedule += ['rank-disabled-zero','update-disabled-zero','original-full-asm','profile-full-asm','timing-full-asm']
for case,n,seed in fixtures:schedule += [f'{case}-n{n}-s{seed}-'+mode for mode in ['record','report','samples']]
assert [x['name'] for x in processes]==schedule
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']
def raw(n):
 rows=list(csv.DictReader((r/(n+'.stdout')).read_text().splitlines()));assert len(rows)==1 and rows[0]['cpu_start']==rows[0]['cpu_end']=='2';return rows[0]
def same(rows):assert all(len({x[k] for x in rows})==1 for k in fields)
for case in ['rank','update']:
 same([raw(case+'-san-original'),raw(case+'-san-disabled')]);same([raw(case+'-disabled-zero'),raw(case+'-n100000-s1-original')]);zero=[]
 for line in (r/(case+'-disabled.stat')).read_text().splitlines():
  if line and not line.startswith('#'):
   row=next(csv.reader([line]));assert row[0].strip() in ['0','<not counted>'];zero.append(row[2])
 assert zero==['cycles:u','instructions:u','branches:u','branch-misses:u']
text=re.sub(r'\x1b\[[0-9;]*m','',(r/'original43.stdout').read_text());assert '43 passed, 0 failed, 43 total' in text
summary={};captures=[]
for case,n,seed in fixtures:
 label=f'{case}-n{n}-s{seed}';rows=[raw(label+'-'+mode) for mode in ['original','disabled','record']];same(rows);assert [rows[0]['case'],int(rows[0]['size']),int(rows[0]['requested_ops']),int(rows[0]['member_bytes']),int(rows[0]['seed']),int(rows[0]['operations'])]==[case,n,5000000,16,seed,5000000];exclusive=collections.Counter();events=collections.Counter();inclusive=collections.Counter();total=0;event_count=0
 for block in re.split(r'\n\s*\n',(r/(label+'-samples.stdout')).read_text().strip()):
  lines=block.splitlines();period=int(lines[0].strip());frames=[re.match(r'\s*([0-9a-f]+)\s+(.*)',line) for line in lines[1:]];frames=[x for x in frames if x];assert frames;top=frames[0][1];name=frames[0][2].split('+')[0];exclusive[name]+=period;events[name]+=1;event_count+=1;total+=period
  for name in {f[2].split('+')[0] for f in frames if f[1]==top}:inclusive[name]+=period
 key=f'{case}/{n}';g=summary.setdefault(key,dict(total_period=0,events=0,operations=0,exclusive_period=collections.Counter(),exclusive_events=collections.Counter(),same_ip_inclusive_period=collections.Counter()));g['total_period']+=total;g['events']+=event_count;g['operations']+=int(rows[0]['operations']);g['exclusive_period'].update(exclusive);g['exclusive_events'].update(events);g['same_ip_inclusive_period'].update(inclusive);captures.append(dict(case=case,size=n,seed=seed,total_period=total,events=event_count,operations=int(rows[0]['operations'])))
for g in summary.values():
 g['exclusive_top']=[dict(symbol=k,period=v,events=g['exclusive_events'][k],period_pct=100*v/g['total_period'],events_per_million_operations=g['exclusive_events'][k]*1000000/g['operations']) for k,v in g['exclusive_period'].most_common(20)]
verified=0
for name,h in c['raw_data_sha256'].items():
 if (r/name).exists():assert hashlib.sha256((r/name).read_bytes()).hexdigest()==h;verified+=1
out=dict(status='pass',commands=74,sampled_captures=12,native_control_pairs=12,sanitizer_pairs=2,disabled_zero_controls=2,raw_perf_hashes_verified=verified,raw_perf_hashes=c['raw_data_sha256'],source_selection='NONE',summary=summary,captures=captures,limits=['Exclusive innermost and same-IP inclusive periods are different; inclusive shares overlap','Unknown/control samples retained; no whole-callchain accumulation','Fixed update history50passes100K/5passes1M; no first-pass attribution transfer','Profile bodies/layout require actual timing-binary mapping before proposal','Sample shares are not exact removable cycles or predicted speedups']);a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:{'events':v['events'],'top':v['exclusive_top'][:6]} for k,v in summary.items()},indent=2))
