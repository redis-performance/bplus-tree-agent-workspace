# Fresh original-delete controls:100K qualifies,1M fails

Fixed48serial processes complete03:43:16–03:43:58UTC. Original frozen delete case, sizes100K/1M, requested1Mops but actual=size,16byte members,seeds1/2/3 each twice, six ABBA blocks. Original baseline binary, CPU2, same checksum/operations/tree-owned bytes within every block. No retry, row exclusion or operation adjustment.

100K effects+0.603,+0.299,+0.145,+0.622,−0.631,+0.742%; minimum21.876ms. Qualified≤1%absolute blocks and≥10ms windows.

1M effects+0.527,+0.520,+0.499,+4.682,+3.035,+1.087%; minimum592.847ms. FAILED precision gate. This noise approaches the nominal5.496% offset-loop sample share. All rows/process metadata retained; wall/thread descriptive comparison is separate and does not change the metric or qualification.

No candidate exists. Chair may chooseNONE on insufficient measurement precision/headroom; any exploratory implementation could not qualify adoption. No source adoption overnight.
