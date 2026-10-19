#!/usr/bin/env python3
"""Resume the interrupted fixed profile plan, never repeat a captured child."""
import importlib.util, json
from pathlib import Path
p=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('lookup_run',p/'run.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
records=[]
for n in (10000,100000,1000000):
    for case in m.CASES:
        name=f'n{n}-{case}';dest=p/'profile'/(name+'.json');raw=p/'profile'/(name+'.stderr');local=Path('scratch/m6-lookup')/(name+'-profile.txt')
        if dest.exists():
            row=json.loads(dest.read_text())
        else:
            if not raw.exists(): m.run(m.args('lookup-profile',n,case,10000000),name,'profile')
            counts={}
            for line in raw.read_text().splitlines():
                if line.startswith('PC,'):
                    symbol=line.split(',')[4];counts[symbol]=counts.get(symbol,0)+1
            row=dict(samples=sum(counts.values()),symbols=counts,raw_sha256=m.sha(raw),raw_location='ignored scratch/m6-lookup/',requested_interval_us=1000,scope='public query loop only; sampled symbol PCs are not exact cost shares')
            raw.rename(local);m.save(dest,row)
        row=dict(size=n,case=case,**row,minimum_samples=25,profile_sufficient=row['samples']>=25)
        records.append(row)
m.save(p/'profile-summary.json',records)
r=m.run(['otool','-tvV',m.BUILD/'lookup'],'release-assembly','profile');lines=r.stdout.splitlines()
for func in ('zbtScoreLeafFindMember','zbtreeScore','zbtreeScoreRaw'):
    a=next(i for i,l in enumerate(lines) if l.strip()=='_'+func+':')
    b=next((i for i in range(a+1,len(lines)) if lines[i].startswith('_') and lines[i].endswith(':')),len(lines))
    (p/'profile'/(func+'.asm')).write_text('\n'.join(lines[a:b])+'\n')
(p/'profile/release-assembly.stdout').rename(Path('scratch/m6-lookup/release-assembly.txt'))
m.save(p/'PROFILE-RESUME.json',dict(reason='Round3 interrupted after 10K miss 13 samples failed minimum25. Preserve insufficient capture; no repeat or threshold reduction.',reused_profiles=2,new_profiles=4,summary='profile-summary.json',original_driver_sha256=m.sha(p/'run.py'),resume_driver_sha256=m.sha(__file__)))
print(json.dumps(records,indent=2))
