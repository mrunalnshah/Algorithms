#include <stdio.h>

int main(){
    int a;
    int* p;
    p = &a;
    a = 10;

    printf("Address stored at p: %p\n", p);
    printf("Value stored at address of p: %d\n", *p);
    printf("Address of a: %p\n", &a);
    printf("Address of p: %p\n", &p);

    return 0;
}