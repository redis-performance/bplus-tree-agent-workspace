"""Apply a retained one-file unified patch exactly; never edits a shared checkout."""
import re

def apply(original, patch):
    lines=original.splitlines(keepends=True);p=patch.splitlines(keepends=True)
    assert p[0].strip()=='--- a/src/zset_btree.c' and p[1].strip()=='+++ b/src/zset_btree.c'
    out=[];cursor=0;i=2
    while i<len(p):
        m=re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',p[i]);assert m,p[i]
        start=int(m[1])-1;assert start>=cursor;out+=lines[cursor:start];cursor=start;i+=1;old=new=0
        while i<len(p) and not p[i].startswith('@@ '):
            kind=p[i][0];text=p[i][1:];assert kind in ' +-'
            if kind in ' -':assert lines[cursor]==text,(cursor,p[i]);cursor+=1;old+=1
            if kind in ' +':out.append(text);new+=1
            i+=1
        assert old==int(m[2] or 1) and new==int(m[4] or 1)
    out+=lines[cursor:];return ''.join(out)
