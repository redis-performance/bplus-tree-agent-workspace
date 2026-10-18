from pathlib import Path
import json,csv,subprocess,collections,hashlib
P=Path(__file__).resolve().parent;R=P.parents[1];m=json.loads((P/'profile-results/manifest.json').read_text());out=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for row in m['runs']:
 for k in ['stdout','stderr']:assert sha(R/row[k])==row[k+'_sha256']
 raw=list(csv.reader((R/row['stderr']).open()));h=[x for x in raw if x[0]=='PROFILE'];pcs=[x for x in raw if x[0]=='PC'];assert len(h)==1 and int(h[0][3])==len(pcs) and h[0][4]=='0' and len(pcs)>=30
 ex=[x for x in pcs if x[1]=='btree-bench'];bases={x[3] for x in ex};assert len(bases)==1;addr=sorted({x[2] for x in ex})
 cmd=['atos','-o',row['binary'],'-l',next(iter(bases)),*addr];q=subprocess.run(cmd,cwd=R,capture_output=True,text=True,timeout=120);assert q.returncode==0
 symbols=q.stdout.splitlines();assert len(symbols)==len(addr);mapping=dict(zip(addr,symbols));counts=collections.Counter(mapping[x[2]].split(' (in ')[0] if x[1]=='btree-bench' else x[4] for x in pcs)
 assert not any(x.startswith('0x') or x=='unknown' for x in counts)
 r=next(csv.DictReader((R/row['stdout']).open()));assert r['operations']=='100000000' and r['checksum']=='4999950000000'
 out.append(dict(name=row['name'],variant=row['variant'],seed=row['seed'],samples=len(pcs),counts=dict(counts),tree_bytes=r['tree_bytes'],command=cmd,symbols=symbols,stderr=q.stderr))
(P/'profile-results/summary.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# Matched iterator profiles','','Descriptive interrupted-PC counts, not unbiased time shares. All samples resolved.']
for r in out:lines.append(f"- {r['name']}: {r['samples']} samples; {r['counts']}")
lines+=['','Codegen: baseline generic function saves six register pairs on entry. C public fast-path','dispatch is separate from noinline generic fallback. Inspect saved assembly for exact','instructions; this supports dispatch/register isolation, not a cycle attribution.','Sampler cadence/perturbation/frequency unknown; no accepted or portable performance claim.']
(P/'profile-results/SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
