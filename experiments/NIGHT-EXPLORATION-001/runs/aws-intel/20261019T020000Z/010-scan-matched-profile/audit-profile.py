from pathlib import Path
import json,csv,re,datetime,collections
p=Path(__file__).parent;records=json.loads((p/'processes.json').read_text());captures=json.loads((p/'captures.json').read_text());complete=json.loads((p/'complete.json').read_text());assert complete['status']=='complete' and complete['captures']==len(captures)==120 and complete['elapsed_seconds']<600
last=None
for x in records:
 assert x['returncode']==0;start=datetime.datetime.fromisoformat(x['started_utc']);end=datetime.datetime.fromisoformat(x['finished_utc']);assert start<=end
 if last is not None:assert last<=start
 last=end
known=json.loads((p/'known-control.json').read_text());assert known['enabled_samples']>=20 and known['known_work_samples']/known['enabled_samples']>=.9 and known['disabled_samples']==0 and known['checksum_equal']
sem=json.loads((p/'semantic-controls.json').read_text());assert len(sem)==8 and all(x['fields_equal'] for x in sem)
meta={}
for f in (p/'profiles').glob('*.hist.csv'):
 tag=f.name.removesuffix('.hist.csv');hist={int(x['offset']):int(x['count']) for x in csv.DictReader(f.open())};stderr=(p/'profiles'/(tag+'.stderr')).read_text();data=dict((k,int(v)) for k,v in re.findall(r'([a-z_]+)=(\d+)',stderr));assert data['bin_bytes']==2 and data['scale']==65536 and data['text_offset_start']==0;assert data['captured']==sum(hist.values()) and data['max_bin']==max(hist.values(),default=0)<65535
 assert all(0<=offset<data['text_offset_end'] and offset%2==0 and 0<count<65535 for offset,count in hist.items())
 if data['disabled']:assert not hist
 else:assert data['interval_ns']>0 and data['cpu_elapsed_ns']//data['interval_ns']+4<65535
 meta[tag]=dict(metadata=data,histogram=hist)
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']
for v in ['base','B']:
 for n in [100,1000,10000]:
  a=list(csv.DictReader((p/'profiles'/f'{v}-original-control-{n}.stdout').open()))[0];b=list(csv.DictReader((p/'profiles'/f'{v}-disabled-control-{n}.stdout').open()))[0];assert all(a[k]==b[k] for k in fields)
 a=list(csv.DictReader((p/'profiles'/(v+'-original-san-control.stdout')).open()))[0];b=list(csv.DictReader((p/'profiles'/(v+'-disabled-san-control.stdout')).open()))[0];assert all(a[k]==b[k] for k in fields)
expected=[]
for repeat in range(10):
 for seed in [301,302,303]:
  for n in [100000,1000000]:
   pair=[x for x in captures if x['repeat']==repeat and x['size']==n and x['seed']==seed];assert len(pair)==2 and {x['variant'] for x in pair}=={'base','B'};assert all(pair[0]['row'][k]==pair[1]['row'][k] for k in fields)
   for v in (['base','B'] if (seed+repeat)%2 else ['B','base']):expected.append((repeat,seed,n,v))
assert [(x['repeat'],x['seed'],x['size'],x['variant']) for x in captures]==expected
schedule=json.loads((p/'capture-schedule.json').read_text());assert [(x['repeat'],x['seed'],x['size'],x['variant']) for x in schedule]==expected
aggregate={};details=[]
for v in ['base','B']:
 base=json.loads((p/(v+'-mapping.json')).read_text())['linker_base'];mapping={int(x['Address'],16)-base:x['Symbol'] for x in json.loads((p/'profiles'/(v+'-inline-map.stdout')).read_text())}
 for n in [100000,1000000]:
  counts=collections.Counter();total=0;callbacks=0;captured_rows=[]
  for c in captures:
   if c['variant']!=v or c['size']!=n:continue
   tag=c['tag'];assert list(csv.DictReader((p/'profiles'/(tag+'.stdout')).open()))==[c['row']];assert c['row']['cpu_start']==c['row']['cpu_end']=='2';hist=meta[tag]['histogram'];one=collections.Counter();samples=sum(hist.values());assert samples>0
   for offset,count in hist.items():
    assert offset in mapping
    for name in {s['FunctionName'] for s in mapping[offset]}:one[name]+=count
   counts.update(one);total+=samples;callbacks+=int(c['row']['operations']);captured_rows.append(tag);details.append(dict(tag=tag,captured=samples,inline_inclusive_samples=dict(one),sampler=meta[tag]['metadata']))
  assert len(captured_rows)==30;aggregate[f'{v}-{n}']=dict(captured=total,actual_callbacks=callbacks,helper_samples_per_million_callbacks=1e6*counts['zbtLeafTagMatches']/callbacks,captured_samples_per_million_callbacks=1e6*total/callbacks,tagmatches=counts['zbtLeafTagMatches'],scan_slot=counts['zbtIndexScanSlot'],tagmatches_pct=100*counts['zbtLeafTagMatches']/total,scan_slot_pct=100*counts['zbtIndexScanSlot']/total,inline_inclusive_samples=dict(counts))
result=dict(status='pass',captures=120,repetitions=10,schedule_exact=True,serial_commands=len(records),known_control=known,matched_semantic_controls=8,exact_cross_source_fixture_identity=True,overflow_bound_checked=True,phase_elapsed_seconds=complete['elapsed_seconds'],denominator='Only captured in-range executable-text samples; libc/outside-range/lost/missed samples excluded or unknown. Nested inline shares overlap.',scope='Scan work plus small timer edges; setup/warmup/postvalidation excluded; no -pg or PMU use',aggregate=aggregate,details=details)
(p/'profile-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:{x:y for x,y in v.items() if x!='inline_inclusive_samples'} for k,v in aggregate.items()},indent=2))
