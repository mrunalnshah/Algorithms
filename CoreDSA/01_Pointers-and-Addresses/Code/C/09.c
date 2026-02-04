#include <stdio.h>

int main(){
    int a = 1025;
    int* p;

    p = &a;

    printf("size of integer is %lu\n", sizeof(int));
    printf("address = %p, value = %d\n\n",p, *p);

    char* pc;
    pc = (char*) p; // typecasting

    printf("size of char is %lu\n", sizeof(char));
    printf("address = %p, value = %d\n\n",pc, *pc);
    // Why its 1?
    // 1025 = 00000000 00000000 00000100 00000001

    return 0;
}