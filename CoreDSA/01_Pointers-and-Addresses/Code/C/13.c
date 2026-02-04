#include <stdio.h>

int main() {
    int x = 5;
    int* p = &x;
    *p = 6;

    int** q = &p;
    int*** r = &q;

    printf("*p is %p\n", p); // Address of pointer p 
    printf("*p is %d\n\n", *p); // Value at address stored in p // 6
    
    printf("q is %p\n", q); // Address of pointer q
    printf("*q is %p\n", *q); // Value at Address stored in pointer q
    printf("**q is %d\n\n", *(*q)); // Value at address stored in pointer q and value at that address.
    
    printf("r is %p\n", r); // Address of r
    printf("*r is %p\n", *r); // Value of Address stored at pointer r 
    printf("**r is %p\n", *(*r)); // Value at address stored in pointer r and value at that address.
    printf("***r is %d\n\n", *(*(*r))); // Value at address stored in pointer r and value at that address and value of that address too.


    ***r = 10;
    printf("***r = 10; x = %d\n\n", x);

    **q = *p + 2;
    printf("**q = *p + 2; x = %d\n\n", x);

    
    return 0;
}