from pathlib import Path
import json,csv,hashlib,statistics as st,math
P=Path(__file__).resolve().parent;M=json.loads((P/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert M['status']=='complete' and len(M['runs'])==480;assert sha(P/'PLAN.md')==M['plan_sha256'];rows=[]
for run in M['runs']+M['warmups']:
 for k in ['csv','stderr']:assert sha(P/run[k])==run[k+'_sha256']
 assert run['returncode']==0;r=list(csv.DictReader((P/run['csv']).open()));assert len(r)==1;r=r[0];assert r['checksum']==r['expected_checksum'] and r['size']=='100000' and r['member_bytes']=='16' and r['encoding']=='integer' and r['direction']=='forward'
 if run in M['runs']:
  assert r['operations']=='20000000' and r['traversals']=='200' and r['seed']==str(run['seed']) and r['mask']==str(run['mask']) and int(r['elapsed_ns'])>=10000000;rows.append(dict(run=run,data=r))
def interval(v):
 mean=st.mean(v);half=2.5705818366147395*st.stdev(v)/math.sqrt(6);return dict(mean=mean,low=mean-half,high=mean+half,values=v)
results=[]
for seed in [19103,19139]:
 for target,mask in [(0,6)]+[(p,m) for p in [16,32,48] for m in [4,6,7]]:
  rr=[r for r in rows if r['run']['seed']==seed and r['run']['target']==target and r['run']['mask']==mask];assert len(rr)==24
  assert all(len({r['data'][k] for r in rr})==1 for k in ['checksum','tree_bytes','construction_fingerprint'])
  effects=[];thread=[]
  for b in range(1,7):
   br=[r for r in rr if r['run']['block']==b];assert ''.join(r['run']['label'] for r in br)=='ABBA'
   for metric,dst in [('elapsed_ns',effects),('thread_elapsed_ns',thread)]:
    v={l:[int(r['data'][metric])/int(r['data']['operations']) for r in br if r['run']['label']==l] for l in 'AB'};dst.append(100*(st.mean(v['B'])/st.mean(v['A'])-1))
  ci=interval(effects);results.append(dict(seed=seed,target=target,mask=mask,wall=ci,thread=interval(thread),aa_qualified=target==0 and ci['low']>=-1 and ci['high']<=1,boundary_migrations=sum(r['data']['cpu_start']!=r['data']['cpu_end'] for r in rr),cpu_ids=sorted({r['data'][k] for r in rr for k in ['cpu_start','cpu_end']}),reported_qos=sorted({r['data'][k] for r in rr for k in ['qos_reported_start','qos_reported_end']}),min_wall_ms=min(int(r['data']['elapsed_ns']) for r in rr)/1e6))
controls=[r for r in results if r['target']==0];primary=[r for r in results if r['target']==16 and r['mask']==6];qualified=all(r['aa_qualified'] for r in controls)
criterion=all(abs(r['wall']['mean'])>=2 and (r['wall']['low']>1 or r['wall']['high']<-1) for r in primary) and math.prod(r['wall']['mean'] for r in primary)>0
out=dict(rows=480,warmups=4,all_invariants=True,aa_qualified=qualified,primary_effect_criterion=criterion,hypothesis='SUPPORTED' if qualified and criterion else 'PARK' if not qualified else 'UNSUPPORTED',results=results,source_acceptance='EXP-004 PARK unchanged');(P/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# Controlled placement diagnostic','','Wall effects: placement/0 minus1;95%t(df5) intervals across six ABBA block means.','Intervals assume independent approximately normal block effects; neither assumption is proven.','All480rows and4prospectivewarmups retained;no exclusions. Thread effects descriptive only.','','| Seed | Offset | Mask | Wall effect % [95% interval] | A/A qualified |','|---|---|---|---|---|']
for r in results:
 c=r['wall'];lines.append(f"| {r['seed']} | {r['target']} | {r['mask']} | {c['mean']:+.3f} [{c['low']:+.3f},{c['high']:+.3f}] | {r['aa_qualified'] if r['target']==0 else 'n/a'} |")
lines+=['',f"Primary hypothesis: {out['hypothesis']}. Both A/A controls qualify: {qualified}; preselected16-byte effect criterion: {criterion}.",'EXP-004 remains PARK; these placements do not qualify the original source comparator.'];(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'}));print('\n'.join(lines[-3:]));print(json.dumps(primary,indent=2))
