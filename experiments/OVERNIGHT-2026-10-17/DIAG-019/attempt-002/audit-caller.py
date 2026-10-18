from pathlib import Path
import re,json,hashlib
P=Path(__file__).resolve().parent;out=[]
def instructions(p):return [x.split(';')[0].strip() for x in p.read_text().splitlines() if x.startswith('\t') and x.strip() and not x.lstrip().startswith(('.', ';'))]
for mode in ['on','off']:
 pa=P/f'control-{mode}-scores.s.txt';pb=P/f'C-{mode}-scores.s.txt';a=instructions(pa);b=instructions(pb);assert len(a)==len(b);diffs=[]
 for i,(x,y) in enumerate(zip(a,b)):
  if x==y:continue
  mx=re.fullmatch(r'mov\s+w1, #(\d+)',x);my=re.fullmatch(r'mov\s+w1, #(\d+)',y);assert mx and my and int(my[1])-int(mx[1])==38,(x,y)
  j=i+1
  while not a[j].startswith('bl\t'):
   assert re.match(r'(adrp|add)\s+x2,',a[j]);j+=1;assert j<=i+3
  assert a[j]==b[j]=='bl\t_standalone_panic';diffs.append(dict(index=i,control=x,C=y,panic_index=j,intervening=a[i+1:j]))
 out.append(dict(mode=mode,instruction_lines=len(a),differences=diffs,otherwise_identical=True,input_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [pa,pb]},scope='compiler assembly zbtreeScores only; not relocated bytes or dynamic instructions'))
(P/'caller-codegen-audit.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS: zbtreeScores differs only in five panic source-line immediates per prefetch mode')
