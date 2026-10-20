"""Read-only result analysis and isolated, explicit-unit MCP import.

Use scratch/topdown-profiler-assessment/.venv/bin/python after harvest.
No capture is dropped from coverage; qualified comparisons require all3 L2 windows.
"""
import asyncio,collections,csv,hashlib,json,math,os,statistics,uuid
from pathlib import Path
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
from topdown.storage.sqlite_backend import SQLiteBackend
from topdown.storage.models import Run,Sample
H=Path(__file__).resolve().parent;R=H.parent.parent;D=H/'results'
ROOTS=['Frontend_Bound','Bad_Speculation','Backend_Bound','Retiring']
def rawrows(path):
 lines=path.read_text().splitlines();start=[i for i,l in enumerate(lines) if l.startswith('Timestamp,Area,Value,Unit,')]
 if len(start)!=1:return []
 return [r for r in csv.DictReader(lines[start[0]:]) if r.get('Area')]
async def main():
 source=json.loads((D/'summary.json').read_text());db=R/'scratch/intel-followup-slots.db'
 if db.exists():db.unlink()
 backend=SQLiteBackend(db);backend.initialize();configurations=[];imports=[]
 for record in source:
  tag=record['cell']+'-'+record['variant'];values=collections.defaultdict(list);captures=[]
  for capture in record['captures']:
   path=D/(capture['tag']+'.stderr');rows=rawrows(path)
   entry={'tag':capture['tag'],'level':capture['level'],'qualified':capture['qualified'],'raw_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'mux_min':capture['mux_min']}
   if capture['level']==2:
    for row in rows:
     if row['Area'].split('.')[0] in ROOTS and row['Unit'] in ('% Slots','% Slots <'):values[row['Area']].append(float(row['Value']))
    if capture['qualified']:
     rid=str(uuid.uuid5(uuid.NAMESPACE_URL,'intel-followup-slot-import:'+entry['raw_sha256']))
     backend.insert_run(Run(run_id=rid,process_name='bplus-intel-followup',level=2,duration_seconds=5,system_wide=True,labels={'cell':record['cell'],'variant':record['variant'],'cpu':'2','raw_sha256':entry['raw_sha256'],'processing':'slot-only; canonicalized unit spelling; unchanged values','timestamp_origin':'ingestion, not capture'}))
     samples=json.loads((D/(capture['tag']+'.samples.json')).read_text())
     backend.insert_samples([Sample(run_id=rid,**dict(s,unit='%_Slots')) for s in samples if s['metric_name'].split('.')[0] in ROOTS and s['unit'] in ('% Slots','% Slots <')])
     entry['run_id']=rid;imports.append({'run_id':rid,'cell':record['cell'],'variant':record['variant'],'rep':capture['rep']})
   captures.append(entry)
  metrics={k:{'mean':statistics.mean(v),'min':min(v),'max':max(v),'n':len(v)} for k,v in values.items()}
  item={'cell':record['cell'],'variant':record['variant'],'status':record['status'],'binary_sha256':record['binary_sha256'],'l2_qualified_windows':sum(c['qualified'] for c in captures),'captures':captures,'slot_metrics_all_retained_windows':metrics,'interpretation_qualified':len([c for c in captures if c['level']==2])==3 and sum(c['qualified'] for c in captures)==3}
  item['deep']=record.get('deep',[]);item['deep_skipped']=record.get('deep_skipped')
  configurations.append(item)
 backend.close()
 summary={'source_commit':'37efd287f','freeze_commit':'52c039e04','condition':'secondary Intel CPU2, sibling50offline, new host condition','collector':'topdown71dea5e;pmu-tools2026.4.7.0','classification':'diagnostic only; each mean includes all retained L2 windows; interpretation requires all3 qualify','configurations':configurations,'imports':imports}
 (H/'analysis.json').write_text(json.dumps(summary,indent=2)+'\n')
 env=dict(os.environ,TOPDOWN_BACKEND='sqlite',TOPDOWN_DB_PATH=str(db));env.pop('TOPDOWN_DSN',None)
 command=str(R/'scratch/topdown-profiler-assessment/.venv/bin/topdown')
 async with stdio_client(StdioServerParameters(command=command,args=['mcp-serve'],env=env)) as (read,write):
  async with ClientSession(read,write) as session:
   await session.initialize();schemas={t.name:t.model_dump(by_alias=True)["inputSchema"] for t in (await session.list_tools()).tools};calls=[]
   qualified={(c['cell'],c['variant']) for c in configurations if c['interpretation_qualified']}
   for run in imports:
    # Every imported window is available. Query one funnel per config and matched
    # first-window pairs; report means still use all3 windows, never only this one.
    if run['rep']!=1 or (run['cell'],run['variant']) not in qualified:continue
    args={'run_id':run['run_id'],'level':2};assert 'get_funnel' in schemas
    res=await session.call_tool('get_funnel',args);calls.append({'tool':'get_funnel','arguments':args,'cell':run['cell'],'variant':run['variant'],'result':res.model_dump(mode='json',by_alias=True)})
    if run['variant']!='base':
     base=next((b for b in imports if b['cell']==run['cell'] and b['variant']=='base' and b['rep']==1),None)
     if base and (base['cell'],'base') in qualified:
      args={'run_id_a':base['run_id'],'run_id_b':run['run_id']};assert 'compare_runs' in schemas
      res=await session.call_tool('compare_runs',args);calls.append({'tool':'compare_runs','arguments':args,'cell':run['cell'],'variant':run['variant'],'result':res.model_dump(mode='json',by_alias=True)})
   (H/'topdown-mcp-calls.json').write_text(json.dumps({'transport':'actual local stdio, isolated slot-only DB','tools':schemas,'calls':calls},indent=2)+'\n')
 print(json.dumps({'configurations':len(configurations),'qualified_configs':sum(c['interpretation_qualified'] for c in configurations),'imported_windows':len(imports),'mcp_calls':len(calls),'mcp_errors':sum(bool(c['result'].get('isError')) for c in calls)}))
asyncio.run(main())
