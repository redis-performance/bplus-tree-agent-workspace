"""Independent read-only reconstruction from immutable git objects; no runner access."""
import hashlib,json,math,subprocess
from datetime import datetime
from pathlib import Path
REV='8a0f9e564'
ROOT='experiments/NIGHT-EXPLORATION-001/ambient-observation/'
INPUTS={}
def raw(path):
    data=subprocess.check_output(['git','show',REV+':'+path])
    INPUTS[path]=hashlib.sha256(data).hexdigest()
    return data
def obj(name):return json.loads(raw(ROOT+name))
def close(a,b):assert math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12),(a,b)
def utc(t):return datetime.fromisoformat(t)
freeze=obj('freeze.json');published=obj('RESULT.json');plan=raw(ROOT+'PLAN.md');script=raw('scripts/observe-idle-runner.py')
assert hashlib.sha256(plan).hexdigest()==freeze['plan_sha256']
assert hashlib.sha256(script).hexdigest()==freeze['script_sha256']
assert INPUTS[ROOT+'freeze.json']==published['freeze_sha256']
assert (freeze['samples_per_host'],freeze['interval_seconds'],freeze['owned_cap_seconds'],freeze['retry_allowed'])==(61,10,620,False)
readme=raw(ROOT+'README.md').decode();hosts={}
for host in ['intel','amd','arm']:
    meta=obj(host+'/metadata.json');job=obj(host+'/job.json')
    samples=[json.loads(line) for line in raw(ROOT+host+'/samples.jsonl').splitlines()]
    intervals=obj(host+'/intervals.json');reported=published['hosts'][host]
    assert len(samples)==61 and len(intervals)==60
    assert meta['status']=='complete' and meta['script_sha256']==freeze['script_sha256']
    assert meta['samples']==61 and meta['expected_intervals']==60 and meta['interval_seconds']==10
    assert job['returncode']==0 and job['limit_seconds']==620 and job['cpu']==2
    assert utc(freeze['frozen_at'])<utc(job['started_utc'])<=utc(meta['started_utc'])<=utc(samples[0]['utc'])
    assert utc(samples[-1]['utc'])<=utc(meta['finished_utc'])<=utc(job['finished_utc'])
    job_elapsed=(utc(job['finished_utc'])-utc(job['started_utc'])).total_seconds()
    assert 600<=meta['elapsed_seconds']<=job_elapsed<=620
    online=set(meta['online_cpus']);siblings=set(meta['target_siblings']);observer=meta['observer_cpu']
    assert 2 in siblings and siblings<=online and observer==min(online-siblings)==0
    labels={'cpu'}|{'cpu'+str(c) for c in siblings|{observer}}
    total={k:[0]*len(samples[0]['counters'][k]) for k in labels};windows={k:[] for k in labels}
    anchors=[];durations=[]
    for i,s in enumerate(samples):
        assert s['index']==i and s['scheduled_offset_seconds']==10*i
        assert set(s['online_cpus'])==online and s['observer_affinity']==[observer]
        assert set(s['counters'])==labels and set(s['reported_frequency_khz'])==set(map(str,siblings))
        assert s['read_seconds']>=0 and s['actual_offset_seconds']>=10*i
        assert set(s['loadavg']) in [{'value'},{'unavailable','errno'}]
        assert set(s['cpu_pressure']) in [{'value'},{'unavailable','errno'}]
        anchors.append(s['monotonic_seconds']-s['actual_offset_seconds'])
        if not i:continue
        previous=samples[i-1];record=intervals[i-1];duration=s['monotonic_seconds']-previous['monotonic_seconds']
        assert duration>0 and utc(s['utc'])>utc(previous['utc']);durations.append(duration)
        assert record['index']==i-1 and record['valid'] is True and record['errors']==[]
        close(record['duration_seconds'],duration);assert set(record['cpu'])==labels
        for label in labels:
            current=s['counters'][label];before=previous['counters'][label]
            assert len(current)==len(before)>=8
            diff=[v-u for u,v in zip(before,current)];assert min(diff)>=0
            tick=sum(diff[:8]);busy=sum(diff[j] for j in [0,1,2,5,6]);assert tick>0
            expected={'raw_delta':diff,'total_ticks':tick,'idle_ticks':diff[3],'iowait_ticks':diff[4],'steal_ticks':diff[7],'nonidle_excluding_iowait_steal_ticks':busy}
            assert record['cpu'][label]==expected,(host,i,label)
            total[label]=[a+b for a,b in zip(total[label],diff)];windows[label].append(100*busy/tick)
    assert max(anchors)-min(anchors)<1e-8
    close(sum(durations),samples[-1]['monotonic_seconds']-samples[0]['monotonic_seconds'])
    assert sum(durations)<=meta['elapsed_seconds']
    cpu={}
    for label,delta in total.items():
        ticks=sum(delta[:8]);busy=sum(delta[j] for j in [0,1,2,5,6])
        r={'nonidle_excluding_iowait_steal_pct':100*busy/ticks,'iowait_pct':100*delta[4]/ticks,'steal_pct':100*delta[7]/ticks,'max_window_nonidle_pct':max(windows[label]),'total_ticks':ticks}
        for key,value in r.items():close(value,reported['cpu'][label][key])
        cpu[label]=dict(r,raw_delta=delta,guest_excluded_from_total_ticks=sum(delta[8:]))
    freq={str(c):sum('value' in s['reported_frequency_khz'][str(c)] for s in samples) for c in siblings}
    assert freq==reported['frequency_available_samples']
    late=max(s['actual_offset_seconds']-s['scheduled_offset_seconds'] for s in samples)
    close(late,reported['maximum_schedule_lateness_seconds'])
    for key in ['started_utc','finished_utc','elapsed_seconds','observer_cpu','target_siblings']:assert meta[key]==reported[key]
    assert reported['samples']==61 and reported['intervals']==reported['valid_intervals']==60
    table=f"| {host.upper()} | 60/60 | {cpu['cpu2']['nonidle_excluding_iowait_steal_pct']:.4f}% | {cpu['cpu2']['max_window_nonidle_pct']:.4f}% | {cpu['cpu2']['steal_pct']:.4f}% | 0 |"
    assert table in readme
    hosts[host]={'samples':61,'valid_intervals':60,'observer_cpu':observer,'siblings':sorted(siblings),'job_elapsed_seconds':job_elapsed,'duration_min_seconds':min(durations),'duration_max_seconds':max(durations),'sum_interval_seconds':sum(durations),'maximum_schedule_lateness_seconds':late,'maximum_read_seconds':max(s['read_seconds'] for s in samples),'frequency_available_samples':freq,'cpu':cpu,'table_row':table}
for name,sha in published['files'].items():assert INPUTS[ROOT+name]==sha
result={'status':'pass','immutable_revision':REV,'samples_audited':183,'intervals_audited':180,'hosts':hosts,'input_sha256':INPUTS,'method':'Independent git-object read, raw endpoint subtraction and summary reconstruction; no producer audit code imported or executed. Observer code previously statically reviewed; read/hash only here.','limits':['Current 600-second idle-window observations only; no historical A/A explanation or qualification change.','No sampled process inventory; low CPU totals alone cannot prove workload absence. Root lease/idle checks are separate evidence.','Reported frequency and governor are metadata, not effective clock/throttle measurement.','Guest fields excluded from totals to avoid double-counting user/nice; all raw fields retained.','No benchmark, candidate, retry, runner access or source adoption.']}
Path(__file__).with_name('audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k in ['status','samples_audited','intervals_audited']}))
