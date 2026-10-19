from pathlib import Path
import json,re,csv,statistics,collections,hashlib
p=Path('scratch/scan-mechanism');out=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/008-scan-tags/mechanism');out.mkdir(exist_ok=True)
config=json.loads(Path('scratch/aws-worker.json').read_text())
def clean(t):
 for k in ['remote_root','remote_repo','ssh_host','ssh_key']:t=t.replace(config[k],'<'+k+'>')
 return '\n'.join(s.rstrip() for s in t.splitlines())+'\n'
symbols=['zbtLeafTagMatches','zbtIndexTagMask','zbtIndexScanSlot','zbtScoreLeafElement','zbtPackedData','zbtIndexHashReachesBucket'];samples=[];combined={};counters=[]
for n in [100000,1000000]:
 for seed in [1,2,3]:
  pair={};sem=[]
  for v in ['base','A']:
   label=f'{v}-n{n}-ops1000000-s{seed}';ctr={}
   for line in (p/(label+'.stat')).read_text().splitlines():
    if not line or line.startswith('#'):continue
    row=next(csv.reader([line]));assert float(row[4])==100.0,row;ctr[row[2]]=int(row[0])
   assert len(ctr)==4
   pair[v]=ctr
   for mode in ['stat','record']:
    r=list(csv.DictReader((p/(label+'-'+mode+'.csv')).read_text().splitlines()))[0];assert int(r['cpu_start'])==int(r['cpu_end'])==2 and int(r['requested_ops'])==1000000
    sem.append(tuple(r[k] for k in ['checksum','tree_bytes','operations','seed','traversals']))
   total=0;events=0;periods=collections.Counter();hits=collections.Counter()
   for block in re.split(r'\n\s*\n',(p/(label+'.samples')).read_text().strip()):
    lines=block.splitlines();period=int(lines[0].strip());frames=[re.match(r'\s*([0-9a-f]+)\s+(.*)',x) for x in lines[1:]];frames=[x for x in frames if x];assert frames
    total+=period;events+=1;top=frames[0].group(1);seen=set()
    for frame in frames:
     if frame.group(1)!=top:continue
     name=frame.group(2).split('+')[0]
     if name in symbols and name not in seen:periods[name]+=period;hits[name]+=1;seen.add(name)
   sr=dict(label=label,size=n,seed=seed,variant=v,total_samples=events,total_period=total,symbol_period=dict(periods),symbol_samples=dict(hits),symbol_percent={k:100*periods[k]/total for k in symbols});samples.append(sr)
   z=combined.setdefault(f'{v}-{n}',dict(total_samples=0,total_period=0,symbol_period=collections.Counter(),symbol_samples=collections.Counter()));z['total_samples']+=events;z['total_period']+=total;z['symbol_period'].update(periods);z['symbol_samples'].update(hits)
  assert len(set(sem))==1,(n,seed,sem)
  counters.append(dict(size=n,seed=seed,counts=pair,effects_pct={k:100*(pair['A'][k]/pair['base'][k]-1) for k in pair['base']}))
for z in combined.values():z['symbol_percent']={k:100*z['symbol_period'][k]/z['total_period'] for k in symbols}
summary={str(n):{k:dict(median_pct=statistics.median(x['effects_pct'][k] for x in counters if x['size']==n),per_seed_pct=[x['effects_pct'][k] for x in counters if x['size']==n]) for k in counters[0]['effects_pct']} for n in [100000,1000000]}
for name,value in [('counter-rows.json',counters),('counter-summary.json',summary),('sample-rows.json',samples),('sample-summary.json',combined),('raw-sha256.json',{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in p.iterdir() if f.is_file()})]:(out/name).write_text(json.dumps(value,indent=2)+'\n')
for f in p.iterdir():
 if f.suffix in ['.csv','.stat','.stderr','.stdout','.asm','.c'] or f.name.endswith('-report.txt'):(out/f.name).write_text(clean(f.read_text()))
print(json.dumps(summary,indent=2));print(json.dumps({k:dict(samples=v['total_samples'],helper_percent=v['symbol_percent']['zbtLeafTagMatches'],helper_samples=v['symbol_samples']['zbtLeafTagMatches']) for k,v in combined.items()},indent=2))
