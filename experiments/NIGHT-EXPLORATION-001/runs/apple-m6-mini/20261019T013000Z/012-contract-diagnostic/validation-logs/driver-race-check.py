from pathlib import Path
import sys,json,hashlib,importlib.util
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parents[1];spec=importlib.util.spec_from_file_location('contract_driver_final',OUT/'driver.py');d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
original=d.os.killpg
def race(pid,sig):original(pid,sig);raise ProcessLookupError('deliberate process-exit race control')
d.os.killpg=race
try:
 try:d.execute(['python3','-c',"import time;print('started',flush=True);time.sleep(5)"],'driver-race-control','validation-logs',.05)
 except RuntimeError:pass
 else:raise AssertionError('timeout not detected')
finally:d.os.killpg=original
r=json.loads((OUT/'commands.jsonl').read_text().splitlines()[-1]);assert r['timed_out'] and r['process_reaped'] and r['returncode']!=0 and r['command'][0]=='python3'
assert (Path('scratch/m6-contract-diagnostic/raw-logs')/'driver-race-control.command.json').exists()
p=OUT/'driver-validation.json';v=json.loads(p.read_text());v['checks'].append('ProcessLookupError exit race handled; final logger preserves original private command');v['real_children']=3;v['driver_sha256']=hashlib.sha256((OUT/'driver.py').read_bytes()).hexdigest();p.write_text(json.dumps(v,indent=2)+'\n');print('PASS: race cleanup and final private/public command logging; child reaped; no benchmark phase')
