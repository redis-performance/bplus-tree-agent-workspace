#!/usr/bin/env python3
"""Prepared baseline-only process-counter diagnostic. No qualification or retry."""
import argparse
import csv
from decimal import Decimal, InvalidOperation
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import re
import resource
import signal
import statistics
import subprocess
import time

EXP=Path('experiments/ARM-LOOKUP-CONT-001')
PROTOCOL=EXP/'diagnostic-variance/PROTOCOL.md'
PHASE='diagnostic-variance-43'
Q4_PIN='531bbabc2b50e26737a0be44773e7d195fa2576ba149e75bdf63a1a5698da743'
PERF='/usr/lib/linux-tools/6.14.0-1010-aws/perf'
TASKSET='/usr/bin/taskset'
LOCALE={'LC_ALL':'C','LANG':'C'}
HARDWARE=('cycles:u','instructions:u','branches:u','branch-misses:u')
SOFTWARE=('task-clock','context-switches','cpu-migrations','minor-faults','major-faults')
EVENTS=HARDWARE+SOFTWARE
EVENT_SPEC='{'+','.join(HARDWARE)+'},'+','.join(SOFTWARE)
BASELINE=('bin/gcc15-lto/lookup','77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb')
OWNED_BYTES=14272

def load_q4(path):
    if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=Q4_PIN:
        raise ValueError('Reviewed isolation dependency changed')
    spec=importlib.util.spec_from_file_location('variance_q4',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

q4=load_q4(Path(__file__).with_name('fleet_profiler_off_qualification.py'))
require,read,write,append,sha=q4.require,q4.read,q4.write,q4.append,q4.sha


def number(text,positive=False,integer=False):
    try:value=Decimal(text)
    except InvalidOperation as error:raise ValueError('Invalid counter number') from error
    require(value.is_finite() and 0<=value<2**64 and (not positive or value>0),'Nonfinite/negative/zero counter')
    require(not integer or value==value.to_integral_value(),'Nonintegral count/runtime')
    return value


def parse_counters(text,verbose=''):
    """Pure strict CSV parser. No event omission, scaling, renamed alias or fallback."""
    events={};footers={};raw_reads=[];csv_lines=[]
    # Linux v6.14 read_counter_cpu writes verbose reads to stat_config.output,
    # hence the -o file. The CPU-map entry is -1 for per-process collection.
    pattern=re.compile(r'^('+ '|'.join(re.escape(e) for e in EVENTS)+r'):\s+(-?\d+):\s+(\d+)\s+(\d+)\s+(\d+)\s*$')
    for line in text.splitlines():
        stripped=line.strip();match=pattern.fullmatch(stripped)
        if match:raw_reads.append(match.groups())
        else:csv_lines.append(line)
    for fields in csv.reader(csv_lines):
        if not fields or not any(v.strip() for v in fields) or fields[0].lstrip().startswith('#'):
            continue
        fields=[v.strip() for v in fields]
        if len(fields)==2 and fields[1] in ('seconds time elapsed','seconds user','seconds sys'):
            require(fields[1] not in footers,'Duplicate perf footer')
            footers[fields[1]]=str(number(fields[0]))
            continue
        require(5<=len(fields)<=7,'Missing runtime/running field or unsupported CSV schema')
        count,unit,event,runtime,running=fields[:5]
        require(event in EVENTS and event not in events,'Missing/duplicate/unexpected event')
        require(unit==('msec' if event=='task-clock' else ''),'Unexpected event unit')
        value=number(count,positive=event in ('task-clock','cycles:u','instructions:u'),integer=event!='task-clock')
        elapsed=number(runtime,positive=True,integer=True)
        require(running=='100.00','Event lacks exact displayed100.00% scheduling')
        events[event]={'count':str(value),'unit':unit,'runtime_ns':int(elapsed),'running_display':running,
                       'unrounded_enabled_ns':None,'unrounded_running_ns':None}
    require(set(events)==set(EVENTS),'All nine events required')
    require(len({events[e]['runtime_ns'] for e in HARDWARE})==1,'Strong hardware group runtime mismatch')
    # Debug attr/error messages are on stderr; any additional raw reads there
    # must obey the same source-verified grammar and cannot duplicate -o reads.
    for line in verbose.splitlines():
        stripped=line.strip();match=pattern.fullmatch(stripped)
        if match:raw_reads.append(match.groups())
        elif re.search(r'\b(?:time_enabled|time_running)\s*[:=]\s*\d',stripped) or \
             any(stripped.startswith(event+':') for event in EVENTS):
            raise ValueError('Unrecognized explicit event timing/read evidence')
    seen=set()
    for event,cpu,raw_count,enabled,running in raw_reads:
        require(cpu=='-1','Unexpected per-CPU raw read in process capture')
        require(event not in seen,'Duplicate verbose event read')
        seen.add(event);enabled=int(number(enabled,positive=True,integer=True))
        running=int(number(running,positive=True,integer=True))
        require(enabled==running==events[event]['runtime_ns'],'Raw enabled/running mismatch')
        if event!='task-clock':require(Decimal(raw_count)==Decimal(events[event]['count']),'Unscaled raw count mismatch')
        events[event]['unrounded_enabled_ns']=enabled;events[event]['unrounded_running_ns']=running
    return {'events':events,'strong_group_runtime_ns':events[HARDWARE[0]]['runtime_ns'],
            'displayed_full_scheduling':True,'unrounded_events':sorted(seen),'perf_footers':footers}


def check_workload(raw,support):
    if support:
        require(set(raw)=={'verified','case','seed','members','owned_bytes'} and raw['verified'] is True and
                raw['case']=='hit' and type(raw['seed']) is int and raw['seed']==43 and
                type(raw['members']) is int and raw['members']==500 and
                type(raw['owned_bytes']) is int and raw['owned_bytes']==OWNED_BYTES,'Support workload/model mismatch')
    else:
        q4.check_raw(raw,'hit',43,250000)
        require(raw['owned_bytes']==OWNED_BYTES,'Frozen memory model mismatch')


def capture_command(root,counters,support):
    return [PERF,'stat','-vv','--no-scale','--no-big-num','-x,','-e',EVENT_SPEC,'-o',str(counters),
            '--',TASKSET,'-c','2',str(Path(root)/BASELINE[0]),
            'verify' if support else 'measure','hit','43','1' if support else '250000']


def describe(rows):
    """Four captures, fixed order. Descriptive only; deliberately no acceptance gate."""
    require([r['capture'] for r in rows]==['D0','D1','D2','D3'],'Incomplete/reordered diagnostic captures')
    series={event:[] for event in EVENTS}
    series.update(inner_elapsed_ns=[],process_wall_ns=[])
    derived=[]
    for row in rows:
        check_workload(row['workload'],False)
        require(type(row['process_wall_ns']) is int and row['process_wall_ns']>0,'Invalid wrapper wall duration')
        counters=row['counters']['events']
        require(set(counters)==set(EVENTS),'Missing parsed counters')
        values={k:number(counters[k]['count'],integer=k!='task-clock') for k in EVENTS}
        for event,entry in counters.items():
            require(entry['unit']==('msec' if event=='task-clock' else '') and
                    entry['running_display']=='100.00' and type(entry['runtime_ns']) is int and
                    0<entry['runtime_ns']<2**64,'Invalid parsed scheduling/unit')
            enabled,running=entry['unrounded_enabled_ns'],entry['unrounded_running_ns']
            require((enabled is None and running is None) or
                    (type(enabled) is int and type(running) is int and
                     enabled==running==entry['runtime_ns']),'Invalid parsed unrounded scheduling')
        require(len({counters[e]['runtime_ns'] for e in HARDWARE})==1,'Parsed group runtime mismatch')
        require(values['cycles:u']>0 and values['instructions:u']>0 and values['task-clock']>0,
                'Nonpositive work count')
        for event in EVENTS:series[event].append(float(values[event]))
        series['inner_elapsed_ns'].append(row['workload']['elapsed_ns'])
        series['process_wall_ns'].append(row['process_wall_ns'])
        derived.append({'capture':row['capture'],
            'user_cycles_per_instruction':float(values['cycles:u']/values['instructions:u']),
            'branch_misses_per_branch':float(values['branch-misses:u']/values['branches:u']) if values['branches:u'] else None,
            'task_clock_over_perf_wrapper_wall':float(values['task-clock']*1000000/row['process_wall_ns']),
            'minor_plus_major_faults':int(values['minor-faults']+values['major-faults'])})
    ranges={}
    for name,values in series.items():
        median=statistics.median(values)
        ranges[name]={'minimum':min(values),'maximum':max(values),'median':median,
                      'range_over_median':(max(values)-min(values))/median if median else None}
    return {'status':'FOUR_VALID_CAPTURES','captures':4,'ranges':ranges,'derived':derived,
            'interpretation':'Descriptive new captures only; no cause or variance episode is automatically classified',
            'qualification':False,'source_adoption':False,'prior_H2_Q4':'PARK retained'}


def claim(root):
    out=Path(root)/PHASE;out.mkdir();return out


def pin_perf_cpu():
    os.sched_setaffinity(0,{0});require(os.sched_getaffinity(0)=={0},'Perf controller must remain CPU0')


def observe_perf(pid):
    try:affinity=sorted(os.sched_getaffinity(pid))
    except ProcessLookupError:return {'available':False,'affinity':None,'reason':'perf process no longer observable'}
    require(affinity==[0],'Perf wrapper escaped CPU0');return {'available':True,'affinity':affinity}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for arg in ('root','collector-sha256','protocol-sha256','isolation-record','isolation-sha256',
                'q4-review','q4-review-sha256','diagnostic-review','review-sha256'):
        p.add_argument('--'+arg,required=True)
    args=p.parse_args();root=Path(args.root).resolve();out=claim(root)
    binding={'collector_sha256':args.collector_sha256,'protocol_sha256':args.protocol_sha256,
             'q4_collector_sha256':Q4_PIN,'isolation_sha256':args.isolation_sha256,
             'q4_review_sha256':args.q4_review_sha256,'diagnostic_review_sha256':args.review_sha256}
    write(out/'admission.json',dict(binding,phase=PHASE,qualification=False,source_adoption=False))
    completed=[];stage='admission'
    try:
        isolation_path=Path(args.isolation_record).resolve();q4_review_path=Path(args.q4_review).resolve()
        review_path=Path(args.diagnostic_review).resolve()
        record=read(isolation_path);q4_review=read(q4_review_path);review=read(review_path)
        q4.validate_record(record,q4_review,root,args.isolation_sha256,Q4_PIN)
        require(review['schema_version']==1 and review['decision']=='APPROVED' and
                type(review['reviewer_role']) is str and review['reviewer_role'].strip() and
                all(review[k]==v for k,v in binding.items() if k!='diagnostic_review_sha256') and
                review['perf_path']==PERF and review['taskset_path']==TASKSET and review['locale_policy']==LOCALE and
                review['events']==EVENT_SPEC and review['baseline_sha256']==BASELINE[1] and
                review['source_sha256']==q4.BASE_SOURCE,'Diagnostic review/identity mismatch')
        environment=dict(os.environ,**LOCALE)
        def identities():
            q4.identities(root,Q4_PIN,isolation_path,args.isolation_sha256,q4_review_path,args.q4_review_sha256,record)
            require(sha(__file__)==args.collector_sha256 and sha(root/PROTOCOL)==args.protocol_sha256 and
                    sha(review_path)==args.review_sha256,'Diagnostic collector/protocol/review changed')
            require(sha(PERF)==review['perf_sha256'] and sha(TASKSET)==review['taskset_sha256'] and
                    platform.release()==review['kernel_release'],'Perf/launcher/kernel identity changed')
        identities();q4.isolation(root,record,out,'metadata-pre')
        for tool in ('perf','taskset'):
            binary=PERF if tool=='perf' else TASKSET
            command=[binary,'--version'];result=subprocess.run(command,capture_output=True,env=environment,timeout=30)
            (out/(tool+'-version.stdout')).write_bytes(result.stdout)
            (out/(tool+'-version.stderr')).write_bytes(result.stderr)
            append(out/'metadata-commands.jsonl',{'argv':command,'returncode':result.returncode,'locale_policy':LOCALE})
            require(result.returncode==0 and not result.stderr and
                    hashlib.sha256(result.stdout).hexdigest()==review[tool+'_version_stdout_sha256'],'Tool version differs')
        write(out/'metadata.json',{'binding':binding,'events':EVENT_SPEC,'locale_policy':LOCALE,
            'kernel_release':review['kernel_release'],'perf_sha256':review['perf_sha256'],
            'taskset_sha256':review['taskset_sha256'],'baseline_sha256':BASELINE[1],
            'source_sha256':q4.BASE_SOURCE,'referee_pins':q4.REFEREE_PINS,
            'scope':'whole taskset/baseline process; starts CPU0 and migrates to CPU2 before baseline exec',
            'rusage_scope':'perf wrapper plus descendants; incomparable to Q4 baseline-child diagnostics',
            'qualification':False,'prior_H2_Q4':'PARK retained'})
        identities();q4.isolation(root,record,out,'metadata-post')
        for stage in ('support','D0','D1','D2','D3'):
            support=stage=='support';identities();q4.isolation(root,record,out,stage+'-pre')
            counterfile=out/(stage+'.counters.csv')
            require(not counterfile.exists(),'Counter capture already exists')
            command={'capture':stage,'argv':capture_command(root,counterfile,support),
                'locale_policy':LOCALE,'started':time.time(),'perf_preexec_cpu':0,
                'launcher_transition':'taskset starts on CPU0; baseline exec constrained to CPU2; counted',
                'baseline_affinity_observation':'launcher contract only; no fabricated benchmark PID observation'}
            append(out/'launches.jsonl',command)
            proc=None;before=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.monotonic_ns()
            try:
                with (out/(stage+'.stdout')).open('wb') as stdout,(out/(stage+'.stderr')).open('wb') as stderr:
                    proc=subprocess.Popen(command['argv'],stdout=stdout,stderr=stderr,env=environment,
                                          preexec_fn=pin_perf_cpu,start_new_session=True)
                    command['pid']=proc.pid;command['perf_affinity_verified_preexec']=True
                    command['perf_affinity_observation']=observe_perf(proc.pid)
                    append(out/'child-starts.jsonl',{'capture':stage,'pid':proc.pid,
                        'guarantee_cpu':0,'observation':command['perf_affinity_observation']})
                    proc.wait(timeout=240)
            except BaseException as error:
                command['error']=type(error).__name__+': '+str(error)
                if proc is not None:
                    if proc.poll() is None:
                        try:os.killpg(proc.pid,signal.SIGKILL)
                        except ProcessLookupError:pass
                    proc.wait()
            wall=time.monotonic_ns()-wall;after=resource.getrusage(resource.RUSAGE_CHILDREN)
            command.update(returncode=None if proc is None else proc.returncode,finished=time.time(),process_wall_ns=wall)
            command['perf_wrapper_rusage']={k:getattr(after,k)-getattr(before,k) for k in
                ('ru_utime','ru_stime','ru_minflt','ru_majflt','ru_nvcsw','ru_nivcsw')}
            append(out/'commands.jsonl',command)
            identities();q4.isolation(root,record,out,stage+'-post')
            require(command['returncode']==0 and 'error' not in command,'Perf/workload failed')
            raw=read(out/(stage+'.stdout'));check_workload(raw,support)
            counters=parse_counters(counterfile.read_text(),(out/(stage+'.stderr')).read_text())
            row={'capture':stage,'workload':raw,'counters':counters,'process_wall_ns':wall,
                 'perf_wrapper_rusage':command['perf_wrapper_rusage']}
            write(out/(stage+'.validated.json'),row)
            if not support:completed.append(row)
            print(stage,'counter/model gates passed',flush=True)
        write(out/'analysis.json',describe(completed))
        write(out/'result.json',{'status':'COMPLETE_DIAGNOSTIC','captures':4,'qualification':False,
              'source_adoption':False,'prior_H2_Q4':'PARK retained','no_additional_capture_authorized':True})
    except BaseException as error:
        write(out/'result.json',{'status':'INCOMPLETE','failed_stage':stage,'completed_captures':len(completed),
            'error_type':type(error).__name__,'error':str(error),'attempt_consumed':True,
            'qualification':False,'source_adoption':False,'prior_H2_Q4':'PARK retained'})
        raise


if __name__=='__main__':main()
