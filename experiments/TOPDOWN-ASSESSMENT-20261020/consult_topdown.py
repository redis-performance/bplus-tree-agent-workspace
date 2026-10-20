"""Actual stdio MCP queries against the imported raw captures; no remote DB writes."""
import asyncio, datetime, json, os
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
async def main():
 data=json.loads((HERE/'analysis.json').read_text())
 env=dict(os.environ,TOPDOWN_BACKEND='sqlite',TOPDOWN_DB_PATH=str(ROOT/'scratch/topdown-assessment.db'))
 env.pop('TOPDOWN_DSN',None)
 command=str(ROOT/'scratch/topdown-profiler-assessment/.venv/bin/topdown')
 async with stdio_client(StdioServerParameters(command=command,args=['mcp-serve'],env=env)) as (read,write):
  async with ClientSession(read,write) as s:
   await s.initialize();listing=await s.list_tools()
   schemas={t.name:t.inputSchema for t in listing.tools}
   calls=[('list_profiling_runs',{'process_name':'bplus-iterator-baseline','last_hours':24}),
          ('query_bottlenecks',{'process_name':'bplus-iterator-baseline','labels':{'size':'1000000'},'last_hours':24})]
   for size,level in [(100000,2),(1000000,2),(1000000,3)]:
    run=next(c for c in data['captures'] if c['size']==size and c['level']==level)
    calls.append(('get_funnel',{'run_id':run['run_id'],'level':level}))
   calls.append(('explain_metric',{'metric_name':'Backend_Bound.Memory_Bound'}))
   records=[]
   for name,args in calls:
    assert name in schemas
    result=await s.call_tool(name,args)
    records.append({'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool':name,'arguments':args,
                    'result':result.model_dump(mode='json',by_alias=True)})
   (HERE/'topdown-mcp-calls.json').write_text(json.dumps({'transport':'local stdio; upstream71dea5e; isolated SQLite containing exact raw captures',
     'tools':schemas,'calls':records},indent=2)+'\n')
   print(json.dumps({'calls':len(records),'errors':sum(bool(r['result'].get('isError')) for r in records)}))
asyncio.run(main())
