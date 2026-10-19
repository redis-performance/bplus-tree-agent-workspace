from pathlib import Path
import json,hashlib,struct
b=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z');p=b/'030-frontend-diagnosis';e=json.loads((p/'original-identity-import.json').read_text());m=json.loads((p/'artifact-retrieval/manifest.json').read_text());ids={'source_commit':'13e459ff8800be3f02b6b45c87dd7b0c39453fa9','source_hashes':e['source_hashes'],'candidate_source_sha256':e['candidate_source_sha256'],'candidate_patch_sha256':e['candidate_patch_sha256'],'binaries':{n:{'path':v['relative_path'],'sha256':v['expected_sha256']} for n,v in m['binaries'].items()},'source_selection':'NONE','prior_decision':'REJECT'};(p/'identities.json').write_text(json.dumps(ids,indent=2)+'\n')
MASK=(1<<64)-1
def rand(state):
 state=(state+0x9e3779b97f4a7c15)&MASK;z=state;z=((z^(z>>30))*0xbf58476d1ce4e5b9)&MASK;z=((z^(z>>27))*0x94d049bb133111eb)&MASK;return state,z^(z>>31)
x={}
for n in [129,100000,1000000]:
 bits_sum=sum(struct.unpack('<Q',struct.pack('<d',float(i)-float(n//2)))[0] for i in range(n))&MASK
 for seed in ([1801] if n==129 else [1601,1602,1603,1701,1702,1703]):
  state=seed
  for _ in range(16):state,_=rand(state)
  order=list(range(n))
  for k in range(n,1,-1):state,z=rand(state);j=z%k;order[k-1],order[j]=order[j],order[k-1]
  h=14695981039346656037
  for i in order:h=((h^i)*1099511628211)&MASK
  x[f'{n}/{seed}']={'h4_one_traversal_checksum':(n+bits_sum)&MASK,'primary_one_traversal_checksum':n*(n-1)//2,'h4_construction_fingerprint':h}
(p/'fixture-oracle.json').write_text(json.dumps(x,indent=2)+'\n');print('Independent exact fixture arithmetic/Fisher-Yates/FNV inputs prepared',len(x))
