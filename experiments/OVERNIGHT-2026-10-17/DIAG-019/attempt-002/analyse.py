from pathlib import Path
import ast,csv,hashlib,json,math,statistics,sys
P=Path(__file__).resolve().parent;R=P.parents[3];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();scope={'mask':(1<<64)-1}
T=ast.parse((R/'experiments/OVERNIGHT-2026-10-17/HARNESS-007/attempt-002/validate.py').read_text())
for name in ['draw','permutation']:
 f=next(n for n in T.body if isinstance(n,ast.FunctionDef) and n.name==name);exec(compile(ast.Module(body=[f],type_ignores=[]),'<independent-fixture-model>','exec'),scope)
def ci(x):
 avg=statistics.mean(x);half=2.570581835636305*statistics.stdev(x)/math.sqrt(len(x));return dict(effects=x,mean=avg,low=avg-half,high=avg+half)
phase=sys.argv[1];D=P/phase;M=json.loads((D/'manifest.json').read_text());assert M['status']=='complete' and len(M['runs'])==192
assert sha(P/'PLAN.md')==M['plan_sha256'] and sha(P/'run.py')==M['runner_sha256'];rows=[];checksums={};memory={}
for seed,qseed in M['seeds']:
 q,qfp=scope['permutation'](8192,qseed,0);_,cfp=scope['permutation'](8192,seed,16);cycles,tail=divmod(2000000,8192);checksums[seed]=(cycles*sum(x+1 for x in q)+sum(x+1 for x in q[:tail]),qfp,cfp)
for r in M['runs']:
 assert r['returncode']==0
 for key in ['stdout','stderr']:assert sha(R/r[key])==r[key+'_sha256']
 values=list(csv.DictReader((R/r['stdout']).open()));assert len(values)==1;v=values[0];checksum,qfp,cfp=checksums[r['seed']]
 want=dict(size=8192,operations=2000000,requested_ops=2000000,member_bytes=16,batch_size=r['batch'],seed=r['seed'],query_seed=r['query_seed'],api_calls=(2000000+r['batch']-1)//r['batch'],hits=2000000,checksum=checksum,query_fingerprint=qfp,construction_fingerprint=cfp,warmup_passes=3,elapsed_zero=0)
 for k,x in want.items():assert int(v[k])==x,(r['name'],k,v[k],x)
 assert v['case']=='hit';memory.setdefault(r['seed'],set()).add(int(v['tree_bytes']));rows.append(dict(r,value=v))
assert all(len(x)==1 for x in memory.values());results=[]
for placement,batch in M['cells']:
 for seed,qseed in M['seeds']:
  rs=[r for r in rows if r['placement']==placement and r['batch']==batch and r['seed']==seed];assert len(rs)==24;effects={k:[] for k in ['elapsed_ns','thread_elapsed_ns']}
  for block in range(1,7):
   b=[r for r in rs if r['block']==block];assert ''.join(r['label'] for r in b)=='ABBA' and [r['step'] for r in b]==[1,2,3,4]
   for k,x in effects.items():
    t=[int(r['value'][k]) for r in b];assert min(t)>0;x.append(100*((t[1]+t[2])/(t[0]+t[3])-1))
  wall=ci(effects['elapsed_ns']);thread=ci(effects['thread_elapsed_ns']);durations=all(int(r['value']['elapsed_ns'])>=10000000 for r in rs)
  rates={label:dict(ns_per_member=statistics.mean(int(r['value']['elapsed_ns'])/2000000 for r in rs if r['label']==label),members_per_second=statistics.mean(2000000*1e9/int(r['value']['elapsed_ns']) for r in rs if r['label']==label)) for label in 'AB'}
  results.append(dict(placement=placement,batch=batch,seed=seed,query_seed=qseed,wall_percent=wall,thread_percent=thread,duration_pass=durations,aa_qualifies=durations and wall['low']>=-1 and wall['high']<=1,rates=rates,tree_bytes=next(iter(memory[seed])),bytes_per_member=next(iter(memory[seed]))/8192,observed_cpu_boundaries=sorted({(r['value']['cpu_start'],r['value']['cpu_end']) for r in rs}),reported_qos=sorted({r['value']['qos_reported_start'] for r in rs})))
interactions=[]
if phase!='aa':
 for seed,qseed in M['seeds']:
  by={(x['placement'],x['batch']):x['wall_percent']['effects'] for x in results if x['seed']==seed};on=[a-b for a,b in zip(by['on',1],by['on',16])];off=[a-b for a,b in zip(by['off',1],by['off',16])];interaction=[a-b for a,b in zip(on,off)];a,b,c=ci(on),ci(off),ci(interaction)
  interactions.append(dict(seed=seed,query_seed=qseed,on_batch_gap_points=a,off_batch_gap_points=b,interaction_points=c,passes_interaction=a['low']>=2 and c['low']>=1 and b['mean']<=.5*a['mean']))
out=dict(phase=phase,rows=len(rows),all_invariants_pass=True,all_durations_pass=all(x['duration_pass'] for x in results),results=results,interactions=interactions,joint_aa_qualifies=all(x['aa_qualifies'] for x in results) if phase=='aa' else None,source_selection='NONE',provenance='uncommitted diagnostic snapshots; no adoption')
(D/'summary.json').write_text(json.dumps(out,indent=2)+'\n');print(phase,'rows',len(rows),'AA qualified',sum(x['aa_qualifies'] for x in results) if phase=='aa' else 'not applicable','interactions',[x['passes_interaction'] for x in interactions])
if phase=='confirm':
 aa=json.loads((P/'aa/summary.json').read_text());dis=json.loads((P/'discovery/summary.json').read_text());supported=aa['joint_aa_qualifies'] and all(x['passes_interaction'] for x in dis['interactions']+interactions) and dis['all_durations_pass'] and out['all_durations_pass'];(P/'decision.json').write_text(json.dumps(dict(supported=supported,decision='local attenuation supported, still diagnostic only' if supported else 'criterion unsupported; PARK causal claim',source_selection='NONE',rows=576,aa_joint=aa['joint_aa_qualifies'],discovery=dis['interactions'],confirmation=interactions),indent=2)+'\n')
