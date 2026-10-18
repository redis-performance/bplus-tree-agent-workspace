#!/usr/bin/env python3
"""Reconstruct EXP-008 timing summaries, block effects and artifact hashes from raw CSVs."""
from collections import defaultdict
import csv,hashlib,json,math,statistics,sys
from pathlib import Path
import argparse
root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('run_dir',nargs='?',default='discovery',help='run directory; defaults to the checked-in discovery')
parser.add_argument('--kind',choices=('discovery','confirmation'),help='expected campaign type; inferred from directory name when omitted')
args=parser.parse_args()
runroot=Path(args.run_dir)
if not runroot.is_absolute():
 runroot=Path.cwd()/runroot if (Path.cwd()/runroot).exists() else root/runroot
kind=args.kind or runroot.name
assert kind in ('discovery','confirmation'),'set --kind when the run directory has a custom name'
expected=15360 if kind=='discovery' else 7680
m=json.loads((runroot/'manifest.json').read_text());saved=json.loads((runroot/'process-summary.json').read_text())
assert m['status']=='complete' and len(m['runs'])==expected==len(saved)
seen={};stats=[];rows_n=0;end=''
for run,sch,ss in zip(m['runs'],m['schedule'],saved):
 assert all(run[k]==v for k,v in sch.items()) and run['returncode']==0 and end<=run['started_utc']<=run['ended_utc'];end=run['ended_utc']
 for key in ('csv','stderr'):assert hashlib.sha256((runroot/run[key]).read_bytes()).hexdigest()==run[key+'_sha256']
 rows=list(csv.DictReader((runroot/run['csv']).read_text().splitlines()));assert len(rows)==129;rows_n+=len(rows)
 values=[]
 for i,r in enumerate(rows):
  assert r['kind']=='time' and int(r['sample'])==i and int(r['operations'])==run['count']*8*math.ceil(49152/(run['count']*8))
  for k in ('width','reversed','count','seed'):assert int(r[k])==run[k]
  assert abs(float(r['elapsed_ns'])/int(r['operations'])-float(r['ns_per_decode']))<2e-8
  ident=(run['width'],run['reversed'],run['count'],run['seed']);inv=tuple(r[k] for k in ('operations','leaf_bytes','offset_mask','crossings_per_round','fixture_hash','checksum'));assert seen.setdefault(ident,inv)==inv
  offsets={(j*run['width'])%8 for j in range(run['count'])};assert int(r['offset_mask'])==sum(1<<o for o in offsets)
  assert int(r['crossings_per_round'])==8*sum(run['width']+(j*run['width'])%8>64 for j in range(run['count']))
  assert r['cycles']==r['instructions']=='';values.append(float(r['ns_per_decode']))
 sv=sorted(values);d=dict(run,min_ns=sv[0],median_ns=statistics.median(sv),p90_ns=sv[int(.9*(len(sv)-1))],max_ns=sv[-1],min_batch_ns=min(float(x['elapsed_ns']) for x in rows),endpoint_migrations=sum(x['cpu_start']!=x['cpu_end'] for x in rows))
 assert all(ss[k]==v for k,v in d.items() if k in ('min_ns','median_ns','p90_ns','max_ns','min_batch_ns','endpoint_migrations'));stats.append(d)
g=defaultdict(list)
for x in stats:g[(x['phase'],x['width'],x['reversed'],x['count'])].append(x)
summary=json.loads((runroot/'summary.json').read_text());assert len(summary)==(640 if kind=='discovery' else 320)
for x in summary:
 group=g[(x['phase'],x['width'],x['reversed'],x['count'])];assert len(group)==24
 for stat in ('min_ns','median_ns'):
  eff=[]
  for b in range(6):
   pair=[q for q in group if q['block']==b];assert ''.join(q['label'] for q in pair)=='ABBA';z=100*(statistics.mean(q[stat] for q in pair if q['label']=='B')/statistics.mean(q[stat] for q in pair if q['label']=='A')-1);eff.append(z);assert z==x[stat]['block_effects'][b]['percent']
  assert statistics.median(eff)==x[stat]['median_effect_pct'] and min(eff)==x[stat]['effect_min_pct'] and max(eff)==x[stat]['effect_max_pct']
assert sum(int(x['samples']) for x in csv.DictReader((runroot/'histogram.csv').read_text().splitlines()))==rows_n
build=json.loads((runroot/'build.json').read_text());assert all(m['binary_hashes_after'][v]==build['variants'][v]['binary_sha256'] for v in ('base','A','B','C'))
assert len(m['runs'])==len(m['schedule'])
result=dict(status='PASS',processes=expected,raw_hash_checks=2*expected,measured_batches=rows_n,fixture_identities=len(seen),cells=len(summary),paired_block_effects=len(summary)*12,serial_schedule='PASS',scope='Independent raw reconstruction, not independent experimental confirmation')
(runroot/'AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
