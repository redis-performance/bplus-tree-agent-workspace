# Sequential chair — choose M6-DECODE-COUNT1-001

Choose proposal A, scalar only for count==1. Ranking A > B > C: A uses the
original exact scalar implementation, is directly supported by primary policy PCs
and bounded release call evidence, and avoids duplicating packed-bit semantics.
B has plausible overhead motivation but changes the full-range policy/caller body;
C adds UB/semantic risk without evidence of scalar decoder inefficiency. Neither
alternative enters this comparison. One hypothesis only, no combination.

Missing reverse/bulk profile sufficiency and control precision remain adoption
gaps. No speedup or participant independence inferred. Three proposal passes and
chair were sequential work by one worker, exact model/cost unknown.

Implementation population: A natural early count1 branch; B inline small policy
plus noinline bulk bridge; C forced-inline policy with early bulk return. All three
call the original scalar only at count1 and byte-identical frozen B otherwise.
No mutable sources/builds shared. Assertions/hash/allocator/compiler flags identical.
Cached published M1 4c48fa7e has no candidate, and is context only. M6 leads.
