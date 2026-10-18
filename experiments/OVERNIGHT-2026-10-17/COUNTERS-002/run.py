import csv,hashlib,json,os,subprocess
from pathlib import Path
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-counters-002';B=S/'base';binary=B/'build/btree-bench'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
F=json.loads((P/'freeze.json').read_text())
for name,h in F['files'].items():assert sha(B/name)==h
assert not (P/'manifest.json').exists();m={'binary_sha256':sha(binary),'plan_sha256':sha(P/'PLAN.md'),'freeze_sha256':sha(P/'freeze.json'),'runs':[]}
for cell in ['AS','BS','AI','BI']:
 out=P/cell;out.mkdir();raw=S/f'{cell}.profraw';data=S/f'{cell}.profdata';export=S/f'{cell}.json'
 args=['--case','lookup-hit','--size','100000','--ops','1000000','--member-bytes','320','--seed','211','--warmup-passes','10','--fixture-order','ascending' if cell[0]=='A' else 'shuffled','--query-order','coupled' if cell[1]=='S' else 'independent']
 with (out/'bench.csv').open('w') as so,(out/'bench.stderr').open('w') as se:
  p=subprocess.run([str(binary),*args],cwd=R,env=dict(os.environ,LLVM_PROFILE_FILE=str(raw)),stdout=so,stderr=se,timeout=120)
 row=dict(cell=cell,command=[str(binary.relative_to(R)),*args],returncode=p.returncode,raw=str(raw.relative_to(R)),runs=[])
 m['runs'].append(row);(P/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');assert p.returncode==0 and raw.exists()
 for step,cmd in enumerate([['xcrun','llvm-profdata','merge','-sparse',str(raw),'-o',str(data)],['xcrun','llvm-cov','export',str(binary),'-instr-profile='+str(data)]]):
  with (out/f'tool{step}.stderr').open('w') as se,(export if step else out/'merge.stdout').open('w') as so:q=subprocess.run(cmd,stdout=so,stderr=se,timeout=120)
  row['runs'].append({'command':[a.replace(str(R),'<workspace>') for a in cmd],'returncode':q.returncode});assert q.returncode==0
 report=json.loads(export.read_text());functions=[f for d in report['data'] for f in d['functions']]
 counts={f['name']:f['count'] for f in functions}
 def count(name):return sum(v for k,v in counts.items() if k==name or k.endswith(':'+name))
 bench=next(csv.DictReader((out/'bench.csv').open()))
 assertions={'lookup_count':count('zbtreeScore')==int(bench['operations'])==1000000,'no_insert':count('zbtreeInsertNew')==0,'no_delete':count('zbtreeDelete')==0}
 tree=[{k:f[k] for k in ['name','count','regions','branches']} for f in functions if any(x.endswith('/src/zset_btree.c') for x in f['filenames'])]
 tree.sort(key=lambda f:f['name']);canonical=json.dumps(tree,sort_keys=True,separators=(',',':'))
 (out/'tree-counts.json').write_text(json.dumps(tree,indent=2)+'\n')
 (out/'function-counts.json').write_text(json.dumps({k:v for k,v in sorted(counts.items()) if v},indent=2)+'\n')
 row.update(assertions=assertions,raw_sha256=sha(raw),data_sha256=sha(data),export_sha256=sha(export),tree_counts_sha256=hashlib.sha256(canonical.encode()).hexdigest(),outputs={f.name:sha(f) for f in out.iterdir() if f.is_file()})
 (P/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');assert all(assertions.values());print(cell,'PASS',flush=True)
for name,h in F['files'].items():assert sha(B/name)==h
m['binary_sha256_after']=sha(binary);assert m['binary_sha256_after']==m['binary_sha256']
paired={a:next(r['tree_counts_sha256'] for r in m['runs'] if r['cell']==a+'S')==next(r['tree_counts_sha256'] for r in m['runs'] if r['cell']==a+'I') for a in 'AB'}
m.update(status='complete',paired_tree_counts_identical=paired);(P/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');print(paired)
