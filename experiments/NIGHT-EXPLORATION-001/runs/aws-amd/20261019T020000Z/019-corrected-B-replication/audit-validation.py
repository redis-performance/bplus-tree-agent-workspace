#!/usr/bin/env python3
import argparse,hashlib,json,pathlib,re
p=argparse.ArgumentParser();p.add_argument('results',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args();here=pathlib.Path(__file__).parent;e=json.loads((here/'expected.json').read_text());x=json.loads((a.results/'result.json').read_text());freeze=json.loads((a.results/'freeze.json').read_text());assert x['status']=='complete' and x['elapsed_seconds']<=600 and len(x['commands'])==60;assert freeze['cpu_affinity']==[2];assert 'clang version 18.1.3' in freeze['compiler'];assert x['baseline_before']==x['baseline_after']==e['source_hashes'];assert x['baseline_binary_before']==x['baseline_binary_after']==freeze['baseline_binary']==e['aa_binary_sha256'];names=[]
for i,r in enumerate(x['commands']):
 assert r['returncode']==0 and r['started_utc']<=r['finished_utc'];names.append(r['name'])
 if i:assert x['commands'][i-1]['finished_utc']<=r['started_utc']
assert len(set(names))==60
oracles={'all_match_guard_oracle':[[]],'scan_interval_oracle':[[]],'wide_scan_oracle':[['7'],['19']],'live_widen_scan_oracle':[['7'],['19']],'resize_generation_oracle':[[]]};schedule=['compiler','archive'];original43=[];oracle_runs=[]
for v in ['base','B']:
 if v=='B':schedule.append('B-patch')
 hashes=freeze['snapshots'][v]['source_hashes'];expected=dict(e['source_hashes']);expected['tests/all_match_guard_oracle.c']=e['oracle_sha256']
 if v=='B':expected['src/zset_btree.c']=e['candidate_c_sha256']
 assert hashes==expected
 for mode in ['native','san']:
  prefix=v+'-'+mode;name=prefix+'-original43';schedule.append(name);s=(a.results/(name+'.stdout')).read_text();s=re.sub(r'\x1b\[[0-9;]*m','',s);assert '43 passed, 0 failed, 43 total' in s;original43.append(name)
  for oracle,seeds in oracles.items():
   schedule.append(prefix+'-'+oracle+'-build')
   for seed in seeds:
    name=prefix+'-'+oracle+('-'+seed[0] if seed else '');schedule.append(name);assert (a.results/(name+'.stdout')).read_text().strip();oracle_runs.append(name)
  if v=='B':schedule += [prefix+'-portable-build',prefix+'-portable'];oracle_runs.append(prefix+'-portable')
schedule.append('B-native-codegen');assert names==schedule;assembly=(a.results/'B-native-codegen.stdout').read_text();assert all(s in assembly for s in ['movdqu','pcmpeqb','pmovmskb']);result=dict(status='pass',commands=60,original43_passes=len(original43),oracle_passes=len(oracle_runs),serial=True,source_and_referee_hashes=True,baseline_binary_unchanged=True,candidate_binary_sha256=freeze['snapshots']['B']['binaries']['build/native/btree-bench'],source_selection='NONE');a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
