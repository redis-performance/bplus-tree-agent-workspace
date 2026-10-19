from pathlib import Path
import collections,csv,json,re
p=Path(__file__).parent;d=p/'matched-profiles';records=[];aggregate={}
for v in ['base','A','B','C']:
 symbols=[]
 for line in (d/f'{v}.symbols.txt').read_text().splitlines():
  cols=line.split()
  if len(cols)==4 and cols[2] in ['T','t']:symbols.append((int(cols[0],16),int(cols[1],16),cols[3]))
 funcs={name:(address,size) for address,size,name in symbols};assert 'zbtreeIteratorNext' in funcs
 for f in sorted(d.glob(v+'-*.hist.csv')):
  tag=f.name[:-9];stderr=(d/(tag+'.stderr')).read_text();meta=dict(re.findall(r'(\w+)=(\d+)',stderr));assert int(meta['bin_bytes'])==2 and int(meta['scale'])==65536
  hist={int(r['offset']):int(r['count']) for r in csv.DictReader(f.open())};total=sum(hist.values());assert total==int(meta['captured']);assert max(hist.values(),default=0)<65535
  interval=int(meta['interval_ns']);assert not interval or int(meta['cpu_elapsed_ns'])//interval+4<65535
  rows=list(csv.DictReader((d/(tag+'.stdout')).open()));assert len(rows)==1;row=rows[0];assert row['checksum']==row['expected_checksum'];assert row['cpu_start']==row['cpu_end']=='2'
  disabled=tag.endswith('-disabled');assert int(meta['disabled'])==disabled
  if disabled:assert total==0
  else:assert total>0
  counts=collections.Counter()
  for offset,count in hist.items():
   names=[name for address,size,name in symbols if address<=offset<address+size];counts[names[0] if names else '<unmapped>']+=count
  records.append(dict(tag=tag,captured=total,disabled=disabled,metadata=meta,symbol_counts=dict(counts),top_buckets=sorted(hist.items(),key=lambda x:x[1],reverse=True)[:12]))
  if not disabled:
   key='-'.join(tag.split('-')[:-1]);out=aggregate.setdefault(key,dict(captured=0,iterator=0,buckets=collections.Counter(),captures=0));out['captured']+=total;out['iterator']+=counts['zbtreeIteratorNext'];out['buckets'].update(hist);out['captures']+=1
 for key,out in aggregate.items():
  if key.startswith(v+'-'):out['iterator_range']=funcs['zbtreeIteratorNext']
assert len(records)==40 and sum(not r['disabled'] for r in records)==36
for key,out in aggregate.items():
 assert out['captures']==3;out['iterator_share']=100*out['iterator']/out['captured'];out['top_buckets']=out['buckets'].most_common(12);del out['buckets']
result=dict(status='pass',enabled_captures=36,disabled_controls=4,denominator='captured in-range samples only',records=records,aggregate=aggregate)
(p/'matched-profile-audit.json').write_text(json.dumps(result,indent=2)+'\n')
for key,out in aggregate.items():print(key,out['captured'],round(out['iterator_share'],2),out['top_buckets'][:4])
mapped=[]
for variant in ['base','A','B','C']:
 instructions=[]
 for line in (d/f'{variant}.next.txt').read_text().splitlines():
  match=re.match(r'\s*([0-9a-f]+):\s*((?:[0-9a-f]{2} )+)\s*(.*)',line)
  if match and match[3]:instructions.append((int(match[1],16),len(match[2].split()),match[3]))
 for key,value in aggregate.items():
  if not key.startswith(variant+'-'):continue
  buckets=[]
  for bucket,count in value['top_buckets']:
   near=[(address,text) for address,size,text in instructions if address<=bucket<address+size]
   buckets.append(dict(bucket=hex(bucket),samples=count,containing_instruction=near))
  mapped.append(dict(cell=key,iterator_range=[hex(x) for x in value['iterator_range']],captured=value['captured'],iterator_share=value['iterator_share'],top_buckets=buckets))
(p/'matched-profile-pc-map.json').write_text(json.dumps(mapped,indent=2)+'\n')
