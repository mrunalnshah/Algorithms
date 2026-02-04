#include <stdio.h>

int main(){
    int a = 1025;
    int* p;

    p = &a;

    printf("size of integer is %lu\n", sizeof(int));
    printf("address = %p, value = %d\n\n",p, *p);

    return 0;
}