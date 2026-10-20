"""Bounded Intel baseline diagnostic using the installed topdown-profiler glue.
Run from the uploaded input root, on an exclusively reserved profiling runner.
No source candidate, speed measurement, system configuration or shared DB write.
"""
import dataclasses, hashlib, json, os, signal, subprocess, time
from pathlib import Path
from topdown.collector.toplev import ToplevOptions, ToplevRunner
from topdown.collector.csv_parser import parse_output

OUT = Path('results'); OUT.mkdir(exist_ok=True)
CPU = 2
LEVEL = int(os.environ.get('BPLUS_TMA_LEVEL', '2'))
assert LEVEL in (2,3)
TOPLEV = '/usr/local/lib/python3.12/dist-packages/toplev.py'
PERF = '/usr/lib/linux-tools/7.0.0-1014-aws/perf'
os.environ['PERF'] = PERF
os.environ['TOPLEV_NO_CHECK'] = '1'
# pids=None is intentional: the deployed pids path silently selects CPU0.
runner = ToplevRunner(TOPLEV, ToplevOptions(level=LEVEL, extra_args=['-C', str(CPU)]))
cmd = runner.build_command()
assert cmd.count('-C') == 1 and cmd[cmd.index('-C')+1] == str(CPU)
(OUT/'collector-command.json').write_text(json.dumps(cmd, indent=2)+'\n')
for size in [100000, 1000000]:
    args = ['taskset','-c',str(CPU),'./build/iterator-profile','--size',str(size),
            '--ops','100000000','--member-bytes','16','--seed','7103',
            '--encoding','integer','--direction','forward','--mask','7']
    env = dict(os.environ, BPLUS_PROFILE_STOP='1')
    with (OUT/f'{size}-workload.stdout').open('w') as out, (OUT/f'{size}-workload.stderr').open('w') as err:
        p = subprocess.Popen(args, env=env, stdout=out, stderr=err)
        try:
            deadline = time.monotonic()+30
            while time.monotonic()<deadline:
                assert p.poll() is None, 'workload exited before readiness'
                status = Path(f'/proc/{p.pid}/status').read_text()
                if '\nState:\tT' in status: break
                time.sleep(.05)
            else: raise RuntimeError('no phase marker')
            assert os.sched_getaffinity(p.pid)=={CPU}
            identity = {'pid':p.pid,'cpu':CPU,'smt_siblings':Path(f'/sys/devices/system/cpu/cpu{CPU}/topology/thread_siblings_list').read_text().strip(),
                        'args':args,'binary_sha256':hashlib.sha256(Path('build/iterator-profile').read_bytes()).hexdigest(),
                        'ready':'SIGSTOP after fixture, oracle and warmup', 'scope':'CPU-wide, not PID filtered', 'diagnostic_ops_multiplier':200,
                        'profiled_process_terminated_after_windows':True}
            (OUT/f'{size}-identity.json').write_text(json.dumps(identity,indent=2)+'\n')
            os.kill(p.pid,signal.SIGCONT)
            for rep in range(1,4):
                assert p.poll() is None and os.sched_getaffinity(p.pid)=={CPU}
                before=Path('/proc/stat').read_text()
                workload_before=Path(f'/proc/{p.pid}/stat').read_text()
                stdout,stderr=runner.run(10)
                after=Path('/proc/stat').read_text()
                workload_after=Path(f'/proc/{p.pid}/stat').read_text()
                stem=OUT/f'{size}-L{LEVEL}-{rep}'
                stem.with_suffix('.scope.json').write_text(json.dumps({'cpu_before':before,'cpu_after':after,'workload_before':workload_before,'workload_after':workload_after,'clock_ticks':os.sysconf('SC_CLK_TCK')},indent=2)+'\n')
                stem.with_suffix('.stdout').write_text(stdout)
                stem.with_suffix('.stderr').write_text(stderr)
                samples=parse_output(stderr) or parse_output(stdout)
                stem.with_suffix('.json').write_text(json.dumps([dataclasses.asdict(s) for s in samples],indent=2)+'\n')
                print(json.dumps({'size':size,'rep':rep,'samples':len(samples),'alive':p.poll() is None}),flush=True)
                assert p.poll() is None, 'workload ended inside profile'
                if not samples: raise RuntimeError('collector returned no metrics; inspect raw output')
        finally:
            if p.poll() is None:
                p.terminate(); os.kill(p.pid,signal.SIGCONT)
                try: p.wait(timeout=5)
                except subprocess.TimeoutExpired: p.kill();p.wait()
