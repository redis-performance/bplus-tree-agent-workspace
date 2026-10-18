from pathlib import Path
import subprocess,csv,json,hashlib,statistics as st
P=Path(__file__).resolve().parent;R=P.parents[2];m=json.loads((P/'manifest.json').read_text());B=R/'scratch/overnight-diag-009/base';S=B.parent/'symbols'
assert m['status']=='complete' and len(m['runs'])==18 and not S.exists();S.mkdir();results=[];commands=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for run in m['runs']:
 for f in ['stdout','stderr']:assert sha(R/run[f])==run[f+'_sha256']
 raw=list(csv.reader((R/run['stderr']).open()));headers=[x for x in raw if x[0]=='PROFILE'];pcs=[x for x in raw if x[0]=='PC']
 assert len(headers)==1 and len(pcs)==int(headers[0][3]) and headers[0][4]=='0'
 executable=[x for x in pcs if x[1]=='calibrate'];bases={x[3] for x in executable};assert len(bases)==1
 addresses=sorted({x[2] for x in executable});cmd=['atos','-o',str((B/'build/release/calibrate').relative_to(R)),'-l',next(iter(bases)),*addresses]
 out=S/(run['name']+'.stdout');err=S/(run['name']+'.stderr')
 with out.open('w') as so,err.open('w') as se:p=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=120)
 assert p.returncode==0;symbols=out.read_text().splitlines();assert len(symbols)==len(addresses)
 commands.append(dict(name=run['name'],command=cmd,returncode=p.returncode,stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=sha(out),stderr_sha256=sha(err)))
 mapping=dict(zip(addresses,symbols));known=sum(x[1]=='calibrate' and mapping[x[2]].startswith('known_arithmetic ') for x in pcs)
 row=next(csv.DictReader((R/run['stdout']).open()));assert row['checksum']=='3200000000' and row['iterations']=='400000000' and int(row['samples'])==len(pcs) and int(row['requested_usec'])==run['profile_usec']
 cpu=int(row['thread_ns']);wall=int(row['wall_ns']);assert min(cpu,wall)>0
 results.append(dict(block=run['block'],requested_usec=run['profile_usec'],reported_interval_sec=int(row['reported_interval_sec']),reported_interval_usec=int(row['reported_interval_usec']),samples=len(pcs),known=known,known_share=known/len(pcs),thread_ns=cpu,wall_ns=wall,rate_per_thread_second=len(pcs)*1e9/cpu,aggregate_thread_ns_per_delivery=cpu/len(pcs),valid=len(pcs)>=20 and known/len(pcs)>=.9))
blocks=[]
for b in range(1,7):
 rates={r['requested_usec']:r['rate_per_thread_second'] for r in results if r['block']==b}
 blocks.append(dict(block=b,ratio_1000_3001=rates[1000]/rates[3001],ratio_17011_1000=rates[17011]/rates[1000]))
a=[b['ratio_1000_3001'] for b in blocks];c=[b['ratio_17011_1000'] for b in blocks]
criterion=all(r['valid'] for r in results) and .9<=st.median(a)<=1.1 and sum(.9<=v<=1.1 for v in a)>=5 and st.median(c)<.75 and sum(v<.75 for v in c)>=5
summary=dict(hypothesis_supported=criterion,all_controls=all(r['valid'] for r in results),blocks=blocks,results=results)
(P/'symbolication.json').write_text(json.dumps(commands,indent=2)+'\n');(P/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# DIAG-009 aggregate timer delivery rates','','These are delivered sample counts per thread CPU duration, not exact interarrival intervals.','Wall/thread brackets include sampler boundary overhead; dump occurs after endpoints.','','| Block | Rate1000 / rate3001 | Rate17011 / rate1000 |','|---|---:|---:|']
for b in blocks:lines.append(f"| {b['block']} | {b['ratio_1000_3001']:.6f} | {b['ratio_17011_1000']:.6f} |")
lines+=['',f"All controls: {summary['all_controls']}; fixed hypothesis supported: {criterion}.",'No GHz inference, source speedup or unbiased profile-share claim.']
(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
