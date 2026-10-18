/* Diagnostic capacity policy only; never a timing/referee replacement. */
typedef union { max_align_t align; struct { size_t capacity; uint64_t magic; } meta; } alloc_header;
static const uint64_t alloc_magic=UINT64_C(0x6170706c79636170);
static size_t outstanding;
static size_t capacity_for(size_t size) {
    size_t n=size?size:1;
    serverAssert(n<=SIZE_MAX-(CAPACITY_QUANTUM-1)-sizeof(alloc_header));
    return (n+CAPACITY_QUANTUM-1)/CAPACITY_QUANTUM*CAPACITY_QUANTUM;
}
size_t zmalloc_usable_size(void *ptr) {
    if(!ptr)return 0;
    alloc_header *h=(alloc_header *)ptr-1;
    serverAssert(h->meta.magic==alloc_magic);return h->meta.capacity;
}
void *zmalloc(size_t size) {
    size_t capacity=capacity_for(size);
    alloc_header *h=malloc(sizeof(*h)+capacity);serverAssert(h);
    h->meta.capacity=capacity;h->meta.magic=alloc_magic;outstanding++;
    return h+1;
}
void *zcalloc(size_t size) {
    void *p=zmalloc(size);memset(p,0,zmalloc_usable_size(p));return p;
}
void zfree(void *ptr) {
    if(!ptr)return;
    alloc_header *h=(alloc_header *)ptr-1;
    serverAssert(h->meta.magic==alloc_magic && outstanding);
    h->meta.magic=0;outstanding--;free(h);
}
void *zmalloc_usable(size_t size,size_t *usable) {
    void *p=zmalloc(size);*usable=zmalloc_usable_size(p);return p;
}
void *zrealloc_usable(void *ptr,size_t size,size_t *usable,size_t *old_usable) {
    *old_usable=zmalloc_usable_size(ptr);
    void *p=zmalloc_usable(size,usable);
    if(ptr)memcpy(p,ptr,*old_usable<*usable?*old_usable:*usable);
    zfree(ptr);return p;
}
void zfree_usable(void *ptr,size_t *usable) {*usable=zmalloc_usable_size(ptr);zfree(ptr);}
size_t diagnostic_outstanding(void) {return outstanding;}
