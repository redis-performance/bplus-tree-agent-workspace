from pathlib import Path
import subprocess,csv,json,hashlib,collections,re
P=Path(__file__).resolve().parent;R=P.parents[2];m=json.loads((P/'manifest.json').read_text());B=R/'scratch/overnight-profile-002/base';S=B.parent/'symbols'
assert m['status']=='complete' and len(m['runs'])==12 and not S.exists();S.mkdir()
results=[];commands=[]
for row in m['runs']:
 for f in ['stdout','stderr']:assert hashlib.sha256((R/row[f]).read_bytes()).hexdigest()==row[f+'_sha256']
 raw=list(csv.reader((R/row['stderr']).open()));headers=[x for x in raw if x[0]=='PROFILE'];pcs=[x for x in raw if x[0]=='PC']
 assert len(headers)==1 and len(pcs)==int(headers[0][3]) and headers[0][4]=='0' and headers[0][1]==row['case']
 executable=[x for x in pcs if x[1]=='btree-bench'];bases={x[3] for x in executable};assert len(bases)==1
 addresses=sorted({x[2] for x in executable});cmd=['atos','-o',str((B/'build/release/btree-bench').relative_to(R)),'-l',next(iter(bases)),*addresses]
 out=S/(row['name']+'.stdout');err=S/(row['name']+'.stderr')
 with out.open('w') as so,err.open('w') as se:p=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=120)
 assert p.returncode==0;symbols=out.read_text().splitlines();assert len(symbols)==len(addresses)
 commands.append(dict(name=row['name'],command=cmd,returncode=p.returncode,stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),stderr_sha256=hashlib.sha256(err.read_bytes()).hexdigest()))
 mapping=dict(zip(addresses,symbols));counts=collections.Counter();locations=collections.Counter();unknown=0
 for pc in pcs:
  if pc[1]=='btree-bench':
   sym=mapping[pc[2]];fn=sym.split(' (in ')[0]
   # Atos emits file:line for inline/static locations; retain basenames only.
   loc=re.sub(r'\((?:[^()]*[/])([^()/]+:\d+)\)',r'(\1)',sym)
   if fn.startswith('0x'):unknown+=1
  else:
   fn=pc[4];loc=pc[1]+':'+fn
   if fn=='unknown':unknown+=1
  counts[fn]+=1;locations[loc]+=1
 bench=next(csv.DictReader((R/row['stdout']).open()))
 result=dict(name=row['name'],seed=row['seed'],interval_usec=row['interval_usec'],case=row['case'],member_bytes=row['member_bytes'],samples=len(pcs),unknown=unknown,sufficient=len(pcs)>=100,counts=dict(counts.most_common()),locations=dict(locations.most_common()),wall_elapsed_ns=int(bench['elapsed_ns']),operations=int(bench['operations']),checksum=int(bench['checksum']),tree_bytes=int(bench['tree_bytes']))
 results.append(result)
(P/'symbolication.json').write_text(json.dumps(commands,indent=2)+'\n');(P/'summary.json').write_text(json.dumps(results,indent=2)+'\n')
lines=['# PROFILE-002 descriptive interrupted-PC counts','','No speedup or unbiased time fraction implied. Timed regions contain sampler overhead;','thread timer additionally includes post-loop profile dump and is unusable for CPU/wall ratios.','Requested intervals may be rounded/coalesced; boundary sampler instructions can be captured.','','| Capture | Samples | Unknown | >=100 | Top sampled symbols (counts) |','|---|---:|---:|---|---|']
for r in results:lines.append(f"| {r['name']} | {r['samples']} | {r['unknown']} | {r['sufficient']} | "+'; '.join(f'{k}: {v}' for k,v in list(r['counts'].items())[:4])+' |')
(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
