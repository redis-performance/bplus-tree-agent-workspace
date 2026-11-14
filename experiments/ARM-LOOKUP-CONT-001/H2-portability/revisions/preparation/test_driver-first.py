"""Synthetic validation only. No subprocess, emulator, service or C execution."""
import copy
import hashlib
import importlib.util
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

spec=importlib.util.spec_from_file_location('portability',Path(__file__).with_name('driver.py'))
d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)

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
        compiler_endian=t['data'],compiler_little=1,compiler_big=2,
        node=20 if n==4 else 24,leaf_data=44 if n==4 else 56,align_u64=n,align_leaf=n,
        cache_size=2 if variant=='B' else 0,cache_offset=18 if variant=='B' else -1,
        flags_offset=14 if variant=='B' else -1,moved_offset=15,resize_offset=16)

def record(root):
    names={'image':root.name+'-portability-image','check':root.name+'-portability-check'}
    return dict(owner=d.OWNER,run_root=str(root),lease_generation='a'*32,lease_sha256='b'*64,
        deadline=5000,coordinator={'pid':123,'start_ticks':'555'},service={'name':'parca.service'},
        containers=names,container_labels={'org.redis-performance.cleanup.owner':d.OWNER,
            'org.redis-performance.cleanup.root':str(root),'org.redis-performance.cleanup.generation':'a'*32},
        cleanup_contract=dict(containers=names,reap_containers_before_resume=True,restore_sibling50=True,ownership_required=True),
        base_image_id=d.BASE_IMAGE,cleanup_timers=['first.timer','second.timer'],
        cleanup_timer_schedules=[dict(unit=t,NextElapseUSecRealtime='reviewed',NextElapseUSecMonotonic='0',fire_epoch=4500) for t in ('first.timer','second.timer')],
        cleanup_services=[dict(unit='cleanup.service',exec_start_sha256=hashlib.sha256(b'exec\n').hexdigest())])

class Validators(unittest.TestCase):
    def test_elf_positive(self):
        for target in d.TARGETS:self.assertEqual(d.check_elf(elf(target),target)['interpreter'],'/lib/guest-loader.so')
    def test_elf_header_and_interpreter_negatives(self):
        for target in d.TARGETS:
            for offset,value in ((0,0),(4,0),(5,0),(18,0),(64,0),(128,ord('.'))):
                b=bytearray(elf(target));b[offset]=value
                with self.subTest(target=target,offset=offset),self.assertRaises(ValueError):d.check_elf(b,target)
            with self.assertRaises(ValueError):d.check_elf(elf(target)[:64],target)
    def test_abi_positive(self):
        for target in d.TARGETS:
            for variant in ('base','B'):d.check_abi(abi(target,variant),target,variant)
    def test_abi_rejects_wrong_width_endian_cache(self):
        for field,value in (('pointer',8),('endian','big'),('mantissa',52),('cache_size',1),('compiler_endian',2)):
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
        for text in (' U clock_gettime\n','00001234 T __wrap_clock_gettime\n U clock_gettime@GLIBC_2.17\n',''):
            with self.assertRaises(ValueError):d.check_clock_symbols(text)
    def test_claim(self):
        with tempfile.TemporaryDirectory() as root:
            d.claim(root,'correctness')
            with self.assertRaises(FileExistsError):d.claim(root,'correctness')
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
                if name.endswith('thread_siblings_list'):return '2,50'
                raise AssertionError(name)
            def run(argv,**kwargs):
                if argv[:3]==['docker','ps','-q']:return SimpleNamespace(returncode=0,stdout=b'other\n' if bad=='docker' else b'',stderr=b'')
                unit=argv[2]
                if '--value' in argv:return SimpleNamespace(returncode=0,stdout=b'changed\n' if bad=='exec' else b'exec\n',stderr=b'')
                if unit.endswith('.timer'):values={'ActiveState':'active','Unit':'cleanup.service','NextElapseUSecRealtime':'changed' if bad=='timer' else 'reviewed','NextElapseUSecMonotonic':'0'}
                else:values={'ActiveState':'active' if bad=='parca' else 'inactive','SubState':'dead','MainPID':'0','CPUAffinity':'','AllowedCPUs':''}
                return SimpleNamespace(returncode=0,stdout=('\n'.join(k+'='+v for k,v in values.items())+'\n').encode(),stderr=b'')
            with patch.object(d,'sha',return_value='b'*64),patch.object(d,'read',return_value=lease),patch.object(d.time,'time',return_value=1000),patch.object(d.os,'sched_getaffinity',return_value={0}),patch.object(d.platform,'machine',return_value='x86_64'),patch.object(Path,'read_text',text),patch.object(Path,'iterdir',return_value=iter([])),patch.object(d.subprocess,'run',side_effect=run):
                d.isolation(root,r,root,'synthetic')
    def test_valid(self):self.exercise()
    def test_live_negative_gates(self):
        for bad in ('generation','expired','coordinator','sibling','docker','exec','timer','parca'):
            with self.subTest(bad=bad),self.assertRaises(ValueError):self.exercise(bad)
    def test_parca_redaction(self):
        result=d.parca_process_match(123,b'parca-agent',b'parca-agent --token SECRET')
        self.assertNotIn('SECRET',str(result));self.assertTrue(result['cmdline_redacted'])

class RunnerTests(unittest.TestCase):
    def test_labels_and_postcheck_after_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);r=record(root);runner=d.Runner(root,root,r,lambda:None,'sha256:'+'c'*64,4000)
            with patch.object(d,'isolation') as gate,patch.object(runner,'raw',side_effect=[b'',ValueError('failed')]) as raw:
                with self.assertRaises(ValueError):runner.container(['qemu-i386','-cpu','max','/guest'],'failure')
                argv=raw.call_args_list[-1].args[0]
                for key,value in r['container_labels'].items():self.assertIn(key+'='+value,argv)
                self.assertEqual(gate.call_count,2);self.assertTrue(gate.call_args.args[-1].endswith('-post'))
    def test_timeout_clamped_to_cleanup_margin(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);r=record(root);runner=d.Runner(root,root,r,lambda:None,'image',1003)
            with patch.object(d.time,'monotonic',return_value=1000),patch.object(d.time,'time',return_value=1000),patch.object(d.subprocess,'run',return_value=SimpleNamespace(returncode=0,stdout=b'ok',stderr=b'')) as run:
                runner.raw(['synthetic'],'bounded',300)
                self.assertEqual(run.call_args.kwargs['timeout'],3)
    def test_expired_budget_never_launches(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);runner=d.Runner(root,root,record(root),lambda:None,'image',999)
            with patch.object(d.time,'monotonic',return_value=1000),patch.object(d.time,'time',return_value=1000),patch.object(d.subprocess,'run') as run:
                with self.assertRaises(ValueError):runner.raw(['synthetic'],'expired')
                run.assert_not_called()

if __name__=='__main__':unittest.main(verbosity=2)
