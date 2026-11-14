/* Correctness-only link guard. Never link this into a fleet measurement ELF. */
#define _POSIX_C_SOURCE 200809L
#include <time.h>
#include <stdlib.h>
int __wrap_clock_gettime(clockid_t clock, struct timespec *time) {
    (void)clock; (void)time;
    abort();
}
