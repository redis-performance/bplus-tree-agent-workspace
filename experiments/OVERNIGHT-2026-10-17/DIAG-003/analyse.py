from pathlib import Path
import csv,json,hashlib,statistics as s
P=Path(__file__).resolve().parent;m=json.loads((P/'manifest.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(P/'PLAN.md')==m['plan_sha256']
assert m['status']=='complete' and len(m['runs'])==6
blocks=[];allrows=[];memory=set();duration_ok=True
for run in m['runs']:
 assert run['returncode']==0
 for f in ['csv','stderr']:assert sha(P/run[f])==run[f+'_sha256']
 rows=list(csv.DictReader((P/run['csv']).open()));assert len(rows)==4
 b=run['block'];assert ''.join(r['arm'] for r in rows)==('RIIR' if b%2 else 'IRRI')
 for i,r in enumerate(rows):
  assert int(r['block'])==b and int(r['sample'])==i
  assert int(r['size'])==100000 and int(r['operations'])==5000000
  assert int(r['fixture_seed'])==1 and int(r['stream_seed'])==17+b
  assert int(r['checksum'])==249997500000 and int(r['access_bytes'])==40000000
  assert int(r['access_storage'])==(b%2 if r['arm']=='R' else 1-b%2)
  memory.add(r['tree_bytes']);duration_ok &= int(r['elapsed_ns'])>=10000000
  r['ns_op']=int(r['elapsed_ns'])/int(r['operations']);allrows.append(r)
 means={a:s.mean(r['ns_op'] for r in rows if r['arm']==a) for a in 'RI'}
 cvs={a:s.stdev(r['ns_op'] for r in rows if r['arm']==a)/means[a] for a in 'RI'}
 for a in 'RI':assert len({r['access_fingerprint'] for r in rows if r['arm']==a})==1
 assert len({r['access_fingerprint'] for r in rows})==2
 blocks.append(dict(block=b,means=means,cvs=cvs,ratio_R_I=means['R']/means['I']))
assert len(memory)==1
ratios=[b['ratio_R_I'] for b in blocks];median=s.median(ratios);lower=sum(r<1 for r in ratios)
result=dict(blocks=blocks,rows=len(allrows),median_ratio_R_I=median,blocks_R_lower=lower,durations_valid=duration_ok,tree_bytes=int(next(iter(memory))),criterion_met=duration_ok and median<=.98 and lower>=5,
 boundary_changes=sum(r['cpu_start']!=r['cpu_end'] for r in allrows),thread_wall_ratios=[int(r['thread_elapsed_ns'])/int(r['elapsed_ns']) for r in allrows],
 pooled_cv={a:s.stdev(r['ns_op'] for r in allrows if r['arm']==a)/s.mean(r['ns_op'] for r in allrows if r['arm']==a) for a in 'RI'})
(P/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
lines=['# DIAG-003 descriptive results','', 'Wall time primary; six process blocks, two windows/arm/block. Local diagnostic only.', '', '| Block | R ns/op | I ns/op | R/I | R CV | I CV |','|---|---:|---:|---:|---:|---:|']
for b in blocks:lines.append(f"| {b['block']} | {b['means']['R']:.3f} | {b['means']['I']:.3f} | {b['ratio_R_I']:.6f} | {b['cvs']['R']:.4%} | {b['cvs']['I']:.4%} |")
lines+=['',f'Median R/I: {median:.6f}; R lower in {lower}/6 blocks. Fixed criterion met: {result["criterion_met"]}.',f'24/24 checked rows; tree bytes {result["tree_bytes"]}; opaque boundary CPU changes {result["boundary_changes"]}.', 'Clock/effective QoS/residency unknown; no causal cache/frequency or portable speed claim.']
(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
