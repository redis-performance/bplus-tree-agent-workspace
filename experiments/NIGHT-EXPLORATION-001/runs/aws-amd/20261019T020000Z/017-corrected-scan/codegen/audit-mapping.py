import pathlib,re,json,hashlib
root=pathlib.Path(__file__).parent
expected={'timing':'1ecbe6a426bd3a593a9fce6b8e8c6796c8c2287706fdd7eafdba595df9bad9ed','original':'8852aff6d846f9549bb9909eec417dbd5c26ee834e39ee88696f6018c47b3685','profile':'3d8edd535ed7b6cffb568c7b9375bfb891f1db8a735ba19e75e8f749daa2bcb8'}
def parse(name):
 assert (root/(name+'.sha')).read_text().split()[0]==expected[name]
 text=(root/(name+'.asm')).read_text();base=int(re.search(r'^([0-9a-f]+) <zbtIndexScanSlot>:',text,re.M)[1],16);rows={};line=None;last=None
 for s in text.splitlines():
  src=re.search(r'zset_btree.c:(\d+)',s)
  if src:line=int(src[1])
  m=re.match(r'\s*([0-9a-f]+):\s*\t([0-9a-f ]+)\t(.*)',s)
  if m:
   last=int(m[1],16)-base;rows[last]={'bytes':m[2].split(),'assembly':m[3],'source_line':line}
  else:
   c=re.match(r'\s*([0-9a-f]+):\s*\t([0-9a-f ]+)\s*$',s)
   if c and last is not None:rows[last]['bytes']+=c[2].split()
 return base,rows
parsed={n:parse(n) for n in expected};regions=[(0x1d3,0x36a),(0x69a,0x7c0)]
selected=[off for off in parsed['profile'][1] if any(lo<=off<hi for lo,hi in regions)]
for off in selected:
 assert len({tuple(parsed[n][1][off]['bytes']) for n in expected})==1
 assert len({parsed[n][1][off]['source_line'] for n in expected})==1
samples=[]
for f in (root.parent/'profile').glob('*-samples.stdout'):
 for x in re.findall(r'zbtLeafTagMatches\+0x([0-9a-f]+)',f.read_text()):
  off=int(x,16);assert off in selected;samples.append(off)
result={'status':'pass','timing_binary_sha256':expected['timing'],'binary_sha256':expected,'function_starts':{n:hex(v[0]) for n,v in parsed.items()},'mapped_half_open_relative_ranges':[[hex(lo),hex(hi)] for lo,hi in regions],'exact_matching_instructions_including_continuation_bytes':len(selected),'sampled_helper_frames_mapped':len(samples),'instructions':[{'relative':hex(off),'bytes':' '.join(parsed['profile'][1][off]['bytes']),'source_line':parsed['profile'][1][off]['source_line'],'addresses':{n:hex(parsed[n][0]+off) for n in expected}} for off in selected],'limits':['Only the two helper instruction regions are byte-equal; whole programs and diagnostic layout differ','Includes helper loops and tails; does not claim other scan-slot caller setup is equivalent or removable','Profile samples remain coarse and cannot predict elapsed gains']}
(root/'mapping.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='instructions'},indent=2))
