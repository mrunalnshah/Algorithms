#include <stdio.h>

int main(){
    int a;
    int* p;
    p = &a;

    printf("%p\n", p);
    printf("%d\n", *p);

    return 0;
}