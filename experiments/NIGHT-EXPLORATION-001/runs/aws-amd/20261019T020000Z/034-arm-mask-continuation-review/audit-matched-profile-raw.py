#!/usr/bin/env python3
"""Independent local reconstruction for ARM029. Never runs a producer or workload."""
import argparse,collections,csv,datetime,decimal,hashlib,json,pathlib,re,sys
D=decimal.Decimal
EVENTS={'cycles:u','instructions:u','branches:u','branch-misses:u'}
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load(path):return json.loads(path.read_text())
def stamp(value):return datetime.datetime.fromisoformat(value)
def symbol(label):return re.sub(r'\+0x[0-9a-f]+(?: \(inlined\))?$','',label).replace(' (inlined)','')
def parse_samples(path):
    rows=[]
    for block in re.split(r'\n\s*\n',path.read_text().strip()):
        if not block.strip():continue
        lines=block.splitlines();assert re.fullmatch(r'\s*[0-9]+\s*',lines[0])
        frames=[]
        for line in lines[1:]:
            match=re.fullmatch(r'\s*([0-9a-f]+)\s+(.+)',line);assert match,(path.name,line)
            frames.append((match[1],match[2]))
        assert frames
        same=[name for ip,name in frames if ip==frames[0][0]]
        physical=next((name for name in reversed(same) if '(inlined)' not in name),'[unknown]')
        rows.append({'period':int(lines[0]),'exclusive':symbol(same[0]),'physical':symbol(physical),'physical_label':physical,'frames':len(frames)})
    return rows

def parse_report(path,rows):
    text=path.read_text();lost=re.search(r'Total Lost Samples:\s*(\d+)',text);total=re.search(r'Event count \(approx\.\):\s*(\d+)',text);label=re.search(r'# Samples:\s*(\S+)\s+of event',text)
    assert lost and total and label
    assert int(total[1])==sum(x['period'] for x in rows)
    if label[1].isdigit():assert int(label[1])==len(rows)
    return {'lost':int(lost[1]),'raw_events':len(rows),'raw_period':int(total[1]),'report_sample_label':label[1]}

def parse_counters(path,enabled):
    data={}
    for line in path.read_text().splitlines():
        if not line or line.startswith('#'):continue
        fields=next(csv.reader([line]));assert len(fields)>=3 and fields[2] not in data
        event=fields[2];value=fields[0].strip();assert event in EVENTS
        if enabled:
            assert len(fields)>4
            count=D(value);runtime=D(fields[4]);assert count.is_finite() and runtime.is_finite() and runtime==100
            assert count>=0 if event=='branch-misses:u' else count>0
        else:assert value in ['0','<not counted>']
        data[event]=value
    assert set(data)==EVENTS
    return data

def affine_power(mult,add,seed,rounds):
    # Homogeneous 2x2 matrix exponentiation, independent of the volatile C loop.
    mask=(1<<64)-1
    def mul(x,y):return tuple(sum(x[i*2+k]*y[k*2+j] for k in range(2))&mask for i in range(2) for j in range(2))
    acc=(1,0,0,1);base=(mult,add,0,1)
    while rounds:
        if rounds&1:acc=mul(acc,base)
        base=mul(base,base);rounds>>=1
    return (acc[0]*seed+acc[1])&mask

def disassembly(path):
    text=path.read_text();assert 'file format elf64-littleaarch64' in text
    funcs={};current=None
    for line in text.splitlines():
        heading=re.fullmatch(r'([0-9a-f]+) <([^>]+)>:',line)
        if heading:
            assert heading[2] not in funcs
            current={'start':int(heading[1],16),'instructions':{}};funcs[heading[2]]=current;continue
        ins=re.match(r'^\s*([0-9a-f]+):\s*\t([^\t]+)\t(.*)$',line)
        if ins:
            assert current is not None and re.fullmatch(r'[0-9a-f]{8}',ins[2].strip())
            addr=int(ins[1],16);off=addr-current['start'];assert addr%4==0 and off>=0 and off not in current['instructions']
            current['instructions'][off]=ins[2].strip()
        elif re.match(r'^\s*[0-9a-f]+:\s*\t',line):raise AssertionError(('unparsed instruction',line))
    assert funcs and all(v['instructions'] for k,v in funcs.items() if k=='zbtreeIteratorNext')
    return funcs

def audit(root,seal_name):
    out=root/'profile';freeze=load(root/'execution-freeze.json');expected=load(root/'expected.json');contracts=load(root/'commands.json');fixtures=load(root/'fixtures.json');state=load(out/'result.json');seal=load(root/seal_name)
    assert digest(root/'execution-freeze.json')=='ecb0a87e282c93305fe77435ea264b9646bff79a3578623f763e81b0533cf1fe'
    assert len(freeze['files'])==23 and len(contracts)==104 and len(fixtures)==6
    for name,value in freeze['files'].items():assert digest(root/name)==value,name
    for name,value in seal.items():assert digest(root/name)==value,name
    publication=load(out/'PUBLICATION.json')
    for name,value in publication.items():assert digest(out/name)==value['public_sha256'],name
    assert state['execution_freeze_sha256']==digest(root/'execution-freeze.json')
    assert state['status']=='complete' and state['cpu']==2 and len(state['commands'])==104 and 0<state['elapsed_seconds']<=600
    assert state['protected_before']==state['protected_after']==expected['protected_binaries']
    for before,after in [('actual_sources_before','actual_sources_after'),('sources_before','sources_after'),('binaries_before','binaries_after')]:assert state[before]==state[after]
    for variant in ['control','A']:
        source=dict(expected['source_hashes'])
        if variant=='A':source['src/zset_btree.c']=expected['candidate_source_sha256']
        assert state['actual_sources_before'][variant]==source
        source.update({'bench/profile-scoped-fifo2.c':expected['scope_sha256'],'bench/known-control.c':digest(root/'known-control.c')})
        assert state['sources_before'][variant]==source
    assert set(state['binaries_before'])=={'control','A'}
    for variant,files in state['binaries_before'].items():
        names={'original','profile','original-san','profile-san','original-check/btree-test'}|({'known-control'} if variant=='control' else set())
        assert set(files)==names and all(re.fullmatch('[0-9a-f]{64}',v) for v in files.values())
    start=stamp(state['started_utc']);end=stamp(state['finished_utc']);deadline=stamp('2026-10-19T10:15:00+00:00');assert 0<(end-start).total_seconds()<=600 and end<=deadline and (deadline-start).total_seconds()>=600
    prev=start;semantic={};counters={};warnings=[];checked_rows=0
    known={'rounds':100000000,'before':format(affine_power(6364136223846793005,1442695040888963407,1,100000000),'016x'),'inside':format(affine_power(2862933555777941757,3037000493,3,100000000),'016x'),'after':format(affine_power(6364136223846793005,1442695040888963407,7,100000000),'016x')}
    assert known==load(root/'known-control-expectations.json')['expected_stdout']
    for record,contract in zip(state['commands'],contracts):
        assert all(record[k]==v for k,v in contract.items()) and record['returncode']==0 and record.get('checked')
        t0=stamp(record['started_utc']);t1=stamp(record['finished_utc']);assert prev<=t0<=t1<=end and (t1-t0).total_seconds()<=120;prev=t1
        stdout=(out/(record['name']+'.stdout')).read_text();stderr=(out/(record['name']+'.stderr')).read_text()
        if stderr.strip():warnings.append({'command':record['name'],'stderr':stderr})
        kind=record['kind']
        if kind=='compiler':assert 'clang version 18.1.3' in stdout and 'aarch64' in stdout
        if kind=='original43':assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',stdout)
        if kind.startswith('tree'):
            rows=list(csv.DictReader(stdout.splitlines()));assert len(rows)==1;row=rows[0];fixture=record['fixture'];n=fixture['size'];traversals=(fixture['requested_ops']+n-1)//n
            model=dict(fixture,operations=traversals*n,traversals=traversals,checksum=traversals*n*(n-1)//2,warmup_passes=1,cpu_start=2,cpu_end=2)
            for key,value in model.items():assert row[key]==str(value),(record['name'],key)
            assert int(row['tree_bytes'])>0 and int(row['elapsed_ns'])>0
            key=(n,fixture['seed'],fixture['requested_ops']);signature={k:row[k] for k in ['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']}
            assert semantic.setdefault(key,signature)==signature;checked_rows+=1
            if 'row' in record:assert record['row']==row
            if kind in ['tree-stat','tree-disabled-stat']:
                name=record['name'][:-5] if kind=='tree-stat' else record['variant']+'-disabled';values=parse_counters(out/(name+'.stat'),kind=='tree-stat')
                if 'counters' in record:assert record['counters']==values
                if kind=='tree-stat':counters[(record['variant'],n,fixture['seed'])]=values
        if kind in ['known','known-stat']:assert json.loads(stdout)==known
        if kind=='known-stat':parse_counters(out/(record['name'][:-5]+'.stat'),record['name']=='known-enabled-stat')
    known_samples=parse_samples(out/'known-samples.stdout');known_report=parse_report(out/'known-report.stdout',known_samples);ke=[r for r in known_samples if r['physical']=='known_work'];outside=[r for r in known_samples if r['physical']=='outside_work'];known_period=sum(r['period'] for r in ke);total_period=known_report['raw_period'];assert total_period>0
    threshold=load(root/'known-control-expectations.json');assert len(ke)>=threshold['known_work_min_events'] and D(100)*known_period/total_period>D(threshold['known_work_min_period_pct_exclusive']) and len(outside)==threshold['outside_work_required_events']
    captures=[];all_samples={};sample_totals=collections.Counter();loss=0
    for fixture in fixtures:
        for variant in ['control','A']:
            label=f'{variant}-iterate-n{fixture["size"]}-s{fixture["seed"]}';samples=parse_samples(out/(label+'-samples.stdout'));report=parse_report(out/(label+'-report.stdout'),samples);assert report['raw_events']>0 and report['raw_period']>0
            ep=collections.Counter();ee=collections.Counter()
            for row in samples:ep[row['exclusive']]+=row['period'];ee[row['exclusive']]+=1
            assert sum(ep.values())==report['raw_period'];loss+=report['lost'];all_samples[(variant,fixture['size'],fixture['seed'])]=samples
            captures.append(dict(variant=variant,fixture=fixture,**report,exclusive_period=dict(ep),exclusive_events=dict(ee)))
            sample_totals[variant]+=report['raw_events']
    assert len(counters)==12
    pairs=[]
    for fixture in fixtures:
        base=counters[('control',fixture['size'],fixture['seed'])];candidate=counters[('A',fixture['size'],fixture['seed'])];visits=((fixture['requested_ops']+fixture['size']-1)//fixture['size'])*fixture['size']
        pairs.append({'fixture':fixture,'control':base,'candidate':candidate,'actual_visits':visits,'instructions_direction_pass':D(candidate['instructions:u'])<D(base['instructions:u'])})
    maps={};map_reports={}
    for variant in ['control','A']:
        assembly={k:disassembly(out/f'{variant}-{k}-full-asm.stdout') for k in ['original','profile','timing']};groups={};unknown=collections.Counter()
        for fixture in fixtures:
            group=groups.setdefault('iterate/'+str(fixture['size']),collections.Counter())
            for row in all_samples[(variant,fixture['size'],fixture['seed'])]:
                period=row['period'];group['events']+=1;group['total_period']+=period;match=re.fullmatch(r'(.+?)\+0x([0-9a-f]+)',row['physical_label']);category='missing';tree=False
                if match:
                    function,offset=match[1],int(match[2],16);tree=function.startswith('zbt');words=[a.get(function,{}).get('instructions',{}).get(offset) for a in assembly.values()]
                    if all(words):category='mapped_equal' if len(set(words))==1 else 'mapped_different'
                else:unknown[row['physical']]+=1
                group[category+'_events']+=1;group[category+'_period']+=period
                if tree:
                    label={'mapped_equal':'tree_equal','mapped_different':'tree_different','missing':'tree_missing'}[category];group[label+'_events']+=1;group[label+'_period']+=period
        fullbody={}
        for function in ['zbtreeIteratorNext']:
            assert all(function in a and a[function]['instructions'] for a in assembly.values());offsets=set.union(*(set(a[function]['instructions']) for a in assembly.values()));differences=[]
            for offset in sorted(offsets):
                words=[a[function]['instructions'].get(offset) for a in assembly.values()]
                if not all(words) or len(set(words))!=1:differences.append(hex(offset))
            fullbody[function]={'offset_entries':len(offsets),'different_entries':len(differences),'different_offsets':differences}
        gate=all(g['tree_equal_events']>0 and not g['tree_different_events'] and not g['tree_missing_events'] for g in groups.values());maps[variant]=gate
        produced=load(out/(variant+'-code-map.json'));assert produced['variant']==variant and produced['actual_timing_binary_sha256']==expected['timing_binaries'][variant]['sha256'] and produced['all_sampled_tree_bytes_match_actual']==gate
        for name,h in produced['raw_assembly_sha256'].items():assert digest(out/(variant+'-'+name+'-full-asm.stdout'))==h
        for key,group in groups.items():
            for name,value in group.items():assert produced['groups'][key][name]==value,(variant,key,name)
        for name,body in fullbody.items():
            other=produced['full_tree_body_comparison'][name];assert other['offset_entries']==body['offset_entries'] and other['different_entries']==body['different_entries']
            assert [x['offset'] for x in other['differences']]==body['different_offsets']
        map_reports[variant]={'groups':{k:dict(v) for k,v in groups.items()},'fullbody':fullbody,'unknown_physical_events':dict(unknown),'sampled_tree_match':gate}
    produced=load(out/'audit.json');assert produced['status']=='pass' and produced['commands']==104 and produced['captures']==captures and produced['all_nonempty_stderr']==warnings and produced['total_lost_events']==loss
    assert produced['known_control']['lost']==known_report['lost'] and produced['known_control']['known_events']==len(ke) and produced['known_control']['outside_events']==len(outside)
    for pair,other in zip(pairs,produced['counter_pairs']):
        assert pair['fixture']==other['fixture'] and pair['instructions_direction_pass']==other['instructions_direction_pass']
        for event in EVENTS:
            metric=other['metrics'][event];assert D(metric['control_count'])==D(pair['control'][event]) and D(metric['candidate_count'])==D(pair['candidate'][event])
            assert D(metric['difference_count'])==D(pair['candidate'][event])-D(pair['control'][event])
            assert D(metric['control_per_visit'])==D(pair['control'][event])/pair['actual_visits'] and D(metric['candidate_per_visit'])==D(pair['candidate'][event])/pair['actual_visits']
    direction=all(x['instructions_direction_pass'] for x in pairs);assert produced['all_six_instruction_direction_pass']==direction
    for key in ['semantic_parity_pass','known_arithmetic_and_scope_pass','counter_runtime_and_positivity_pass','disabled_zero_pass']:assert produced[key] is True
    assert len(state['raw_data_sha256'])==13 and produced['raw_data_sha256']==state['raw_data_sha256'];checked_raw=[];unavailable_raw=[]
    for name,value in state['raw_data_sha256'].items():
        if (out/name).exists():assert digest(out/name)==value;checked_raw.append(name)
        else:unavailable_raw.append(name)
    warning_list=[w for w in warnings if re.search(r'\b(lost|dropped|overflow|overrun)\b',w['stderr'],re.I)]
    gates={'integrity_complete':True,'all_104_commands':True,'semantic_parity':True,'known_arithmetic_and_scope':True,'positive_fully_running_counters':True,'both_disabled_zero':True,'zero_known_loss':known_report['lost']==0,'zero_scientific_loss':loss==0,'no_unresolved_loss_warning':not warning_list,'all_six_instruction_direction':direction}
    for variant in ['control','A']:gates[variant+'_own_timing_binary_identity']=True;gates[variant+'_all_sampled_tree_bytes_match_actual']=maps[variant]
    valid=load(out/'profile-validity.json');assert valid['gates']==gates and valid['failed_gates']==[k for k,v in gates.items() if not v] and valid['unresolved_loss_warnings']==warning_list
    assert valid['execution_freeze_sha256']==digest(root/'execution-freeze.json')
    for name,h in valid['input_sha256'].items():assert digest(out/name)==h
    verdict='VALIDATED_MECHANISM_SUPPORT_NOT_ACCEPTANCE' if all(gates.values()) else 'PARK_PROFILE_VALIDITY_GATES';assert valid['status']==verdict and valid['source_selection']=='NONE'
    return {'integrity':'PASS','profile_validity':verdict,'gate_pass':all(gates.values()),'gates':gates,'commands':104,'semantic_rows':checked_rows,'captures':12,'counter_pairs':pairs,'known':dict(known_report,known_events=len(ke),outside_events=len(outside),known_period=known_period),'sample_totals':dict(sample_totals),'mapping':map_reports,'seal_entries':len(seal),'public_artifacts':len(publication),'raw_perf_rehashed':checked_raw,'raw_perf_unavailable_hashes_only':unavailable_raw,'input_seal_sha256':digest(root/seal_name),'execution_freeze_sha256':digest(root/'execution-freeze.json'),'source_selection':'NONE','runner_access':False,'limits':['Operator identity records joined, not a live binary inspection','Unavailable raw perf files are hash provenance only; public perf-script/report artifacts independently parsed','Exclusive samples and same-function offsets do not prove whole-callchain or elapsed-time causality','Unknown/caller/body differences remain; no post hoc threshold or row removal','Profile support does not repair guard noise or authorize acceptance']}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('root',type=pathlib.Path);parser.add_argument('--seal',required=True);parser.add_argument('--out',required=True,type=pathlib.Path);args=parser.parse_args()
    try:result=audit(args.root,args.seal);rc=0 if result['gate_pass'] else 2
    except Exception as error:result={'integrity':'FAIL_OR_INCOMPLETE','error':type(error).__name__+': '+str(error),'source_selection':'NONE','runner_access':False};rc=1
    args.out.write_text(json.dumps(result,indent=2)+'\n');return rc
if __name__=='__main__':sys.exit(main())
