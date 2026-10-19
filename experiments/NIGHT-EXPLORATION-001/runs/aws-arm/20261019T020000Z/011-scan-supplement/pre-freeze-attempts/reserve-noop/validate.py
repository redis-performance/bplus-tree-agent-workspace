#!/usr/bin/env python3
"""Standalone supplement validation only: all passes zero, no timing clocks."""
from pathlib import Path
import argparse,subprocess,json,hashlib,time,datetime,itertools,struct
p=argparse.ArgumentParser();p.add_argument('--native',required=True,type=Path);p.add_argument('--sanitize',required=True,type=Path);p.add_argument('--out',required=True,type=Path);p.add_argument('--seconds',type=int,default=600);a=p.parse_args();o=a.out.resolve();o.mkdir(exist_ok=False,parents=True);start=time.monotonic();rows=[];fixtures=[];cells=[]
def run(cmd,label,expected=0,needle=None):
 remaining=a.seconds-(time.monotonic()-start);assert remaining>0
 began=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run([str(x)for x in cmd],capture_output=True,text=True,timeout=min(60,remaining));ended=datetime.datetime.now(datetime.timezone.utc).isoformat();(o/(label+'.stdout')).write_text(r.stdout);(o/(label+'.stderr')).write_text(r.stderr);rows.append(dict(label=label,command=[str(x)for x in cmd],start_utc=began,end_utc=ended,returncode=r.returncode,expected_returncode=expected));(o/'commands.json').write_text(json.dumps(rows,indent=2)+'\n');assert r.returncode==expected,(label,r.returncode,r.stderr)
 if needle:assert needle in r.stderr,(label,r.stderr,needle)
 return [json.loads(x)for x in r.stdout.splitlines()] if expected==0 and label not in ['native-upstream','sanitize-upstream'] else []
for mode,b in [('native',a.native),('sanitize',a.sanitize)]:run([b/'upstream-test'],mode+'-upstream')
for history,width,encoding,seed in itertools.product(['trim','resize'],[8,319,320,321,1024],[0,1,2],[201,202,203]):
 n=7169 if history=='resize' else 7 if width==319 else 31;name=f'{history}-b{width}-e{encoding}-s{seed}';h=hashlib.sha256()
 for i in range(n):
  key=i.to_bytes(8,'big')+bytes((i*37+seed*13+j*19)&255 for j in range(8,width))
  if width>8:key=key[:8]+b'\0'+key[9:]
  score=i+0.25 if encoding==0 else 0.25 if encoding==1 else -0.0 if i&1 else 0.0
  h.update(key);h.update(struct.pack('>d',score))
 fixtures.append(dict(cell=name,n=n,width=width,encoding=encoding,seed=seed,live_model_sha256=h.hexdigest(),hash_input='ascending exact binary key bytes followed by big-endian IEEE754 score bits per member'))
 for mode,b in [('native',a.native),('sanitize',a.sanitize)]:
  d=run([b/'scan-census','run',history,width,seed,encoding,0,0],name+'-'+mode+'-census');assert len(d)==2;c,r=d
  assert c['members']==n and sum(c['tag_histogram'])==n and c['full16_members']==c['full16_chunks']*16
  if history=='trim':assert c['leaves']==1 and c['reversed_members']==n and c['reversed_leaves']==1 and c['reversed_full16_chunks']==n//16
  else:assert c['active_rehash'] and c['old_live']>0 and 0<c['new_live']<n/2 and c['old_live']+c['new_live']==n
  assert c['wide_old']==c['wide_new']==0
  if width==8:assert c['short_records']==n and c['external']==c['long_records']==0
  elif width==319:assert c['long_records']==n and c['external']==c['short_records']==c['full16_chunks']==0
  else:assert c['external']==n and c['short_records']==c['long_records']==0
  actual=run([b/'scan-supplement','run',history,width,seed,encoding,0,0],name+'-'+mode+'-public')[0];assert actual==r,(name,mode,actual,r)
  assert r['elapsed_ns']==0 and r['thread_elapsed_ns']==0 and r['passes']==0
  cells.append(dict(cell=name,build=mode,census=c,run=r));(o/'cells.json').write_text(json.dumps(cells,indent=2)+'\n')
(o/'fixture-model-manifest.json').write_text(json.dumps(fixtures,indent=2)+'\n')
for mode,b in [('native',a.native),('sanitize',a.sanitize)]:
 for fault,needle in [(1,'bits(d) == bits(score(id, o->mode))'),(2,'len == o->width'),(3,'o.seen[id]'),(4,'!memcmp(s, o->keys[id], len)'),(7,'bits(d) == bits(score(id, o->mode))')]:run([b/'scan-supplement','run','trim',321,201,2,0,fault],f'fault-{mode}-{fault}',2,needle)
 run([b/'scan-census','run','trim',321,201,2,0,5],f'fault-{mode}-5',2,'before.reversed_members == n')
 run([b/'scan-census','run','resize',321,201,2,0,6],f'fault-{mode}-6',2,'before.rehash')
 run([b/'scan-census','run','trim',321,201,2,1,0],f'fault-{mode}-timing-refusal',2,'passes == 0')
(o/'RESULT.json').write_text(json.dumps({'status':'pass','commands':len(rows),'fixture_cells':len(fixtures),'census_cells':len(cells),'source_builds':['native','ASan+UBSan'],'original_tests_per_build':43,'oracle_faults_detected':10,'structural_faults_detected':4,'census_timing_refusals':2,'baseline_timing_windows':0,'candidate_timings':0,'seconds':time.monotonic()-start},indent=2)+'\n')
