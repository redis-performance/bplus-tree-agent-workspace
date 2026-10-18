from pathlib import Path
import collections,datetime,hashlib,json,re
P=Path(__file__).resolve().parent;R=P.parents[1];E=R/'experiments/EXP-006/profile-results';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for item in json.loads((E/'codegen.json').read_text()):
 v=item['variant'];p=E/(v+'-leaf-assembly.txt');assert sha(p)==item['leaf_assembly_sha256'];assert sha(R/item['assembly'])==item['assembly_sha256']
 raw=p.read_text();ins=[]
 for lineno,line in enumerate(raw.splitlines(),1):
  text=line.split(';',1)[0].strip()
  if not text or text.startswith('.') or text.endswith(':'):continue
  match=re.fullmatch(r'([a-z][a-z0-9.]*)(?:\s+(.*))?',text)
  if match:ins.append(dict(line=lineno,opcode=match[1],operands=match[2] or '',text=text))
 frame=[x for x in ins if x['opcode']=='sub' and re.fullmatch(r'sp,\s*sp,\s*#\d+',x['operands'])];assert len(frame)==1
 stack=[x for x in ins if re.search(r'\[(sp|x29)(?:,|\])',x['operands'])]
 loads=[x for x in stack if x['opcode'].startswith(('ldr','ldur','ldp'))]
 stores=[x for x in stack if x['opcode'].startswith(('str','stur','stp'))]
 assert len(loads)+len(stores)==len(stack)
 calls=[x['operands'] for x in ins if x['opcode']=='bl'];assert calls==item['leaf_calls']
 rows.append(dict(variant=v,input=str(p.relative_to(R)),input_sha256=sha(p),full_assembly=item['assembly'],full_assembly_sha256=item['assembly_sha256'],compiler_command=item['command'],static_instruction_lines=len(ins),own_frame_bytes=int(frame[0]['operands'].rsplit('#',1)[1]),static_stack_load_sites=len(loads),static_stack_store_sites=len(stores),calls=calls,stack_accesses=stack,opcode_histogram=dict(sorted(collections.Counter(x['opcode'] for x in ins).items()))))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PASS',scope='Post-hoc descriptive inventory of already frozen round18 compiler assembly; no new compilation, execution, timing, preregistered hypothesis test or diagnostic count.',limitations=['Includes prologue/epilogue, callee-save traffic, all branch paths and cold assertions.','Static sites are not dynamic counts, cycles, stalls, performance or cache pressure.','Own frame omits called libc frames; do not infer peak call-chain stack or tree-owned memory.','No inference that frame difference explains single-lane versus batched timing.','Compiler assembly is not a linked address-layout or alignment audit.'],rows=rows)
(P/'ROUND-020-STATIC-LEAF-AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{k:r[k] for k in ['variant','static_instruction_lines','own_frame_bytes','static_stack_load_sites','static_stack_store_sites']} for r in rows],indent=2))
