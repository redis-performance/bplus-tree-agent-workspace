from pathlib import Path
import csv,json,hashlib,statistics as st
P=Path(__file__).resolve().parent;R=P.parents[2];m=json.loads((P/'manifest.json').read_text());assert m['status']=='complete' and len(m['runs'])==24
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(P/'PLAN.md')==m['plan_sha256']
results=[];allrows=[]
for size,miss in [(16,0),(16,1),(320,0),(320,1)]:
 processes=[];memory=set();fps=set();cellrows=[]
 for run in m['runs']:
  if (run['member_bytes'],run['miss'])!=(size,miss):continue
  assert run['returncode']==0 and sha(P/run['csv'])==run['csv_sha256'] and sha(P/run['stderr'])==run['stderr_sha256']
  rows=list(csv.DictReader((P/run['csv']).open()));assert len(rows)==16
  for w,r in enumerate(rows):
   assert int(r['window'])==w and r['windows']=='16' and r['size']=='100000' and r['operations']=='500000'
   assert r['seed']=='1301' and r['query_seed']=='1409' and r['member_bytes']==str(size)
   assert r['case']==('lookup-miss' if miss else 'lookup-hit')
   assert int(r['checksum'])==int(r['expected'])==(0 if miss else 24999750000)
   assert r['qos_effective']=='unknown' and r['warmup_passes']=='10'
   memory.add(r['tree_bytes']);fps.add((r['construction_fingerprint'],r['query_fingerprint']))
  vals=[int(r['elapsed_ns'])/500000 for r in rows]
  outer=int(rows[0]['outer_elapsed_ns']);gap=int(rows[0]['gap_ns'])
  assert outer==sum(int(r['elapsed_ns']) for r in rows)+gap and gap>=0
  assert len({(r['outer_elapsed_ns'],r['gap_ns']) for r in rows})==1
  ratio=st.mean(vals[:4])/st.mean(vals[-4:])
  processes.append(dict(block=run['block'],first_last_ratio=ratio,wall_ns_op=vals,thread_ns_op=[int(r['thread_elapsed_ns'])/500000 for r in rows],cpu_pairs=[(int(r['cpu_start']),int(r['cpu_end'])) for r in rows],qos_pairs=[(r['qos_reported_start'],r['qos_reported_end']) for r in rows],gap_fraction=gap/outer,outer_ns=outer,mean_ns_op=st.mean(vals),cv=st.stdev(vals)/st.mean(vals)))
  cellrows+=rows
 assert len(processes)==6 and len(memory)==1 and len(fps)==1
 ratios=[p['first_last_ratio'] for p in processes];control=all(p['gap_fraction']<=.01 for p in processes) and min(int(r['elapsed_ns']) for r in cellrows)>=10000000
 supported=control and st.median(ratios)>=1.03 and sum(x>1 for x in ratios)>=5
 results.append(dict(member_bytes=size,case='lookup-miss' if miss else 'lookup-hit',rows=len(cellrows),controls=control,phase_criterion_met=supported,ratios=ratios,median_ratio=st.median(ratios),direction_count=sum(x>1 for x in ratios),tree_bytes=int(next(iter(memory))),min_wall_ns=min(int(r['elapsed_ns']) for r in cellrows),max_gap_fraction=max(p['gap_fraction'] for p in processes),cpu_boundary_changes=sum(r['cpu_start']!=r['cpu_end'] for r in cellrows),thread_wall_ratios=[int(r['thread_elapsed_ns'])/int(r['elapsed_ns']) for r in cellrows],position_mean_ns_op=[st.mean(p['wall_ns_op'][w] for p in processes) for w in range(16)],processes=processes))
 allrows+=cellrows
out=dict(rows=len(allrows),processes=24,hypothesis_supported=all(r['controls'] for r in results) and sum(r['phase_criterion_met'] for r in results)>=2,cells=results)
(P/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# DIAG-007 phase results','','All384 windows retained. Wall time primary; no independent-window confidence interval.','','| Cell | First/last median ratio | Ratios >1 | Controls | Phase criterion |','|---|---:|---:|---|---|']
for r in results:lines.append(f"| {r['case']}/{r['member_bytes']} | {r['median_ratio']:.6f} | {r['direction_count']}/6 | {r['controls']} | {r['phase_criterion_met']} |")
lines+=['',f"Fixed overall hypothesis supported: {out['hypothesis_supported']}.",'All per-process ratios,16-position means, CPU pairs, thread durations and gap fractions are in summary.json.','Boundary CPU IDs are opaque; no filtering, core-type or clock inference. No source precision qualification.']
(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
