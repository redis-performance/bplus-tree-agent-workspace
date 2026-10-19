#!/usr/bin/env python3
import argparse,collections,csv,datetime,hashlib,json,pathlib,re
from profile_helpers import samples,report,known_gate
p=argparse.ArgumentParser();p.add_argument('results',type=pathlib.Path);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args();r=a.results;here=pathlib.Path(__file__).parent
read=lambda n:json.loads((r/n).read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
e=json.loads((here/'expected.json').read_text());c=read('complete.json');b=read('build-freeze.json');records=read('processes.json')
assert c['status']=='complete' and c['elapsed_seconds']<=600 and c['sampled_captures']==6 and c['enabled_tree_counter_captures']==0 and c['known_sample_captures']==c['known_counter_captures']==1
assert c['execution_freeze_sha256']==sha(here/'execution-freeze.json')
for name,h in json.loads((here/'execution-freeze.json').read_text())['files'].items():assert sha(here/name)==h
assert c['source_hashes_after']==b['source_hashes']==e['source_hashes'];assert c['protected_binaries_before']==c['protected_binaries_after']==e['protected_binaries'];assert b['commit']==e['commit'] and b['scope_sha256']==e['scope_sha256'] and b['cpu_affinity']==[2]
assert b['known_source_sha256']==sha(here/'known-control.c') and b['binary_sha256']==c['binary_hashes_after'] and 'clang version 18.1.3' in b['compiler']
fixtures=[(n,seed) for seed in [1,2,3] for n in [100000,1000000]]
sequence=['source-archive','compiler-version']+[n+'-build' for n in ['original','profile','original-san','profile-san']]+['known-control-build','original43']
for n,seed in fixtures:sequence += [f'iterate-n{n}-s{seed}-'+mode for mode in ['original','disabled']]
sequence+=['iterate-san-original','iterate-san-disabled','iterate-disabled-zero','known-plain','known-disabled-stat','known-enabled-stat','known-record','known-report','known-samples','known-full-asm','original-full-asm','profile-full-asm','timing-full-asm']
for n,seed in fixtures:sequence += [f'iterate-n{n}-s{seed}-'+mode for mode in ['record','report','samples']]
assert len(sequence)==51 and [x['name'] for x in records]==sequence
contracts=json.loads((here/'commands.json').read_text());assert len(contracts)==51
for i,x in enumerate(records):
 assert {k:x[k] for k in ['name','command','cwd','profile_env']}==contracts[i]
 assert x['returncode']==0 and datetime.datetime.fromisoformat(x['started_utc'])<=datetime.datetime.fromisoformat(x['finished_utc'])
 if i:assert datetime.datetime.fromisoformat(records[i-1]['finished_utc'])<=datetime.datetime.fromisoformat(x['started_utc'])
 assert (r/(x['name']+'.stdout')).exists() and (r/(x['name']+'.stderr')).exists()
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']
def row(name):
 x=list(csv.DictReader((r/(name+'.stdout')).read_text().splitlines()));assert len(x)==1 and x[0]['cpu_start']==x[0]['cpu_end']=='2';return x[0]
def same(rows):assert all(len({x[k] for x in rows})==1 for k in fields)
def contract(z,n,ops,seed):
 traversals=1+(ops-1)//n
 assert [z['case'],int(z['size']),int(z['requested_ops']),int(z['member_bytes']),int(z['seed']),int(z['operations']),int(z['traversals']),int(z['checksum']),int(z['warmup_passes'])]==['iterate',n,ops,16,seed,traversals*n,traversals,(n*(n-1)//2)*traversals,1]
same([row('iterate-san-original'),row('iterate-san-disabled')]);contract(row('iterate-san-original'),1000,2001,101)
same([row('iterate-disabled-zero'),row('iterate-n100000-s1-original')])
known_expected=json.loads((here/'known-control-expectations.json').read_text())['expected_stdout']
for name in ['known-plain','known-disabled-stat','known-enabled-stat','known-record']:assert read(name+'.stdout')==known_expected
for name,enabled in [('iterate-disabled',False),('known-disabled',False),('known-enabled',True)]:
 counts={}
 for line in (r/(name+'.stat')).read_text().splitlines():
  if line and not line.startswith('#'):
   rr=next(csv.reader([line]));counts[rr[2]]=rr[0].strip()
 assert set(counts)=={'cycles:u','instructions:u','branches:u','branch-misses:u'}
 if not enabled:assert all(v in ['0','<not counted>'] for v in counts.values())
 else:assert all(float(counts[k])>0 for k in ['cycles:u','instructions:u','branches:u']) and float(counts['branch-misses:u'])>=0
text=re.sub(r'\x1b\[[0-9;]*m','',(r/'original43.stdout').read_text());assert '43 passed, 0 failed, 43 total' in text
known=known_gate(r,here);summary={};captures=[]
for n,seed in fixtures:
 label=f'iterate-n{n}-s{seed}';rows=[row(label+'-'+mode) for mode in ['original','disabled','record']];same(rows);contract(rows[0],n,50000000,seed)
 parsed=samples(r/(label+'-samples.stdout'));loss=report(r/(label+'-report.stdout'),parsed);assert loss['raw_events']>0 and loss['raw_period']>0
 exclusive=collections.Counter();events=collections.Counter();inclusive=collections.Counter()
 for sample in parsed:
  exclusive[sample['exclusive']]+=sample['period'];events[sample['exclusive']]+=1
  for symbol in sample['same_ip_inclusive']:inclusive[symbol]+=sample['period']
 g=summary.setdefault(str(n),dict(events=0,total_period=0,operations=0,lost=0,exclusive_period=collections.Counter(),exclusive_events=collections.Counter(),same_ip_inclusive_period=collections.Counter()))
 g['events']+=loss['raw_events'];g['total_period']+=loss['raw_period'];g['operations']+=50000000;g['lost']+=loss['lost'];g['exclusive_period'].update(exclusive);g['exclusive_events'].update(events);g['same_ip_inclusive_period'].update(inclusive)
 captures.append(dict(size=n,seed=seed,operations=50000000,**loss))
for g in summary.values():
 g['exclusive_top']=[dict(symbol=k,period=v,events=g['exclusive_events'][k],period_pct=100*v/g['total_period'],events_per_million_operations=g['exclusive_events'][k]*1000000/g['operations']) for k,v in g['exclusive_period'].most_common(25)]
 assert sum(g['exclusive_period'].values())==g['total_period'] and sum(g['exclusive_events'].values())==g['events']
verified=0
for name,h in c['raw_data_sha256'].items():
 if (r/name).exists():assert sha(r/name)==h;verified+=1
assert len(c['raw_data_sha256'])==7
result=dict(status='pass',commands=51,tree_sample_captures=6,known_control=known,native_pairs=6,sanitizer_pairs=1,tree_disabled_zero_controls=1,raw_data_hashes=c['raw_data_sha256'],raw_data_hashes_verified=verified,summary=summary,captures=captures,source_selection='NONE',limits=['Unknown/control samples retained in denominator','Same-IP inline-inclusive shares overlap; exclusive attribution reported separately','No ancestor accumulation or elapsed speed claim','Mapping to actual timing binary required before any hypothesis','Known-work control excluded from tree totals; sample loss reported, not silently corrected'])
a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({n:g['exclusive_top'][:8] for n,g in summary.items()},indent=2))
