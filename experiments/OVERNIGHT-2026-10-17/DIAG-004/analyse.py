from pathlib import Path
from collections import defaultdict
import csv,json,hashlib,statistics as s
P=Path(__file__).resolve().parent;m=json.loads((P/'manifest.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(P/'PLAN.md')==m['plan_sha256'] and m['status']=='complete' and len(m['runs'])==48
cells=defaultdict(list);structures=defaultdict(set);rows=[];duration_ok=True
for run in m['runs']:
 assert run['returncode']==0
 for f in ['csv','stderr']:assert sha(P/run[f])==run[f+'_sha256']
 data=list(csv.DictReader((P/run['csv']).open()));assert len(data)==1;r=data[0]
 b=run['block'];size=run['member_bytes'];a=run['arm'];seed=run['seed']
 assert [1,1,17,17,101,101][b-1]==seed
 assert r['fixture_order']==('ascending' if a=='A' else 'shuffled')
 assert int(r['seed'])==seed and int(r['member_bytes'])==size and int(r['size'])==100000
 assert int(r['operations'])==10000000 and int(r['checksum'])==499995000000
 assert int(r['warmup_passes'])==10 and int(r['elapsed_ns'])>=0
 duration_ok &= int(r['elapsed_ns'])>=10000000
 r.update(block=b,arm=a,slot=run['slot'],seed=seed,member_bytes=size)
 r['ns_op']=int(r['elapsed_ns'])/10000000
 cells[b,size].append(r);rows.append(r)
 structures[seed,size,a].add(tuple(int(r[x]) for x in ['tree_bytes','leaf_count','leaf_min','leaf_max']))
assert all(len(v)==1 for v in structures.values())
blocks=[]
for (b,size),group in sorted(cells.items()):
 assert len(group)==4 and ''.join(r['arm'] for r in group)==('ABBA' if b%2 else 'BAAB')
 means={a:s.mean(r['ns_op'] for r in group if r['arm']==a) for a in 'AB'}
 cv={a:s.stdev(r['ns_op'] for r in group if r['arm']==a)/means[a] for a in 'AB'}
 structure={a:dict(zip(['tree_bytes','leaf_count','leaf_min','leaf_max'],next(iter(structures[group[0]['seed'],size,a])))) for a in 'AB'}
 blocks.append(dict(block=b,seed=group[0]['seed'],member_bytes=size,means=means,cv=cv,ratio_A_B=means['A']/means['B'],structure=structure))
ratios=[b['ratio_A_B'] for b in blocks if b['member_bytes']==16];median=s.median(ratios);lower=sum(r<1 for r in ratios)
result=dict(rows=48,blocks=blocks,primary_median_ratio_A_B=median,primary_blocks_A_lower=lower,durations_valid=duration_ok,criterion_met=duration_ok and median<=.95 and lower>=5,
 boundary_changes=sum(r['cpu_start']!=r['cpu_end'] for r in rows),thread_wall_ratios=[int(r['thread_elapsed_ns'])/int(r['elapsed_ns']) for r in rows])
(P/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
lines=['# DIAG-004 descriptive results','','Ascending A and shuffled B construction; identical shuffled lookup order.','Wall time primary; memory/leaf changes are fixture effects, not source savings.','', '| Block | Seed | Bytes/key | A ns/op | B ns/op | A/B | A CV | B CV | A/B tree bytes | A/B leaves |','|---|---|---|---:|---:|---:|---:|---:|---:|---:|']
for b in blocks:
 a=b['structure']['A'];c=b['structure']['B']
 lines.append(f"| {b['block']} | {b['seed']} | {b['member_bytes']} | {b['means']['A']:.3f} | {b['means']['B']:.3f} | {b['ratio_A_B']:.6f} | {b['cv']['A']:.3%} | {b['cv']['B']:.3%} | {a['tree_bytes']}/{c['tree_bytes']} | {a['leaf_count']}/{c['leaf_count']} |")
lines+=['',f'Primary median A/B: {median:.6f}, A lower in {lower}/6 blocks; fixed criterion met: {result["criterion_met"]}.',f'48/48 checked rows, structure stable per seed/arm/size; boundary CPU changes: {result["boundary_changes"]}.', 'No A/A qualification, portable speed claim or source acceptance. Frequency/QoS/residency unknown.']
(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
