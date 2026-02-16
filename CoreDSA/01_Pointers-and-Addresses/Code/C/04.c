#include <stdio.h>

int main(){
    int a;
    int* p;
    p = &a;
    a = 10;

    printf("a = %d\n", a);
    *p = 12; // dereferencing
    printf("a = %d\n", a);
 
    return 0;
}