#!/usr/bin/env python3
from pathlib import Path
import csv,datetime,hashlib,json,statistics
p=Path(__file__).resolve().parent;r=p/'screen';m=json.loads((r/'result.json').read_text());schedule=json.loads((p/'screen-schedule.json').read_text());freeze=json.loads((p/'comparison-freeze.json').read_text());rows=m['rows'];assert len(rows)<=144
last=None;hashes={}
for i,row in enumerate(rows):
 for k,v in schedule[i].items():assert row[k]==v,(i,k)
 rr=list(csv.DictReader((r/'raw'/f'screen-{i:03d}.stdout').open()));assert rr==[row['row']];assert not (r/'raw'/f'screen-{i:03d}.stderr').read_text()
 assert row['returncode']==0 and row['row']['cpu_start']==row['row']['cpu_end']=='2'
 assert row['row']['case']=='scan' and row['row']['requested_ops']=='5000000' and row['row']['member_bytes']=='16'
 assert int(row['row']['size'])==row['size'] and int(row['row']['seed'])==row['seed']
 start=datetime.datetime.fromisoformat(row['started_utc']);end=datetime.datetime.fromisoformat(row['finished_utc']);assert start<=end
 if last:assert last<=start
 last=end
 for suffix in ['stdout','stderr']:
  f=r/'raw'/f'screen-{i:03d}.{suffix}';hashes[str(f.relative_to(r))]=hashlib.sha256(f.read_bytes()).hexdigest()
effects=[]
for i in range(0,len(rows)-3,4):
 rr=rows[i:i+4];assert len({tuple(x['row'][k]for k in ['checksum','operations','tree_bytes','traversals','warmup_passes','size','seed','member_bytes'])for x in rr})==1
 ns=[int(x['row']['elapsed_ns'])/int(x['row']['operations'])for x in rr];effect=100*((ns[1]+ns[2])/(ns[0]+ns[3])-1);minimum=min(int(x['row']['elapsed_ns'])for x in rr);effects.append(dict(variant=rr[0]['variant'],size=rr[0]['size'],seed=rr[0]['seed'],block=rr[0]['block'],effect_pct=effect,min_window_ns=minimum,primary_gate=effect<=-2 and minimum>=10000000))
complete=m['status']=='complete'
if complete:assert len(rows)==len(m['attempts'])==144 and effects==m['effects'] and all(x['returncode']==0 for x in m['attempts'])
summary=[]
for variant in ['A','B','C']:
 for size in [100000,1000000]:
  group=[x for x in effects if x['variant']==variant and x['size']==size]
  if group:
   values=[x['effect_pct']for x in group];summary.append(dict(variant=variant,size=size,blocks=len(group),minimum=min(values),maximum=max(values),median=statistics.median(values),min_window_ns=min(x['min_window_ns']for x in group),all_primary_gates=complete and len(group)==6 and all(x['primary_gate']for x in group),effects=values))
survivors=[v for v in ['B','C','A']if len([x for x in summary if x['variant']==v])==2 and all(x['all_primary_gates']for x in summary if x['variant']==v)]
result=dict(status='pass',phase_status=m['status'],rows=len(rows),complete_blocks=len(effects),partial_rows=len(rows)%4,exact_schedule_prefix=True,serial_windows=True,cpu2=True,fixture_output_owned_bytes_equal=True,summary=summary,maintenance_order=freeze['maintenance_order'],primary_survivors=survivors,selected_for_further_gates=survivors[0]if survivors else 'NONE',source_adoption='NONE',limitations='Discovery only; all required guards, fresh independent confirmation, matched profile and independent review remain. No intrinsic performance ranking between implementations.',raw_sha256=hashes)
(p/'screen-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k]for k in ['phase_status','rows','complete_blocks','primary_survivors','selected_for_further_gates','summary']},indent=2))
