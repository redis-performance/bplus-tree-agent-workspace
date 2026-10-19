from pathlib import Path
import subprocess,json,hashlib,shutil,difflib,resource,datetime
resource.setrlimit(resource.RLIMIT_CORE,(0,0))
r=Path.cwd();d=r/'scratch/amd-scan-faults';d.mkdir(exist_ok=False)
source=(r/'scratch/amd-scan-build/A/src/zset_btree.c').read_text()
mutations={
 'fold':('if (tag == 1)\n            equal = _mm_or_si128(equal, _mm_cmpeq_epi8(block, zero));','/* Deliberate fault: omit folded physical-zero matches. */'),
 'order':('unsigned int pos = base + (unsigned int)__builtin_ctz(mask);','unsigned int pos = base + 15U - (unsigned int)__builtin_ctz(mask);'),
 'tail':('unsigned int words = count / 8;\n    for (unsigned int w = base / 8;', 'if (base) return found; /* Deliberate fault: omit residual tags. */\n    unsigned int words = count / 8;\n    for (unsigned int w = base / 8;'),
 'aligned-load':('_mm_loadu_si128((const __m128i *)(tags + base))','_mm_load_si128((const __m128i *)(tags + base))')
}
records=[]
for name,(old,new) in mutations.items():
 assert source.count(old)==1,(name,source.count(old));changed=source.replace(old,new)
 p=d/name;p.mkdir();shutil.copytree(r/'scratch/amd-scan-build/A/src',p/'src');(p/'src/zset_btree.c').write_text(changed)
 (p/'tests').mkdir();shutil.copy(r/'scratch/amd-scan-input/all_match_guard_oracle_v2.c',p/'tests/all_match_guard_oracle.c')
 (p/'fault.patch').write_text(''.join(difflib.unified_diff(source.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
 for mode in ['native','san']:
  flags=['-O3'] if mode=='native' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
  cmd=['clang','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer',*flags,'-I'+str(p/'src'),'-Icompat','-Ivendor/redis',str(p/'tests/all_match_guard_oracle.c'),'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',str(p/mode)]
  b=subprocess.run(cmd,capture_output=True,text=True,timeout=30);(p/(mode+'-build.stdout')).write_text(b.stdout);(p/(mode+'-build.stderr')).write_text(b.stderr);b.check_returncode()
  start=datetime.datetime.now(datetime.timezone.utc).isoformat();x=subprocess.run([str(p/mode)],capture_output=True,text=True,timeout=30)
  (p/(mode+'.stdout')).write_text(x.stdout);(p/(mode+'.stderr')).write_text(x.stderr)
  records.append(dict(fault=name,mode=mode,start=start,end=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=x.returncode,detected=x.returncode!=0,source_sha256=hashlib.sha256(changed.encode()).hexdigest(),binary_sha256=hashlib.sha256((p/mode).read_bytes()).hexdigest()))
  (d/'results.json').write_text(json.dumps(records,indent=2)+'\n')
# Preserve all evidence even if a deliberately injected fault escapes.
assert all(x['detected'] for x in records),'undetected injected fault; inspect retained evidence'
