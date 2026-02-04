#include <stdio.h>

int main(){
    int a = 10;
    int* p;
    p = &a;

    // Pointer Arithmetic
    printf("Address of p is %p\n",p); // p is 2002
    printf("Value at address p is %d\n\n",*p);

    printf("Size of integer is %lu bytes\n\n", sizeof(int)); 

    printf("Address of p + 1 is %p\n",p+1); // p is 2006, why ? p + 1 moves to next integer so its +4 (size of int)
    printf("Value at address p+1 is %d\n\n",*(p+1));

    printf("Address of p + 2 is %p\n",p+2); // p + 8 --> 2 integers moved ahead.
    printf("Value at address p+2 is %d\n\n",*(p+2));

    return 0;
}