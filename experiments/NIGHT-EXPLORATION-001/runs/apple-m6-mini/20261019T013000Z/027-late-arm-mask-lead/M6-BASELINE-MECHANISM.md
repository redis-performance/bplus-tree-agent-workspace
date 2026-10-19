# Retained M6 baseline mask window

The original mask-selection path exists in the retained corrected-adapter M6 baseline. This is a read-only observation of the already validated native binary and its saved disassembly.

The unique IteratorNext body has 114 static instructions. Its symbol-relative window is:

```asm
+0x100  mov    x13, #-0x1
+0x104  lsl    x14, x13, x11
+0x108  cmp    w11, #0x40
+0x10c  csinv  x11, x13, x14, hs
+0x110  and    x11, x12, x11
```

These five lines include the constant load and final AND. The compare/select handles the original width-64 special case. The source's outer `bits != 0` guard remains present. The historical patch replaces the conditional mask expression inside that guard; it has not been compiled or measured on M6 here.

No sampled cycle cost, removable fraction or gain follows from this window. Prior PC locations are not reassigned across binaries. Patched local codegen, fresh qualified controls and all validation and acceptance gates remain future work under a new plan. No candidate is selected, and no native workload or build ran for this report. File and binary identities are in the adjacent JSON.
