#!/usr/bin/env python3
"""Synthetic decision tests only, no performance/correctness workload."""
import copy,hashlib,json,pathlib,subprocess,tempfile
here=pathlib.Path(__file__).resolve().parent;e=json.loads((here/'expected.json').read_text());checks=[]
base=dict(status='pass',commands=104,semantic_parity_pass=True,known_arithmetic_and_scope_pass=True,counter_runtime_and_positivity_pass=True,disabled_zero_pass=True,known_control={'lost':0},total_lost_events=0,all_nonempty_stderr=[],all_six_instruction_direction_pass=True)
for fault in [None,'known-loss','science-loss','direction','mapped-bytes','actual-identity','scope','counters','disabled','warning']:
 with tempfile.TemporaryDirectory() as tmp:
  out=pathlib.Path(tmp);audit=copy.deepcopy(base);maps={v:dict(actual_timing_binary_sha256=e['timing_binaries'][v]['sha256'],all_sampled_tree_bytes_match_actual=True,groups={},full_tree_body_comparison={},limits=['synthetic, not scientific data']) for v in ['control','A']}
  if fault=='known-loss':audit['known_control']['lost']=1
  if fault=='science-loss':audit['total_lost_events']=1
  if fault=='direction':audit['all_six_instruction_direction_pass']=False
  if fault=='mapped-bytes':maps['A']['all_sampled_tree_bytes_match_actual']=False
  if fault=='actual-identity':maps['A']['actual_timing_binary_sha256']='wrong'
  if fault=='scope':audit['known_arithmetic_and_scope_pass']=False
  if fault=='counters':audit['counter_runtime_and_positivity_pass']=False
  if fault=='disabled':audit['disabled_zero_pass']=False
  if fault=='warning':audit['all_nonempty_stderr']=[dict(command='synthetic',stderr='lost events warning')]
  (out/'audit.json').write_text(json.dumps(audit))
  for v,m in maps.items():(out/(v+'-code-map.json')).write_text(json.dumps(m))
  r=subprocess.run(['python3',str(here/'finalize-profile.py'),str(out)],capture_output=True,text=True);assert r.returncode==(0 if fault is None else 1),(fault,r.stderr)
  z=json.loads((out/'profile-validity.json').read_text());assert bool(z['failed_gates'])==(fault is not None);checks.append(dict(synthetic_fault=fault or 'none',expected='PASS' if fault is None else 'PARK',observed=z['status']))
(here/'VALIDITY-LOCAL-CHECKS.json').write_text(json.dumps(dict(scope='Synthetic local gate tests only; no runner access or workload. Temporary invented inputs removed.',tests=checks),indent=2)+'\n')
