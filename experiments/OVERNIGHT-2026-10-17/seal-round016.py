"""Close the finalizer's own stdout hash after that process has exited."""
from pathlib import Path
import datetime,hashlib,json
P=Path(__file__).resolve().parent;R=P.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
f=P/'ROUND-016-SHA256.json';before=sha(f);m=json.loads(f.read_text());changed=[n for n,h in m.items() if sha(R/n)!=h]
name=str((P/'ROUND-016-FINALIZE.stdout').relative_to(R));assert changed==[name],changed
assert m[name]==hashlib.sha256(b'').hexdigest()
row=dict(status='pass',reason='Finalizer stdout was still open when initial manifest was written; process has exited. Only that closing log changed.',initial_manifest_sha256=before,changed_file=name,initial_sha256=m[name],closed_sha256=sha(R/name),sealed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
r=P/'ROUND-016-SEAL.json';assert not r.exists();r.write_text(json.dumps(row,indent=2)+'\n');m[name]=row['closed_sha256']
for p in [r,Path(__file__).resolve()]:m[str(p.relative_to(R))]=sha(p)
f.write_text(json.dumps(dict(sorted(m.items())),indent=2)+'\n')
assert all(sha(R/n)==h for n,h in m.items())
print(json.dumps(dict(status='pass',sealed_files=len(m),all_hashes_match=True),indent=2))
