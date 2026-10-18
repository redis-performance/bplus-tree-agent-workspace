from pathlib import Path
import csv,json,hashlib,statistics as st
P=Path(__file__).resolve().parent;R=P.parents[2];m=json.loads((P/'manifest.json').read_text());assert m['status']=='complete' and len(m['runs'])==48
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(P/'PLAN.md')==m['plan_sha256'];results=[];global_controls=True
for size in [16,320]:
 processes=[];memory=set();fps=set();cellrows=[]
 for run in m['runs']:
  if run['member_bytes']!=size:continue
  assert run['returncode']==0 and sha(P/run['csv'])==run['csv_sha256'] and sha(P/run['stderr'])==run['stderr_sha256']
  rows=list(csv.DictReader((P/run['csv']).open()));assert len(rows)==16
  for w,r in enumerate(rows):
   assert int(r['window'])==w and r['windows']=='16' and r['size']=='100000' and r['operations']=='500000'
   assert r['seed']=='1723' and r['query_seed']=='1861' and r['member_bytes']==str(size)
   assert r['case']=='lookup-miss' and int(r['checksum'])==int(r['expected'])==0
   assert r['qos_effective']=='unknown' and r['warmup_passes']=='10'
   assert r['warmup_case']==('lookup-hit' if run['label']=='A' else 'lookup-miss')
   memory.add(r['tree_bytes']);fps.add((r['construction_fingerprint'],r['query_fingerprint']))
  vals=[int(r['elapsed_ns'])/500000 for r in rows];outer=int(rows[0]['outer_elapsed_ns']);gap=int(rows[0]['gap_ns'])
  assert outer==sum(int(r['elapsed_ns']) for r in rows)+gap and gap>=0
  assert len({(r['outer_elapsed_ns'],r['gap_ns']) for r in rows})==1
  ratio=st.mean(vals[:4])/st.mean(vals[-4:])
  processes.append(dict(block=run['block'],slot=run['slot'],label=run['label'],first_last_ratio=ratio,wall_ns_op=vals,first_mean=st.mean(vals[:4]),last_mean=st.mean(vals[-4:]),thread_ns_op=[int(r['thread_elapsed_ns'])/500000 for r in rows],cpu_pairs=[(int(r['cpu_start']),int(r['cpu_end'])) for r in rows],qos_pairs=[(r['qos_reported_start'],r['qos_reported_end']) for r in rows],gap_fraction=gap/outer,mean_ns_op=st.mean(vals),warmup_elapsed_ns=int(rows[0]['warmup_elapsed_ns'])))
  cellrows+=rows
 assert len(processes)==24 and len(memory)==len(fps)==1
 blocks=[]
 for b in range(1,7):
  rr=[p for p in processes if p['block']==b];assert ''.join(p['label'] for p in rr)=='ABBA'
  a=st.mean(p['first_last_ratio'] for p in rr if p['label']=='A');bb=st.mean(p['first_last_ratio'] for p in rr if p['label']=='B')
  blocks.append(dict(block=b,pA=a,pB=bb,contrast=a/bb))
 contrasts=[b['contrast'] for b in blocks];bs=[b['pB'] for b in blocks]
 control=all(p['gap_fraction']<=.01 for p in processes) and min(int(r['elapsed_ns']) for r in cellrows)>=10000000
 global_controls &= control
 criterion=control and st.median(contrasts)>=1.02 and sum(x>1 for x in contrasts)>=5 and .99<=st.median(bs)<=1.01
 results.append(dict(member_bytes=size,rows=len(cellrows),controls=control,criterion=criterion,median_contrast=st.median(contrasts),direction_count=sum(x>1 for x in contrasts),median_B_phase=st.median(bs),tree_bytes=int(next(iter(memory))),min_wall_ns=min(int(r['elapsed_ns']) for r in cellrows),max_gap_fraction=max(p['gap_fraction'] for p in processes),blocks=blocks,processes=processes))
out=dict(rows=768,processes=48,hypothesis_supported=global_controls and results[0]['criterion'],cells=results)
(P/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# DIAG-008 warmup intervention results','','All768 windows retained. Primary miss16; miss320 secondary only.','','| Member bytes | Median phase contrast A/B | Contrasts >1 | Median B early/late | Controls | Criterion |','|---|---:|---:|---:|---|---|']
for r in results:lines.append(f"| {r['member_bytes']} | {r['median_contrast']:.6f} | {r['direction_count']}/6 | {r['median_B_phase']:.6f} | {r['controls']} | {r['criterion']} |")
lines+=['',f"Fixed primary hypothesis supported: {out['hypothesis_supported']}.",'All process/window values in summary.json; no source speedup, frequency inference or A/A qualification.']
(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
