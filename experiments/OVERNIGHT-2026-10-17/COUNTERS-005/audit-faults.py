from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rows=json.loads((P/'faults.json').read_text());out=[]
expected={'no-reversal':'leaves==1 && reversed==(trimmed?n:0)','zero-sign':'score_bits(nextscore)==score_bits(model_score(nexti,n,encoding))'}
for r in rows:
 p=P/f'fault-{r["name"]}.stderr';assert sha(p)==r['stderr_sha256'];s=p.read_text();assert r['returncode']==-6 and expected[r['name']] in s
 out.append(dict(name=r['name'],detected=True,original_driver_detection=r['detected'],checked_assertion=expected[r['name']],stderr_sha256=sha(p),child_repeated=False))
(P/'fault-audit.json').write_text(json.dumps(out,indent=2)+'\n');print('Both faults detected;zero sign stopped earlier at copy-state exact-bit oracle. No rerun.')
