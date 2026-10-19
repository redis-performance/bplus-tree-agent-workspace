"""Strict sample accounting shared by diagnostics; never charges ancestor frames."""
import collections,json,pathlib,re

def samples(path):
    result=[]
    for block in re.split(r'\n\s*\n',path.read_text().strip()):
        if not block.strip():continue
        lines=block.splitlines();assert re.fullmatch(r'\s*\d+\s*',lines[0]);period=int(lines[0]);frames=[]
        for line in lines[1:]:
            m=re.fullmatch(r'\s*([0-9a-f]+)\s+(.+)',line);assert m,line
            frames.append((m[1],m[2]))
        assert frames;top=frames[0][0];same=[name for ip,name in frames if ip==top]
        physical=next((name for name in reversed(same) if '(inlined)' not in name),'[unknown]')
        symbol=lambda label:re.sub(r'\+0x[0-9a-f]+(?: \(inlined\))?$','',label).replace(' (inlined)','')
        result.append(dict(period=period,exclusive=symbol(same[0]),physical=symbol(physical),same_ip_inclusive=sorted({symbol(x) for x in same})))
    return result

def report(path,rows):
    text=path.read_text();lost=int(re.search(r'Total Lost Samples:\s*(\d+)',text)[1]);period=sum(r['period'] for r in rows)
    assert int(re.search(r'Event count \(approx\.\):\s*(\d+)',text)[1])==period
    label=re.search(r'# Samples:\s*(\S+)\s+of event',text)[1]
    if label.isdigit():assert int(label)==len(rows)
    return dict(lost=lost,report_sample_label=label,raw_events=len(rows),raw_period=period)

def known_gate(out,here):
    out=pathlib.Path(out);here=pathlib.Path(here);expected=json.loads((here/'known-control-expectations.json').read_text());rows=samples(out/'known-samples.stdout');r=report(out/'known-report.stdout',rows)
    known=[x for x in rows if x['physical']=='known_work'];outside=[x for x in rows if x['physical']=='outside_work'];period=sum(x['period'] for x in rows);assert period>0
    pct=100*sum(x['period'] for x in known)/period
    assert len(known)>=expected['known_work_min_events'] and pct>expected['known_work_min_period_pct_exclusive'] and len(outside)==expected['outside_work_required_events']
    return dict(status='pass',known_events=len(known),outside_events=len(outside),known_period_pct=pct,**r)
