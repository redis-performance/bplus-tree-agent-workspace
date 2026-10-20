#!/usr/bin/env python3
"""Render repository decision Sankeys; no timing values or inferred wins."""
import collections
import hashlib
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.path import Path as MPath
from matplotlib.patches import PathPatch, Rectangle

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = json.loads((HERE/'experiments.json').read_text())
COLORS = {'Parked': '#cf982c', 'Rejected': '#c65b55', 'Approved': '#278d70'}
ARCH_COLORS = {'ARM': '#527bb8', 'Intel': '#6e68ad', 'AMD': '#448f91'}
INK = '#203147'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.fonttype': 'none', 'svg.hashsalt': 'bplus-experiment-flows'})


def ribbon(ax, x0, y0, x1, y1, height, color, alpha=.21):
    dx = (x1-x0)*.45
    vertices = [(x0,y0),(x0+dx,y0),(x1-dx,y1),(x1,y1),
                (x1,y1+height),(x1-dx,y1+height),(x0+dx,y0+height),
                (x0,y0+height),(x0,y0)]
    codes = [MPath.MOVETO,MPath.CURVE4,MPath.CURVE4,MPath.CURVE4,
             MPath.LINETO,MPath.CURVE4,MPath.CURVE4,MPath.CURVE4,MPath.CLOSEPOLY]
    ax.add_patch(PathPatch(MPath(vertices,codes), facecolor=color, edgecolor='none', alpha=alpha))


def text(ax,x,y,value,size=12,color=INK,**kw):
    ax.text(x,y,value,fontsize=size,color=color,va='center',**kw)


def node(ax,x,y,h,color):
    ax.add_patch(Rectangle((x,y),16,h,color=color,lw=0))


def canvas(height,title,subtitle,counts):
    fig,ax=plt.subplots(figsize=(19,height/100),dpi=100)
    fig.subplots_adjust(0,0,1,1)
    ax.set(xlim=(0,1900),ylim=(height,0));ax.axis('off');fig.patch.set_facecolor('#fbfcfe')
    text(ax,42,44,'B+ TREE  /  EXPERIMENT ATLAS',11,color='#61738b',weight='bold')
    text(ax,42,94,title,27,weight='bold')
    text(ax,42,136,subtitle,12,color='#61738b')
    x=42
    for name in ['Parked','Rejected','Approved']:
        text(ax,x,183,f'{counts[name]:02d}  {name.upper()}',14,color=COLORS[name],weight='bold');x+=240
    return fig,ax


def save(fig,name):
    for suffix in ['png','svg']:
        target = HERE/f'{name}.{suffix}'
        metadata = {'Date': None} if suffix == 'svg' else {}
        fig.savefig(target,dpi=140,facecolor=fig.get_facecolor(),metadata=metadata)
        if suffix == 'svg':
            target.write_text('\n'.join(line.rstrip() for line in target.read_text().splitlines())+'\n')
    plt.close(fig)


def overview(records):
    counts=collections.Counter(r['status'] for r in records)
    height=390+len(records)*17+26*(len({r['host'] for r in records})-1)
    fig,ax=canvas(height,f'{len(records)} experiment attempts. Zero approved.',
        'Architecture → measured host → decision  ·  includes populations, replications and qualification attempts',counts)
    for x,label in [(85,'ARCHITECTURE'),(590,'MEASURED HOST'),(1470,'OUTCOME')]:
        text(ax,x,246,label,10,color='#61738b',weight='bold')
    unit=17
    hosts=list(dict.fromkeys(r['host'] for r in records))
    groups={h:[r for r in records if r['host']==h] for h in hosts}
    y=280;host_y={}
    for host,rs in groups.items():host_y[host]=y;y+=len(rs)*unit+26
    arch_y={};y=280
    for arch in ARCH_COLORS:
        rs=[r for r in records if r['architecture']==arch]
        arch_y[arch]=y;y+=len(rs)*unit+42
    dest_y={};next_y=280
    for status in COLORS:
        if counts[status]:
            dest_y[status]=next_y;next_y+=counts[status]*unit+52
    aoff=collections.Counter();doff=collections.Counter()
    for host,rs in groups.items():
        arch=rs[0]['architecture'];h=len(rs)*unit
        ribbon(ax,275,arch_y[arch]+aoff[arch],655,host_y[host],h,ARCH_COLORS[arch],.27)
        aoff[arch]+=h
        off=0
        for status in ['Parked','Rejected','Approved']:
            n=sum(r['status']==status for r in rs)
            if not n:continue
            ribbon(ax,671,host_y[host]+off,1480,dest_y[status]+doff[status],n*unit,COLORS[status],.27)
            doff[status]+=n*unit;off+=n*unit
        node(ax,655,host_y[host],h,ARCH_COLORS[arch])
        text(ax,690,host_y[host]+h/2,f'{host}  ·  {len(rs)}',13,weight='bold',bbox=dict(facecolor='#fbfcfe',edgecolor='none',pad=4))
    for arch in ARCH_COLORS:
        n=sum(r['architecture']==arch for r in records);h=n*unit
        node(ax,259,arch_y[arch],h,ARCH_COLORS[arch])
        text(ax,235,arch_y[arch]+h/2,f'{arch}  ·  {n}',17,ha='right',weight='bold')
    for status,y in dest_y.items():
        node(ax,1480,y,counts[status]*unit,COLORS[status])
        text(ax,1520,y+counts[status]*unit/2,f'{status}  ·  {counts[status]}',18,color=COLORS[status],weight='bold')
    text(ax,42,height-47,'22 new populations + 5 replications + 6 qualification attempts. Shared Apple history counted once.',11,color='#61738b')
    text(ax,42,height-21,'Source decisions through 19 Oct 2026  ·  Snapshot 20 Oct 2026  ·  Passed tests and merged harnesses are not approved optimizations.',10,color='#61738b')
    save(fig,'overview')


def detailed(records,name,title):
    host_order=['Apple M1','Apple M6','AWS Graviton','AWS Intel','AWS AMD']
    records=sorted(records,key=lambda r:host_order.index(r['host']))
    arches=[a for a in ARCH_COLORS if any(r['architecture']==a for r in records)]
    heights={a:max(210,48*sum(r['architecture']==a for r in records)+65) for a in arches}
    total=290+sum(heights.values())
    counts=collections.Counter(r['status'] for r in records)
    fig,ax=canvas(total,title,'One ribbon per attempt  ·  POP = new population  ·  REP = replication  ·  AA = qualification  ·  P → R = parked then rejected',counts)
    for x,label in [(30,'ARCHITECTURE'),(320,'HOST'),(815,'EXPERIMENT'),(1630,'OUTCOME')]:
        text(ax,x,231,label,10,color='#61738b',weight='bold')
    top=260;unit=14
    for arch in arches:
        rs=[r for r in records if r['architecture']==arch];height=heights[arch]
        cy=top+height/2-15;ay=cy-len(rs)*unit/2
        groups={host:[r for r in rs if r['host']==host] for host in dict.fromkeys(r['host'] for r in rs)}
        rows={r['id']:top+25+i*48 for i,r in enumerate(rs)}
        stat=collections.Counter(r['status'] for r in rs)
        statuses=[s for s in ['Parked','Rejected','Approved'] if stat[s]]
        status_y={};dy=cy-(len(rs)*unit+50*(len(statuses)-1))/2
        for s in statuses:status_y[s]=dy;dy+=stat[s]*unit+50
        offsets=collections.Counter();aoff=0
        for host,items in groups.items():
            hy=(rows[items[0]['id']]+rows[items[-1]['id']]+unit)/2-len(items)*unit/2
            ribbon(ax,205,ay+aoff,530,hy,len(items)*unit,ARCH_COLORS[arch],.24);aoff+=len(items)*unit
            for i,r in enumerate(items):
                ey=rows[r['id']];status=r['status'];sy=status_y[status]+offsets[status]
                ribbon(ax,546,hy+i*unit,1170,ey,unit,COLORS[status],.12)
                ribbon(ax,1186,ey,1640,sy,unit,COLORS[status],.22)
                offsets[status]+=unit;node(ax,1170,ey,unit,COLORS[status])
                label=r['label']
                if len(r['history'])>1:label+='  [P → R]'
                text(ax,1150,ey+unit/2,label,12,ha='right',bbox=dict(facecolor='#fbfcfe',edgecolor='none',pad=2))
                tag={'population':'POP','replication':'REP','qualification':'AA'}[r['attempt_type']]
                text(ax,560,ey+unit/2,tag+' · '+r['id'],7,color='#61738b',bbox=dict(facecolor='#fbfcfe',edgecolor='none',pad=1))
            node(ax,530,hy,len(items)*unit,ARCH_COLORS[arch])
            text(ax,510,hy+len(items)*unit/2,f'{host}\n{len(items)} records',12,ha='right',bbox=dict(facecolor='#fbfcfe',edgecolor='none',pad=3))
        node(ax,189,ay,len(rs)*unit,ARCH_COLORS[arch])
        text(ax,166,cy,f'{arch}\n{len(rs)}',18,ha='right',weight='bold')
        for s,y in status_y.items():
            node(ax,1640,y,stat[s]*unit,COLORS[s]);text(ax,1672,y+stat[s]*unit/2,f'{s}\n{stat[s]}',14,color=COLORS[s],weight='bold')
        ax.plot([30,1845],[top+height-10]*2,color='#e4eaf1',lw=.8)
        top+=height
    text(ax,40,total-17,'Approved = adopted source optimization. Historical decisions retain their own host/source scope. Evidence links and reasons: README.md / experiments.json.',10,color='#61738b')
    save(fig,name)


def main():
    records=DATA['records'];assert len({r['id'] for r in records})==len(records)
    for r in records:
        assert hashlib.sha256((ROOT/r['source']).read_bytes()).hexdigest()==r['source_sha256'],r['id']
        assert r['status'] in COLORS
        if r['parent']:assert r['parent'] in {x['id'] for x in records}
    populations=[r for r in records if r['kind']=='population']
    followups=[r for r in records if r['kind']=='followup']
    assert collections.Counter(r['status'] for r in populations)=={'Rejected':13,'Parked':9}
    assert collections.Counter(r['architecture'] for r in populations)=={'ARM':16,'Intel':2,'AMD':4}
    assert collections.Counter(r['status'] for r in records)=={'Rejected':16,'Parked':17}
    assert collections.Counter(r['architecture'] for r in records)=={'ARM':24,'Intel':4,'AMD':5}
    overview(records)
    detailed(records,'all-attempts','All 33 experiment attempts, by architecture')
    detailed(populations,'all-populations','All 22 candidate populations, by architecture')
    for arch in ARCH_COLORS:
        detailed([r for r in records if r['architecture']==arch],arch.lower(),f'{arch} · all experiment attempts')
    detailed(followups,'followups','11 replications and qualification attempts · separate count')
    audit={'source_commit':DATA['source_commit'],'attempt_count':len(records),'attempt_statuses':dict(collections.Counter(r['status'] for r in records)),
           'attempts_by_architecture':dict(collections.Counter(r['architecture'] for r in records)),
           'attempt_types':dict(collections.Counter(r['attempt_type'] for r in records)),'population_count':len(populations),'population_statuses':dict(collections.Counter(r['status'] for r in populations)),
           'followup_count':len(followups),'followup_statuses':dict(collections.Counter(r['status'] for r in followups)),
           'verified_evidence_sha256':len(records),'unique_ids':True,'valid_parent_links':True,
           'flow_conservation':'Each record contributes one unit at every layer; grouped node widths are exact record sums.',
           'generated_assets':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(HERE.iterdir()) if p.suffix in ('.svg','.png')}}
    (HERE/'VALIDATION.json').write_text(json.dumps(audit,indent=2)+'\n')
    print(json.dumps({k:v for k,v in audit.items() if k!='generated_assets'},indent=2))

if __name__=='__main__':main()
