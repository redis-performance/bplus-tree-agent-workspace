# Launcher interruption and retained baseline attempt

At 01:32 UTC the application server restarted while the initial baseline was
connected to its command-output pipe. All seven build/native/sanitizer validations
passed. Four ABBA processes for size 100 completed before the runner hit a broken
stdout pipe while printing progress. Its failed manifest and four raw processes
remain in baseline/. No performance decision is made from this partial attempt.

The replacement attempt uses baseline-attempt002/ and writes stdout/stderr to
ignored scratch files through a detached launcher. Source, flags, seeds and
measurement protocol stay unchanged. This is recovery from an infrastructure
failure, not a retry to improve a measured outcome. LAUNCH-STATUS.json identifies
the selected baseline and durable supervisor/coordinator startup.
