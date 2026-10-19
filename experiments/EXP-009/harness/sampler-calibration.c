#define _DARWIN_C_SOURCE 1
#include "server.h"
#include <inttypes.h>
#include <string.h>
#include "sampler.h"
__attribute__((noinline)) uint64_t sampler_probe(uint64_t n) {
    volatile uint64_t x = 1;
    for (uint64_t i=0;i<n;i++) x=x*UINT64_C(1664525)+UINT64_C(1013904223);
    return x;
}
int main(void) {
    sample_init();sample_start();
    volatile uint64_t result=sampler_probe(UINT64_C(200000000));
    sample_stop("sampler_probe");
    printf("result,%" PRIu64 "\n",result);
    return 0;
}
