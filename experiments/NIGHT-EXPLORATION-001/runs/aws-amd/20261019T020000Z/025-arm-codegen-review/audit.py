#!/usr/bin/env python3
"""Independent instruction/dataflow inventory; never executes ARM binaries."""
import argparse,collections,hashlib,json,pathlib,re
p=argparse.ArgumentParser();p.add_argument('validation_campaign',type=pathlib.Path);p.add_argument('diagnosis',type=pathlib.Path);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args();d=a.validation_campaign
read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
f=read(d/'comparison-freeze.json');vf=read(d/'validation/freeze.json');vr=read(d/'validation/result.json');vm=read(d/'validation-evidence-sha256.json');claimed=read(a.diagnosis/'analysis.json')
regions={'A':[(0x10498,0x1052c),(0x106bc,0x10750)],'B':[(0x1049c,0x10530),(0x1059c,0x10630)],'C':[(0x10498,0x10530),(0x106a4,0x1073c)]}
starts={'base':0x105f4,'A':0x106bc,'B':0x1059c,'C':0x106a4};summaries={}
for v in ['base','A','B','C']:
    artifact=d/'validation'/(v+'-native-codegen.stdout');s=artifact.read_text();h=sha(artifact)
    assert h==vm[str(artifact.relative_to(d))]==claimed['variants'][v]['sha256']
    parsed=[(int(addr,16),opcode,text.strip()) for addr,opcode,text in re.findall(r'^\s*([0-9a-f]+):\s+([0-9a-f]{8})\s+(.*)$',s,re.M)];ins={addr:(op,txt) for addr,op,txt in parsed}
    assert len(ins)==len(parsed) and all(b[0]==a[0]+4 for a,b in zip(parsed,parsed[1:]))
    commands=[c for c in vr['commands'] if c['name']==v+'-native-codegen'];assert len(commands)==1 and commands[0]['returncode']==0
    assert commands[0]['command']==['objdump','-dSl','--disassemble=zbtIndexScanSlot','build/btree-bench']
    assert commands[0]['cwd']=='scratch/arm-corrected-neon/'+v
    if v!='base':assert vf['snapshots'][v]['timing_binary_sha256']==f['sources'][v]['binary_sha256']
    else:
        assert vf['baseline_binary']==vr['aa_binary_before']==vr['aa_binary_after']==f['sources']['base']['binary_sha256']
        assert vf['snapshots']['base']['text_sha256'] in f['same_text_groups'] and f['same_text_groups'][vf['snapshots']['base']['text_sha256']]==['base']
    stack=96+int(re.search(r'sub\s+sp, sp, #0x([0-9a-f]+)',s)[1],16)
    predicates=[]
    for lo,hi in regions.get(v,[]):
        selected=[]
        for addr,opcode,text in parsed:
            if lo<=addr<hi:
                mnemonic=text.split()[0]
                if mnemonic in ['strb','ldrh','ubfx','lsr','fmov'] or (mnemonic=='and' and re.match(r'and\s+w',text)) or (mnemonic=='mov' and re.match(r'mov\s+v\d+\.b\[',text)):selected.append((addr,opcode,text))
        counts=collections.Counter(t.split()[0] for _,_,t in selected)
        assert dict(counts)=={'strb':2,'ldrh':1,'and':1,'ubfx':14,'fmov':1,'mov':15,'lsr':1}
        assert len(selected)==35
        lanes=sorted(int(re.search(r'\.b\[(\d+)\]',t)[1]) for _,_,t in selected if t.startswith('mov'))
        assert lanes==list(range(1,16));assert sum(t.startswith('fmov\ts1,') for _,_,t in selected)==1
        assert [dict(address=hex(addr),opcode=op,instruction=t) for addr,op,t in selected]==claimed['variants'][v]['predicate_reconstruction'][len(predicates)]['exact_instructions']
        predicates.append(dict(start=hex(lo),end=hex(hi),count=35,mnemonics=dict(counts),lanes=lanes))
    # Trace the continuing zero-mask branch: cbz taken, cbnz not taken,
    # and final-chunk exit conditions false. No execution or cycle inference.
    start=starts[v];pc=start;path=[]
    while not path or pc!=start:
        assert len(path)<100;op,t=ins[pc];path.append(dict(address=hex(pc),opcode=op,instruction=t));mn=t.split()[0]
        if mn=='b' or mn=='cbz':pc=int(re.search(r'\b([0-9a-f]+) <',t)[1],16)
        elif mn in ['cbnz','b.eq','b.ls','b.cs','b.hi']:pc+=4
        else:
            assert not mn.startswith('b.') and mn not in ['tbz','tbnz','ret','bl'];pc+=4
    c=claimed['variants'][v]
    assert path==c['forward_continuing_zero_mask_path']['exact_instructions']
    assert len(parsed)==c['static_instructions'] and len(parsed)*4==c['static_bytes'] and stack==c['stack_frame_bytes']
    assert ('cnt' in [i['instruction'].split()[0] for i in path])==(v in ['A','C'])
    summaries[v]=dict(artifact_sha256=h,instruction_count=len(parsed),bytes=len(parsed)*4,stack_frame_bytes=stack,predicates=predicates,continuing_zero_mask_instructions=len(path),chunk_bytes=8 if v=='base' else 16,trace=path)
result=dict(status='pass',diagnosis_revision='3e085fdcf',scope='Read-only exact existing artifact analysis; no build, source edits, runner access, timing or sampling',variants=summaries,reviewer='AMD agent authored C; independent static analysis, not independent C authorship review',limits='Candidate provenance joins exact timing binary hashes through validation snapshots; baseline text equality is attested by successful immutable validation assertion and matching text pin, raw ELF text not independently rehashed here. Static counts cannot apportion regression or establish dynamic cycles.')
a.out.write_text(json.dumps(result,indent=2)+'\n');print({v:{k:q[k] for k in ['instruction_count','stack_frame_bytes','continuing_zero_mask_instructions']} for v,q in summaries.items()})
