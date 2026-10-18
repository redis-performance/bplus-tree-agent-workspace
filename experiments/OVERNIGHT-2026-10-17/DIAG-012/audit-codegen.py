from pathlib import Path
import json,re,hashlib
P=Path(__file__).resolve().parent;R=P.parents[2];D=P/'attempt-002/validation';F=json.loads((P/'attempt-002/freeze.json').read_text());S=R/F['snapshot_root'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def symbols(pad):
 return {m[2]:int(m[1],16) for line in (D/f'{pad}-symbols.stdout').read_text().splitlines() if (m:=re.match(r'^([0-9a-f]+)\s+\w\s+(.+)$',line))}
def body(pad,name):
 text=(D/f'{pad}-assembly.stdout').read_text();a=text.index(name+':\n');b=text.find('\n_',a+1);s=text[a:b];s=s[:s.rindex('\tret\n')+5] if name=='_zbtreeIteratorNext' else s;start=symbols(pad)[name];out=[]
 for line in s.splitlines()[1:]:
  m=re.match(r'([0-9a-f]+)\s+(.+)',line)
  if not m:continue
  ins=m[2].split(' ; ')[0];ins=re.sub(r'0x[0-9a-f]+',lambda m:'@'+str(int(m[0],16)-start) if start<=int(m[0],16)<start+0x1000 else m[0],ins);out.append(ins)
 return out
base=symbols(0);checks=[]
for pad in [0,16,32,48]:
 ss=symbols(pad);assert ss.keys()==base.keys()
 moved={n:ss[n]-base[n] for n in ss if ss[n]!=base[n]};assert moved==({'_zbtreeIteratorNext':pad} if pad else {}),moved
 for name in ['_traverse','_zbtreeIteratorNext']:assert body(pad,name)==body(0,name),(pad,name)
 for kind in ['release','sanitize','upstream']:
  original=(S/'0'/f'build/{kind}-original.s').read_bytes();placed=(S/str(pad)/f'build/{kind}-placed.s').read_bytes();a=original.index(b'\t.globl\t_zbtreeIteratorNext');b=original.index(b'\t.cfi_endproc',a)+len(b'\t.cfi_endproc');assert placed==original[:a]+f'\t.space {pad}\n'.encode()+original[a:b]+f'\n\t.space {64-pad}\n'.encode()+original[b:]
 checks.append(dict(pad=pad,iterator_address=hex(ss['_zbtreeIteratorNext']),mod64=ss['_zbtreeIteratorNext']%64,caller_address=hex(ss['_traverse']),only_symbol_moved=moved,caller_instructions=len(body(pad,'_traverse')),iterator_instructions=len(body(pad,'_zbtreeIteratorNext'))))
(P/'codegen-audit.json').write_text(json.dumps(dict(pass_all=True,checks=checks,freeze_sha256=sha(P/'attempt-002/freeze.json')),indent=2)+'\n')
(P/'CODEGEN.md').write_text('# Linked-code isolation audit\n\nAll C inputs match HARNESS-004. All assembler bytes outside the two inserted padding\ndirectives round-trip exactly, including binary test literals. All named symbols keep\ntheir addresses except zbtreeIteratorNext, which moves by the specified offset. Caller\naddress and relocation-normalized instructions match; iterator instructions/relative\ncontrol flow match. Direct-call displacement encodings necessarily follow the moved\ncallee. This is not an assertion that every binary byte is identical. Padding is outside\nfunction entry/return paths. No cache or predictor mechanism established.\n\n'+json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks))
