#!/usr/bin/env python3
from pathlib import Path
import subprocess,hashlib,json,csv,io,time,difflib
from datetime import datetime,timezone
ROOT=Path.cwd();OUT=Path(__file__).resolve().parents[1];LOG=OUT/'lookup-batch-logs';SCR=Path('scratch/m6-caller/harness-lookup');SCR.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
records=[];report=dict(status='RUNNING',participant='/root/followup_proposal_b',backend='Codex/GPT-6 family; exact serving model/token usage/monetary cost unknown',started_utc=utc(),commands=records,source_sha256=sha('src/zset_btree.c'),referees={n:sha(OUT/n) for n in ('lookup.c','batch.c')},semantic_rows=[],fault_controls=[])
def save():(OUT/'lookup-batch-validation.json').write_text(json.dumps(report,indent=2)+'\n')
def run(cmd,name,expect=0,marker=None):
 start=utc();t=time.monotonic();r=subprocess.run(list(map(str,cmd)),capture_output=True,text=True,timeout=120)
 for channel,data in [('stdout',r.stdout),('stderr',r.stderr)]:
  raw=SCR/(name+'.raw.'+channel);raw.write_text(data)
  data=data.replace(str(ROOT),'<workspace>');(LOG/(name+'.'+channel)).write_text(data)
 records.append(dict(name=name,command=[str(arg).replace(str(ROOT)+'/', '') for arg in cmd],cwd='workspace-root',started_utc=start,finished_utc=utc(),wall_seconds=time.monotonic()-t,returncode=r.returncode,stdout_sha256=sha(LOG/(name+'.stdout')),stderr_sha256=sha(LOG/(name+'.stderr'))));save()
 if expect is None:assert r.returncode!=0 and marker in r.stderr,(name,r.returncode)
 else:assert r.returncode==expect,(name,r.returncode)
 return r
base=['clang','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']
def build(kind,san=False,source=None,label=None):
 suf='-san' if san else '';label=label or kind+suf;flags=['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'] if san else ['-O3'];binary=SCR/label
 run([*base,*flags,'-Isrc','-Icompat','-Ivendor/redis',source or OUT/(kind+'.c'),'src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary],'build-'+label);return binary
try:
 for san in (False,True):
  suf='-san' if san else ''
  for kind in ('lookup','batch'):
   binary=build(kind,san);matrix=[]
   if kind=='lookup':
    for n in (100,1000,10000,100000,1000000):
     for case in ('lookup-hit','lookup-miss','lookup-mixed'):matrix.append((n,16,case,1,2003))
    for m in (8,16,319,320,321,1024):
     for case in ('lookup-hit','lookup-miss','lookup-mixed'):matrix.append((100,m,case,1,17))
   else:
    for batch in (1,16):
     for case in ('lookup-hit','lookup-miss','lookup-mixed'):
      for ops in (1,17,2003):matrix.append((10000,16,case,batch,ops))
   for idx,(n,m,case,batch,ops) in enumerate(matrix):
    cmd=[binary,'--size',str(n),'--member-bytes',str(m),'--case',case,'--ops',str(ops),'--seed','1','--warmup-passes','1']
    if kind=='batch':cmd+=['--batch-size',str(batch)]
    result=run(cmd,kind+suf+'-cell'+str(idx));rows=list(csv.DictReader(io.StringIO(result.stdout)));assert len(rows)==1;row=rows[0]
    assert row['case']==case and int(row['operations'])==ops and int(row['tree_bytes'])>0
    assert int(row['elapsed_ns'])>=0
    if kind=='batch':assert int(row['api_calls'])==(ops+batch-1)//batch
    report['semantic_rows'].append(dict(kind=kind,build='sanitizer' if san else 'native',size=n,member_bytes=m,case=case,batch=batch,ops=ops,checksum=row['checksum'],tree_bytes=row['tree_bytes'],status='PASS'));save()
   invalid=[['--case','bogus'],['--case','all'],['--size','0'],['--size','1000001'],['--ops','-1'],['--member-bytes','7'],['--member-bytes','65537'],['--seed'],['--unknown','1']]
   if kind=='batch':invalid += [['--batch-size','0'],['--batch-size','2'],['--batch-size','17']]
   for idx,args in enumerate(invalid):run([binary,*args],kind+suf+'-invalid'+str(idx),expect=2)
   print('validated',kind,suf or 'native',len(matrix),'cells',flush=True)
 faults=[('lookup','mixed-score','if (found) serverAssert(score == (double)query_order[i]);','if (found && c == 8) score += 1; if (found) serverAssert(score == (double)query_order[i]);','score == (double)query_order[i]'),('batch','missed-lane','unsigned found=zbtreeScores(tree,members,count,out+2);serverAssert(found==expected);','unsigned found=zbtreeScores(tree,members,count,out+2);found &= ~1U;serverAssert(found==expected);','found==expected'),('batch','mixed-score','if(verify)serverAssert(out[j+2]==(double)query[(offset+j)%n]);','if(verify && mode==2)out[j+2]+=1; if(verify)serverAssert(out[j+2]==(double)query[(offset+j)%n]);','out[j+2]==(double)query[(offset+j)%n]')]
 for kind,fault,old,new,marker in faults:
  original=(OUT/(kind+'.c')).read_text();assert original.count(old)==1;changed=original.replace(old,new);source=SCR/(kind+'-'+fault+'.c');source.write_text(changed)
  (LOG/(kind+'-'+fault+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/'+kind+'.c',tofile='b/'+kind+'.c')))
  for san in (False,True):
   label=kind+'-fault-'+fault+('-san' if san else '');binary=build(kind,san,source,label)
   cmd=[binary,'--case','lookup-mixed','--size','100','--ops','17','--seed','1','--member-bytes','16','--warmup-passes','1']
   if kind=='batch':cmd+=['--batch-size','16']
   r=run(cmd,label,expect=None,marker=marker);report['fault_controls'].append(dict(kind=kind,fault=fault,build='sanitizer' if san else 'native',detected=True,returncode=r.returncode,assertion=marker,source_sha256=sha(source)));save()
 report.update(status='PASS',finished_utc=utc(),binaries={p.name:sha(p) for p in SCR.iterdir() if p.is_file() and p.name in ('lookup','lookup-san','batch','batch-san')},notes='Bounded baseline semantic validation only. Incidental elapsed fields are not comparative performance evidence. All original references remain unchanged.');save()
except Exception as e:report.update(status='FAIL',finished_utc=utc(),error=repr(e));save();raise
print('lookup/batch validation and fault controls PASS',flush=True)
