#!/usr/bin/env python3
"""Prepared H8 profiler-off screen. No execution without complete Q4 admission."""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import time

EXP = Path('experiments/ARM-LOOKUP-CONT-001')
Q4_PIN = '531bbabc2b50e26737a0be44773e7d195fa2576ba149e75bdf63a1a5698da743'
PHASES = ('H8-profiler-off-native-17','H8-profiler-off-lto-17')
PROTOCOL = EXP / 'H8-profiler-off/PROTOCOL.md'

def load_q4(path):
    if hashlib.sha256(Path(path).read_bytes()).hexdigest() != Q4_PIN:
        raise ValueError('Reviewed Q4 dependency changed')
    spec = importlib.util.spec_from_file_location('reviewed_q4',path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

q4 = load_q4(Path(__file__).with_name('fleet_profiler_off_qualification.py'))
require, read, write, append, sha = q4.require, q4.read, q4.write, q4.append, q4.sha

def lines(path):
    def unique(pairs):
        out={}
        for k,v in pairs:
            require(k not in out,'Duplicate JSON key')
            out[k]=v
        return out
    return [json.loads(line,object_pairs_hook=unique,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
        for line in Path(path).read_text().splitlines()]


def cohort_for(phase):
    require(phase in PHASES,'Unknown H8 screen phase')
    return 'native' if phase==PHASES[0] else 'gcc15-lto'


def compare_rows(phase, variants, rows, control_memory):
    """Pure full-grid comparison: no filtering, pooling, or candidate selection input."""
    cohort=cohort_for(phase);scale=1 if cohort=='native' else 5
    require(type(variants) is list and variants==[v for v in 'ABC' if v in variants] and variants,
            'Variant order/duplicates invalid')
    require(len(rows)==72*len(variants),'Missing/extra comparison row')
    fields=q4.ROW_FIELDS|{'variant','candidate_source_sha256'}
    report={'phase':phase,'cohort':cohort,'seed':17,'rows':len(rows),'variants':{},'source_adoption':False}
    offset=0
    for variant in variants:
        pin=BUILDS[cohort]['variants'][variant]
        blocks=[]
        for case,count in q4.CASES.items():
            case_rows=rows[offset:offset+12]
            for block in range(3):
                rr=case_rows[block*4:block*4+4]
                for slot,row in enumerate(rr):
                    label='ABBA'[slot]
                    require(set(row)==fields,'Unexpected row schema')
                    require(row['phase']==phase and row['cohort']==cohort and row['variant']==variant and
                            type(row['block']) is int and row['block']==block and
                            type(row['slot']) is int and row['slot']==slot and row['label']==label,
                            'Wrong/duplicate/reordered coordinate')
                    require(type(row['sweeps']) is int and row['sweeps']==count*scale and
                            row['candidate_source_sha256']==pin['source_sha256'] and
                            row['referee_sha256']==q4.REFEREE_PINS['lookup.c'],'Wrong count/source/referee')
                    expected_binary=q4.BASELINES[cohort][1] if label=='A' else pin['binary_sha256']
                    expected_source=q4.BASE_SOURCE if label=='A' else pin['source_sha256']
                    require(row['binary_sha256']==expected_binary and row['source_sha256']==expected_source,
                            'Wrong executed source/ELF')
                    q4.check_raw({k:row[k] for k in q4.RAW_FIELDS},case,17,count*scale)
                base=[r for r in rr if r['label']=='A'];candidate=[r for r in rr if r['label']=='B']
                a=sum(r['elapsed_ns'] for r in base);b=sum(r['elapsed_ns'] for r in candidate)
                limit=98 if case=='hit' else 101
                memory_by_label={label:{r['owned_bytes'] for r in case_rows if r['label']==label} for label in 'AB'}
                require(memory_by_label['A']=={control_memory[case]},'Baseline memory differs from Q4 control')
                stable_memory=all(len(values)==1 for values in memory_by_label.values())
                memory_pass=stable_memory and all(r['owned_bytes']*100<=control_memory[case]*101 for r in candidate)
                minimum=min(r['elapsed_ns'] for r in rr)
                blocks.append({'case':case,'block':block,'delta_pct':100*(b/a-1),
                    'memory_delta_pct':100*(sum(r['owned_bytes'] for r in candidate)/(2*control_memory[case])-1),
                    'minimum_ns':minimum,'memory_reproducible':stable_memory,
                    'pass':b*100<=a*limit and memory_pass and minimum>=250000000})
            offset+=12
        report['variants'][variant]={'eligible':all(b['pass'] for b in blocks),
            'source_sha256':pin['source_sha256'],'binary_sha256':pin['binary_sha256'],'blocks':blocks}
    return report


def target_variants(native_report, native_rows, control_memory):
    recomputed=compare_rows(PHASES[0],list('ABC'),native_rows,control_memory)
    require(native_report==recomputed,'Native decision is not exact full-grid recomputation')
    return [v for v in 'ABC' if recomputed['variants'][v]['eligible']]


def claim(root):
    require(not any((Path(root)/p).exists() for p in PHASES),'A fixed H8 phase already exists')
    out=Path(root)/'H8-profiler-off-screen'
    out.mkdir()
    return out


def verify_result(raw,case):
    require(set(raw)=={'verified','case','seed','members','owned_bytes'} and raw['verified'] is True and
            raw['case']==case and type(raw['seed']) is int and raw['seed']==17 and
            type(raw['members']) is int and raw['members']==500 and
            type(raw['owned_bytes']) is int and raw['owned_bytes']>0,'Verification model failed')


def check_processes(root,out,specs,record):
    """Exact process/raw/affinity/pre-post joins; used for Q4 and native admission."""
    commands=lines(out/'commands.jsonl');launches=lines(out/'launches.jsonl');starts=lines(out/'child-starts.jsonl')
    require(len(commands)==len(launches)==len(starts)==len(specs),'Incomplete/extra process evidence')
    for command,launch,start,spec in zip(commands,launches,starts,specs):
        stem=spec['stem']
        require(command['stem']==launch['stem']==start['stem']==stem and
                command['argv']==launch['argv']==spec['argv'] and command['returncode']==0 and
                'child_error' not in command and command['preflight_passed'] is True and
                command['binary_sha256']==launch['binary_sha256']==spec['binary_sha256'],
                'Wrong/reordered/failed process command')
        require(launch=={k:command[k] for k in ('argv','stem','started','binary_sha256','preflight_passed')},
                'Launch/completion evidence mismatch')
        guarantee={'scope':'preexec','cpu':2,'verified':True}
        require(command['child_affinity_guarantee']==start['guarantee']==guarantee and
                command['child_affinity_observation']==start['observation'] and
                type(command['pid']) is int and command['pid']==start['pid'] and command['pid']>0,
                'Child launch affinity identity mismatch')
        obs=start['observation']
        require(obs=={'available':True,'affinity':[2]} or
                obs=={'available':False,'affinity':None,'reason':'sched_getaffinity reported no such process'},
                'Invalid child affinity observation')
        require(all(type(command[k]) in (int,float) and math.isfinite(command[k]) for k in ('started','finished')) and
                command['finished']>=command['started'],'Invalid child timestamps')
        require(set(command['rusage'])=={'ru_utime','ru_stime','ru_minflt','ru_majflt','ru_nvcsw','ru_nivcsw'} and
                all(type(v) in (int,float) and math.isfinite(v) and v>=0 for v in command['rusage'].values()),
                'Invalid whole-child diagnostic')
        raw=read(out/(stem+'.stdout'))
        require(raw==spec['raw'] and not (out/(stem+'.stderr')).read_bytes(),'Raw/process join failed')
        for boundary in ('pre','post'):
            state=read(out/'isolation'/(stem+'-'+boundary+'-snapshot.json'))
            require(state['passed'] is True and state['controller_affinity']==[0] and
                    state['cpu2_online']=='1' and state['cpu2_siblings']=='2' and
                    state['parca_processes']==[] and
                    state['coordinator']=={'pid':record['coordinator']['pid'],'state':'T',
                                          'start_ticks':str(record['coordinator']['start_ticks'])},
                    'Pre/post process isolation join failed')
            require(state['checked']<=command['started'] if boundary=='pre' else
                    state['checked']>=command['finished'],'Isolation boundary time mismatch')


def tree_pins(root,directories):
    return {str(p.relative_to(root)):sha(p) for d in directories for p in sorted((root/d).rglob('*')) if p.is_file()}


def audit_q4(root,record,binding):
    """All four Q4 cohorts must actually pass, not merely contain a PASS label."""
    overall=root/'Q4-profiler-off'
    admission=read(overall/'admission.json');result=read(overall/'result.json')
    expected={'phases':list(q4.PHASES),'collector_sha256':Q4_PIN,
              'isolation_sha256':binding['isolation_sha256'],'review_sha256':binding['q4_review_sha256'],
              'baseline_only':True,'source_adoption':False}
    require(admission==expected and result=={'status':'PASS','completed_phases':list(q4.PHASES),
                'source_adoption':False,'candidate_executed':False},'Entire Q4 sequence has not passed')
    controls={}
    for phase in q4.PHASES:
        out=root/phase;cohort,seed,scale=q4.phase_spec(phase)
        rows=lines(out/'aa.jsonl');analysis=q4.analyse_rows(phase,rows)
        require(analysis['all_pass'] and read(out/'analysis.json')==analysis,'Q4 raw control does not qualify')
        require(read(out/'result.json')=={'status':'PASS','complete':True,'rows':72,
                'source_adoption':False,'candidate_executed':False},'Q4 partial/failed cohort')
        metadata=read(out/'metadata.json')
        require(all(metadata[k]==v for k,v in expected.items()) and
                metadata['phase']==phase and metadata['cohort']==cohort and metadata['seed']==seed and
                metadata['sweeps']=={k:v*scale for k,v in q4.CASES.items()} and
                metadata['upstream']==q4.UPSTREAM and metadata['source_sha256']==q4.BASE_SOURCE and
                metadata['baseline_sha256']==q4.BASELINES[cohort][1] and metadata['referee_pins']==q4.REFEREE_PINS,
                'Q4 metadata/source/condition mismatch')
        binary,binary_hash=q4.BASELINES[cohort];specs=[]
        for case in q4.CASES:
            stem='verify-'+case;raw=read(out/(stem+'.stdout'))
            require(set(raw)=={'verified','case','seed','members','owned_bytes'} and
                    raw['verified'] is True and raw['case']==case and type(raw['seed']) is int and
                    raw['seed']==seed and raw['members']==500 and type(raw['owned_bytes']) is int and
                    raw['owned_bytes']>0,'Q4 verification mismatch')
            specs.append({'stem':stem,'argv':['taskset','-c','2',str(root/binary),'verify',case,str(seed),'1'],
                          'binary_sha256':binary_hash,'raw':raw})
        for row in rows:
            specs.append({'stem':f'aa-{row["case"]}-{row["block"]}-{row["slot"]}',
                'argv':['taskset','-c','2',str(root/binary),'measure',row['case'],str(seed),str(row['sweeps'])],
                'binary_sha256':binary_hash,'raw':{k:row[k] for k in q4.RAW_FIELDS}})
        check_processes(root,out,specs,record)
        if seed==17:
            controls[cohort]={case:next(r['owned_bytes'] for r in rows if r['case']==case) for case in q4.CASES}
    return controls,tree_pins(root,['Q4-profiler-off',*q4.PHASES])


def audit_native(root,record,binding,controls):
    out=root/PHASES[0];metadata=read(out/'metadata.json');rows=lines(out/'comparison.jsonl')
    require(metadata['binding']==binding and metadata['variants']==list('ABC') and
            metadata['phase']==PHASES[0] and metadata['cohort']=='native' and metadata['seed']==17 and
            metadata['sweeps']==q4.CASES and metadata['build_pins']==BUILDS['native'] and
            metadata['baseline_sha256']==q4.BASELINES['native'][1] and
            metadata['control_phase']=='Q4-native-17' and metadata['q4_evidence_sha256']==
            sha(root/'H8-profiler-off-screen/q4-evidence-pins.json'),
            'Native metadata/condition/source binding failed')
    report=compare_rows(PHASES[0],list('ABC'),rows,controls['native'])
    require(read(out/'analysis.json')==report and read(out/'result.json')==
            {'status':'COMPLETE','rows':216,'source_adoption':False},'Native cohort incomplete/decision mismatch')
    specs=[]
    for variant in 'ABC':
        binary='bin/H8-native-'+variant;pin=BUILDS['native']['variants'][variant]
        for case in q4.CASES:
            stem=f'verify-{variant}-{case}';raw=read(out/(stem+'.stdout'));verify_result(raw,case)
            specs.append({'stem':stem,'argv':['taskset','-c','2',str(root/binary),'verify',case,'17','1'],
                          'binary_sha256':pin['binary_sha256'],'raw':raw})
        for row in [r for r in rows if r['variant']==variant]:
            executed=q4.BASELINES['native'][0] if row['label']=='A' else binary
            specs.append({'stem':f'compare-{variant}-{row["case"]}-{row["block"]}-{row["slot"]}',
                'argv':['taskset','-c','2',str(root/executed),'measure',row['case'],'17',str(row['sweeps'])],
                'binary_sha256':row['binary_sha256'],'raw':{k:row[k] for k in q4.RAW_FIELDS}})
    check_processes(root,out,specs,record)
    return target_variants(report,rows,controls['native']),tree_pins(root,[PHASES[0]])
BUILDS = {'gcc15-lto': {'metadata_sha256': '266d1d27394763f1ff4656af4c32275dbbb3dd16434a4ab6b64ae48f40710758',
               'origin': 'H8-lto',
               'variants': {'A': {'binary_sha256': '9305171dfab56897a01e2a202ed786700c4ba81793d292c4a5c02b82a5c22316',
                                  'source_sha256': 'e63caad0a6f81066a67ff964333cf0391c4a2ba71b592ce335bedefbd289f7f0'},
                            'B': {'binary_sha256': 'b9789ab86976ff0f29667d8449a92dd08948e9858b38abb62a27b3ad11bcbd35',
                                  'source_sha256': '24151adc87c1c7c7262adfc360b2b2e7ae662320050c60f1014889bf7c8f5040'},
                            'C': {'binary_sha256': 'ac80bc78a94591d8ba12209db82d6a8f788e9b38f321389670e3ed320e596068',
                                  'source_sha256': '37f5c33a57120e33a5a0203dc05bfb41f9e528cd5dabef934c66335526b2de0e'}}},
 'native': {'metadata_sha256': '8b466cfef99008ef73725f1fe9a297a12a08a1a88b83556545604558f83ccd69',
            'origin': 'H8-native',
            'variants': {'A': {'binary_sha256': 'b4656e11b498f7cce4933c8bd38940c8883fc67a828c87a34b8cbe4caaea1519',
                               'source_sha256': 'e63caad0a6f81066a67ff964333cf0391c4a2ba71b592ce335bedefbd289f7f0'},
                         'B': {'binary_sha256': 'd5bdbfe282f01bc29ff1520cf75365ac780cf13416e55d764299f7e53d4c6bd6',
                               'source_sha256': '24151adc87c1c7c7262adfc360b2b2e7ae662320050c60f1014889bf7c8f5040'},
                         'C': {'binary_sha256': '47071bd029d907da775dd55c2abaaf41e21f8a21e894f6a596d0904079343174',
                               'source_sha256': '37f5c33a57120e33a5a0203dc05bfb41f9e528cd5dabef934c66335526b2de0e'}}}}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('root','collector-sha256','protocol-sha256','isolation-record','isolation-sha256',
                 'q4-review','q4-review-sha256','screen-review','screen-review-sha256'):
        p.add_argument('--'+name,required=True)
    args=p.parse_args();root=Path(args.root).resolve()
    overall=claim(root);current=None
    binding={'q4_collector_sha256':Q4_PIN,'screen_collector_sha256':args.collector_sha256,
             'protocol_sha256':args.protocol_sha256,'isolation_sha256':args.isolation_sha256,
             'q4_review_sha256':args.q4_review_sha256,'screen_review_sha256':args.screen_review_sha256}
    write(overall/'admission.json',dict(binding,phases=list(PHASES),source_adoption=False))
    try:
        isolation_path=Path(args.isolation_record).resolve();q4_review_path=Path(args.q4_review).resolve()
        screen_review_path=Path(args.screen_review).resolve()
        record=read(isolation_path);q4_review=read(q4_review_path);review=read(screen_review_path)
        q4.validate_record(record,q4_review,root,args.isolation_sha256,Q4_PIN)
        require(review['schema_version']==1 and review['decision']=='APPROVED' and
                type(review['reviewer_role']) is str and review['reviewer_role'].strip() and
                all(review[k]==v for k,v in binding.items() if k!='screen_review_sha256') and
                review['static_admitted_variants']==list('ABC') and review['build_pins']==BUILDS,
                'Screen review/static admission not exact')
        evidence_pins={}
        def identities():
            q4.identities(root,Q4_PIN,isolation_path,args.isolation_sha256,
                          q4_review_path,args.q4_review_sha256,record)
            require(sha(__file__)==args.collector_sha256 and sha(root/PROTOCOL)==args.protocol_sha256 and
                    sha(screen_review_path)==args.screen_review_sha256,'Screen collector/protocol/review changed')
            for cohort,build in BUILDS.items():
                require(sha(root/build['origin']/'metadata.json')==build['metadata_sha256'],
                        'Previously built H8 metadata changed')
                for variant,pin in build['variants'].items():
                    require(sha(root/'variants'/build['origin']/variant/'zset_btree.c')==pin['source_sha256'] and
                            sha(root/'bin'/(build['origin']+'-'+variant))==pin['binary_sha256'],
                            'H8 source/ELF differs from frozen build')
            for relative,expected in evidence_pins.items():
                require(sha(root/relative)==expected,'Consumed control/native evidence changed: '+relative)
        identities()
        controls,q4_pins=audit_q4(root,record,binding)
        evidence_pins.update(q4_pins)
        write(overall/'q4-evidence-pins.json',q4_pins)
        write(overall/'control-memory.json',controls)
        eligible=list('ABC')
        for phase in PHASES:
            if phase==PHASES[1]:
                eligible,native_pins=audit_native(root,record,binding,controls)
                evidence_pins.update(native_pins)
                admission={'native_evidence_pins':native_pins,'variants':eligible,
                           'native_build_pins':BUILDS['native'],'target_build_pins':BUILDS['gcc15-lto'],
                           'binding':binding,'source_adoption':False}
                write(overall/'target-admission.json',admission)
                if not eligible:
                    write(overall/'result.json',{'status':'NONE','reason':'no complete native gate passer',
                          'target_executed':False,'source_adoption':False})
                    return
            identities()
            out=root/phase;out.mkdir();current=out
            cohort=cohort_for(phase);scale=1 if cohort=='native' else 5;build=BUILDS[cohort]
            metadata={'phase':phase,'cohort':cohort,'seed':17,'variants':eligible,
                'sweeps':{k:v*scale for k,v in q4.CASES.items()},'binding':binding,'build_pins':build,
                'baseline_sha256':q4.BASELINES[cohort][1],
                'control_phase':'Q4-native-17' if cohort=='native' else 'Q4-lto-17',
                'q4_evidence_sha256':sha(overall/'q4-evidence-pins.json'),'started':time.time()}
            write(out/'metadata.json',metadata)
            def run(binary,binary_hash,mode,case,count,stem):
                identities();q4.isolation(root,record,out,stem+'-pre')
                command={'argv':['taskset','-c','2',str(root/binary),mode,case,'17',str(count)],
                         'stem':stem,'started':time.time(),'binary_sha256':binary_hash,'preflight_passed':True}
                append(out/'launches.jsonl',command)
                proc=None;before=resource.getrusage(resource.RUSAGE_CHILDREN)
                try:
                    with (out/(stem+'.stdout')).open('wb') as stdout,(out/(stem+'.stderr')).open('wb') as stderr:
                        proc=subprocess.Popen(command['argv'],stdout=stdout,stderr=stderr,preexec_fn=q4.pin_child_cpu)
                        command['pid']=proc.pid
                        command['child_affinity_guarantee']={'scope':'preexec','cpu':2,'verified':True}
                        command['child_affinity_observation']=q4.observe_child_affinity(proc.pid)
                        append(out/'child-starts.jsonl',{'stem':stem,'pid':proc.pid,
                            'guarantee':command['child_affinity_guarantee'],'observation':command['child_affinity_observation']})
                        proc.wait(timeout=240)
                except BaseException as error:
                    command['child_error']=type(error).__name__+': '+str(error)
                    if proc is not None and proc.poll() is None:proc.kill();proc.wait()
                after=resource.getrusage(resource.RUSAGE_CHILDREN)
                command['rusage']={name:getattr(after,name)-getattr(before,name) for name in
                    ('ru_utime','ru_stime','ru_minflt','ru_majflt','ru_nvcsw','ru_nivcsw')}
                command['rusage_scope']='Whole taskset/baseline-or-candidate child; includes setup/warmup; outside frozen inner loop'
                command.update(returncode=None if proc is None else proc.returncode,finished=time.time())
                append(out/'commands.jsonl',command)
                identities();q4.isolation(root,record,out,stem+'-post')
                q4.check_child_completion(command,(out/(stem+'.stderr')).read_bytes())
                return read(out/(stem+'.stdout'))
            rows=[]
            for variant in eligible:
                candidate='bin/'+build['origin']+'-'+variant;pin=build['variants'][variant]
                for case in q4.CASES:
                    verify_result(run(candidate,pin['binary_sha256'],'verify',case,1,f'verify-{variant}-{case}'),case)
                for case,count in q4.CASES.items():
                    for block in range(3):
                        for slot,label in enumerate('ABBA'):
                            binary,binary_hash=q4.BASELINES[cohort] if label=='A' else (candidate,pin['binary_sha256'])
                            stem=f'compare-{variant}-{case}-{block}-{slot}'
                            raw=run(binary,binary_hash,'measure',case,count*scale,stem)
                            q4.check_raw(raw,case,17,count*scale)
                            row=dict(raw,phase=phase,cohort=cohort,variant=variant,block=block,slot=slot,label=label,
                                sweeps=count*scale,candidate_source_sha256=pin['source_sha256'],
                                source_sha256=q4.BASE_SOURCE if label=='A' else pin['source_sha256'],
                                referee_sha256=q4.REFEREE_PINS['lookup.c'],binary_sha256=binary_hash)
                            append(out/'comparison.jsonl',row);rows.append(row);print(phase,stem,flush=True)
            report=compare_rows(phase,eligible,rows,controls[cohort])
            write(out/'analysis.json',report)
            write(out/'result.json',{'status':'COMPLETE','rows':72*len(eligible),'source_adoption':False})
        write(overall/'result.json',{'status':'SCREEN_COMPLETE','source_adoption':False,
            'target_eligible':[v for v in eligible if report['variants'][v]['eligible']],
            'remaining_gates':['Intel portability','supplemental and affected guards','held-out confirmation',
                               'matched profiles','independent final review']})
    except BaseException as error:
        failure={'status':'ERROR','attempt_consumed':True,'error_type':type(error).__name__,
                 'error':str(error),'source_adoption':False}
        write(overall/'result.json',failure)
        if current is not None:write(current/'result.json',failure)
        raise


if __name__=='__main__':main()
