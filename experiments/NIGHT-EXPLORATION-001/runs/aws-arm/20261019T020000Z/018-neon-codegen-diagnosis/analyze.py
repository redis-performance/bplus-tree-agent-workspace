#!/usr/bin/env python3
"""Read-only existing assembly analysis. No build, execution or performance sampling."""
from pathlib import Path
import re,json,hashlib,collections
out=Path(__file__).resolve().parent;p=out.parent/'017-corrected-neon'
ranges={'A':[(0x10498,0x1052c),(0x106bc,0x10750)],'B':[(0x1049c,0x10530),(0x1059c,0x10630)],'C':[(0x10498,0x10530),(0x106a4,0x1073c)]}
loops={'base':[(0x105f4,0x10634),(0x105e8,0x105f4)],'A':[(0x106bc,0x1078c),(0x106ac,0x106bc)],'B':[(0x1059c,0x10654),(0x10588,0x1059c)],'C':[(0x106a4,0x1076c),(0x10694,0x106a4)]}
result={'scope':'Static existing zbtIndexScanSlot disassembly only; no new timing, build, profiling or source change. Address intervals are half-open. Counts are instructions, not cycles or dynamic samples.','variants':{}}
for v in ['base','A','B','C']:
 f=p/'validation'/(v+'-native-codegen.stdout');s=f.read_text();ins=[(int(a,16),op,t)for a,op,t in re.findall(r'^\s*([0-9a-f]+):\s+([0-9a-f]{8})\s+(.*)$',s,re.M)];assert ins[0][0]==0x10298
 def entry(x):return {'address':hex(x[0]),'opcode':x[1],'instruction':x[2]}
 x={'artifact':str(f.relative_to(out.parent)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'static_instructions':len(ins),'static_bytes':4*len(ins),'stack_frame_bytes':528 if v=='base'else 544,'predicate_reconstruction':[]}
 for direction,(lo,hi) in zip(['reversed','forward'],ranges.get(v,[])):
  block=[a for a in ins if lo<=a[0]<hi];pred=[a for a in block if a[2].split('\t')[0] not in ['ldr','lsl','cmeq']];assert len(pred)==35,(v,direction,len(pred));x['predicate_reconstruction'].append(dict(direction=direction,enclosing_halfopen=[hex(lo),hex(hi)],instructions=35,breakdown={'stack_byte_stores':2,'stack_halfword_reload':1,'scalar_bit_extracts':16,'scalar_to_vector_transfers':16},exact_instructions=[entry(a)for a in pred]))
 path=[a for lo,hi in loops[v]for a in ins if lo<=a[0]<hi];x['forward_continuing_zero_mask_path']={'chunk_bytes':8 if v=='base'else 16,'instructions':len(path),'ranges':[[hex(lo),hex(hi)]for lo,hi in loops[v]],'exact_instructions':[entry(a)for a in path]}
 x['forward_population_count_instructions']=[entry(a)for a in ins if a[2].startswith(('cnt\t','uaddlv\t'))];result['variants'][v]=x
(out/'analysis.json').write_text(json.dumps(result,indent=2)+'\n')
print({v:{k:x[k]for k in ['static_instructions','static_bytes','stack_frame_bytes']}for v,x in result['variants'].items()})
print({v:x['forward_continuing_zero_mask_path']['instructions']for v,x in result['variants'].items()})
