#include "server.h"
int main(void) {
    const size_t sizes[]={319,320,321};
    puts("requested_bytes,min_usable_bytes,max_usable_bytes,repetitions");
    for (size_t i=0;i<sizeof(sizes)/sizeof(*sizes);i++) {
        size_t minimum=SIZE_MAX,maximum=0;
        for (int j=0;j<100;j++) {
            size_t usable;
            void *p=zmalloc_usable(sizes[i],&usable);
            if (usable<minimum) minimum=usable;
            if (usable>maximum) maximum=usable;
            zfree(p);
        }
        printf("%zu,%zu,%zu,100\n",sizes[i],minimum,maximum);
    }
}
