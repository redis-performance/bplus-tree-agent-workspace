from pathlib import Path
import ast,csv,hashlib,json,math,statistics
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'manifest.json').read_text());assert M['status']=='complete' and len(M['runs'])==240
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(P/'PLAN.md')==M['plan_sha256'];assert sha(R/M['binary'])==M['binary_sha256']==M['binary_sha256_after']
T=ast.parse((P.parent/'HARNESS-007/attempt-002/validate.py').read_text());scope={'mask':(1<<64)-1}
for name in ['draw','permutation']:
 node=next(n for n in T.body if isinstance(n,ast.FunctionDef) and n.name==name);exec(compile(ast.Module(body=[node],type_ignores=[]),'<independent-fixture-model>','exec'),scope)
rows=[]
for r in M['runs']:
 assert r['returncode']==0
 for file in ['csv','stderr']:assert sha(P/r[file])==r[file+'_sha256']
 v=list(csv.DictReader((P/r['csv']).open()));assert len(v)==1;v=v[0];assert int(v['elapsed_zero'])==0
 row=dict(r);row['value']=v;rows.append(row)
def interval(values):
 avg=statistics.mean(values);half=2.570581835636305*statistics.stdev(values)/math.sqrt(6)
 return dict(effects=values,mean=avg,low=avg-half,high=avg+half)
results=[]
for c in M['cells']:
 for seed,qseed in M['seeds']:
  subset=[r for r in rows if r['cell']==c['name'] and r['seed']==seed];assert len(subset)==24
  q,qfp=scope['permutation'](8192,qseed,0);_,cfp=scope['permutation'](8192,seed,16)
  ix=[i for i in range(2000000) if c['layout']=='hit' or (c['layout']=='mixed' and i%2==0)];expected=sum(q[i%8192]+1 for i in ix)
  memory=set();effects=[];thread=[];minwall=min(int(r['value']['elapsed_ns']) for r in subset)
  for block in range(1,7):
   rs=[r for r in subset if r['block']==block];assert ''.join(r['label'] for r in rs)=='ABBA' and [r['step'] for r in rs]==[1,2,3,4]
   for r in rs:
    v=r['value'];want=dict(size=8192,requested_ops=2000000,operations=2000000,member_bytes=c['bytes'],seed=seed,query_seed=qseed,batch_size=c['batch'],api_calls=(2000000+c['batch']-1)//c['batch'],hits=len(ix),checksum=expected,warmup_passes=3,construction_fingerprint=cfp,query_fingerprint=qfp)
    for k,x in want.items():assert int(v[k])==x,(r['name'],k,v[k],x)
    assert v['case']==c['layout'] and v['qos_effective']=='unknown';memory.add(int(v['tree_bytes']))
   for key,target in [('elapsed_ns',effects),('thread_elapsed_ns',thread)]:
    values=[int(r['value'][key]) for r in rs];assert min(values)>0
    target.append(100*((values[1]+values[2])/(values[0]+values[3])-1))
  assert len(memory)==1
  wall=interval(effects);qual=wall['low']>=-1 and wall['high']<=1 and minwall>=10000000
  results.append(dict(cell=c['name'],seed=seed,query_seed=qseed,decision='QUALIFIED' if qual else 'PARK',wall_percent=wall,thread_percent=interval(thread),min_wall_ns=minwall,tree_bytes=memory.pop(),median_ns_per_member=statistics.median(int(r['value']['elapsed_ns'])/2000000 for r in subset)))
joint={c['name']:all(r['decision']=='QUALIFIED' for r in results if r['cell']==c['name']) for c in M['cells']}
out=dict(status='complete',rows=240,results=results,joint_qualified=joint,source_selection='NONE',limitations='Local unpinned M1; frequency/effective QoS/migration unknown; independent block assumption; new fixtures cannot replace original unresolved guards.')
(P/'summary.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(joint_qualified=joint,results=[dict(cell=r['cell'],seed=r['seed'],decision=r['decision'],low=r['wall_percent']['low'],high=r['wall_percent']['high']) for r in results]),indent=2))
