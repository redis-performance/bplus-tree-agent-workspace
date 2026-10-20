/* Diagnostic-only phase marker. Does not replace a timing referee. */
#include <signal.h>
#include <stdlib.h>
void sample_begin(void) { if (getenv("BPLUS_PROFILE_STOP")) raise(SIGSTOP); }
void sample_end(void) {}
