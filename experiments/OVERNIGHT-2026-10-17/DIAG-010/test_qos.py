from pathlib import Path
import subprocess,json,csv,io,hashlib
P=Path(__file__).resolve().parent;R=P.parents[2];records=[]
assert not (P/'qos-validation.json').exists()
for kind in ['release','sanitize']:
 binary=R/f'scratch/overnight-diag-010/base/build/{kind}/btree-bench'
 for size in [8,16,319,320,321]:
  for qos in ['user-interactive','user-initiated']:
   cmd=[str(binary.relative_to(R)),'--size','1000','--ops','2137','--member-bytes',str(size),'--seed','3001','--query-seed','3209','--query-order','independent','--requested-qos',qos]
   p=subprocess.run(cmd,cwd=R,capture_output=True,text=True,timeout=120)
   records.append(dict(command=cmd,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0
   rows=list(csv.DictReader(io.StringIO(p.stdout)));assert len(rows)==8
   for row in rows:
    assert row['qos_reported_start']==row['qos_reported_end']==qos
    assert row['qos_relpri_start']==row['qos_relpri_end']=='0'
    assert row['qos_effective']=='unknown'
 for value in ['bad','background']:
  cmd=[str(binary.relative_to(R)),'--requested-qos',value];p=subprocess.run(cmd,cwd=R,capture_output=True,text=True,timeout=120)
  records.append(dict(command=cmd,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==2
(P/'qos-validation.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS 160 case rows across two requested classes and builds; 4 rejected unsupported values')
