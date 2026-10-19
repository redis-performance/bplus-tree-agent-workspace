#!/usr/bin/env python3
"""Synthetic metadata-only checks; does not invoke phase main or a benchmark."""
import copy
import datetime
import importlib.util
import json
from pathlib import Path
import sys
sys.dont_write_bytecode=True
here=Path(__file__).resolve().parent

def module(name,file):
    spec=importlib.util.spec_from_file_location(name,here/file)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj
run=module('heldout_driver','run-phase.py');audit=module('heldout_auditor','audit-phase.py')
checks=[]
def expect(label,function,error=False):
    try:function()
    except (RuntimeError,ValueError):
        if not error:raise
    else:
        if error:raise AssertionError('expected refusal: '+label)
    checks.append(label)
def classify(effects,qualified=True,**kw):
    cell=dict(complete=True,qualified=qualified,memory_pass=True,block_effect_pct=effects);cell.update(kw)
    return run.diagnostic_classification(cell)
def equals(actual,want):
    if actual != want:raise AssertionError((actual,want))
expect('qualified all6<=1 is PASS',lambda:equals(classify([0,1,-2,0.5,-1,1]),'PASS'))
expect('qualified all6>1 is REJECT',lambda:equals(classify([1.01]*6),'REJECT'))
expect('qualified mixed >1 is PARK',lambda:equals(classify([1.01,0,0,0,0,0]),'PARK'))
expect('unqualified diagnostic retained',lambda:equals(classify([2]*6,False),'UNQUALIFIED_DIAGNOSTIC'))
expect('incomplete diagnostic refuses',lambda:classify([0]*6,complete=False),True)
expect('memory failure refuses even unqualified',lambda:classify([0]*6,False,memory_pass=False),True)
expect('missing block refuses',lambda:classify([0]*5),True)
expect('nonfinite block refuses',lambda:classify([0]*5+['NaN']),True)
expect('nonboolean qualification refuses',lambda:classify([0]*6,'false'),True)
artifacts=[dict(path='aa/'+str(i)+suffix,sha256=str(i)+suffix) for i in range(48) for suffix in ('.csv','.stderr')]
hashes={Path(x['path']).name:x['sha256'] for x in artifacts}
expect('96 exact audited hashes join',lambda:run.verify_raw_audit_join(artifacts,{'raw_file_sha256':hashes},set(hashes)))
bad=copy.deepcopy(artifacts);bad[0]['sha256']='substituted'
expect('valid names but substituted hash refuses',lambda:run.verify_raw_audit_join(bad,{'raw_file_sha256':hashes},set(hashes)),True)
bad=copy.deepcopy(artifacts);bad[-1]=bad[0]
expect('duplicate raw filename refuses',lambda:run.verify_raw_audit_join(bad,{'raw_file_sha256':hashes},set(hashes)),True)
start=datetime.datetime(2026,10,19,9,tzinfo=datetime.timezone.utc)
expect('30 seconds allowed',lambda:audit.check_child_interval(start,start+datetime.timedelta(seconds=30)))
expect('30.000001 seconds refuses',lambda:audit.check_child_interval(start,start+datetime.timedelta(seconds=30,microseconds=1)),True)
expect('negative child interval refuses',lambda:audit.check_child_interval(start,start-datetime.timedelta(microseconds=1)),True)
result={'status':'PASS','synthetic_metadata_checks':len(checks),'checks':checks,'phase_main_invoked':False,'benchmark_build_or_remote_workload':False}
(here/'GATE-REPAIR-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
