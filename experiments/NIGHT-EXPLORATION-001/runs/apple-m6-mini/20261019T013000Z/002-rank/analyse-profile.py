#!/usr/bin/env python3
"""Reconstruct diagnostic PC counts using the inspected accumulation region."""
from pathlib import Path
from collections import Counter
import hashlib,json
p=Path(__file__).resolve().parent/'profile'
asm=(p/'night-rank-profile-zbtreeRank.asm').read_text().splitlines();start=int(asm[1].split()[0],16)
lo=next(int(l.split()[0],16) for l in asm if '\tldur\tw0, [x29, #-0x54]' in l)
hi=next(int(l.split()[0],16) for l in asm if '\tcbz\tw12,' in l and int(l.split()[0],16)>lo)
out={'scope':'diagnostic PCs in timed public rank loop, instrumented separate binary; not exact runtime fractions','requested_interval_us':1000,'accumulation_offsets_in_zbtreeRank':[lo-start,hi-start],'already_vectorized':True,'neon_add_2d_static_count':sum('\tadd.2d\t' in l for l in asm),'calibrations':[],'profiles':[]}
for f in sorted(p.glob('sampler-calibration-*.stderr')):
 lines=f.read_text().splitlines();pcs=[l.split(',') for l in lines if l.startswith('PC,')];c=Counter(l[4] for l in pcs);assert pcs and c['sampler_probe']==len(pcs)
 out['calibrations'].append({'file':f.name,'samples':len(pcs),'symbols':dict(c),'header':lines[0]})
for n in [10000,100000,1000000]:
 f=p/f'public-n{n}.stderr';lines=f.read_text().splitlines();pcs=[l.split(',') for l in lines if l.startswith('PC,')];c=Counter(l[4] for l in pcs)
 count=sum(l[4]=='zbtreeRank' and lo-start<=int(l[2],16)-int(l[5],16)<hi-start for l in pcs)
 assert pcs and lines[0].split(',')[-1]=='0'
 out['profiles'].append({'size':n,'samples':len(pcs),'symbols':dict(c),'accumulation_region_samples':count,'file':f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
out['assembly_sha256']={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in p.glob('*.asm')}
(p/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
