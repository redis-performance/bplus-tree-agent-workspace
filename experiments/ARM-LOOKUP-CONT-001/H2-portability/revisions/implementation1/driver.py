#!/usr/bin/env python3
"""Fleet-only cross-ABI correctness driver. Offline validators perform no execution."""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import re
import subprocess
import time

EXP=Path('experiments/ARM-LOOKUP-CONT-001')
HARNESS=EXP/'H2-portability'
OWNER='bplus ARM-LOOKUP-CONT-001'
BASE_IMAGE='sha256:9ca91b05c7b07d2979f16413e8b2cd6ec8a7c80ffca4121ccab0aeba33f90460'
CLEANUP_CAPS={'Type':'exec','TimeoutStartUSec':'3min','RuntimeMaxUSec':'3min',
              'TimeoutStopUSec':'15s','KillMode':'control-group','SendSIGKILL':'yes'}
TIMER_CAPS={'AccuracyUSec':'1us','RandomizedDelayUSec':'0'}
Q4_PIN='531bbabc2b50e26737a0be44773e7d195fa2576ba149e75bdf63a1a5698da743'
BASE='16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9'
B='63b18cd5aa70d455fb2639e826386045841052b8f2cea85e5b97f9018d829f29'
CASES=('hit','score','miss','long','external','update')
SEEDS=(17,29,43)
TARGETS={'i686':{'prefix':'i686-linux-gnu','qemu':'qemu-i386','pointer':4,'endian':'little','class':1,'data':1,'machine':3},
         's390x':{'prefix':'s390x-linux-gnu','qemu':'qemu-s390x','pointer':8,'endian':'big','class':2,'data':2,'machine':22}}
q4_path=Path(__file__).parent.parent/'fleet_profiler_off_qualification.py'
if hashlib.sha256(q4_path.read_bytes()).hexdigest()!=Q4_PIN:raise ValueError('Q4 dependency changed')
spec=importlib.util.spec_from_file_location('portability_q4',q4_path)
q4=importlib.util.module_from_spec(spec);spec.loader.exec_module(q4)
require,read,write,append,sha=q4.require,q4.read,q4.write,q4.append,q4.sha
parca_process_match=q4.parca_process_match


def check_elf(data,target):
    expected=TARGETS[target]
    require(len(data)>=64 and data[:4]==b'\x7fELF','Missing ELF header')
    require(data[4]==expected['class'] and data[5]==expected['data'] and data[6]==1,'Wrong ELF class/endian')
    machine=int.from_bytes(data[18:20],expected['endian'])
    require(machine==expected['machine'],'Wrong ELF machine')
    byteorder=expected['endian']
    word=lambda offset,size:int.from_bytes(data[offset:offset+size],byteorder)
    phoff=word(28,4) if expected['class']==1 else word(32,8)
    entsize=word(42,2) if expected['class']==1 else word(54,2)
    count=word(44,2) if expected['class']==1 else word(56,2)
    require(0<count<256 and entsize>=(32 if expected['class']==1 else 56) and
            phoff+count*entsize<=len(data),'Invalid program header table')
    interpreters=[]
    for i in range(count):
        offset=phoff+i*entsize
        if word(offset,4)==3:
            start=word(offset+4,4) if expected['class']==1 else word(offset+8,8)
            length=word(offset+16,4) if expected['class']==1 else word(offset+32,8)
            require(1<length<256 and start+length<=len(data),'Invalid interpreter segment')
            raw=data[start:start+length];require(raw[-1:]==b'\0' and b'\0' not in raw[:-1],'Bad interpreter text')
            interpreter=raw[:-1].decode('ascii')
            require(interpreter.startswith('/') and '..' not in interpreter.split('/'),'Unsafe ELF interpreter')
            interpreters.append(interpreter)
    require(len(interpreters)==1,'Exactly one dynamic guest interpreter required')
    return {'class':data[4],'data':data[5],'machine':machine,'interpreter':interpreters[0]}


def check_clock_symbols(text):
    require(re.search(r'^[0-9a-fA-F]+ [Tt] __wrap_clock_gettime$',text,re.M) is not None,'Missing defined clock guard')
    require(re.search(r'\bU (?:__)?clock_gettime(?:64)?(?:@|$)',text,re.M) is None,'Unwrapped lookup clock symbol')


def check_clock_disassembly(text):
    require(re.search(r'\b(?:callq?|brasl)\b[^\n]*<__wrap_clock_gettime(?:[+>])',text) is not None,
            'No emitted call to lookup clock guard')


def check_abi(row,target,variant):
    expected=TARGETS[target]
    require(all(type(v) is int for k,v in row.items() if k not in ('variant','endian')),
            'ABI fields must be exact integers')
    require(row['compiler_little']==1234 and row['compiler_big']==4321,'Unexpected compiler endian constants')
    require(row['variant']==variant and row['endian']==expected['endian'],'Wrong ABI identity')
    require(all(type(row[k]) is int and row[k]==expected['pointer'] for k in ('pointer','size_t','ulong')),'Wrong pointer/integer ABI')
    require(all(type(row[k]) is int and row[k]==v for k,v in {'u64':8,'double':8,'char_bit':8,'radix':2,'mantissa':53,'max_exp':1024,'moved_size':1,'resize_size':2}.items()),'Unsupported numeric/field representation')
    require(row['compiler_endian']==row['compiler_'+expected['endian']],'Compiler/runtime byte order disagreement')
    require(row['node']>0 and row['leaf_data']>row['node'] and row['leaf_data']%2==0 and
            row['align_u64'] in (4,8) and row['align_leaf']>=row['align_u64'],'Unsupported header alignment')
    if target=='s390x':require(row['node']==24 and row['leaf_data']==56,'64-bit footprint changed')
    if variant=='B':require(row['cache_size']==2 and 0<=row['flags_offset']<row['node'] and 0<=row['cache_offset']<row['node'],'Cache/flags ABI mismatch')
    else:require(row['cache_size']==0 and row['cache_offset']==-1 and row['flags_offset']==-1,'Fake baseline cache')
    return row


def check_unit(text):
    text=re.sub(r'\x1b\[[0-9;]*m','',text)
    rows=re.findall(r'^(\d+) - .+: (PASSED|FAILED)$',text,re.M)
    require(rows==[(str(i),'PASSED') for i in range(1,58)],'Original57 unit results missing/duplicate/failed')
    require(len(re.findall(r'^  Tests: +57 passed, 0 failed, 57 total$',text,re.M))==1,'Missing/duplicate unit summary')
    require('FAILED' not in text and 'WARNING' not in text,'Unit failure text')


def check_verify(row,case,seed):
    require(set(row)=={'verified','case','seed','members','owned_bytes'} and row['verified'] is True and
            row['case']==case and type(row['seed']) is int and row['seed']==seed and
            type(row['members']) is int and row['members']==500 and
            type(row['owned_bytes']) is int and row['owned_bytes']>0,'Verify model mismatch/timing row')


def check_oracle(row,kind):
    if kind in ('output_oracle','output_external_oracle'):
        require(set(row)=={'passed','output_checks'} and row['passed'] is True and type(row['output_checks']) is int and
                row['output_checks']==(90000 if kind=='output_oracle' else 45000),'Output oracle mismatch')
    else:
        fields={'passed','zero_full_reversed','flag_shift_cases','validations','leaves_checked','relocated_pages'}
        if kind=='paired':fields.add('refresh_sites')
        require(set(row)==fields and row['passed'] is True and row['zero_full_reversed'] is True and
                type(row['flag_shift_cases']) is int and row['flag_shift_cases']==256 and
                type(row['validations']) is int and row['validations']==7693 and
                type(row['leaves_checked']) is int and row['leaves_checked']>0 and
                type(row['relocated_pages']) is int and row['relocated_pages']>0,'Metadata oracle mismatch')
        if kind=='paired':require(type(row['refresh_sites']) is int and row['refresh_sites']==4,'Missing refresh-site proof')


def execution_plan(target,variant):
    require(target in TARGETS and variant in ('base','B'),'Unknown matrix cell')
    plan=[('abi',()),('unit',())]
    plan += [('lookup',('verify',case,str(seed),'1')) for seed in SEEDS for case in CASES]
    plan += [(kind,()) for kind in ('output_oracle','output_external_oracle','paired')]
    if variant=='B':plan.append(('original_metadata',()))
    return plan


def claim(root,mode):
    require(mode in ('image-receipt','correctness'),'Unknown phase')
    out=Path(root)/('H2-portability-'+mode+'-001');out.mkdir();return out


def validate_record(record,review,root,record_pin,manifest_pin,mode,image):
    q4.validate_record(record,dict(schema_version=1,decision=review['decision'],reviewer_role=review['reviewer_role'],
        isolation_sha256=review['isolation_sha256'],collector_sha256=review['manifest_sha256']),root,record_pin,manifest_pin)
    require(review['schema_version']==1 and review['phase']==mode and review['image_id']==image and
            review['manifest_sha256']==manifest_pin,'Wrong phase/image/manifest review')
    names={'image':Path(root).name+'-portability-image','check':Path(root).name+'-portability-check'}
    require(record['containers']==names and record['cleanup_contract']==dict(containers=names,
        reap_containers_before_resume=True,restore_sibling50=True,ownership_required=True),'Cleanup/container ownership contract mismatch')
    require(record['base_image_id']==BASE_IMAGE,'Wrong immutable build base')
    started,deadline=record['task_started_epoch'],record['task_deadline_epoch']
    require(all(type(v) in (int,float) and math.isfinite(v) for v in (started,deadline)) and
            0<started<deadline<=record['deadline']-300 and deadline-started<=1800,
            'Single task budget must be positive and at most30min including image preparation')
    require(record['cleanup_service_properties']==CLEANUP_CAPS and record['timer_properties']==TIMER_CAPS,
            'Cleanup service/timer caps differ')
    retired=record['retired_timers']
    require(type(retired) is list and len(retired)==2 and len(set(retired))==2 and
            not set(retired)&set(record['cleanup_timers']) and all(type(t) is str and t.endswith('.timer') and '/' not in t for t in retired),
            'Two distinct retired timers required')
    require(re.fullmatch('[0-9a-f]{32}',record['lease_generation']) is not None,'Missing lease generation')
    require(record['container_labels']=={
        'org.redis-performance.cleanup.owner':OWNER,
        'org.redis-performance.cleanup.root':str(Path(root).resolve()),
        'org.redis-performance.cleanup.generation':record['lease_generation']},'Cleanup label contract mismatch')


def isolation(root, record, out, stem):
    """Fleet-only operational audit. Every command/raw result is retained."""
    audit = out / 'isolation'
    audit.mkdir(exist_ok=True)
    def command(argv, name):
        started = time.time()
        try:
            p = subprocess.run(argv, capture_output=True, timeout=30)
            stdout, stderr, code = p.stdout, p.stderr, p.returncode
        except subprocess.TimeoutExpired as error:
            stdout, stderr, code = error.stdout or b'', error.stderr or b'', None
        (audit / (stem + '-' + name + '.stdout')).write_bytes(stdout)
        (audit / (stem + '-' + name + '.stderr')).write_bytes(stderr)
        append(out / 'isolation-commands.jsonl', {'argv':argv, 'stem':stem+'-'+name,
               'started':started, 'finished':time.time(), 'returncode':code})
        require(code == 0 and not stderr, 'Isolation command failed: ' + name)
        return stdout
    def show(unit, properties, name):
        data = command(['systemctl','show',unit] + ['--property='+p for p in properties], name)
        values = dict(line.split('=',1) for line in data.decode().splitlines())
        require(set(values) == set(properties), 'Incomplete systemd state')
        return values
    snapshot = {'checked':time.time(), 'controller_affinity':sorted(os.sched_getaffinity(0))}
    write(audit / (stem + '-snapshot.json'), snapshot)
    lease_path = root / 'reservation.json'
    require(sha(lease_path) == record['lease_sha256'], 'Owned lease changed')
    lease = read(lease_path)
    require(lease['owner'] == OWNER and lease['state'] == 'RESERVED' and
            lease['deadline'] == record['deadline'] and time.time() < lease['deadline']-300,
            'Owned lease/cleanup margin unavailable')
    require(lease['run_root']==record['run_root'] and lease['lease_generation']==record['lease_generation'],
            'Lease generation/root differs')
    pid, ticks = record['coordinator']['pid'], str(record['coordinator']['start_ticks'])
    require(lease['coordinator_pid'] == pid and str(lease['coordinator_ticks']) == ticks,
            'Lease coordinator differs from reviewed identity')
    stat = (Path('/proc') / str(pid) / 'stat').read_text()
    fields = stat.rsplit(') ',1)[1].split()
    snapshot['coordinator'] = {'pid':pid, 'state':fields[0], 'start_ticks':fields[19]}
    require(fields[0] == 'T' and fields[19] == ticks, 'Saved coordinator not identically paused')
    require(os.sched_getaffinity(0) == {0} and platform.machine() == 'x86_64',
            'Controller must be Intel CPU0')
    cpu = Path('/sys/devices/system/cpu/cpu2')
    snapshot['cpu2_online'] = (cpu/'online').read_text().strip()
    snapshot['cpu2_siblings'] = (cpu/'topology/thread_siblings_list').read_text().strip()
    require(snapshot['cpu2_online'] == '1' and snapshot['cpu2_siblings'] == '2,50' and
            Path('/sys/devices/system/cpu/cpu50/online').read_text().strip() == '0',
            'CPU2 offline or unexpected sibling')
    expected_services = {s['unit']:s['exec_start_sha256'] for s in record['cleanup_services']}
    schedules = {s['unit']:s for s in record['cleanup_timer_schedules']}
    used_services = set()
    for i, timer in enumerate(record['cleanup_timers']):
        state = show(timer, ['ActiveState','Unit','NextElapseUSecRealtime','NextElapseUSecMonotonic',*TIMER_CAPS], 'timer'+str(i))
        require(all(state[k]==v for k,v in TIMER_CAPS.items()),'Cleanup timer precision/randomization changed')
        schedule = schedules[timer]
        require(state['ActiveState'] == 'active' and state['Unit'] in expected_services,
                'Cleanup timer inactive/unreviewed target')
        require(all(state[p] == schedule[p] for p in ('NextElapseUSecRealtime','NextElapseUSecMonotonic')) and
                time.time() < schedule['fire_epoch']-300, 'Cleanup timer schedule changed/too close')
        used_services.add(state['Unit'])
    require(used_services == set(expected_services), 'Reviewed cleanup service not armed by timer')
    for i,timer in enumerate(record['retired_timers']):
        require(show(timer,['ActiveState'],'retired'+str(i))=={'ActiveState':'inactive'},'Old cleanup timer still active')
    for i, (unit, expected) in enumerate(expected_services.items()):
        require(show(unit,list(CLEANUP_CAPS),'cleanup-caps'+str(i))==CLEANUP_CAPS,
                'Cleanup live service bounds changed')
        raw = command(['systemctl','show',unit,'--property=ExecStart','--value'], 'cleanup-exec'+str(i))
        require(hashlib.sha256(raw).hexdigest() == expected, 'Cleanup service ExecStart changed')
    state = show(record['service']['name'], ['ActiveState','SubState','MainPID','CPUAffinity','AllowedCPUs'], 'parca')
    require(state == {'ActiveState':'inactive','SubState':'dead','MainPID':'0',
                      'CPUAffinity':'','AllowedCPUs':''}, 'Parca active/process/policy state mismatch')
    matches = []
    for path in Path('/proc').iterdir():
        if not path.name.isdigit():
            continue
        try:
            comm = (path/'comm').read_bytes().lower()
            cmdline = (path/'cmdline').read_bytes().lower()
        except FileNotFoundError:
            continue  # Process exited; permission/read failures remain fatal.
        match = parca_process_match(int(path.name), comm, cmdline)
        if match is not None:
            matches.append(match)
    snapshot['parca_processes'] = matches
    write(audit / (stem + '-snapshot.json'), snapshot)
    require(not matches, 'Parca process remains')
    require(not command(['docker','ps','-q'], 'docker').strip(), 'Concurrent Docker work')
    snapshot['passed'] = True
    write(audit / (stem + '-snapshot.json'), snapshot)


class Runner:
    def __init__(self,root,out,record,identities,image,deadline):
        self.root,self.out,self.record,self.identities,self.image=root,out,record,identities,image
        self.index=0;self.deadline=deadline
    def raw(self,argv,stem,timeout=30):
        remaining=min(self.deadline-time.monotonic(),self.record['task_deadline_epoch']-time.time(),self.record['deadline']-time.time()-300,
                      min(s['fire_epoch'] for s in self.record['cleanup_timer_schedules'])-time.time()-300)
        require(remaining>0,'No remaining execution/cleanup budget')
        timeout=min(timeout,remaining)
        try:
            result=subprocess.run(argv,capture_output=True,timeout=timeout,env=dict(os.environ,LC_ALL='C',LANG='C'))
            code,stdout,stderr=result.returncode,result.stdout,result.stderr
        except subprocess.TimeoutExpired as e:
            code,stdout,stderr=None,e.stdout or b'',e.stderr or b''
        (self.out/(stem+'.stdout')).write_bytes(stdout);(self.out/(stem+'.stderr')).write_bytes(stderr)
        append(self.out/'commands.jsonl',dict(argv=argv,stem=stem,returncode=code,timeout_seconds=timeout))
        require(code==0,'Command failed/unsupported/timed out: '+stem)
        return stdout
    def container(self,arguments,stem,timeout=120):
        self.index+=1;stem=f'{self.index:03d}-'+stem
        self.identities();isolation(self.root,self.record,self.out,stem+'-pre')
        name=self.record['containers']['check']
        existing=self.raw(['docker','ps','-aq','--filter','name=^/'+name+'$'],stem+'-name')
        require(not existing.strip(),'Owned correctness container already exists')
        argv=['docker','run','--rm','--name',name]
        for key,value in sorted(self.record['container_labels'].items()):argv+=['--label',key+'='+value]
        argv+=['--cpuset-cpus','2','--network','none','--memory','4g','--pids-limit','256',
            '--cap-drop','ALL','--security-opt','no-new-privileges',
            '-e','LC_ALL=C','-e','LANG=C','-v',str(self.root)+':/work:ro',
            '-v',str(self.out)+':/out:rw','-w','/work',self.image]+arguments
        error=None;result=None
        try:result=self.raw(argv,stem,timeout)
        except BaseException as e:error=e
        # No name-based force removal here: independent reviewed cleanup owns it.
        # A failed docker client can leave a running named container; post-gate
        # records that failure and external cleanup must reap it before resume.
        self.identities();isolation(self.root,self.record,self.out,stem+'-post')
        if error:raise error
        return result,stem


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for arg in ('root','mode','image-id','manifest-sha256','isolation-record','isolation-sha256','review','review-sha256'):
        p.add_argument('--'+arg,required=True)
    p.add_argument('--image-receipt');p.add_argument('--image-receipt-sha256')
    args=p.parse_args();root=Path(args.root).resolve();out=claim(root,args.mode)
    completed=[];stage='admission';deadline=time.monotonic()+1800
    try:
        record_path=Path(args.isolation_record).resolve();review_path=Path(args.review).resolve()
        record,review=read(record_path),read(review_path)
        require(re.fullmatch('sha256:[0-9a-f]{64}',args.image_id),'Use full image content ID')
        validate_record(record,review,root,args.isolation_sha256,args.manifest_sha256,args.mode,args.image_id)
        deadline=time.monotonic()+record['task_deadline_epoch']-time.time()
        manifest_path=root/HARNESS/'files.json';manifest=read(manifest_path)
        def identities():
            require(time.monotonic()<deadline and record['task_started_epoch']<=time.time()<record['task_deadline_epoch'],
                    'Fixed shared task budget unavailable')
            require(sha(record_path)==args.isolation_sha256 and sha(review_path)==args.review_sha256 and
                    sha(manifest_path)==args.manifest_sha256,'Admission bytes changed')
            for relative,pin in manifest['files'].items():require(sha(root/relative)==pin,'Input changed: '+relative)
            require(sha(root/EXP/'current/src/zset_btree.c')==BASE and sha(root/'H2-B-source/zset_btree.c')==B,'Source pair changed')
            for artifact in record['cleanup_artifacts']:
                path=Path(artifact['path']);path=path if path.is_absolute() else root/path
                require(sha(path)==artifact['sha256'],'Cleanup artifact changed')
            if args.mode=='correctness':
                require(sha(args.image_receipt)==args.image_receipt_sha256==review['image_receipt_sha256'],'Image receipt changed')
        identities();runner=Runner(root,out,record,identities,args.image_id,deadline)
        isolation(root,record,out,'admission')
        inspected=json.loads(runner.raw(['docker','image','inspect',args.image_id],'image-inspect'))
        require(len(inspected)==1 and inspected[0]['Id']==args.image_id,'Wrong image')
        labels=inspected[0]['Config'].get('Labels') or {}
        require(labels.get('h2.portability.base')==BASE_IMAGE and
                labels.get('h2.portability.prepare')==manifest['files'][str(HARNESS/'prepare-image.sh')],
                'Image lacks exact reviewed preparation/base binding')
        write(out/'admission.json',dict(mode=args.mode,image=args.image_id,manifest=args.manifest_sha256,
            isolation=args.isolation_sha256,review=args.review_sha256,qualification=False,prior_H2='PARK'))
        if args.mode=='image-receipt':
            metadata={}
            commands={'packages':['dpkg-query','-W','-f=${binary:Package}\t${Version}\t${Architecture}\n'],
                'package-receipt':['cat','/opt/h2-portability-receipts/packages.tsv'],
                'export-receipts':['sh','/work/'+str(HARNESS/'export_receipts.sh')]}
            for target,spec in TARGETS.items():
                prefix=spec['prefix'];commands[target+'-compiler']=[prefix+'-gcc','--version']
                commands[target+'-target']=[prefix+'-gcc','-dumpmachine']
                commands[target+'-emulator']=[spec['qemu'],'--version']
                commands[target+'-cpu-models']=[spec['qemu'],'-cpu','help']
                commands[target+'-macros']=[prefix+'-gcc','-dM','-E','-x','c','/dev/null']
                commands[target+'-tools-sha']=['sha256sum','/usr/bin/'+prefix+'-gcc','/usr/bin/'+prefix+'-ld','/usr/bin/'+spec['qemu']]
                commands[target+'-libraries']=['find','/usr/'+prefix,'-type','f','-exec','sha256sum','{}','+']
            for stage,argv in commands.items():
                data,stem=runner.container(argv,'metadata-'+stage)
                metadata[stage]={'sha256':hashlib.sha256(data).hexdigest(),'file':stem+'.stdout'}
                if stage.endswith('-target'):require(data.decode().strip()==TARGETS[stage[:-7]]['prefix'],'Cross target mismatch')
                if stage.endswith('-cpu-models'):require(re.search(rb'\bmax\b',data) is not None,'Fixed QEMU max model unavailable')
            require(metadata['packages']['sha256']==metadata['package-receipt']['sha256'],'Installed package receipt mismatch')
            write(out/'receipt.json',dict(schema_version=1,status='IMAGE_PREPARED',image_id=args.image_id,
                base_image_id=BASE_IMAGE,manifest_sha256=args.manifest_sha256,metadata=metadata,cpu_policy='-cpu max',
                workload_executed=False,qualification=False))
        else:
            require(args.image_receipt and args.image_receipt_sha256,'Reviewed image receipt required')
            receipt=read(args.image_receipt)
            require(receipt['schema_version']==1 and receipt['status']=='IMAGE_PREPARED' and
                    receipt['image_id']==args.image_id and receipt['base_image_id']==BASE_IMAGE and
                    receipt['manifest_sha256']==args.manifest_sha256 and receipt['cpu_policy']=='-cpu max','Image preparation join mismatch')
            for target in TARGETS:
                baseline_memory={};baseline_abi=None
                for variant in ('base','B'):
                    stage=target+'-'+variant+'-build'
                    runner.container(['sh','/work/'+str(HARNESS/'compile.sh'),target,variant],stage,120)
                    directory=out/(target+'-'+variant);binary_pins={};elfs={}
                    for binary in directory.iterdir():
                        require(binary.is_file(),'Unexpected build output')
                        elfs[binary.name]=check_elf(binary.read_bytes(),target);binary_pins[binary.name]=sha(binary)
                    write(directory/'binary-pins.json',binary_pins);write(directory/'elf-headers.json',elfs)
                    interpreters={e['interpreter'] for e in elfs.values()}
                    require(len(interpreters)==1,'Guest binaries disagree on interpreter')
                    loader='/usr/'+TARGETS[target]['prefix']+next(iter(interpreters))
                    loader_stdout,_=runner.container(['readlink','-e',loader],stage+'-loader')
                    resolved=loader_stdout.decode().strip()
                    require(resolved.startswith('/usr/'+TARGETS[target]['prefix']+'/'),'Guest loader escapes pinned sysroot')
                    runner.container(['sha256sum',resolved],stage+'-loader-sha')
                    symbols,_=runner.container([TARGETS[target]['prefix']+'-nm','-a',
                        '/out/'+target+'-'+variant+'/lookup'],stage+'-clock-symbols')
                    check_clock_symbols(symbols.decode())
                    assembly,_=runner.container([TARGETS[target]['prefix']+'-objdump','-dr',
                        '/out/'+target+'-'+variant+'/lookup'],stage+'-clock-disassembly')
                    check_clock_disassembly(assembly.decode())
                    for kind,arguments in execution_plan(target,variant):
                        stage='-'.join((target,variant,kind,*arguments))
                        binary=directory/kind;require(sha(binary)==binary_pins[kind],'Built ELF changed')
                        argv=[TARGETS[target]['qemu'],'-cpu','max','-L','/usr/'+TARGETS[target]['prefix'],
                              '/out/'+target+'-'+variant+'/'+kind,*arguments]
                        stdout,stem=runner.container(argv,stage,300 if kind=='unit' else 120)
                        require(sha(binary)==binary_pins[kind],'ELF changed during execution')
                        require(not (out/(stem+'.stderr')).read_bytes(),'Guest/emulator diagnostic stderr')
                        if kind=='unit':check_unit(stdout.decode())
                        else:
                            row=read(out/(stem+'.stdout'))
                            if kind=='abi':
                                check_abi(row,target,variant)
                                if variant=='base':baseline_abi=row
                                else:require(all(row[k]==baseline_abi[k] for k in ('node','leaf_data','align_u64','align_leaf')),'ABI footprint differs')
                            elif kind=='lookup':
                                _,case,seed,_=arguments;check_verify(row,case,int(seed));key=(case,seed)
                                if variant=='base':baseline_memory[key]=row['owned_bytes']
                                else:require(row['owned_bytes']==baseline_memory[key],'Paired guest memory differs')
                            else:check_oracle(row,kind)
                        completed.append(stage);append(out/'completed.jsonl',dict(stage=stage,elf_sha256=binary_pins[kind],passed=True))
        write(out/'result.json',dict(status='IMAGE_PREPARED' if args.mode=='image-receipt' else 'CORRECTNESS_COMPLETE',
            completed=completed,qualification=False,source_adoption=False,prior_H2='PARK'))
    except BaseException as error:
        write(out/'result.json',dict(status='INCOMPLETE_OR_UNSUPPORTED',stage=stage,completed=completed,
            error_type=type(error).__name__,error=str(error),attempt_consumed=True,qualification=False,prior_H2='PARK'))
        raise


if __name__=='__main__':main()
