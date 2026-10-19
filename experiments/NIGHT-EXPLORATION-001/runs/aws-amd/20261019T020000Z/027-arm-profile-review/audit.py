#!/usr/bin/env python3
"""Independent post-filter reconstruction; no worker analyzer import or execution."""
import argparse,collections,csv,datetime,hashlib,json,pathlib,re,subprocess
p=argparse.ArgumentParser();p.add_argument('evidence',type=pathlib.Path);p.add_argument('--discovery',type=pathlib.Path,required=True);p.add_argument('--static',type=pathlib.Path,required=True);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args();d=a.evidence
read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=datetime.datetime.fromisoformat
f=read(d/'plan-freeze.json');prior=read(a.discovery/'comparison-freeze.json');static=read(a.static/'analysis.json');result=read(d/'profiles/result.json')
for name,h in f['inputs_sha256'].items():assert sha(d/name)==h
assert sha(a.discovery/'comparison-freeze.json')==f['comparison_freeze_sha256'] and sha(a.static/'analysis.json')==f['static_analysis_sha256']
assert f['timed_main_return_offset']=='0xe04' and f['verify_main_return_offset']=='0xf90' and f['frequency_hz']==997 and f['cpu']==2 and f['budget_seconds']==600
rel='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/019-neon-matched-profile/'
assert subprocess.check_output(['git','show','d8b21e3c6:'+rel+'plan-freeze.json'])==(d/'plan-freeze.json').read_bytes()
pred=set(int(x,16) for x in f['B_predicate_addresses']);assert len(pred)==70
assert pred=={int(i['address'],16) for r in static['variants']['B']['predicate_reconstruction'] for i in r['exact_instructions']}
# Main call sites and callback setup inspected directly from frozen assembly.
for v in ['base','B']:
    s=(d/(v+'-main.asm')).read_text();assert re.search(r'0000000000000f18 <main>:',s)
    for addr in ['1d18','1ea4']:assert re.search(r'^\s*'+addr+r':\s+[0-9a-f]{8}\s+bl\s+[^\n]*<zbtreeScan>',s,re.M)
    assert re.search(r'^\s*1d1c:',s,re.M) and re.search(r'^\s*1ea8:',s,re.M)
expected_identity={v:dict(binary_sha256=prior['sources'][v]['binary_sha256'],source_referee_hashes_verified=len(prior['sources'][v]['source_hashes'])) for v in ['base','B']}
assert result['identity_before']==result['identity_after']==expected_identity and result['status']=='complete' and result['elapsed_seconds']<=600
schedule=[dict(variant=v,size=n,seed=s) for s in [1,2,3] for n in [100000,1000000] for v in (['B','base'] if s==2 else ['base','B'])]
assert schedule==f['capture_schedule'] and len(result['captures'])==12
for want,got in zip(schedule,result['captures']):
    assert all(got[k]==v for k,v in want.items());assert re.fullmatch('[0-9a-f]{64}',got['raw_perf_sha256']) and got['raw_perf_bytes']>0
# Exact command sequence, successful outcomes, serial intervals and enabled/disabled PMU contracts.
commands=result['commands'];assert len(commands)==52
expected_names=[f'{v}-n{n}-s1-disabled' for v in ['base','B'] for n in [100000,1000000]]+[f"{i['variant']}-n{i['size']}-s{i['seed']}-{mode}" for i in schedule for mode in ['plain','sampled','samples','report']]
assert [c['name'] for c in commands]==expected_names
for j,c in enumerate(commands):
    assert c['returncode']==0 and utc(c['started_utc'])<=utc(c['finished_utc'])
    if j:assert utc(commands[j-1]['finished_utc'])<=utc(c['started_utc'])
    cmd=c['command'];name=c['name'];err=(d/'profiles'/(name+'.stderr')).read_text()
    if name.endswith('-disabled'):assert '-D' in cmd and cmd[cmd.index('-D')+1]=='-1' and cmd[1]=='stat' and err.strip()=='Events disabled'
    else:assert not err
    if name.endswith('-sampled'):assert cmd[1:9]==['record','-q','-e','cycles:u','-F997','-g','--call-graph','fp']
    if name.endswith('-samples'):assert cmd[1]=='script' and cmd[-2:]==['-F','ip,sym,symoff,period']
    if name.endswith('-report'):assert cmd[1:5]==['report','--stdio','--no-children','--sort'] and cmd[5]=='symbol'
semantics=['case','size','requested_ops','member_bytes','seed','operations','checksum','tree_bytes','traversals','warmup_passes'];fixtures={};semantic_rows=0
for i in schedule:
    v,n,seed=i['variant'],i['size'],i['seed'];tag=f'{v}-n{n}-s{seed}'
    for mode in ['plain','sampled']+(['disabled'] if seed==1 else []):
        c=next(c for c in commands if c['name']==tag+'-'+mode);args=[str(pathlib.Path(prior['sources'][v]['root'])/prior['sources'][v]['timing_binary']),'--case','scan','--size',str(n),'--ops','5000000','--member-bytes','16','--seed',str(seed)]
        assert c['command'][-len(args):]==args
        rows=list(csv.DictReader((d/'profiles'/(tag+'-'+mode+'.stdout')).read_text().splitlines()));assert len(rows)==1;z=rows[0];semantic_rows+=1
        assert [z['case'],int(z['size']),int(z['requested_ops']),int(z['member_bytes']),int(z['seed'])]==['scan',n,5000000,16,seed]
        assert int(z['cpu_start'])==int(z['cpu_end'])==2 and int(z['operations'])>=5000000
        signature=tuple(z[k] for k in semantics)
        if (n,seed) in fixtures:assert signature==fixtures[n,seed]
        else:fixtures[n,seed]=signature
        if mode=='disabled':
            stat=[line for line in (d/'profiles'/(tag+'-disabled.stat')).read_text().splitlines() if line and not line.startswith('#')];assert len(stat)==1
            parts=stat[0].split(',');assert parts[0] in ['0','<not counted>'] and parts[2]=='cycles:u'
assert semantic_rows==28

def parse_block(block):
    lines=block.splitlines();assert re.fullmatch(r'\s*\d+\s*',lines[0]);period=int(lines[0]);frames=[]
    for line in lines[1:]:
        m=re.fullmatch(r'\s*([0-9a-f]+)\s+(.+)',line);assert m,line
        frames.append((m[1],m[2].strip()))
    assert frames
    top=frames[0][0];labels=[label for addr,label in frames if addr==top]
    mains=[]
    for addr,label in frames:
        m=re.fullmatch(r'main(?:\+0x([0-9a-f]+))?',label)
        if m:mains.append(int(m[1] or '0',16))
    if not mains:scope='incomplete'
    elif len(mains)!=1:scope='ambiguous'
    elif mains[0]==0xe04:scope='timed'
    elif mains[0]==0xf90:scope='verify'
    else:scope='other'
    slots=[]
    for label in labels:
        m=re.fullmatch(r'zbtIndexScanSlot(?:\+0x([0-9a-f]+))?',label)
        if m:slots.append(int(m[1] or '0',16))
    assert len(slots)<=1
    return dict(period=period,scope=scope,top_ip=top,top_labels=labels,slot_offset=slots[0] if slots else None,main_offsets=mains)
# Independent negative controls are synthetic text, never a benchmark run.
controls=[('timed','10\n 100 zbtIndexScanSlot+0x204\n 200 main+0xe04','timed',0x204),('verify','10\n 100 zbtIndexScanSlot+0x204\n 200 main+0xf90','verify',0x204),('missing','10\n 100 zbtIndexScanSlot+0x204','incomplete',0x204),('conflicting','10\n 100 zbtIndexScanSlot+0x204\n 200 main+0xe04\n 300 main+0xf90','ambiguous',0x204),('inlined-only','10\n 100 zbtIndexScanSlot+0x204\n 200 main+0xe04 (inlined)','incomplete',0x204),('other','10\n 100 zbtIndexScanSlot+0x204\n 200 main+0x800','other',0x204),('ancestor-only','10\n 100 memcpy+0x8\n 150 zbtIndexScanSlot+0x204\n 200 main+0xe04','timed',None),('duplicate-main','10\n 100 zbtIndexScanSlot+0x204\n 200 main+0xe04\n 300 main+0xe04','ambiguous',0x204)]
for name,text,scope,offset in controls:
    q=parse_block(text);assert q['scope']==scope and q['slot_offset']==offset,name
classifications=[];captures=[]
for item in schedule:
    v,n,seed=item['variant'],item['size'],item['seed'];tag=f'{v}-n{n}-s{seed}';samples=[parse_block(b) for b in re.split(r'\n\s*\n',(d/'profiles'/(tag+'-samples.stdout')).read_text().strip()) if b.strip()]
    for i,s in enumerate(samples):classifications.append(dict(s,capture=tag,index=i))
    report=(d/'profiles'/(tag+'-report.stdout')).read_text();lost=int(re.search(r'Total Lost Samples:\s*(\d+)',report)[1]);assert lost==0
    # Some report headers abbreviate counts (2K); raw callchains supply exact counts.
    count_label=re.search(r'# Samples:\s*(\S+)\s+of event',report)[1]
    if count_label.isdigit():assert int(count_label)==len(samples)
    else:assert count_label=='2K' and 1000<=len(samples)<3000
    period=sum(s['period'] for s in samples);assert int(re.search(r'Event count \(approx\.\):\s*(\d+)',report)[1])==period
    scopes={k:dict(events=sum(s['scope']==k for s in samples),period=sum(s['period'] for s in samples if s['scope']==k)) for k in ['timed','verify','other','incomplete','ambiguous']}
    assert sum(z['events'] for z in scopes.values())==len(samples) and sum(z['period'] for z in scopes.values())==period
    slot=[s for s in samples if s['slot_offset'] is not None];assigned=[s for s in slot if s['scope'] in ['timed','verify']];timed=[s for s in slot if s['scope']=='timed'];predicate=[s for s in timed if v=='B' and 0x10298+s['slot_offset'] in pred]
    fraction=len(assigned)/len(slot) if slot else 0;den=scopes['timed']['period'];assert den>0
    q=dict(**item,events=len(samples),period=period,scopes=scopes,slot_events=len(slot),slot_assignable_events=len(assigned),timed_slot_events=len(timed),timed_slot_period=sum(s['period'] for s in timed),predicate_events=len(predicate),predicate_period=sum(s['period'] for s in predicate),slot_stack_assignable_fraction=fraction,stack_gate=fraction>=.9,predicate_timed_period_pct=100*sum(s['period'] for s in predicate)/den,slot_timed_period_pct=100*sum(s['period'] for s in timed)/den)
    captures.append(q)
assert classifications==read(d/'analysis/sample-classifications.json')
assert captures==read(d/'analysis/capture-summary.json')
pooled=[]
for v in ['base','B']:
    for n in [100000,1000000]:
        group=[r for r in captures if r['variant']==v and r['size']==n];assert len(group)==3
        den=sum(r['scopes']['timed']['period'] for r in group);pp=sum(r['predicate_period'] for r in group);ev=sum(r['predicate_events'] for r in group)
        gate=all(r['stack_gate'] for r in group);pct=100*pp/den
        pooled.append(dict(variant=v,size=n,timed_events=sum(r['scopes']['timed']['events'] for r in group),timed_period=den,slot_timed_period_pct=100*sum(r['timed_slot_period'] for r in group)/den,predicate_events=ev,predicate_period=pp,predicate_timed_period_pct=pct,all_capture_stack_gate=gate,material_support=v=='B' and gate and pct>=5 and ev>=100 and all(r['predicate_timed_period_pct']>=1 for r in group)))
assert pooled==read(d/'analysis/summary.json')
manifest=read(d/'evidence-sha256.json')
for name,h in manifest.items():assert sha(d/name)==h
out=dict(status='pass',revision='cb708e4ec',commands=52,semantic_executions=28,captures=12,source_identity=expected_identity,manifest_entries=len(manifest),samples=len(classifications),scope_totals={k:dict(events=sum(c['scopes'][k]['events'] for c in captures),period=sum(c['scopes'][k]['period'] for c in captures)) for k in ['timed','verify','other','incomplete','ambiguous']},predicate_addresses=70,lost_samples_reported=0,synthetic_parser_controls=[q[0] for q in controls],capture_summary=captures,pooled=pooled,source_adoption='NONE',limits='Full-process PMU with exact-callsite post-filter only; sampled-period attribution is not causal cycle cost. Raw perf.data runner-local hashes attested but not independently rehashed. Reviewer authored C, prior static review disclosed; no runner access or candidate edits.')
a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['capture_summary','source_identity']}))
