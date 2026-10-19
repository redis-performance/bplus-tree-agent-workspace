# Exclusive original baseline mask attribution

Read-only analysis of the existing019 baseline samples identifies **word-mask
construction at10.79%/13.68% of timed sampled period** for100K/1M, versus **byte
recheck at5.47%/3.17%** and **position output at2.06%/1.18%**. These categories are
exclusive; each sampled IP is assigned once. No source hypothesis, implementation,
new workload, new profile, or timing was performed.

The exact baseline is869425ed/source13e459ff8. The rebuilt017 baseline disassembly
has the same text as that timing binary.019's already independently audited physical
main return0xe04 filter supplies only timed-call-site samples. PMU capture itself was
full-process; setup/verification/incomplete samples are retained in019 and excluded
here by its frozen scope. Sample-period shares are not elapsed-time savings or a
bound on recoverable work. The macro name `candidate` below refers to approximate
word-mask match positions in the baseline, not an optimization implementation.

| Exclusive category | 100K period | 1M period |
|---|---:|---:|
| Query-pattern setup | 0.16% | 0.06% |
| Word-mask construction, constants and fold selection | 10.79% | 13.68% |
| Word load and address calculation | 1.59% | 0.87% |
| Candidate-position bit extraction | 2.06% | 1.74% |
| Candidate-byte recheck | 5.47% | 3.17% |
| Candidate-position output and found-count update | 2.06% | 1.18% |
| Candidate-mask clear/test/branch control | 6.26% | 4.98% |
| Word-loop increment/test control | 1.59% | 0.81% |
| Scalar tails and their setup | 6.82% | 3.79% |
| Remaining helper pointer/dispatch setup | 0.79% | 1.43% |
| zbtIndexScanSlot outside helper scope | 54.88% | 55.72% |
| Outside zbtIndexScanSlot | 7.53% | 12.56% |

The denominator is1261/1608 timed baseline events (period3528142362/4492641972), pooled
only over the existing three seeds within each size. Per-seed values and raw sampled
IPs remain in per-capture.json and sampled-ips.json. No candidate-B samples are mixed.
Rounding may make displayed totals differ slightly from100%; integer period sums
and event counts close exactly in analyze.py.

## Exact source-linked scope

All-match plus its local setup is exactly209 baseline instructions in half-open ELF
ranges[0x103f8,0x104a0) and[0x104dc,0x10778), relative to physical zbtIndexScanSlot0x10298.
Earlier leaf-ID assertions/resize checks, the count assertion at0x10778 and subsequent
member/score decoding are excluded. exclusive-map.json lists every opcode/address
with its one category. The original source-linked assembly is retained under
../017-corrected-neon/validation/base-native-codegen.stdout and its hash is pinned.

Word-mask math includes the reversed-folded loop at0x10520/0x1052c–0x10540, forward
loop at0x105f8/0x105fc/0x10600 and0x10608–0x10628, and reversed-ordinary loop at0x10698/
0x1069c and0x106a4–0x106b0. Query broadcast setup is separate. Loads and loop branches
are not silently included in that arithmetic category.

Byte rechecks are exact loads/condition tests at0x10564–0x1056c,0x10644 plus0x10650–
0x10664, and0x106d4–0x106dc. Bit extraction (`rbit`/`clz`/position arithmetic) and
position stores/count updates have distinct exclusive maps. Thus a large sample on a
position-output instruction is not counted again as byte recheck or mask construction.
The same separation applies to all three physical-direction/fold word paths.

## What the data does and does not support

The single mask-construction IP0x1060c (`add x1,x0,x2`) carries6.03%/10.20% of timed
period. This is ordinary mask subtraction expressed as addition, not exclusively the
optional folded-zero path. Its large sampled share does not establish that a simple
add itself consumes those cycles; load dependencies and sampling skid can matter.
Likewise, recheck IP0x10658 (`cset w2,eq`) carries3.57%/2.30%, but that is a sampled
location, not a precise standalone instruction cost.

A transparent nested subset identifies the forward folded-zero construction/selection
IPs0x105fc,0x10610,0x10618,0x10620,0x10624,0x10628:3.014%/1.989% (38/32 events).
This subset is already inside word-mask construction and must not be added to it.
It shows why treating the entire10.79–13.68% as optional folded work would overstate
the evidence. It is a small sample, not proof of zero cost elsewhere or a hard speed
limit. No conclusion about a winning portable transformation follows automatically.

021's chair chose NONE before implementation: a proposed static gate and~17% sampled
predicate share did not establish enough support to overcome017's prior55–79% B
losses. That decision and all rejected017/fresh020 evidence remain final. This022
baseline diagnosis is additional evidence only. Runner remained idle. Actual author
/root/aws_arm; exact model and measured costs unknown.
