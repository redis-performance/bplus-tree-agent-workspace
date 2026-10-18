# Pre-timing audit correction

The first caller audit incorrectly ended at the last textual return instruction;
Clang places additional mask-specific blocks after that shared epilogue. Corrected
audit includes every instruction through the next function label. Iterator retains
its terminal-return cutoff solely to exclude padding. The initial120instruction
caller audit is preserved; no measurements started before the corrected full audit.
