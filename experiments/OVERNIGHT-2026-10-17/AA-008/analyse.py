from pathlib import Path
import csv,json,statistics as st,math,hashlib
P=Path(__file__).resolve().parent;M=json.loads((P/'manifest.json').read_text());result=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for cell in M['cells']:
 rows=[];failures=[]
 for run in M['runs']:
  if run['cell']!=cell['name']:continue
  for k in ['csv','stderr']:assert sha(P/run[k])==run[k+'_sha256']
  if run['returncode']!=0:failures.append(run);continue
  data=list(csv.DictReader((P/run['csv']).open()));assert len(data)==1
  row=data[0];row.update(block=run['block'],label=run['label']);rows.append(row)
 effects=[]
 for b in range(1,7):
  ab={l:[int(r['elapsed_ns'])/int(r['operations']) for r in rows if r['block']==b and r['label']==l] for l in 'AB'}
  if all(len(v)==2 for v in ab.values()):effects.append(100*(st.mean(ab['B'])/st.mean(ab['A'])-1))
 invariant=len(rows)==24 and not failures and all(len({r[k] for r in rows})==1 for k in ['checksum','operations','tree_bytes','construction_fingerprint'])
 invariant &= all(int(r['size'])==100000 and int(r['operations'])==100000000 and int(r['traversals'])==1000 and r['seed']==str(cell['seed']) and r['direction']==cell['direction'] and r['encoding']==cell['encoding'] and int(r['mask'])==cell['mask'] and int(r['member_bytes'])==cell['bytes'] and r['checksum']==r['expected_checksum'] for r in rows)
 mean=st.mean(effects) if effects else None;half=2.5705818366147395*st.stdev(effects)/math.sqrt(6) if len(effects)==6 else None
 low,high=(mean-half,mean+half) if half is not None else (None,None)
 times=[int(r['elapsed_ns']) for r in rows];ns=[int(r['elapsed_ns'])/int(r['operations']) for r in rows];shares=[int(r['thread_elapsed_ns'])/int(r['elapsed_ns']) for r in rows if int(r['thread_elapsed_ns'])>=0]
 result.append(dict(cell=cell['name'],rows=len(rows),invariants=invariant,qualified=bool(invariant and low is not None and low>=-1 and high<=1 and min(times)>=10000000),effects_pct=effects,mean_pct=mean,ci95_low_pct=low,ci95_high_pct=high,median_ns_op=st.median(ns) if ns else None,min_wall_ms=min(times)/1e6 if times else None,thread_wall_min=min(shares) if shares else None,thread_wall_max=max(shares) if shares else None,cpu_ids=sorted({r[k] for r in rows for k in ['cpu_start','cpu_end']}),boundary_changes=sum(r['cpu_start']!=r['cpu_end'] for r in rows),qos=sorted({r[k] for r in rows for k in ['qos_reported_start','qos_reported_end']}),tree_bytes=sorted({r['tree_bytes'] for r in rows}),failures=failures))
(P/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
lines=['# AA-008 — wall-time precision','', 'Fixed six-block A/A; all rows retained. 95% t intervals assume independent normal block effects.','Frequency, effective QoS and within-window placement unknown. No source speed claim.','', '| Cell | Rows | B/A mean % [95% interval] | Qualified |','|---|---:|---|---|']
for r in result:lines.append(f"| {r['cell']} | {r['rows']} | {r['mean_pct']:+.3f} [{r['ci95_low_pct']:+.3f},{r['ci95_high_pct']:+.3f}] | {r['qualified']} |" if r['mean_pct'] is not None and r['ci95_low_pct'] is not None else f"| {r['cell']} | {r['rows']} | incomplete | False |")
(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(json.dumps(dict(status=M['status'],rows=len(M['runs']),qualified=sum(x['qualified'] for x in result),cells=len(result))))
