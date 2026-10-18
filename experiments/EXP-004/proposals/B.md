# Proposal B — unified nonzero-width score mask

Sequential proposal pass B,not independent agent. Backend/model/token cost unknown.
Same frozen source/profile/qualification/history inputs. Source mask condition bits<64
compiles to mov/lsl/cmp/csinv/and in the baseline iterator;this is already branchless.
An unconditional UINT64_MAX>>(64-bits) inside bits!=0 may remove the compare/select.
Hypothesis:one fewer score-mask instruction gives >=2% score-only benefit and no guards
regress. Exact target zbtScoreLeafScore only. Risk is width0/64 shift UB;retain outer
zero test and exhaustive geometry oracle. No memory change expected. Member/no-output
cases may change via register/layout allocation. Primary must pass unchanged gates;
reject or park on noise. Expected gain small and compiler may produce equal instructions.
Do not claim branch elimination because baseline code already uses conditional select.
This is distinct from public entry dispatch/member outlining previously rejected.
