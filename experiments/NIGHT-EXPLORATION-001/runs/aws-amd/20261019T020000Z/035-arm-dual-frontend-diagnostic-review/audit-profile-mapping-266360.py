import pathlib,re,json,collections,hashlib,sys
P=pathlib.Path(sys.argv[1]);O=P/'profile';a=json.loads((O/'audit.json').read_text());seal=json.loads((P/'profile-evidence-seal.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for n,h in seal['files'].items():assert sha(P/n)==h,n

def assembly(path):
 funcs={};current=None
 for line in path.read_text().splitlines():
  m=re.fullmatch(r'([0-9a-f]+) <([^>]+)>:',line)
  if m:current=m[2];funcs[current]={'base':int(m[1],16),'words':{}}
  m=re.match(r'^\s*([0-9a-f]+):\s*\t([0-9a-f]{8})\s*\t(.*)',line)
  if m:assert current;funcs[current]['words'][int(m[1],16)-funcs[current]['base']]=m[2]
 return funcs

def strict(fn,other,off):
 if fn==other:return 'same_offset_exact',off
 if not all(off+i in fn for i in range(-12,13,4)):return 'unmatched',None
 hits=[j for j in other if all(other.get(j+i)==fn[off+i] for i in range(-12,13,4))]
 return ('unique_exact_seven_word_window',hits[0]) if len(hits)==1 else ('ambiguous_or_unmatched',None)

maps={};stats=collections.Counter();unmatched=[];own_pcs=0
for front in ['primary','h4']:
 for variant in ['control','A']:
  key=front+'-'+variant;maps[key]={mode:assembly(O/(key+'-'+mode+'-full-asm.stdout')) for mode in ['profile','original','actual']};m=maps[key]
  flattened=lambda fs:{fn['base']+offset:word for fn in fs.values() for offset,word in fn['words'].items()}
  assert flattened(m['original'])==flattened(m['actual'])
for p in a['profiles']:
 key=p['fixture']['frontend']+'-'+p['variant'];m=maps[key];bases=set();treebad=0
 for sample in p['samples']:
  sym,off=sample['symbol'],sample['offset']
  if sym not in m['profile'] or off not in m['profile'][sym]['words']:continue
  own_pcs+=1;fn=m['profile'][sym];pc=fn['base']+off;base=int(sample['physical_ip'],16)-pc;assert base>=0 and base%4096==0 and base==sample['load_base'];bases.add(base)
  for mode in ['original','actual']:
   status,at=strict(fn['words'],m[mode].get(sym,{}).get('words',{}),off);assert status==sample[mode]['status'];assert at is None or at==sample[mode]['offset']
  if sym.startswith('zbt'):
   good=sample['actual']['status'] in ['same_offset_exact','unique_exact_seven_word_window'];stats['tree_events']+=1;stats['tree_matched' if good else 'tree_unmatched']+=1
   if not good:
    treebad+=1;other=m['actual'].get(sym,{}).get('words',{});same=fn['words'][off]==other.get(off);stats['unmatched_same_isolated_word' if same else 'unmatched_different_isolated_word']+=1;unmatched.append(dict(label=p['label'],symbol=sym,offset=off,period=sample['period'],same_isolated_word=same,status=sample['actual']['status']))
 assert len(bases)==1 and p['all_sampled_tree_bytes_match_actual']==(treebad==0)
print(json.dumps(dict(sealed_files=len(seal['files']),strict_mapping_independently_reconstructed=True,own_physical_pcs=own_pcs,tree=dict(stats),unmatched_events=unmatched),indent=2))
