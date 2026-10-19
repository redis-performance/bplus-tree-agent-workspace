#define _GNU_SOURCE 1
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>
#include <unistd.h>
extern char __executable_start, etext;
static unsigned short *histogram;
static size_t bins;
static uintptr_t base;
static struct itimerval timer;
static uint64_t cpu_start;
static uint64_t cpu_ns(void) {
    struct timespec t;assert(!clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&t));
    return (uint64_t)t.tv_sec*1000000000+(uint64_t)t.tv_nsec;
}
void sample_begin(void) {
    assert(!histogram);base=(uintptr_t)&__executable_start;
    bins=((uintptr_t)&etext-base+1)/2;
    histogram=calloc(bins,sizeof(*histogram));assert(histogram);
#ifndef SAMPLE_DISABLED
    assert(!profil(histogram,bins*sizeof(*histogram),base,65536));
    assert(!getitimer(ITIMER_PROF,&timer));
    assert(timer.it_interval.tv_sec || timer.it_interval.tv_usec);
#endif
    cpu_start=cpu_ns();
}
void sample_end(void) {
    uint64_t cpu_elapsed=cpu_ns()-cpu_start;
    assert(!profil(histogram,0,base,0));
    uint64_t interval=(uint64_t)timer.it_interval.tv_sec*1000000000+(uint64_t)timer.it_interval.tv_usec*1000;
    /* Every child is separately capped120s. Also prove the observed CPU duration
     * cannot produce enough timer events to wrap one16-bit histogram bin. */
    assert(!interval || cpu_elapsed/interval+4<65535);
    unsigned long long samples=0;unsigned maximum=0;
    const char *out=getenv("SAMPLE_OUT");assert(out);
    FILE *f=fopen(out,"w");assert(f);fprintf(f,"offset,count\n");
    for(size_t i=0;i<bins;i++)if(histogram[i]) {
        assert(histogram[i]<65535);samples+=histogram[i];
        if(histogram[i]>maximum)maximum=histogram[i];
        fprintf(f,"%zu,%u\n",2*i,histogram[i]);
    }
    assert(!fclose(f));
    fprintf(stderr,"SAMPLER text_offset_start=0 text_offset_end=%zu scale=65536 bin_bytes=2 bins=%zu interval_ns=%llu cpu_elapsed_ns=%llu captured=%llu max_bin=%u disabled=%d\n",
            (size_t)((uintptr_t)&etext-base),bins,(unsigned long long)interval,(unsigned long long)cpu_elapsed,samples,maximum,
#ifdef SAMPLE_DISABLED
            1
#else
            0
#endif
    );
    free(histogram);histogram=NULL;
}
#ifdef SAMPLE_SELF_TEST
__attribute__((noinline)) static uint64_t known_work(uint64_t x) {
    for(uint64_t i=0;i<500000000;i++){x^=x>>17;x*=0xd6e8feb86659fd93ULL;}
    return x;
}
int main(void){sample_begin();uint64_t x=known_work(19);sample_end();printf("%llu\n",(unsigned long long)x);}
#endif
