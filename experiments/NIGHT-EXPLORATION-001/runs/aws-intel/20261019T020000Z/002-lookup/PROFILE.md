# Profile and qualification

Six whole-process gprof captures use a separate -pg binary (20millionqueries/cell). At100K successful queries zbtScoreLeafFindMember accounts for38.66% sampled self time, at1M31.66%. These are instrumented executable-profile shares including setup/warmup/destruction and limited shared-library visibility, not unbiased timed-loop shares. Release assembly retains a memchr PLT call inside this function. PMU perf stat failed at perf_event_paranoid4; failure retained, no permission changes or privileged retry.

Six-cell A/A:100K hit(-0.643..+0.140%) and1M miss(-0.247..+0.258%) pass all six±1%blocks.10K hit(-2.594..+0.436),1M hit(-0.293..+1.458),10K miss(-2.825..+2.789),100K miss(-0.980..+1.068) fail. All144raw rows retained. At least one primary is unqualified, so exploratory screen only.

Transfer note: initial rsync archive-mode attempted group metadata on existing root-owned service logs and failed. No permission changes or retry of group ownership; later transfers omit ownership metadata and exclude remote service logs on upload. Experimental jobs were unaffected. Raw gmon artifacts stay on runner; hashes and text reports are public.
