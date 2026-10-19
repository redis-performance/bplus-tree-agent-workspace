#!/usr/bin/env python3
"""Static inventory of already captured matched adapter disassemblies; no execution."""
from pathlib import Path
import hashlib,json,re
OUT=Path(__file__).resolve().parent
BASE=OUT.parent
SOURCE=BASE/'012-contract-diagnostic'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def parse(p):
 functions={};name=None
 for line in p.read_text().splitlines():
  if re.fullmatch(r'_[^\s:]+:',line):name=line[:-1];functions[name]=[]
  elif name and re.match(r'^[0-9a-f]{16}\s',line):functions[name].append(line.split(None,1)[1])
 return functions
def describe(lines):
 if lines is None:return None
 frame=0
 for line in lines[:16]:
  instruction=line.split(';',1)[0]
  m=re.search(r'^sub\s+sp, sp, #(0x[0-9a-f]+|[0-9]+)',instruction)
  if m:frame+=int(m[1],0);continue
  m=re.search(r'\[sp, #-(0x[0-9a-f]+|[0-9]+)\]!',instruction)
  if m:frame+=int(m[1],0);continue
  if re.match(r'^(stp|str)\s',instruction) and '[sp' in instruction:continue
  if re.match(r'^(add|mov)\s+x29, sp',instruction):continue
  break
 return dict(instruction_lines=len(lines),entry_prefix_frame_bytes=frame,
             stack_related_instruction_lines=sum('[sp' in s or re.search(r'\bsp, sp\b',s) is not None for s in lines),
             direct_call_instruction_lines=sum(re.match(r'^bl\s',s) is not None for s in lines))
def main():
 sources={a:SOURCE/'build-logs'/('assembly-'+a+'.stdout') for a in ['old','new']}
 parsed={a:parse(p) for a,p in sources.items()}
 frozen=json.loads((SOURCE/'freeze.json').read_text())
 for p,h in (frozen['files_sha256']|frozen['binaries_sha256']).items():assert sha(Path(p))==h,p
 rows=[dict(symbol=n,**{a:describe(parsed[a].get(n)) for a in ['old','new']}) for n in sorted(set(parsed['old'])|set(parsed['new']))]
 changed=[r for r in rows if r['old']!=r['new']]
 identity={str(p.relative_to(BASE)):sha(p) for p in [*sources.values(),SOURCE/'freeze.json',SOURCE/'PLAN.json']}
 out=dict(classification='STATIC code generation inventory only; no benchmark, profile capture, candidate or population',inputs_sha256=identity,source_and_binary_identity='012-contract-diagnostic/freeze.json',symbol_counts={a:len(x) for a,x in parsed.items()},changed_summary_rows=len(changed),rows=rows,entry_frame_method='Contiguous function-entry prefix only; stops at first ordinary instruction. Not a CFG/stack-depth proof. Cold path frames remain counted only among stack-related instructions.',limitations=['Instruction lines are static size, not retired instructions, cycles or speed','Separate binary layout/call/inlining decisions are compiler consequences of the truthful adapter contract','Not comparable to other benchmark binaries or historical006 code sizes','No elapsed fields or PC counts are used'],participant='/root',backend='Inherited Codex/GPT-6 family; exact serving model/token/currency cost unknown')
 (OUT/'inventory.json').write_text(json.dumps(out,indent=2)+'\n')
 selected=['_traverse','_zbtreeIteratorNext','_zbtreeScoreRaw','_zbtScoreLeafFindMember','_zbtreeRank']
 lines=['# Adapter compiler-contract static inventory','', 'This analyzes the already captured old/new disassemblies from012. No executable is launched, source edited, or timing/profile data collected. Both original disassembly hashes are checked against their captured command log below; frozen source and binary hashes are reverified. Static size is not dynamic work or speed.','', '|Symbol|Instruction lines old→new|Entry-prefix frame bytes old→new|','|---|---|---|']
 for n in selected:
  r=next(x for x in rows if x['symbol']==n);a,b=r['old'],r['new'];lines.append(f'|`{n}`|{a["instruction_lines"]}→{b["instruction_lines"]}|{a["entry_prefix_frame_bytes"]}→{b["entry_prefix_frame_bytes"]}|')
 journal=[json.loads(s) for s in (SOURCE/'commands.jsonl').read_text().splitlines()]
 for a,p in sources.items():
  record=next(x for x in journal if x['name']=='assembly-'+a);assert record['logs']['stdout']['sha256']==sha(p)
 lines+=['', 'The compiler-contract correction changes more than the iterator frame. Other functions can shrink or grow as inlining and cold-path decisions change. A smaller entry frame combined with larger code is not evidence of either a speedup or regression. The leaf search helper keeps a144-byte entry frame in these binaries.','', 'The iterator has no function-entry frame after correction; its cold panic frame remains16bytes, independently mapped in013. Entry-prefix inventory is a simple assembly parser, not a general control-flow/stack-depth proof. Full rows, source/binary identities, method and limits are in inventory.json.','', 'Historical tree candidates and old-adapter profiles retain their original identity. These static observations do not adopt, re-rank or reconfirm any candidate; future comparisons need a corrected-adapter baseline and local evidence. Counts unchanged.','', 'Reproduce from the repository root: `python3 '+str(OUT.relative_to(Path.cwd())/'inventory.py')+'`. Actual participant/root; inherited Codex/GPT-6 family, exact serving backend/token/currency costs unknown.']
 (OUT/'README.md').write_text('\n'.join(lines)+'\n')
 print(json.dumps(dict(symbol_counts=out['symbol_counts'],changed_summary_rows=len(changed),status='STATIC inventory complete')))
if __name__=='__main__':main()
