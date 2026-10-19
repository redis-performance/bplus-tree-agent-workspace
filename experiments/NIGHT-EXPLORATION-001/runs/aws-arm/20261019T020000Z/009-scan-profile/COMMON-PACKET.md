# Original ARM all-match SCAN evidence packet

Baseline8fab511e, tree SHA256d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2,
header496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83. NeoverseV2,
Clang18.1.3, unchanged-O3/assertions/hash/allocator and original16-byte fixtures. Six
baseline captures:100K/1M × seeds1/2/3, requested1M SCAN operations per process. The
bounded180s CPU2 job completed in20.4s; all workloads serial. No changed operation
counts, candidate, new optimization population or A/A trial. Raw perfdata remains on
runner with committedSHA256; samples/reports and exactsource-linkedassembly are public.

The exact existing AMD FIFO-scoped diagnostic only adds enable/disable commands around
the original elapsed window. It includes small control/clock edges. One disabled perf
control reports no counted events. All six original/disabled/profile outputs match
actualcallbacks, checksum, treebytes, traversals, fixture/seed/warmup fields. Both CPU
observations are2 in all18processes. This is not a timing or causal speedup claim.

The physical symbol is zbtIndexScanSlot; zbtLeafTagMatches is inlined. Exact half-open
relative ranges[0x1bc,0x238) and[0x294,0x540) cover all-match processing including local
pointer/loop setup, but exclude the earlier leaf-ID assertion, rehash guards, and later
member decode/hash/callback. Codegen parity confirms202 selected instruction encodings
are identical between original and instrumented builds. No SIMD vector-register
instruction occurs in these ranges. Scalar64-bit word comparisons handle8 tags,
then rbit/clz chooses candidate lanes, byte rechecks remove SWAR false positives, and
logical positions are emitted with reversed handling. Residual tags use scalar loops.

Across three seeds,100K has247events: all-match ranges84events/34.459% periodweight,
forward word loop67/26.344%, mask/foldselect38/14.995%, candidate byte recheck12/4.689%,
scalar tails15/7.238%. At1M,330events: all-match85/26.769%, forwardword76/23.792%,
mask/foldselect53/16.866%, recheck8/2.357%, tails6/2.098%. Subranges overlap the all-match
total and must never be added as independent fractions. Sampling/skid and modest event
counts limit precision; these are not instruction cycle costs or exact speed ceilings.
No sampled reversed-word path is not proof of no cost or coverage. Profiles do not
replace a physical census. The dominant forward loop computes both ordinary/folded
masks and uses a tag comparison/select for each8-byte word.

Evidence supports investigating the native all-match mechanism; no implementation is
selected here. A later population could assess exact bounded native-vector matching,
portable exact word masks, or another supported mechanism. Preserve original semantics:
all matches, physical ascending enumeration with logical reversal mapping, folded zero/one,
count0..96, bounded loads/no record overread, endian lane order and untouched fallback.
AArch64 mask extraction/shuffle overhead and dense-output stores may erase any benefit;
no x86 speedup is portable evidence. Dense/folded/external/reversed guards and active
resize semantics are required;007 focused referee establishes only sparse64-member
reversed coverage and no active-resize performance/wideIDs. Original43 tests remain.

This is distinct from002lookup's withdrawn first-match mask attribution and AMD/Intel's
x86SSE2 candidate. The initial index lookup attribution was wrong and remains withdrawn.
Any ARM implementation requires an actual three-proposal/chair process and three isolated
implementations, same-session fixed A/A/ABBA, full qualified guards, independent confirmation
and adversarial review. No candidate or control retries are authorized by this packet.
ChooseNONE if independent review finds the mechanism unsupported. Actual participant
/root/aws_arm; nativeCodex backend; servingmodel, measuredtokens and monetarycost unknown.
