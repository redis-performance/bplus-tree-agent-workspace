from pathlib import Path
import json,subprocess,hashlib,datetime,time,itertools,sys,math
p=Path(__file__).parent;phase=sys.argv[1];assert phase in ['calibration','aa','b'];cap=300 if phase=='calibration' else 900;out=p/(phase+'.json');assert not out.exists();assert json.loads((p/'validation-summary.json').read_text())['status']=='pass';(p/'raw').mkdir(exist_ok=True)
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
for f in json.loads((p/'fixture-manifest.json').read_text()):assert sha(p/'fixtures'/(f['name']+'.bin'))==f['sha256']
freeze=json.loads((p/'build-freeze.json').read_text())
for v in ['base','B']:assert sha(Path('scratch/intel-focused-scan')/v/'build/focused/scan-guard')==freeze[v]['build/focused/scan-guard']
if phase!='calibration':
 frozen=json.loads((p/'timing-freeze.json').read_text())
 for f,h in frozen['files'].items():assert sha(p/f)==h
if phase=='b':assert json.loads((p/'aa-audit.json').read_text())['phase_status']=='complete'
schedule=json.loads((p/(phase+'-schedule.json')).read_text());start=time.monotonic();m=dict(status='running',phase=phase,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),phase_cap_seconds=cap,rows=[])
try:
 for spec in schedule:
  left=cap-(time.monotonic()-start)
  if left<=0:raise TimeoutError('fixed focused '+phase+' cap')
  file=p/'fixtures'/f's{spec["seed"]}-n{spec["n"]}-b{spec["bytes"]}-d{spec["distribution"]}.bin';cmd=['scratch/intel-focused-scan/'+spec['binary']+'/build/focused/scan-guard','run',str(file),str(spec['order']),str(spec['passes']),'0'];tag=f'{phase}-{spec["index"]:04d}';t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(left,60))
  (p/'raw'/(tag+'.stdout')).write_text(r.stdout);(p/'raw'/(tag+'.stderr')).write_text(r.stderr);assert r.returncode==0,r.stderr;row=json.loads(r.stdout);assert row['start_cpu']==row['end_cpu']==2 and row['validation']=='pass'
  for k in ['n','bytes','seed','distribution','order','passes']:assert row[k]==spec[k]
  m['rows'].append(dict(**spec,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),row=row));out.write_text(json.dumps(m,indent=2)+'\n')
 m['status']='complete'
except Exception as e:
 m['status']='stopped';m['error']=repr(e);raise
finally:
 m.update(finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);out.write_text(json.dumps(m,indent=2)+'\n')
print('COMPLETE',phase,len(m['rows']),'rows')
