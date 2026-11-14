#!/usr/bin/env python3
"""Offline synthetic tests only: no perf, workload, service or real clock calls."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

SOURCE=Path(__file__).resolve().parents[1]/'fleet_variance_diagnostic.py'
spec=importlib.util.spec_from_file_location('variance',SOURCE)
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)


def csv_text(changes=None,omit=(),extra='',raw=False):
    changes=changes or {};lines=['# synthetic fixture, not a measurement']
    for event in v.EVENTS:
        if event in omit:continue
        fields=['100' if event!='task-clock' else '10.00','msec' if event=='task-clock' else '',event,'123456789','100.00','','']
        for key,value in changes.get(event,{}).items():fields[key]=value
        if raw:lines.append(f'{event}: -1: {10000000 if event=="task-clock" else fields[0]} 123456789 123456789')
        lines.append(','.join(fields))
    return '\n'.join(lines)+'\n'+extra


def workload(support=False):
    if support:return dict(verified=True,case='hit',seed=43,members=500,owned_bytes=14272)
    return dict(case='hit',seed=43,ops=125000000,elapsed_ns=3000000000,hits=125000000,score_sum=0,owned_bytes=14272)


def rows():
    return [dict(capture=f'D{i}',workload=workload(),counters=v.parse_counters(csv_text(raw=True)),process_wall_ns=4000000000) for i in range(4)]


class ParserTests(unittest.TestCase):
    def test_source_verified_verbose_in_output(self):
        result=v.parse_counters(csv_text(raw=True))
        self.assertEqual(result['unrounded_events'],sorted(v.EVENTS))
        self.assertEqual(result['events']['cycles:u']['unrounded_enabled_ns'],123456789)

    def test_no_raw_precision_is_explicit(self):
        result=v.parse_counters(csv_text())
        self.assertEqual(result['unrounded_events'],[])
        self.assertIsNone(result['events']['cycles:u']['unrounded_enabled_ns'])

    def test_all_event_omissions_rejected(self):
        for event in v.EVENTS:
            with self.subTest(event=event),self.assertRaises(ValueError):v.parse_counters(csv_text(omit=[event]))

    def test_duplicate_and_unknown(self):
        for extra in ('100,,cycles:u,123456789,100.00,,','100,,other,123456789,100.00,,'):
            with self.subTest(extra=extra),self.assertRaises(ValueError):v.parse_counters(csv_text(extra=extra))

    def test_invalid_values(self):
        for value in ('NaN','Infinity','-1','<not supported>','<not counted>','1.5','1e99999',str(2**64),''):
            with self.subTest(value=value),self.assertRaises(ValueError):v.parse_counters(csv_text({'cycles:u':{0:value}}))

    def test_zero_work_rejected(self):
        for event in ('cycles:u','instructions:u','task-clock'):
            with self.subTest(event=event),self.assertRaises(ValueError):v.parse_counters(csv_text({event:{0:'0'}}))

    def test_zero_misc_counts_valid(self):
        changes={e:{0:'0'} for e in v.EVENTS if e not in ('cycles:u','instructions:u','task-clock')}
        self.assertEqual(v.parse_counters(csv_text(changes))['events']['branch-misses:u']['count'],'0')

    def test_runtime_required_for_every_event(self):
        for event in v.EVENTS:
            for value in ('','0','-1','NaN','0.5'):
                with self.subTest(event=event,value=value),self.assertRaises(ValueError):v.parse_counters(csv_text({event:{3:value}}))

    def test_exact_scheduling_display(self):
        for value in ('99.99','0','100','100.000','NaN','101.00',''):
            with self.subTest(value=value),self.assertRaises(ValueError):v.parse_counters(csv_text({'minor-faults':{4:value}}))

    def test_group_runtime_and_units(self):
        for changes in ({'instructions:u':{3:'123456788'}},{'task-clock':{1:'ns'}},{'cycles:u':{1:'msec'}}):
            with self.subTest(changes=changes),self.assertRaises(ValueError):v.parse_counters(csv_text(changes))

    def test_verbose_unrounded_mismatch(self):
        for line in ('cycles:u: -1: 100 123456790 123456789','cycles:u: -1: 101 123456789 123456789',
                     'cycles:u: 2: 100 123456789 123456789','cycles:u: 100 123456789 123456789'):
            with self.subTest(line=line),self.assertRaises(ValueError):v.parse_counters(csv_text(),line)

    def test_raw_duplicate_and_unknown_timing(self):
        for verbose in ('cycles:u: -1: 100 123456789 123456789','time_enabled=123456790 time_running=123456789'):
            with self.subTest(verbose=verbose),self.assertRaises(ValueError):v.parse_counters(csv_text(raw=True),verbose)

    def test_raw_task_clock_rejects_zero_overflow_and_mismatch(self):
        for count in ('0',str(2**64),'20000000','9994999','10005001'):
            fixture=csv_text(raw=True).replace('task-clock: -1: 10000000 ',f'task-clock: -1: {count} ')
            with self.subTest(count=count),self.assertRaises(ValueError):v.parse_counters(fixture)

    def test_raw_task_clock_two_decimal_rounding_bounds(self):
        for count in ('9995000','9999999','10000001','10005000'):
            fixture=csv_text(raw=True).replace('task-clock: -1: 10000000 ',f'task-clock: -1: {count} ')
            with self.subTest(count=count):
                self.assertEqual(v.parse_counters(fixture)['events']['task-clock']['count'],'10.00')

    def test_partial_raw_read_sets_rejected(self):
        fixture=csv_text(raw=True)
        for omitted in v.EVENTS:
            partial='\n'.join(line for line in fixture.splitlines() if not line.startswith(omitted+':'))
            with self.subTest(omitted=omitted),self.assertRaises(ValueError):v.parse_counters(partial)
        with self.assertRaises(ValueError):
            v.parse_counters(csv_text(),'cycles:u: -1: 100 123456789 123456789')

    def test_unknown_csv_layout(self):
        for extra in ('99,,cycles:u','1,2,3,4,5,6,7,8','cycles:u: nonsense'):
            with self.subTest(extra=extra),self.assertRaises(ValueError):v.parse_counters(csv_text(extra=extra))


class AnalysisTests(unittest.TestCase):
    def test_models(self):
        v.check_workload(workload(True),True);v.check_workload(workload(),False)
        for support in (True,False):
            keys=('case','seed','owned_bytes','members','verified') if support else ('case','seed','owned_bytes','ops','hits','score_sum','elapsed_ns')
            for key in keys:
                raw=workload(support);raw[key]='wrong'
                with self.subTest(support=support,key=key),self.assertRaises((ValueError,TypeError)):v.check_workload(raw,support)

    def test_descriptive_only_and_clock_free(self):
        with patch.object(v.time,'time',side_effect=AssertionError('clock')),patch.object(v.time,'monotonic_ns',side_effect=AssertionError('clock')),patch.object(v.subprocess,'Popen',side_effect=AssertionError('process')):
            result=v.describe(rows())
        self.assertEqual(result['ranges']['cycles:u']['range_over_median'],0)
        self.assertEqual(result['derived'][0]['user_cycles_per_instruction'],1)
        self.assertFalse(result['qualification']);self.assertFalse(result['source_adoption'])
        self.assertEqual(result['prior_H2_Q4'],'PARK retained')

    def test_exact_four_in_order(self):
        original=rows()
        for altered in (original[:3],original+original[:1],list(reversed(original)),[original[0]]*4):
            with self.subTest(altered=len(altered)),self.assertRaises(ValueError):v.describe(altered)

    def test_describe_revalidates_parsed_scheduling(self):
        for field,value in (('running_display','99.99'),('runtime_ns',0),('runtime_ns',123),
                            ('unrounded_enabled_ns',123),('unit','wrong'),('count','NaN'),('count','0.5')):
            data=rows();data[0]['counters']['events']['cycles:u'][field]=value
            with self.subTest(field=field,value=value),self.assertRaises(ValueError):v.describe(data)

    def test_describe_rejects_partial_raw_precision(self):
        data=rows()
        for field in ('unrounded_enabled_ns','unrounded_running_ns'):
            data[0]['counters']['events']['cycles:u'][field]=None
        with self.assertRaises(ValueError):v.describe(data)

    def test_zero_software_median(self):
        data=rows()
        for row in data:row['counters']['events']['major-faults']['count']='0'
        self.assertIsNone(v.describe(data)['ranges']['major-faults']['range_over_median'])

    def test_fixed_command(self):
        for support,count,mode in ((True,'1','verify'),(False,'250000','measure')):
            command=v.capture_command('/reviewed','counter.csv',support)
            self.assertEqual(command[0],v.PERF)
            self.assertEqual(command[-4:],[mode,'hit','43',count])
            self.assertEqual(command[command.index('--')+1:command.index('--')+4],[v.TASKSET,'-c','2'])
            self.assertEqual(command[command.index('-e')+1],'{cycles:u,instructions:u,branches:u,branch-misses:u},task-clock,context-switches,cpu-migrations,minor-faults,major-faults')
            self.assertIn('--no-scale',command)
            self.assertNotIn('-r',command)
        self.assertEqual(v.LOCALE,{'LC_ALL':'C','LANG':'C'})

    def test_claim_single_use(self):
        with tempfile.TemporaryDirectory() as directory:
            v.claim(directory)
            with self.assertRaises(FileExistsError):v.claim(directory)

    def test_dependency_pin(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'changed.py';path.write_text('raise Exception("must not import")')
            with self.assertRaises(ValueError):v.load_q4(path)

    def test_affinity_enforced_and_race_honest(self):
        with patch.object(v.os,'sched_setaffinity') as setter,patch.object(v.os,'sched_getaffinity',return_value={0}):
            v.pin_perf_cpu();setter.assert_called_once_with(0,{0})
            self.assertEqual(v.observe_perf(999)['affinity'],[0])
        with patch.object(v.os,'sched_getaffinity',side_effect=ProcessLookupError):
            self.assertEqual(v.observe_perf(999)['affinity'],None)
        with patch.object(v.os,'sched_getaffinity',return_value={2}):
            with self.assertRaises(ValueError):v.observe_perf(999)


class OrchestrationTests(unittest.TestCase):
    def exercise(self,bad_stage=None,reaped_interrupt=False):
        # Real temporary JSON I/O only. All OS process, identity, isolation,
        # clocks, accounting and affinity operations are deterministic mocks.
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);pin='a'*64;version=b'synthetic version\n'
            review=dict(schema_version=1,decision='APPROVED',reviewer_role='independent reviewer',
                collector_sha256=pin,protocol_sha256=pin,q4_collector_sha256=v.Q4_PIN,isolation_sha256=pin,
                q4_review_sha256=pin,perf_path=v.PERF,taskset_path=v.TASKSET,locale_policy=v.LOCALE,
                events=v.EVENT_SPEC,baseline_sha256=v.BASELINE[1],source_sha256=v.q4.BASE_SOURCE,
                perf_sha256=pin,taskset_sha256=pin,kernel_release='synthetic',
                perf_version_stdout_sha256=hashlib.sha256(version).hexdigest(),
                taskset_version_stdout_sha256=hashlib.sha256(version).hexdigest())
            for name,value in (('isolation',{}),('q4-review',{}),('review',review)):
                (root/name).write_text(json.dumps(value))
            argv=['collector','--root',directory,'--collector-sha256',pin,'--protocol-sha256',pin,
                '--isolation-record',str(root/'isolation'),'--isolation-sha256',pin,
                '--q4-review',str(root/'q4-review'),'--q4-review-sha256',pin,
                '--diagnostic-review',str(root/'review'),'--review-sha256',pin]
            calls=[]
            class FakeProcess:
                pid=999;returncode=0;waited=False
                def __init__(self,command,**kwargs):
                    stage='support' if not calls else 'D'+str(len(calls)-1)
                    calls.append((stage,command,kwargs['env']))
                    self.stage=stage
                    self.returncode=1 if bad_stage==stage else 0
                    raw=workload(stage=='support');kwargs['stdout'].write(json.dumps(raw).encode());kwargs['stdout'].flush()
                    Path(command[command.index('-o')+1]).write_text(csv_text(raw=True))
                    if kwargs['preexec_fn'] is not v.pin_perf_cpu:raise AssertionError('wrong preexec')
                def wait(self,timeout=None):
                    if reaped_interrupt and not self.waited:
                        self.waited=True;raise KeyboardInterrupt('synthetic after reaping')
                    return self.returncode
                def poll(self):return self.returncode
            usage=SimpleNamespace(**{k:0 for k in ('ru_utime','ru_stime','ru_minflt','ru_majflt','ru_nvcsw','ru_nivcsw')})
            from contextlib import ExitStack
            with ExitStack() as stack:
                mocks=[patch('sys.argv',argv),patch.object(v,'sha',return_value=pin),
                    patch.object(v.q4,'validate_record'),patch.object(v.q4,'identities'),
                    patch.object(v.platform,'release',return_value='synthetic'),
                    patch.object(v.subprocess,'run',return_value=SimpleNamespace(returncode=0,stdout=version,stderr=b'')),
                    patch.object(v.subprocess,'Popen',side_effect=FakeProcess),
                    patch.object(v,'observe_perf',return_value={'available':True,'affinity':[0]}),
                    patch.object(v.resource,'getrusage',return_value=usage),patch.object(v.time,'time',return_value=1),
                    patch.object(v.time,'monotonic_ns',side_effect=range(1,100)),patch('builtins.print')]
                for mock in mocks:stack.enter_context(mock)
                isolation=stack.enter_context(patch.object(v.q4,'isolation'))
                kill=stack.enter_context(patch.object(v.os,'killpg'))
                if bad_stage or reaped_interrupt:
                    with self.assertRaises(ValueError):v.main()
                else:v.main()
                self.assertTrue(all(call[2]['LC_ALL']=='C' and call[2]['LANG']=='C' for call in calls))
                self.assertIn(calls[-1][0]+'-post',[x.args[-1] for x in isolation.call_args_list])
                kill.assert_not_called()
            result=json.loads((root/v.PHASE/'result.json').read_text())
            return calls,result

    def test_fixed_support_plus_four(self):
        calls,result=self.exercise()
        self.assertEqual([x[0] for x in calls],['support','D0','D1','D2','D3'])
        self.assertEqual(result['status'],'COMPLETE_DIAGNOSTIC');self.assertFalse(result['qualification'])

    def test_support_failure_stops_all_captures(self):
        calls,result=self.exercise('support')
        self.assertEqual(len(calls),1);self.assertEqual(result['status'],'INCOMPLETE')
        self.assertTrue(result['attempt_consumed'])

    def test_midsequence_failure_not_replaced(self):
        calls,result=self.exercise('D1')
        self.assertEqual([x[0] for x in calls],['support','D0','D1'])
        self.assertEqual(result['completed_captures'],1)

    def test_reaped_child_never_signaled(self):
        calls,result=self.exercise(reaped_interrupt=True)
        self.assertEqual(len(calls),1);self.assertEqual(result['status'],'INCOMPLETE')


if __name__=='__main__':unittest.main(verbosity=2)
