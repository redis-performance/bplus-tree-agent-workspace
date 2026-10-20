/* Outside the timed region; identical binary for timing and TMA collection. */
#include <signal.h>
#include <stdlib.h>
void sample_begin(void) { if (getenv("BPLUS_PROFILE_STOP")) raise(SIGSTOP); }
void sample_end(void) {}
