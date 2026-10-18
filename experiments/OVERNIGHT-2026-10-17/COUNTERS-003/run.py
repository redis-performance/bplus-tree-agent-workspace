from pathlib import Path
import json,hashlib,shutil,subprocess,datetime,itertools,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-counters-003/base';assert not B.exists();B.mkdir(parents=True)
F=json.loads((P.parent/'HARNESS-004/freeze.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert sha(src)==h;dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
s=(B/'bench/iterator_modes.c').read_text();assert s.count('int main(int argc,char **argv)')==1
(B/'bench/iterator_helpers.h').write_text(s.split('int main(int argc,char **argv)')[0]);shutil.copy2(P/'census.c',B/'bench/census.c');(B/'build').mkdir()
M=dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),provenance='uncommitted structural census, tree unchanged',plan_sha256=sha(P/'PLAN.md'),sources={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()},builds=[],runs=[],status='preparing')
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(name,cmd,section,meta={}):
 row=dict(name=name,command=cmd,cwd=str(B.relative_to(R)),started_utc=utc(),**meta)
 with (P/f'{name}.stdout').open('w') as so,(P/f'{name}.stderr').open('w') as se:
  try:q=subprocess.run(cmd,cwd=B,stdout=so,stderr=se,timeout=120);rc=q.returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(P/f'{name}.stdout'),stderr_sha256=sha(P/f'{name}.stderr'));M[section].append(row);save();assert rc==0,name
 return row
for kind in ['release','sanitize']:
 flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-DREDIS_DEBUG',*flags,'bench/census.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',f'build/{kind}']
 run(kind+'-build',cmd,'builds')
cells=[(4096,b,s,e,o) for s,e,o,b in itertools.product([7103,11213],['integer','fraction','wide','zero'],['shuffled','ascending','descending'],[16,253,254,255,319,320])]
cells += [(100000,b,s,e,'shuffled') for s,e,b in itertools.product([7103,11213],['integer','fraction','wide','zero'],[16,320])]
M['status']='running';save();results=[]
for kind in ['release','sanitize']:
 for i,cell in enumerate(cells):
  name=f'{kind}-{i:03d}';row=run(name,[f'build/{kind}',*map(str,cell)],'runs',dict(kind=kind,cell=cell,binary_sha256=sha(B/f'build/{kind}')))
  data=json.loads((P/f'{name}.stdout').read_text());assert sum(data['widths'])==sum(data['shifts'])==data['n']==data['elements'];row['result']=data;results.append(row);save()
  if i%20==0:print(kind,i,'PASS',flush=True)
for i in range(len(cells)):assert results[i]['result']==results[len(cells)+i]['result']
for name,h in M['sources'].items():assert sha(B/name)==h
primary=[r['result'] for r in results if r['kind']=='release' and r['cell'][0]==100000 and r['cell'][3]=='integer']
M['primary']=[dict(seed=d['seed'],bytes=d['bytes'],fraction=d['narrow_nonzero']/d['n'],passes=d['narrow_nonzero']>=.99*d['n']) for d in primary]
M['coverage_hypothesis_supported']=all(x['passes'] for x in M['primary']);M['status']='complete';save();print(M['primary'],flush=True)
