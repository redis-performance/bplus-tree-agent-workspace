from pathlib import Path
import sys,importlib.util,json,copy
sys.dont_write_bytecode=True;ROOT=Path.cwd();OUT=Path(__file__).resolve().parents[1];spec=importlib.util.spec_from_file_location('contract_driver',OUT/'driver.py');d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
checks=[]
try:d.execute(['python3','-c',"import time; print('started',flush=True); time.sleep(5)"],'driver-timeout-control','validation-logs',.05)
except RuntimeError:pass
else:raise AssertionError('timeout not enforced')
records=[json.loads(x) for x in (OUT/'commands.jsonl').read_text().splitlines()];r=records[-1];assert r['timed_out'] and r['process_reaped'] and r['returncode']!=0;checks.append('timeout kills/reaps process group and preserves output')
original=d.subprocess.Popen
class InterruptOnce:
 def __init__(self,*a,**kw):self.child=original(*a,**kw);self.first=True
 @property
 def pid(self):return self.child.pid
 @property
 def returncode(self):return self.child.returncode
 def poll(self):return self.child.poll()
 def communicate(self,*a,**kw):
  if self.first:self.first=False;raise KeyboardInterrupt('deliberate driver cleanup control')
  return self.child.communicate(*a,**kw)
d.subprocess.Popen=InterruptOnce
try:
 try:d.execute(['python3','-c','import time; time.sleep(5)'],'driver-interrupt-control','validation-logs',1)
 except RuntimeError:pass
 else:raise AssertionError('interrupt not preserved')
finally:d.subprocess.Popen=original
r=json.loads((OUT/'commands.jsonl').read_text().splitlines()[-1]);assert 'interrupted' in r and r['process_reaped'] and r['returncode']!=0;checks.append('KeyboardInterrupt kills/reaps child and retains interruption')
runs=[]
for c in d.CELLS:
 for block in range(6):
  for step,label in enumerate('ABBA'):runs.append(dict(cell=c['id'],block=block,comparison='old-vs-new',step=step,label=label,checksum='fixed',operations=100000000,tree_bytes=1234,csv={'construction_fingerprint':str(block)},ns_op=1,elapsed_ns=100000000))
controls=[dict(cell=c['id'],comparison=a,qualified=True) for c in d.CELLS for a in ('old','new')]
assert all(x['all_comparison_windows_minimum_met'] for x in d.derive(runs,'compare',controls))
short=copy.deepcopy(runs);short[0]['elapsed_ns']=1000000;result=d.derive(short,'compare',controls);assert not result[0]['all_comparison_windows_minimum_met'] and result[0]['interpretation'].startswith('conditional');checks.append('short comparison window is conditional even with qualifying controls')
for field in ('tree_bytes','construction_fingerprint'):
 bad=copy.deepcopy(runs)
 if field=='tree_bytes':bad[0][field]+=1
 else:bad[0]['csv'][field]='different'
 try:d.derive(bad,'compare',controls)
 except AssertionError:checks.append('ABBA '+field+' mismatch detected')
 else:raise AssertionError(field+' mismatch not detected')
(OUT/'driver-validation.json').write_text(json.dumps(dict(status='PASS',checks=checks,scope='synthetic driver controls only; no benchmark phase, timing effect or performance row',real_children=2,all_children_stopped=True),indent=2)+'\n');print('PASS:',len(checks),'synthetic driver checks; no measured phase')
