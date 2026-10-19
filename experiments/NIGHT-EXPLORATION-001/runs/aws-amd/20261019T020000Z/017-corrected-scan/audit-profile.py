#!/usr/bin/env python3
"""Independent corrected baseline profile controls and coarse attribution audit."""
import argparse,collections,csv,datetime,hashlib,json,pathlib,re
p=argparse.ArgumentParser();p.add_argument('results',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args();root=a.results;read=lambda n:json.loads((root/n).read_text());expected=json.loads((pathlib.Path(__file__).parent/'expected.json').read_text());complete=read('complete.json');build=read('build-freeze.json');assert complete['status']=='complete' and complete['sampled_captures']==complete['counter_captures']==6 and complete['elapsed_seconds']<=600;assert build['commit']==expected['commit'];assert build['source_hashes']==complete['source_hashes_after']==expected['source_hashes'];assert build['scope_sha256']==expected['scope_sha256'];assert build['binary_sha256']==complete['binary_hashes_after'];assert build['cpu_affinity']==[2]
records=read('processes.json');assert len(records)==44;assert len({r['name'] for r in records})==44
for i,r in enumerate(records):
 assert r['returncode']==0 and datetime.datetime.fromisoformat(r['started_utc'])<=datetime.datetime.fromisoformat(r['finished_utc'])
 if i:assert datetime.datetime.fromisoformat(records[i-1]['finished_utc'])<=datetime.datetime.fromisoformat(r['started_utc'])
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']
def raw(name):
 rows=list(csv.DictReader((root/(name+'.stdout')).read_text().splitlines()));assert len(rows)==1 and rows[0]['cpu_start']==rows[0]['cpu_end']=='2';return rows[0]
def same(rr):
 for k in fields:assert len({r[k] for r in rr})==1,k
same([raw('san-original'),raw('san-disabled')]);zero=[]
for line in (root/'disabled.stat').read_text().splitlines():
 if line and not line.startswith('#'):
  r=next(csv.reader([line]));assert r[0].strip() in ['0','<not counted>'];zero.append(r[2])
assert len(zero)==4;same([raw('disabled-zero'),raw('n100000-s1-original')]);symbols=['zbtLeafTagMatches','zbtIndexTagMask','zbtIndexScanSlot','zbtScoreLeafElement','zbtPackedData','zbtIndexHashReachesBucket'];capture_rows=[];groups={n:dict(total_period=0,events=0,actual_callbacks=0,symbol_period=collections.Counter(),symbol_events=collections.Counter()) for n in [100000,1000000]};counter_rows=[];schedule=[]
for seed in [1,2,3]:
 for n in [100000,1000000]:
  label=f'n{n}-s{seed}';rr=[raw(label+'-'+mode) for mode in ['original','disabled','stat','record']];same(rr);assert [rr[0]['case'],int(rr[0]['size']),int(rr[0]['seed']),int(rr[0]['requested_ops']),int(rr[0]['member_bytes'])]==['scan',n,seed,5000000,16]
  counts={}
  for line in (root/(label+'.stat')).read_text().splitlines():
   if line and not line.startswith('#'):
    r=next(csv.reader([line]));assert float(r[4])==100.0;counts[r[2]]=int(r[0])
  assert set(counts)==set(['cycles:u','instructions:u','branches:u','branch-misses:u']);counter_rows.append(dict(size=n,seed=seed,counts=counts,actual_callbacks=int(rr[0]['operations']),per_callback={k:v/int(rr[0]['operations']) for k,v in counts.items()}))
  periods=collections.Counter();hits=collections.Counter();total=0;events=0
  for block in re.split(r'\n\s*\n',(root/(label+'-samples.stdout')).read_text().strip()):
   lines=block.splitlines();period=int(lines[0].strip());frames=[re.match(r'\s*([0-9a-f]+)\s+(.*)',line) for line in lines[1:]];frames=[f for f in frames if f];assert frames;events+=1;total+=period;top=frames[0].group(1);seen=set()
   for frame in frames:
    if frame.group(1)!=top:continue
    name=frame.group(2).split('+')[0]
    if name in symbols and name not in seen:periods[name]+=period;hits[name]+=1;seen.add(name)
  row=dict(size=n,seed=seed,total_period=total,events=events,symbol_period=dict(periods),symbol_events=dict(hits),symbol_share_pct={k:100*periods[k]/total for k in symbols});capture_rows.append(row);g=groups[n];g['total_period']+=total;g['events']+=events;g['actual_callbacks']+=int(rr[0]['operations']);g['symbol_period'].update(periods);g['symbol_events'].update(hits);schedule.extend([label+'-'+mode for mode in ['stat','record','report','samples']])
assert [r['name'] for r in records][-24:]==schedule
for n,g in groups.items():g['symbol_share_pct']={k:100*g['symbol_period'][k]/g['total_period'] for k in symbols}
verified_data=0
for name,h in complete['raw_data_sha256'].items():
 if (root/name).exists():
  assert hashlib.sha256((root/name).read_bytes()).hexdigest()==h;verified_data+=1
result={'raw_data_hashes_verified':verified_data,'expected_raw_data_hashes':complete['raw_data_sha256'],'status':'pass','commit':expected['commit'],'commands':44,'native_original_disabled_pairs':6,'sanitizer_pair':1,'disabled_zero_counters':zero,'sampled_captures':6,'counter_captures':6,'capture_rows':capture_rows,'sample_summary':groups,'counter_rows':counter_rows,'source_selection':'NONE','candidate_measurements':0,'limits':['FIFO acknowledgement and clock edges included, setup/warmup/postvalidation excluded','Same-IP inline period shares overlap; unknown/control samples retained in denominator','Sample attribution is coarse and diagnostic binary layout differs from original timing binary','No cross-identity or candidate timing inference']};a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({n:{'events':g['events'],'helper_events':g['symbol_events']['zbtLeafTagMatches'],'helper_pct':g['symbol_share_pct']['zbtLeafTagMatches']} for n,g in groups.items()},indent=2))
