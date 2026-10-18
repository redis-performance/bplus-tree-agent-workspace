from pathlib import Path
import json,csv,hashlib,subprocess,collections
P=Path(__file__).resolve().parent;R=P.parents[2];D=P/'profiles';M=json.loads((D/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();results=[]
for section in ['calibrations','runs']:
 for row in M[section]:
  for k in ['stdout','stderr']:assert sha(R/row[k])==row[k+'_sha256']
  raw=list(csv.reader((R/row['stderr']).open()));heads=[r for r in raw if r[0]=='PROFILE'];pcs=[r for r in raw if r[0]=='PC'];assert len(heads)==1 and int(heads[0][3])==len(pcs) and heads[0][4]=='0';module=Path(row['binary']).name;ex=[r for r in pcs if r[1]==module];bases={r[3] for r in ex};assert len(bases)==1;addr=sorted({r[2] for r in ex});cmd=['atos','-o',row['binary'],'-l',next(iter(bases)),*addr];q=subprocess.run(cmd,cwd=R,capture_output=True,text=True,timeout=120);assert q.returncode==0;symbols=q.stdout.splitlines();assert len(symbols)==len(addr);mapping=dict(zip(addr,symbols));counts=collections.Counter(mapping[r[2]].split(' (in ')[0] if r[1]==module else r[4] for r in pcs);resolved=not any(s.startswith('0x') or s=='unknown' for s in counts);data=next(csv.DictReader((R/row['stdout']).open()))
  if section=='calibrations':controls=len(pcs)>=30 and sum(v for k,v in counts.items() if 'known_arithmetic' in k)>=.9*len(pcs) and data['checksum']=='3200000000'
  else:controls=len(pcs)>=15 and data['operations']=='100000000' and data['checksum']==data['expected_checksum'] and data['mask']==str(row['mask']) and data['seed']=='14107'
  results.append(dict(name=row['name'],section=section,controls=controls and resolved,samples=len(pcs),counts=dict(counts),symbolization_command=cmd,symbols=symbols,stderr=q.stderr))
(D/'summary.json').write_text(json.dumps(results,indent=2)+'\n');lines=['# DIAG-011 caller-context profiles','','Descriptive interrupted-PC counts;not unbiased time shares or exact-cycle attribution.','All instrumented timing values excluded from source speed comparison.','']
for r in results:lines.append(f"- {r['name']}: controls={r['controls']};{r['samples']} samples;{r['counts']}")
(D/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines));assert all(r['controls'] for r in results)
