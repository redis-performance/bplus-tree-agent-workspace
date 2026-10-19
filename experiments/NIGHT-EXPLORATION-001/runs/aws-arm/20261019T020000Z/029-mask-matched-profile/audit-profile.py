#!/usr/bin/env python3
"""Reconstruct fixed matched captures, semantic contracts, scoped counters and losses."""
import argparse,collections,csv,datetime,decimal,hashlib,json,pathlib,re
from profile_helpers import samples,report,known_gate
p=argparse.ArgumentParser();p.add_argument('results',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args();out=a.results;here=pathlib.Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();D=decimal.Decimal
s=json.loads((out/'result.json').read_text());e=json.loads((here/'expected.json').read_text());contracts=json.loads((here/'commands.json').read_text());freeze=json.loads((here/'execution-freeze.json').read_text());fixtures=json.loads((here/'fixtures.json').read_text())
assert s['status']=='complete' and s['cpu']==2 and 0<s['elapsed_seconds']<=600 and len(s['commands'])==len(contracts)==104
for n,h in freeze['files'].items():assert sha(here/n)==h
assert s['execution_freeze_sha256']==sha(here/'execution-freeze.json');assert s['protected_before']==s['protected_after']==e['protected_binaries']
assert s['actual_sources_before']==s['actual_sources_after']
assert s['sources_before']==s['sources_after'] and s['binaries_before']==s['binaries_after']
for v in ['control','A']:
 expected=dict(e['source_hashes']);expected['bench/profile-scoped-fifo2.c']=e['scope_sha256'];expected['bench/known-control.c']=sha(here/'known-control.c')
 if v=='A':expected['src/zset_btree.c']=e['candidate_source_sha256']
 assert s['sources_before'][v]==expected
 actual_expected={n:expected[n] for n in e['source_hashes']};assert s['actual_sources_before'][v]==actual_expected
start=datetime.datetime.fromisoformat(s['started_utc']);end=datetime.datetime.fromisoformat(s['finished_utc']);deadline=datetime.datetime(2026,10,19,10,15,tzinfo=datetime.timezone.utc)
assert 0<=(end-start).total_seconds()<=600 and end<=deadline and (deadline-start).total_seconds()>=600
previous=start;semantic={};counter_rows={};warnings=[]
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']
def counters(path,enabled):
 parsed={}
 for line in path.read_text().splitlines():
  if not line or line.startswith('#'):continue
  row=next(csv.reader([line]));assert row[2] not in parsed;parsed[row[2]]=row
 assert set(parsed)=={'cycles:u','instructions:u','branches:u','branch-misses:u'}
 for event,row in parsed.items():
  if enabled:assert D(row[0])>=(0 if event=='branch-misses:u' else 1) and D(row[4])==100
  else:assert row[0].strip() in ['0','<not counted>']
 return {k:v[0].strip() for k,v in parsed.items()}
for r,c in zip(s['commands'],contracts):
 assert {k:r[k] for k in c}==c and r['returncode']==0
 st=datetime.datetime.fromisoformat(r['started_utc']);en=datetime.datetime.fromisoformat(r['finished_utc']);assert previous<=st<=en<=end and (en-st).total_seconds()<=120;previous=en
 stdout=(out/(r['name']+'.stdout')).read_text();stderr=(out/(r['name']+'.stderr')).read_text()
 if stderr.strip():warnings.append(dict(command=r['name'],stderr=stderr))
 if r['kind']=='compiler':assert 'clang version 18.1.3' in stdout and 'aarch64' in stdout
 if r['kind']=='original43':assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',stdout)
 if r['kind'].startswith('tree'):
  z=list(csv.DictReader(stdout.splitlines()));assert len(z)==1;z=z[0];f=r['fixture'];n=f['size'];traversals=(f['requested_ops']+n-1)//n
  expected=dict(f,operations=traversals*n,traversals=traversals,checksum=traversals*n*(n-1)//2,warmup_passes=1,cpu_start=2,cpu_end=2)
  for k,v in expected.items():assert z[k]==str(v),(r['name'],k)
  assert int(z['tree_bytes'])>0 and int(z['elapsed_ns'])>0;key=(n,f['seed'],f['requested_ops']);ref=semantic.setdefault(key,z);assert all(ref[k]==z[k] for k in fields)
  if r['kind'] in ['tree-stat','tree-disabled-stat']:
   name=r['name'][:-5] if r['kind']=='tree-stat' else r['variant']+'-disabled';values=counters(out/(name+'.stat'),r['kind']=='tree-stat')
   if r['kind']=='tree-stat':counter_rows[(r['variant'],n,f['seed'])]=values
 if r['kind'] in ['known','known-stat']:assert json.loads(stdout)==json.loads((here/'known-control-expectations.json').read_text())['expected_stdout']
 if r['kind']=='known-stat':counters(out/(r['name'][:-5]+'.stat'),r['name']=='known-enabled-stat')
known=known_gate(out,here);captures=[];groups={}
for f in fixtures:
 for v in ['control','A']:
  label=f'{v}-iterate-n{f["size"]}-s{f["seed"]}';parsed=samples(out/(label+'-samples.stdout'));loss=report(out/(label+'-report.stdout'),parsed);assert loss['raw_events']>0 and loss['raw_period']>0
  period=collections.Counter();events=collections.Counter()
  for item in parsed:period[item['exclusive']]+=item['period'];events[item['exclusive']]+=1
  assert sum(period.values())==loss['raw_period'] and sum(events.values())==loss['raw_events']
  captures.append(dict(variant=v,fixture=f,**loss,exclusive_period=dict(period),exclusive_events=dict(events)))
pairs=[]
for f in fixtures:
 c=counter_rows[('control',f['size'],f['seed'])];v=counter_rows[('A',f['size'],f['seed'])];visits=((f['requested_ops']+f['size']-1)//f['size'])*f['size'];metrics={event:dict(control_count=c[event],candidate_count=v[event],control_per_visit=str(D(c[event])/visits),candidate_per_visit=str(D(v[event])/visits),difference_count=str(D(v[event])-D(c[event]))) for event in c};pairs.append(dict(fixture=f,metrics=metrics,instructions_direction_pass=D(v['instructions:u'])<D(c['instructions:u'])))
assert len(counter_rows)==12 and len(captures)==12 and len(s['raw_data_sha256'])==13
for n,h in s['raw_data_sha256'].items():
 if (out/n).exists():assert sha(out/n)==h
result=dict(status='pass',commands=104,semantic_parity_pass=True,known_arithmetic_and_scope_pass=True,counter_runtime_and_positivity_pass=True,disabled_zero_pass=True,captures=captures,counter_pairs=pairs,all_six_instruction_direction_pass=all(x['instructions_direction_pass'] for x in pairs),known_control=known,total_lost_events=sum(x['lost'] for x in captures),all_nonempty_stderr=warnings,raw_data_sha256=s['raw_data_sha256'],source_selection='NONE',limits=['Scoped diagnostic counters are not speed proof','Actual own timing mapping required separately','Unknown and incomplete frames retained in parser totals','Loss/warnings retained, never silently corrected','Original027 failure preserved; profile does not repair guard or confirmation failures'])
a.out.write_text(json.dumps(result,indent=2)+'\n')
