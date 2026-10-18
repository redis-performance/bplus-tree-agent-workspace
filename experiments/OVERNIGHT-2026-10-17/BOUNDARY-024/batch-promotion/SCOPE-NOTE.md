# Initial batch recipe scope mismatch

The initial recipe passes actual batched promotion and catches the stale cached-table
fault. A source review found that its lane expression `1+i%2` is evaluated only where
`i%4==1`, so it selects ID2 every time. The plan described IDs1/2; ID1 was not requested
in those batch lanes (it remains checked by the full models). Initial outputs and
snapshots are preserved, including fresh confirmation, without claiming that scope.

Attempt002 changes only this lane selection to `1+(i/4)%2`, alternating IDs1 and2.
All assertions, bounds, score patterns, counts, seeds and source candidates stay the
same. Both matrices and the stale-cache fault run in fresh isolated directories.
This is an explicit fixture correction, not evidence that production failed.
