from pathlib import Path
import json,csv,statistics as st,math,hashlib
R=Path(__file__).resolve().parents[2];O=R/'experiments/OVERNIGHT-2026-10-17';E=R/'experiments/EXP-004';checked=0
for D,manifest,summary,nblocks,t in [(O/'AA-007','manifest.json','summary.json',6,2.5705818366147395),(O/'AA-008','manifest.json','summary.json',6,2.5705818366147395),(E,'manifest.json','summary.json',3,4.302652729911275),(E,'confirmation.json','confirmation-summary.json',3,4.302652729911275),(O/'DIAG-011','manifest.json','summary.json',3,4.302652729911275)]:
 M=json.loads((D/manifest).read_text());S=json.loads((D/summary).read_text());groups={}
 for run in M['runs']:
  key=(run.get('variant'),run.get('seed'),run.get('cell'),run.get('caller'),run.get('mask'))
  # For DIAG the source variant is A/control, not population identity.
  if D.name=='DIAG-011':key=(None,run['seed'],None,run['caller'],run['mask'])
  row=next(csv.DictReader((D/run['csv']).open()));groups.setdefault(key,[]).append((run,int(row['elapsed_ns'])/int(row['operations'])))
 for key,rows in groups.items():
  vals=[]
  for block in range(1,nblocks+1):
   rr=[(r,x) for r,x in rows if r['block']==block];assert ''.join(r['label'] for r,x in rr)=='ABBA';a=[x for r,x in rr if r['label']=='A'];b=[x for r,x in rr if r['label']=='B'];vals.append(100*(st.mean(b)/st.mean(a)-1))
  mean=st.mean(vals);half=t*st.stdev(vals)/math.sqrt(nblocks)
  if D.name.startswith('AA-'):q=next(c for c in S if c['cell']==key[2]);wanted=[q['mean_pct'],q['ci95_low_pct'],q['ci95_high_pct']]
  elif D.name=='DIAG-011':q=next(c for c in S['results'] if (c['seed'],c['caller'],c['mask'])==(key[1],key[3],key[4]));wanted=[q['mean'],q['low'],q['high']]
  else:
   v=next(c for c in S['results'] if c['variant']==key[0]);q=next(c for c in v['cells'] if c['cell']==key[2] and (key[1] is None or c['seed']==key[1]));wanted=[q['mean_pct'],q['low_pct'],q['high_pct']]
  assert all(abs(a-b)<1e-10 for a,b in zip(wanted,[mean,mean-half,mean+half]));checked+=1
out=dict(status='pass',effect_intervals_recomputed_from_raw_rows=checked);(O/'ROUND-008-EFFECTS-AUDIT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
