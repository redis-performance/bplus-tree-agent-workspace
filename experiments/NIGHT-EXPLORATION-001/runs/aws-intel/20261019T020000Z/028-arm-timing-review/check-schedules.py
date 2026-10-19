#!/usr/bin/env python3
"""Independent immutable manifest reconstruction; no producer code execution."""
import hashlib,itertools,json,subprocess
from pathlib import Path
REV='8d11db31a'
BASE='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup/'
HERE=Path(__file__).resolve().parent
inputs={}
def raw(name):
    data=subprocess.check_output(['git','show',REV+':'+BASE+name]);inputs[name]=hashlib.sha256(data).hexdigest();return data
def load(name):return json.loads(raw(name))
freeze=load('timing-freeze.json')
for name,digest in freeze['files'].items():assert hashlib.sha256(raw(name)).hexdigest()==digest
iterator=load('iterator-guards.json');original=load('original-guards.json')
def key(c):return(c['referee'],c['size'],c['member_bytes'],c['encoding'],c['direction'],c['mask'],c['requested_ops'],c.get('construction'))
expected=set()
for n,d,m in itertools.product([100000,1000000],['forward','reverse'],range(8)):
 expected.add(('HARNESS-004',n,16,'integer',d,m,50000000 if m==6 else 20000000,None))
for encoding,d,m in itertools.product(['fraction','wide','zero'],['forward','reverse'],[2,4,6,7]):
 expected.add(('HARNESS-004',100000,16,encoding,d,m,20000000,None))
for width,d,m in itertools.product([8,319,320,321,1024],['forward','reverse'],[2,6]):
 expected.add(('HARNESS-004',4096,width,'integer',d,m,20000000,None))
for construction,d in itertools.product(['shuffled','ascending','descending'],['forward','reverse']):
 expected.add(('HARNESS-005',4096,16,'alternating-zero',d,4,20000000,construction))
assert len(iterator)==len(expected)==82 and set(map(key,iterator))==expected
assert all(c['required_for_acceptance'] is True and c['warmup_passes']==3 for c in iterator)
operations=['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete']
assert len(original)==40 and len({(c['size'],c['case']) for c in original})==40
for cell in original:
 assert cell['size'] in [100,1000,10000,100000,1000000] and cell['case'] in operations
 required=cell['case'] in ['lookup-hit','lookup-miss','rank','scan','update'] or (cell['case'] in ['insert','delete'] and cell['size']>=100000)
 assert cell['required_for_acceptance']==required and cell['member_bytes']==16 and cell['requested_ops']==1000000
assert sum(c['required_for_acceptance'] for c in original)==29
base='<checkout>/scratch/adapter-worktree-13e459ff8/build/adapter-requalification/btree-bench'
candidate='<checkout>/scratch/arm-exp005A-replication-13e459ff8/A/build/adapter-requalification/btree-bench'
counts={}
for phase in ['primary-AA','primary-replication','original-AA','original-comparison','iterator-AA','iterator-comparison']:
 rows=load('schedules/'+phase+'.json');family=phase.split('-')[0];aa=phase.endswith('AA');index=0
 cells=iterator if family=='iterator' else [dict(id=family+'-'+str(n),size=n) for n in ([100000,1000000] if family=='primary' else [100,1000,10000,100000,1000000])]
 for block in range(6):
  for cell in cells if block%2==0 else list(reversed(cells)):
   for position,label in enumerate('ABBA'):
    row=rows[index];variant='control' if aa or label=='A' else 'A';seed=(1101 if family=='primary' else 1301)+block%3;n=cell['size']
    assert row['index']==index and row['name']==f"b{block}-{cell['id']}-p{position}-{label}"
    assert (row['block'],row['position'],row['label'],row['variant'],row['seed'])==(block,position,label,variant,seed)
    if family=='iterator':
     assert row['cell']==cell
     args=['<job>/'+variant+'/build/native/'+('modes5' if cell['referee']=='HARNESS-005' else 'modes'),'--size',str(n),'--ops',str(cell['requested_ops']),'--member-bytes',str(cell['member_bytes']),'--seed',str(seed),'--mask',str(cell['mask']),'--direction',cell['direction'],'--encoding',cell['encoding'],'--warmup-passes','3']
     if cell.get('construction'):args+=['--construction',cell['construction']]
    else:
     count=50000000 if family=='primary' else 1000000;case='iterate' if family=='primary' else 'all'
     assert row['cell']['id']==cell['id'] and row['cell']['size']==n and row['cell']['requested_ops']==count and row['cell']['member_bytes']==16 and row['cell']['case']==case
     args=[base if variant=='control' else candidate,'--case',case,'--size',str(n),'--ops',str(count),'--member-bytes','16','--seed',str(seed)]
    assert row['command']==args,(phase,index)
    index+=1
 assert index==len(rows);counts[phase]=index
report=dict(status='PASS',revision=REV,frozen_input_count=len(freeze['files']),schedule_rows=counts,total_scheduled_processes=sum(counts.values()),required_iterator_cells=82,required_original_cells=29,coverage_diagnostic_cells=11,source_adoption='NONE',limitations=['Static manifest review only; no timing or producer audit code executed.','Original failed preparation/composite closure and audit repairs remain separate blockers.'])
(HERE/'schedule-review.json').write_text(json.dumps(report,indent=2)+'\n');(HERE/'input-hashes.json').write_text(json.dumps(inputs,indent=2,sort_keys=True)+'\n');print(json.dumps(report))
