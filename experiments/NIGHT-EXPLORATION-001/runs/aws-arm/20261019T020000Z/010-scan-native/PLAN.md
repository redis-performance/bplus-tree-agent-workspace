# Native ARM all-match investigation: fixed fresh controls

Profile009 atc9664ab44 supplies the immutable original-code evidence. This phase is
baseline A/A only, before any candidate or implementation. Source8fab511e; original
uninstrumented bench/microbench.c, compat and vendor frozen. Fresh100K/1M SCAN,16bytes,
5M requested operations, held-outseeds101/102/103 twice, six same-binary ABBA blocks
per size (48processes). Alternate size order byblock.5M is chosen BEFORE A/A for
longerwindows and consistency with Intel's independent replication protocol; no
observation from this new A/A can change operationcount, seeds, repeats or durations.

Every block must have absolute paired ns/actual emittedoperation effect<=1%, minimum
window>=10ms, exact checksum/callbackcount/treebytes identity and CPU2 observations.
Both primaries must qualify. OriginalSCAN permits legitimate duplicatecallbacks; use
actualemittedoperations and preserve requestedops separately. Preserve everyrawrow,
serial start/end timestamps and partial prefixes. No retry, adaptive counts, exclusions
or metric substitutions. Fixed300second AAphase, with subprocess timeout bounded by
remainingphasebudget. A failed/incomplete control meansPARK for later acceptance.

A separate60second bounded leasejob builds exact isolatedbaseline fromgitarchive8fab511e,
using originalMakefile CC=clang BUILD=build OPT=-O3 build/btree-bench. Later candidates
must compile in own isolatedsnapshot with IDENTICAL relative source/include/outputpaths,
flags, hash, allocator and assertions. Profileexecutables are never timingcontrols.
Recordtree/header/referee/compat/vendor/compiler/binary/driverhashes beforeAA; root's
requested48processschedule isfixed. Timingjobs serialCPU2 viaexistingleasehelper.

This is distinct nativeARMinvestigation, not adoption of x86SSE2. No candidate or new
measuredpopulation yet. Root coordinates actualthreeproposals/chair and isolatedthree
implementations only aftercommonpacket/evidence review. Actualparticipant/root/aws_arm,
nativeCodexbackend; exactservingmodel, measuredtokens and monetarycostunknown.
