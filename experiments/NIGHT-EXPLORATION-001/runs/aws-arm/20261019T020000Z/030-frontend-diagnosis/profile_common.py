import csv,hashlib,json,pathlib,re,struct,decimal
from native_common import HERE,ORACLE,IDS,sha,SEMANTIC,same_semantics
EVENTS={'cycles:u','instructions:u','branches:u','branch-misses:u'}
def row(text,f):
 rows=list(csv.DictReader(text.splitlines()));assert len(rows)==1;z=rows[0];n=f['size'];t=(f['requested_ops']+n-1)//n;o=ORACLE[f'{n}/{f["seed"]}'];check=(o[f['frontend']+'_one_traversal_checksum']*t)&((1<<64)-1)
 expected=dict(case='iterate' if f['frontend']=='primary' else 'iterator-modes',size=n,seed=f['seed'],requested_ops=f['requested_ops'],member_bytes=16,operations=t*n,traversals=t,checksum=check,warmup_passes=f['warmup_passes'],cpu_start=2,cpu_end=2)
 if f['frontend']=='h4':expected.update(direction=f['direction'],mask=4,encoding='integer',expected_checksum=check,construction_fingerprint=o['h4_construction_fingerprint'])
 for k,v in expected.items():assert z[k]==str(v),(k,z.get(k),v)
 assert int(z['elapsed_ns'])>0 and int(z['tree_bytes'])>0 and int(z['thread_elapsed_ns'])>0
 return z
def counters(path,enabled):
 values={};runtime={}
 for line in path.read_text().splitlines():
  if not line or line.startswith('#'):continue
  z=next(csv.reader([line]));assert len(z)>=3 and z[2] not in values;values[z[2]]=z[0].strip()
  if enabled:
   assert len(z)>4 and decimal.Decimal(z[4]).is_finite() and decimal.Decimal(z[4])==100;ns=decimal.Decimal(z[3]);assert ns.is_finite() and ns>0;runtime[z[2]]=dict(percent=z[4],runtime_ns=z[3])
 assert set(values)==EVENTS
 if enabled:
  assert all(re.fullmatch(r'[0-9]+',v) for v in values.values());assert all(int(values[k])>0 for k in ['cycles:u','instructions:u','branches:u']);assert int(values['branch-misses:u'])>=0
 else:assert all(v in ['0','<not counted>'] for v in values.values())
 return dict(values=values,runtime_pct=runtime,enabled=enabled)
def census(text,f,z):
 lines=text.splitlines();assert len(lines)==1 and lines[0].startswith('CENSUS ');c=json.loads(lines[0][7:]);n=f['size'];assert c['members']==n and c['tree_bytes']==int(z['tree_bytes']);assert len(c['width_entry_hist'])==len(c['shift_entry_hist'])==65 and len(c['occupancy_leaf_hist'])==97
 assert sum(c['width_entry_hist'])==sum(c['shift_entry_hist'])==n;assert sum(c['occupancy_leaf_hist'])==c['leaves'];assert sum(i*v for i,v in enumerate(c['occupancy_leaf_hist']))==n;assert sum(x[3] for x in c['joint_leaf_hist'])==c['leaves'];assert c['width0_entries']==c['width_entry_hist'][0] and c['width64_entries']==c['width_entry_hist'][64];assert c['width0_entries']+c['aligned_nonzero_entries']+c['unaligned_nonzero_entries']==n;assert c['ninth_byte_entries']<=c['unaligned_nonzero_entries'];assert c['transitions_per_traversal']==c['leaves']-1;assert c['reversed_leaves']==sum(x[3] for x in c['joint_leaf_hist'] if x[2]);assert 0<=c['reversed_members']<=n
 expected=json.loads((HERE/'census-score-oracle.json').read_text())[f'{f["frontend"]}/{n}'];assert c['score_digest']==expected
 return c
def elf_text(path):
 b=path.read_bytes();assert b[:6]==b'\x7fELF\x02\x01';assert struct.unpack_from('<H',b,18)[0]==183;off=struct.unpack_from('<Q',b,40)[0];entsize,num,strings=struct.unpack_from('<HHH',b,58);assert entsize==64;table=[struct.unpack_from('<IIQQQQIIQQ',b,off+i*entsize) for i in range(num)];names=b[table[strings][4]:table[strings][4]+table[strings][5]]
 for x in table:
  name=names[x[0]:].split(b'\0',1)[0]
  if name==b'.text':return b[x[4]:x[4]+x[5]]
 raise AssertionError('missing .text')
def raw_samples(path):
 result=[]
 for block in re.split(r'\n\s*\n',path.read_text().strip()):
  if not block.strip():continue
  lines=block.splitlines();assert re.fullmatch(r'\s*\d+\s*',lines[0]);period=int(lines[0]);assert period>0;frames=[]
  for line in lines[1:]:
   m=re.fullmatch(r'\s*([0-9a-f]+)\s+(.+)',line);assert m,line;frames.append(dict(ip=m[1],label=m[2]))
  assert frames;top=frames[0]['ip'];same=[x for x in frames if x['ip']==top];physical=next((x['label'] for x in reversed(same) if '(inlined)' not in x['label']),'[unknown]');m=re.fullmatch(r'(.+?)\+0x([0-9a-f]+)',physical)
  result.append(dict(period=period,raw_frames=frames,physical_ip=top,physical_label=physical,symbol=m[1] if m else physical,offset=int(m[2],16) if m else None))
 return result

def mapping(fn,other,off):
 if set(fn)==set(other) and all(fn[i]['bytes']==other[i]['bytes'] for i in fn):return dict(status='same_offset_exact',offset=off)
 window=[off+4*i for i in range(-3,4)]
 if not all(i in fn for i in window):return dict(status='unmatched')
 matches=[j for j in other if all(j+4*i in other and other[j+4*i]['bytes']==fn[off+4*i]['bytes'] for i in range(-3,4))]
 return dict(status='unique_exact_seven_word_window',offset=matches[0]) if len(matches)==1 else dict(status='ambiguous_or_unmatched',matches=matches)

def scope_validity(all_losses,warnings,all_pc):
 return bool(all_losses and not warnings and all_pc)
