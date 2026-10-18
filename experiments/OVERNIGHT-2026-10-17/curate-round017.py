from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent;R=P.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();records=[]
for i,base in enumerate([P/'BOUNDARY-024/batch-promotion/faults',P/'BOUNDARY-024/batch-promotion/attempt-002/faults']):
 mf=base/'manifest.json';original=R/('scratch/round017-batch-fault'+str(i)+'-manifest-original.json');assert not original.exists();original.write_bytes(mf.read_bytes());d=json.loads(mf.read_text())
 for f in d:
  for row in f['runs']:
   err=base/(f['name']+'-'+row['stage']+'.stderr')
   if str(R) not in err.read_text():continue
   raw=R/('scratch/round017-batch-fault'+str(i)+'-'+row['stage']+'-stderr-original.txt');assert not raw.exists();raw.write_bytes(err.read_bytes());assert sha(raw)==row['stderr_sha256']
   err.write_text(raw.read_text().replace(str(R),'<workspace>'));row['raw_stderr']=str(raw.relative_to(R));row['raw_stderr_sha256']=sha(raw);row['stderr_sha256']=sha(err)
   records.append(dict(original_manifest=str(original.relative_to(R)),original_manifest_sha256=sha(original),raw_stderr=row['raw_stderr'],raw_sha256=sha(raw),public_stderr=str(err.relative_to(R)),public_sha256=sha(err)))
 mf.write_text(json.dumps(d,indent=2)+'\n')
(P/'ROUND-017-CURATION.json').write_text(json.dumps(dict(status='pass',changes=records),indent=2)+'\n');print('curated',len(records),'stderr files; originals preserved')
