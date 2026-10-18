from pathlib import Path
import datetime,difflib,hashlib,json,shutil,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'manifest.json').read_text());assert M['status']=='complete'
desc=M['snapshots']['control'];base=R/desc['path'];D=P/'faults';D.mkdir();S=R/'scratch/overnight-boundary-025-faults';assert not S.exists();S.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
original=(base/'src/zset_btree.c').read_text()
a=original.index('unsigned int zbtreeScores(');b=original.index('/* Lookup used by ZADD.',a)
region=original[a:b]
region=region.replace('    unsigned int found = 0;', '    zbtIndexTable cached_table = zs->member_index; /* deliberate cached descriptor */\n    unsigned int found = 0;')
old='        if (zbtIndexFind(zs, hashes[i], (unsigned char *)members[i],\n                         sdslen(members[i]), &scores[i], NULL, NULL, NULL, NULL))\n            found |= 1U << i;'
assert region.count(old)==1
new='        int hit = zbtIndexFind(zs, hashes[i], (unsigned char *)members[i],\n                         sdslen(members[i]), &scores[i], NULL, NULL, NULL, NULL);\n        if (!zs->member_rehash)\n            hit = zbtIndexTableFind(zs, &cached_table, hashes[i],\n                (unsigned char *)members[i], sdslen(members[i]), &scores[i],\n                NULL, NULL, NULL, NULL, NULL, NULL); /* deliberate stale table after promotion */\n        if (hit) found |= 1U << i;'
omit=original[:a]+region.replace(old,new)+original[b:]
region=original[a:b]
last=region.replace('    unsigned int found = 0;', '    int active_before = zs->member_rehash != NULL;\n    unsigned int found = 0;').replace('found |= 1U << i;', 'if (!(active_before && !zs->member_rehash && i+1==count)) found |= 1U << i; /* deliberate promotion last hit omission */')
overrun=region.replace('    unsigned int found = 0;', '    int active_before = zs->member_rehash != NULL;\n    unsigned int found = 0;').replace('    return found;', '    if (count && active_before && !zs->member_rehash) scores[count] = 0.0; /* deliberate outside-count write */\n    return found;')
rows=[]
for name,changed in [('cached-table-after-promotion',omit),('last-hit-omission',original[:a]+last+original[b:]),('outside-count-write',original[:a]+overrun+original[b:])]:
    B=S/name;shutil.copytree(base,B,ignore=shutil.ignore_patterns('build'));(B/'build').mkdir()
    for n,h in desc['files'].items():assert sha(B/n)==h
    (B/'src/zset_btree.c').write_text(changed);(D/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
    row=dict(name=name,snapshot=str(B.relative_to(R)),source_sha256=sha(B/'src/zset_btree.c'),runs=[])
    cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O1','-Wall','-Wextra','-Werror','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all','tests/partial_batch_promotion_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/fault']
    for stage,args in [('build',cmd),('run',['build/fault','80503'])]:
        tag=name+'-'+stage;r=dict(stage=stage,command=args,cwd=str(B.relative_to(R)),started_utc=utc())
        with (D/(tag+'.stdout')).open('w') as out,(D/(tag+'.stderr')).open('w') as err:
            try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
            except subprocess.TimeoutExpired:rc='timeout'
        r.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(D/(tag+'.stdout')),stderr_sha256=sha(D/(tag+'.stderr')));row['runs'].append(r)
        (D/'manifest.json').write_text(json.dumps(rows+[row],indent=2)+'\n');assert rc==0 if stage=='build' else isinstance(rc,int)
    row['detected']=rc!=0 and any(x in (D/(name+'-run.stderr')).read_text() for x in ['live-score','AddressSanitizer','Assertion','src/zset_btree.c:']);row['outcome']='detected' if row['detected'] else 'SURVIVED';row['binary_sha256']=sha(B/'build/fault');rows.append(row)
    (D/'manifest.json').write_text(json.dumps(rows,indent=2)+'\n');print(name,row['outcome'],flush=True)
