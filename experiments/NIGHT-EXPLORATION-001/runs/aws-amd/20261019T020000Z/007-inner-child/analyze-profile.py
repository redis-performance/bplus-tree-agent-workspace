from pathlib import Path
import re,json,collections,hashlib
src=Path('scratch/child-profile');rows=[];combined={}
for f in sorted(src.glob('*.samples')):
 blocks=re.split(r'\n\s*\n',f.read_text().strip());total=0;fn=0;loop=0;transition=0;events=0;offsets=collections.defaultdict(lambda:{'samples':0,'period':0})
 for block in blocks:
  lines=block.splitlines();period=int(lines[0].strip());frames=[re.match(r'\s*([0-9a-f]+)\s+(.*)',x) for x in lines[1:]];frames=[x for x in frames if x];assert frames
  total+=period;events+=1;top=frames[0].group(1)
  for frame in frames:
   m=re.fullmatch(r'zbtScoreFindLeaf\+0x([0-9a-f]+)',frame.group(2))
   if frame.group(1)==top and m:
    off=int(m.group(1),16);fn+=period;offsets[hex(off)]['samples']+=1;offsets[hex(off)]['period']+=period
    if 0x60<=off<=0x7e:loop+=period
    if 0x37<=off<=0x48:transition+=period
    break
 n=int(re.search(r'-n(\d+)-',f.name).group(1));row=dict(label=f.stem,size=n,total_samples=events,total_period=total,findleaf_period=fn,loop_period=loop,transition_period=transition,offsets=dict(offsets));rows.append(row)
 c=combined.setdefault(n,dict(total_samples=0,total_period=0,findleaf_period=0,loop_period=0,transition_period=0,findleaf_samples=0,loop_samples=0))
 for k in ['total_samples','total_period','findleaf_period','loop_period','transition_period']:c[k]+=row[k]
 c['findleaf_samples']+=sum(x['samples'] for x in offsets.values());c['loop_samples']+=sum(x['samples'] for off,x in offsets.items() if 0x60<=int(off,16)<=0x7e)
for c in combined.values():
 for k in ['findleaf','loop','transition']:c[k+'_pct_total']=100*c[k+'_period']/c['total_period']
 c['loop_pct_findleaf']=100*c['loop_period']/c['findleaf_period']
d=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/007-inner-child');out=d/'matched-profile';out.mkdir(exist_ok=True)
(out/'rows.json').write_text(json.dumps(rows,indent=2)+'\n');(out/'summary.json').write_text(json.dumps(combined,indent=2)+'\n');(out/'raw-sha256.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in src.iterdir()},indent=2)+'\n')
for f in src.iterdir():
 if f.suffix in ['.csv','.stderr']:(out/f.name).write_bytes(f.read_bytes())
print(json.dumps(combined,indent=2))
