"""Synthetic validation only. No subprocess, emulator, service or C execution."""
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

spec=importlib.util.spec_from_file_location('portability',Path(__file__).with_name('driver.py'))
d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
# Synthetic operational clock only; production constants remain frozen in driver.
d.TASK_WINDOW=(1000,2800)

def elf(target):
    t=d.TARGETS[target];bits=t['class'];order=t['endian'];buf=bytearray(256)
    buf[:7]=b'\x7fELF'+bytes([bits,t['data'],1])
    def word(offset,n,value):buf[offset:offset+n]=value.to_bytes(n,order)
    word(18,2,t['machine']);word(28 if bits==1 else 32,4 if bits==1 else 8,64)
    word(42 if bits==1 else 54,2,32 if bits==1 else 56);word(44 if bits==1 else 56,2,1)
    interp=b'/lib/guest-loader.so\0';word(64,4,3);word(68 if bits==1 else 72,4 if bits==1 else 8,128)
    word(80 if bits==1 else 96,4 if bits==1 else 8,len(interp));buf[128:128+len(interp)]=interp
    return bytes(buf)

def abi(target,variant):
    t=d.TARGETS[target];n=t['pointer']
    return dict(variant=variant,endian=t['endian'],pointer=n,size_t=n,ulong=n,u64=8,double=8,
        char_bit=8,radix=2,mantissa=53,max_exp=1024,moved_size=1,resize_size=2,
        compiler_endian=1234 if t['endian']=='little' else 4321,compiler_little=1234,compiler_big=4321,
        node=20 if n==4 else 24,leaf_data=44 if n==4 else 56,align_u64=n,align_leaf=n,
        cache_size=2 if variant=='B' else 0,cache_offset=18 if variant=='B' else -1,
        flags_offset=14 if variant=='B' else -1,moved_offset=15,resize_offset=16)

def record(root):
    names={'image':root.name+'-portability-image','check':root.name+'-portability-check'}
    return dict(owner=d.OWNER,run_root=str(root),lease_generation='a'*32,lease_sha256='b'*64,
        cpu2_expected_siblings='2',saved_sibling_pair='2,50',deadline=5000,task_started_epoch=1000,task_deadline_epoch=2800,coordinator={'pid':123,'start_ticks':'555'},service={'name':'parca.service'},
        containers=names,container_labels={'org.redis-performance.cleanup.owner':d.OWNER,
            'org.redis-performance.cleanup.root':str(root),'org.redis-performance.cleanup.generation':'a'*32},
        cleanup_contract=dict(containers=names,reap_containers_before_resume=True,restore_sibling50=True,ownership_required=True),
        base_image_id=d.BASE_IMAGE,cleanup_service_properties=d.CLEANUP_CAPS,timer_properties=d.TIMER_CAPS,
        retired_timers=['old-one.timer','old-two.timer'],cleanup_timers=['first.timer','second.timer'],
        cleanup_timer_schedules=[dict(unit=t,NextElapseUSecRealtime='reviewed',NextElapseUSecMonotonic='0',fire_epoch=4500) for t in ('first.timer','second.timer')],
        cleanup_services=[dict(unit='cleanup.service',exec_start_sha256=hashlib.sha256(b'exec\n').hexdigest())])

class Validators(unittest.TestCase):
    def test_elf_positive(self):
        for target in d.TARGETS:self.assertEqual(d.check_elf(elf(target),target)['interpreter'],'/lib/guest-loader.so')
    def test_elf_header_and_interpreter_negatives(self):
        for target in d.TARGETS:
            for offset,value in ((0,0),(4,0),(5,0),(18,0),(64,0),(128,ord('.'))):
                b=bytearray(elf(target));b[offset]^=1
                with self.subTest(target=target,offset=offset),self.assertRaises(ValueError):d.check_elf(b,target)
            with self.assertRaises(ValueError):d.check_elf(elf(target)[:64],target)
    def test_abi_positive(self):
        for target in d.TARGETS:
            for variant in ('base','B'):d.check_abi(abi(target,variant),target,variant)
    def test_abi_rejects_wrong_width_endian_cache(self):
        for field,value in (('pointer',8),('endian','big'),('mantissa',52),('cache_size',1),('compiler_endian',4321),('compiler_little',1),('pointer',True),('node',20.0)):
            row=abi('i686','B');row[field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):d.check_abi(row,'i686','B')
    def test_baseline_no_fake_cache(self):
        row=abi('i686','base');row['cache_size']=2
        with self.assertRaises(ValueError):d.check_abi(row,'i686','base')
    def test_unit_exact57(self):
        text='\n'.join(f'{i} - test: PASSED' for i in range(1,58))+'\n  Tests:       57 passed, 0 failed, 57 total\n'
        d.check_unit(text)
        for bad in (text.replace('1 -','2 -',1),text.replace('PASSED','FAILED',1),text+text,text.replace('57 total','56 total')):
            with self.assertRaises(ValueError):d.check_unit(bad)
    def test_verify(self):
        row=dict(verified=True,case='hit',seed=17,members=500,owned_bytes=123)
        d.check_verify(row,'hit',17)
        for field,value in (('case','miss'),('seed',29),('members',499),('owned_bytes',0),('elapsed_ns',1)):
            bad=dict(row);bad[field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):d.check_verify(bad,'hit',17)
    def test_oracle_counts(self):
        d.check_oracle({'passed':True,'output_checks':90000},'output_oracle')
        with self.assertRaises(ValueError):d.check_oracle({'passed':True,'output_checks':45000},'output_oracle')
        with self.assertRaises(ValueError):d.check_oracle({'passed':True,'output_checks':90000.0},'output_oracle')
        row=dict(passed=True,zero_full_reversed=True,flag_shift_cases=256,validations=7693,leaves_checked=1,relocated_pages=1,refresh_sites=4)
        d.check_oracle(row,'paired')
        for field,value in (('refresh_sites',3),('validations',7692),('relocated_pages',0)):
            bad=dict(row);bad[field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):d.check_oracle(bad,'paired')
    def test_no_measure_plan_and_exact_grid(self):
        for target in d.TARGETS:
            for variant in ('base','B'):
                plan=d.execution_plan(target,variant);lookups=[a for k,a in plan if k=='lookup']
                self.assertEqual(lookups,[('verify',case,str(seed),'1') for seed in (17,29,43) for case in d.CASES])
                self.assertFalse(any('measure' in a for _,a in plan))
                self.assertEqual(sum(k=='original_metadata' for k,_ in plan),int(variant=='B'))
    def test_clock_symbols(self):
        d.check_clock_symbols('00001234 T __wrap_clock_gettime\n U abort@GLIBC_2.2\n')
        for text in ('00001234 T __wrap_clock_gettime\n U __clock_gettime64@GLIBC_2.34\n',' U clock_gettime\n','00001234 T __wrap_clock_gettime\n U clock_gettime@GLIBC_2.17\n',''):
            with self.assertRaises(ValueError):d.check_clock_symbols(text)
    def test_clock_call_proof(self):
        for text in ('123: call 567 <__wrap_clock_gettime>','123: brasl %r14,567 <__wrap_clock_gettime>'):
            d.check_clock_disassembly(text)
        with self.assertRaises(ValueError):d.check_clock_disassembly('00001234 <__wrap_clock_gettime>:\n')
    def test_claim(self):
        with tempfile.TemporaryDirectory() as root:
            d.claim(root,'correctness')
            with self.assertRaises(FileExistsError):d.claim(root,'correctness')
    def test_staging_identity_and_completeness(self):
        receipt=dict(schema_version=1,status='STAGED',run_root='/reviewed',manifest_sha256='m',
            verified_files={'source':'h'},failed_files=[],isolation_sha256='i')
        d.validate_staging(receipt,Path('/reviewed'),'m',{'source':'h'},'i')
        for key,value in (('status','FAILED'),('schema_version',True),('run_root','/other'),
                          ('manifest_sha256','wrong'),('isolation_sha256','old'),
                          ('verified_files',{}),('failed_files',['source'])):
            bad=dict(receipt);bad[key]=value
            with self.subTest(key=key),self.assertRaises(ValueError):
                d.validate_staging(bad,Path('/reviewed'),'m',{'source':'h'},'i')

    def test_record_shared_budget_rejects_extension(self):
        root=Path('/reviewed');r=record(root);r['task_deadline_epoch']=2801
        review=dict(schema_version=1,decision='APPROVED',reviewer_role='reviewer',isolation_sha256='x',manifest_sha256='y',phase='correctness',image_id='z')
        with patch.object(d.q4,'validate_record'):
            with self.assertRaises(ValueError):d.validate_record(r,review,root,'x','y','correctness','z')
    def test_record_label_binding(self):
        root=Path('/reviewed');r=record(root)
        review=dict(schema_version=1,decision='APPROVED',reviewer_role='reviewer',isolation_sha256='x',manifest_sha256='y',phase='correctness',image_id='z')
        with patch.object(d.q4,'validate_record'):
            d.validate_record(r,review,root,'x','y','correctness','z')
            r['container_labels']['org.redis-performance.cleanup.generation']='wrong'
            with self.assertRaises(ValueError):d.validate_record(r,review,root,'x','y','correctness','z')

class Isolation(unittest.TestCase):
    def exercise(self,bad=None):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);r=record(root)
            lease=dict(owner=d.OWNER,state='RESERVED',deadline=5000,coordinator_pid=123,coordinator_ticks='555',run_root=str(root),lease_generation='a'*32)
            if bad=='generation':lease['lease_generation']='wrong'
            if bad=='expired':lease['deadline']=1100
            def text(path,*a,**k):
                name=str(path)
                if name.endswith('/123/stat'):return '123 (coord) '+' '.join(['R' if bad=='coordinator' else 'T']+['0']*18+['555'])
                if name.endswith('/cpu2/online'):return '1'
                if name.endswith('/cpu50/online'):return '1' if bad=='sibling' else '0'
                if name.endswith('thread_siblings_list'):return '2,50' if bad=='online-topology' else '2'
                raise AssertionError(name)
            def run(argv,**kwargs):
                if argv[:3]==['docker','ps','-q']:return SimpleNamespace(returncode=0,stdout=b'other\n' if bad=='docker' else b'',stderr=b'')
                unit=argv[2]
                if '--value' in argv:return SimpleNamespace(returncode=0,stdout=b'changed\n' if bad=='exec' else b'exec\n',stderr=b'')
                if unit in r['retired_timers']:values={'ActiveState':'active' if bad=='old-timer' else 'inactive'}
                elif unit=='cleanup.service':values=dict(d.CLEANUP_CAPS,KillMode='process' if bad=='service-caps' else 'control-group')
                elif unit.endswith('.timer'):values={'ActiveState':'active','Unit':'cleanup.service','NextElapseUSecRealtime':'changed' if bad=='timer' else 'reviewed','NextElapseUSecMonotonic':'0',**dict(d.TIMER_CAPS,AccuracyUSec='1s' if bad=='timer-caps' else '1us')}
                else:values={'ActiveState':'active' if bad=='parca' else 'inactive','SubState':'dead','MainPID':'0','CPUAffinity':'','AllowedCPUs':''}
                return SimpleNamespace(returncode=0,stdout=('\n'.join(k+'='+v for k,v in values.items())+'\n').encode(),stderr=b'')
            with patch.object(d,'sha',return_value='b'*64),patch.object(d,'read',return_value=lease),patch.object(d.time,'time',return_value=1000),patch.object(d.os,'sched_getaffinity',return_value={0}),patch.object(d.platform,'machine',return_value='x86_64'),patch.object(Path,'read_text',text),patch.object(Path,'iterdir',return_value=iter([])),patch.object(d.subprocess,'run',side_effect=run):
                d.isolation(root,r,root,'synthetic')
    def test_valid(self):self.exercise()
    def test_live_negative_gates(self):
        for bad in ('generation','expired','coordinator','sibling','docker','exec','timer','parca','old-timer','service-caps','timer-caps','online-topology'):
            with self.subTest(bad=bad),self.assertRaises(ValueError):self.exercise(bad)
    def test_parca_redaction(self):
        result=d.parca_process_match(123,b'parca-agent',b'parca-agent --token SECRET')
        self.assertNotIn('SECRET',str(result));self.assertTrue(result['cmdline_redacted'])

class RunnerTests(unittest.TestCase):
    def test_labels_and_postcheck_after_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);r=record(root);runner=d.Runner(root,root,r,lambda:None,'sha256:'+'c'*64,4000,'correctness')
            with patch.object(d.time,'time',return_value=1000),patch.object(d,'isolation') as gate,patch.object(runner,'raw',side_effect=[b'',ValueError('failed')]) as raw:
                with self.assertRaises(ValueError):runner.container(['qemu-i386','-cpu','max','/guest'],'failure')
                argv=raw.call_args_list[-1].args[0]
                for key,value in r['container_labels'].items():self.assertIn(key+'='+value,argv)
                self.assertEqual(gate.call_count,2);self.assertTrue(gate.call_args.args[-1].endswith('-post'))
                wrapper=argv.index('/work/'+str(d.HARNESS/'bounded-command.sh'))
                self.assertEqual(argv[wrapper+1],'1120')
                self.assertEqual(argv[wrapper+2:],['qemu-i386','-cpu','max','/guest'])
    def test_host_export_forbidden_in_correctness(self):
        root=Path('/reviewed');runner=d.Runner(root,root,record(root),lambda:None,'image',4000,'correctness')
        with patch.object(runner,'raw',side_effect=AssertionError('Docker forbidden')) as raw:
            with self.assertRaises(ValueError):runner.export_receipts()
            raw.assert_not_called()
    def test_exact_stopped_container_identity(self):
        cid='c'*64;labels={'owner':'owned'}
        info=dict(Id=cid,Name='/owned',Image='image',Config={'Labels':labels},State={'Status':'created','Running':False,'Pid':0},
            HostConfig={'NetworkMode':'none','ReadonlyRootfs':True,'CapDrop':['ALL'],'CapAdd':[]},Mounts=[],Path='/bin/true',Args=[])
        d.check_export_container(info,cid,'owned','image',labels)
        for section,key,value in ((None,'Id','f'*64),(None,'Image','foreign'),('Config','Labels',{'owner':'foreign'}),
                                  ('State','Pid',123),('State','Status','exited'),('HostConfig','CapAdd',['CHOWN'])):
            bad=copy.deepcopy(info)
            if section:bad[section][key]=value
            else:bad[key]=value
            with self.subTest(section=section,key=key),self.assertRaises(ValueError):d.check_export_container(bad,cid,'owned','image',labels)
    def test_foreign_container_rejected_before_copy(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);r=record(root);runner=d.Runner(root,root,r,lambda:None,'image',4000,'image-receipt')
            outputs=[b'',('c'*64).encode(),json.dumps([{'Id':'f'*64}]).encode()]
            with patch.object(d,'isolation'),patch.object(runner,'raw',side_effect=outputs) as raw:
                with self.assertRaises(ValueError):runner.export_receipts()
                self.assertFalse(any(call.args[0][:2]==['docker','cp'] for call in raw.call_args_list))
                self.assertFalse(any(call.args[0][:2]==['docker','rm'] for call in raw.call_args_list))
    def test_host_export_exact_six_items_never_starts_container(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);r=record(root);runner=d.Runner(root,root,r,lambda:None,'image',4000,'image-receipt')
            cid='c'*64;name=r['containers']['check'];calls=[]
            info=dict(Id=cid,Name='/'+name,Image='image',Config={'Labels':r['container_labels']},
                State={'Status':'created','Running':False,'Pid':0},HostConfig={'NetworkMode':'none','ReadonlyRootfs':True,'CapDrop':['ALL'],'CapAdd':[]},Mounts=[],Path='/bin/true',Args=[])
            def raw(argv,*args):
                calls.append(argv)
                if argv[1]=='ps':return b''
                if argv[1]=='create':return cid.encode()
                if argv[1]=='inspect':return json.dumps([info]).encode()
                if argv[1]=='cp':
                    target=Path(argv[-1])
                    if target.name in ('apt-config','apt-lists'):
                        target.mkdir()
                        if target.name=='apt-lists':
                            (target/'partial').mkdir(mode=0o700);(target/'auxfiles').mkdir(mode=0o700)
                    else:target.write_text('receipt')
                    return b''
                if argv[1]=='rm':return cid.encode()
                raise AssertionError(argv)
            with patch.object(d,'isolation'),patch.object(runner,'raw',side_effect=raw):runner.export_receipts()
            copies=[x for x in calls if x[1]=='cp']
            self.assertEqual(len(copies),6)
            self.assertEqual([x[-2].split('/')[-1] for x in copies],list(d.RECEIPT_ITEMS))
            self.assertTrue(all(x[2]=='-a' and '-L' not in x for x in copies))
            self.assertEqual(calls[-1],['docker','rm',cid]);self.assertFalse(any(x[1]=='start' for x in calls))

    def test_host_inventory_preserves_partial_and_symlinks(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            for item in d.RECEIPT_ITEMS:
                if item in ('apt-config','apt-lists'):(root/item).mkdir()
                else:(root/item).write_text('receipt')
            (root/'apt-lists/partial').mkdir(mode=0o700);(root/'apt-lists/auxfiles').mkdir(mode=0o700)
            (root/'apt-config/link').symlink_to('not-followed')
            rows=d.receipt_inventory(root)
            self.assertTrue(any(r['path']=='apt-lists/partial' and r['mode']==0o700 for r in rows))
            self.assertTrue(any(r['kind']=='symlink' and r['target']=='not-followed' for r in rows))
            (root/'apt-lists/partial').rmdir()
            with self.assertRaises(ValueError):d.receipt_inventory(root)

    def test_absolute_command_ceiling_and_grace(self):
        r=record(Path('/reviewed'))
        self.assertEqual(d.command_ceiling(r,120,1000),1120)
        self.assertEqual(d.command_ceiling(r,300,1000),1300)
        self.assertEqual(d.command_ceiling(r,300,2700),2800)
        r['cleanup_timer_schedules'][0]['fire_epoch']=1400
        self.assertEqual(d.command_ceiling(r,300,1000),1100)
        with self.assertRaises(ValueError):d.command_ceiling(r,300,1083)
        with self.assertRaises(ValueError):d.command_ceiling(r,301,1000)
    def test_delayed_start_cannot_renew_timeout(self):
        ceiling=d.command_ceiling(record(Path('/reviewed')),120,1000)
        # Exact shell arithmetic after Docker startup, no clock/process calls.
        self.assertEqual(ceiling-1050-17,53)
        self.assertLessEqual(ceiling-1103-17,0)
        text=(Path(__file__).parent.parent/'H2-portability/bounded-command.sh').read_text()
        self.assertIn('portability_ceiling - portability_now - 17',text)
        self.assertIn('exec /usr/bin/timeout --signal=TERM --kill-after=15s',text)
        self.assertIn('"$@"',text)
    def test_timeout_clamped_to_cleanup_margin(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);r=record(root);runner=d.Runner(root,root,r,lambda:None,'image',1003,'correctness')
            with patch.object(d.time,'monotonic',return_value=1000),patch.object(d.time,'time',return_value=1000),patch.object(d.subprocess,'run',return_value=SimpleNamespace(returncode=0,stdout=b'ok',stderr=b'')) as run:
                runner.raw(['synthetic'],'bounded',300)
                self.assertEqual(run.call_args.kwargs['timeout'],3)
    def test_expired_budget_never_launches(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);runner=d.Runner(root,root,record(root),lambda:None,'image',999,'correctness')
            with patch.object(d.time,'monotonic',return_value=1000),patch.object(d.time,'time',return_value=1000),patch.object(d.subprocess,'run') as run:
                with self.assertRaises(ValueError):runner.raw(['synthetic'],'expired')
                run.assert_not_called()

class MatrixTests(unittest.TestCase):
    def exercise(self,fail_baseline=False,failed_staging=False):
        from contextlib import ExitStack
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);h=root/d.CODE;h.mkdir(parents=True)
            (root/d.HARNESS).mkdir(parents=True)
            source=root/d.EXP/'current/src/zset_btree.c';source.parent.mkdir(parents=True);source.write_bytes(b'baseline')
            candidate=root/'H2-B-source/zset_btree.c';candidate.parent.mkdir();candidate.write_bytes(b'candidate')
            prepare=root/d.HARNESS/'prepare-image.sh';prepare.write_bytes(b'prepared')
            manifest={'files':{str(x.relative_to(root)):d.sha(x) for x in (source,candidate,prepare)}}
            manifest_path=h/'files.json';d.write(manifest_path,manifest);manifest_sha=d.sha(manifest_path)
            image='sha256:'+'c'*64
            receipt_path=root/'receipt.json';d.write(receipt_path,dict(schema_version=1,status='IMAGE_PREPARED',image_id=image,base_image_id=d.BASE_IMAGE,manifest_sha256=manifest_sha,cpu_policy='-cpu max'))
            r=record(root);r['cleanup_artifacts']=[];record_path=root/'record.json';d.write(record_path,r)
            staging_path=root/'staging.json';d.write(staging_path,dict(schema_version=1,status='FAILED' if failed_staging else 'STAGED',
                run_root=str(root),manifest_sha256=manifest_sha,verified_files=manifest['files'],failed_files=['failed'] if failed_staging else [],isolation_sha256=d.sha(record_path)))
            review_path=root/'review.json';d.write(review_path,{'image_receipt_sha256':d.sha(receipt_path),'staging_receipt_sha256':d.sha(staging_path)})
            argv=['driver','--root',str(root),'--mode','correctness','--image-id',image,
                '--manifest-sha256',manifest_sha,'--isolation-record',str(record_path),'--isolation-sha256',d.sha(record_path),
                '--review',str(review_path),'--review-sha256',d.sha(review_path),
                '--image-receipt',str(receipt_path),'--image-receipt-sha256',d.sha(receipt_path),
                '--staging-receipt',str(staging_path),'--staging-receipt-sha256',d.sha(staging_path)]
            calls=[]
            class FakeRunner:
                def __init__(self,root,out,*args):
                    if failed_staging:raise AssertionError('Runner constructed after failed staging')
                    self.out=out;self.sequence=0
                def raw(self,argv,stem):
                    return json.dumps([{'Id':image,'Config':{'Labels':{'h2.portability.base':d.BASE_IMAGE,'h2.portability.prepare':d.sha(prepare)}}}]).encode()
                def container(self,argv,stage,timeout=120):
                    self.sequence+=1;stem=str(self.sequence);calls.append(stage);output=b''
                    if argv[0]=='sh':
                        target,variant=argv[-2:];directory=self.out/(target+'-'+variant);directory.mkdir()
                        for name in {k for k,a in d.execution_plan(target,variant)}:(directory/name).write_bytes(elf(target))
                    elif argv[0]=='readlink':output=(argv[-1]+'\n').encode()
                    elif argv[0].endswith('-nm'):output=b'00001234 T __wrap_clock_gettime\n'
                    elif argv[0].endswith('-objdump'):output=b'123: call 567 <__wrap_clock_gettime>\n'
                    elif argv[0].startswith('qemu-'):
                        binary=next(x for x in argv if x.startswith('/out/'));cell,kind=binary.split('/')[-2:]
                        target,variant=cell.split('-')
                        if kind=='abi':output=json.dumps(abi(target,variant)).encode()
                        elif kind=='unit':
                            output=('FAILED\n' if fail_baseline and variant=='base' else '\n'.join(f'{i} - test: PASSED' for i in range(1,58))+'\n  Tests:       57 passed, 0 failed, 57 total\n').encode()
                        elif kind=='lookup':
                            _,case,seed,_=argv[-4:];output=json.dumps(dict(verified=True,case=case,seed=int(seed),members=500,owned_bytes=123)).encode()
                        elif kind in ('output_oracle','output_external_oracle'):
                            output=json.dumps(dict(passed=True,output_checks=90000 if kind=='output_oracle' else 45000)).encode()
                        else:
                            row=dict(passed=True,zero_full_reversed=True,flag_shift_cases=256,validations=7693,leaves_checked=1,relocated_pages=1)
                            if kind=='paired':row['refresh_sites']=4
                            output=json.dumps(row).encode()
                    (self.out/(stem+'.stdout')).write_bytes(output);(self.out/(stem+'.stderr')).write_bytes(b'')
                    return output,stem
            with ExitStack() as stack:
                for context in (patch('sys.argv',argv),patch.object(d,'Runner',FakeRunner),patch.object(d,'validate_record'),
                    patch.object(d,'isolation'),patch.object(d,'BASE',d.sha(source)),patch.object(d,'B',d.sha(candidate)),
                    patch.object(d.time,'time',return_value=1000),patch.object(d.time,'monotonic',return_value=1000),
                    patch.object(d.subprocess,'run',side_effect=AssertionError('real process prohibited'))):stack.enter_context(context)
                if fail_baseline or failed_staging:
                    with self.assertRaises(ValueError):d.main()
                else:d.main()
                with self.assertRaises(FileExistsError):d.main()
            result=d.read(root/'H2-portability-r3-correctness-001/result.json')
            return calls,result
    def test_failed_staging_never_constructs_or_launches_container(self):
        calls,result=self.exercise(failed_staging=True)
        self.assertEqual(calls,[]);self.assertTrue(result['attempt_consumed'])
        self.assertEqual(result['status'],'INCOMPLETE_OR_UNSUPPORTED')
    def test_complete_mocked_matrix(self):
        calls,result=self.exercise()
        self.assertEqual(result['status'],'CORRECTNESS_COMPLETE');self.assertEqual(len(result['completed']),94)
        self.assertEqual([c for c in calls if c.endswith('-build')],['i686-base-build','i686-B-build','s390x-base-build','s390x-B-build'])
        self.assertFalse(result['qualification']);self.assertEqual(result['prior_H2'],'PARK')
    def test_baseline_failure_never_runs_B_or_next_ABI(self):
        calls,result=self.exercise(True)
        self.assertEqual(result['status'],'INCOMPLETE_OR_UNSUPPORTED');self.assertTrue(result['attempt_consumed'])
        self.assertFalse(any('-B-' in c or c.startswith('s390x') for c in calls))

if __name__=='__main__':unittest.main(verbosity=2)
