from pathlib import Path
import json,csv,hashlib,statistics as st,math
P=Path(__file__).resolve().parent;R=P.parents[1];M=json.loads((P/'manifest.json').read_text());AA=json.loads((R/'experiments/OVERNIGHT-2026-10-17/AA-009/summary.json').read_text());qual={r['cell']:r['qualified'] for r in AA};sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(P/'PLAN.md')==M['plan_sha256'];results=[]
for v in ['A','B','C']:
 cells=[]
 for cell in M['cells']:
  rows=[]
  for run in M['runs']:
   if run['variant']!=v or run['cell']!=cell['name']:continue
   for k in ['csv','stderr']:assert sha(P/run[k])==run[k+'_sha256']
   assert run['returncode']==0;data=list(csv.DictReader((P/run['csv']).open()));assert len(data)==1;row=data[0];row.update(block=run['block'],label=run['label']);rows.append(row)
  controls=len(rows)==12 and all(r['size']=='100000' and r['operations']=='20000000' and r['traversals']=='200' and r['seed']=='20101' and r['direction']==cell['direction'] and r['encoding']==cell['encoding'] and int(r['mask'])==cell['mask'] and int(r['member_bytes'])==cell['bytes'] and r['checksum']==r['expected_checksum'] and int(r['elapsed_ns'])>=10000000 for r in rows)
  controls &= all(len({r[k] for r in rows})==1 for k in ['checksum','operations','tree_bytes','construction_fingerprint'])
  effects=[]
  for b in range(1,4):
   rr=[r for r in rows if r['block']==b];assert ''.join(r['label'] for r in rr)=='ABBA';ns={l:[int(r['elapsed_ns'])/int(r['operations']) for r in rr if r['label']==l] for l in 'AB'};effects.append(100*(st.mean(ns['B'])/st.mean(ns['A'])-1))
  mean=st.mean(effects);half=4.302652729911275*st.stdev(effects)/math.sqrt(3)
  cells.append(dict(cell=cell['name'],qualified=qual.get(cell['name'],False),controls=controls,mean_pct=mean,low_pct=mean-half,high_pct=mean+half,effects_pct=effects,demonstrated_regression=bool(qual.get(cell['name'],False) and controls and mean-half>1),rows=rows))
 primary=next(c for c in cells if c['cell']=='f-int16-m4');regress=[c['cell'] for c in cells if c['demonstrated_regression']]
 results.append(dict(variant=v,cells=cells,primary_pass=primary['qualified'] and primary['controls'] and primary['high_pct']<=-2,regressed_guards=regress,eligible=not regress and all(c['controls'] for c in cells) and primary['high_pct']<=-2 and all(c['high_pct']<=1 for c in cells if c['qualified'] and c['cell']!='f-int16-m4')))
passing=[r for r in results if r['eligible']];winner='NONE'
if passing:
 primary=lambda r:next(c for c in r['cells'] if c['cell']=='f-int16-m4')
 best=min(passing,key=lambda r:primary(r)['mean_pct']);bc=primary(best)
 overlap=[r for r in passing if primary(r)['low_pct']<=bc['high_pct'] and primary(r)['high_pct']>=bc['low_pct']]
 winner=min(overlap,key=lambda r:len((P/'variants'/r['variant']/'candidate.patch').read_bytes()))['variant']
out=dict(status=M['status'],rows=len(M['runs']),expanded_preference=winner,acceptance='PARK',results=results);(P/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# EXP-005 width-mask screening','','All rows retained; wall time primary. 95% t intervals across3 ABBA blocks (df2).','Unqualified modes diagnostic only. Frequency/effective QoS/within-window residency unknown.','','| Variant | Mode | Qualified | Mean B/A % [95% interval] | Controls | Demonstrated regression |','|---|---|---|---|---|---|']
for r in results:
 for c in r['cells']:lines.append(f"| {r['variant']} | {c['cell']} | {c['qualified']} | {c['mean_pct']:+.3f} [{c['low_pct']:+.3f},{c['high_pct']:+.3f}] | {c['controls']} | {c['demonstrated_regression']} |")
lines+=['',f'Expanded preference: {winner}. No source acceptance.'];(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(json.dumps({r['variant']:dict(primary_pass=r['primary_pass'],regressed_guards=r['regressed_guards'],eligible=r['eligible']) for r in results},indent=2))
