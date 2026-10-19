#include "server.h"
#include <string.h>
int main(int argc, char **argv) {
    if (argc != 2) return 2;
    if (!strcmp(argv[1], "assert")) {
        serverAssert(0);
    } else if (!strcmp(argv[1], "panic")) {
        serverPanic("contract probe panic");
    } else return 2;
    fputs("AFTER_PANIC\n", stderr);
    return 99;
}
