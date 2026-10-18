"""Preserve raw MCP retrieval privately; publish brief method/audit metadata only."""
from pathlib import Path
import hashlib,json,shutil
P=Path(__file__).resolve().parent;R=P.parents[1];S=R/'scratch/overnight-round004-mcp-raw'
assert not S.exists() and not (P/'ROUND-004-CURATION.json').exists();S.mkdir();records=[]
files=['HARNESS-002/cpu-mcp.json','AA-003/evidence-check.json','PROFILE-002/cpu-mcp-ask.json','PROFILE-002/evidence-check.json','DIAG-006/evidence-check.json']
for name in files:
 source=P/name;dest=S/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dest)
 raw_sha=hashlib.sha256(dest.read_bytes()).hexdigest()
 if name=='HARNESS-002/cpu-mcp.json':
  summary={'consulted':['cpu_perf.ask','cpu_perf.get_benchmark:05-measurement-pitfalls(method,code)','cpu_perf.get_benchmark:14-pcore-vs-ecore(method,code)'],'method_urls':['https://github.com/usamahz/cpu-performance-engineering/tree/main/misc/benchmarks/05-measurement-pitfalls','https://github.com/usamahz/cpu-performance-engineering/tree/main/misc/benchmarks/14-pcore-vs-ecore'],'applicable_method':'Consume and check results, retain repeated fixed measurements, report thread time and boundary CPU IDs as observations. Source examples run on M4 Pro; no numbers/topology transferred.','retrieval_limit':'Roofline passage irrelevant; Google Benchmark main-thread timer scope is related but does not justify independent-query noise cure.'}
 elif name.endswith('cpu-mcp-ask.json'):
  summary={'consulted':'cpu_perf.ask','topic':'Public in-process ITIMER_PROF/SIGPROF interrupted-PC profile limitations','retrieval_limit':'NAPI and Linux perf snippets unrelated to this macOS API. Not cited as support. Installed SDK manuals/headers are primary API evidence.'}
 else:
  verdict='drop_number' if name.startswith('PROFILE-002') else 'no_number'
  summary={'consulted':'cpu_perf.check_evidence','verdict':verdict,'limitations':'Frequency absent; heuristic partially parses supplied machine/compiler/method context. No portable rates, clocks, cycles or source-speedup promoted.','interpretation':'Local preregistered decisions only; see experiment README/PLAN and raw rows. Diagnostic sample counts and requested timer values are not portable performance rates.'}
 summary.update(raw_path=str(dest.relative_to(R)),raw_sha256=raw_sha,curation='Full source excerpts, code and irrelevant editorial examples retained privately instead of republished; no measurement rows changed.')
 source.write_text(json.dumps(summary,indent=2)+'\n');records.append({'file':name,'raw_path':str(dest.relative_to(R)),'raw_sha256':raw_sha,'public_sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
(P/'ROUND-004-CURATION.json').write_text(json.dumps(records,indent=2)+'\n')
