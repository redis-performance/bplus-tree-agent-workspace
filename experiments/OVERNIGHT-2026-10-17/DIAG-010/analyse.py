from pathlib import Path
import csv,json,hashlib,statistics as st
P=Path(__file__).resolve().parent;m=json.loads((P/'manifest.json').read_text());results=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(P/'PLAN.md')==m['plan_sha256'] and sha(P/'run.py')==m['runner_sha256']
complete=m['status']=='complete' and len(m['runs'])==96
for cell,case,size,ops in m['cells']:
 rows=[];failures=[]
 for run in m['runs']:
  if run['cell']!=cell:continue
  for k in ['csv','stderr']:assert sha(P/run[k])==run[k+'_sha256']
  if run['returncode']!=0:failures.append(run);continue
  rr=list(csv.DictReader((P/run['csv']).open()));assert len(rr)==1
  row=rr[0];row.update(block=run['block'],label=run['label'],step=run['step']);rows.append(row)
 controls=len(rows)==24 and not failures
 for r in rows:
  expected=(ops//100000)*100000*99999//2 if case=='lookup-hit' else 0
  controls &= all([r['case']==case,r['seed']=='3001',r['query_seed']=='3209',r['query_order']=='independent',int(r['size'])==100000,int(r['operations'])==ops,int(r['member_bytes'])==size,int(r['checksum'])==expected,int(r['elapsed_ns'])>=10000000,r['qos_reported_start']==r['qos_reported_end']==('user-interactive' if r['label']=='A' else 'user-initiated'),r['qos_relpri_start']==r['qos_relpri_end']=='0',r['qos_effective']=='unknown',r['warmup_case']==case,r['warmup_passes']=='10'])
 controls &= all(len({r[k] for r in rows})==1 for k in ['tree_bytes','construction_fingerprint','query_fingerprint'])
 blocks=[]
 for b in range(1,7):
  rr=[r for r in rows if r['block']==b];assert ''.join(r['label'] for r in rr)=='ABBA'
  a=[int(r['elapsed_ns'])/ops for r in rr if r['label']=='A'];bb=[int(r['elapsed_ns'])/ops for r in rr if r['label']=='B']
  da=abs(a[0]-a[1])/st.mean(a);db=abs(bb[0]-bb[1])/st.mean(bb)
  blocks.append(dict(block=b,A_ns_op=a,B_ns_op=bb,dA=da,dB=db,mean_contrast_pct=100*(st.mean(bb)/st.mean(a)-1)))
 da=st.median(b['dA'] for b in blocks);db=st.median(b['dB'] for b in blocks);directions=sum(b['dB']<b['dA'] for b in blocks)
 criterion=controls and da>0 and db<=.5*da and directions>=5 and db<=.01
 results.append(dict(cell=cell,controls=controls,criterion=criterion,median_dA=da,median_dB=db,improved_blocks=directions,blocks=blocks,rows=rows,failures=failures))
out=dict(status=m['status'],rows=sum(len(r['rows']) for r in results),hypothesis_supported=complete and all(r['controls'] for r in results) and results[0]['criterion'],cells=results)
(P/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# DIAG-010 results','','Wall-time repeat distances, same binary with requested-QoS intervention. All rows retained.','','| Cell | Median dA | Median dB | Smaller B | Controls | Criterion |','|---|---:|---:|---:|---|---|']
for r in results:lines.append(f"| {r['cell']} | {r['median_dA']:.6f} | {r['median_dB']:.6f} | {r['improved_blocks']}/6 | {r['controls']} | {r['criterion']} |")
lines+=['',f"Primary hypothesis supported: {out['hypothesis_supported']}.",'All raw wall/thread times, IDs, QoS, bytes and checksums retained in raw/ and summary.json.','No source speedup, core/frequency attribution or A/A qualification. A/B are QoS arms, not source candidates.']
(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
