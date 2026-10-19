#!/usr/bin/env python3
"""Independent offline clock audit. Reads public raw EXP009 rows; no subprocess."""
from pathlib import Path
from fractions import Fraction
from statistics import median
from collections import Counter
from datetime import datetime, timezone
import csv, hashlib, io, json, math, re

W=Path(__file__).resolve().parents[3]
E=W/'experiments/EXP-009'
D=Path(__file__).resolve().parents[1]
ROOT=W.parents[1]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
inputs={}
def pin(p):
    p=Path(p);inputs[str(p.relative_to(W))]=sha(p);return p
def ratio(n,d):return float(Fraction(n,d))

summary=load(pin(E/'bench-results/aa/summary.json'))
schedule=load(pin(E/'bench-results/calibrate/aa-schedule.json'))
journal=[json.loads(line) for line in pin(E/'bench-results/aa/commands.jsonl').read_text().splitlines()]
plan=load(pin(E/'PLAN.json'))
assert len(summary['rows'])==len(schedule)==len(journal)==48
rows=[]
for i,(entry,command) in enumerate(zip(schedule,journal)):
    assert entry['index']==i and command['name']==f'{i:03d}'
    assert command['returncode']==0 and command['child_reaped'] and command['owned_group_empty'] and command['release_safe']
    assert command['command'][0]=='build/exp009-baseline/native/lookup'
    raw=pin(E/f'bench-results/aa/raw/{i:03d}.stdout')
    err=pin(E/f'bench-results/aa/raw/{i:03d}.stderr')
    assert sha(raw)==command['raw']['stdout']['sha256']
    assert sha(err)==command['raw']['stderr']['sha256'] and err.stat().st_size==0
    data=list(csv.DictReader(io.StringIO(raw.read_text())))
    assert len(data)==1 and data[0]==summary['rows'][i]['csv']
    x=data[0];wall=int(x['elapsed_ns']);thread=int(x['thread_elapsed_ns'])
    assert wall>0 and thread>0 and int(x['operations'])==entry['operations']
    assert x['size']==str(entry['size']) and x['seed']==str(entry['seed'])
    assert x['case']=='lookup-hit' and x['member_bytes']=='16' and x['warmup_passes']=='1'
    residual=wall-thread
    rows.append(dict(index=i,block=entry['block'],size=entry['size'],seed=entry['seed'],position=entry['position'],side=entry['side'],
        operations=int(x['operations']),checksum=x['checksum'],tree_bytes=int(x['tree_bytes']),wall_ns=wall,thread_ns=thread,
        wall_minus_thread_ns=residual,residual_percent_wall=ratio(100*residual,wall),wall_over_thread_percent=ratio(100*residual,thread),
        warmup_elapsed_ns=int(x['warmup_elapsed_ns']),cpu_start=int(x['cpu_start']),cpu_end=int(x['cpu_end']),
        endpoints_differ=x['cpu_start']!=x['cpu_end'],qos_reported_start=x['qos_reported_start'],qos_reported_end=x['qos_reported_end'],qos_effective=x['qos_effective']))
blocks=[]
for i in range(0,48,4):
    q=rows[i:i+4];assert ''.join(x['side'] for x in q)=='ABBA'
    assert len({(x['size'],x['seed'],x['operations'],x['checksum'],x['tree_bytes']) for x in q})==1
    WA=q[0]['wall_ns']+q[3]['wall_ns'];WB=q[1]['wall_ns']+q[2]['wall_ns']
    TA=q[0]['thread_ns']+q[3]['thread_ns'];TB=q[1]['thread_ns']+q[2]['thread_ns']
    RA=WA-TA;RB=WB-TB;dw=WB-WA;dt=TB-TA;dr=RB-RA
    assert dw==dt+dr
    wall_ok=abs(dw)*100<=WA and min(x['wall_ns'] for x in q)>=plan['minimum_elapsed_ns']
    thread_ok=abs(dt)*100<=TA and min(x['thread_ns'] for x in q)>=plan['minimum_elapsed_ns']
    assert wall_ok==summary['blocks'][i//4]['qualified']
    # Signed-side nuisance contribution needed to move the recorded thread ratio to its nearest ±1% boundary.
    margin=Fraction(0)
    if TB*100>TA*101:margin=Fraction(TB*100-TA*101,100)
    elif TB*100<TA*99:margin=Fraction(TA*99-TB*100,100)
    blocks.append(dict(block=q[0]['block'],size=q[0]['size'],seed=q[0]['seed'],wall_A_ns_sum=WA,wall_B_ns_sum=WB,
        thread_A_ns_sum=TA,thread_B_ns_sum=TB,residual_A_ns_sum=RA,residual_B_ns_sum=RB,
        wall_delta_ns=dw,thread_delta_ns=dt,residual_delta_ns=dr,exact_delta_identity=True,
        wall_effect_percent=ratio(100*dw,WA),thread_effect_percent_diagnostic_only=ratio(100*dt,TA),
        thread_delta_percent_wall_denominator=ratio(100*dt,WA),residual_delta_percentage_points_wall=ratio(100*dr,WA),
        wall_qualified=wall_ok,thread_diagnostic_within_original_threshold=thread_ok,
        thread_margin_beyond_1percent_ns=str(margin),thread_margin_beyond_1percent_ms=float(margin/1000000),
        residual_contrast_fraction_of_wall_delta=ratio(dr,dw) if dw else None))
assert len(blocks)==12
failure=[b for b in blocks if not b['wall_qualified']]
assert len(failure)==3 and all(b['size']==1000000 for b in failure)

source=pin(E/'harness/lookup.c').read_text()
order=['int cpu_start = cpu_id();','int64_t thread_start = thread_ns();','uint64_t start = now_ns();','uint64_t elapsed = now_ns() - start;','int64_t thread_end = thread_ns();','int cpu_end = cpu_id();']
positions=[source.index(x) for x in order];assert positions==sorted(positions)
build=load(pin(E/'bench-results/build/build-manifest.json'))
assert '-fno-lto' in build['native_flags'] and '-O3' in build['native_flags']
metadata=build['metadata']['native']['assembly'];asm_path=pin(E/'bench-results/build/raw'/Path(metadata).name)
assert sha(asm_path)==build['files_sha256'][metadata]
text=asm_path.read_text();main=text.split('_main:\n')[1].split('\n_')[0];ins=[]
for line in main.splitlines():
    m=re.match(r'^([0-9a-fA-F]{16})\s+(.+)$',line)
    if m:ins.append((int(m[1],16),m[2]))
start=ins[0][0]
calls=[]
for i,(a,x) in enumerate(ins):
    if 'symbol stub for: _clock_gettime' in x:
        prior=ins[i-1][1]
        calls.append(dict(main_offset=hex(a-start),prior_instruction=prior,window=[dict(offset=hex(aa-start),instruction=xx) for aa,xx in ins[max(0,i-3):i+4]]))
assert [c['prior_instruction'] for c in calls][-4:]==['mov\tw0, #0x10','mov\tw0, #0x6','mov\tw0, #0x6','mov\tw0, #0x10']

consults=[]
for who,base in [('own',ROOT/'scratch/cpu-perf-m6-metrology-C-20261019'),('shared-root',ROOT/'scratch/cpu-perf-m6-metrology-20261019')]:
    for f in [base/'discover-calls.jsonl',base/'consult-calls.jsonl',base/'bracket-calls.jsonl']:
        if not f.exists():continue
        for line in f.read_text().splitlines():
            x=json.loads(line);response=x['response'];params=x['params']
            consults.append(dict(ownership=who,record_file=str(f.relative_to(ROOT)),record_file_sha256=sha(f),method=x['method'],tool=params.get('name'),
                started_utc=x['started_utc'],finished_utc=x['finished_utc'],params=params,arguments=params.get('arguments'),
                response_sha256=hashlib.sha256(json.dumps(response,sort_keys=True).encode()).hexdigest(),is_error=response.get('result',{}).get('isError',False)))
res=[x['wall_minus_thread_ns'] for x in rows]
result=dict(status='COMPLETE_OFFLINE_DIAGNOSTIC',participant='/root/followup_proposal_c',backend='Codex/GPT-6 family; exact serving model, tokens and currency unknown',
    source_selection='NONE',exp009_decision='PARK unchanged',candidate_population=False,created_utc=datetime.now(timezone.utc).isoformat(),
    hypothesis='Recorded wall/thread evidence is sufficient to explain all three failed1M wall contrasts solely by descheduling.',
    operational_result='NOT SUPPORTED: all three failed wall blocks also fail the diagnostic thread ±1% contrast.',
    physical_causal_result='UNDERDETERMINED: boundary CPU work/clock error lack independent bounds; a failed measured-thread contrast alone does not strictly falsify every physical descheduling-only model.',
    rows=rows,blocks=blocks,failed_wall_blocks=failure,wall_qualified_blocks={str(n):sum(x['wall_qualified'] for x in blocks if x['size']==n) for n in [100000,1000000]},
    thread_diagnostic_qualified_blocks={str(n):sum(x['thread_diagnostic_within_original_threshold'] for x in blocks if x['size']==n) for n in [100000,1000000]},
    residual_summary=dict(min_ns=min(res),median_ns=median(res),max_ns=max(res),all_nonnegative=all(x>=0 for x in res),
        max_abs_failed_residual_contrast_percentage_points=max(abs(x['residual_delta_percentage_points_wall']) for x in failure),
        all_wall_ns_multiple1000=all(x['wall_ns']%1000==0 for x in rows),note='Observed granularity and residuals are not calibrated resolution/error bounds or exact off-CPU durations.'),
    endpoints=dict(differ_rows=sum(x['endpoints_differ'] for x in rows),equal_rows=sum(not x['endpoints_differ'] for x in rows),cpu_values=sorted({x[k] for x in rows for k in ['cpu_start','cpu_end']}),
        effective_qos_values=sorted({x['qos_effective'] for x in rows}),limits='Endpoints outside/broader than wall interval. Equality does not exclude migration; inequality supplies no residency/core-class/frequency/time share.'),
    instrumentation=dict(source_call_order=order,native_main_clock_calls=calls,actual_clock_argument_order_last4=['thread0x10','wall0x6','wall0x6','thread0x10'],
        accounting_equation='For ideal clocks: W=C+S; T=C+B; W-T=S-B. B is extra on-CPU work in the outer thread-clock bracket. Recorded values add unmeasured clock error. Thus W-T is not S.',
        error_bound='No same-scope bracketing overhead, actual clock resolution/error budget or scheduler trace was captured. No numerical upper bound on B or clock error is inferred from residuals alone.',
        profile_warning='Only native AA binary clocks used. Profile binary includes sample_start/stop and symbolization in the outer thread bracket; do not pool its W-T with native rows.'),
    mcp=dict(direct_tool_catalog_matches=0,transport='Own copied local stdio client, uvx --offline cpu-perf serve, auto-index/update disabled, separate ignored data directory; server reaped after calls.',
        server_version='0.1.1',bundled_revision='deb5a0bac467',initial_library='0/287 sources;0passages;keyword only',
        limitations='Initial own ask did not recognise pasted output and returned no source passages; explicit read_source retrieved Linux manual text. Bracket follow-up retrieved a Coz passage irrelevant to this clock bound; no source passage establishes the proposed algebra or Darwin accounting accuracy. Later library reported2/287sources84passages. check_evidence heuristically returned drop_number, partly misreading compact metadata and correctly flagging unknown frequency/microarchitecture. Preserve forensic raw numbers with explicit limits; no portable gain claim. Shared root LLVM text supplies OS-specific benchmarking caution, not Apple-specific measurements.',
        calls=consults),
    initial_readme_scope_correction='A failed measured-thread contrast does not unconditionally falsify the physical descheduling-only explanation because outer bracket CPU work and clock error have no numerical bound. It rejects only the operational assertion that recorded W-T differences alone suffice.',
    conditional_next_design=dict(origin='Root suggested; independently assessed by C. Preparation/design only; no native work selected or queued.',
        order='w0,t0,w1 / unchanged body / w2,t1,w3; CPU/QoS observations outside w0..w3',
        definitions='I=w2-w1; T=t1-t0; M=(w1-w0)+(w3-w2)',
        ideal_bounds='Assuming monotonic accurate wall reads, reliable CPU accounting and sample instants within call brackets: boundaryCPU B in[0,M]; innerCPU C in[max(0,T-M),min(T,I)]; offCPU S in[I-T,I-T+M] intersect[0,I].',
        block_rule='Sum each row lower/upper innerCPU bounds by ABBA side. Positive-denominator ratio interval is [C_B_lower/C_A_upper-1,C_B_upper/C_A_lower-1]. A wholly outside +/-1% interval conditionally excludes descheduling-only stable-work explanation; overlap is inconclusive, never proof. Apply separately to every block with all rows retained.',
        limits='Read-completion latency is included by outer wall brackets, but timestamp quantization/accuracy and thread accounting lag need explicit conservative error terms. clock_getres is nominal resolution, not an accuracy/lag bound; empty controls do not prove a worst-case workload bound. Boundary preemption widens M and makes a result inconclusive; never discard it.',
        feasibility='Concrete narrower instrumentation-validity diagnostic, materially different from repeating EXP009 counts/warmups. Requires separately published harness, actual codegen ordering checks, controlled empty/workload fixtures, predeclared uncertainty/inconclusive gates and independent review before any native authorization. Cannot qualify future candidate/101guards merely by passing a two-primary pilot.',
        prior_methods='012 already reported descriptive endpoints/wall-thread inflation;017 resident-worker method choseNONE for lifecycle/guard-transfer/budget gaps; EXP009 already used600ms target and stillfailed. No resident/longer-count retry or causal repetition is proposed.'),
    method_limits='Independent raw reconstruction, no driver calculation import. No benchmark/profile/build/source change or Git mutation. Other new reviewer reports not read. No wall-gate replacement, exclusion, retry, DVFS/cache/core attribution or optimization count.',
    inputs_sha256=inputs,analysis_script_sha256=sha(__file__))
out=D/'reviews/C.json'
with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(dict(status=result['status'],wall=result['wall_qualified_blocks'],thread=result['thread_diagnostic_qualified_blocks'],
    residual=result['residual_summary'],endpoints=result['endpoints'],failed=[{k:x[k] for k in ['block','wall_effect_percent','thread_effect_percent_diagnostic_only','residual_delta_ns','residual_delta_percentage_points_wall','thread_margin_beyond_1percent_ms']} for x in failure]),indent=2))
