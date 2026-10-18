"""Read-only audit of round2 evidence; does not rerun measurements."""
import csv,hashlib,json,math,statistics as st
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for experiment in ['AA-002','DIAG-002']:
 d=P/experiment;m=json.loads((d/'manifest.json').read_text())
 assert m['status']=='complete'
 assert sha(d/'PLAN.md')==m['plan_sha256']
 assert sha(d/'run.py')==m['runner_sha256']
 assert m['binary_sha256']==m['binary_sha256_after']
 binary=ROOT/m['binary'];assert sha(binary)==m['binary_sha256']
 for run in m['runs']+m['warmup']:
  assert run['returncode']==0
  for f in ['csv','stderr']:assert sha(d/run[f])==run[f+'_sha256']
  rows=list(csv.DictReader((d/run['csv']).open()))
  assert len(rows)==(1 if experiment=='AA-002' else 4)
  for r in rows:
   assert int(r['size'])==1000000 and int(r['seed'])==1
   n=int(r['size']);ops=int(r['operations']);case=r.get('case','lookup-hit')
   expected=0 if case=='lookup-miss' else n*(n-1)//2*(ops//n)
   assert int(r['checksum'])==expected
   if experiment=='AA-002':assert int(r['requested_ops'])==ops
   else:assert ops==5000000 and int(r['adds'])==128000000
 if experiment=='AA-002':
  assert len(m['runs'])==96
  summary=json.loads((d/'summary.json').read_text())
  for cell in summary:
   effects=[]
   for block in range(1,7):
    values={a:[] for a in 'AB'}
    runs=[r for r in m['runs'] if r['cell']==cell['cell'] and r['block']==block]
    assert [r['label'] for r in runs]==list('ABBA')
    for run in runs:
     r=next(csv.DictReader((d/run['csv']).open()));values[run['label']].append(int(r['elapsed_ns'])/int(r['operations']))
    effects.append(100*(st.mean(values['B'])/st.mean(values['A'])-1))
   mean=st.mean(effects);half=2.5705818366147395*st.stdev(effects)/math.sqrt(6)
   assert math.isclose(mean-half,cell['ci95_low_pct'],abs_tol=1e-10)
   assert math.isclose(mean+half,cell['ci95_high_pct'],abs_tol=1e-10)
 else:assert len(m['runs'])==6
 print(experiment,'raw hashes, schedule/counts/checksums and binary: PASS')
for name in ['HARNESS-001','DIAG-002']:
 f=json.loads((P/name/'freeze.json').read_text());snapshot=ROOT/f['snapshot']
 for path,h in f['files'].items():assert sha(snapshot/path)==h
 if name=='HARNESS-001':
  for path in f['files']:
   if path.startswith(('src/','compat/','vendor/','bench/')):assert sha(ROOT/path)==f['files'][path]
 print(name,'snapshot/source integrity: PASS')
for name in ['BOUNDARY-003','BOUNDARY-004']:
 d=P/name;m=json.loads((d/'manifest.json').read_text())
 for path,h in m['sources'].items():assert sha(ROOT/path)==h
 for run in m['runs']:
  assert run['returncode']==0
  for stream in ['stdout','stderr']:assert sha(d/(run['name']+'.'+stream))==run[stream+'_sha256']
 for f in (d/'mutations').glob('*/manifest.json'):
  mutant=json.loads(f.read_text());assert mutant['detected']
  assert mutant['runs'][0]['returncode']==0 and mutant['runs'][1]['returncode']!=0
  for run in mutant['runs']:
   for stream in ['stdout','stderr']:assert sha(f.parent/(run['name']+'.'+stream))==run[stream+'_sha256']
 print(name,'source/command/log hashes and expected fault detections: PASS')
print('PASS: read-only coordinator audit; not independent performance confirmation')
