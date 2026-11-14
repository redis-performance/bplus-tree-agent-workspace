"""Correctness-only tests. No workload execution, clocks, or fleet operations."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
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


if __name__=='__main__':
    unittest.main(verbosity=2)
