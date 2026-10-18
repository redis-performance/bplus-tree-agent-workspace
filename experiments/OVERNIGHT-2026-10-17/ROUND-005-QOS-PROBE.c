/* Capability preparation only: no benchmark, sleep, affinity or clock estimate. */
#define _DARWIN_C_SOURCE 1
#include <pthread.h>
#include <pthread/qos.h>
#include <stdio.h>
int main(void) {
    qos_class_t before=QOS_CLASS_UNSPECIFIED,after=QOS_CLASS_UNSPECIFIED;
    int rel_before=0,rel_after=0;
    int get_before=pthread_get_qos_class_np(pthread_self(),&before,&rel_before);
    /* One attempt on this short-lived child; no retry if the API rejects it. */
    int set_result=pthread_set_qos_class_self_np(QOS_CLASS_USER_INITIATED,0);
    int get_after=pthread_get_qos_class_np(pthread_self(),&after,&rel_after);
    printf("get_before=%d requested_before=%u rel_before=%d set_user_initiated=%d get_after=%d requested_after=%u rel_after=%d\n",
        get_before,(unsigned)before,rel_before,set_result,get_after,(unsigned)after,rel_after);
    puts("effective_qos=unknown core_type=unknown residency=unknown frequency=unknown");
    return get_before || get_after || set_result;
}
