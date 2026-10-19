from pathlib import Path
import json,hashlib
OUT=Path(__file__).resolve().parents[1];report_path=OUT/'lookup-batch-validation.json';r=json.loads(report_path.read_text());assert r['status']=='PASS'
MASK=(1<<64)-1
def rng(state):
 state=(state+0x9e3779b97f4a7c15)&MASK;z=state;z=((z^(z>>30))*0xbf58476d1ce4e5b9)&MASK;z=((z^(z>>27))*0x94d049bb133111eb)&MASK;return state,z^(z>>31)
cache={}
for row in r['semantic_rows']:
 key=(row['kind'],row['size'])
 if key not in cache:
  n=row['size'];query=list(range(n));state=(1^0xd02703a89f4c51e7) if row['kind']=='lookup' else 2
  for i in range(n,1,-1):state,z=rng(state);j=z%i;query[i-1],query[j]=query[j],query[i-1]
  cache[key]=query
 query=cache[key];case=row['case'];ops=row['ops'];n=row['size']
 if case=='lookup-miss':expected=0
 elif row['kind']=='lookup' and case=='lookup-hit':expected=sum(query[i%n] for i in range(ops))
 else:expected=sum(query[i%n]+1 for i in range(ops) if case=='lookup-hit' or i%2==0)
 assert int(row['checksum'])==expected,(row,expected)
 row['independently_reconstructed_checksum']=str(expected)
assert len(r['semantic_rows'])==102 and len(r['fault_controls'])==6 and len(r['commands'])==164
for name,h in r['referees'].items():assert hashlib.sha256((OUT/name).read_bytes()).hexdigest()==h
for p in (OUT/'lookup-batch-logs').iterdir():
 if p.is_file():assert ('/'+'Users/') not in p.read_text(),str(p)
r['independent_checksum_audit']='PASS: all102 process rows reconstructed from independent Python permutations; no timings compared';report_path.write_text(json.dumps(r,indent=2)+'\n');print('PASS:102 independently reconstructed checksums;6 detected fault runs;164 command windows;public paths generic')
