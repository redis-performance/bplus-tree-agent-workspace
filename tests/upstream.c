#include "server.h"
#include "testhelp.h"
int __failed_tests;
int __test_num;
int zsetBtreeTest(int argc, char **argv, int flags);
int main(int argc, char **argv) {
    int rc = zsetBtreeTest(argc, argv, 0);
    test_report();
    return rc || __failed_tests;
}
