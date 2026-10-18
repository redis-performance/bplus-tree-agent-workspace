from pathlib import Path
import json,hashlib,shutil,subprocess,datetime,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'manifest.json').read_text());S=R/'scratch/overnight-counters-006-trace';assert not S.exists();S.mkdir();D=P/'trace';D.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();M=dict(status='preparing',plan_sha256=sha(P/'TRACE-PLAN.md'),sources={},runs=[])
def save():(D/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
for policy,desc in F['snapshots'].items():
 B=S/policy;B.mkdir()
 for n,h in desc['files'].items():
  src=R/desc['path']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 p=B/'src/zset_btree.c';original=p.read_text();a='    if (zmalloc_usable_size(leaf) >=\n        2 * zbtScoreLeafLiveBytes(leaf) + ZBT_SCORE_LEAF_RESERVE)';assert original.count(a)==1
 s=original.replace(a,'    fprintf(stderr,"COMPACT_CHECK count=%u reversed=%u usable=%zu live=%zu reserve=%u decision=%d\\n",leaf->n.count,leaf->reversed,zmalloc_usable_size(leaf),zbtScoreLeafLiveBytes(leaf),(unsigned)ZBT_SCORE_LEAF_RESERVE,zmalloc_usable_size(leaf)>=2*zbtScoreLeafLiveBytes(leaf)+ZBT_SCORE_LEAF_RESERVE);\n'+a);p.write_text(s)
 (D/(policy+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
 p=B/'tests/diagnostic.c';s=p.read_text().split('int main(void) {')[0]
 s=s.replace('        mix(&layout_hash,leaf->n.count);','        fprintf(stderr,"STATE check=%"PRIu64" n=%u reversed=%u usable=%zu live=%zu bits=%u shift=%u\\n",checks,leaf->n.count,leaf->reversed,zmalloc_usable_size(leaf),zbtScoreLeafLiveBytes(leaf),leaf->score_bits,leaf->n.score_shift);\n        mix(&layout_hash,leaf->n.count);')
 s+='int main(void) {fprintf(stderr,"FIXTURE n6 bytes320\\n");exercise(6,320,0,31121);fprintf(stderr,"FIXTURE n7 bytes16\\n");exercise(7,16,0,31121);serverAssert(checks==49 && exact==1567);}\n';p.write_text(s)
 M['sources'][policy]={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()};(B/'build').mkdir()
M['status']='frozen';save()
for policy,desc in F['snapshots'].items():
 B=S/policy
 for san in ['native','sanitize']:
  flags=[] if san=='native' else ['-fsanitize=address,undefined','-fno-sanitize-recover=all'];name=policy+'-'+san
  cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O1','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG',f'-DCAPACITY_QUANTUM={desc["quantum"]}',*flags,'tests/diagnostic.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+san]
  for stage,args in [('build',cmd),('run',['build/'+san])]:
   label=name+'-'+stage;row=dict(name=label,command=args,started_utc=utc())
   with (D/(label+'.stdout')).open('w') as out,(D/(label+'.stderr')).open('w') as err:
    try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
    except subprocess.TimeoutExpired:rc='timeout'
   row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(D/(label+'.stdout')),stderr_sha256=sha(D/(label+'.stderr')));M['runs'].append(row);save();assert rc==0,label
  M.setdefault('binaries',{})[name]=sha(B/'build'/san);save()
for policy,files in M['sources'].items():
 for n,h in files.items():assert sha(S/policy/n)==h
M['status']='complete';save();print('Six trace cells pass')
