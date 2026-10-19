# Proposal A — count-one scalar path

Sequential proposal pass1 by one native Codex worker; model variant and measured token cost unknown. The B bulk control spends40.03% of cycle samples in the outlined policy, including35.72% in bulk geometry, for count1. The identical-output scalar root adapter has no policy call in its generated hot loop.

Hypothesis: dispatch only count==1 to the existing scalar decoder, retaining the frozen B algorithm for count2+, reduces width60/forward/count1 elapsed time by at least2%. This can bypass geometry dispatch and loop setup. Exact bits, signed zero, empty and partial ranges must remain unchanged. Guard every width/orientation and count2+. A speedup is conditional on experimental B; no root or public-iterator claim follows.
