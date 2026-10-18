from pathlib import Path
import json,csv,hashlib,statistics as st,math
P=Path(__file__).resolve().parent;M=json.loads((P/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert M['status']=='complete' and len(M['runs'])==144;assert sha(P/'PLAN.md')==M['plan_sha256'];rows=[]
for run in M['runs']:
 for k in ['csv','stderr']:assert sha(P/run[k])==run[k+'_sha256']
 assert run['returncode']==0;r=list(csv.DictReader((P/run['csv']).open()));assert len(r)==1;r=r[0];assert r['checksum']==r['expected_checksum'] and r['operations']=='100000000' and r['traversals']=='1000' and r['size']=='100000' and r['member_bytes']=='16' and r['encoding']=='integer' and r['direction']=='forward' and r['seed']==str(run['seed']) and r['mask']==str(run['mask']) and int(r['elapsed_ns'])>=10000000;rows.append(dict(run=run,data=r))
def interval(v):
 mean=st.mean(v);half=4.302652729911275*st.stdev(v)/math.sqrt(3);return dict(mean=mean,low=mean-half,high=mean+half,values=v)
results=[];interactions=[]
for seed in [14107,14143]:
 for mask in [4,6,7]:
  matching=[r for r in rows if r['run']['seed']==seed and r['run']['mask']==mask]
  assert all(len({r['data'][k] for r in matching})==1 for k in ['checksum','tree_bytes','construction_fingerprint'])
  effects={}
  for caller in ['dynamic','fixed']:
   values=[]
   for b in range(1,4):
    rr=[r for r in matching if r['run']['caller']==caller and r['run']['block']==b];assert ''.join(r['run']['label'] for r in rr)=='ABBA';v={l:[int(r['data']['elapsed_ns'])/int(r['data']['operations']) for r in rr if r['run']['label']==l] for l in 'AB'};values.append(100*(st.mean(v['B'])/st.mean(v['A'])-1))
   effects[caller]=values;results.append(dict(seed=seed,mask=mask,caller=caller,**interval(values)))
  d=interval([a-b for a,b in zip(effects['dynamic'],effects['fixed'])]);dynamic=interval(effects['dynamic']);d.update(seed=seed,mask=mask,support=dynamic['low']>1 and d['low']>max(1,.5*dynamic['mean']));interactions.append(d)
supported=all(r['support'] for r in interactions if r['mask']==6);out=dict(rows=144,controls=True,hypothesis_supported=supported,results=results,interactions=interactions,source_acceptance='PARK unchanged');(P/'summary.json').write_text(json.dumps(out,indent=2)+'\n');lines=['# Caller-context diagnostic','','Effects are descriptive in this altered caller;not source acceptance or A/A qualification.','All144rows and exact invariants retained.95%t intervals across3blocks.','','| Seed | Mask | Caller | A/control effect % [95%interval] |','|---|---|---|---|']
for r in results:lines.append(f"| {r['seed']} | {r['mask']} | {r['caller']} | {r['mean']:+.3f} [{r['low']:+.3f},{r['high']:+.3f}] |")
lines+=['','| Seed | Mask | Dynamic-minus-fixed % [95%interval] | Criterion |','|---|---|---|---|']
for r in interactions:lines.append(f"| {r['seed']} | {r['mask']} | {r['mean']:+.3f} [{r['low']:+.3f},{r['high']:+.3f}] | {r['support']} |")
lines+=['',f'Hypothesis supported on BOTH mask6seeds: {supported}. EXP-004 PARK unchanged.'];(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(json.dumps(out,indent=2))
