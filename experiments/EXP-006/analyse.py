from pathlib import Path
import ast,csv,hashlib,json,math,statistics,sys
P=Path(__file__).resolve().parent;R=P.parents[1];phase=sys.argv[1];D=P/'bench-results'/phase;M=json.loads((D/'manifest.json').read_text());assert M['status']=='complete';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(P/'PLAN.md')==M['plan_sha256']
T=ast.parse((R/'experiments/OVERNIGHT-2026-10-17/HARNESS-007/attempt-002/validate.py').read_text());scope={'mask':(1<<64)-1}
for name in ['draw','permutation']:
 f=next(n for n in T.body if isinstance(n,ast.FunctionDef) and n.name==name);exec(compile(ast.Module(body=[f],type_ignores=[]),'<fixture-model>','exec'),scope)
expected_rows=len(M['variants'])*len(M['cells'])*len(M['seeds'])*M['blocks']*4;assert len(M['runs'])==expected_rows
rows=[]
for r in M['runs']:
 assert r['returncode']==0
 for key in ['csv','stderr']:assert sha(D/r[key])==r[key+'_sha256']
 v=next(csv.DictReader((D/r['csv']).open()));row=dict(r,value=v);rows.append(row)
tcrit=4.302652729911275 if M['blocks']==3 else 2.570581835636305
results=[]
for variant in M['variants']:
 for cell in M['cells']:
  for seed,qseed in M['seeds']:
   rs=[r for r in rows if r['variant']==variant and r['cell']==cell['name'] and r['seed']==seed];assert len(rs)==M['blocks']*4
   q,qfp=scope['permutation'](8192,qseed,0);_,cfp=scope['permutation'](8192,seed,16);layout=cell['layout']
   hits=[i for i in range(2000000) if layout=='hit' or (layout=='mixed' and i%2==0)];checksum=sum(q[i%8192]+1 for i in hits)
   owned=set();effects=[];thread=[];control=[];candidate=[]
   for r in rs:
    v=r['value'];want=dict(size=8192,operations=2000000,requested_ops=2000000,member_bytes=cell['bytes'],batch_size=cell['batch'],seed=seed,query_seed=qseed,api_calls=(2000000+cell['batch']-1)//cell['batch'],hits=len(hits),checksum=checksum,construction_fingerprint=cfp,query_fingerprint=qfp,elapsed_zero=0,warmup_passes=3)
    for k,x in want.items():assert int(v[k])==x,(r['name'],k)
    assert v['case']==layout and int(v['elapsed_ns'])>=10000000;owned.add(int(v['tree_bytes']));(control if r['label']=='A' else candidate).append(int(v['elapsed_ns'])/2000000)
   assert len(owned)==1
   for block in range(1,M['blocks']+1):
    b=[r for r in rs if r['block']==block];assert ''.join(r['label'] for r in b)=='ABBA'
    for key,dest in [('elapsed_ns',effects),('thread_elapsed_ns',thread)]:
     x=[int(r['value'][key]) for r in b];assert min(x)>0;dest.append(100*((x[1]+x[2])/(x[0]+x[3])-1))
   def ci(x):
    avg=statistics.mean(x);half=tcrit*statistics.stdev(x)/math.sqrt(len(x));return dict(effects=x,mean=avg,low=avg-half,high=avg+half)
   results.append(dict(variant=variant,cell=cell['name'],seed=seed,query_seed=qseed,wall_percent=ci(effects),thread_percent=ci(thread),tree_bytes=owned.pop(),control_ns_per_member=statistics.mean(control),candidate_ns_per_member=statistics.mean(candidate)))
quality={};means={}
for v in M['variants']:
 primary=[r for r in results if r['variant']==v and r['cell']=='mixed16-b16'];guard=[r for r in results if r['variant']==v and r['cell']=='hit320-b16'];means[v]=statistics.mean(r['wall_percent']['mean'] for r in primary);quality[v]=all(r['wall_percent']['high']<=-2 for r in primary) and all(r['wall_percent']['high']<=1 for r in guard)
choice='NONE'
if phase=='screen':
 eligible=[v for v in M['variants'] if quality[v]]
 if eligible:choice=min(eligible,key=lambda v:(len((P/'variants'/v/'candidate.patch').read_bytes()),means[v]))
 elif min(means.values())<0:choice=min(means,key=means.get)
out=dict(phase=phase,rows=expected_rows,status='complete',results=results,passes_primary_and_qualified_guard=quality,primary_mean_percent=means,confirmation_choice=choice if phase=='screen' else M['variants'],source_selection='NONE',acceptance='blocked by unqualified original/additional guards, independent review and committed provenance')
(D/'summary.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))
