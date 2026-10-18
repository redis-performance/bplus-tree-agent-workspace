#define _DARWIN_C_SOURCE 1
#include "server.h"
#include <inttypes.h>
#include <string.h>
#include <time.h>
#include "self_sampler.h"
static uint64_t clock_ns(clockid_t clock) {
    struct timespec ts;serverAssert(clock_gettime(clock,&ts)==0);
    return (uint64_t)ts.tv_sec*UINT64_C(1000000000)+(uint64_t)ts.tv_nsec;
}
__attribute__((noinline)) static uint64_t known_arithmetic(uint64_t count) {
    uint64_t x=0;
    for(uint64_t i=0;i<count;i++) __asm__ volatile(
      "add %0,%0,#1\n\tadd %0,%0,#1\n\tadd %0,%0,#1\n\tadd %0,%0,#1\n\t"
      "add %0,%0,#1\n\tadd %0,%0,#1\n\tadd %0,%0,#1\n\tadd %0,%0,#1\n\t" : "+r"(x));
    return x;
}
int main(int argc,char **argv) {
    serverAssert(argc==2);char *end;uint64_t count=strtoull(argv[1],&end,10);
    serverAssert(*argv[1] && !*end && count>0 && count<=400000000);
    sample_init();
    uint64_t t0=clock_ns(CLOCK_THREAD_CPUTIME_ID),w0=clock_ns(CLOCK_MONOTONIC);
    sample_start();struct itimerval armed;serverAssert(getitimer(ITIMER_PROF,&armed)==0);
    uint64_t result=known_arithmetic(count);
    sample_stop();
    uint64_t wall=clock_ns(CLOCK_MONOTONIC)-w0,thread=clock_ns(CLOCK_THREAD_CPUTIME_ID)-t0;
    unsigned samples=atomic_load_explicit(&sample_count,memory_order_relaxed);
    sample_dump("known_arithmetic");
    serverAssert(result==count*8);
    puts("requested_usec,reported_interval_sec,reported_interval_usec,iterations,checksum,samples,wall_ns,thread_ns");
    printf("%u,%ld,%d,%" PRIu64 ",%" PRIu64 ",%u,%" PRIu64 ",%" PRIu64 "\n",sample_usec,
        armed.it_interval.tv_sec,armed.it_interval.tv_usec,count,result,samples,wall,thread);
}
