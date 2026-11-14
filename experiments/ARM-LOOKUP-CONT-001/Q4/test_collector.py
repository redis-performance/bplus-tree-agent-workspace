"""Correctness-only tests. No workload execution, clocks, or fleet operations."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[1] / 'fleet_profiler_off_qualification.py'
spec = importlib.util.spec_from_file_location('q4', SOURCE)
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)


def sample(phase=q.PHASES[0]):
    cohort, seed, scale = q.phase_spec(phase)
    rows = []
    for case, count in q.CASES.items():
        count *= scale
        for block in range(3):
            for slot, label in enumerate('ABBA'):
                rows.append(dict(case=case,seed=seed,ops=count*500,elapsed_ns=1000000000,
                    hits=0 if case=='miss' else count*500,
                    score_sum=count*125250 if case=='score' else 0,owned_bytes=40000,
                    phase=phase,cohort=cohort,block=block,slot=slot,label=label,sweeps=count,
                    source_sha256=q.BASE_SOURCE,referee_sha256=q.REFEREE_PINS['lookup.c'],
                    binary_sha256=q.BASELINES[cohort][1]))
    return rows


class Analysis(unittest.TestCase):
    def test_all_fixed_cohorts_no_side_effects(self):
        with patch.object(q.time,'time',side_effect=AssertionError('clock')), \
             patch.object(q.subprocess,'run',side_effect=AssertionError('process')), \
             patch.object(q.os,'sched_getaffinity',side_effect=AssertionError('host')):
            for phase in q.PHASES:
                rows = sample(phase)
                before = copy.deepcopy(rows)
                result = q.analyse_rows(phase,rows)
                self.assertTrue(result['all_pass'])
                self.assertEqual(result['rows'],72)
                self.assertEqual(rows,before)
                self.assertFalse(result['candidate_executed'])

    def test_missing_duplicate_extra_reordered(self):
        original = sample()
        cases = [original[:-1],original+[original[0]],
                 original[:1]+[original[0]]+original[2:],
                 original[1:2]+original[:1]+original[2:]]
        for rows in cases:
            with self.subTest(rows=len(rows)), self.assertRaises(ValueError):
                q.analyse_rows(q.PHASES[0],rows)

    def test_nonfinite_wrong_model_identity_and_schema(self):
        mutations = [('elapsed_ns',float('nan')),('elapsed_ns',float('inf')),
            ('score_sum',float('-inf')),('owned_bytes',True),('ops',0),('hits',0),
            ('score_sum',1),('seed',17),('sweeps',50000),('case','miss'),('slot',True),
            ('block',1),('label','B'),('phase','Q4-native-17'),('cohort','native'),
            ('source_sha256','0'*64),('referee_sha256','0'*64),('binary_sha256','0'*64)]
        for key,value in mutations:
            rows = sample();rows[0][key] = value
            with self.subTest(key=key,value=value), self.assertRaises(ValueError):
                q.analyse_rows(q.PHASES[0],rows)
        rows=sample();rows[0]['excluded']=True
        with self.assertRaises(ValueError):q.analyse_rows(q.PHASES[0],rows)
        rows=sample();del rows[0]['owned_bytes']
        with self.assertRaises(ValueError):q.analyse_rows(q.PHASES[0],rows)

    def test_short_and_noisy_never_excluded(self):
        for delta in (-11000000,11000000):
            rows=sample()
            rows[1]['elapsed_ns']+=delta;rows[2]['elapsed_ns']+=delta
            result=q.analyse_rows(q.PHASES[0],rows)
            self.assertFalse(result['all_pass']);self.assertEqual(result['rows'],72)
        rows=sample();rows[0]['elapsed_ns']=249999999
        self.assertFalse(q.analyse_rows(q.PHASES[0],rows)['all_pass'])

    def test_exact_one_percent_and_duration_boundaries(self):
        for delta in (-10000000,10000000):
            rows=sample();rows[1]['elapsed_ns']+=delta;rows[2]['elapsed_ns']+=delta
            self.assertTrue(q.analyse_rows(q.PHASES[0],rows)['all_pass'])
        rows=sample()
        for r in rows:r['elapsed_ns']=250000000
        self.assertTrue(q.analyse_rows(q.PHASES[0],rows)['all_pass'])
        rows[1]['elapsed_ns']=252500001;rows[2]['elapsed_ns']=252500001
        self.assertFalse(q.analyse_rows(q.PHASES[0],rows)['all_pass'])

    def test_memory_exact_within_and_across_blocks(self):
        rows=sample();rows[1]['owned_bytes']+=1
        self.assertFalse(q.analyse_rows(q.PHASES[0],rows)['all_pass'])
        rows=sample()
        for r in rows[4:8]:r['owned_bytes']+=1
        self.assertFalse(q.analyse_rows(q.PHASES[0],rows)['all_pass'])

    def test_phase_unknown(self):
        with self.assertRaises(ValueError):q.phase_spec('Q4-lto-99')


class Claims(unittest.TestCase):
    def test_overall_one_shot_failed_or_partial(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);q.claim_sequence(root,{'test':True})
            with self.assertRaises(FileExistsError):q.claim_sequence(root,{'test':False})
            self.assertEqual(json.loads((root/'Q4-profiler-off/admission.json').read_text()),{'test':True})

    def test_phase_overwrite_skip_and_failed_predecessor(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            q.claim_phase(root,q.PHASES[0],{})
            with self.assertRaises(FileExistsError):q.claim_phase(root,q.PHASES[0],{})
            with self.assertRaises(ValueError):q.claim_phase(root,q.PHASES[2],{})
            with self.assertRaises(ValueError):q.claim_phase(root,q.PHASES[1],{q.PHASES[0]:{'all_pass':False}})
            q.claim_phase(root,q.PHASES[1],{q.PHASES[0]:{'all_pass':True}})
            with self.assertRaises(ValueError):q.claim_sequence(root,{})

    def test_json_rejects_duplicate_key_and_nonfinite(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json'
            for content in ('{"a":1,"a":2}','{"a":NaN}','{"a":Infinity}'):
                p.write_text(content)
                with self.assertRaises(ValueError):q.read(p)


class Record(unittest.TestCase):
    def record(self,root):
        pin='1'*64
        rec={'schema_version':1,'owner':q.OWNER,'run_root':str(root),'lease_sha256':pin,
             'deadline':1794640800,'coordinator':{'pid':123,'start_ticks':'456'},
             'service':{'name':'snap.parca-agent.parca-agent-svc.service','saved_active_state':'active',
                        'saved_cpu_affinity':'','saved_allowed_cpus':''},
             'cleanup_timers':['release.timer','backup.timer'],
             'cleanup_timer_schedules':[
                 {'unit':'release.timer','NextElapseUSecRealtime':'calendar-value',
                  'NextElapseUSecMonotonic':'0','fire_epoch':1794640800},
                 {'unit':'backup.timer','NextElapseUSecRealtime':'0',
                  'NextElapseUSecMonotonic':'monotonic-value','fire_epoch':1794640700}],
             'cleanup_services':[{'unit':'release.service','exec_start_sha256':pin}],
             'cleanup_artifacts':[{'path':'cleanup.py','sha256':pin}],
             'restore_service':True,'resume_saved_coordinator':True,'reap_owned_children_before_resume':True}
        review={'schema_version':1,'decision':'APPROVED','reviewer_role':'independent reviewer',
                'isolation_sha256':pin,'collector_sha256':pin}
        return rec,review,pin

    def test_record_review_binding(self):
        with tempfile.TemporaryDirectory() as root:
            rec,review,pin=self.record(root)
            q.validate_record(rec,review,root,pin,pin)
            for key,value in [('decision','PENDING'),('collector_sha256','2'*64),
                              ('isolation_sha256','2'*64),('reviewer_role','')]:
                wrong=dict(review);wrong[key]=value
                with self.assertRaises(ValueError):q.validate_record(rec,wrong,root,pin,pin)

    def test_record_missing_recovery_identity_or_policy(self):
        with tempfile.TemporaryDirectory() as root:
            rec,review,pin=self.record(root)
            for key,value in [('owner','other'),('deadline',float('nan')),
                ('cleanup_timers',['same.timer','same.timer']),('cleanup_artifacts',[]),
                ('restore_service',False),('resume_saved_coordinator',False),
                ('reap_owned_children_before_resume',False)]:
                wrong=copy.deepcopy(rec);wrong[key]=value
                with self.assertRaises(ValueError):q.validate_record(wrong,review,root,pin,pin)
            wrong=copy.deepcopy(rec);wrong['service']['saved_cpu_affinity']='0'
            with self.assertRaises(ValueError):q.validate_record(wrong,review,root,pin,pin)

    def test_timer_schedule_schema_and_lease_bound(self):
        with tempfile.TemporaryDirectory() as root:
            rec,review,pin=self.record(root)
            for field,value in [('fire_epoch',rec['deadline']+1),('fire_epoch',float('nan')),
                                ('unit','backup.timer')]:
                wrong=copy.deepcopy(rec);wrong['cleanup_timer_schedules'][0][field]=value
                with self.assertRaises(ValueError):q.validate_record(wrong,review,root,pin,pin)
            wrong=copy.deepcopy(rec)
            wrong['cleanup_timer_schedules'][0]['NextElapseUSecRealtime']='0'
            with self.assertRaises(ValueError):q.validate_record(wrong,review,root,pin,pin)


class ProcessSafety(unittest.TestCase):
    def test_parca_detection_never_serializes_arguments(self):
        secret=b'Bearer private-token-value-123'
        cmd=b'/snap/parca-agent/bin/agent\x00--bearer-token\x00'+secret+b'\x00'
        result=q.parca_process_match(99,b'agent\n',cmd)
        retained=json.dumps(result)
        self.assertEqual(set(result),{'pid','comm','parca_detected','cmdline_redacted'})
        self.assertTrue(result['parca_detected'] and result['cmdline_redacted'])
        for forbidden in ('private-token-value','Bearer','--bearer-token','/snap/'):
            self.assertNotIn(forbidden,retained)
        self.assertIsNone(q.parca_process_match(1,b'worker',secret))
        self.assertTrue(q.parca_process_match(2,b'PARCA-AGENT',b'')['parca_detected'])

    def test_preexec_enforces_and_verifies_cpu2(self):
        with patch.object(q.os,'sched_setaffinity') as setter, \
             patch.object(q.os,'sched_getaffinity',return_value={2}) as getter:
            q.pin_child_cpu()
            setter.assert_called_once_with(0,{2});getter.assert_called_once_with(0)
        with patch.object(q.os,'sched_setaffinity'), \
             patch.object(q.os,'sched_getaffinity',return_value={0,2}):
            with self.assertRaises(ValueError):q.pin_child_cpu()

    def test_live_affinity_checked_exit_race_honestly_unavailable(self):
        with patch.object(q.os,'sched_getaffinity',return_value={2}):
            self.assertEqual(q.observe_child_affinity(123),{'available':True,'affinity':[2]})
        with patch.object(q.os,'sched_getaffinity',return_value={0}):
            with self.assertRaises(ValueError):q.observe_child_affinity(123)
        with patch.object(q.os,'sched_getaffinity',side_effect=ProcessLookupError):
            observed=q.observe_child_affinity(123)
            self.assertFalse(observed['available']);self.assertIsNone(observed['affinity'])
        command={'returncode':0,'child_affinity_observation':observed}
        q.check_child_completion(command,b'')
        for failed in ({**command,'returncode':1},{**command,'returncode':-9},
                       {**command,'child_error':'TimeoutExpired'}):
            with self.assertRaises(ValueError):q.check_child_completion(failed,b'')
        with self.assertRaises(ValueError):q.check_child_completion(command,b'error')


class IsolationBranches(unittest.TestCase):
    """Real isolation function, fake proc/sys trees and fully mocked commands/clocks."""
    def exercise(self, fault=None):
        with tempfile.TemporaryDirectory() as d:
            tmp=Path(d);root=tmp/'run';root.mkdir();out=root/'phase';out.mkdir()
            proc=tmp/'proc';proc.mkdir();coordinator=proc/'123';coordinator.mkdir()
            ticks='457' if fault=='coordinator_ticks' else '456'
            (coordinator/'stat').write_text('123 (coordinator) '+' '.join(['T']+['0']*18+[ticks]))
            (coordinator/'comm').write_bytes(b'coordinator\n')
            (coordinator/'cmdline').write_bytes(b'coordinator\0')
            cpu=tmp/'cpu2';(cpu/'topology').mkdir(parents=True)
            (cpu/'online').write_text('1');(cpu/'topology/thread_siblings_list').write_text('2')
            deadline=1100 if fault=='expired_margin' else 10000
            lease={'owner':q.OWNER,'state':'RESERVED','deadline':deadline,
                   'coordinator_pid':123,'coordinator_ticks':'456'}
            q.write(root/'reservation.json',lease)
            record,_,_=Record().record(root)
            record['deadline']=deadline
            record['lease_sha256']=q.sha(root/'reservation.json')
            for s in record['cleanup_timer_schedules']:s['fire_epoch']=deadline
            if fault=='timer_too_close':record['cleanup_timer_schedules'][0]['fire_epoch']=1200
            exact_exec=b'{ path=/reviewed/cleanup.py ; argv[]=/reviewed/cleanup.py ; }\n'
            record['cleanup_services'][0]['exec_start_sha256']=q.hashlib.sha256(exact_exec).hexdigest()
            if fault=='lease_changed':
                lease['state']='RELEASED';q.write(root/'reservation.json',lease)
            if fault=='leftover_profiler':
                leftover=proc/'321';leftover.mkdir()
                (leftover/'comm').write_bytes(b'agent\n')
                (leftover/'cmdline').write_bytes(b'parca-agent\0--bearer-token\0SECRET-DO-NOT-RETAIN\0')
            def fake_path(value):
                value=str(value)
                if value=='/proc':return proc
                if value=='/sys/devices/system/cpu/cpu2':return cpu
                raise AssertionError('Unexpected host path: '+value)
            def fake_run(argv,**kwargs):
                if argv==['docker','ps','-q']:
                    stdout=b'container-id\n' if fault=='docker' else b''
                elif argv[-2:]==['--property=ExecStart','--value']:
                    stdout=b'/unreviewed/path\n' if fault=='exec_start' else exact_exec
                elif argv[2].endswith('.timer'):
                    s=next(x for x in record['cleanup_timer_schedules'] if x['unit']==argv[2])
                    state={'ActiveState':'active','Unit':'release.service',
                           'NextElapseUSecRealtime':s['NextElapseUSecRealtime'],
                           'NextElapseUSecMonotonic':s['NextElapseUSecMonotonic']}
                    if fault=='timer_schedule':state['NextElapseUSecMonotonic']='changed'
                    if fault=='timer_inactive':state['ActiveState']='inactive'
                    stdout=''.join(k+'='+v+'\n' for k,v in state.items()).encode()
                elif argv[2]=='snap.parca-agent.parca-agent-svc.service':
                    state={'ActiveState':'inactive','SubState':'dead','MainPID':'0',
                           'CPUAffinity':'','AllowedCPUs':''}
                    if fault=='active_profiler':state['ActiveState']='active'
                    stdout=''.join(k+'='+v+'\n' for k,v in state.items()).encode()
                else:raise AssertionError('Unexpected real command: '+repr(argv))
                return SimpleNamespace(returncode=0,stdout=stdout,stderr=b'')
            def fake_append(path,value):
                with path.open('a') as stream:
                    stream.write(json.dumps(value)+'\n')
            with patch.object(q,'Path',side_effect=fake_path), \
                 patch.object(q,'read',side_effect=lambda p:json.loads(p.read_text())), \
                 patch.object(q,'write',side_effect=lambda p,v:p.write_text(json.dumps(v))), \
                 patch.object(q,'append',side_effect=fake_append), \
                 patch.object(q,'sha',side_effect=lambda p:q.hashlib.sha256(p.read_bytes()).hexdigest()), \
                 patch.object(q.time,'time',return_value=1000), \
                 patch.object(q.os,'sched_getaffinity',return_value={0}), \
                 patch.object(q.platform,'machine',return_value='aarch64'), \
                 patch.object(q.subprocess,'run',side_effect=fake_run):
                if fault:
                    with self.assertRaises(ValueError):q.isolation(root,record,out,'before')
                else:
                    q.isolation(root,record,out,'before')
                    self.assertTrue(json.loads((out/'isolation/before-snapshot.json').read_text())['passed'])
            for p in out.rglob('*'):
                if p.is_file():self.assertNotIn('SECRET-DO-NOT-RETAIN',p.read_text())

    def test_valid_calendar_and_monotonic_timer_paths(self):self.exercise()

    def test_isolation_negatives(self):
        for fault in ('timer_schedule','timer_inactive','timer_too_close','exec_start','active_profiler',
                      'leftover_profiler','lease_changed','expired_margin','coordinator_ticks','docker'):
            with self.subTest(fault=fault):self.exercise(fault)


if __name__=='__main__':
    unittest.main(verbosity=2)
