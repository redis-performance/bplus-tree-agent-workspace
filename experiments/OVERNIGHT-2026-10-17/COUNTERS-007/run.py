from pathlib import Path
import datetime,hashlib,json,os,shutil,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-counters-007';assert not S.exists();S.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
cases=[('lifecycle',P.parent/'BOUNDARY-019/attempt-002','leaf_id_lifecycle_oracle',4),('relocation',P.parent/'BOUNDARY-020','active_resize_defrag_oracle',4),('mutation',P.parent/'BOUNDARY-020/mutation-extension/attempt-002','active_resize_mutation_oracle',8)]
M=dict(status='preparing',scope='whole-process oracle execution counts, no timings',plan_sha256=sha(P/'PLAN.md'),cases={},runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(tag,args,B,outpath,env=None):
 row=dict(name=tag,command=[x.replace(str(R),'<workspace>') for x in args],cwd=str(B.relative_to(R)),started_utc=utc(),stdout=str(outpath.relative_to(R)))
 err=P/(tag+'.stderr')
 with outpath.open('w') as out,err.open('w') as e:
  try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=e,env=env,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(outpath),stderr_sha256=sha(err));M['runs'].append(row);save();assert rc==0
for name,parent,oracle,n in cases:
 F=json.loads((parent/'manifest.json').read_text());assert F['status']=='complete';desc=F['snapshots']['control'];B=S/name;B.mkdir()
 for f,h in desc['files'].items():
  src=R/desc['path']/f;assert sha(src)==h;dst=B/f;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 (B/'build').mkdir();M['cases'][name]=dict(base_commit=F['base_commit'],source_manifest_sha256=sha(parent/'manifest.json'),snapshot=str(B.relative_to(R)),files=desc['files'],fixtures=n,oracle=oracle)
M['status']='frozen';M['frozen_utc']=utc();save()
for name,parent,oracle,n in cases:
 B=S/name;cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-O1','-DREDIS_DEBUG','-fprofile-instr-generate','-fcoverage-mapping','tests/'+oracle+'.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/census']
 run(name+'-build',cmd,B,P/(name+'-build.stdout'));M['cases'][name]['binary_sha256']=sha(B/'build/census');save()
for name,parent,oracle,n in cases:
 B=S/name;raw=B/'counts.profraw';data=B/'counts.profdata';export=B/'export.json';binary=B/'build/census'
 run(name+'-capture',['build/census'],B,P/(name+'-capture.stdout'),dict(os.environ,LLVM_PROFILE_FILE=str(raw)))
 assert 'PASS fixtures='+str(n)+' ' in (P/(name+'-capture.stdout')).read_text()
 run(name+'-merge',['xcrun','llvm-profdata','merge','-sparse',str(raw),'-o',str(data)],B,P/(name+'-merge.stdout'))
 run(name+'-export',['xcrun','llvm-cov','export',str(binary),'-instr-profile='+str(data)],B,export)
 report=json.loads(export.read_text());functions=[f for d in report['data'] for f in d['functions']]
 names=['zbtScoreRegisterLeaf','zbtScoreReleaseLeafId','zbtScoreRemoveLeaf','zbtIndexRehashStep','zbtreeDefragStart','zbtreeDefragStep','zbtScoreLeafById','zbtreeInsertNewRaw','zbtreeInsertNewAppend','zbtreeDeleteRangeByRank','zbtreeUpdateScore','zbtreeDelete']
 selected=[]
 for fname in names:
  fs=[f for f in functions if f['name']==fname or f['name'].endswith(':'+fname)];assert len(fs)==1,(fname,len(fs))
  f=fs[0];selected.append(dict(name=fname,count=f['count'],regions=f['regions'],branches=f['branches']))
 counts={f['name']:f['count'] for f in selected};assert counts['zbtScoreRegisterLeaf']>0 and counts['zbtreeDeleteRangeByRank']>0
 assert (counts['zbtreeDefragStep']==0)==(name=='lifecycle')
 (P/(name+'-counts.json')).write_text(json.dumps(selected,indent=2)+'\n')
 source=(B/'src/zset_btree.c').read_text().splitlines();lines=set()
 for f in selected:
  for b in f['branches']:lines.update(range(b[0],b[2]+1))
 (P/(name+'-source-lines.json')).write_text(json.dumps({str(i):source[i-1] for i in sorted(lines)},indent=2)+'\n')
 M['cases'][name].update(raw_sha256=sha(raw),profdata_sha256=sha(data),export_sha256=sha(export),counts=counts,counts_sha256=sha(P/(name+'-counts.json')),source_lines_sha256=sha(P/(name+'-source-lines.json')));save();print(name,'PASS',counts,flush=True)
for name,d in M['cases'].items():
 B=R/d['snapshot'];assert sha(B/'build/census')==d['binary_sha256']
 for f,h in d['files'].items():assert sha(B/f)==h
M['status']='complete';save()
