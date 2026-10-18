from pathlib import Path
import datetime,difflib,hashlib,json,shutil,subprocess
P=Path(__file__).resolve().parent;R=P.parents[3];M=json.loads((P/'manifest.json').read_text());assert M['status']=='complete'
desc=M['snapshots']['control'];base=R/desc['path'];D=P/'faults';D.mkdir();S=R/'scratch/overnight-boundary-023-relocation-faults';assert not S.exists();S.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
original=(base/'src/zset_btree.c').read_text()
old='        size_t bytes = zbtIndexTableBytes(source);'
assert original.count(old)==1
short=original.replace(old,'        size_t bytes = source->size * sizeof(zbtIndexBucket16); /* deliberate truncated wide clone */')
old='            zs->member_rehash->table.buckets = zbtDefragPlainAllocation('
assert original.count(old)==1
stale=original.replace(old,'            (void)zbtDefragPlainAllocation( /* deliberate lost relocated destination */')
rows=[]
for name,changed,mode in [('truncate-wide-clone',short,0),('stale-relocated-destination',stale,1)]:
    B=S/name;shutil.copytree(base,B,ignore=shutil.ignore_patterns('build'));(B/'build').mkdir()
    for n,h in desc['files'].items():assert sha(B/n)==h
    (B/'src/zset_btree.c').write_text(changed);(D/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
    row=dict(name=name,snapshot=str(B.relative_to(R)),source_sha256=sha(B/'src/zset_btree.c'),runs=[])
    cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O1','-Wall','-Wextra','-Werror','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all','tests/live_widen_relocation_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/fault']
    for stage,args in [('build',cmd),('run',['build/fault','66509',str(mode)])]:
        tag=name+'-'+stage;r=dict(stage=stage,command=args,cwd=str(B.relative_to(R)),started_utc=utc())
        raw_err=B/(tag+'.raw.stderr')
        with (D/(tag+'.stdout')).open('w') as out,raw_err.open('w') as err:
            try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
            except subprocess.TimeoutExpired:rc='timeout'
        (D/(tag+'.stderr')).write_text(raw_err.read_text().replace(str(R),'<workspace>'))
        r.update(raw_stderr=str(raw_err.relative_to(R)),raw_stderr_sha256=sha(raw_err))
        r.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(D/(tag+'.stdout')),stderr_sha256=sha(D/(tag+'.stderr')));row['runs'].append(r)
        (D/'manifest.json').write_text(json.dumps(rows+[row],indent=2)+'\n');assert rc==0 if stage=='build' else isinstance(rc,int)
    row['detected']=rc!=0 and any(x in (D/(name+'-run.stderr')).read_text() for x in ['live-widen','AddressSanitizer','tests/../src/zset_btree.c:']);row['outcome']='detected' if row['detected'] else 'SURVIVED';row['binary_sha256']=sha(B/'build/fault');rows.append(row)
    (D/'manifest.json').write_text(json.dumps(rows,indent=2)+'\n');print(name,row['outcome'],flush=True)
