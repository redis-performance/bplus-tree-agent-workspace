from pathlib import Path
import datetime,difflib,hashlib,json,shutil,subprocess,re
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/experiment006-scalar-fallback-round020';F=json.loads((P.parent/'tag-guard/manifest.json').read_text())
assert not S.exists();S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
M=dict(status='preparing',plan_sha256=sha(P/'PLAN.md'),driver_sha256=sha(Path(__file__)),parent_manifest_sha256=sha(P.parent/'tag-guard/manifest.json'),snapshots={},runs=[],binaries={},preprocessing={})
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(tag,args,B,private_out=False):
 if datetime.datetime.now(datetime.timezone.utc)>=datetime.datetime.fromisoformat('2026-10-18T06:27:00+00:00'):M['status']='budget-exhausted';save();raise SystemExit(3)
 out=B/(tag+'.raw.stdout') if private_out else P/(tag+'.stdout');raw=B/(tag+'.raw.stderr');err=P/(tag+'.stderr')
 r=dict(name=tag,command=args,cwd=str(B.relative_to(R)),started_utc=utc())
 with out.open('w') as o,raw.open('w') as e:
  try:rc=subprocess.run(args,cwd=B,stdout=o,stderr=e,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 err.write_text(raw.read_text().replace(str(R),'<workspace>'))
 r.update(returncode=rc,ended_utc=utc(),stdout=str(out.relative_to(R)),stdout_sha256=sha(out),stderr=str(err.relative_to(R)),stderr_sha256=sha(err),raw_stderr=str(raw.relative_to(R)),raw_stderr_sha256=sha(raw));M['runs'].append(r);save();return rc,out,err
header='''#define _DARWIN_C_SOURCE 1
#define _GNU_SOURCE 1
#include "../compat/server.h"
#include "../src/zset_btree.h"
#include <math.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>
#include <inttypes.h>
#include <sys/mman.h>
#include <unistd.h>
#ifdef FORCE_SCALAR_TAG_FALLBACK
#pragma push_macro("__BYTE_ORDER__")
#undef __BYTE_ORDER__
#endif
'''
footer='''
#ifdef FORCE_SCALAR_TAG_FALLBACK
#pragma pop_macro("__BYTE_ORDER__")
#endif
'''
common=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG']
for v in ['control','A','B','C']:
 d=F['snapshots'][v];B=S/v;B.mkdir()
 for n,h in d['files'].items():
  src=R/d['path']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 for oracle in ['tag_search_oracle.c','tag_guard_oracle.c']:
  (B/'tests'/('fallback_'+oracle)).write_text(header+'#include "'+oracle+'"\n'+footer)
 M['snapshots'][v]=dict(path=str(B.relative_to(R)),files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()});(B/'build').mkdir();save()
 for oracle in ['tag_search_oracle.c','tag_guard_oracle.c']:
  src='tests/fallback_'+oracle;outputs=[]
  for config in ['native','forced']:
   tag=v+'-'+oracle+'-preprocess-'+config
   rc,out,err=run(tag,common+(['-DFORCE_SCALAR_TAG_FALLBACK'] if config=='forced' else [])+['-E','-P',src],B,True);assert rc==0;outputs.append(out.read_text())
  pat=r'static inline uint8_t \*zbtInlineTagSearch\([^\n]+\{.*?\n\}'
  if v in ['B','C']:
   helpers=[re.search(pat,x,re.S).group(0) for x in outputs]
   assert outputs[0].replace(helpers[0],'HELPER')==outputs[1].replace(helpers[1],'HELPER')
   forced=helpers[1];assert 'while (n--)' in forced and all(x not in forced for x in ['memcpy','matches','ctz'])
   (P/(v+'-'+oracle+'-forced-helper.c.txt')).write_text(forced+'\n')
  else:assert outputs[0]==outputs[1]
  M['preprocessing'][v+'-'+oracle]='PASS exact text equality except B/C helper';save()
 M['frozen_'+v]=utc();save()
 for kind in ['native','sanitize']:
  flags=['-O3'] if kind=='native' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
  for oracle,field,count in [('tag_search_oracle.c','tagchecks',1585152),('tag_guard_oracle.c','guardchecks',198144)]:
   tag=v+'-'+kind+'-'+oracle;binary='build/'+kind+'-'+oracle[:-2]
   cmd=common+['-DFORCE_SCALAR_TAG_FALLBACK']+flags+['tests/fallback_'+oracle,'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
   rc,_,_=run(tag+'-build',cmd,B);assert rc==0
   M['binaries'][str((B/binary).relative_to(R))]=sha(B/binary);save()
   rc,out,_=run(tag+'-run',[binary],B);assert rc==0 and out.read_text().startswith('PASS '+field+'='+str(count)+' ')
   print(tag,'PASS',flush=True)
for oracle in ['tag_search_oracle.c','tag_guard_oracle.c']:
 rows=[r for r in M['runs'] if r['name'].endswith(oracle+'-run')];assert len(rows)==8
 assert len({(R/r['stdout']).read_text() for r in rows})==1
M.update(status='normal-complete',normal_complete_utc=utc());save()
# Fixed sensitivity control, source deliberately modified only in its scalar arm.
d=M['snapshots']['C'];B=S/'fault';B.mkdir()
for n,h in d['files'].items():
 src=R/d['path']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
(B/'build').mkdir();source=B/'src/zset_btree.c';old=source.read_text();needle='    while (n--) { if (*p == tag) return p; p++; }';assert old.count(needle)==1
new=old.replace(needle,'    if (!n) { volatile uint8_t byte = *p; (void)byte; } /* deliberate zero-span read */\n'+needle);source.write_text(new)
(P/'zero-span-read.patch').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
M['snapshots']['fault']=dict(path=str(B.relative_to(R)),files={n:sha(B/n) for n in d['files']});save()
cmd=common+['-DFORCE_SCALAR_TAG_FALLBACK','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all','tests/fallback_tag_guard_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/fault']
rc,_,_=run('fault-build',cmd,B);assert rc==0;M['binaries'][str((B/'build/fault').relative_to(R))]=sha(B/'build/fault');save()
rc,_,err=run('fault-run',['build/fault'],B)
M['fault_outcome']='detected' if isinstance(rc,int) and rc!=0 and ('AddressSanitizer' in err.read_text() or 'runtime error:' in err.read_text()) else ('SURVIVED' if rc==0 else 'inconclusive')
for d in M['snapshots'].values():
 for n,h in d['files'].items():assert sha(R/d['path']/n)==h
M.update(status='complete',ended_utc=utc());save();print('COMPLETE',M['fault_outcome'],flush=True)
