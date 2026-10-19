#!/usr/bin/env python3
"""Offline retained-text/binary review only; never launches a native child."""
from pathlib import Path
import collections, datetime, hashlib, json, re, struct
W = Path(__file__).resolve().parents[3]
E = W / 'experiments/M6-CLOCK-BRACKET-001'
ROOT = W.parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def parse(p):
    out = {}; name = None
    for line in p.read_text().splitlines():
        if re.fullmatch(r'_[A-Za-z0-9_.$]+:', line):
            name = line[:-1]; out[name] = []
        else:
            m = re.match(r'^([0-9a-f]{16})\s+(\S+)\s*(.*)$', line)
            if m and name: out[name].append((int(m[1],16),m[2],m[3]))
    return out
oldp = E/'review/codegen/old-lookup.asm'; newp = E/'results/build/raw/lookup-assembly.stdout'
controlp = E/'results/build/raw/controls-assembly.stdout'
old, new, controls = map(parse, (oldp,newp,controlp))
def norm(row, allfunc, rows, i):
    address, op, arg = row
    if ' ; symbol stub for: ' in arg:
        return (op,re.sub(r'0x[0-9a-f]+','STUB',arg)), 'external stub address with identical symbol'
    if op == 'add' and ' ; literal pool for: ' in arg:
        return (op,re.sub(r'#[0-9a-fx]+','LITERAL_RELOCATION',arg)), 'literal low-address with identical annotated string'
    if op == 'adrp' and ' ; ' in arg:
        reg = arg.split(',')[0]
        if i+1 < len(rows):
            nxt = rows[i+1]
            if nxt[1]=='add' and nxt[2].startswith(reg+', '+reg+', #') and ' ; literal pool for: ' in nxt[2]:
                return (op,reg+', LITERAL '+nxt[2].split(' ; literal pool for: ')[1]), 'adjacent ADRP+ADD identical annotated literal'
        return (op,reg+', EFFECTIVE_PAGE '+arg.split(' ; ')[1]), 'ADRP identical effective absolute page'
    if op in ('b','bl','cbz','cbnz','tbz','tbnz') or op.startswith('b.'):
        matches = list(re.finditer(r'0x[0-9a-f]+',arg))
        if matches:
            # Last hex token is the target, not the TBZ/TBNZ bit-number immediate.
            m=matches[-1]; target=int(m[0],16)
            for name, rs in allfunc.items():
                if rs and rs[0][0]<=target<rs[-1][0]+4 and (target-rs[0][0])%4==0:
                    return (op,arg[:m.start()]+name+'+'+str(target-rs[0][0])+arg[m.end():]), 'aligned branch target identical symbol+instruction offset'
    return (op,arg), 'unchanged operands'
functions=[]; changes=collections.Counter(); unresolved=[]
names=[n for n in old if n.startswith('_zbt')]
assert names == [n for n in new if n.startswith('_zbt')]
for name in names + ['_OUTLINED_FUNCTION_0','_OUTLINED_FUNCTION_1']:
    a,b=old[name],new[name]; assert len(a)==len(b)
    na=[];nb=[];local=collections.Counter()
    for i,(x,y) in enumerate(zip(a,b)):
        nx,why=norm(x,old,a,i); ny,_=norm(y,new,b,i)
        na.append(nx);nb.append(ny)
        if nx!=ny: unresolved.append(dict(function=name,instruction=i,old=x,new=y,old_normalized=nx,new_normalized=ny))
        if x[1:]!=y[1:]: changes[why]+=1;local[why]+=1
    functions.append(dict(name=name,instructions=len(a),old_start=hex(a[0][0]),new_start=hex(b[0][0]),start_delta=b[0][0]-a[0][0],old_normalized_sha256=hashlib.sha256(json.dumps(na).encode()).hexdigest(),new_normalized_sha256=hashlib.sha256(json.dumps(nb).encode()).hexdigest(),relocation_changes=dict(local)))
assert not unresolved
# Verify the actual direct clock call order/constant IDs and identify bracket work.
def reads(rows):
    out=[]
    for i,x in enumerate(rows):
        if x[1]=='bl' and x[2].endswith('symbol stub for: _clock_gettime'):
            prev=rows[i-1]; assert prev[1]=='mov' and prev[2].startswith('w0, #')
            out.append(dict(index=i,address=hex(x[0]),clock_id=int(prev[2].split('#')[1],16)))
    return out
lookup_reads=reads(new['_main']); control_reads=reads(controls['_main'])
assert [x['clock_id'] for x in lookup_reads]==[6,6,6,16,6,6,16,6]
assert [x['clock_id'] for x in control_reads]==[6,16,6,6,6,6,16,6]
assert new['_main'][1108][1:]==('bl','_zbtreeScore')
assert controls['_main'][55][1:]==('madd','x23, x23, x9, x10')
assert controls['_main'][56][1:]==('subs','w8, w8, #0x1')
assert controls['_main'][57][1:]==('b.ne','0x100000674')
assert controls['_main'][74][2].endswith('symbol stub for: _nanosleep')
assert controls['_main'][86][2].endswith('symbol stub for: _nanosleep')
assert controls['_main'][79][1:]==('cmp','w8, #0x4')
# Validate remaining vendor literal loads by reading Mach-O segments, without execution.
def vm_bytes(p, address, length):
    raw=p.read_bytes();magic,cpu,sub,typ,ncmds,sz,flags,res=struct.unpack_from('<8I',raw)
    assert magic==0xfeedfacf; off=32
    for _ in range(ncmds):
        cmd,size=struct.unpack_from('<2I',raw,off)
        if cmd==0x19:
            vm,vms,fileoff,filesz=struct.unpack_from('<4Q',raw,off+24)
            if vm<=address and address+length<=vm+filesz:
                start=fileoff+address-vm;return raw[start:start+length]
        off+=size
    raise ValueError('VM range not file-backed')
binbase=W/'build/m6-clock-bracket-001/native'
vendor=[]
for oldaddr,newaddr in [(0x100012380,0x100012470),(0x100012390,0x100012480)]:
    a=vm_bytes(binbase/'old-lookup',oldaddr,16);b=vm_bytes(binbase/'lookup',newaddr,16)
    assert a==b;vendor.append(dict(old_address=hex(oldaddr),new_address=hex(newaddr),length=16,sha256=hashlib.sha256(a).hexdigest(),equal=True))
paths=[oldp,newp,controlp,E/'review/codegen/command.json',E/'results/build/status.json',E/'results/build/build-manifest.json',E/'inputs.json',E/'driver.py',E/'PLAN.json',E/'harness/clock-bracket.h',E/'harness/lookup.c',E/'harness/controls.c',W/'src/zset_btree.c',W/'src/zset_btree.h',binbase/'lookup',binbase/'controls',binbase/'old-lookup']
inputs=json.loads((E/'inputs.json').read_text())['files_sha256']
mismatches=[k for k,v in inputs.items() if sha(W/k)!=v]
assert not mismatches
consult=ROOT/'scratch/cpu-perf-m6-bracket-20261019/codegen/codegen-calls.jsonl'
shared=[]
for line in consult.read_text().splitlines():
    item=json.loads(line)
    shared.append(dict(method=item['method'],tool=item['params'].get('name'),started_utc=item['started_utc'],finished_utc=item['finished_utc'],request_sha256=hashlib.sha256(json.dumps(item['params'],sort_keys=True).encode()).hexdigest(),response_sha256=hashlib.sha256(json.dumps(item['response'],sort_keys=True).encode()).hexdigest()))
report=dict(status='PASS',scope='Independent retained native codegen review only; no performance or clock-accuracy qualification',reviewer='/root/followup_proposal_b',model='Inherited Codex/GPT-6 family; exact serving variant/token/currency costs unknown',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),native_execution=False,peer_new_reviews_read=False,offline_attempt_history=['Initial offline analyzer attempt looked for input-manifest.json rather than actual inputs.json and stopped with FileNotFoundError after assembly checks; no result/native execution. Filename corrected.'],
 provenance_sha256={str(p.relative_to(W)):sha(p) for p in paths},input_pins=dict(count=len(inputs),mismatches=mismatches),tree=dict(functions=len(names),instructions=sum(len(old[n]) for n in names),all_same_instruction_counts=True,all_normalized_equal=True,unresolved=unresolved,relocation_normalization_counts=dict(changes),function_details=functions,compiler_outlined_helpers=2),
 lookup=dict(all_clock_calls=lookup_reads,bracket_clock_calls=lookup_reads[2:],bracket_clock_ids=[6,16,6,6,16,6],score_call='0x100001738',score_loop_head='0x100001704',score_loop_exit_test='0x100001700',score_loop_continue='0x10000175c -> 0x1000016e4 -> 0x100001704',after_w3_cpu_endpoint_call='0x1000019f8',timestamp_csv_printf='0x10000124c',observation='Score call, score checksum conversion and query/count backedge remain after w1 and before w2 on the actual hit path; dispatch overhead remains in I. Conversion/emission uses the six retained timestamps; no extra profiling hooks.'),
 controls=dict(all_clock_calls=control_reads,outer_clock_indices=[32,37,42,102,108,115],outer_clock_ids=[6,16,6,6,16,6],lcg=dict(iterations=2000000,initial=1,multiplier=1664525,increment=1013904223,modulus='2^64',loop_madd='0x100000674',loop_decrement='0x100000678',loop_backedge='0x10000067c',not_folded=True),block=dict(requested_ns=20000000,first_nanosleep='0x1000006c0',retry_nanosleep='0x1000006f0',errno_eintr_test='0x1000006d4',inner_wall_start='0x1000006ac',inner_wall_end='0x100000700',remaining_request_copy='0x1000006dc..0x1000006e0',all_inside_outer_brackets=True),sink_update='0x10000079c..0x1000007ac after w3',timestamp_csv_printf='0x10000083c'),
 ancillary=dict(scan_verify='Harness-only cold assertion file/line differences are retained, expected from lookup frontend path and line movement; excluded from tree-equality claim.',siphash_nocase_relocated_vectors=vendor,tree_scope='All 72 emitted _zbt labels and both compiler-outlined helpers; inlined target operations are covered within their containing function. Not a formal whole-program equivalence proof.'),
 mcp=dict(own_availability_check_utc='2026-10-19T15:09:02Z',own_exposed_matching_tools=[],consultation='Explicit shared root stdio consultation, not a B-owned endpoint call',journal_generic='scratch/cpu-perf-m6-bracket-20261019/codegen/codegen-calls.jsonl',journal_sha256=sha(consult),calls=shared,coverage='2 of 287 indexed sources, 93 passages, keyword-only',limitation='Actual arm64 otool context misclassified as perf stat and routed to irrelevant Intel/AMD recommendations; no relevant supporting passage. No routing advice or recommendations used.'),
 limits=['Static instruction placement does not bound clock accuracy, resolution error, accounting lag, interrupt/descheduling latency or sample cost.','Conditional thread interval remains conditional; empirical controls cannot establish a worst-case error bound.','Relocations change addresses/layout. Static normalized instruction agreement is not a claim of identical runtime performance, branch-predictor/cache state or unchanged surrounding harness overhead.','No native build, benchmark, profile or control execution was performed by this reviewer.'])
(E/'review/CODEGEN-B.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(status=report['status'],tree_functions=len(names),tree_instructions=report['tree']['instructions'],input_pins=len(inputs),relocations=dict(changes),report_sha256=sha(E/'review/CODEGEN-B.json')),indent=2))
