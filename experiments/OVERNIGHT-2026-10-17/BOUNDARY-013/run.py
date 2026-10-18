from pathlib import Path
import json,hashlib,shutil,subprocess,time,difflib,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-boundary-013/base';assert not B.exists();B.mkdir(parents=True);F=json.loads((P.parent/'HARNESS-004/freeze.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for n,h in F['files'].items():
 src=R/F['snapshot']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
shutil.copy2(R/'tests/packed_decode_oracle.c',B/'tests/packed_decode_oracle.c');(B/'build').mkdir()
(P/'oracle.patch').write_text(''.join(difflib.unified_diff([], (R/'tests/packed_decode_oracle.c').read_text().splitlines(True),fromfile='/dev/null',tofile='b/tests/packed_decode_oracle.c')))
M=dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),plan_sha256=sha(P/'PLAN.md'),sources={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()},runs=[],status='running')
for kind in ['release','sanitize']:
 flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
 commands=[['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-DREDIS_DEBUG',*flags,'tests/packed_decode_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',f'build/{kind}'],[f'build/{kind}']]
 for i,cmd in enumerate(commands):
  name=f'{kind}-{i}';start=datetime.datetime.now(datetime.timezone.utc).isoformat()
  with (P/(name+'.stdout')).open('w') as so,(P/(name+'.stderr')).open('w') as se:
   try:q=subprocess.run(cmd,cwd=B,stdout=so,stderr=se,timeout=120);rc=q.returncode
   except subprocess.TimeoutExpired:rc='timeout'
  M['runs'].append(dict(name=name,command=cmd,returncode=rc,started_utc=start,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),stdout_sha256=sha(P/(name+'.stdout')),stderr_sha256=sha(P/(name+'.stderr'))));(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n');assert rc==0,name
  print(name,rc,flush=True)
M['binaries']={k:sha(B/f'build/{k}') for k in ['release','sanitize']};M['status']='pass';(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
