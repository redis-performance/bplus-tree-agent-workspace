from pathlib import Path
import hashlib,json,shutil
P=Path(__file__).resolve().parent;R=P.parents[1];S=R/'scratch/round018-curation';S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();records=[]
pairs=[(P/'BOUNDARY-025/faults/cached-table-after-promotion-run.stderr',P/'BOUNDARY-025/faults/manifest.json'),(R/'experiments/EXP-006/tag-guard/fault-sanitize.stderr',R/'experiments/EXP-006/tag-guard/manifest.json')]
for i,(file,manifest) in enumerate(pairs):
 old=sha(file);raw=S/(str(i)+'-raw.stderr');shutil.copy2(file,raw);saved=S/(str(i)+'-manifest-before.json');shutil.copy2(manifest,saved);s=file.read_text();assert str(R) in s;file.write_text(s.replace(str(R),'<workspace>'));new=sha(file);m=json.loads(manifest.read_text());changed=0
 def update(x):
  global changed
  if isinstance(x,dict):
   for k,v in x.items():
    if k=='stderr_sha256' and v==old:x[k]=new;changed+=1
    else:update(v)
  elif isinstance(x,list):
   for v in x:update(v)
 update(m);assert changed==1;manifest.write_text(json.dumps(m,indent=2)+'\n');records.append(dict(file=str(file.relative_to(R)),original=str(raw.relative_to(R)),original_sha256=old,curated_sha256=new,manifest_before=str(saved.relative_to(R)),manifest_before_sha256=sha(saved),manifest_after_sha256=sha(manifest)))
(P/'ROUND-018-CURATION.json').write_text(json.dumps(records,indent=2)+'\n');print('curated',len(records),'stderr files; raw originals preserved')
