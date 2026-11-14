/* Compile/disassemble only. This file must never be executed locally. */
#define _POSIX_C_SOURCE 200809L
#include <time.h>
int main(void) { struct timespec value; return clock_gettime(CLOCK_MONOTONIC,&value); }
