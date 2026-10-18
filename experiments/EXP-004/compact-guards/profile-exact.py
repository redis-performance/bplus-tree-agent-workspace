from pathlib import Path
import json,hashlib,subprocess,datetime,os
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'profiles/manifest.json').read_text());S=R/'scratch/exp-004-compact-profiles';D=P/'profiles-exact';D.mkdir();O=S/'exact-guard';O.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();M=dict(status='running',plan_sha256=sha(P/'EXACT-PROFILE-PLAN.md'),parent_manifest_sha256=sha(P/'profiles/manifest.json'),calibrations=[],runs=[])
def save():(D/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(name,binary,args,section,meta):
 out=O/(name+'.stdout');err=O/(name+'.stderr');cmd=[str(binary.relative_to(R)),*args]
 row=dict(name=name,command=cmd,binary=str(binary.relative_to(R)),binary_sha256=sha(binary),started_utc=utc(),**meta)
 with out.open('w') as so,err.open('w') as se:
  try:rc=subprocess.run(cmd,cwd=R,env=dict(os.environ,PROFILE_USEC='1000'),stdout=so,stderr=se,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row.update(returncode=rc,ended_utc=utc(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=sha(out),stderr_sha256=sha(err));M[section].append(row);save();assert rc==0,name
for v,files in F['sources'].items():
 for n,h in files.items():assert sha(S/v/n)==h
for i in range(2):run('calibrate-'+str(i),S/'control/build/release/calibrate',['400000000'],'calibrations',{})
for v in ['control','A','B','C']:
 b=S/v/'build/release/iterator-modes';assert sha(b)==next(r['binary_sha256'] for r in F['runs'] if r['variant']==v)
 for seed in [41051,41063]:
  run(v+'-zero-trim-f4-'+str(seed),b,['--size','95','--ops','100000000','--seed',str(seed),'--warmup-passes','3','--direction','forward','--encoding','alternating-zero','--construction','trimmed','--member-bytes','16','--mask','4'],'runs',dict(variant=v,seed=seed,mask=4,direction='forward',encoding='alternating-zero',construction='trimmed'))
M['status']='complete';save();print('8 exact-mask profiles and2 calibrations complete')
