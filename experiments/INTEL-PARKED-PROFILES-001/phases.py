"""Expose ordered capture phases, including failed observations, without filtering."""
import collections,csv,json,statistics
from pathlib import Path
h=Path(__file__).resolve().parent;phases=[]
for config in json.loads((h/'analysis.json').read_text())['configurations']:
 origin=None
 for cap in config['captures']:
  sc=json.loads((h/'results'/(cap['tag']+'.scope.json')).read_text())
  if origin is None:origin=sc['before']['time']
  lines=(h/'results'/(cap['tag']+'.stderr')).read_text().splitlines();start=next(i for i,l in enumerate(lines) if l.startswith('Timestamp,Area,Value,Unit,'));groups=collections.defaultdict(list)
  for r in csv.DictReader(lines[start:]):
   if r.get('Area') and r['Unit'] in ['% Slots','% Slots <']:groups[r['Area']].append(float(r['Value']))
  phases.append({'cell':config['cell'],'variant':config['variant'],'tag':cap['tag'],'level':cap['level'],'qualified':cap['qualified'],'start_seconds_since_first_capture':sc['before']['time']-origin,'end_seconds_since_first_capture':sc['after']['time']-origin,'slot_means':{k:statistics.mean(v) for k,v in groups.items()},'use':'L3 exploratory; L2 mean numeric observations retained even when config unavailable; no steady-state assumption'})
(h/'window-phases.json').write_text(json.dumps(phases,indent=2)+'\n')
