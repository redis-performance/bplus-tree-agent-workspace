#!/usr/bin/env python3
from pathlib import Path
import collections,csv,hashlib,json,re,sys
p=Path(__file__).resolve().parent

def parse(block):
 lines=block.strip().splitlines();assert lines and re.fullmatch(r'\s*\d+\s*',lines[0]);period=int(lines[0]);frames=[]
 for line in lines[1:]:
  m=re.match(r'\s*([0-9a-f]+)\s+(.*)',line);assert m,line
  frames.append((m[1],m[2]))
 assert frames
 main=[int(m[1],16)for ip,name in frames if '(inlined)'not in name and (m:=re.match(r'main\+0x([0-9a-f]+)(?:\s|$)',name))]
 scope='incomplete'if not main else 'ambiguous'if len(main)!=1 else 'timed'if main==[0xe04]else 'verify'if main==[0xf90]else 'other'
 same=[name for ip,name in frames if ip==frames[0][0]]
 offsets=[int(m[1],16)for name in same if '(inlined)'not in name and (m:=re.match(r'zbtIndexScanSlot\+0x([0-9a-f]+)(?:\s|$)',name))];assert len(offsets)<=1
 return dict(period=period,scope=scope,top_ip=frames[0][0],top_labels=same,slot_offset=offsets[0]if offsets else None,main_offsets=main)
def negatives():
 t=lambda rest:'100\n 1000 zbtIndexScanSlot+0x304\n'+rest
 cases=[('timed',t(' 2000 main+0xe04'),'timed'),('verify',t(' 2000 main+0xf90'),'verify'),('missing',t(' 2000 unknown'),'incomplete'),('conflict',t(' 2000 main+0xe04\n 3000 main+0xf90'),'ambiguous'),('inlined-only',t(' 2000 main+0xe04 (inlined)'),'incomplete'),('other',t(' 2000 main+0xdf0'),'other')]
 for name,text,want in cases:assert parse(text)['scope']==want,name
 x=parse('100\n 1000 unrelated+0x304\n 2000 main+0xe04');assert x['scope']=='timed'and x['slot_offset']is None
 return {'cases':7,'status':'pass','controls':[x[0]for x in cases]+['unrelated-IP-not-slot']}
if '--self-test'in sys.argv:print(json.dumps(negatives()));sys.exit(0)
f=json.loads((p/'plan-freeze.json').read_text());d=p/'profiles';m=json.loads((d/'result.json').read_text());assert m['status']=='complete'and len(m['captures'])==12 and len(m['commands'])==52
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes'];fixtures={};controls=[];rows=[];samples=[]
regions={int(a,16)-0x10298 for a in f['B_predicate_addresses']};assert len(regions)==70
for item in f['capture_schedule']:
 v,n,seed=item['variant'],item['size'],item['seed'];name=f'{v}-n{n}-s{seed}'
 kinds=['plain','sampled']+(['disabled']if seed==1 else []);rr={}
 for k in kinds:
  q=list(csv.DictReader((d/(name+'-'+k+'.stdout')).open()));assert len(q)==1;row=q[0];assert row['cpu_start']==row['cpu_end']=='2';assert row['case']=='scan'and int(row['size'])==n and row['requested_ops']=='5000000'and row['member_bytes']=='16'and int(row['seed'])==seed;rr[k]=tuple(row[x]for x in fields)
 assert len(set(rr.values()))==1
 key=(n,seed)
 if key in fixtures:assert fixtures[key]==rr['plain']
 fixtures[key]=rr['plain'];controls.append(dict(item,semantic_parity=True,modes=kinds))
 if seed==1:assert '<not counted>,,cycles:u,0,'in(d/(name+'-disabled.stat')).read_text()
 r=dict(item,events=0,period=0,scopes={x:{'events':0,'period':0}for x in ['timed','verify','other','incomplete','ambiguous']},slot_events=0,slot_assignable_events=0,timed_slot_events=0,timed_slot_period=0,predicate_events=0,predicate_period=0)
 for idx,block in enumerate(re.split(r'\n\s*\n',(d/(name+'-samples.stdout')).read_text().strip())):
  x=parse(block);x.update(capture=name,index=idx);samples.append(x);r['events']+=1;r['period']+=x['period'];r['scopes'][x['scope']]['events']+=1;r['scopes'][x['scope']]['period']+=x['period']
  if x['slot_offset']is not None:
   r['slot_events']+=1
   if x['scope']in ['timed','verify']:r['slot_assignable_events']+=1
   if x['scope']=='timed':
    r['timed_slot_events']+=1;r['timed_slot_period']+=x['period']
    if v=='B'and x['slot_offset']in regions:r['predicate_events']+=1;r['predicate_period']+=x['period']
 assert r['events'] and r['scopes']['timed']['period']
 r['slot_stack_assignable_fraction']=r['slot_assignable_events']/r['slot_events']if r['slot_events']else 0;r['stack_gate']=r['slot_stack_assignable_fraction']>=.90;r['predicate_timed_period_pct']=100*r['predicate_period']/r['scopes']['timed']['period'];r['slot_timed_period_pct']=100*r['timed_slot_period']/r['scopes']['timed']['period'];rows.append(r)
summary=[]
for v in ['base','B']:
 for n in [100000,1000000]:
  rr=[r for r in rows if r['variant']==v and r['size']==n];assert len(rr)==3;events=sum(r['predicate_events']for r in rr);period=sum(r['predicate_period']for r in rr);total=sum(r['scopes']['timed']['period']for r in rr);pct=100*period/total;gate=all(r['stack_gate']for r in rows if r['size']==n)
  summary.append(dict(variant=v,size=n,timed_events=sum(r['scopes']['timed']['events']for r in rr),timed_period=total,slot_timed_period_pct=100*sum(r['timed_slot_period']for r in rr)/total,predicate_events=events,predicate_period=period,predicate_timed_period_pct=pct,all_capture_stack_gate=gate,material_support=(v=='B'and gate and events>=100 and pct>=5 and all(r['predicate_timed_period_pct']>=1 for r in rr))))
(o:=p/'analysis').mkdir(exist_ok=True)
for name,data in [('parser-controls',negatives()),('semantic-controls',controls),('sample-classifications',samples),('capture-summary',rows),('summary',summary)]: (o/(name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(summary,indent=2))
