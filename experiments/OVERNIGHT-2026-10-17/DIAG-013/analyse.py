from pathlib import Path
import json,csv,hashlib,statistics as st,math
P=Path(__file__).resolve().parent;M=json.loads((P/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();results=[]
assert M['status']=='complete' and len(M['runs'])==192
for c in M['cells']:
 for seed in M['seeds']:
  for policy,passes in M['policies'].items():
   rows=[]
   for run in M['runs']:
    if (run['cell'],run['seed'],run['policy'])!=(c['name'],seed,policy):continue
    assert run['returncode']==0
    for k in ['csv','stderr']:assert sha(P/run[k])==run[k+'_sha256']
    data=list(csv.DictReader((P/run['csv']).open()));assert len(data)==1
    row=data[0];row.update(block=run['block'],label=run['label']);rows.append(row)
   invariant=len(rows)==24 and all(len({r[k] for r in rows})==1 for k in ['checksum','operations','tree_bytes','construction_fingerprint'])
   invariant &= all(int(r['size'])==95 and int(r['operations'])==20000065 and int(r['traversals'])==210527 and r['seed']==str(seed) and r['direction']==c['direction'] and r['encoding']==c['encoding'] and r['construction']==c['construction'] and int(r['mask'])==c['mask'] and int(r['member_bytes'])==c['bytes'] and r['checksum']==r['expected_checksum'] and int(r['warmup_passes'])==passes for r in rows)
   effects={};intervals={}
   for metric in ['elapsed_ns','thread_elapsed_ns']:
    e=[]
    for block in range(1,7):
     ab={arm:[int(r[metric])/int(r['operations']) for r in rows if r['block']==block and r['label']==arm] for arm in 'AB'}
     assert all(len(x)==2 and min(x)>0 for x in ab.values());e.append(100*(st.mean(ab['B'])/st.mean(ab['A'])-1))
    mean=st.mean(e);half=2.5705818366147395*st.stdev(e)/math.sqrt(6);effects[metric]=e;intervals[metric]=[mean,mean-half,mean+half]
   ci=intervals['elapsed_ns'];wall=[int(r['elapsed_ns']) for r in rows]
   results.append(dict(cell=c['name'],seed=seed,policy=policy,invariants=invariant,effects_pct=effects,intervals=intervals,qualified=bool(invariant and ci[1]>=-1 and ci[2]<=1 and min(wall)>=10000000),min_wall_ms=min(wall)/1e6,warmup_ms=[int(r['warmup_elapsed_ns'])/1e6 for r in rows],tree_bytes=sorted({r['tree_bytes'] for r in rows}),checksum=rows[0]['checksum'],fingerprint=rows[0]['construction_fingerprint'],cpu_ids=sorted({r[k] for r in rows for k in ['cpu_start','cpu_end']}),boundary_changes=sum(r['cpu_start']!=r['cpu_end'] for r in rows),qos=sorted({r[k] for r in rows for k in ['qos_reported_start','qos_reported_end']})))
contrasts=[]
for c in M['cells']:
 for seed in M['seeds']:
  pair={r['policy']:r for r in results if r['cell']==c['name'] and r['seed']==seed};a=pair['short'];b=pair['long']
  assert all(a[k]==b[k] for k in ['tree_bytes','checksum','fingerprint'])
  contrasts.append(dict(cell=c['name'],seed=seed,short_bias_pct=a['intervals']['elapsed_ns'][0],long_bias_pct=b['intervals']['elapsed_ns'][0],halved=abs(b['intervals']['elapsed_ns'][0])<=.5*abs(a['intervals']['elapsed_ns'][0])))
valid=all(r['invariants'] and r['min_wall_ms']>=10 for r in results);short_all=all(r['qualified'] for r in results if r['policy']=='short');long_all=all(r['qualified'] for r in results if r['policy']=='long');halved=sum(r['halved'] for r in contrasts)
status='inconclusive' if short_all else 'supported' if valid and long_all and halved>=3 else 'unsupported'
result=dict(status=status,invariants=valid,short_all_qualified=short_all,long_all_qualified=long_all,pairs_bias_halved=halved,results=results,contrasts=contrasts)
(P/'summary.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='results'},indent=2));assert valid
