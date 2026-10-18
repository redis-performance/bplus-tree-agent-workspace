from pathlib import Path
import json,csv,statistics as st,math,hashlib
P=Path(__file__).resolve().parent;M=json.loads((P/'confirmation.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert M['status']=='complete' and len(M['runs'])==216 and sha(P/'CONFIRMATION-PLAN.md')==M['plan_sha256'];result=[]
for v in ['A','B','C']:
 cells=[]
 for cell in M['cells']:
  for seed in M['seeds']:
   rows=[]
   for run in M['runs']:
    if run['variant']!=v or run['cell']!=cell['name'] or run['seed']!=seed:continue
    for k in ['csv','stderr']:assert sha(P/run[k])==run[k+'_sha256']
    assert run['returncode']==0;r=list(csv.DictReader((P/run['csv']).open()));assert len(r)==1;r=r[0];r.update(block=run['block'],label=run['label']);rows.append(r)
   controls=len(rows)==12 and all(r['size']=='100000' and r['operations']=='20000000' and r['traversals']=='200' and r['seed']==str(seed) and r['direction']=='forward' and r['encoding']=='integer' and int(r['mask'])==cell['mask'] and r['member_bytes']=='16' and r['checksum']==r['expected_checksum'] and int(r['elapsed_ns'])>=10000000 for r in rows)
   controls &= all(len({r[k] for r in rows})==1 for k in ['checksum','tree_bytes','construction_fingerprint']);effects=[]
   for b in range(1,4):
    rr=[r for r in rows if r['block']==b];assert ''.join(r['label'] for r in rr)=='ABBA';vals={l:[int(r['elapsed_ns'])/int(r['operations']) for r in rr if r['label']==l] for l in 'AB'};effects.append(100*(st.mean(vals['B'])/st.mean(vals['A'])-1))
   mean=st.mean(effects);half=4.302652729911275*st.stdev(effects)/math.sqrt(3);cells.append(dict(cell=cell['name'],seed=seed,controls=controls,effects_pct=effects,mean_pct=mean,low_pct=mean-half,high_pct=mean+half,rows=rows))
 guards=[name for name in ['f-int16-m0','f-int16-m7'] if all(c['controls'] and c['low_pct']>1 for c in cells if c['cell']==name)]
 result.append(dict(variant=v,confirmed_guard_regressions=guards,decision='REJECT' if guards else 'PARK',cells=cells))
out=dict(status=M['status'],rows=len(M['runs']),decision='REJECT' if all(r['confirmed_guard_regressions'] for r in result) else 'PARK',selection='NONE',results=result);(P/'confirmation-summary.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# Fresh-seed guard confirmation','','216 fixed rows; wall time primary;3 ABBA blocks/seed;95% t df2. All rows retained.','Guard rejection requires lower bound>1% for BOTH fresh seeds;no tradeoff declared.','','| Variant | Mode | Seed | B/A mean % [95% interval] | Controls |','|---|---|---:|---|---|']
for r in result:
 for c in r['cells']:lines.append(f"| {r['variant']} | {c['cell']} | {c['seed']} | {c['mean_pct']:+.3f} [{c['low_pct']:+.3f},{c['high_pct']:+.3f}] | {c['controls']} |")
lines+=['',f"Decision: {out['decision']}; selection NONE. Same coordinator,not independent confirmation."]
(P/'CONFIRMATION.md').write_text('\n'.join(lines)+'\n');print(json.dumps({r['variant']:r['confirmed_guard_regressions'] for r in result},indent=2))
