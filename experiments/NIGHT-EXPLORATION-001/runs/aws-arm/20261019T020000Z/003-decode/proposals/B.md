# Proposal B — inline the bulk policy

Sequential proposal pass2 by the same worker; not independent. Hypothesis: forcing policy inlining removes a per-leaf call and improves count1. The profile contains a real call boundary, but expanded geometry can increase code size and harm bulk guards. This changes compiler policy for every count, whereas the count-one fallback targets the observed short range. Rank below A for broader risk and prior outlining sensitivity.
