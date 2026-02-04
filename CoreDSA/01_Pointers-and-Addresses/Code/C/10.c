#include <stdio.h>

int main(){
    int a = 1025;
    int* p;

    p = &a;

    printf("size of integer is %lu\n", sizeof(int));
    printf("address = %p, value = %d\n",p, *p);
    printf("address = %p, value = %d\n\n",p+1, *(p+1));

    char* pc;
    pc = (char*) p; // typecasting

    printf("size of char is %lu\n", sizeof(char));
    printf("address = %p, value = %d\n",pc, *pc);
    printf("address = %p, value = %d\n\n",pc+1, *(pc+1)); // 4 because 100 in byte 1

    return 0;
}