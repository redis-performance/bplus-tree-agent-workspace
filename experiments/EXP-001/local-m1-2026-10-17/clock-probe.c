#define _POSIX_C_SOURCE 200809L
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <time.h>
static uint64_t ns(struct timespec t) { return (uint64_t)t.tv_sec*1000000000+t.tv_nsec; }
int main(void) {
    struct timespec a,b,res;
    if (clock_getres(CLOCK_MONOTONIC,&res)) return 1;
    uint64_t minimum=UINT64_MAX,total=0,zero=0;
    for (int i=0;i<100000;i++) {
        if (clock_gettime(CLOCK_MONOTONIC,&a) || clock_gettime(CLOCK_MONOTONIC,&b)) return 1;
        uint64_t d=ns(b)-ns(a);
        total+=d;
        if (!d) zero++;
        else if(d<minimum) minimum=d;
    }
    printf("clock=CLOCK_MONOTONIC\nreported_resolution_ns=%" PRIu64 "\nminimum_nonzero_back_to_back_delta_ns=%" PRIu64 "\nmean_back_to_back_delta_ns=%.3f\nzero_deltas=%" PRIu64 "\npairs=100000\n",ns(res),minimum,total/100000.0,zero);
}
