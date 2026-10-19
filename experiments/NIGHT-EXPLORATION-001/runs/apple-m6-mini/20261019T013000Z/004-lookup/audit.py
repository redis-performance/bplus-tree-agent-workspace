#!/usr/bin/env python3
"""Reconstruct this target's raw rows, effects, patches and serial command windows."""
import csv,hashlib,json,statistics,subprocess,tempfile
from pathlib import Path
from datetime import datetime
OUT=Path(__file__).resolve().parent;BASE=Path('scratch/m6-lookup/variants')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def equal(a,b):assert abs(a-b)<=1e-10,(a,b)
launch=json.loads((OUT.parent/'launch-manifest.json').read_text());root_files=0
for p,h in launch['source_hashes'].items():assert sha(p)==h,p;root_files+=1
freeze=json.loads((OUT/'freeze.json').read_text())
for p,h in freeze['files'].items():assert sha(p)==h,p
cal=json.loads((OUT/'calibration.json').read_text());q=json.loads((OUT/'qualification.json').read_text());d=json.loads((OUT/'discovery.json').read_text());rows=cal['observations']+q['runs']+d['runs']
for row in rows:
 p=OUT/row['file'];assert sha(p)==row['sha256'];rs=list(csv.DictReader(p.open()));assert len(rs)==1;x=rs[0]
 assert int(x['size'])==row['size'] and int(x['operations'])==row['ops'];assert int(x['elapsed_ns'])==row['elapsed_ns'];equal(row['ns_op'],int(x['elapsed_ns'])/int(x['operations']));assert x['checksum']==row['checksum'];assert int(x['tree_bytes'])==row['tree_bytes']
for n in (100,1000,10000,100000,1000000):
 for case in ('lookup-hit','lookup-miss'):
  import math
  rs=[r for r in cal['observations'] if r['size']==n and r['case']==case];assert len(rs)==3
  assert cal['fixed_ops'][f'{n}-{case}']==min(100000000,math.ceil(50000000/min(r['ns_op'] for r in rs)))
effects=0
for data in (q,d):
 for result in data['results']:
  for block,expected in enumerate(result['effects_pct']):
   rs=[r for r in data['runs'] if r['block']==block and r['size']==result['size'] and ('variant' not in result or r['variant']==result['variant'])];assert len(rs)==4;assert ''.join(r['label'] for r in rs)=='ABBA';assert len({r['checksum'] for r in rs})==1;assert len({r['ops'] for r in rs})==1
   effect=100*(statistics.mean(r['ns_op'] for r in rs if r['label']=='B')/statistics.mean(r['ns_op'] for r in rs if r['label']=='A')-1);equal(effect,expected);effects+=1
   if 'variant' in result:assert len({r['tree_bytes'] for r in rs})==1
manifest=json.loads((OUT/'implementation-manifest.json').read_text());val=json.loads((OUT/'candidate-validation.json').read_text());patches=0;referees=0
for v in ('0','A','B','C'):
 folder=BASE/v;assert sha(folder/'src/zset_btree.c')==manifest['variants'][v]['source_sha256']==val['variants'][v]['source'];assert sha(folder/'build/lookup')==val['variants'][v]['binary']
 for name in ('compat','vendor','tests','bench'):
  for p in Path(name).rglob('*'):
   if p.is_file():assert sha(p)==sha(folder/p);referees+=1
 assert sha(folder/'src/zset_btree.h')==sha('src/zset_btree.h');assert sha(folder/OUT.relative_to(Path.cwd())/'lookup-bench.c')==sha(OUT/'lookup-bench.c')
 if v!='0':
  patch=OUT/'variants'/v/'candidate.patch';assert sha(patch)==manifest['variants'][v]['patch_sha256']
  with tempfile.TemporaryDirectory(prefix='m6-lookup-audit-',dir='scratch') as tmp:
   target=Path(tmp)/'src';target.mkdir();(target/'zset_btree.c').write_bytes(Path('src/zset_btree.c').read_bytes())
   subprocess.run(['patch','-s','-p1','-i',str(patch)],cwd=tmp,check=True,capture_output=True);assert sha(target/'zset_btree.c')==sha(folder/'src/zset_btree.c')
  patches+=1
windows=[]
for log in ('commands.jsonl','candidate-commands.jsonl'):
 for l in (OUT/log).read_text().splitlines():
  row=json.loads(l);a=datetime.fromisoformat(row['started_utc']);b=datetime.fromisoformat(row['finished_utc']);assert a<=b;windows.append((a,b,row['name']))
windows.sort()
for x,y in zip(windows,windows[1:]):assert x[1]<=y[0],(x[2],y[2])
profiles=json.loads((OUT/'profile-summary.json').read_text())
for row in profiles:
 raw=Path('scratch/m6-lookup')/(f"n{row['size']}-{row['case']}-profile.txt");assert sha(raw)==row['raw_sha256'];assert sum(row['symbols'].values())==row['samples']
 assert sum(l.startswith('PC,') for l in raw.read_text().splitlines())==row['samples']
result=dict(status='pass',root_files=root_files,raw_rows=len(rows),reconstructed_effects=effects,reconstructed_patches=patches,matched_referee_files=referees,serial_command_windows=len(windows),profiles=len(profiles),sufficient_profiles=sum(r['profile_sufficient'] for r in profiles),last_experimental_child_utc=windows[-1][1].isoformat(),source_selection='NONE',review='sequential worker audit; independent review pending')
(OUT/'final-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
