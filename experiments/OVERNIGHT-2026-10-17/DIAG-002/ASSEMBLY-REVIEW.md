# Assembly check before timing

Build, release smoke and ASan/UBSan smoke passed. The first inspection script exited1
because it assumed the dependent chain would use x0. Preserved emitted assembly shows
Clang chose x8 instead: eight `add x8,x8,#1`, an independent x9 loop counter increment,
compare and conditional branch. No load/store in the loop. The register-specific
inspector was wrong; no source or fixture change made. Corrected inspection matches
any single register used by all eight adds. This is a validation-script correction
before any measurement, not a relaxed benchmark criterion. Frequency remains unknown.
