#define _POSIX_C_SOURCE 200809L
#include <float.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include "zset_btree.c"

static uint64_t random_state=0x8e1174ad;
static uint64_t next_random(void) {
    random_state ^= random_state << 13;
    random_state ^= random_state >> 7;
    return random_state ^= random_state << 17;
}
static int bytes_compare(const unsigned char *a,size_t an,const unsigned char *b,size_t bn) {
    int c=memcmp(a,b,an<bn?an:bn);
    return c?c:(an>bn)-(an<bn);
}
static unsigned int oracle(zbtScoreLeaf *leaf,double score,const unsigned char *key,size_t len) {
    for (unsigned int i=0;i<leaf->n.count;i++) {
        double s=zbtScoreLeafScore(leaf,i);
        if(s>score)return i;
        if(s==score) {
            size_t n;const unsigned char *p=zbtScoreLeafElement(leaf,i,&n);
            if(bytes_compare(p,n,key,len)>=0)return i;
        }
    }
    return leaf->n.count;
}
int main(int argc,char **argv) {
    if(argc>1)random_state=strtoull(argv[1],NULL,10);
    uint8_t hashseed[16];for(size_t i=0;i<16;i++)hashseed[i]=(uint8_t)next_random();
    dictSetHashFunctionSeed(hashseed);
    uint64_t checks=0,leaves=0,reversed=0;
    for(int mode=0;mode<5;mode++)for(int direction=0;direction<3;direction++)for(int lengths=0;lengths<4;lengths++) {
        enum {N=257};sds keys[N];double scores[N];unsigned int order[N];
        size_t lengths_set[]={8,16,320,321};size_t bytes=lengths_set[lengths];
        for(unsigned int i=0;i<N;i++) {
            char buf[321];memset(buf,'a',bytes);for(int j=0;j<8;j++)buf[j]=(unsigned char)((uint64_t)i>>(j*8));
            keys[i]=sdsnewlen(buf,bytes);order[i]=i;
            if(mode==0)scores[i]=(double)i*4;
            else if(mode==1)scores[i]=(double)(i%7);
            else if(mode==2)scores[i]=i%2?-0.0:0.0;
            else if(mode==3)scores[i]=ldexp((double)(i+1),i%200-100)*(i%2?-1:1);
            else {double edge[]={-DBL_MAX,-DBL_MIN,-0.0,0.0,DBL_MIN,DBL_MAX};scores[i]=edge[i%6];}
        }
        if(direction==1)for(unsigned int i=0;i<N;i++)order[i]=N-i-1;
        if(direction==2)for(unsigned int i=N;i>1;i--){unsigned int j=next_random()%i,t=order[i-1];order[i-1]=order[j];order[j]=t;}
        zbtreeSet *tree=zbtreeCreate();
        for(unsigned int i=0;i<N;i++) {
            unsigned int k=order[i];zbtreeInsertPosition p;double old;
            serverAssert(!zbtreeFindForAdd(tree,keys[k],&old,&p));zbtreeInsertNew(tree,scores[k],keys[k],&p);
        }
        for(zbtScoreLeaf *leaf=tree->score_first;leaf;leaf=leaf->next) {
            leaves++;reversed+=leaf->reversed;
            for(unsigned int i=0;i<N;i++) {
                double query[]={scores[i],nextafter(scores[i],-INFINITY),nextafter(scores[i],INFINITY),-0.0,0.0};
                for(unsigned int v=0;v<5;v++) {
                    if(!isfinite(query[v]))continue;
                    size_t querylens[]={0,1,sdslen(keys[i])/2,sdslen(keys[i])};
                    for(unsigned int q=0;q<4;q++) {
                        unsigned int got=zbtScoreLeafLowerBound(leaf,query[v],(unsigned char*)keys[i],querylens[q]);
                        unsigned int want=oracle(leaf,query[v],(unsigned char*)keys[i],querylens[q]);
                        serverAssert(got==want);checks++;
                    }
                }
            }
        }
        for(unsigned int i=0;i<N;i++){double s;serverAssert(zbtreeScore(tree,keys[i],&s));serverAssert(!memcmp(&s,&scores[i],sizeof(s)));sdsfree(keys[i]);}
        zbtreeFree(tree);
    }
    printf("checks=%llu leaves=%llu reversed=%llu\n",(unsigned long long)checks,(unsigned long long)leaves,(unsigned long long)reversed);
    serverAssert(reversed>0);
    return 0;
}
