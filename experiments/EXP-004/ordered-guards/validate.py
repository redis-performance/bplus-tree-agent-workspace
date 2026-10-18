from pathlib import Path
import subprocess,json,hashlib,time,csv,itertools,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
for v in ['A','B','C']:
 D=P/v/'validation';D.mkdir();rows=[];F=json.loads((P/v/'freeze.json').read_text());S=R/F['snapshot']
 def run(name,cmd):
  out=D/(name+'.stdout');err=D/(name+'.stderr');started=utc()
  with out.open('w') as so,err.open('w') as se:
   try:q=subprocess.run(cmd,cwd=S,stdout=so,stderr=se,timeout=120);rc=q.returncode
   except subprocess.TimeoutExpired:rc='timeout'
  row=dict(name=name,command=cmd,returncode=rc,started_utc=started,ended_utc=utc(),stdout=str(out.relative_to(P/v)),stderr=str(err.relative_to(P/v)),stdout_sha256=sha(out),stderr_sha256=sha(err));rows.append(row);(P/v/'validation.json').write_text(json.dumps(rows,indent=2)+'\n');assert rc==0,name
  return out
 for kind in ['release','sanitize']:
  (S/f'build/{kind}').mkdir(parents=True)
  flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']+(['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'])
  common=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags];support=['src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm']
  run(kind+'-build',common+['bench/iterator_modes.c',*support,'-o',f'build/{kind}/iterator-modes'])
  run(kind+'-upstream-build',common+['-DREDIS_TEST','-DREDIS_DEBUG','tests/upstream.c',*support,'-o',f'build/{kind}/upstream'])
  run(kind+'-upstream',[f'build/{kind}/upstream'])
  for oracle in ['packed_decode_oracle','zero_physical_oracle']:
   run(kind+'-'+oracle+'-build',common+['-DREDIS_DEBUG',f'tests/{oracle}.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',f'build/{kind}/{oracle}'])
   run(kind+'-'+oracle,[f'build/{kind}/{oracle}'])
  cells=list(itertools.product([97,513],[16,320],['integer','alternating-zero'],['shuffled','ascending','descending'],['forward','reverse'],[0,4,6,7]));assert len(cells)==192
  for i,(n,b,e,c,d,m) in enumerate(cells):
   out=run(f'{kind}-{i:03d}',[f'build/{kind}/iterator-modes','--size',str(n),'--ops',str(n*2+1),'--member-bytes',str(b),'--encoding',e,'--construction',c,'--direction',d,'--mask',str(m),'--seed','31013'])
   data=list(csv.DictReader(out.open()));assert len(data)==1;r=data[0];assert int(r['operations'])==3*n and r['traversals']=='3' and r['checksum']==r['expected_checksum'] and r['construction']==c
  print(v,kind,'192fixtures/original/packed/zero PASS',flush=True)
 for name,h in F['files'].items():assert sha(S/name)==h
 (P/v/'binaries.json').write_text(json.dumps({k:sha(S/f'build/{k}/iterator-modes') for k in ['release','sanitize']},indent=2)+'\n')
