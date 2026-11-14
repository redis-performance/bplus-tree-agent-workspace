/* Applied identically to baseline/B; reaching a benchmark clock is a failure. */
#define _POSIX_C_SOURCE 200809L
#include <time.h>
#include <stdlib.h>
int __wrap_clock_gettime(clockid_t clock_id, struct timespec *result) {
    (void)clock_id; (void)result;
    abort();
}
