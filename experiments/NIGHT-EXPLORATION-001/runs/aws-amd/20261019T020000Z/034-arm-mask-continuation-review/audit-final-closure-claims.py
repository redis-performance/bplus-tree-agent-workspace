import subprocess,json,decimal,collections,statistics,hashlib,datetime
D=decimal.Decimal;decimal.getcontext().prec=40
prefix='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup/';canonical='experiments/ARM-MASK-FOLLOWUP-001/'
def raw(rev,path):return subprocess.check_output(['git','show',rev+':'+path])
def j(rev,path):return json.loads(raw(rev,path))
final=j('2a53fc3f3',canonical+'FINAL-DECISION.json');release=j('2a53fc3f3',canonical+'RELEASE-FINAL.json');states={x:j('f30ac4330',prefix+x+'/result.json') for x in ['iterator-AA','iterator-comparison']};cells={};total_rows=0
for phase,state in states.items():
 assert state['status']=='complete' and len(state['runs'])==1968;groups={}
 for run in state['runs']:
  assert len(run['rows'])==1 and run['returncode']==0 and run['checked'];total_rows+=1
  groups.setdefault((run['cell']['id'],run['block']),[]).append(run)
 assert len(groups)==492;result={}
 for (cell,block),runs in groups.items():
  assert [x['position'] for x in runs]==[0,1,2,3] and [x['label'] for x in runs]==['A','B','B','A'];rows=[x['rows'][0] for x in runs]
  for field in ['size','seed','member_bytes','requested_ops','operations','checksum','tree_bytes','traversals','warmup_passes','direction','mask','encoding','construction_fingerprint','expected_checksum']:assert len({z[field] for z in rows})==1
  ns=[int(z['elapsed_ns']) for z in rows];effect=(D(ns[1]+ns[2])/D(ns[0]+ns[3])-1)*100
  result.setdefault(cell,{'fixture':runs[0]['cell'],'blocks':[]})['blocks'].append(dict(block=block,effect=effect,min_ns=min(ns)))
 cells[phase]=result
assert len(cells['iterator-AA'])==len(cells['iterator-comparison'])==82
classified={};medians={};ids=[]
for cell,aa in cells['iterator-AA'].items():
 assert len(aa['blocks'])==6;qualified=all(abs(b['effect'])<=1 and b['min_ns']>=10000000 for b in aa['blocks']);comp=cells['iterator-comparison'][cell];values=[b['effect'] for b in comp['blocks']]
 verdict='UNQUALIFIED' if not qualified else ('PASS' if all(v<=1 for v in values) else ('REJECT' if all(v>1 for v in values) else 'MIXED'))
 classified[cell]=verdict
 if verdict=='REJECT':
  fixture=comp['fixture'];assert fixture['mask']==4 and fixture['requested_ops']==20000000 and fixture['member_bytes']==16 and fixture['warmup_passes']==3 and fixture['referee']=='HARNESS-004'
  medians[cell]=str(statistics.median(values));ids.append(cell);entry=next(x for x in final['rejected_qualified_cases'] if x['fixture']['id']==cell);assert entry['fixture']==fixture
  for b in comp['blocks']:
   other=next(x for x in entry['blocks'] if x['block']==b['block']);assert D(other['effect_pct'])==b['effect'] and other['minimum_window_ns']==b['min_ns']
assert dict(collections.Counter(classified.values()))=={'REJECT':9,'PASS':30,'MIXED':4,'UNQUALIFIED':39}
assert set(ids)=={'g004','g012','g020','g028','g033','g037','g041','g049','g053'}
# Verify decisive raw CSV bytes against publication and the result rows, not summaries alone.
import csv
pub=j('f30ac4330',prefix+'iterator-comparison/PUBLICATION.json');checked=0
for run in states['iterator-comparison']['runs']:
 if run['cell']['id'] not in ids:continue
 name=run['name']+'.csv';blob=raw('f30ac4330',prefix+'iterator-comparison/'+name);assert hashlib.sha256(blob).hexdigest()==pub[name]['public_sha256'];assert list(csv.DictReader(blob.decode().splitlines()))==run['rows'];checked+=1
assert checked==216
for a,b in zip(states['iterator-AA']['runs'],states['iterator-comparison']['runs']):
 assert (a['cell'],a['block'],a['position'],a['seed'])==(b['cell'],b['block'],b['position'],b['seed'])
 for k in ['operations','checksum','tree_bytes','traversals','warmup_passes','construction_fingerprint','expected_checksum']:assert a['rows'][0][k]==b['rows'][0][k]
assert final['decision']=='REJECT' and final['source_selection']=='NONE' and final['new_population'] is False
assert final['total_timing_processes']==48+48+120+120+1968+1968==4272
assert final['total_timing_rows']==48+48+960+960+1968+1968==5952
assert final['profile']=='UNEXECUTED_AFTER_DECISIVE_REJECTION' and final['heldout_confirmation']=='UNEXECUTED_INELIGIBLE'
s=release['state'];assert s['coordinator_running'] and s['coordinator_pid']==2927719 and s['saved_pid_matches_live'] and s['fresh_marker'] and s['verified_released'];assert s['slice_state']=='inactive' and s['active_owned_units']==[] and s['owned_cgroup_process_count']==0 and s['inspection_errors']==[] and s['units_query_ok']
assert 'RUNNING' in s['saved_release_status'] and '2927719' in s['saved_release_status'] and '2927719' in s['coordinator_status']
a=datetime.datetime.fromisoformat(release['checked_at']);b=datetime.datetime.fromisoformat(release['finished_at']);assert datetime.datetime.fromisoformat(s['release_marker'].replace('Z','+00:00'))<a<b<datetime.datetime.fromisoformat('2026-10-19T10:15:00+00:00')
assert raw('2a53fc3f3','src/zset_btree.c')==raw('13e459ff8','src/zset_btree.c') and raw('2a53fc3f3','src/zset_btree.h')==raw('13e459ff8','src/zset_btree.h')
print(json.dumps(dict(status='FINAL_CLAIMS_AND_RELEASE_RECORD_REVIEW_PASS',source_selection='NONE',decision='REJECT',recorded_iterator_rows=total_rows,decisive_comparison_raw_csv_rehashed=checked,classifications=dict(collections.Counter(classified.values())),rejected_medians=medians,total_timing_processes=4272,total_timing_rows=5952,source_unchanged=True,release_checked=release['checked_at'],release_finished=release['finished_at'],release_record_verified=True,runner_access=False,limits=['Final claim review reconstructs all recorded iterator rows plus216decisive raw CSV files; root/Intel full raw audits remain separately attributed','Release is verified from immutable operator live-observation record, not new reviewer SSH','Profile and held-out confirmation remain unexecuted; causality unmeasured']),indent=2))
