from pathlib import Path
import json,csv,hashlib,statistics as st,math
P=Path(__file__).resolve().parent;m=json.loads((P/'manifest.json').read_text());assert m['status']=='complete' and len(m['runs'])==72
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(P/'PLAN.md')==m['plan_sha256'];results=[]
for v in ['A','B','C']:
 cells=[]
 for size in [16,320]:
  rows=[]
  for run in m['runs']:
   if run['variant']!=v or run['member_bytes']!=size:continue
   for k in ['csv','stderr']:assert sha(P/run[k])==run[k+'_sha256']
   assert run['returncode']==0;rr=list(csv.DictReader((P/run['csv']).open()));assert len(rr)==1;r=rr[0];r.update(block=run['block'],label=run['label']);rows.append(r)
  controls=len(rows)==12 and all(r['case']=='iterate' and r['size']=='100000' and r['operations']=='50000000' and r['checksum']=='2499975000000' and r['member_bytes']==str(size) and r['seed']=='4109' and r['query_seed']=='4201' and r['query_order']=='independent' and r['traversals']=='500' and int(r['elapsed_ns'])>=10000000 for r in rows)
  controls &= all(len({r[k] for r in rows})==1 for k in ['tree_bytes','construction_fingerprint','query_fingerprint'])
  effects=[]
  for b in range(1,4):
   rr=[r for r in rows if r['block']==b];assert ''.join(r['label'] for r in rr)=='ABBA'
   vals={l:[int(r['elapsed_ns'])/int(r['operations']) for r in rr if r['label']==l] for l in 'AB'}
   effects.append(100*(st.mean(vals['B'])/st.mean(vals['A'])-1))
  mean=st.mean(effects);half=4.302652729911275*st.stdev(effects)/math.sqrt(3)
  cells.append(dict(member_bytes=size,controls=controls,mean_pct=mean,low_pct=mean-half,high_pct=mean+half,effects_pct=effects,rows=rows))
 eligible=all(c['controls'] for c in cells) and cells[0]['high_pct']<=-2 and cells[1]['high_pct']<=1
 results.append(dict(variant=v,screen_pass=eligible,cells=cells))
passing=[r for r in results if r['screen_pass']]
winner='NONE'
if passing:
 best=min(passing,key=lambda r:r['cells'][0]['mean_pct']);bc=best['cells'][0]
 overlap=[r for r in passing if r['cells'][0]['low_pct']<=bc['high_pct'] and r['cells'][0]['high_pct']>=bc['low_pct']]
 winner=min(overlap,key=lambda r:len((P/'variants'/r['variant']/'candidate.patch').read_bytes()))['variant']
out=dict(rows=72,screen_winner=winner,results=results,acceptance='PENDING' if passing else 'NONE')
(P/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# EXP-002 implementation screening','','Three sequential implementations; no independent agents. All72 observations retained.','','| Variant | Member bytes | B/A mean % [95% interval] | Controls | Screen pass |','|---|---:|---|---|---|']
for r in results:
 for c in r['cells']:lines.append(f"| {r['variant']} | {c['member_bytes']} | {c['mean_pct']:+.3f} [{c['low_pct']:+.3f},{c['high_pct']:+.3f}] | {c['controls']} | {r['screen_pass']} |")
lines+=['',f'Screen winner: {winner}. No source accepted.','Reverse/full-output guards, fresh confirmation, matched profiles, independent review and commit review remain required.']
(P/'bench-results/SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
