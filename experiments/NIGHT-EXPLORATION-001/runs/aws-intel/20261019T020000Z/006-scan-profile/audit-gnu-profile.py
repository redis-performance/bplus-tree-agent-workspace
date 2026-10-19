from pathlib import Path
import json,csv,re,collections,datetime,hashlib
p=Path(__file__).parent;mapping=json.loads((p/'mapping-command.json').read_text());base=mapping['linker_base'];frames={};address=None;lines=[]
def flush():
 if address is not None:
  assert len(lines)%2==0
  frames[address-base]=[dict(function=lines[i],location=lines[i+1]) for i in range(0,len(lines),2)]
for line in (p/'inline-map.txt').read_text().splitlines():
 if re.fullmatch('0x[0-9a-fA-F]+',line):flush();address=int(line,16);lines=[]
 else:lines.append(line)
flush();records=[];aggregate={}
for n in [100000,1000000]:
 aggregate[str(n)]=dict(captured=0,tagmatches=0,scan_slot=0,captures=0)
 for seed in [1,2,3]:
  tag=f'scan-{n}-seed{seed}';hist={int(r['offset']):int(r['count']) for r in csv.DictReader((p/'profiles'/(tag+'.hist.csv')).open())};meta=dict(re.findall(r'(\w+)=(\d+)',(p/'profiles'/(tag+'.stderr')).read_text()));total=sum(hist.values())
  assert total==int(meta['captured'])>0;assert int(meta['disabled'])==0;assert int(meta['bin_bytes'])==2 and int(meta['scale'])==65536
  assert int(meta['cpu_elapsed_ns'])//int(meta['interval_ns'])+4<65535 and max(hist.values())<65535
  counts=collections.Counter()
  for offset,count in hist.items():
   assert offset in frames and offset<int(meta['text_offset_end'])
   for name in {f['function'] for f in frames[offset]}:counts[name]+=count
  a=aggregate[str(n)];a['captured']+=total;a['tagmatches']+=counts['zbtLeafTagMatches'];a['scan_slot']+=counts['zbtIndexScanSlot'];a['captures']+=1
  records.append(dict(tag=tag,captured=total,inclusive_inline_samples=dict(counts),metadata=meta,top_buckets=[dict(offset=hex(offset),samples=count,frames=frames[offset]) for offset,count in sorted(hist.items(),key=lambda x:x[1],reverse=True)[:12]]))
for a in aggregate.values():
 a['tagmatches_pct']=100*a['tagmatches']/a['captured'];a['scan_slot_pct']=100*a['scan_slot']/a['captured'];a['materially_present']=a['tagmatches']>=10 and a['tagmatches_pct']>=5
processes=json.loads((p/'processes.json').read_text());assert len(processes)==15;last=None
for r in processes:
 rows=list(csv.DictReader((p/'profiles'/(r['tag']+'.stdout')).open()));assert rows==[r['row']]
 assert r['row']['cpu_start']==r['row']['cpu_end']=='2'
 start=datetime.datetime.fromisoformat(r['started_utc']);end=datetime.datetime.fromisoformat(r['finished_utc']);assert start<=end
 if last is not None:assert last<=start
 last=end
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes'];bytag={r['tag']:r['row'] for r in processes}
for n in [100,1000,10000]:assert all(bytag[f'original-{n}'][k]==bytag[f'disabled-{n}'][k] for k in fields)
assert all(bytag['original-sanitize-control'][k]==bytag['sanitize-control'][k] for k in fields)
assert bytag['original-san-control']['tree_bytes']!=bytag['sanitize-control']['tree_bytes']
for f in (p/'profiles').glob('*disabled*.hist.csv'):assert sum(int(r['count']) for r in csv.DictReader(f.open()))==0
assert sum(int(r['count']) for r in csv.DictReader((p/'profiles/sanitize-control.hist.csv').open()))==0
manifest=json.loads((p/'source-manifest.json').read_text());assert hashlib.sha256((p/'scan-profile.c').read_bytes()).hexdigest()==manifest['profile_referee_sha256'];assert hashlib.sha256((p/'sampler.c').read_bytes()).hexdigest()==manifest['sampler_sha256']
result=dict(status='pass',captures=6,serial_process_windows=15,scope='original scan loop plus timer/control edges; setup/warmup/postvalidation excluded',denominator='captured executable-range samples only; nested inline scopes overlap',aggregate=aggregate,records=records)
(p/'profile-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(aggregate,indent=2))
