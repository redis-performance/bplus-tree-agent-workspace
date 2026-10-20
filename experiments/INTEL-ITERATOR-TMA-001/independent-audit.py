"""Independent, read-only reconstruction of sealed raw evidence; prints JSON.

Usage: python3 independent-audit.py <results-directory>
Does not modify campaign scripts, inputs or their automated result.
"""
import csv, hashlib, json, math, sys
from collections import defaultdict
from pathlib import Path

D=Path(sys.argv[1]); P=json.loads((Path(__file__).parent/'protocol.json').read_text())
checks={}; captures=[]; blocks=[]; roots={'Frontend_Bound','Bad_Speculation','Backend_Bound','Retiring'}
def read(name):return json.loads((D/name).read_text())
def filehash(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def occupancy(a,b,cpu):
 delta=[y-x for x,y in zip(a[str(cpu)],b[str(cpu)])]
 return 100*(sum(delta)-delta[3]-delta[4])/sum(delta)
def ticks(text):
 fields=text.rsplit(')',1)[1].split();return int(fields[11])+int(fields[12])
def csvrow(path):
 rows=list(csv.DictReader(path.read_text().splitlines()));assert len(rows)==1,path
 return rows[0]
for size in P['profile']['sizes']:
 for rep in range(1,P['profile']['windows_per_size']+1):
  tag=f'profile-{size}-{rep}'; path=D/(tag+'.stderr'); lines=path.read_text().splitlines()
  starts=[i for i,line in enumerate(lines) if line.startswith('Timestamp,Area,Value,Unit,')]
  assert len(starts)==1,(tag,'missing/duplicate CSV header')
  parsed=list(csv.DictReader(lines[starts[0]:])); rows=[r for r in parsed if r.get('Area')]
  rejected_rows=[r for r in parsed if not r.get('Area')]
  bytime=defaultdict(list); means=defaultdict(list)
  for r in rows:
   assert r['Timestamp'] is not None and math.isfinite(float(r['Timestamp'])),(tag,r)
   assert math.isfinite(float(r['Value'])),(tag,r)
   if r['Area'] in roots:bytime[r['Timestamp']].append(r)
   means[(r['Area'],r['Unit'])].append(float(r['Value']))
  root_ok=len(bytime)==10 and all(len(rs)==4 and {r['Area'] for r in rs}==roots and all(r['Unit'] in ('% Slots','% Slots <') and 0<=float(r['Value'])<=100 for r in rs) and abs(sum(float(r['Value']) for r in rs)-100)<=.3 for rs in bytime.values())
  scope=read(tag+'.scope.json'); smt=occupancy(scope['cpu_before'],scope['cpu_after'],50)
  delta=[b-a for a,b in zip(scope['cpu_before']['2'],scope['cpu_after']['2'])]; busy=sum(delta)-delta[3]-delta[4]
  wd=ticks(scope['workload_after'])-ticks(scope['workload_before'])
  accounting=100*abs(busy-wd)/max(busy,1)
  mux=all(float(r['Multiplex'])==100 for r in rows)
  scope_ok=scope['alive'] and scope['affinity']==[2] and smt<=1 and accounting<=1
  assert abs(smt-scope['sibling_busy_pct'])<1e-9 and abs(accounting-scope['workload_accounting_error_pct'])<1e-9
  captures.append({'tag':tag,'raw_sha256':filehash(path),'header_line':starts[0]+1,'preamble':lines[:starts[0]],'nondata_tail_rows':rejected_rows,'metric_rows':len(rows),'intervals':len(bytime),'root_partition_pass':root_ok,'all_mux_100':mux,'scope_pass':scope_ok,'sibling_busy_percent':smt,'workload_accounting_error_percent':accounting,'pass':root_ok and mux and scope_ok,'metrics':[{'metric':k[0],'unit':k[1],'count':len(v),'mean':sum(v)/len(v),'min':min(v),'max':max(v)} for k,v in sorted(means.items())]})
counts=read('frozen-counts.json'); computed_counts=[]
for cell,c in enumerate(P['cells']):
 rs=[csvrow(D/f'calibration-{cell}-{seed}.stdout') for seed in P['calibration']['seeds']]
 assert all(int(r['requested_ops'])==P['calibration']['visits'] and int(r['operations'])==P['calibration']['visits'] and r['checksum']==r['expected_checksum'] for r in rs)
 denominator=min(int(r['elapsed_ns']) for r in rs)*c['size']
 numerator=P['calibration']['visits']*P['calibration']['target_ns']
 count=((numerator+denominator-1)//denominator)*c['size'];assert count<=P['calibration']['max_visits']
 computed_counts.append(count)
checks['calibration_counts_match']=computed_counts==counts['counts']
expected=[]
for block,seed in enumerate(P['seeds']):
 for cell in range(len(P['cells'])):
  for position in range(4):expected.append({'index':len(expected),'block':block,'seed':seed,'cell':cell,'position':position,'ops':computed_counts[cell]})
schedule=read('schedule.json'); checks['schedule_matches']=schedule==expected
rows=[]; last_end=0
for item in expected:
 path=D/f"aa-{item['index']:03}.stdout"
 if not path.exists():break
 r=csvrow(path); meta=read(f"aa-{item['index']:03}.process.json"); c=P['cells'][item['cell']]
 assert meta['returncode']==0 and meta['started']>=last_end;last_end=meta['ended']
 assert r['cpu_start']==r['cpu_end']=='2' and r['checksum']==r['expected_checksum']
 assert int(r['requested_ops'])==item['ops'] and int(r['operations'])==item['ops'] and int(r['size'])==c['size']
 assert int(r['seed'])==item['seed'] and r['encoding']==c['layout'] and r['direction']==c['direction'] and int(r['mask'])==c['output_mask']
 smt=occupancy(meta['cpu_before'],meta['cpu_after'],50); assert abs(smt-meta['sibling_busy_pct'])<1e-9
 rows.append({'schedule':item,'row':r,'meta':meta,'smt':smt})
for offset in range(0,len(rows)-3,4):
 rs=rows[offset:offset+4]; ns=[int(r['row']['elapsed_ns']) for r in rs]; outer=ns[0]+ns[3]; inner=ns[1]+ns[2]
 invariants=['size','operations','traversals','checksum','expected_checksum','tree_bytes','construction_fingerprint','seed','mask','direction','encoding']
 same=all(len({r['row'][k] for r in rs})==1 for k in invariants)
 precision=abs(inner-outer)*100<=outer;duration=min(ns)>=P['minimum_window_ns'];smt=all(r['smt']<=1 for r in rs)
 blocks.append({'cell':rs[0]['schedule']['cell'],'block':rs[0]['schedule']['block'],'effect_percent':100*(inner/outer-1),'min_ns':min(ns),'precision':precision,'duration':duration,'smt':smt,'invariants':same,'pass':precision and duration and smt and same})
checks['rows_complete']=len(rows)==192
checks['serial_and_within_budget']=bool(rows) and rows[-1]['meta']['ended']-rows[0]['meta']['started']<=P['aa_budget_seconds']
checks['counts_frozen_before_aa']=bool(rows) and counts['frozen_before_aa']<=rows[0]['meta']['started']
checks['all_aa_blocks_pass']=len(blocks)==48 and all(b['pass'] for b in blocks)
checks['all_tma_captures_pass']=len(captures)==6 and all(c['pass'] for c in captures)
# Correctness and recorded build provenance: independent raw reconstruction.
parity_keys=['case','size','operations','member_bytes','seed','direction','mask','encoding','traversals','checksum','expected_checksum','tree_bytes','construction_fingerprint']
parity_count=0
for encoding in ['integer','fraction','wide','zero']:
 for direction in ['forward','reverse']:
  for mask in range(8):
   tag=f'parity-{encoding}-{direction}-{mask}'
   a=csvrow(D/(tag+'-original.stdout'));b=csvrow(D/(tag+'-long.stdout'))
   assert all(a[k]==b[k] for k in parity_keys)
   for suffix in ['original','long']:assert read(tag+'-'+suffix+'.process.json')['returncode']==0
   parity_count+=1
boundary=csvrow(D/'long-ops-boundary.stdout');assert int(boundary['requested_ops'])==100000001 and int(boundary['operations'])==100100000 and boundary['checksum']==boundary['expected_checksum']
assert read('long-ops-boundary.process.json')['returncode']==0
for variant in ['base','B']:
 for mode in ['native','sanitize']:
  test=(D/f'{variant}-tests-{mode}.txt').read_text()
  assert '43 passed' in test and '0 failed, 43 total' in test
  for name,num in [('cache-oracle',28192),('cache-oracle-additive',89428)]:
   assert (D/f'{variant}-{name}-{mode}.txt').read_text().strip()==f'PASS {num} iterator state checks sizeof=16'
checks['correctness_logs_and_64_parity_pairs_pass']=parity_count==64
manifest=json.loads((Path(__file__).parent/'input-manifest.json').read_text())
build_hashes={line.split(None,1)[1]:line.split(None,1)[0] for line in (D/'build-sha256.txt').read_text().splitlines()}
assert build_hashes['build/base/iterator']==counts['binary_sha256']
assert counts['protocol_sha256']==filehash(Path(__file__).parent/'protocol.json')
checked_input_hashes=0
for path,digest in build_hashes.items():
 if path in manifest:
  assert digest==manifest[path],path;checked_input_hashes+=1
checks['recorded_build_inputs_and_frozen_binary_match']=checked_input_hashes>=10
checks['no_candidate_timing_in_process_records']=all('build/B/iterator' not in read(p.name)['args'] for p in D.glob('*.process.json'))
result={'reviewer':'/root/intel_b_review','scope':'raw TMA and calibration/A-A reconstruction; release/correctness/build provenance reviewed separately','checks':checks,'rows':len(rows),'qualified_blocks':sum(b['pass'] for b in blocks),'blocks':blocks,'captures':captures,'automated_result_preserved':read('RESULT.json'),'automated_profile_quality_preserved':read('profile-quality.json'),'derived_preregistered_gate_result':'BASELINE_QUALIFIED' if all(checks.values()) else 'PARK','candidate_timing_runs':0,'source_adoption':'NONE'}
print(json.dumps(result,indent=2))
