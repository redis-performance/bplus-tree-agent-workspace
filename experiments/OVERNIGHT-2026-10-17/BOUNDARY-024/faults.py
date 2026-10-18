from pathlib import Path
import datetime,difflib,hashlib,json,shutil,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'manifest.json').read_text());assert M['status']=='complete'
desc=M['snapshots']['control'];base=R/desc['path'];D=P/'faults';D.mkdir();S=R/'scratch/overnight-boundary-024-faults';assert not S.exists();S.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
original=(base/'src/zset_btree.c').read_text()
old='        zbtIndexTableInsertRaw(&zs->member_rehash->table,\n                               hash, new_leaf_id);'
assert original.count(old)==1
omit=original.replace(old,'        /* deliberate missing destination insertion */')
a=original.index('static int zbtScoreUpdateInPlace(');b=original.index('/* Record the page share',a)
region=original[a:b];old='        zbtWriteBits(leaf->data, (size_t)physical * leaf->score_bits,'
assert region.count(old)==1
narrow=original[:a]+region.replace(old,'        if (0) zbtWriteBits(leaf->data, (size_t)physical * leaf->score_bits, /* deliberate stale score */')+original[b:]
rows=[]
for name,changed in [('omit-moved-destination',omit),('stale-inplace-score',narrow)]:
    B=S/name;shutil.copytree(base,B,ignore=shutil.ignore_patterns('build'));(B/'build').mkdir()
    for n,h in desc['files'].items():assert sha(B/n)==h
    (B/'src/zset_btree.c').write_text(changed);(D/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
    row=dict(name=name,snapshot=str(B.relative_to(R)),source_sha256=sha(B/'src/zset_btree.c'),runs=[])
    cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O1','-Wall','-Wextra','-Werror','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all','tests/live_widen_score_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/fault']
    for stage,args in [('build',cmd),('run',['build/fault','70501'])]:
        tag=name+'-'+stage;r=dict(stage=stage,command=args,cwd=str(B.relative_to(R)),started_utc=utc())
        with (D/(tag+'.stdout')).open('w') as out,(D/(tag+'.stderr')).open('w') as err:
            try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
            except subprocess.TimeoutExpired:rc='timeout'
        r.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(D/(tag+'.stdout')),stderr_sha256=sha(D/(tag+'.stderr')));row['runs'].append(r)
        (D/'manifest.json').write_text(json.dumps(rows+[row],indent=2)+'\n');assert rc==0 if stage=='build' else isinstance(rc,int)
    row['detected']=rc!=0 and any(x in (D/(name+'-run.stderr')).read_text() for x in ['live-score','AddressSanitizer','Assertion','src/zset_btree.c:']);row['outcome']='detected' if row['detected'] else 'SURVIVED';row['binary_sha256']=sha(B/'build/fault');rows.append(row)
    (D/'manifest.json').write_text(json.dumps(rows,indent=2)+'\n');print(name,row['outcome'],flush=True)
