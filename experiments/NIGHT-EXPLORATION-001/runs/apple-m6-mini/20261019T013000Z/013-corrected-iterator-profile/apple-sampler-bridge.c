/* Profiler bridge only: frozen iterator/referee files remain byte-identical. */
#define _GNU_SOURCE 1
#define _DARWIN_C_SOURCE 1
#define _POSIX_C_SOURCE 200809L
#include "server.h"
#include <inttypes.h>
#include <string.h>
#include "../002-rank/night-rank-sampler.h"
void sample_begin(void) {
    static int initialized;
    if (!initialized) { sample_init(); initialized = 1; }
    sample_start();
}
void sample_end(void) { sample_stop("iterator-existing-profile-hooks"); }
