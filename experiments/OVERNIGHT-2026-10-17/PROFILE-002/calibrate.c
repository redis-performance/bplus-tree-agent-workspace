#define _DARWIN_C_SOURCE 1
#include "server.h"
#include <inttypes.h>
#include <string.h>
#include "self_sampler.h"
__attribute__((noinline)) static uint64_t known_arithmetic(uint64_t count) {
    uint64_t x=0;
    for(uint64_t i=0;i<count;i++) __asm__ volatile(
      "add %0,%0,#1\n\tadd %0,%0,#1\n\tadd %0,%0,#1\n\tadd %0,%0,#1\n\t"
      "add %0,%0,#1\n\tadd %0,%0,#1\n\tadd %0,%0,#1\n\tadd %0,%0,#1\n\t" : "+r"(x));
    return x;
}
int main(void) {
    sample_init(); sample_start();
    uint64_t result=known_arithmetic(200000000);
    sample_stop("known_arithmetic");
    serverAssert(result==UINT64_C(1600000000));
    printf("checksum=%" PRIu64 "\n",result);
}
