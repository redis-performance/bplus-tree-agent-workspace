from pathlib import Path
import json,csv,hashlib,statistics as st,math
P=Path(__file__).resolve().parent;R=P.parents[2];m=json.loads((P/'manifest.json').read_text());assert m['status']=='complete' and len(m['runs'])==48
results=[]
for size,ops in [(16,10000000),(320,5000000)]:
 rows=[];invariants=True
 for run in m['runs']:
  if run['member_bytes']!=size:continue
  assert hashlib.sha256((P/run['csv']).read_bytes()).hexdigest()==run['csv_sha256']
  assert hashlib.sha256((R/run['stderr']).read_bytes()).hexdigest()==run['stderr_sha256']
  data=list(csv.DictReader((P/run['csv']).open()));assert len(data)==1;r=data[0]
  profile=list(csv.reader((R/run['stderr']).open()));head=[x for x in profile if x[0]=='PROFILE'];pc=[x for x in profile if x[0]=='PC']
  assert len(head)==1 and head[0][1]=='lookup-hit' and head[0][2]==run['profile_usec'] and head[0][4]=='0' and int(head[0][3])==len(pc)
  assert r['query_seed']=='1201' and r['seed']=='1103' and r['query_order']=='independent' and int(r['operations'])==ops and int(r['checksum'])==ops*99999//2
  invariants &= len(pc)==0 if run['label']=='A' else len(pc)>=50
  rows.append(dict(r,block=run['block'],label=run['label'],slot=run['slot'],samples=len(pc),ns_op=int(r['elapsed_ns'])/ops))
 invariants &= all(len({r[k] for r in rows})==1 for k in ['tree_bytes','checksum','operations','construction_fingerprint','query_fingerprint'])
 effects=[]
 for block in range(1,7):
  rr=[r for r in rows if r['block']==block];assert ''.join(r['label'] for r in rr)=='ABBA'
  effects.append(100*(st.mean(r['ns_op'] for r in rr if r['label']=='B')/st.mean(r['ns_op'] for r in rr if r['label']=='A')-1))
 mean=st.mean(effects);half=2.5705818366147395*st.stdev(effects)/math.sqrt(6);lo=mean-half;hi=mean+half;min_ns=min(int(r['elapsed_ns']) for r in rows)
 results.append(dict(member_bytes=size,rows=24,block_effects_pct=effects,mean_pct=mean,ci95_low_pct=lo,ci95_high_pct=hi,invariants=bool(invariants),min_wall_ns=min_ns,sample_counts=[r['samples'] for r in rows],criterion_met=bool(invariants) and min_ns>=100000000 and lo>=-5 and hi<=5))
(P/'summary.json').write_text(json.dumps(results,indent=2)+'\n')
lines=['# DIAG-006 descriptive sampler perturbation','','Off/on same executable; all fixed48 rows retained. Wall time primary.','No source acceptance or unbiased sample-fraction claim. Clock/effective QoS/residency unknown.','','| Member bytes | Rows | On/off mean effect % [95% t interval] | Controls | Fixed bound met |','|---|---:|---|---|---|']
for r in results:lines.append(f"| {r['member_bytes']} | {r['rows']} | {r['mean_pct']:+.3f} [{r['ci95_low_pct']:+.3f}, {r['ci95_high_pct']:+.3f}] | {r['invariants']} | {r['criterion_met']} |")
lines+=['',f"Both-cell bounded-perturbation criterion: {all(r['criterion_met'] for r in results)}."]
(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
