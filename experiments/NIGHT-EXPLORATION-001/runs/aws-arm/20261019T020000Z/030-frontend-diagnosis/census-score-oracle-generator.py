import json,struct,pathlib
result={}
for front in ['primary','h4']:
 for n in [129,100000,1000000]:
  digest=14695981039346656037
  for i in range(n):
   bits=struct.unpack('<Q',struct.pack('<d',float(i-(n//2 if front=='h4' else 0))))[0];digest=((digest^bits)*1099511628211)&((1<<64)-1)
  result[f'{front}/{n}']=digest
p=pathlib.Path(__file__).parent/'census-score-oracle.json';assert json.loads(p.read_text())==result;print('six independently modeled score digests verified')
