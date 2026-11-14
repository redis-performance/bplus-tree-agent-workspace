"""Offline synthetic evidence only: no collector main, subprocess, clock or workload."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SOURCE=Path(__file__).resolve().parents[1]/'fleet_h8_profiler_off_screen.py'
spec=importlib.util.spec_from_file_location('h8screen',SOURCE)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
MEMORY={c:40000 for c in h.q4.CASES}
BINDING={'isolation_sha256':'a'*64,'q4_review_sha256':'b'*64}
RECORD={'coordinator':{'pid':123,'start_ticks':'456'}}


def sample(phase=h.PHASES[0],variants=None):
    variants=list('ABC') if variants is None else variants
    cohort=h.cohort_for(phase);scale=1 if cohort=='native' else 5;rows=[]
    for variant in variants:
        pin=h.BUILDS[cohort]['variants'][variant]
        for case,count in h.q4.CASES.items():
            for block in range(3):
                for slot,label in enumerate('ABBA'):
                    rows.append(dict(case=case,seed=17,ops=count*scale*500,
                        elapsed_ns=970000000 if case=='hit' and label=='B' else 1000000000,
                        hits=0 if case=='miss' else count*scale*500,
                        score_sum=count*scale*125250 if case=='score' else 0,owned_bytes=40000,
                        phase=phase,cohort=cohort,block=block,slot=slot,label=label,sweeps=count*scale,
                        source_sha256=h.q4.BASE_SOURCE if label=='A' else pin['source_sha256'],
                        referee_sha256=h.q4.REFEREE_PINS['lookup.c'],variant=variant,
                        candidate_source_sha256=pin['source_sha256'],
                        binary_sha256=h.q4.BASELINES[cohort][1] if label=='A' else pin['binary_sha256']))
    return rows


def process_artifacts(root,out,specs):
    (out/'isolation').mkdir()
    for pid,spec in enumerate(specs,1000):
        stem=spec['stem'];guarantee={'scope':'preexec','cpu':2,'verified':True}
        observation={'available':True,'affinity':[2]}
        launch={'argv':spec['argv'],'stem':stem,'started':2,'binary_sha256':spec['binary_sha256'],
                'preflight_passed':True}
        command=dict(launch,returncode=0,finished=3,pid=pid,child_affinity_guarantee=guarantee,
            child_affinity_observation=observation,
            rusage={k:0 for k in ('ru_utime','ru_stime','ru_minflt','ru_majflt','ru_nvcsw','ru_nivcsw')})
        h.append(out/'launches.jsonl',launch);h.append(out/'commands.jsonl',command)
        h.append(out/'child-starts.jsonl',{'stem':stem,'pid':pid,'guarantee':guarantee,'observation':observation})
        h.write(out/(stem+'.stdout'),spec['raw']);(out/(stem+'.stderr')).write_text('')
        for boundary,checked in [('pre',1),('post',4)]:
            h.write(out/'isolation'/(stem+'-'+boundary+'-snapshot.json'),
                {'passed':True,'controller_affinity':[0],'cpu2_online':'1','cpu2_siblings':'2',
                 'parca_processes':[],'coordinator':{'pid':123,'state':'T','start_ticks':'456'},'checked':checked})


def q4_fixture(root):
    overall=root/'Q4-profiler-off';overall.mkdir()
    expected={'phases':list(h.q4.PHASES),'collector_sha256':h.Q4_PIN,
              'isolation_sha256':BINDING['isolation_sha256'],'review_sha256':BINDING['q4_review_sha256'],
              'baseline_only':True,'source_adoption':False}
    h.write(overall/'admission.json',expected)
    h.write(overall/'result.json',{'status':'PASS','completed_phases':list(h.q4.PHASES),
                                 'source_adoption':False,'candidate_executed':False})
    for phase in h.q4.PHASES:
        out=root/phase;out.mkdir();cohort,seed,scale=h.q4.phase_spec(phase)
        binary,binary_hash=h.q4.BASELINES[cohort];rows=[];specs=[]
        for case in h.q4.CASES:
            specs.append({'stem':'verify-'+case,
                'argv':['taskset','-c','2',str(root/binary),'verify',case,str(seed),'1'],
                'binary_sha256':binary_hash,
                'raw':{'verified':True,'case':case,'seed':seed,'members':500,'owned_bytes':40000}})
        for case,count in h.q4.CASES.items():
            for block in range(3):
                for slot,label in enumerate('ABBA'):
                    row=dict(case=case,seed=seed,ops=count*scale*500,elapsed_ns=1000000000,
                        hits=0 if case=='miss' else count*scale*500,
                        score_sum=count*scale*125250 if case=='score' else 0,owned_bytes=40000,
                        phase=phase,cohort=cohort,block=block,slot=slot,label=label,sweeps=count*scale,
                        source_sha256=h.q4.BASE_SOURCE,referee_sha256=h.q4.REFEREE_PINS['lookup.c'],
                        binary_sha256=binary_hash)
                    rows.append(row);h.append(out/'aa.jsonl',row)
                    specs.append({'stem':f'aa-{case}-{block}-{slot}',
                        'argv':['taskset','-c','2',str(root/binary),'measure',case,str(seed),str(count*scale)],
                        'binary_sha256':binary_hash,'raw':{k:row[k] for k in h.q4.RAW_FIELDS}})
        h.write(out/'metadata.json',dict(expected,phase=phase,cohort=cohort,seed=seed,
            sweeps={k:v*scale for k,v in h.q4.CASES.items()},upstream=h.q4.UPSTREAM,
            source_sha256=h.q4.BASE_SOURCE,baseline_sha256=binary_hash,referee_pins=h.q4.REFEREE_PINS))
        h.write(out/'analysis.json',h.q4.analyse_rows(phase,rows))
        h.write(out/'result.json',{'status':'PASS','complete':True,'rows':72,
                                  'source_adoption':False,'candidate_executed':False})
        process_artifacts(root,out,specs)


def native_fixture(root):
    overall=root/'H8-profiler-off-screen';overall.mkdir()
    h.write(overall/'q4-evidence-pins.json',{'synthetic':'1'*64})
    out=root/h.PHASES[0];out.mkdir();rows=sample();specs=[]
    # B fails one guard block; A and C must be the sole derived target variants.
    for row in rows:
        if row['variant']=='B' and row['case']=='miss' and row['block']==0 and row['label']=='B':
            row['elapsed_ns']=1020000000
        h.append(out/'comparison.jsonl',row)
    report=h.compare_rows(h.PHASES[0],list('ABC'),rows,MEMORY)
    h.write(out/'analysis.json',report)
    h.write(out/'result.json',{'status':'COMPLETE','rows':216,'source_adoption':False})
    h.write(out/'metadata.json',{'binding':BINDING,'variants':list('ABC'),'phase':h.PHASES[0],
        'cohort':'native','seed':17,'sweeps':h.q4.CASES,'build_pins':h.BUILDS['native'],
        'baseline_sha256':h.q4.BASELINES['native'][1],'control_phase':'Q4-native-17',
        'q4_evidence_sha256':h.sha(overall/'q4-evidence-pins.json')})
    for variant in 'ABC':
        binary='bin/H8-native-'+variant;pin=h.BUILDS['native']['variants'][variant]
        for case in h.q4.CASES:
            specs.append({'stem':f'verify-{variant}-{case}',
                'argv':['taskset','-c','2',str(root/binary),'verify',case,'17','1'],
                'binary_sha256':pin['binary_sha256'],
                'raw':{'verified':True,'case':case,'seed':17,'members':500,'owned_bytes':40000}})
        for row in [r for r in rows if r['variant']==variant]:
            executed=h.q4.BASELINES['native'][0] if row['label']=='A' else binary
            specs.append({'stem':f'compare-{variant}-{row["case"]}-{row["block"]}-{row["slot"]}',
                'argv':['taskset','-c','2',str(root/executed),'measure',row['case'],'17',str(row['sweeps'])],
                'binary_sha256':row['binary_sha256'],'raw':{k:row[k] for k in h.q4.RAW_FIELDS}})
    process_artifacts(root,out,specs)


class Analysis(unittest.TestCase):
    def test_pure_native_and_target_models(self):
        with patch.object(h.time,'time',side_effect=AssertionError('clock')), \
             patch.object(h.subprocess,'run',side_effect=AssertionError('process')):
            for phase in h.PHASES:
                rows=sample(phase);before=copy.deepcopy(rows)
                report=h.compare_rows(phase,list('ABC'),rows,MEMORY)
                self.assertTrue(all(v['eligible'] for v in report['variants'].values()));self.assertEqual(rows,before)

    def test_strict_primary_guard_memory_and_duration(self):
        for case,elapsed,passed in [('hit',980000000,True),('hit',980000001,False),
                                    ('score',1010000000,True),('score',1010000001,False)]:
            rows=sample()
            for r in rows:
                if r['variant']=='A' and r['case']==case and r['label']=='B':r['elapsed_ns']=elapsed
            self.assertEqual(h.compare_rows(h.PHASES[0],list('ABC'),rows,MEMORY)['variants']['A']['eligible'],passed)
        for field,value in [('owned_bytes',40401),('elapsed_ns',249999999)]:
            rows=sample();rows[1][field]=value
            self.assertFalse(h.compare_rows(h.PHASES[0],list('ABC'),rows,MEMORY)['variants']['A']['eligible'])

    def test_malformed_count_model_pin_and_grid(self):
        for field,value in [('elapsed_ns',float('nan')),('ops',1),('hits',0),('score_sum',1),
             ('candidate_source_sha256','0'*64),('source_sha256','0'*64),('binary_sha256','0'*64),
             ('referee_sha256','0'*64),('variant','C'),('slot',True),('sweeps',1),('seed',43)]:
            rows=sample();rows[0][field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):h.compare_rows(h.PHASES[0],list('ABC'),rows,MEMORY)
        for rows in [sample()[:-1],sample()+sample()[:1],sample()[1:2]+sample()[:1]+sample()[2:]]:
            with self.assertRaises(ValueError):h.compare_rows(h.PHASES[0],list('ABC'),rows,MEMORY)
        rows=sample();rows[1]=copy.deepcopy(rows[0])
        with self.assertRaises(ValueError):h.compare_rows(h.PHASES[0],list('ABC'),rows,MEMORY)

    def test_target_selection_cannot_trust_forged_eligibility(self):
        rows=sample();report=h.compare_rows(h.PHASES[0],list('ABC'),rows,MEMORY)
        self.assertEqual(h.target_variants(report,rows,MEMORY),list('ABC'))
        report['variants']['B']['eligible']=False
        with self.assertRaises(ValueError):h.target_variants(report,rows,MEMORY)
        with self.assertRaises(ValueError):h.target_variants(report,rows[:72],MEMORY)

    def test_memory_must_match_q4_control_and_be_reproducible(self):
        rows=sample();rows[0]['owned_bytes']+=1
        with self.assertRaises(ValueError):h.compare_rows(h.PHASES[0],list('ABC'),rows,MEMORY)
        rows=sample();rows[1]['owned_bytes']+=1
        self.assertFalse(h.compare_rows(h.PHASES[0],list('ABC'),rows,MEMORY)['variants']['A']['eligible'])


class Evidence(unittest.TestCase):
    def test_all_q4_cohorts_required_and_reconstructed(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);q4_fixture(root)
            controls,pins=h.audit_q4(root,RECORD,BINDING)
            self.assertEqual(controls,{'native':MEMORY,'gcc15-lto':MEMORY});self.assertGreater(len(pins),1000)
            p=root/'Q4-profiler-off/result.json';result=h.read(p);result['status']='PARK';h.write(p,result)
            with self.assertRaises(ValueError):h.audit_q4(root,RECORD,BINDING)

    def test_q4_forged_pass_rejected_from_raw_noisy_grid(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);q4_fixture(root);p=root/h.q4.PHASES[0]/'aa.jsonl';rows=h.lines(p)
            rows[1]['elapsed_ns']=1100000000
            p.write_text(''.join(json.dumps(r)+'\n' for r in rows))
            with self.assertRaises(ValueError):h.audit_q4(root,RECORD,BINDING)

    def test_q4_missing_postflight_or_wrong_condition_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);q4_fixture(root)
            p=root/h.q4.PHASES[-1]/'isolation/verify-hit-post-snapshot.json'
            raw=p.read_bytes();p.unlink()
            with self.assertRaises(FileNotFoundError):h.audit_q4(root,RECORD,BINDING)
            p.write_bytes(raw)
            with self.assertRaises(ValueError):h.audit_q4(root,RECORD,{**BINDING,'isolation_sha256':'c'*64})

    def test_native_exact_join_derives_only_complete_passers(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);native_fixture(root)
            eligible,_=h.audit_native(root,RECORD,BINDING,{'native':MEMORY})
            self.assertEqual(eligible,['A','C'])
            p=root/h.PHASES[0]/'analysis.json';report=h.read(p);report['variants']['B']['eligible']=True;h.write(p,report)
            with self.assertRaises(ValueError):h.audit_native(root,RECORD,BINDING,{'native':MEMORY})

    def test_native_raw_and_command_tamper_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);native_fixture(root);p=root/h.PHASES[0]/'commands.jsonl';commands=h.lines(p)
            commands[0]['argv'][3]='unapproved-candidate'
            p.write_text(''.join(json.dumps(r)+'\n' for r in commands))
            with self.assertRaises(ValueError):h.audit_native(root,RECORD,BINDING,{'native':MEMORY})

    def test_one_shot_and_q4_import_pin(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);h.claim(root)
            with self.assertRaises(FileExistsError):h.claim(root)
            (root/h.PHASES[0]).mkdir()
            with self.assertRaises(ValueError):h.claim(root)
            wrong=root/'wrong.py';wrong.write_text('raise AssertionError("must not import")')
            with self.assertRaises(ValueError):h.load_q4(wrong)


if __name__=='__main__':unittest.main(verbosity=2)
