import pathlib,json,csv,math,statistics,sys
p=pathlib.Path(sys.argv[1]);roots={'Frontend_Bound','Bad_Speculation','Backend_Bound','Retiring'};out={'captures':[],'metrics':{}};values={}
for i in range(3):
 stem='tma-'+str(i);sc=json.loads((p/(stem+'.scope.json')).read_text());cmd=json.loads((p/(stem+'.command.json')).read_text());streams=[(p/(stem+'.stderr')).read_text(),(p/(stem+'.stdout')).read_text()]
 candidates=[]
 for text in streams:
  lines=text.splitlines();heads=[j for j,l in enumerate(lines) if l.startswith('Timestamp,') and 'Area' in l and 'Multiplex' in l]
  if len(heads)==1:candidates.append(lines[heads[0]:])
 assert len(candidates)==1
 rows=[];advisories=[];invalid=[]
 for r in csv.DictReader(candidates[0]):
  try:stamp=float(r.get('Timestamp',''))
  except (ValueError,TypeError):advisories.append(r);continue
  if not r.get('Area'):invalid.append(r);continue
  rows.append(r)
 groups={}
 for r in rows:
  if r['Area'] in roots:groups.setdefault(r['Timestamp'],[]).append(r)
 try:
  partition=len(groups)==5 and all(len(rs)==4 and {r['Area'] for r in rs}==roots and all(r['Unit'] in ['% Slots','% Slots <'] and math.isfinite(float(r['Value'])) and 0<=float(r['Value'])<=100 for r in rs) and abs(sum(float(r['Value']) for r in rs)-100)<=.3 for rs in groups.values())
  mux=[float(r['Multiplex']) for r in rows];muxok=bool(rows) and all(x==100 for x in mux)
 except (ValueError,TypeError,KeyError):partition=False;muxok=False;mux=[]
 good=not invalid and cmd['returncode']==0 and sc['pass'] and partition and muxok
 out['captures'].append({'capture':stem,'qualified':good,'metric_rows':len(rows),'intervals':len(groups),'scope':sc['pass'],'accounting_error_percent':sc['accounting_error_percent'],'root_partition':partition,'mux_all_100':muxok,'invalid_numeric_rows':invalid,'non_metric_advisory_rows':advisories})
 for r in rows:
  if r['Unit'] not in ['% Slots','% Slots <']:continue
  try:x=float(r['Value']);assert math.isfinite(x)
  except (ValueError,TypeError,AssertionError):continue
  values.setdefault(r['Area'],[]).append(x)
out['all_qualified']=all(x['qualified'] for x in out['captures'])
for k,v in values.items():out['metrics'][k]={'mean':statistics.mean(v),'min':min(v),'max':max(v),'n':len(v),'unit':'% total pipeline slots','qualified':out['all_qualified']}
for kind in ['counters','samples']:out[kind+'_scope']=json.loads((p/(kind+'.scope.json')).read_text())['pass']
(p/'analysis.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'all_qualified':out['all_qualified'],'roots':{k:v for k,v in out['metrics'].items() if k in roots},'counter_scope':out['counters_scope'],'sample_scope':out['samples_scope']},indent=2))
