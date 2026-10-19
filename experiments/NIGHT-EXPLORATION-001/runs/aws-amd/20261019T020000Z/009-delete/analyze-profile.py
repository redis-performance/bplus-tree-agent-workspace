from pathlib import Path
import json,re,csv,hashlib,collections
p=Path('scratch/delete-profile');rows=[];comb={}
for f in sorted(p.glob('*.samples')):
 n=int(re.search(r'-n(\d+)-',f.name).group(1));periods=collections.Counter();hits=collections.Counter();tops=collections.Counter();offsets=collections.defaultdict(lambda:dict(samples=0,period=0));total=0;events=0
 for block in re.split(r'\n\s*\n',f.read_text().strip()):
  lines=block.splitlines();period=int(lines[0].strip());frames=[re.match(r'\s*([0-9a-f]+)\s+(.*)',x) for x in lines[1:]];frames=[x for x in frames if x];assert frames
  total+=period;events+=1;top=frames[0].group(1);same=[x for x in frames if x.group(1)==top];seen=set()
  for frame in same:
   name=frame.group(2).split('+')[0]
   if name not in seen:periods[name]+=period;hits[name]+=1;seen.add(name)
   m=re.match(r'zbtScoreDeleteInPlace\+0x([0-9a-f]+)',frame.group(2))
   if m:offsets[m.group(1)]['period']+=period;offsets[m.group(1)]['samples']+=1
  tops[same[-1].group(2).split('+')[0]]+=period
 row=dict(label=f.stem,size=n,total_samples=events,total_period=total,same_ip_symbol_period=dict(periods),same_ip_symbol_samples=dict(hits),physical_symbol_period=dict(tops),delete_offsets=dict(offsets));rows.append(row)
 z=comb.setdefault(n,dict(samples=0,period=0,symbols=collections.Counter(),physical=collections.Counter(),offsets=collections.defaultdict(lambda:dict(samples=0,period=0))));z['samples']+=events;z['period']+=total;z['symbols'].update(periods);z['physical'].update(tops)
 for k,v in offsets.items():
  for key in v:z['offsets'][k][key]+=v[key]
for z in comb.values():
 z['top_physical_pct']={k:100*v/z['period'] for k,v in z['physical'].most_common(15)};z['top_inclusive_pct']={k:100*v/z['period'] for k,v in z['symbols'].most_common(20)}
out=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/009-delete/profile');out.mkdir(exist_ok=True)
(out/'rows.json').write_text(json.dumps(rows,indent=2)+'\n');(out/'summary.json').write_text(json.dumps(comb,indent=2)+'\n');(out/'raw-sha256.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in p.iterdir() if f.is_file()},indent=2)+'\n')
config=json.loads(Path('scratch/aws-worker.json').read_text())
for f in p.iterdir():
 if f.suffix in ['.csv','.stderr','.asm','.annotate'] or f.name.endswith('-report.txt'):
  t=f.read_text()
  for k in ['remote_root','remote_repo','ssh_host','ssh_key']:t=t.replace(config[k],'<'+k+'>')
  (out/f.name).write_text('\n'.join(x.rstrip() for x in t.splitlines())+'\n')
print(json.dumps({n:{k:z[k] for k in ['samples','top_physical_pct','top_inclusive_pct']} for n,z in comb.items()},indent=2))
