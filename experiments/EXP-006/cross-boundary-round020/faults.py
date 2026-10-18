from pathlib import Path
import datetime,difflib,hashlib,json,shutil,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'manifest.json').read_text());assert M['status']=='complete'
desc=M['snapshots']['C'];base=R/desc['path'];D=P/'faults';D.mkdir();S=R/'scratch/experiment006-cross-boundary-round020-faults';assert not S.exists();S.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
original=(base/'src/zset_btree.c').read_text();a=original.index('unsigned int zbtreeScores(');b=original.index('/* Lookup used by ZADD.',a);region=original[a:b]
old='        if (zbtIndexFind(zs, hashes[i], (unsigned char *)members[i],\n                         sdslen(members[i]), &scores[i], NULL, NULL, NULL, NULL))\n            found |= 1U << i;'
assert region.count(old)==1
new='        int hit = zbtIndexFind(zs, hashes[i], (unsigned char *)members[i],\n                         sdslen(members[i]), &scores[i], NULL, NULL, NULL, NULL);\n        if (!zs->member_rehash)\n            hit = zbtIndexTableFind(zs, &cached_table, hashes[i],\n                (unsigned char *)members[i], sdslen(members[i]), &scores[i],\n                NULL, NULL, NULL, NULL, NULL, NULL); /* deliberate stale table after promotion */\n        if (hit) found |= 1U << i;'
cache=region.replace('    unsigned int found = 0;', '    zbtIndexTable cached_table = zs->member_index; /* deliberate cached descriptor */\n    unsigned int found = 0;').replace(old,new)
last=region.replace('    unsigned int found = 0;', '    int active_before = zs->member_rehash != NULL;\n    unsigned int found = 0;').replace('found |= 1U << i;', 'if (!(active_before && !zs->member_rehash && i+1==count)) found |= 1U << i; /* deliberate promotion last hit omission */')
overrun=region.replace('    unsigned int found = 0;', '    int active_before = zs->member_rehash != NULL;\n    unsigned int found = 0;').replace('    return found;', '    if (count && active_before && !zs->member_rehash) scores[count] = 0.0; /* deliberate outside-count write */\n    return found;')
assert original.count('        leaf->id = id;')==1
stale=original.replace('        leaf->id = id;','        /* deliberate stale leaf ID in compacted registry */')
assert original.count('                zbtExternalSetPointer(record, newptr);')==1
shallow=original.replace('                zbtExternalSetPointer(record, newptr);','                (void)newptr; /* deliberate shallow external pointer after clone */')
items=[('cached-table-after-promotion',original[:a]+cache+original[b:],'partial_batch_promotion_oracle.c',[]),('last-hit-omission',original[:a]+last+original[b:],'partial_batch_promotion_oracle.c',[]),('outside-count-write',original[:a]+overrun+original[b:],'partial_batch_promotion_oracle.c',[]),('stale-renumbered-leaf-id',stale,'live_widen_narrow_oracle.c',[]),('shallow-external-clone',shallow,'live_widen_external_oracle.c',['0'])]
F=dict(status='preparing',plan_sha256=sha(P/'FAULT-PLAN.md'),driver_sha256=sha(Path(__file__)),parent_manifest_sha256=sha(P/'manifest.json'),runs=[])
def save():(D/'manifest.json').write_text(json.dumps(F,indent=2)+'\n')
for name,changed,oracle,mode in items:
 B=S/name;B.mkdir()
 for n,h in desc['files'].items():
  assert sha(base/n)==h;dest=B/n;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(base/n,dest)
 (B/'build').mkdir();(B/'src/zset_btree.c').write_text(changed)
 (D/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
 row=dict(name=name,path=str(B.relative_to(R)),files={n:sha(B/n) for n in desc['files']},patch_sha256=sha(D/(name+'.patch')),commands=[]);F['runs'].append(row);save()
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all','tests/'+oracle,'compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/fault']
 for stage,args in [('build',cmd),('run',['build/fault','92503']+mode)]:
  if datetime.datetime.now(datetime.timezone.utc)>=datetime.datetime.fromisoformat('2026-10-18T06:27:00+00:00'):F['status']='budget-exhausted';save();raise SystemExit(3)
  tag=name+'-'+stage;r=dict(stage=stage,command=args,cwd=str(B.relative_to(R)),started_utc=utc());raw=B/(tag+'.raw.stderr')
  with (D/(tag+'.stdout')).open('w') as out,raw.open('w') as err:
   try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
   except subprocess.TimeoutExpired:rc='timeout'
  (D/(tag+'.stderr')).write_text(raw.read_text().replace(str(R),'<workspace>'))
  r.update(returncode=rc,ended_utc=utc(),raw_stderr=str(raw.relative_to(R)),raw_stderr_sha256=sha(raw),stdout_sha256=sha(D/(tag+'.stdout')),stderr_sha256=sha(D/(tag+'.stderr')));row['commands'].append(r);save()
  if stage=='build' and rc!=0:F['status']='build-failed';save();raise SystemExit(tag+' failed')
 err=(D/(name+'-run.stderr')).read_text();row['detected']=isinstance(rc,int) and rc!=0 and any(x in err for x in ['live-score','live-widen','AddressSanitizer','runtime error:','tests/../src/zset_btree.c:'])
 row['outcome']='detected' if row['detected'] else ('SURVIVED' if rc==0 else 'inconclusive');row['binary_sha256']=sha(B/'build/fault');save();print(name,row['outcome'],flush=True)
F.update(status='complete',ended_utc=utc());save()
