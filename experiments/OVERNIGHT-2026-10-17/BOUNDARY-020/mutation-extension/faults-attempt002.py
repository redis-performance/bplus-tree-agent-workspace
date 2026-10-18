from pathlib import Path
import datetime,difflib,hashlib,json,shutil,subprocess
P=Path(__file__).resolve().parent/'attempt-002';R=P.parents[4];M=json.loads((P/'manifest.json').read_text());assert M['status']=='complete'
desc=M['snapshots']['control'];base=R/desc['path'];D=P/'faults';D.mkdir();S=R/'scratch/overnight-boundary-020-mutation-faults';assert not S.exists();S.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
original=(base/'src/zset_btree.c').read_text()
old='zs->member_rehash->table.buckets = zbtDefragPlainAllocation(';assert original.count(old)==1
lost=original.replace(old,'(void)zbtDefragPlainAllocation(')
begin=original.index('int zbtreeDefragStep(');end=original.index('/* -------------------------- Lookup',begin)
part=original[begin:end];old='zs->score_first ? zs->score_first->id : ZBT_NO_LEAF_ID;';assert part.count(old)==2
first=part.index(old);second=part.index(old,first+len(old))
part=part[:second]+'ZBT_NO_LEAF_ID;'+part[second+len(old):]
skipped=original[:begin]+part+original[end:];rows=[]
for name,changed in [('lost-relocated-resize-buckets',lost),('skip-retired-defrag-cursor',skipped)]:
    B=S/name;shutil.copytree(base,B,ignore=shutil.ignore_patterns('build'));(B/'build').mkdir()
    for n,h in desc['files'].items():assert sha(B/n)==h
    (B/'src/zset_btree.c').write_text(changed);(D/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
    row=dict(name=name,snapshot=str(B.relative_to(R)),source_sha256=sha(B/'src/zset_btree.c'),runs=[])
    cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O1','-Wall','-Wextra','-Werror','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all','tests/active_resize_mutation_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/fault']
    for stage,args in [('build',cmd),('run',['build/fault'])]:
        tag=name+'-'+stage;r=dict(stage=stage,command=args,cwd=str(B.relative_to(R)),started_utc=utc())
        with (D/(tag+'.stdout')).open('w') as out,(D/(tag+'.stderr')).open('w') as err:
            try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
            except subprocess.TimeoutExpired:rc='timeout'
        r.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(D/(tag+'.stdout')),stderr_sha256=sha(D/(tag+'.stderr')));row['runs'].append(r)
        (D/'manifest.json').write_text(json.dumps(rows+[row],indent=2)+'\n');assert rc==0 if stage=='build' else isinstance(rc,int) and rc!=0
    assert any(x in (D/(name+'-run.stderr')).read_text() for x in ['active-resize-defrag','AddressSanitizer']);row['detected']=True;row['binary_sha256']=sha(B/'build/fault');rows.append(row)
    (D/'manifest.json').write_text(json.dumps(rows,indent=2)+'\n');print(name,'DETECTED',flush=True)
