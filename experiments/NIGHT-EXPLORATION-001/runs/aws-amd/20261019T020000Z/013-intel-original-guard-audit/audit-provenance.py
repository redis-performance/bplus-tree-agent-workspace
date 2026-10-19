#!/usr/bin/env python3
"""Read-only independent bounded-job and final artifact identity reconstruction."""
import argparse,datetime,hashlib,json,pathlib
p=argparse.ArgumentParser();p.add_argument('guards',type=pathlib.Path);p.add_argument('--post',required=True,type=pathlib.Path);p.add_argument('--candidate-freeze',required=True,type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args();clock=datetime.datetime.fromisoformat
expected=json.loads(a.candidate_freeze.read_text());post=json.loads(a.post.read_text());assert post['status']=='pass' and not post['mismatches'];assert post['read_only'] and post['no_workload_executed'];assert post['expected_manifest_sha256']==hashlib.sha256(a.candidate_freeze.read_bytes()).hexdigest();assert post['observed']=={v:expected[v] for v in ['base','B']}
assert expected['base']['src/zset_btree.c']=='d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2'
assert expected['B']['src/zset_btree.c']=='204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23'
for key in expected['base']:
 if key!='src/zset_btree.c' and not key.startswith('build/'):assert expected['base'][key]==expected['B'][key]
jobs={}
for phase,name in [('aa','aa.json'),('b','b-comparison.json')]:
 job=json.loads((a.guards/f'guard-{phase}.sh.job.json').read_text());data=json.loads((a.guards/name).read_text())
 assert job['returncode']==0 and job['cpu']==2 and job['limit_seconds']==1440
 assert clock(job['started_utc'])<=clock(data['started_utc'])<=clock(data['finished_utc'])<=clock(job['finished_utc'])
 jobs[phase]=job
assert clock(jobs['aa']['finished_utc'])<clock(jobs['b']['started_utc'])
assert clock(jobs['b']['finished_utc'])<=clock(post['started_utc'])<=clock(post['finished_utc'])
a.out.write_text(json.dumps({'status':'pass','jobs':jobs,'post_phase_sha256':hashlib.sha256(a.post.read_bytes()).hexdigest(),'candidate_freeze_sha256':hashlib.sha256(a.candidate_freeze.read_bytes()).hexdigest(),'post_observations':post['observed'],'post_phase_finished_utc':post['finished_utc'],'final_identity_check':'all frozen base/B source, referee, test, compile manifest and binary entries match','source_adoption':'NONE','reviewer':'independent AMD native agent; exact model and costs unknown'},indent=2)+'\n');print('PASS bounded job and post-phase artifact identity')
