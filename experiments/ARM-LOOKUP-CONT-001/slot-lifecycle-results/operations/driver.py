"""Fleet-only native lifecycle correctness check. Separate one-shot claims; no timing."""
import argparse, hashlib, importlib.util, json, math, os, pathlib, re, subprocess, sys, time
sys.dont_write_bytecode = True
P = pathlib.Path
EXPERIMENT = P('experiments/ARM-LOOKUP-CONT-001')
SOURCE = EXPERIMENT/'slot-lifecycle-check'
OLD_SOURCE = EXPERIMENT/'slot-hint-census'
OLD_FREEZE = 'f2f8f882de6d48a6207ffff86f9af5fae53461ff0593e9e06bcc39c4fa82849b'
SOURCE_CUTOFF = 1794636900 # 06:15 UTC
REVIEW_CUTOFF = 1794637800 # 06:30 UTC
STAGE_START = 1794636000 # 06:00 UTC
INFRA_MODULE = EXPERIMENT/'H2-portability-r3/driver.py'
INFRA_SHA = 'dde7363b1d25e2b7c6ce4920b1fc22f3e5a306d4fb6be2bfb6865d4aaa592e80'
INFRA_RECORD_SHA = '66c805dc8eaa4f6f168a09aca177d5d6df2e81c9ea17d0a22e7d7aeeab63ed98'
MODES = ('native',)
FINAL_DEADLINE = 1794638700  # 2026-11-14 06:45 UTC; execution ceiling, unchanged.
BOUNDED = EXPERIMENT/'H2-portability/bounded-command.sh'

def require(value, message):
    if not value: raise ValueError(message)
def timestamp(value): return type(value) in (int,float) and math.isfinite(value)
def sha(path): return hashlib.sha256(P(path).read_bytes()).hexdigest()
def read(path): return json.loads(P(path).read_text())
def write(path, data): P(path).write_text(json.dumps(data, indent=2)+'\n')
def append(path, data):
    with P(path).open('a') as f: f.write(json.dumps(data)+'\n')
def remaining(deadline, cap, now=None):
    now = time.time() if now is None else now
    require(type(cap) is int and 0 < cap <= 300, 'Invalid command cap')
    left = math.floor(min(cap, deadline-now))
    require(left > 20, 'Insufficient command/termination budget')
    return left

def required_inputs(root):
    """Join the complete source freeze and every build/generator dependency."""
    pins={}
    require(sha(root/OLD_SOURCE/'SHA256SUMS')==OLD_FREEZE,'Original census freeze changed')
    for directory in (SOURCE,OLD_SOURCE):
        for line in (root/directory/'SHA256SUMS').read_text().splitlines():
            match=re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
            require(match is not None,'Malformed source freeze')
            pin,rel=match.groups();path=P(rel)
            require(not path.is_absolute() and '..' not in path.parts,'Unsafe frozen path')
            key=str(directory/path);require(key not in pins,'Duplicate frozen path');pins[key]=pin
            require(not (root/key).is_symlink(),'Symlink frozen input')
        pins[str(directory/'SHA256SUMS')]=sha(root/directory/'SHA256SUMS')
    required=('build.sh','check_output.py','validate_static.py','PROTOCOL.md','lifecycle.c','generated/zset_btree.c','shadow.h','deny_clock.c','DEPENDENCIES.json')
    require(all(str(SOURCE/name) in pins for name in required),'Incomplete lifecycle source freeze')
    for directory in ('src','compat','vendor'):
        files=sorted((root/EXPERIMENT/'current'/directory).rglob('*'))
        require(any(f.is_file() for f in files),'Empty build dependency directory')
        for f in files:
            if f.is_file():
                require(not f.is_symlink(),'Symlink dependency');pins[str(f.relative_to(root))]=sha(f)
    for rel in (EXPERIMENT/'lookup.c',BOUNDED,INFRA_MODULE,EXPERIMENT/'fleet_profiler_off_qualification.py'):
        pins[str(rel)]=sha(root/rel)
    dependencies=read(root/SOURCE/'DEPENDENCIES.json')
    require(isinstance(dependencies,dict) and dependencies,'Empty dependency manifest')
    for rel,pin in dependencies.items():
        path=P(rel);require(not path.is_absolute() and '..' not in path.parts,'Unsafe declared dependency')
        key=str(EXPERIMENT/path)
        require(key in pins and pins[key]==pin and sha(root/key)==pin,'Declared dependency not in frozen mapping: '+rel)
    return pins

def admission(root, cfg, approval, mode, now=None):
    now = time.time() if now is None else now
    require(cfg['task_kind']=='SLOT_LIFECYCLE_CORRECTNESS' and cfg['qualification'] is False, 'Wrong task')
    require(cfg['window_scope']=='fleet_execution_only','Execution window scope must be explicit')
    require(all(timestamp(cfg[k]) for k in ('started_epoch','deadline_epoch','source_frozen_epoch')),'Nonfinite or invalid time')
    require(cfg['started_epoch'] <= now < cfg['deadline_epoch'] == FINAL_DEADLINE, 'Diagnostic window closed')
    require(cfg['deadline_epoch']-cfg['started_epoch'] <= 3600, 'Diagnostic window exceeds one hour')
    require(timestamp(cfg['source_frozen_epoch']) and STAGE_START <= cfg['source_frozen_epoch'] <= SOURCE_CUTOFF,'Source freeze missed hard cutoff')
    require(cfg['started_epoch'] >= cfg['source_frozen_epoch'],'Staging predates source freeze')
    require(timestamp(approval['reviewed_epoch']) and cfg['source_frozen_epoch'] <= approval['reviewed_epoch'] <= min(REVIEW_CUTOFF,now),'Independent review missed hard cutoff')
    require(cfg['input_pins']==required_inputs(root),'Incomplete or altered full input mapping')
    require(approval['decision']=='APPROVED' and approval['phase']==mode, 'Unapproved phase')
    require(approval['source_freeze_sha256']==cfg['source_freeze_sha256'] and approval['input_pins']==cfg['input_pins'], 'Review/input mismatch')
    require(cfg['infra_module_sha256']==INFRA_SHA and cfg['infra_record_sha256']==INFRA_RECORD_SHA, 'Infrastructure binding changed')
    require(sha(root/INFRA_MODULE)==INFRA_SHA and sha(root/'portability-staging/isolation-r2.json')==INFRA_RECORD_SHA, 'Immutable infrastructure evidence changed')
    require(sha(root/SOURCE/'SHA256SUMS')==cfg['source_freeze_sha256'], 'Source freeze changed')
    for rel, pin in cfg['input_pins'].items():
        path=P(rel)
        require(not path.is_absolute() and '..' not in path.parts, 'Unsafe input path')
        require(sha(root/path)==pin, 'Input changed: '+rel)
    require(approval['driver_sha256']==sha(__file__), 'Unreviewed operational driver')
    if mode=='test':
        receipt_path=root/'slot-lifecycle-build-001/build-receipt.json'
        require(sha(receipt_path)==approval['build_receipt_sha256'],'Reviewed build receipt changed')
        receipt=read(receipt_path)
        require(receipt['build_only'] is True and receipt['qualification'] is False and set(receipt['artifacts'])==set(MODES),'Incomplete build receipt scope')
        require(receipt['source_freeze_sha256']==cfg['source_freeze_sha256'] and receipt['input_pins']==cfg['input_pins'] and receipt['config_sha256']==approval['config_sha256'],'Build provenance mismatch')
        require(set(approval['binaries'])==set(MODES), 'Missing emitted-code review')
        for build, pin in approval['binaries'].items():
            require(sha(root/'slot-lifecycle-build'/build/'lifecycle')==pin, 'Reviewed ELF changed')
            directory=root/'slot-lifecycle-build'/build
            require(receipt['artifacts'][build]=={'elf_sha256':pin,'assembly_sha256':sha(directory/'assembly.txt'),'compiler_sha256':sha(directory/'compiler.txt'),'flags':'-O3'},'Emitted artifact/compiler/flags mismatch')

def main():
    parser=argparse.ArgumentParser()
    for arg in ('root','mode','config','config-sha256','review','review-sha256','staging-receipt','staging-sha256'): parser.add_argument('--'+arg,required=True)
    args=parser.parse_args();root=P(args.root).resolve();mode=args.mode
    require(mode in ('build','test'),'Unknown phase')
    require(sha(args.config)==args.config_sha256 and sha(args.review)==args.review_sha256, 'Review/config hash mismatch')
    cfg=read(args.config);approval=read(args.review)
    require(approval['config_sha256']==args.config_sha256, 'Review/config join mismatch')
    require(sha(args.staging_receipt)==args.staging_sha256==approval['staging_sha256'], 'Staging receipt changed')
    staged=read(args.staging_receipt)
    require(type(staged.get('schema_version')) is int,'Invalid staging schema version type')
    require(staged=={'schema_version':1,'status':'STAGED','run_root':str(root),'input_pins':cfg['input_pins'],'config_sha256':args.config_sha256,'driver_sha256':sha(__file__),'source_freeze_sha256':cfg['source_freeze_sha256'],'failed_files':[]}, 'Staging incomplete')
    admission(root,cfg,approval,mode)
    os.chdir(root)
    spec=importlib.util.spec_from_file_location('reviewed_infrastructure',root/INFRA_MODULE)
    infra=importlib.util.module_from_spec(spec);spec.loader.exec_module(infra)
    record=read(root/'portability-staging/isolation-r2.json')
    # Finish read-only imports before consuming the exclusive phase directory.
    out=root/('slot-lifecycle-'+mode+'-001');out.mkdir(exist_ok=False)
    # Only the unchanged infrastructure audit is reused. The expired portability
    # task validator/runner is never called and its task window is never rewritten.
    def isolation(stem):
        require(sha(args.config)==args.config_sha256 and sha(args.review)==args.review_sha256 and sha(args.staging_receipt)==args.staging_sha256,'Bound control artifact changed')
        admission(root,cfg,approval,mode)
        for artifact in record['cleanup_artifacts']: require(sha(root/artifact['path'])==artifact['sha256'],'Cleanup changed')
        infra.isolation(root,record,out,stem)
    def run(argv, stem, cap=120):
        bound=remaining(cfg['deadline_epoch'],cap)
        command=['/usr/bin/timeout','--signal=TERM','--kill-after=15s',str(bound-17)+'s',*argv]
        try:
            result=subprocess.run(command,capture_output=True,timeout=bound)
            stdout,stderr,code=result.stdout,result.stderr,result.returncode
        except subprocess.TimeoutExpired as err:
            stdout,stderr,code=err.stdout or b'',err.stderr or b'',None
        (out/(stem+'.stdout')).write_bytes(stdout);(out/(stem+'.stderr')).write_bytes(stderr)
        append(out/'commands.jsonl',{'argv':command,'returncode':code,'cap_seconds':bound,'stem':stem,'qualification':False})
        require(code==0,'Command failed or timed out: '+stem)
        return stdout
    def bracket(argv,stem,cap=120):
        isolation(stem+'-pre')
        primary=None
        try:
            return run(argv,stem,cap)
        except BaseException as error:
            primary=error
            write(out/(stem+'-command-error.json'),{'type':type(error).__name__,'error':str(error)})
            raise
        finally:
            try: isolation(stem+'-post')
            except BaseException as error:
                write(out/(stem+'-isolation-error.json'),{'type':type(error).__name__,'error':str(error),'command_error_also_present':primary is not None})
                if primary is None: raise
    completed=[]
    try:
        isolation('admission')
        write(out/'admission.json',{'phase':mode,'config_sha256':args.config_sha256,'review_sha256':args.review_sha256,'staging_sha256':args.staging_sha256,'qualification':False,'source_adoption':False,'prior_H2':'PARK'})
        if mode=='build':
            target=root/'slot-lifecycle-build';target.mkdir(exist_ok=False)
            cmd=['env','TASK_CC=cc','LC_ALL=C','LANG=C','sh',str(SOURCE/'build.sh'),str(target/'native'),'native']
            bracket(cmd,'native-compile',300)
            directory=target/'native'
            artifacts={'native':{'elf_sha256':sha(directory/'lifecycle'),'assembly_sha256':sha(directory/'assembly.txt'),'compiler_sha256':sha(directory/'compiler.txt'),'flags':'-O3'}}
            completed.append('native')
            bracket(['python3',str(SOURCE/'validate_static.py'),str(directory)],'static-validation')
            isolation('final')
            write(out/'build-receipt.json',{'artifacts':artifacts,'input_pins':cfg['input_pins'],'source_freeze_sha256':cfg['source_freeze_sha256'],'config_sha256':args.config_sha256,'build_only':True,'qualification':False})
        else:
            bracket(['taskset','-c','2',str(root/'slot-lifecycle-build/native/lifecycle')],'native-lifecycle',120)
            require(not (out/'native-lifecycle.stderr').read_bytes(),'Unexpected lifecycle stderr')
            completed.append('native-lifecycle')
            bracket(['python3',str(SOURCE/'check_output.py'),str(out/'native-lifecycle.stdout')],'native-validation')
            isolation('final')
        write(out/'COMPLETE.json',{'status':'COMPLETE_BUILD_ONLY' if mode=='build' else 'COMPLETE_LIFECYCLE_CORRECTNESS','completed':completed,'qualification':False,'source_adoption':False})
    except BaseException as error:
        write(out/'ERROR.json',{'status':'INCOMPLETE_DIAGNOSTIC','completed':completed,'error_type':type(error).__name__,'error':str(error),'attempt_consumed':True,'qualification':False,'source_adoption':False});raise
if __name__=='__main__': main()
